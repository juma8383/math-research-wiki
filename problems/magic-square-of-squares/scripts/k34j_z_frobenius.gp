Zpts(p) = p + 1 + sum(xx=0, p-1, kronecker(8*xx^8 + 1016*xx^4 + 9, p));
JL = ellinit([0,0,0,-27894240,56491485696]);
EZ = ellinit([0,1016,0,576,0]);
okJ = 0; badJ = 0;
forprime(p=13, 300, if(p==17 || p==19 || p==271, next); tz = p+1 - Zpts(p); pred = ellap(JL,p) + ellap(EZ,p); if(tz==pred, okJ++, badJ++, print("  mismatch at p=",p,": tZ=",tz," pred=",pred)));
print("Z trace vs J_L+E_Z traces, good primes 13..300: ok=", okJ, " mismatch=", badJ);
print("#Z(F_13)=", Zpts(13), "  #Z(F_23)=", Zpts(23), "  #Z(F_5)=", Zpts(5));
quit