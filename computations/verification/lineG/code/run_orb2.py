import sys,os,subprocess,numpy as np,time
sys.path.insert(0,'computations/verification/lineE/referee/code')
from aud import data,K1,fullkick,fvals
kick=sys.argv[1]; m=int(sys.argv[2]); eta=float(sys.argv[3]); out=sys.argv[4]; thr=sys.argv[5] if len(sys.argv)>5 else '8'
C=K1 if kick=='k1' else fullkick()
h=data(m)['h']; tab=np.exp(1j*eta*fvals(C,0.5+np.arange(h)/h)).astype(np.complex128)
tf=f'/tmp/lg_tab_{os.getpid()}.bin'; tab.tofile(tf); t0=time.time()
subprocess.run(['./classes_orb2',str(m),str(h),tf,out],check=True,env=dict(os.environ,OMP_NUM_THREADS=thr))
os.remove(tf); print('done',kick,m,h,time.time()-t0,'s',flush=True)
