import sys, numpy as np, json
sys.path.insert(0,'.'); from spot5 import members, P
m,sg,D=33,1,8119; tb=members(m,sg,D); k=np.arange(D)
def Ehat(specs):
    A=np.zeros(D,complex)
    for s in specs:
        f=np.load(P+f'p11_s1_{s}.npz'); Z0=complex(f['Z0']); nz=~((f['bx']==0)&(f['by']==0))
        np.add.at(A,f['Nm'][nz],(f['w']*f['Zh']/Z0)[nz])
    return (D*np.fft.ifft(A))[tb], A
E,_=Ehat(['ii','ui','iu']); Eu,Au=Ehat(['uu'])
f=np.load(P+'p11_s1_uu.npz'); print('uu total',int(f['total']),'nsamp',len(f['w']),'w',f['w'][0])
r0=np.abs(1+E)**2; r1=np.abs(1+E+Eu)**2
print('dev/main exact3',r0.mean()-1,' with sampled uu',r1.mean()-1,' mean Eu',Eu.mean(),' var Eu (noisy)',np.var(Eu))
# noise floor: split sample in halves
rng=np.random.default_rng(0); idx=rng.permutation(len(f['w']))
Z0=complex(f['Z0']); u=f['w']*f['Zh']/Z0
for half in (idx[:2000],idx[2000:]):
    A=np.zeros(D,complex); np.add.at(A,f['Nm'][half],2*u[half]); Eh=(D*np.fft.ifft(A))[tb]
    print(' half: mean',Eh.mean(),'var',np.var(Eh),'dev',(np.abs(1+E+Eh)**2).mean()-1)
