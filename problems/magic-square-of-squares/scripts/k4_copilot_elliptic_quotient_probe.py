from fractions import Fraction as F

def add(P,Q,a2,a4):
 if P is None:return Q
 if Q is None:return P
 x1,y1=P;x2,y2=Q
 if x1==x2 and y1==-y2:return None
 if P!=Q:m=(y2-y1)/(x2-x1)
 else:
  if y1==0:return None
  m=(3*x1*x1+2*a2*x1+a4)/(2*y1)
 x3=m*m-a2-x1-x2
 y3=-(y1+m*(x3-x1))
 return x3,y3
for name,a2,P in [('Et',512,(F(4),F(504))),('Et',512,(F(-256),F(1024))),('Eu',496,(F(0),F(0)))]:
 Q=None
 print(name,P)
 for n in range(1,13):
  Q=add(Q,P,a2,61440)
  print(n,Q)
