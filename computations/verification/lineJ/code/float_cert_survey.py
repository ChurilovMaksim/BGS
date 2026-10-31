import numpy as np, scipy.sparse.linalg as ssl, json, sys
CL='1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2'.split(',')
out={}
for A in (2,-2):
  for S in (0,2,4,6):
    for T in 'VE':
      for b,c in enumerate(CL):
        M=np.load(f'data/cert/{T}_{A}_s{S}_b{b}_mid.npy')
        ev=ssl.eigs(M,k=7,which='LM',return_eigenvectors=False,tol=1e-12,maxiter=20000); ev=ev[np.argsort(-abs(ev))]
        key=f'{T} a={A} s{S} {c}'; out[key]=[(round(abs(z),9),round(np.angle(z),9)) for z in ev]
        print(key,out[key][0],out[key][3][0],flush=True)
json.dump(out,open('logs/cert/float_survey.json','w'),indent=0)
