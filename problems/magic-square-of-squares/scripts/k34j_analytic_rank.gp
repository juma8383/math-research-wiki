\\ bad primes: 2, 3, 7, 17, AND 271 (singular at 271 — 271 | disc(P)).
\\ disc(x*N(x)) = disc(N)*0-branch... 271 appeared in J_L's conductor; include it.
P5 = x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x;
S = 0.0;
{
  forprime(p=5, 5000,
    if(p == 2 || p == 3 || p == 7 || p == 17 || p == 271, next);
    fp = P5*Mod(1,p);
    cp = hyperellcharpoly(fp);
    a1 = -polcoeff(cp, 3);
    S = S + a1/p*1.0;
    if(p % 500 < 5, print("p=", p, "  sum = ", S));
  );
}
print("FINAL sum a_p/p up to 5000: ", S);
quit