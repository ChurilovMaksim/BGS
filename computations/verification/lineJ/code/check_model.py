"""[N] check: Zhat_C(m) ~ (1-lam^-m) sum_a c_a(case) mu_{C,a}^m (top orbits) vs zpred class sums; Z0 via Line F."""
import numpy as np, json
LAM=3+2*np.sqrt(2)
sec=json.load(open('logs/sectors_exact.json'))['cases']
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
spec={}
for A in (2,-2):
    for j,c in enumerate(cls):
        for S in (0,2,4,6):
            M=np.load(f'data/sec/V_{A}_s{S}_b{j}_mid.npy'); ev=np.linalg.eigvals(M); spec[(A,c,S)]=ev
def case(m): return {9:9,15:15,21:21,3:27}[m%24]
for A in (2,-2):
  for m in (39,63,81,105,117,123):
    cs=sec[f'{case(m)},{A}']['c']
    Zh=np.load(f'/workspace/bgs-lineI/data/zpred_d7_{A}_8_m{m}_K40.npy')
    out=[]
    for c in ('1:3','2:1','0:1','1:2'):
        bx,by=map(int,c.split(':'))
        pred=(1-LAM**-m)*sum(complex(cs[str(S)]['c'])*np.sum(spec[(A,c,S)]**m)/3 for S in (0,2,4,6))
        out.append(f'{c}: rel {abs(pred/Zh[bx,by]-1):.2e}')
    print('a',A,'m',m,' '.join(out))
