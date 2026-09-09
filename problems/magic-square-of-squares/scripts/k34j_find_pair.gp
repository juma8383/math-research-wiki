\\ Jac(Z) splits into 3 elliptics: J_L (middle trace) + a +-pair of twists.
\\ The +-pair has ap(23)=+-4, ap(31)=+-8, ap(47)=+-8, ap(79)=+-10, ap(151)=+-12,
\\ ap(191)=+-18, ap(199)=+-2. Search small curves y^2=x^3+a*x^2+b*x for these traces.
\\ ap at good p computed by brute force in gp via ellap.
{
  for(a=-80, 80,
    for(b=1, 400,
      E = ellinit([0,a,0,b,0]);
      if(E.disc == 0, next);
      if(ellap(E,23) != 4 && ellap(E,23) != -4, next);
      if(abs(ellap(E,31)) != 8, next);
      if(abs(ellap(E,47)) != 8, next);
      if(abs(ellap(E,79)) != 10, next);
      print("CANDIDATE: a=", a, " b=", b, " cond=", ellglobalred(E)[1],
            " ap: 23:", ellap(E,23), " 31:", ellap(E,31), " 47:", ellap(E,47),
            " 79:", ellap(E,79), " 103:", ellap(E,103), " 151:", ellap(E,151),
            " 191:", ellap(E,191), " 199:", ellap(E,199));
    );
  );
}
quit