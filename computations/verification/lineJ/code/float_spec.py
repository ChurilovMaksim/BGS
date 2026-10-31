import numpy as np, json, sys
cls=['1:3','2:1','0:1','1:2','1:5','0:3','1:0','0:2']
for A in (2,-2):
  print('=== a =',A)
  for typ in ('V','E'):
    for j,c in enumerate(cls):
        row=[]
        for S in (0,2,4,6):
            M=np.load(f'data/sec/{typ}_{A}_s{S}_b{j}_mid.npy'); ev=np.linalg.eigvals(M); o=np.argsort(-abs(ev)); ev=ev[o]
            row.append(f's{S}: '+' '.join(f'{abs(z):.7f}' for z in ev[:4:3])+f' [{ev[0]:.6f}]')
        print(typ,c,' | '.join(row))
