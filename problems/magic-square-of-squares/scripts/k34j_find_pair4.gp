\\ Search wider for the pair curve: y^2 = x^3 + A x + B, |A|<=3000, |B|<=3000.
\\ Trace targets (absolute values): 23:4, 31:8, 47:8, 79:10, 103:10, 151:12,
\\ 191:18, 199:2, 223:26, 239:2, 241:30. Use the first 4 as filters, rest as check.
{
  for(A=1, 3000,
    for(B=1, 3000,
      if(4*A^3 + 27*B^2 == 0, next);
      E = ellinit([0,0,0,A,B]);
      if(abs(ellap(E,23)) != 4, next);
      if(abs(ellap(E,31)) != 8, next);
      if(abs(ellap(E,47)) != 8, next);
      if(abs(ellap(E,79)) != 10, next);
      if(abs(ellap(E,103)) != 10, next);
      if(abs(ellap(E,151)) != 12, next);
      if(abs(ellap(E,191)) != 18, next);
      print("MATCH: A=", A, " B=", B,
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199), " 223:", ellap(E,223),
            " 239:", ellap(E,239), " 241:", ellap(E,241));
    );
  );
}
quit