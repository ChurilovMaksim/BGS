"""Referee: sector antiunitary map at Galerkin level: sigma(V^{-2}_{beta,a+4}) = conj sigma(V^{+2}_{beta,a}) (and E).
Compare top eigenvalues (ARPACK, k=8) and Frobenius norms / sorted |entries| of the mid matrices."""
import numpy as np, scipy.sparse.linalg as ssl, json
J='/workspace/bgs-lineJ/data/cert/'
out=[]; worst=0; worstF=0; worstS=0
for T in 'VE':
  for a in (0,2,4,6):
    for b in range(8):
      Mp=np.load(J+f'{T}_2_s{a}_b{b}_mid.npy'); Mm=np.load(J+f'{T}_-2_s{(a+4)%8}_b{b}_mid.npy')
      ep=ssl.eigs(Mp,k=8,which='LM',tol=1e-13,return_eigenvectors=False); em=ssl.eigs(Mm,k=8,which='LM',tol=1e-13,return_eigenvectors=False)
      ep=np.conj(ep)
      # match
      d=max(min(abs(z-em)) for z in ep[np.argsort(-abs(ep))][:6])/abs(ep).max()
      F=abs(np.linalg.norm(Mp)-np.linalg.norm(Mm))/np.linalg.norm(Mp)
      S=np.max(abs(np.sort(abs(Mp).ravel())-np.sort(abs(Mm).ravel())))
      worst=max(worst,d); worstF=max(worstF,F); worstS=max(worstS,S)
      out.append((T,a,b,float(abs(ep).max()),d,F,S))
      print(T,'s%d->s%d'%(a,(a+4)%8),'b',b,'|top| %.10f'%abs(ep).max(),'eigdiff %.2e'%d,'Fro %.1e'%F,'sorted|entries| %.1e'%S,flush=True)
print('WORST eig rel diff',worst,'Fro',worstF,'entries',worstS)
