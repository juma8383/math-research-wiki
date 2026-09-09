\\ The Jac(Z) Frobenius factors as quadratic * quartic (2+1 split? no: deg 6 = 2+4).
\\ p=23: (x^2-4x+23)(x^2+23)(x^2+4x+23): FULLY SPLIT at p=23! traces: 4, 0, -4.
\\ p=19: quadratic x^2+6x+19 (trace -6) + irreducible quartic.
\\ The quartic factor at p=13, 29: degree-4 — an abelian surface factor?
\\ The quadratic factor at p=19: x^2+6x+19: trace -6; p=13: x^2+13 trace 0.
\\ Compare with candidate elliptic curves: E_Z traces at 13: ap=2; at 19: ?; at 23: 0.
\\ quadratic factors: p=13: t=0; p=19: t=-6; p=23: t=4 (x^2-4x+23 => t=4).
\\ E_Z ap: 13: 2; 19: ?; 23: 0. Not matching.
\\ J_L ap: 13: 0; 19: ?; 23: 0. p=13 quadratic t=0 = J_L trace 0 ✓!!
\\ p=23: quadratic factors t=4, 0, -4: J_L ap(23) = 0 ✓ (one factor); the others
\\ 4 and -4: two more elliptic curves with traces ±4 at p=23.
\\ So Jac(Z) might FULLY SPLIT into 3 elliptics: J_L x E2 x E3 where E2+E3 traces
\\ are ±4 at 23, -6+? at 19... but at p=13, 19, 29 the quartic doesn't split over F_p
\\ — that's fine (factors can be irreducible mod p while the curves are defined over Q).
\\ Get more factorizations to pin E2, E3.
forprime(p=31, 200, if(p==17, next); fp = 8*Mod(1,p)*x^8 + 1016*Mod(1,p)*x^4 + Mod(9,p); cp = hyperellcharpoly(fp); fct = factor(cp); if(matsize(fct)[1] >= 3, print("p=", p, ": ", fct)));
quit