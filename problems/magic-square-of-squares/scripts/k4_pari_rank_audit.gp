\\ Rank audit for the k=4 multiplier line (Copilot-contribution frontier).
\\ Curves (scaled Jacobians of the Klein-four quotient quartics):
\\   E_u  : y^2 = x^3 + 31x^2 + 240x   (= J_u scaled, x(x+15)(x+16))
\\   E_t  : y^2 = x^3 + 32x^2 + 240x   (= J_t scaled, x(x+12)(x+20))
\\   E_u' : y^2 = x^3 - 62x^2 + x      (2-isogenous to E_u)
\\   E_t' : y^2 = x^3 - 64x^2 + 64x    (2-isogenous to E_t)
\\   E_s  : Jacobian of sign quotient  y^2 = x^4 - 252x^3 + 518x^2 - 252x + 1
\\ Plus: C4 Jacobian charpoly must factor as product of the three quotient charpolys.
Eu  = ellinit([0,31,0,240,0]);
Et  = ellinit([0,32,0,240,0]);
Eup = ellinit([0,-62,0,1,0]);
Etp = ellinit([0,-64,0,64,0]);
print("== ellrank (2-descent) ==");
print("E_u  [0,31,0,240,0]:   ", ellrank(Eu));
print("E_t  [0,32,0,240,0]:   ", ellrank(Et));
print("E_u' [0,-62,0,1,0]:    ", ellrank(Eup));
print("E_t' [0,-64,0,64,0]:   ", ellrank(Etp));
print("== torsion ==");
print("E_u torsion:  ", elltors(Eu));
print("E_t torsion:  ", elltors(Et));
print("E_u' torsion: ", elltors(Eup));
print("E_t' torsion: ", elltors(Etp));
print("== point checks ==");
print("2*(1/4,63/8) on E_t: ", ellmul(Et, [1/4,63/8], 2));
print("(4,504) on J_t model [0,512,0,61440,0], 2P: ",
      ellmul(ellinit([0,512,0,61440,0]), [4,504], 2));
print("== sign quotient: genus-1 quartic -> Weierstrass ==");
Es = ellfromeqn(x^4-252*x^3+518*x^2-252*x+1);
print("E_s ellinit vec: ", Es);
Esc = ellinit(Es);
print("E_s rank: ", ellrank(Esc));
print("E_s torsion: ", elltors(Esc));
print("== C4 (genus 3) Jacobian charpoly must factor into 3 cubics x Z^2 ==");
f = x^8-252*x^6+518*x^4-252*x^2+1;
cp = hyperellcharpoly(f);
print("charpoly: ", cp);
print("factored: ", factor(cp));
quit