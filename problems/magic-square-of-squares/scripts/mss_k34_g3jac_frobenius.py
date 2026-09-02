#!/usr/bin/env python
# [mss-k34-g3jac] Part 1: Frobenius decomposition of J(C3_A), J(C3_B).
#
# C3_A: W^2 = x^8 + 132x^6 - 250x^4 + 132x^2 + 1   (genus 3)
# C3_B: W^2 = 9x^8 - 92x^6 + 310x^4 - 92x^2 + 9    (genus 3)
# x -> -x quotients each onto M_A ~ E_A (rank 1), resp. M_B ~ E_B (rank 1),
# so J(C3) ~ E x P with P the Prym (dim 2).  For good primes p we count
# #C3(F_p), #C3(F_p^2), #C3(F_p^3) at small p to recover the FULL degree-6
# Frobenius polynomial P_p(T) via Newton's identities, then:
#   (a) check P_p(T) = P_{E,p}(T) * Q_p(T) exactly (integer division),
#   (b) factor Q_p over Z into two elliptic charpolys and match against
#       E_A, E'_A, E_B, E'_B traces,
#   (c) verify the predicted #C3(F_p) = p+1-(t_E+t_1+t_2) at MANY primes.
#
# Everything is exact integer/F_p arithmetic.  ASCII output only.
import sys
import numpy as np

def out(*a):
    print(*a)
    sys.stdout.flush()

# ---------------------------------------------------------------- curves ---
C3 = {
    "A": [1, 0, 132, 0, -250, 0, 132, 0, 1],      # x^8..x^0, ascending below
    "B": [9, 0, -92, 0, 310, 0, -92, 0, 9],
}
# Weierstrass cubics y^2 = x^3 + a2 x^2 + a4 x (+a6); store (a2, a4, a6)
EC = {
    "E_A":  (-250, 17420, 35848),
    "EB_t": (256, -18432, 0),      # E~_A  (isomorphic to E_A)
    "EP_A": (512, -8192, 0),       # E'_A  (2-isogeny dual of E~_A)
    "E_B":  (310, 8140, 51912),
    "EBt":  (-256, -2048, 0),      # E~_B  (isomorphic to E_B)
    "EP_B": (-512, 73728, 0),      # E'_B  (2-isogeny dual of E~_B)
}

# ----------------------------------------------------------- point counts --
def legendre_count_poly(coeffs, p):
    """#C3(F_p) for W^2 = f(x), f given ascending, deg 8.
    2 points at infinity iff leading coeff is a QR (checked)."""
    lead = coeffs[-1] % p
    li = pow(lead, (p - 1) // 2, p)
    assert li == 1, "leading coeff not a QR mod %d" % p
    n = 0
    for x in range(p):
        v = 0
        for c in reversed(coeffs):
            v = (v * x + c) % p
        if v == 0:
            n += 1          # W=0: one point
        else:
            l = pow(v, (p - 1) // 2, p)
            if l == 1:
                n += 2
    return n + 2

def count_cubic(a2, a4, a6, p):
    """#E(F_p) for y^2 = x^3 + a2 x^2 + a4 x + a6."""
    n = 1  # infinity
    for x in range(p):
        v = (x * x * x + a2 * x * x + a4 * x + a6) % p
        if v == 0:
            n += 1
        else:
            if pow(v, (p - 1) // 2, p) == 1:
                n += 2
    return n

# ------------------------------------------------- F_p^k batched counting --
def find_irrel(p, k):
    """monic irreducible h = u^k + h_{k-1}u^{k-1}+...+h_0 over F_p (k=2,3:
    irreducible iff no root).  Returns rel[] with u^k = sum rel[j] u^j."""
    for h0 in range(p):
        for h1 in range(p):
            if k == 2:
                if all((a * a + h1 * a + h0) % p for a in range(p)):
                    return [(-h0) % p, (-h1) % p]
            else:
                for h2 in range(p):
                    if all((a ** 3 + h2 * a * a + h1 * a + h0) % p
                           for a in range(p)):
                        return [(-h0) % p, (-h1) % p, (-h2) % p]
    raise RuntimeError

def batch_mul(A, B, p, k, rel):
    """elementwise product in F_{p^k}; A,B (N,k) int64 coeff arrays."""
    N = A.shape[0]
    C = np.zeros((N, 2 * k - 1), dtype=np.int64)
    for i in range(k):
        for j in range(k):
            C[:, i + j] = (C[:, i + j] + A[:, i] * B[:, j]) % p
    for m in range(2 * k - 2, k - 1, -1):
        cm = C[:, m].copy()
        if cm.any():
            for j in range(k):
                C[:, m - k + j] = (C[:, m - k + j] + cm * rel[j]) % p
    return C[:, :k]

def count_fk(coeffs, p, k):
    """#C3(F_{p^k}) for W^2 = f(x), f ascending.  Uses norm-square test:
    v in F_{p^k} is a square (or 0) iff v^((p^k-1)/(p-1)) lies in F_p and is
    a QR (or 0) there."""
    N = p ** k
    idx = np.arange(N, dtype=np.int64)
    E = np.zeros((N, k), dtype=np.int64)
    tmp = idx.copy()
    for j in range(k):
        E[:, j] = tmp % p
        tmp //= p
    rel = np.array(find_irrel(p, k), dtype=np.int64)
    res = np.zeros((N, k), dtype=np.int64)
    res[:, 0] = coeffs[-1] % p
    for c in coeffs[-2::-1]:
        res = batch_mul(res, E, p, k, rel)
        res[:, 0] = (res[:, 0] + c) % p
    # norm = v^e, e = (p^k-1)/(p-1)
    e = (p ** k - 1) // (p - 1)
    acc = np.zeros((N, k), dtype=np.int64)
    acc[:, 0] = 1
    base = res % p
    while e:
        if e & 1:
            acc = batch_mul(acc, base, p, k, rel)
        e >>= 1
        if e:
            base = batch_mul(base, base, p, k, rel)
    assert acc[:, 1:].max() == 0, "norm not in F_p"
    nv = acc[:, 0]
    nzero = int((nv == 0).sum())
    qrs = np.array(sorted({(a * a) % p for a in range(p) if a}), dtype=np.int64)
    nqr = int(np.isin(nv[nv != 0], qrs).sum())
    return 2 * nqr + nzero + 2

# --------------------------------------------------- Frobenius extraction --
def frob_poly(N1, N2, N3, p):
    """degree-6 Frobenius charpoly [1, -e1, e2, -e3, p*e2, -p^2*e1, p^3]
    (ascending).  Returns None if Newton identities fail."""
    s1 = p + 1 - N1
    s2 = p * p + 1 - N2
    s3 = p ** 3 + 1 - N3
    e1 = s1
    num = s1 * s1 - s2
    if num % 2:
        return None
    e2 = num // 2
    num3 = s3 - e1 * s2 + e2 * s1
    if num3 % 3:
        return None
    e3 = num3 // 3
    # Weil bounds (g=3): |e1|<=6 sqrt(p), e2<=15p, |e3|<=20 p^1.5
    if abs(e1) > 6 * np.sqrt(p) + 1e-9 or abs(e2) > 15 * p or \
       abs(e3) > 20 * p ** 1.5 + 1e-9:
        return None
    return [1, -e1, e2, -e3, p * e2, -p * p * e1, p ** 3]

def polydiv(num_asc, den_asc):
    """Exact division of integer polys given ASCENDING (lead coeffs may
    exceed 1).  Returns ascending quotient or None."""
    num = list(num_asc)
    den = list(den_asc)
    while den and den[-1] == 0:
        den.pop()
    dn, dd = len(num) - 1, len(den) - 1
    if dd < 0 or dn < dd:
        return None
    lead = den[dd]
    q = [0] * (dn - dd + 1)
    for i in range(dn - dd, -1, -1):
        c = num[i + dd]
        if c % lead:
            return None
        q[i] = c // lead
        if q[i]:
            for j in range(dd + 1):
                num[i + j] -= q[i] * den[j]
    if any(num):
        return None
    return q

def split_quartic(q):
    """Q(T)=T^4+b1T^3+b2T^2+b3T+b4 abelian-surface L-poly (ascending list).
    Try Q=(T^2-t1T+p)(T^2-t2T+p); return sorted [t1,t2] or None."""
    # ascending q = [1, b1, b2, b3, b4]
    b1, b2, b3, b4 = q[1], q[2], q[3], q[4]
    p = b4  # = p^2 -> p = isqrt
    pp = int(round(np.sqrt(b4)))
    if pp * pp != b4 or b3 != pp * b1:
        return ("not-as", b1, b2, b3, b4)
    disc = b1 * b1 - 4 * (b2 - 2 * pp)
    if disc < 0:
        return ("irred-gl2", b1, b2, b3, b4)
    r = int(round(np.sqrt(disc)))
    if r * r != disc or (b1 + r) % 2:
        return ("irred-gl2", b1, b2, b3, b4)
    t1 = (-(b1) + r) // 2
    t2 = (-(b1) - r) // 2
    return ("split", sorted([t1, t2]), pp)

def trace_of(name, p):
    a2, a4, a6 = EC[name]
    return p + 1 - count_cubic(a2, a4, a6, p)

# ------------------------------------------------------------------- main --
def analyze(tag):
    coeffs = C3[tag]
    # bad primes: discriminant of the octic
    import sympy
    x = sympy.symbols("x")
    poly = sum(c * x ** i for i, c in enumerate(coeffs))
    disc = int(sympy.discriminant(poly, x))
    fac = {}
    n = abs(disc)
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    bad = sorted(fac)
    out("=" * 70)
    out("C3_%s: W^2 = %s" % (tag, " + ".join(
        "%d*x^%d" % (c, i) for i, c in enumerate(coeffs) if c)))
    out("disc(octic) sign*bits: %d digits, prime factors: %s"
        % (len(str(abs(disc))), bad))
    out("bad primes (p | disc, plus 2):", sorted(set(bad) | {2}))

    def isprime(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True
    good = [p for p in range(7, 401) if isprime(p) and p not in fac]
    full_primes = [p for p in good if p <= 31][:10]   # N1,N2,N3 here
    many_primes = [p for p in good if p not in full_primes][:36]
    out("full-frob primes (N1,N2,N3):", full_primes)
    out("N1-check primes (%d):" % len(many_primes), many_primes)

    # ---- full Frobenius polynomial at full_primes
    out("-" * 70)
    quots = []
    for p in full_primes:
        N1 = legendre_count_poly(coeffs, p)
        N2 = count_fk(coeffs, p, 2)
        N3 = count_fk(coeffs, p, 3)
        P6 = frob_poly(N1, N2, N3, p)
        if P6 is None:
            out("p=%3d: N=(%d,%d,%d)  Newton/Weil FAILED" % (p, N1, N2, N3))
            continue
        nJ = sum(P6)  # P6(1) = #J(F_p)
        # divide by E charpoly of the base elliptic curve
        ename = "E_A" if tag == "A" else "E_B"
        tE = p + 1 - count_cubic(*EC[ename], p)
        den = [1, -tE, p]
        Q = polydiv(P6, den)
        if Q is None:
            out("p=%3d: N=(%d,%d,%d) tE=%d  NOT divisible by E_%s charpoly!"
                % (p, N1, N2, N3, tE, tag))
            continue
        res = split_quartic(Q)
        nP = sum(Q)
        out("p=%3d: N1=%6d N2=%8d N3=%8d  #J=%9d #E_%s=%5d #Prym=%6d"
            % (p, N1, N2, N3, nJ, tag, count_cubic(*EC[ename], p), nP))
        out("        Q_p(T) (asc) = %s   split -> %s" % (Q, res))
        quots.append((p, Q, res))
    return bad, full_primes, many_primes, quots

def identify(tag, full_primes, many_primes, quots):
    out("-" * 70)
    ename = "E_A" if tag == "A" else "E_B"
    cands = ["E_A", "EB_t", "EP_A", "E_B", "EBt", "EP_B"]
    cands.remove(ename)
    # match quartic factors at full primes
    scores = {}
    for p, Q, res in quots:
        if not (isinstance(res, tuple) and res[0] == "split"):
            continue
        t1, t2 = res[1]
        tr = {c: trace_of(c, p) for c in cands}
        for c1 in cands:
            for c2 in cands:
                if sorted([tr[c1], tr[c2]]) == [t1, t2]:
                    key = tuple(sorted([c1, c2]))
                    scores[key] = scores.get(key, 0) + 1
    out("quartic-factor candidate matches over full primes:")
    for k, v in sorted(scores.items(), key=lambda kv: -kv[1]):
        out("   %s : %d primes" % (str(k), v))
    if not scores:
        out("   NO elliptic-pair match; Prym looks like a simple/gl2 surface")
        best = None
    else:
        best = max(scores, key=scores.get)
        out("   BEST: P ~ %s x %s" % best)
    # verify predicted N1 at many primes (and N2 where available)
    if best:
        ok = 0
        bad = 0
        for p in many_primes:
            pred = p + 1 - (trace_of(ename, p) + trace_of(best[0], p)
                            + trace_of(best[1], p))
            act = legendre_count_poly(C3[tag], p)
            if pred == act:
                ok += 1
            else:
                bad += 1
                if bad <= 5:
                    out("   MISMATCH p=%d pred=%d act=%d" % (p, pred, act))
        out("   predicted #C3_%s(F_p) = p+1-(t_%s+t_%s+t_%s): %d/%d primes OK"
            % (tag, ename, best[0], best[1], ok, ok + bad))
        # also re-verify full frob prediction N2,N3 at full primes
        for p in full_primes:
            tr = [trace_of(c, p) for c in (ename,) + best]
            # charpoly roots: combine three quadratics
            # e-poly of product: multiply L-polys (1 - t T + p T^2) each
            L = [1]
            for t in tr:
                L = np.convolve(L, [1, -t, p]).tolist()
            s1 = -L[1]
            s2 = -L[2] + 0  # L[2] = e2 of degree6? careful: L=prod(1-aT):
            # L[1] = -s1, L[2] = e2, L[3] = -e3
            e1v, e2v, e3v = -L[1], L[2], -L[3]
            s2 = s1 * s1 - 2 * e2v
            s3 = e1v * s2 - e2v * s1 + 3 * e3v
            N1p, N2p, N3p = p + 1 - s1, p * p + 1 - s2, p ** 3 + 1 - s3
            a1 = legendre_count_poly(C3[tag], p)
            a2 = count_fk(C3[tag], p, 2)
            a3 = count_fk(C3[tag], p, 3)
            out("   p=%3d full check N:(%d,%d,%d) pred:(%d,%d,%d) %s"
                % (p, a1, a2, a3, N1p, N2p, N3p,
                   "OK" if (a1, a2, a3) == (N1p, N2p, N3p) else "MISMATCH"))
    return best

out("Frobenius decomposition of J(C3_A), J(C3_B)  [mss-k34-g3jac]")
resA = analyze("A")
bestA = identify("A", *resA[1:])
resB = analyze("B")
bestB = identify("B", *resB[1:])
out("=" * 70)
out("SUMMARY")
out("  C3_A: Prym candidates -> %s" % (bestA,))
out("  C3_B: Prym candidates -> %s" % (bestB,))