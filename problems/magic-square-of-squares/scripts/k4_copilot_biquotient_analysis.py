from math import isqrt

def primes(n):
 return [p for p in range(3,n) if all(p%d for d in range(2,isqrt(p)+1))]
# C4 projective mod p: z^2=P(a,b); count nondegenerate affine x values
for p in primes(100):
 sq={z*z%p for z in range(p)}
 xs=[]
 for x in range(p):
  P=(pow(x,8,p)-252*pow(x,6,p)+518*pow(x,4,p)-252*pow(x,2,p)+1)%p
  if P in sq and x not in (0,1,p-1): xs.append(x)
 print(p,len(xs),xs[:6])
# exact reciprocal quotient identity checks
for x in [2,3,5,7]:
 P=x**8-252*x**6+518*x**4-252*x**2+1
 t_num=x*x+1 # t=(x^2+1)/x
 # x^4*(t^4-256t^2+1024)=P
 rhs=t_num**4-256*t_num**2*x*x+1024*x**4
 assert P==rhs
print('quotient identity checks passed')
