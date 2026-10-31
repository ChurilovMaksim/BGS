"""N15 rigorous binary64 helpers (N14-referee F14.1).  Model: IEEE-754 binary64, round-to-nearest, standard model fl(a op b)=(a op b)(1+d),
|d|<=u=2^-53 for + - * / sqrt on reals; complex products/sums via real ops (Higham Lemma 3.5: complex inner products of length n satisfy
|fl(x^T y)-x^T y| <= sqrt2 gamma_{n+2} |x|^T|y|, gamma_n = nu/(1-nu)); libm exp/cos/sin within 1 ulp (assumption, stated).
BLAS/einsum/np.add.at may sum in any order: the standard-model bound holds for every order.  All bounds below are applied with an
extra factor 1.01 for the rounding of the bound computations themselves (all quantities O(1), lengths < 10^4)."""
import numpy as np, math
u=2.0**-53
def gam(n): return n*u/(1-n*u)
def cgam(n): return math.sqrt(2)*gam(n+2)            # complex inner product of length n
def fro(M): return float(np.sqrt(np.sum(np.abs(M)**2)))*(1+gam(M.size+2))*1.01   # rigorous upper bound of ||M||_F
def matmul_err(A,B):
    """returns fl(AB) and a rigorous Frobenius bound on |fl(AB)-AB|"""
    return A@B, cgam(A.shape[1])*fro(np.abs(A)@np.abs(B))*1.01
def norm2_upper(S,m=7):
    """rigorous upper bound of ||S||_2 without eigen-solvers: lam_max(G)^(2^m) <= ||G^(2^m)||_F, G=S^*S, by repeated (scaled) squaring
    with tracked errors; overestimate factor <= rank^(1/2^(m+2))."""
    G,eG=matmul_err(S.conj().T,S); G=(G+G.conj().T)/2; eG=eG+gam(2)*fro(G)
    c=fro(G); H=G/c; e=eG/c*(1+2*u)          # T_0 = G_true/c, ||H - T_0||_F <= e   (G_true = S^*S)
    logC=math.log(c); expo=1.0                # lam_max(S^*S) = c * (lam_max(T_m) * prod c_k^{w_k})^(1/2^m)
    acc=0.0
    for k in range(m):
        nH=fro(H); H2,eM=matmul_err(H,H); H2=(H2+H2.conj().T)/2
        e2=e*(nH+nH+e)+eM+gam(2)*fro(H2)      # ||H^2 - T^2|| <= e(||H||+||T||) + rounding (+ symmetrisation)
        ck=fro(H2); H=H2/ck; e=e2/ck*(1+2*u)
        acc+=(2.0**(m-1-k))*math.log(ck)
    lam_Tm=fro(H)+e
    loglam=logC+(math.log(lam_Tm)+acc)/(2.0**m)
    return math.exp(loglam/2)*(1+1e-12)
def psd_lower(W):
    """rigorous lower bound of lambda_min(W_true) for Hermitian W given exactly as the float matrix (caller adds its own input error):
    W = V Lam V^* + R,  lam_min >= min(Lam)*(1 -/+ ||V^*V - I||) - ||R||."""
    lam,V=np.linalg.eigh(W)
    VL=V*lam[None,:]; P,eP=matmul_err(VL,V.conj().T); R=W-P; nR=fro(R)+eP+gam(1)*fro(W)
    E,eE=matmul_err(V.conj().T,V); E=E-np.eye(W.shape[0]); nE=fro(E)+eE
    lmin=float(lam.min()); 
    lo=lmin*(1-nE) if lmin>=0 else lmin*(1+nE)
    return lo-nR, dict(lmin_float=lmin,R=nR,E=nE)
