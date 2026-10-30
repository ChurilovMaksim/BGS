import numpy as np, scipy.sparse.linalg as ssl, sys
A=np.load(sys.argv[1]); ev=ssl.eigs(A,k=8,which='LM',tol=1e-12,return_eigenvectors=False)
print(sys.argv[1],'top |eig|:',np.sort(abs(ev))[::-1].round(6))
