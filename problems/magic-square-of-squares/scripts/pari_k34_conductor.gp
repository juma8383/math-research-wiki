\\ pari_k34_conductor.gp -- conductors of the two K34 sieve curves (2026-09-03)
\\ tE_A: y^2 = x^3 - 256x^2 + 18432x ; tE_B: y^2 = x^3 + 256x^2 - 2048x
\\ (a1=0, a2=+-256, a3=0, a4=+-..., a6=0 -> PARI ellinit format [a1,a2,a3,a4,a6])
EA = ellinit([0,-256,0,18432,0]);
EB = ellinit([0, 256,0,-2048,0]);
print("tE_A conductor = ", ellglobalrank == 0, ""); \\ placeholder guard
print("tE_A conductor = ", EA[1]);
\\ ellglobalrank does not exist in older pari; use ellsearch? No: use ellidentify via ellsearch? Simplest: ellchange/ellglobalred
redA = ellglobalred(EA);
redB = ellglobalred(EB);
print("tE_A minimal model = ", redA[1], "  conductor N = ", redA[2]);
print("tE_B minimal model = ", redB[1], "  conductor = ", redB[2]);
print("tE_A j = ", ellj(EA));
print("tE_B j = ", ellj(EB));
print("tE_A disc = ", ellsearch == 0, "");
\\ sigma and Verzobio C
DA = ellglobalred(EA)[3]; \\ minimal discriminant
DB = ellglobalred(EB)[3];
\\ conductor values:
NA = redA[2]; NB = redB[2];
\\
sigmaA = log(abs(DA))/log(NA); sigmaB = log(abs(DB))/log(NB);
print("sigma_A = ", sigmaA = sigmaA, "");
quit;