Ez = ellinit([0,1016,0,576,0]);
print("E_Z: y^2 = x^3 + 1016x^2 + 576x");
print("j = ", Ez.j);
print("disc = ", factor(Ez.disc));
print("cond = ", ellglobalred(Ez)[1], " = ", factor(ellglobalred(Ez)[1]));
print("torsion = ", elltors(Ez));
print("rank = ", ellrank(Ez));
print("bad primes: ", factor(ellglobalred(Ez)[1])[,1]~);
quit