\\ init curves once; single-line loop with if(p!=17, ...)
EZ = ellinit([0,1016,0,576,0]);
JL = ellinit([0,0,0,-27894240,56491485696]);
forprime(p=23, 60, if(p != 17, print("p=", p, ": apEZ=", ellap(EZ,p), " apJL=", ellap(JL,p))));
quit