"""N11b [N]/[P-sketch] bookkeeping: X model vs unit-gas Y model and bounds at p=5..59 (+ asymptotic exponents)."""
import json, math, cmath
Lam=complex(7.490e-4,3.722e-4); ReLlo=6.238e-4
LU=complex(1.005429e-3,-1.834361e-3); AU=3.9569e-3   # c_LambdaU p=29,47 (identical to 1e-11)
mu=1.9154732; eps=1+math.sqrt(2); lam=eps*eps
def hp(p):
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    return x
rows=[]
for p in [5,7,11,13,29,37,47,59]:
    h=hp(p); n=h-2
    X=2*((1+Lam)**p-1)
    Ygas_c=-(2/n)*2*((1+Lam+LU)**p-(1+Lam)**p)      # kappa ~ -1 part
    Ygas_b=(2/n)*2*((1+abs(Lam)+AU)**p-(1+abs(Lam))**p)
    Ybulk_b=(2/n)*h*h*(1.2744/mu)**(3*p)             # C' route (squarefree), [P+CA mod C' inputs]
    Xlo=2*((1+ReLlo)**p)-1
    rows.append(dict(p=p,h=h,X=[X.real,X.imag],abs1X=abs(1+X),Ygas_central=[Ygas_c.real,Ygas_c.imag],absYgas_bound=Ygas_b,
                     Ybulk_Cprime_bound=Ybulk_b,abs1XY_model=abs(1+X+Ygas_c),Xlo_floor=Xlo,ratio_Ygas_over_X=abs(Ygas_c)/abs(X)))
for r in rows: print(r['p'],'|1+X|=%.6f'%r['abs1X'],'Ygas~%.2e%+.2ei'%tuple(r['Ygas_central']),'|Ygas|<=%.2e'%r['absYgas_bound'],'Cprime<=%.2e'%r['Ybulk_Cprime_bound'],'|1+X+Y|=%.6f'%r['abs1XY_model'],'floor %.6f'%r['Xlo_floor'],'ratio %.1e'%r['ratio_Ygas_over_X'])
exps=dict(X_growth=math.log(1+ReLlo),unit_gas_rel=math.log(abs(1+Lam+LU))-math.log(abs(1+Lam))-math.log(eps),
          unit_gas_abs_bound=math.log(1+abs(Lam)+AU)-math.log(eps),Cprime=3*math.log(1.2744/mu)+math.log(eps),
          mixed_rate_at_Tprime=math.log(eps)+3*math.log(1.4279/mu),mixed_rate_at_1p36=math.log(eps)+3*math.log(1.36/mu),
          mixed_rate_at_1p2624=math.log(eps)+3*math.log(1.2624/mu))
print(json.dumps(exps,indent=1)); json.dump(dict(rows=rows,exponents_per_p=exps),open('logs/e_model.json','w'),indent=1)
