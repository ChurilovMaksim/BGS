import numpy as np, json
W=json.load(open('code/monomial_intertw.json'))['neg_9_2']
info=json.load(open('data/sm_src92.json')); A64=np.load('data/sm_src92_b0_mid.npy'); A13=np.load('data/sm_src92_b1_mid.npy')
NS=info['NS']; K0=info['K0']; cores=[c2 for c2 in range(-2*K0,2*K0+1,2)]
Kc={c2:(info['K2'] if abs(c2/2)>K0-1 else info['K']) for c2 in cores}
off={};o=0
for c in cores: off[c]=o; o+=NS*Kc[c]
D=o; Q=np.zeros((D,D),complex)
for c2 in cores:
    Ko=Kc[c2]
    for pos in range(16):
        for i in range(3):
            for k in range(Ko):
                Q[off[-c2]+(W['pi'][pos]*3+i)*Ko+k, off[c2]+(pos*3+i)*Ko+k]=(-1)**k*np.exp(-2j*np.pi*W['c'][pos]/8)
for nm,S,T in [('R x Y: L_{1:3} -> L_{-(1:3)}',A13,A64),('R x Y: L_{-(1:3)} -> L_{1:3}',A64,A13),('NEG CONTROL identity',A13,A13)]:
    print(nm,'max dev %.2e'%np.abs(T-Q@S@np.linalg.inv(Q)).max())
