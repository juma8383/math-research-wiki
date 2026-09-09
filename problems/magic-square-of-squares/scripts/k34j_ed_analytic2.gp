E = ellinit([0,-6973560,0,14122871424,0]);
g = ellglobalred(E); disc = g[1];
print("disc = ", disc);
N = 5000;
s = 0.0;
cnt = 0;
p = 2;
while(p < N, ap = ellap(E, p); if(gcd(p, disc) == 1, s += ap/p*1.0); p = nextprime(p+1));
print("sum a_p/p up to ", N, " = ", s);
print("log-log N = ", log(log(N)*1.0));
print("DONE")