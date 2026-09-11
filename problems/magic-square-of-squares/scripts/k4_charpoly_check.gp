C4 = x^8 - 252*x^6 + 518*x^4 - 252*x^2 + 1;
g1 = x^4 - 252*x^3 + 518*x^2 - 252*x + 1;
g2 = x^4 - 256*x^2 + 1024;
g3 = x^4 - 248*x^2 + 16;
allok = 1; tested = 0; bad = 0;
forprime(p = 3, 100, ok = 1; iferr(cp4 = hyperellcharpoly(C4*Mod(1,p)); q1 = hyperellcharpoly(g1*Mod(1,p)); q2 = hyperellcharpoly(g2*Mod(1,p)); q3 = hyperellcharpoly(g3*Mod(1,p)), E, bad = bad+1; ok = -1); if(ok == 1, tested = tested+1; if(cp4 != q1*q2*q3, allok = 0; print("REAL MISMATCH at p = ", p)), if(ok == 0, allok = 0)));
print("primes tested (good reduction): ", tested, ", skipped (bad reduction): ", bad);
print("J(C4) ~ E_s x E_t x E_u (charpoly product identity): ", allok);
quit