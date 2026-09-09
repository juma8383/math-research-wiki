\\ Full 11-prime filter search: |ap| must match the +-pair at ALL of
\\ 23,31,47,79,103,151,191,199,223,239,241: (4,8,8,10,10,12,18,2,26,2,30).
\\ Wider: A in [-6000,6000], B in [1,6000]. Prefilter: the first 4 primes.
{
  for(A=1, 6000,
    for(B=1, 6000,
      if(4*A^3 + 27*B^2 == 0, next);
      E = ellinit([0,0,0,A,B]);
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
      print("FULL-MATCH: A=", A, " B=", B,
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199), " 223:", ellap(E,223),
            " 239:", ellap(E,239), " 241:", ellap(E,241));
    );
  );
}
quit