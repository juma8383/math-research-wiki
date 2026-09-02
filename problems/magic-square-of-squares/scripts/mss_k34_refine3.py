#!/usr/bin/env python
# K34 refine3: Shipsey-style EDS engine -- W_n = psi_n(x_G) mod p^K in
# O(log n) steps -- plus the first full depth census b_q = v_q(W_{ord_q(G)})
# for (E~_A, G_A) and (E~_B, G_B).  Empirical basis for the odd-depth
# primitive-divisor gate (notes.md sec 2e).
#
# Engine: master EDS identity
#   W_{m+n} W_{m-n} = W_{m+1} W_{m-1} W_n^2 - W_{n+1} W_{n-1} W_m^2
# with W_1 = 1, W_0 = 0, W_{-n} = -W_n, W_2 = 2 y_G.
# Maintain the 7-window (W_{n-3} .. W_{n+3}) at the current binary prefix n;
# doubling (n -> 2n) uses only division by W_2 (a power of 2, invertible for
# p >= 5); the add step extends the window right by one (valuation-tracked
# division).  All values are (valuation, unit mod p^PREC) pairs.
import sys, time
from fractions import Fraction as F
def out(*a): print(*a); sys.stdout.flush()

# ---------- exact reference W_n (bootstrap from exact x(nG)) ----------
def exact_W(A2, A4, G, NMAX):
    from fractions import Fraction as Fr
    G = ((Fr(G[0]), Fr(G[1])))
    def add(P, Q):
        if P is None: return Q
        if Q is None: return P
        x1,y1 = P; x2,y2 = Q
        if x1 == x2 and y1 == -y2: return None
        lam = (y2-y1)/(x2-x1) if P != Q else (3*x1*x1+2*A2*x1+A4)/(2*y1)
        x3 = lam*lam - A2 - x1 - x2
        return (x3, -(y1 + lam*(x3-x1)))
    def mul(P, n):
        R = None; Q = P
        while n:
            if n & 1: R = add(R, Q)
            Q = add(Q, Q); n >>= 1
        return R
    xG, yG = G
    W = {0: 0, 1: 1, 2: int(2*yG)}
    for n in range(2, NMAX):
        # x(nG) = xG - W_{n-1} W_{n+1} / W_n^2
        val = (xG - mul(G, n)[0]) * W[n]**2 / W[n-1]
        assert val.denominator == 1, (n, val)
        W[n+1] = int(val)
    # identity cross-checks (independent of the bootstrap route)
    assert W[5] == W[4]*W[2]**3 - W[3]**3
    assert W[6]*W[2] == W[5]*W[3]*W[2]**2 - W[3]*W[4]**2
    return W

# ---------- valuation-tracked arithmetic mod p^PREC ----------
def make_ops(p, PREC):
    P2 = p**PREC
    Z = (PREC, 0)                       # canonical zero
    def norm(v, u):
        u %= P2
        while u and u % p == 0 and v < PREC:
            u //= p; v += 1
        return Z if (u == 0 or v >= PREC) else (v, u)
    def add(x, y):
        xv, xu = x; yv, yu = y
        if xv >= PREC: return y
        if yv >= PREC: return x
        if xv == yv: return norm(xv, xu + yu)
        if xv > yv: x, y = y, x; xv, yv = yv, xv
        gap = yv - xv
        if gap >= PREC: return x
        return norm(xv, xu + pow(p, gap, P2) * yu)
    def sub(x, y): return add(x, (y[0], (-y[1]) % P2))
    def mul(x, y):
        if x[0] + y[0] >= PREC: return Z
        return norm(x[0] + y[0], x[1] * y[1])
    def div(x, y):
        assert x[0] >= y[0], "negative valuation"
        if x[0] >= PREC: return Z
        return norm(x[0] - y[0], x[1] * pow(y[1], -1, P2))
    return norm, add, sub, mul, div, Z

# ---------- window steps ----------
def win_double(w, W2, W3, add, sub, mul, div):
    # w = (W_{n-3},...,W_{n+3}) -> (W_{2n-3},...,W_{2n+3}); divisions: /W_2 only
    Wm3, Wm2, Wm1, Wn, Wp1, Wp2, Wp3 = w
    W2sq = mul(W2, W2)
    r0 = sub(mul(Wn, mul(Wm2, mul(Wm2, Wm2))),
             mul(Wm3, mul(Wm1, mul(Wm1, Wm1))))
    r1 = div(sub(mul(mul(Wp1, Wm1), mul(Wm2, Wm2)),
                 mul(mul(Wm1, Wm3), mul(Wn, Wn))), W2)
    r2 = sub(mul(Wp1, mul(Wm1, mul(Wm1, Wm1))),
             mul(Wm2, mul(Wn, mul(Wn, Wn))))
    r3 = div(mul(Wn, sub(mul(Wp2, mul(Wm1, Wm1)), mul(Wm2, mul(Wp1, Wp1)))), W2)
    r4 = sub(mul(Wp2, mul(Wn, mul(Wn, Wn))),
             mul(Wm1, mul(Wp1, mul(Wp1, Wp1))))
    r5 = div(sub(mul(mul(Wp3, Wp1), mul(Wn, Wn)),
                 mul(mul(Wp1, Wm1), mul(Wp2, Wp2))), W2)
    r6 = sub(mul(Wp3, mul(Wp1, mul(Wp1, Wp1))),
             mul(Wn, mul(Wp2, mul(Wp2, Wp2))))
    return [r0, r1, r2, r3, r4, r5, r6]

def win_extend(w, W2, W3, add, sub, mul, div):
    # (W_{m-3}..W_{m+3}) -> append W_{m+4}:
    # W_{m+4} W_m = W_{m+3} W_{m+1} W_2^2 - W_3 W_{m+2}^2   [(m+2, 2)]
    val = sub(mul(mul(w[6], w[4]), mul(W2, W2)), mul(W3, mul(w[5], w[5])))
    return div(val, w[3])

def engine_W(A2, A4, G, Wex, N, p, PREC):
    norm, add, sub, mul, div, Z = make_ops(p, PREC)
    W2 = norm(0, 2*G[1] % p**PREC)
    W3 = norm(0, Wex[3] % p**PREC)
    # initial window at n=1: indices -2..4
    w = [norm(0, (-Wex[2]) % p**PREC),
         norm(0, (-Wex[1]) % p**PREC),
         Z,
         norm(0, 1),
         norm(0, Wex[2] % p**PREC),
         norm(0, Wex[3] % p**PREC),
         norm(0, Wex[4] % p**PREC)]
    n = 1
    for bit in bin(N)[3:]:
        w = win_double(w, W2, W3, add, sub, mul, div)
        n *= 2
        if bit == '1':
            w = w[1:] + [win_extend(w, W2, W3, add, sub, mul, div)]
            n += 1
    return w[3]

def vp_of_W(A2, A4, G, Wex, N, p, PREC=8):
    """v_p(W_N) up to PREC-1, or None if engine failed (precision)."""
    try:
        v, u = engine_W(A2, A4, G, Wex, N, p, PREC)
        return PREC if v >= PREC else v
    except AssertionError:
        return None

# ---------- group order / ord_p(G) mod p ----------
def count_E(A2, A4, p):
    cnt = 1
    qrs = set(t*t % p for t in range(1, p))
    for x in range(p):
        v = (x*x*x + A2*x*x + A4*x) % p
        if v == 0: cnt += 1
        elif v in qrs: cnt += 2
    return cnt

def ec_add_mod(P, Q, p, A2, A4):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None
    if P == Q:
        if y1 % p == 0: return None
        lam = (3*x1*x1 + 2*A2*x1 + A4) * pow(2*y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam*lam - A2 - x1 - x2) % p
    return (x3, (-(y1 + lam*(x3 - x1))) % p)

def ec_mul_mod(P, n, p, A2, A4):
    R = None; Q = (P[0] % p, P[1] % p)
    while n:
        if n & 1: R = ec_add_mod(R, Q, p, A2, A4)
        Q = ec_add_mod(Q, Q, p, A2, A4)
        n >>= 1
    return R

def ord_of_G(G, p, A2, A4):
    N = count_E(A2, A4, p)
    fs = {}; m = N; dd = 2
    while dd*dd <= m:
        while m % dd == 0: fs[dd] = fs.get(dd,0)+1; m //= dd
        dd += 1 if dd == 2 else 2
    if m > 1: fs[m] = fs.get(m,0)+1
    o = N
    for f in sorted(fs):
        for _ in range(fs[f]):
            if ec_mul_mod(G, o//f, p, A2, A4) is None: o //= f
            else: break
    return o

def primes_upto(B):
    sieve = bytearray([1])*(B+1); sieve[0:2] = b'\x00\x00'
    for i in range(2, int(B**0.5)+1):
        if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(B+1) if sieve[i]]

# ================= main =================
if __name__ == "__main__":
    t00 = time.time()
    curves = {
      "A": ({"A2": -256, "A4": 18432, "G": (128, 512)}),
      "B": ({"A2": 256, "A4": -2048, "G": (-128, 1536)}),
    }
    BMAX = 20000
    for tag, c in curves.items():
        A2, A4, G = c["A2"], c["A4"], c["G"]
        Wex = exact_W(A2, A4, G, 60)
        out("=== curve %s: W_2=%d W_3=%d (identity checks passed) ===" % (tag, Wex[2], Wex[3]))
        # 1) engine validation vs exact W_n
        ps = primes_upto(2000)[::37][:25]
        bad = 0; tested = 0
        for p in ps:
            P2 = p**8
            for N in list(range(2, 40)) + [47, 53, 59, 60]:
                gotv = engine_W(A2, A4, G, Wex, N, p, 8)
                exact_res = Wex[N] % P2
                if gotv[0] >= 8:
                    ok = (exact_res == 0)
                else:
                    ok = ((pow(p, gotv[0], P2) * gotv[1]) % P2 == exact_res)
                tested += 1
                if not ok:
                    bad += 1
                    out("  MISMATCH p=%d N=%d" % (p, N))
        out("  engine vs exact: %d checks, %d failures" % (tested, bad))
        # 2) depth census b_q for all primes q <= BMAX
        hist = {}; wie = []; nrows = 0
        t0 = time.time()
        for p in primes_upto(BMAX)[2:]:        # skip 2,3 (bad reduction)
            o = ord_of_G(G, p, A2, A4)
            b = vp_of_W(A2, A4, G, Wex, o, p)
            if b is None:
                out("  PRECISION FAIL p=%d ord=%d" % (p, o)); continue
            nrows += 1
            hist[b] = hist.get(b, 0) + 1
            if b % 2 == 0: wie.append((p, o, b))
        out("  census q<=%d (%d primes, %.0fs): depth histogram %s"
            % (BMAX, nrows, time.time()-t0, dict(sorted(hist.items()))))
        out("  odd-Wieferich (even depth) primes: %s" % (wie if wie else "NONE"))
    out("total %.0fs" % (time.time()-t00))