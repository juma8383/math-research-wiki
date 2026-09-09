\\ Compute Jac(P)'s charpoly at primes 31, 53, 59, 61, 67, 71 and compare with
\\ E_a's ap (and E_b's) at the same primes.
P5 = x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x;
Ea = ellinit([0,0,0,-78,396]);
Eb = ellinit([0,0,0,377,400]);
{
  forprime(p=31, 200,
    if(p == 17, next);
    fp = P5*Mod(1,p);
    cpP = hyperellcharpoly(fp);
    apEa = ellap(Ea,p);
    apEb = ellap(Eb,p);
    print("p=", p, ": cpP=", cpP, "  apEa=", apEa, " apEb=", apEb);
  );
}
quit