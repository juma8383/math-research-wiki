\\ Jac(Z) is NOT J_L x E_Z. The genus-3 octic's Jacobian must decompose
\\ differently. The octic 8w^8+1016w^4+9 is even: w->-w quotient = C1 (quartic).
\\ Jac(Z) ~ Jac(C1) x Prym. Compute the actual Frobenius of Z and try to fit
\\ Jac(Z) ~ J_L x (some elliptic E?) using 3 factors: maybe Jac(Z) ~ E1 x E2 x E3
\\ with traces t_i summing to tZ. Fit: find E1,E2,E3 with t1+t2+t3 = tZ at all p.
\\ J_L is ONE factor (the C1 quotient is genus 1 = Jac(C1) = J_L — verify trace
\\ Jac(C1) = J_L's trace).
C1pts(p) = p + 1 + sum(xx=0, p-1, kronecker(8*xx^4 + 1016*xx^2 + 9, p));
JL = ellinit([0,0,0,-27894240,56491485696]);
ok1 = 0; bad1 = 0;
forprime(p=13, 300, if(p==17 || p==19 || p==271, next); tc = p+1-C1pts(p); if(tc==ellap(JL,p), ok1++, bad1++));
print("C1 trace vs J_L: ok=", ok1, " mismatch=", bad1);
\\ get Z traces list for fitting
forprime(p=13, 60, if(p==17||p==19, next); print("p=",p,": tZ=", p+1-Zpts(p), " tC1=", p+1-C1pts(p), " tJL=", ellap(JL,p)));
quit