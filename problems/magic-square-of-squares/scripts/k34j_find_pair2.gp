\\ ellinit on singular curves returns a t_VEC of zeros (not an ell); guard by
\\ checking discriminant via poldegree-safe trick: use ellinit and test ellap
\\ inside a try-like construct. gp has no try; test singularity first:
\\ singular iff disc == 0: disc([0,a,0,b,0]) = -16(4b^3 + ... )? a2=a: disc =
\\ 16 b (a^2-4b)^2? For y^2=x^3+ax^2+bx: disc = 16 b^2 (a^2-4b)? Let me compute
\\ the discriminant formula directly and skip singular ones BEFORE ellinit.
{
  for(a=-120, 120,
    for(b=1, 1500,
      disc = 16*b*(a*a - 4*b)*(a*a - 4*b);
      if(disc == 0, next);
      E = ellinit([0,a,0,b,0]);
      if(abs(ellap(E,23)) != 4, next);
      if(abs(ellap(E,31)) != 8, next);
      if(abs(ellap(E,47)) != 8, next);
      if(abs(ellap(E,79)) != 10, next);
      if(abs(ellap(E,103)) != 10, next);
      if(abs(ellap(E,151)) != 12, next);
      if(abs(ellap(E,191)) != 18, next);
      if(abs(ellap(E,199)) != 2, next);
      print("MATCH: a=", a, " b=", b,
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199));
    );
  );
}
quit