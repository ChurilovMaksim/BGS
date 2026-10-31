"""N16 (1) [N]: local carry-entry weight.  Single isolated carry c: letters v = (c, -6c, c).  Ratio of the Frobenius norm of
K_c K_{-6c} K_c (Y) to K_0^3 (Y) for Y = Perron matrix Y* of K (normalised) and for Y = Phi Phi^*; also the Y_c (N14 certificate) relative size
sup-ratio lambda_max(Y_c^-1/2 |.| Y_c^-1/2) of the Hermitian part.  usage: g_triple.py"""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N16/code'); sys.argv=[sys.argv[0],'0','0']
import g_scalar as G
import fastops as F
Yc=np.load('/workspace/bgs-lineN/N14/logs/b_cp2_Yc_0.28.npz')['Yc']; Li=np.linalg.inv(np.linalg.cholesky(Yc))
Y=np.outer(F.Phi,F.Phi.conj())
for _ in range(30): Y=G.Tv(0,Y); Y/=np.trace(Y).real
out={}
for name,Y0 in (('Perron',Y),('PhiPhi*',np.outer(F.Phi,F.Phi.conj()))):
    base=G.Tv(0,G.Tv(0,G.Tv(0,Y0)))
    for c in (1,2,3):
        Z=G.Tv(c,G.Tv(-6*c,G.Tv(c,Y0)))
        H=Li@Z@Li.conj().T; Hb=Li@base@Li.conj().T
        r=dict(fro_ratio=float(np.linalg.norm(Z)/np.linalg.norm(base)),Yc_ratio=float(np.abs(np.linalg.eigvalsh((H+H.conj().T)/2)).max()/np.linalg.eigvalsh((Hb+Hb.conj().T)/2).max()),
               psi_ratio=float(abs(F.psi@Z@F.psi.conj())/abs(F.psi@base@F.psi.conj())))
        out[f'{name}_c{c}']=r; print(name,c,r,flush=True)
json.dump(out,open('/workspace/bgs-lineN/N16/logs/g_triple.json','w'),indent=1)
