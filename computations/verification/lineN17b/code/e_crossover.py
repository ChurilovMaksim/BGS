# Crossover of the gas lower bound G(p) vs Robin bound on I_p (inherited levels floor), [P-arith, float]
import math
a=6.234e-4-5.14415e-7; g=0.5772156649015329
def G(p): return (2*(1+a)**p-1)**2-1
def lnh(p): return 0.881373587019543*p-math.log(2)   # h_p = S_{(p-1)/2} ~ eps^p/2 (h_5=41)
def Ib(p):
    L=math.log(2*lnh(p)+math.log(4)); return math.exp(g)*L+0.6483/L-1
def Ib_d(p):  # Robin applied to divisors of K_p only up to sqrt(h_m): same bound (monotone), keep
    return Ib(p)
for p in [1289,1300,1400,1450,1500,1600,2000,3000]:
    print(p, round(G(p),3), round(Ib(p),3), round(G(p)-Ib(p),3))
p=1289
while G(p)<=Ib(p): p+=1
print("first p with G>I_bound:",p)
