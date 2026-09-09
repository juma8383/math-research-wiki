\\ Find E1: y^2 = x^3+A x+B with ap(23)=-4, ap(29)=0, ap(37)=-10, ap(41)=-6, ap(43)=0, ap(47)=0.
\\ and E2: ap(23)=-4, ap(29)=-2, ap(37)=+10, ap(41)=-6, ap(43)=-4, ap(47)=-4.
\\ Wide search in the (A,B) box, first 4 primes as filter.
{
  for(A=-500, 500,
    for(B=-500, 500,
      if(4*A^3 + 27*B^2 == 0, next);
      E = ellinit([0,0,0,A,B]);
      if(ellap(E,23) != -4, next);
      if(ellap(E,29) != 0 && ellap(E,29) != -2, next);
      if(abs(ellap(E,37)) != 10, next);
      if(ellap(E,41) != -6, next);
      if(abs(ellap(E,43)) != 4 && ellap(E,43) != 0, next);
      if(abs(ellap(E,47)) != 4 && ellap(E,47) != 0, next);
      print("FACTOR-CANDIDATE: A=", A, " B=", B,
            " ap: 23:", ellap(E,23), " 29:", ellap(E,29), " 31:", ellap(E,31),
            " 37:", ellap(E,37), " 41:", ellap(E,41), " 43:", ellap(E,43),
            " 47:", ellap(E,47), " cond=", ellglobalred(E)[1], " j=", E.j);
    );
  );
}
quit