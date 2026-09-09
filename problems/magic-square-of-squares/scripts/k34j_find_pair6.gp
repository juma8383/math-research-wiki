\\ The pair search over the 2-torsion family y^2 = x^3 + a x^2 + b x, larger bounds.
\\ Pair trace targets (abs): 23:4, 31:8, 47:8, 79:10, 103:10, 151:12, 191:18,
\\ 199:2, 223:26, 239:2, 241:30.
{
  for(a=-1500, 1500,
    for(b=1, 6000,
      if(a*a - 4*b == 0 || b == 0, next);
      E = ellinit([0,a,0,b,0]);
      if(abs(ellap(E,23)) != 4, next);
      if(abs(ellap(E,31)) != 8, next);
      if(abs(ellap(E,47)) != 8, next);
      if(abs(ellap(E,79)) != 10, next);
      if(abs(ellap(E,103)) != 10, next);
      if(abs(ellap(E,151)) != 12, next);
      if(abs(ellap(E,191)) != 18, next);
      if(abs(ellap(E,199)) != 2, next);
      if(abs(ellap(E,223)) != 26, next);
      if(abs(ellap(E,239)) != 2, next);
      if(abs(ellap(E,241)) != 30, next);
      print("PAIR-MATCH: a=", a, " b=", b,
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199), " 223:", ellap(E,223),
            " 239:", ellap(E,239), " 241:", ellap(E,241));
    );
  );
}
quit