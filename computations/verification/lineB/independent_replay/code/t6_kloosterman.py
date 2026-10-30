"""Check phase-3 §1 'self-duality' identities for prime h (239) and composite h (1393=7*199)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math
for h in [41,239,1393]:
    a,b=np.meshgrid(np.arange(h),np.arange(h),indexing='ij')
    Nm=(a*a+6*a*b+b*b)%h; Tr=(2*a+6*b)%h
    Kl=np.array([np.sum(np.exp(2j*np.pi*Tr[Nm==u]/h)) for u in range(h)])
    R=np.arange(h); G=np.array([[np.sum(Kl[(R*s)%h]*np.conj(Kl[(R*t)%h])) for t in range(h)] for s in range(h)]) if h<300 else None
    # gauss: sum_y e((A Nm y + Tr y)/h)
    gs=[]
    for A in [1,2,5]:
        if math.gcd(A,h)!=1: continue
        v=np.sum(np.exp(2j*np.pi*((A*Nm+Tr)%h)/h)); Ai=pow(A,-1,h)
        gs.append((A, v/(h*np.exp(-2j*np.pi*Ai/h))))
    msg=f'h={h}: Gauss ratio sum/(h e(-A^-1/h)) = '+', '.join(f'A={A}:{r.real:+.6f}{r.imag:+.1e}i' for A,r in gs)
    if G is not None:
        pred=h*(h*np.eye(h)-1)
        msg+=f' | max|sum_r Kl(rs)conj Kl(rs\') - h(h[s=s\']-1)| = {np.max(np.abs(G-pred)):.3e}; s=s\'=0 entry {G[0,0].real:.1f} vs {pred[0,0]:.1f}; s=s\'=1 {G[1,1].real:.1f} vs {pred[1,1]:.1f}'
    print(msg, flush=True)
for h in [41,239]:
    a,b=np.meshgrid(np.arange(h),np.arange(h),indexing='ij')
    Nm=(a*a+6*a*b+b*b)%h; Tr=(2*a+6*b)%h
    Kl=np.array([np.sum(np.exp(2j*np.pi*Tr[Nm==u]/h)) for u in range(h)]); R=np.arange(h)
    G=np.array([[np.sum(Kl[(R*s)%h]*np.conj(Kl[(R*t)%h])) for t in range(h)] for s in range(h)]); pred=h*(h*np.eye(h)-1)
    print(f'h={h}: restricted to s,s\' != 0: max dev = {np.max(np.abs(G[1:,1:]-pred[1:,1:])):.2e}; row s=0 vs s\'!=0: G[0,1]={G[0,1].real:.1f} (formula {pred[0,1]:.0f})')
