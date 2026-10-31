"""Referee [N]: size of the h_p-level iso deviation in W'_m units: phi(2h)^-1 * sum_{rho=(+-2,8)} (q-2)|Z0|^2/q^2 (2ReX+|X|^2), times
the inherited-level factor A' = 1 + sum_{e | h/q, e>1, e q <= sqrt h} n_e/e^2 (TRACE-228, n_e multiplicative: q_i - 2 per prime), divided by m;
compared with 1.0184224^m/m (the D7 scale of Theorem J, up to K_j)."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineI/code'); from law import mdata
from sympy import totient, factorint, divisors
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
out=[]
for p,f in [(7,'logs/ref_depth_sum_p7_K120_s1.json'),(19,'logs/ref_depth_sum_p19_K400_s1.json'),(29,'logs/ref_depth_sum_p29_K200_s1.json'),(47,'logs/ref_depth_sum_p47_K100_s1.json')]:
    d=json.load(open(f)); m=3*p; q=hp(p); h=mdata(m)['h']; phi=int(totient(2*h))
    Z0=abs(complex(*d['Z0'])); X=complex(*d['X'])
    dev=(q-2)*Z0**2/q**2*(2*X.real+abs(X)**2)
    Ap=1.0
    for e in divisors(h//q):
        e=int(e)
        if e==1 or (e*q)**2>h: continue
        ne=1
        for r,v in factorint(e).items(): ne*= (int(r)-2) if v==1 else (int(r)-1)
        Ap+=ne/e**2
    val=2*dev*Ap/phi/m
    rec=dict(p=p,m=m,dev_factor=2*X.real+abs(X)**2,Aprime=Ap,phi_digits=len(str(phi)),Wprime_over_m_contribution=val,D7_scale=1.0184224**m/m,ratio=val/(1.0184224**m/m))
    out.append(rec); print(json.dumps(rec))
json.dump(out,open('logs/ref_wprime_size.json','w'),indent=1)
