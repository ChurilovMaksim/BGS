"""Second reader: Prop C self-duality remark.  Fresh code.  y = a + b*lambda in O/hO, Nm y = a^2+6ab+b^2, Tr y = 2a+6b.
(i) Gauss sum G(A) = sum_y e((A Nm y + Tr y)/h) vs h e(-Abar/h), A unit;  (ii) orthogonality
sum_r Kl(rs) conj Kl(rs') = h(h[s=s'] - 1) for s,s' units, h prime;  (iii) the s=0 row (expected to fail)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, json, math
def run(h):
    a=np.arange(h); A,B=np.meshgrid(a,a,indexing='ij'); Nm=((A*A+6*A*B+B*B)%h).ravel(); Tr=((2*A+6*B)%h).ravel()
    ph=np.exp(2j*np.pi*Tr/h)
    Kl=np.bincount(Nm,weights=ph.real,minlength=h)+1j*np.bincount(Nm,weights=ph.imag,minlength=h)
    gdev=0.0
    for Aa in range(1,h):
        if math.gcd(Aa,h)!=1: continue
        G=np.sum(np.exp(2j*np.pi*((Aa*Nm+Tr)%h)/h)); gdev=max(gdev,abs(G-h*np.exp(-2j*np.pi*pow(Aa,-1,h)/h)))
    r=np.arange(h); U=[s for s in range(1,h) if math.gcd(s,h)==1]
    M=np.array([[np.sum(Kl[(r*s)%h]*np.conj(Kl[(r*t)%h])) for t in U] for s in U])
    E=h*(h*np.eye(len(U))-1); odev=float(np.max(np.abs(M-E)))
    row0=[complex(np.sum(Kl[(r*0)%h]*np.conj(Kl[(r*t)%h]))) for t in U[:3]]
    return dict(h=h,gauss_sum_max_dev=float(gdev),orth_max_dev_units=odev,s0_row_first3=[str(np.round(z,6)) for z in row0],
                s0_formula_value=-h, Kl0=str(np.round(Kl[0],9)))
for h in [7,41,239,1393]:
    print(json.dumps(run(h)),flush=True)
