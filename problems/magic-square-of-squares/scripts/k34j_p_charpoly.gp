\\ multiline loop with proper block braces
{
  forprime(p=23, 60,
    if(p == 17, next);
    fp = (x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x)*Mod(1,p);
    cp = hyperellcharpoly(fp);
    print("p=", p, ": ", factor(cp));
  );
}
quit