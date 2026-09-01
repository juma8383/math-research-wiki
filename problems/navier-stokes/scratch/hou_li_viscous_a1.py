"""
Viscous Hou-Li 1D model regime scan (robust version).
    u_t + 2a psi u_z = 2 u psi_z + nu u_zz
    w_t + 2a psi w_z = (u_z)^2 + nu w_zz
    psi_zz = -w   (periodic, spectral, 2/3-rule dealiasing, fixed dt RK4)
Controls: a<1, nu>0 -> KNOWN blowup (Hou-Wang 2024 regime 3); a=1,nu=0 inviscid.
Test: a=1, nu>0 -> OPEN. Data u=w=A sin x (=> psi=A sin x).
"""
import numpy as np

def run(a, nu, A, N=512, dt=1e-4, T=1.0, thresh=1e4, verbose=False):
    x = 2*np.pi*np.arange(N)/N
    k = np.fft.fftfreq(N)*N
    de = np.ones(N); de[(3*N)//6 > np.abs(k)] = 1.0
    # 2/3 rule: zero modes |k| > N/3
    keep = np.abs(k) <= N/3
    def d(f):
        fh = np.fft.fft(f); fh[~keep] = 0
        return np.real(np.fft.ifft(1j*k*fh))
    def lap(f):
        fh = np.fft.fft(f); fh[~keep] = 0
        return np.real(np.fft.ifft(-k**2*fh))
    def psi_of_w(w):
        wh = np.fft.fft(w); wh[~keep] = 0
        ph = np.zeros(N, dtype=complex); nz = keep & (k != 0)
        ph[nz] = wh[nz]/k[nz]**2
        return np.real(np.fft.ifft(ph))
    u = A*np.sin(x); w = A*np.sin(x)
    maxw0 = max(np.max(np.abs(w)), 1e-30)
    nsteps = int(T/dt)
    t = 0.0
    hist = []
    for s in range(nsteps):
        mw = np.max(np.abs(w))
        if not np.isfinite(mw):
            return dict(a=a,nu=nu,A=A,blowup=True,t=t,maxw=float('inf'),hist=hist,note='NaN')
        if mw > thresh:
            return dict(a=a,nu=nu,A=A,blowup=True,t=t,maxw=mw,hist=hist,note='threshold')
        def rhs(u,w):
            p = psi_of_w(w)
            return (-2*a*p*d(u) + 2*u*d(p) + nu*lap(u),
                    -2*a*p*d(w) + d(u)**2 + nu*lap(w))
        k1u,k1w = rhs(u,w)
        k2u,k2w = rhs(u+0.5*dt*k1u, w+0.5*dt*k1w)
        k3u,k3w = rhs(u+0.5*dt*k2u, w+0.5*dt*k2w)
        k4u,k4w = rhs(u+dt*k3u, w+dt*k3w)
        u = u + dt*(k1u+2*k2u+2*k3u+k4u)/6
        w = w + dt*(k1w+2*k2w+2*k3w+k4w)/6
        t += dt
        if s % 500 == 0:
            hist.append((t, np.max(np.abs(w))))
    mw = np.max(np.abs(w))
    return dict(a=a,nu=nu,A=A,blowup=(not np.isfinite(mw)) or mw>thresh, t=t,
                maxw=mw if np.isfinite(mw) else -1.0, hist=hist, note='end')

if __name__ == "__main__":
    cases = [
        (0.75, 0.01, 6.0, "CONTROL known blowup regime (a<1, nu>0)"),
        (1.00, 0.01, 6.0, "TEST open regime (a=1, nu>0)"),
        (1.00, 0.00, 6.0, "inviscid full advection"),
        (0.50, 0.01, 6.0, "CONTROL a=0.5"),
        (1.00, 0.10, 6.0, "TEST a=1 stronger viscosity"),
    ]
    for a,nu,A,label in cases:
        r = run(a,nu,A,T=1.0)
        print(f"a={a:.2f} nu={nu:.2f} A={A}: [{label}] blowup={r['blowup']} "
              f"t={r['t']:.4f} max|w|={r['maxw']:.4e} ({r['note']})")
        if r['hist']:
            hs = " ".join(f"({tt:.3f},{mm:.2e})" for tt,mm in r['hist'][::max(1,len(r['hist'])//6)])
            print("   hist:", hs)