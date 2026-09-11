from math import gcd
Ds=[1,-1,2,-2,3,-3,5,-5,6,-6,10,-10,15,-15,30,-30]
mods=[8,16,3,5,7,11,13,17,19,23,29,31]
for d in Ds:
 out=[]
 for m in mods:
  sq={x*x%m for x in range(m)}; ok=False
  # homogeneous primitive mod each prime-ish modulus: at least one of U,V unit wrt m's prime factors
  for u in range(m):
   for v in range(m):
    if gcd(gcd(u,v),m)!=1: continue
    # use multiplied equation d*N^2=d^2 U4+31d U2V2+240V4, avoids division
    rhs=(d*d*pow(u,4,m)+31*d*u*u*v*v+240*pow(v,4,m))%m
    # d*n^2 rhs
    if any((d*n*n-rhs)%m==0 for n in range(m)):
     ok=True;break
   if ok:break
  if not ok:out.append(m)
 print(d,'obstructed',out)
