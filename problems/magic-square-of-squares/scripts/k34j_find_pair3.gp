\\ no match in the (a,b) 2-torsion family up to b<=1500. Broaden: also try
\\ a=0 general curves y^2 = x^3+A x+B (no rational 2-torsion) — the Prym factor
\\ need not have rational 2-torsion.
{
  for(A=-300, 300,
    for(B=-300, 300,
      disc = -16*(4*A^3 + 27*B^2);
      if(disc == 0, next);
      E = ellinit([0,0,0,A,B]);
      if(abs(ellap(E,23)) != 4, next);
      if(abs(ellap(E,31)) != 8, next);
      if(abs(ellap(E,47)) != 8, next);
      if(abs(ellap(E,79)) != 10, next);
      if(abs(ellap(E,103)) != 10, next);
      if(abs(ellap(E,151)) != 12, next);
      if(abs(ellap(E,191)) != 18, next);
      if(abs(ellap(E,199)) != 2, next);
      print("MATCH: A=", A, " B=", B,
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199), " j=", E.j, " cond=", ellglobalred(E)[1]);
    );
  );
}
quit