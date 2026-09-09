P5 = x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x;
{
  my(vl = [157, 163, 179, 197, 211, 223, 241]);
  for(i=1, #vl,
    p = vl[i];
    fp = P5*Mod(1,p);
    cp = hyperellcharpoly(fp);
    print("p=", p, ": cp = ", cp);
  );
}
quit