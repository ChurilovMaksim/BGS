"""Exact recurrence, floating execution; bounded hypotheses discriminator.

The rank-one update is an identity. No uniform stochastic drift estimate
or limiting universality conclusion is implemented or claimed here.
"""
import json
from pathlib import Path
import numpy as np
from frame_probe import haar, fourier, rng


def energy(r):
    leverage = np.diag(r).real
    assert leverage.min() > 0
    return float(np.sum(np.abs(r)**4/(leverage[:, None]*leverage[None, :])))


def evolve(w):
    n = len(w)
    order = rng.permutation(n)
    w = w[np.ix_(order, order)]
    s, b, x, r = w.copy(), w.copy(), np.eye(n, dtype=complex), np.eye(n, dtype=complex)
    observations, residuals = [], []
    for u in range(n, 2, -1):
        if u in (n, n//2, 24, 12, 6, 3):
            direct = b@np.linalg.solve(b.conj().T@b, b.conj().T)
            direct_r_error = float(np.linalg.norm(direct-r))
            step = n-u
            if step:
                l = np.linalg.solve(np.eye(step)-w[:step, :step],w[:step,step:])
                direct_s = w[step:,step:]+w[step:,:step]@l
            else:
                direct_s = w
            direct_s_error = float(np.linalg.norm(direct_s-s))
            # Left phases on current output rows leave energy invariant.
            phases = np.r_[np.ones(step), np.exp(2j*np.pi*rng.random(u))]
            rephased = phases[:,None]*r*phases.conj()[None,:]
            phase_invariance = float(abs(energy(rephased)-energy(r)))
            assert max(direct_r_error,direct_s_error,phase_invariance) < 5e-8
            en = energy(r)
            observations.append({'u':u, 'energy':en,
                'complex_target':2*u/(u+1), 'energy_defect':en-2*u/(u+1),
                'inverse_clock_first_moment':float((n/u**2)*np.trace(x).real),
                'retained_leverage_mean':float(np.mean(np.diag(r).real[step:])),
                'removed_leverage_mean':float(np.mean(np.diag(r).real[:step])) if step else None,
                'direct_projection_error':direct_r_error,'direct_schur_error':direct_s_error,
                'phase_invariance_error':phase_invariance})
        if u==3:
            break
        ell = -s[0,:].conj()
        ell[0] += 1
        v = x@ell
        denominator = float(np.vdot(ell,v).real)
        assert denominator>0
        z = b@v/np.sqrt(denominator)
        residuals.append(float(abs(np.vdot(z,z)-1)))
        q = 1/(1-s[0,0])
        next_s = s[1:,1:]+np.outer(s[1:,0],q*s[0,1:])
        next_b = b[:,1:]+np.outer(b[:,0],q*s[0,1:])
        next_x = (x-np.outer(v,v.conj())/denominator)[1:,1:]
        r = r-np.outer(z,z.conj())
        s,b,x = next_s,next_b,(next_x+next_x.conj().T)/2
    assert max(residuals)<5e-8
    return {'observations':observations,'rank_one_unit_norm_error':max(residuals)}


def main():
    result=[]
    for model in ('haar','broken_fourier','symmetric_fourier'):
        for sample in range(4):
            n=101
            u=haar(n) if model=='haar' else fourier(n,model=='broken_fourier')
            w=np.exp(2j*np.pi*rng.random(n))[:,None]*u
            result.append({'model':model,'sample':sample,**evolve(w)})
    output={'seed':202610091,'N':101,'paths':12,'arithmetic':'complex128',
        'non_claim':'No uniform contraction, inverse-clock theorem, or BGS theorem follows from these paths.',
        'results':result}
    Path(__file__).with_name('projection_evolution_results.json').write_text(json.dumps(output,indent=2)+'\n')
    for model in ('haar','broken_fourier','symmetric_fourier'):
        paths=[p for p in result if p['model']==model]
        print(model,[(r['u'],round(float(np.mean([p['observations'][i]['energy_defect'] for p in paths])),6)) for i,r in enumerate(paths[0]['observations'])])


if __name__=='__main__':
    main()
