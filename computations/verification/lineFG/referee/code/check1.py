import sys; sys.path.insert(0,'.')
from own_lift import *
eta=2.0
kap={5:7,7:5,9:3,11:1,13:7,15:5,1:3,3:1}
ev={}
for a in (0,2,4,6):
    V,E=build(wk1(eta,a),30,5,1.0,0.6,36)
    ev[a]=(np.linalg.eigvals(V),np.linalg.eigvals(E))
    lv=sorted(abs(ev[a][0]))[::-1][:3]; le=sorted(abs(ev[a][1]))[::-1][:2]
    print('sector',a,'top|V|',lv,'top|E|',le,flush=True)
def Zlift(m,kappa):
    c=ca(kappa); return (1-LAM**-m)*sum(c[a]*(np.sum(ev[a][0]**m)-np.sum(ev[a][1]**m)) for a in (0,2,4,6))
for m,L in ((5,8),):
    zb=brute_Z(m,eta,kap[m],L); zl=Zlift(m,kap[m])
    print('m',m,'brute',zb,'lift',zl,'rel',abs(zb-zl)/abs(zb),flush=True)
# |c_a| check
for k in (1,3,5,7): print('kappa',k,[round(abs(ca(k)[a]),15) for a in range(8)])
