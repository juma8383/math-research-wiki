# Twist-assembly numerical grounding.
# Lavrik/Dokchitser: Lambda(s) = sum_n a_n int_1^infty (u^{s-1} + w u^{1-s}) e^{-2 pi n u / sqrt(N)} du
# L(s) = Lambda(s) * (2 pi / sqrt(N))^s / Gamma(s)
# Calibrated on 11a1 (expect L(1)=0.253841860186...), 37a1 (expect L(1)=0, rank 1).
# Then: for E=37a1 and twists by fundamental D<0, (D,2*37)=1, (D/37)=+1 (Heegner hyp),
# find D with rank(E^D)=1: L(E^D,1)=0 and L'(E^D,1) != 0  => rank-2-over-K split 1+1.

import mpmath as mp
import sympy
mp.mp.dps = 25

NB = 1200  # a_n table size (enough for |D| up to ~ 30; extended later if needed)

def count_points_min(a1, a2, a3, a4, a6, p):
    cnt = 1
    for x in range(p):
        b = (a1 * x + a3) % p
        f = (x * x * x + a2 * x * x + a4 * x + a6) % p
        disc = (b * b + 4 * f) % p
        if disc == 0:
            cnt += 1
        else:
            if pow(disc, (p - 1) // 2, p) == 1:
                cnt += 2
    return cnt

def an_table(a1, a2, a3, a4, a6, cond_p, NB):
    """cond_p: the conductor prime (multiplicative reduction, |a_p|=1, geometric powers)."""
    an = {1: 1}
    plist = list(sympy.primerange(2, NB + 1))
    for p in plist:
        ap = p + 1 - count_points_min(a1, a2, a3, a4, a6, p) if p != cond_p else None
        if p == cond_p:
            ap = p + 1 - count_points_min(a1, a2, a3, a4, a6, p)
            assert abs(ap) == 1
        pk = p; prev = 1; cur = ap  # a_{p^0}=1
        while pk <= NB:
            an[pk] = cur
            nxt = (cur * ap if p == cond_p else ap * cur - p * prev)
            prev, cur = cur, nxt
            pk *= p
    for n in range(2, NB + 1):
        if n in an:
            continue
        p, e = list(sympy.factorint(n).items())[0]
        an[n] = an[p ** e] * an[n // p ** e]
    return an

def twist_an(anE, D, NB):
    """naive coefficient twist: a_n(E^D) = chi_D(n) a_n(E)."""
    anT = {1: 1}
    plist = list(sympy.primerange(2, NB + 1))
    for p in plist:
        if D % p == 0:
            ap = 0
        elif p == 2:
            chi = 1 if (D % 8) in (1, 3) else -1  # (2/D) for odd fundamental D
            ap = chi * anE[2]
        else:
            ap = sympy.jacobi_symbol(D, p) * anE[p]
        pk = p; prev = 1; cur = ap  # a_{p^0}=1
        while pk <= NB:
            anT[pk] = cur
            nxt = 0 if D % p == 0 else ap * cur - p * prev
            prev, cur = cur, nxt
            pk *= p
    for n in range(2, NB + 1):
        if n in anT:
            continue
        p, e = list(sympy.factorint(n).items())[0]
        anT[n] = anT[p ** e] * anT[n // p ** e]
    return anT

# ---- 37a1: y^2 + y = x^3 - x, conductor 37
anE = an_table(0, 0, 1, -1, 0, 37, NB)
# ---- 11a1 for calibration: y^2 + y = x^3 - x^2 - 10x - 20, conductor 11
an11 = an_table(0, -1, 1, -10, -20, 11, 400)

def Lval_factory(an, N, w):
    sq = mp.sqrt(N)
    c = 2 * mp.pi / sq
    def Lam(s):
        tot = mp.mpf(0)
        for n in range(1, max(an) + 1):
            a = an[n]
            if a == 0:
                continue
            k = c * n
            if k > 130:
                break
            up = 1 + 130 / k  # e^{-130} < 1e-56
            f = mp.quad(lambda u: (u ** (s - 1) + w * u ** (1 - s)) * mp.e ** (-k * u), [1, up])
            tot += a * f
        return tot
    def L(s):
        return Lam(s) * c ** s / mp.gamma(s)
    return L

# debug: term-by-term Lambda(1) for 11a1
c = 2 * mp.pi / mp.sqrt(11)
dbg = 0
for n in range(1, 12):
    a = an11[n]
    k = c * n
    t = a * 2 * mp.e ** (-k) / k  # exact closed form of the integral at s=1, w=+1
    dbg += t
print("  closed-form sum (n<=11):", mp.nstr(dbg * c, 16))
print("  a_n(11a1) n=1..20:", [an11[n] for n in range(1, 21)])

L11 = Lval_factory(an11, 11, +1)
print("11a1  L(1)  =", mp.nstr(L11(1), 16), " expect 0.2538418601865296")

L37 = Lval_factory(anE, 37, -1)
print("37a1  L(1)  =", mp.nstr(L37(1), 16), " expect 0 (rank 1)")
print("37a1  L'(1) =", mp.nstr(mp.diff(L37, 1), 12))

# ---------------- twist study ----------------
def direct_series_L(an, s, NB):
    """parameter-free L(s) for Re s large enough (s=4): sum a_n/n^s."""
    tot = mp.mpf(0)
    for n in range(1, NB + 1):
        tot += mp.mpf(an[n]) / n ** s
    return tot

def pin_root_number(an, Np, s_test=4, NBseries=None):
    """Decide w' empirically: Lavrik(s=4) with w=+1 vs -1 must reproduce direct series."""
    if NBseries is None:
        NBseries = max(an)
    Ldir = direct_series_L(an, s_test, NBseries)
    lam_direct = (mp.sqrt(Np) / (2 * mp.pi)) ** s_test * mp.gamma(s_test) * Ldir
    sq = mp.sqrt(Np); c = 2 * mp.pi / sq
    res = {}
    for w in (+1, -1):
        tot = mp.mpf(0)
        for n in range(1, max(an) + 1):
            a = an[n]
            if a == 0:
                continue
            k = c * n
            if k > 130:
                break
            up = 1 + 130 / k
            f = mp.quad(lambda u: (u ** (s_test - 1) + w * u ** (1 - s_test)) * mp.e ** (-k * u), [1, up])
            tot += a * f
        res[w] = tot
    dplus = abs(res[1] - lam_direct); dminus = abs(res[-1] - lam_direct)
    wbest = 1 if dplus < dminus else -1
    return wbest, min(dplus, dminus) / abs(lam_direct)

Dlist = [-7, -11, -15, -19, -35, -43, -51, -67, -91, -115, -123, -163, -187, -235, -267, -403]
print()
print(" D      chi(D,37)  N'=37D^2     w'  (rel.err)   L(E^D,1)      L'(E^D,1)     -> rank")
good = []
NBglobal = NB
for D in Dlist:
    if sympy.jacobi_symbol(D, 37) != 1:
        continue  # need 37 split in K (Heegner hypothesis)
    Np = 37 * D * D
    need = int(9.6 * mp.sqrt(Np)) + 10
    if need > NBglobal:
        anE.update(an_table(0, 0, 1, -1, 0, 37, need))
        NBglobal = need
    anT = twist_an(anE, D, need)
    wbest, relerr = pin_root_number(anT, Np, 4)
    LT = Lval_factory(anT, Np, wbest)
    L1 = LT(1)
    L1p = mp.diff(LT, 1)
    rank = "?"
    if wbest == -1:
        rank = 1 if abs(L1p) > 1e-8 else ">=3"
    else:
        rank = 0 if abs(L1) > 1e-6 else "2?"
    print(f"{D:6d}  {int(sympy.jacobi_symbol(D,37)):+9d}  {Np:9d}   {wbest:+2d}  ({mp.nstr(relerr,2)})  {mp.nstr(L1,10):>13}  {mp.nstr(L1p,10):>13}  -> {rank}")
    if wbest == -1 and abs(L1p) > 1e-8:
        good.append(D)
print()
print("rank-1 twists with Heegner hypothesis (D/37)=+1:", good)