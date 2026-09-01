import math

def dset(w):
    ds = set()
    for m in range(2, int(math.isqrt(w)) + 1):
        mm = m * m
        for n in range(1, m):
            s = mm + n * n
            if s > w:
                break
            if w % s:
                continue
            d0 = 2 * (mm - n * n) * (2 * m * n)
            k = w // s
            ds.add(d0 * k * k)
    return sorted(ds)

for (e, p, k) in [(1, 5, 1), (2, 5, 1), (1, 5, 2), (3, 5, 2), (1, 13, 2), (2, 17, 2), (1, 5, 3)]:
    w = (2 ** e) * (p ** k)
    ds = dset(w)
    dpk = dset(p ** k)
    pred = sorted(2 ** (2 * e) * d for d in dpk)
    print(f"w=2^{e}*{p}^{k}={w}: |D|={len(ds)} match_2^2e_D(p^k)={ds == pred}")
    dset_ = set(ds)
    A2 = any((ds[i] + ds[j]) in dset_ for i in range(len(ds)) for j in range(i + 1, len(ds)))
    print("   A2 hit:", A2)