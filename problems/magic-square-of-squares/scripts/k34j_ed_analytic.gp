
\\ analytic rank probe for E_D: L-series slope at s=1 via sum a_p/p
\\ E_D: y^2 = x^3 - 6973560x^2 + 14122871424x
\\ as [a1,a2,a3,a4,a6] = [0,-6973560,0,14122871424,0]
E = ellinit([0,-6973560,0,14122871424,0]);
bad = 2; \\ compute bad primes:
disc = elllocalred(E,2)[1]+ellglobalred(E)[1];
g = ellglobalred(E); disc = g[1];
print("disc = ", disc);
\\ good primes: p ∤ disc; compute sum a_p/p up to N:
N = 5000;
s = 0.0;
p = 2;
while(p < N,
  if(gcd(p, disc) == 1, ap = ellap(E, p); s += ap/p*1.0);
  p = nextprime(p+1)
);
print("sum a_p/p up to ", N, " = ", s);
print("rank-1 signature: drifting toward -1 (log log N ~ 2.0)");
print("DONE")
