\\ direct checks at p=271
P5 = x^5 - 4*x^4 - 604*x^3 - 952*x^2 + 56644*x;
fp = P5*Mod(1,271);
g = gcd(fp, derivative(fp));
print("gcd(fp, fp') mod 271 = ", g, "  degree ", poldegree(g));
print("squarefree? ", poldegree(g) == 0);
\\ also try polgcd naming
print("polgcd attempt: ", polgcd(fp, derivative(fp)));
print("hyperellcharpoly: ", hyperellcharpoly(fp));
quit