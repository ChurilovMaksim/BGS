if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from parity_transfer import *
sg=(1,-1,1,-1)
print('Validation: chi_m transfer vs direct support sum')
for m in [3,5,7,9]:
    for eta in [2,10,50,200]:
        K=8 if eta<=50 else 14
        t=chi_transfer(eta,m,K,sg); d=chi_direct(eta,m)
        print(f' m={m} eta={eta} K={K} transfer={t.real:+.10f}{t.imag:+.1e}j direct={d.real:+.10f} |diff|={abs(t-d):.1e}',flush=True)
print('Leading eigenvalues |mu| of M_a (a=0..3) and of |M_a| (positive majorant), eta grid; K convergence')
for eta in [0.5,1,2,5,10,25,50,100,200,400]:
    for K in ([8,12] if eta<=100 else [14,20]):
        Ms=Mats(eta,K)
        mu=[np.max(np.abs(np.linalg.eigvals(M))) for M in Ms]
        rp=[np.max(np.abs(np.linalg.eigvals(np.abs(M)))) for M in Ms]
        print(f' eta={eta:5g} K={K} max|mu_a|={max(mu):.6f} (per a: {" ".join(f"{x:.5f}" for x in mu)})  rho(|M|) max={max(rp):.4f}  m_half(=log2/-log|mu|)={np.log(2)/-np.log(max(mu)):.1f}',flush=True)
