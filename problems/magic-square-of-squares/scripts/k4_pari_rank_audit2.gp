\\ Part 2: E_s model + point checks + Klein-four Jacobian decomposition check.
\\ Sign quotient: s = x^2 (automorphism x -> -x of C4), quotient curve
\\   Z^2 = s^4 - 252 s^3 + 518 s^2 - 252 s + 1   (genus 1).
Et = ellinit([0,32,0,240,0]);
Jt = ellinit([0,512,0,61440,0]);
print("2*(4,504) on J_t model: ", ellmul(Jt, [4,504], 2));
print("2*(1/4,63/8) on E_t:    ", ellmul(Et, [1/4,63/8], 2));
print("== E_s from binary quartic ==");
f = y^2 - (x^4 - 252*x^3 + 518*x^2 - 252*x + 1);
Es = ellfromeqn(f);
print("E_s Weierstrass: ", Es);
Esc = ellinit(Es);
print("E_s rank (2-descent): ", ellrank(Esc));
print("E_s torsion: ", elltors(Esc));
print("== Klein-four decomposition: C4 charpoly =?= product of 3 quotient charpolys ==");
C4 = x^8 - 252*x^6 + 518*x^4 - 252*x^2 + 1;
g1 = x^4 - 252*x^3 + 518*x^2 - 252*x + 1;  \\ sign quotient
g2 = x^4 - 256*x^2 + 1024;                 \\ reciprocal quotient (t = x+1/x)
g3 = x^4 - 248*x^2 + 16;                   \\ negative-reciprocal quotient (u = x-1/x)
forprime(p = 3, 60,
  cp4 = hyperellcharpoly(C4*Mod(1,p));
  q1  = hyperellcharpoly(g1*Mod(1,p));
  q2  = hyperellcharpoly(g2*Mod(1,p));
  q3  = hyperellcharpoly(g3*Mod(1,p));
  print(p, ": match = ", cp4 == q1*q2*q3)
);
quit