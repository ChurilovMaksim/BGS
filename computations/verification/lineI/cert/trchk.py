"""Float check of a certG_build core matrix: partial trace Tr[(I x |e_(0,0)><1_{i=0}|) A^m] vs reference Zhat, and leading |eig|."""
import sys, json, numpy as np
pre=sys.argv[1]; j=sys.argv[2]; m=int(sys.argv[3]); ref=complex(sys.argv[4]) if len(sys.argv)>4 else None
info=json.load(open(pre+'.json')); A=np.load(pre+f'_b{j}_mid.npy'); NS=info['NS']; cyc=NS!=len(info['states'])
K0=info['K0']; K=info['K']; K2=info['K2']; typ=info['typ']
Rc=K0 if typ=='V' else K0-0.5
cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if (c2%2==(0 if typ=='V' else 1)) and abs(c2/2)<=Rc]
Kc={c2:(K2 if abs(c2/2)>Rc-1 else K) for c2 in cores}
X=np.linalg.matrix_power(A,m); tr=0; off=0
for c2 in cores:
    Ko=Kc[c2]
    for e in range(NS):
        if cyc and e%3: continue
        for k in range(Ko): tr+=X[off+e*Ko+k, off+0*Ko+k]
    off+=NS*Ko
ev=np.sort(abs(np.linalg.eigvals(A)))[::-1]
print('ptrace',tr,'ref',ref,'top|eig|',ev[:6].round(5))
