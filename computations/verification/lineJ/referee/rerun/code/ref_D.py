import sys; sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from law import mdata, pell
bad=0
for m in range(9,3000,6):
    D=mdata(m); h=D['h']; x,y=pell(m)
    if h%2==0 or 4*h*h!=2*(x-1) or x*x-8*y*y!=1: bad+=1
print('(D) m=9..2997 (m=3 mod 6): h odd, 4h^2=2(x_m-1), x_m^2-8y_m^2=1 (=> 4h^2 = lam^m+lam^-m-2 < lam^m): failures',bad)
