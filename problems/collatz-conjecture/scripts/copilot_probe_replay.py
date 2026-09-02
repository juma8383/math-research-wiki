# Independent re-run of the Copilot exponent-word probe (k<=9, A-window +9),
# plus cyclic-normalization lemma checks. ASCII output only.
from itertools import combinations
from math import log2, isqrt

def comps(total,k):
    for cuts in combinations(range(1,total),k-1):
        pts=(0,)+cuts+(total,)
        yield tuple(pts[i+1]-pts[i] for i in range(k))

def candidate(a):
    k=len(a); A=sum(a); pref=0; S=0
    for j,x in enumerate(a):
        S += 3**(k-1-j) * 2**pref
        pref += x
    D=2**A-3**k
    if D<=0 or S%D: return None
    n=S//D
    vals=[n]
    for x in a:
        m=3*vals[-1]+1
        if m%(2**x): return None
        q=m//(2**x)
        if q%2==0: return None
        vals.append(q)
    if vals[-1]!=n: return None
    return n,vals[:-1]

print("k amin tested integers cycles nontrivial")
for k in range(1,10):
    amin=int(k*log2(3))+1
    tested=integers=cycles=0; found=[]
    for A in range(amin,amin+9):
        for a in comps(A,k):
            tested+=1
            pref=0; S=0
            for j,x in enumerate(a):
                S += 3**(k-1-j)*2**pref; pref+=x
            D=2**A-3**k
            if D>0 and S%D==0: integers+=1
            c=candidate(a)
            if c:
                cycles+=1
                n,vals=c
                if set(vals)!={1}: found.append((a,n))
    print(k,amin,tested,integers,cycles,len(found))
    if found: print("  FOUND:",found[:5])

# --- cyclic normalization lemma check ---
# for each composition, rotate so Delta_j = A_j - j*A/k is minimized at j=0;
# then Delta_j >= 0 for all prefixes, so 2^{A_j} >= 2^{jA/k} > 3^j (j>=1),
# giving S > k*3^{k-1}. Verify S > k*3^{k-1} after min-rotation for ALL words.
from fractions import Fraction
bad_norm = 0; bad_bound = 0; nwords = 0
for k in range(2,10):
    amin=int(k*log2(3))+1
    for A in range(amin,amin+9):
        for a in comps(A,k):
            nwords += 1
            Ajs=[]; p=0
            for x in a: Ajs.append(p); p+=x
            best=None; shift=0
            for r in range(k):
                dr = Ajs[(r)%k]
                # Delta at index j of rotation r: A_{r+j} - A_r - j*A/k (cyclic,
                # with A_k = A, A_{k+r} = A + A_r)
                # minimum prefix value: compute partial sums of (a_i - A/k)
                pass
            # direct: partial sums s_i = A_i - i*A/k for i=0..k (s_k = 0 by
            # definition since A - k*A/k = 0). Find argmin over i=0..k-1.
            frA = Fraction(A,k)
            s = [Fraction(Ajs[i]) - i*frA for i in range(k)]
            mn = min(s); idx = s.index(mn)
            rot = a[idx:]+a[:idx]
            # recompute prefix discrepancies for rotated word (cyclically)
            ok = True
            cum = 0
            for j in range(k):
                if cum - j*frA < -Fraction(1,10**9) is not None: pass
                if Fraction(cum) - j*frA < 0: ok=False; break
                cum += rot[j]
            if not ok: bad_norm += 1
            # S for rotated word is the same (cyclic invariance of S? no! S is
            # NOT rotation invariant: S depends on rotation through weights
            # 3^{k-1-j}). Recompute S for the rotated word.
            Scum=0; Srot=0
            for j,x in enumerate(rot):
                Srot += 3**(k-1-j)*2**Scum; Scum += x
            if not (Srot > k*3**(k-1)): bad_bound += 1
print("normalization: words",nwords,"prefix-discrepancy violations",bad_norm,
      "S>k*3^{k-1} violations",bad_bound)
