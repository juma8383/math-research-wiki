\\ cpJ is a polynomial in the main variable x — but cpZ/cpP are also in x;
\\ conflict: use polynomials directly, print trace coefficients only.
fD = x^8 - 4*x^6 - 604*x^4 - 952*x^2 + 56644;
JL = ellinit([0,0,0,-27894240,56491485696]);
{
  forprime(p=23, 60,
    if(p == 17, next);
    fp = fD*Mod(1,p);
    cpZ = hyperellcharpoly(fp);
    tZ = -polcoeff(cpZ, 5);
    tJ = ellap(JL, p);
    fpP = (x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x)*Mod(1,p);
    cpP = hyperellcharpoly(fpP);
    tP = -polcoeff(cpP, 3);
    print("p=", p, ": tZ=", tZ, " tJ=", tJ, " tP=", tP, " tJ+tP=", tJ+tP);
  );
}
quit