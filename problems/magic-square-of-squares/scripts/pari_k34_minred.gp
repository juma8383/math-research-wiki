// pari_k34_minred.gp -- minimal models + conductors of the two K34 sieve
// curves, via PARI's ellminimalmodel + mwrank cross-check (2026-09-03).
// tE_A: y^2 = x^3 - 256x^2 + 18432x  (a1=a3=a6=0)
// tE_B: y^2 = x^3 + 256x^2 - 2048x
\\ ellglobalred returns [u,r,s,t, vs, vr, N, ...]? Probe format first:
EA = ellinit([0,-256,0,18432,0]);
EB = ellinit([0,256,0,-2048,0]);
\\ PARI 2.17: ellglobalred(E) deprecated -> use ellchange? Try ellminimalmodel:
\\ PARI 2.17 has ellglobalred returning [u, r, s, t, N, ...]? Let's probe with
\\ the known curve y^2=x^3-x (32a3): expect conductor 32, disc 64 (min disc -64? minimal disc of 32a3 is 64? Actually -64 for 32a1...)
\\ Probe:
E32 = ellinit([0,0,0,-1,0]);
red32 = ellglobalred(E32);
print("probe32 raw = ", red32);
\\ PARI docs: [u, r, s, t, vs, vr, N, ...] but exact layout version-dependent;
\\ safest: use ellminimalmodel + ellchange for the minimal model, and
\\ ellglobalred(...)[1] = u; conductor = ellglobalred[7]? probe:
print("probe32 vec length = ", #red32);
quit;