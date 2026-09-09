\\ Test: is Jac(P) actually Res_{K/Q}(E_K)? A Res surface's charpoly at a SPLIT
\\ prime p = charpoly_E(p) * charpoly_{E^sigma}(p); at an INERT prime p it is
\\ the F_{p^2} Weierstrass polynomial of E. Check consistency of E_a as E/K's
\\ factor at more primes, and check the two candidates' 2-isogeny class.
Ea = ellinit([0,0,0,-78,396]);
Eb = ellinit([0,0,0,377,400]);
print("Ea: cond=", ellglobalred(Ea)[1], " = ", factor(ellglobalred(Ea)[1]));
print("Eb: cond=", ellglobalred(Eb)[1], " = ", factor(ellglobalred(Eb)[1]));
print("torsion Ea: ", elltors(Ea), "  Eb: ", elltors(Eb));
print("Ea rank: ", ellrank(Ea));
print("Eb rank: ", ellrank(Eb));
\\ Ea traces vs Jac(P) traces at more primes (31, 53, 59, 61, 67, 71):
for(p=[31, 53, 59, 61, 67, 71], print("p=", p, ": apEa=", ellap(Ea,p), " apEb=", ellap(Eb,p)));
quit