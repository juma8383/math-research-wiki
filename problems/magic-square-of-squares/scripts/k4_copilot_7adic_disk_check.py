P=lambda x:x**8-252*x**6+518*x**4-252*x**2+1
# one Newton square root lift modulo 7^n for fixed integer x
def lift_sqrt(x,z0,n):
 z=z0
 for k in range(1,n):
  mod=7**(k+1)
  e=(z*z-P(x))//(7**k)
  c=(-e*pow(2*z,-1,7))%7
  z+=c*7**k
 assert (z*z-P(x))%(7**n)==0
 return z
for x,z0 in [(7,1),(14,1),(8,3),(-6,3),(1,4),(-1,4)]:
 z=lift_sqrt(x,z0,6)
 print(x,z,(z*z-P(x))%(7**6))
print('all lifts verified mod 7^6')
