import sys,os,subprocess,numpy as np,time
sys.path.insert(0,'computations/verification/lineE/referee/code')
from aud import data,K1,fvals
m=int(sys.argv[1]); eta=float(sys.argv[2]); out=sys.argv[3]; thr=sys.argv[4] if len(sys.argv)>4 else '8'
h=data(m)['h']; tab=np.exp(1j*eta*fvals(K1,0.5+np.arange(h)/h)).astype(np.complex128)
tf=f'/tmp/lg_tab_{os.getpid()}.bin'; tab.tofile(tf); t0=time.time()
subprocess.run(['./classes_sym',str(m),str(h),tf,out],check=True,env=dict(os.environ,OMP_NUM_THREADS=thr))
os.remove(tf); print('done',m,h,time.time()-t0,'s',flush=True)
