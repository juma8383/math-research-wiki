\\ L(s) evaluation with proper stack and bad-prime exclusions.
\\ Evaluate L(s) = prod L_p(s) at s = 1.5, 1.25, 1.125, 1.0625, 1.03125
\\ (converging to 1 from above): if L(s) stays well above 0 with no sign
\\ of a zero as s -> 1, analytic rank 0 is supported; a rank-1 zero would
\\ show L(s) ~ c(s-1) -> 0 linearly.
default(parisizemax, 8000000000);
P5 = x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x;
bad = [2, 3, 7, 17, 271];
{
  for(sden = 2, 32,
    s = 1.0 + 1.0/sden;
    Ls = 1.0;
    forprime(p=5, 30000,
      if(p == 17 || p == 271, next);
      fp = P5*Mod(1,p);
      cp = hyperellcharpoly(fp);
      T = p^(-s);
      val = 1 + polcoeff(cp,3)*T + polcoeff(cp,2)*T^2 + polcoeff(cp,1)*T^3 + polcoeff(cp,0)*T^4;
      Ls = Ls / val;
    );
    print("s = ", s, ":  L(s) = ", Ls);
  );
}
quit