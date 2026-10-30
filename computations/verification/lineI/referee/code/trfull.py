import numpy as np, sys
sys.path.insert(0,'code'); from ptrace import ptrace
lam=3+2*2**.5; m=9
tv,_=ptrace('data/V_1_3',0,m); te,_=ptrace('data/E_1_3',0,m)
Z=np.load('data/zpred_d7_2_8_m9_K40.npy')
z=(1-lam**-m)*(tv-te)
print('TrV',tv,'TrE',te,'(1-lam^-9)(V-E)',z,'zpred Zhat(1,3)',Z[1,3],'rel diff %.2e'%(abs(z-Z[1,3])/abs(Z[1,3])))
