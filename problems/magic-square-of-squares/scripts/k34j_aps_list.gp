EZ = ellinit([0,1016,0,576,0]);
JL = ellinit([0,0,0,-27894240,56491485696]);
forprime(p=23, 300, if(p != 17 && p != 271, print("p=", p, ": apJL=", ellap(JL,p), " apEZ=", ellap(EZ,p))));
quit