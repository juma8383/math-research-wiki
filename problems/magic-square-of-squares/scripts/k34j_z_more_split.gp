\\ factor() returns [x^2-t1x+p, 1] rows — the polynomial is fct[1,1] (t_POL);
\\ coefficient of x: polcoeff(fct[1,1],1). trace t = -coeff(x).
f = 8*x^8 + 1016*x^4 + 9;
{
  forprime(p=100, 400,
    if(p == 17, next);
    fp = 8*Mod(1,p)*x^8 + 1016*Mod(1,p)*x^4 + Mod(9,p);
    fct = factor(hyperellcharpoly(fp));
    if(matsize(fct)[1] == 3,
      t1 = -polcoeff(fct[1,1], 1);
      t2 = -polcoeff(fct[2,1], 1);
      t3 = -polcoeff(fct[3,1], 1);
      print("p=", p, ": traces = (", t1, ", ", t2, ", ", t3, ")");
    );
  );
}
quit