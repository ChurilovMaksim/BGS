"""N4 (B16) [CA]: assemble Lambda_free^{16V/E} <= f + pi from b16_schur (core, both permutation patterns) and cert_lift16 (error terms).
Tensor factor: A_n = (diag unitary) * swap^(n+PAR).  Even-letter part = (1/2)(L + L^{(-1)^n}) (phases +-1), a direct sum of two scalar-phase
operators -> each Line F bound (uniform in unimodular letter phases) applies; odd part likewise times (I (x) swap).  Hence
delta, Delta, ||X|| of the tensor operator <= 2 x (scalar bounds) [P].  Norm |||(u,t,y)||| = max(||Ru||,||t||,b||y||), R = D^{-1}
(D = diag d, max d = 1), ||R|| = 1/min d, ||R^{-1}|| = 1;  pi = eps max(||R||,1,b)(||R^{-1}||+1+1/b),  b = f/(||X||(||R^{-1}||+1))."""
import json, numpy as np, math
from flint import arb
r2={'V':arb('1.0534557'),'E':arb('1.0529202')}; thr={'V':3.04126,'E':3.04280}
out={}
for typ in 'VE':
    cj=json.load(open(f'logs/cert16_{typ}.json'))
    eps=2*(arb(cj['delta1'])+arb(cj['delta2'])+arb(cj['Delta'])); Xn=2*arb(cj['Xnorm'])
    worst=None
    for P in (0,1):
        sj=json.load(open(f'logs/b16_schur_{typ}_P{P}.json')); d=np.load(f'logs/b16_schur_{typ}_P{P}_d.npy')
        f=arb(sj['f_core']); nR=arb(1/float(d.min()))*(1+arb('1e-12')); nRi=arb(1)*(1+arb('1e-12'))
        b=f/(Xn*(nRi+1)); pen=eps*max(nR,arb(1),b)*(nRi+1+1/b)
        L=(f+pen).upper(); rate=((f+pen)*r2[typ]).root(3).upper()
        rec=dict(PAR=P,f_core=float(f),normR=float(nR.upper()),b=float(b.mid()),eps=float(eps.upper()),Xnorm_tensor=float(Xn.upper()),penalty=float(pen.upper()),
                 Lambda_free_upper=float(L),threshold=thr[typ],unit_point_rate=float(rate))
        out[f'{typ}_P{P}']=rec; print(typ,P,json.dumps(rec))
json.dump(out,open('logs/b16_final.json','w'),indent=1)
