"""Referee: partial trace Tr[(I x |1_{i=0}><e_0|)-type] of core Galerkin matrix powers (own implementation of the layout)."""
import numpy as np, json, sys
def ptrace(pre,j,m):
    info=json.load(open(pre+'.json')); A=np.load(f'{pre}_b{j}_mid.npy'); NS=info['NS']; K0=info['K0']; typ=info['typ']
    Rc=K0 if typ=='V' else K0-0.5
    cores=[c2 for c2 in range(-2*K0-2,2*K0+3) if c2%2==(0 if typ=='V' else 1) and abs(c2/2)<=Rc]
    Kc={c2:(info['K2'] if abs(c2/2)>Rc-1 else info['K']) for c2 in cores}
    X=np.linalg.matrix_power(A,m); tr=0; off=0
    for c2 in cores:
        Ko=Kc[c2]
        for e in range(0,NS,3):
            tr+=np.trace(X[off+e*Ko:off+(e+1)*Ko, off:off+Ko])
        off+=NS*Ko
    assert off==A.shape[0]
    return tr, info['classes'][str(j)]
if __name__=='__main__':
    m=int(sys.argv[3]); Zh=np.load(sys.argv[4]); lam=3+2*2**.5
    for j in range(int(sys.argv[5])):
        tv,c=ptrace(sys.argv[1],j,m); te,_=ptrace(sys.argv[2],j,m)
        b=tuple(int(t) for t in c.split(':')); bc=(b[0],(-b[1])%7); z=Zh[b]
        print(c,'TrV',np.round(tv,6),'TrE',np.round(te,6),'V-E',np.round(tv-te,6),'brute',np.round(z,6),'conj-brute',np.round(Zh[bc],6),
              'rel|V-E-brute|=%.2e'%(abs(tv-te-z)/abs(z)), 'rel|(1-lam^-m)(V-E)-brute|=%.2e'%(abs((1-lam**-m)*(tv-te)-z)/abs(z)))
