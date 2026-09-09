\\ C1 trace does NOT match J_L! So my claimed C1-Jacobian J_L is wrong?? The
\\ invariants matched (1033120, -2092277248) for D, C1, C2 — but invariants
\\ determine the Jacobian only up to TWIST. C1 is a TWIST of D's Jacobian!
\\ The Frobenius mismatch says C1's Jacobian is a different twist of J_L.
C1pts(p) = p + 1 + sum(xx=0, p-1, kronecker(8*xx^4 + 1016*xx^2 + 9, p));
JL = ellinit([0,0,0,-27894240,56491485696]);
print("p: tC1 vs tJL:");
forprime(p=13, 47, if(p==17||p==19, next); print("p=",p,": tC1=", p+1-C1pts(p), " tJL=", ellap(JL,p)));
\\ twist structure: C1 = 8x^4+1016x^2+9; D's quartic family has ae=238 (D: a=1,e=56644? no D is not diagonal).
\\ The diagonal covers of J_L^sh: y^2 = d x^4 - 2a2 x^2 + (a2^2-4a4)/d with a2=-18288, a4=83589408:
\\ y^2 = d x^4 + 36456 x^2 + 93312/d. For d=1: x^4+36456x^2+93312. Invariants?
def IJ(a,b,c,d,e) = { my(I=12*a*e-3*b*d+c*c, J=72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c^3); print("I=",I," J=",J); }
IJ(1,0,36456,0,93312);
quit