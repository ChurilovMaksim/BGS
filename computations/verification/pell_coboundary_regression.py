#!/usr/bin/env python3
"""Second-order coboundary kicks: exact arithmetic and matrix falsifiers.

The universal proof is in mathematics/pell_coboundary_resonance.md. Exact
pair-key enumeration and floating-point operator checks have separate scope.
Default checks use NumPy and mpmath. --extended also requires SciPy.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import subprocess

import mpmath as mp
import numpy as np

from pell_floquet_regression import design, weyl, hermitian_exponential

ROOT = Path(__file__).resolve().parents[2]
Atom = tuple[int, int, int]  # time, species (u=0,w=1), sign
Pair = tuple[Atom, Atom]


def advance(v: tuple[int, int], n: int) -> tuple[int, int]:
    return ((3*v[0]+2*v[1]) % n, (4*v[0]+3*v[1]) % n)


def species_vectors(k: int) -> tuple[int, list[list[tuple[int, int]]]]:
    n, _, _ = design(k)
    out = []
    for v in ((2, 4), (4, 4)):
        vs = []
        for _ in range(k):
            vs.append(v)
            v = advance(v, n)
        assert v == vs[0]
        out.append(vs)
    return n, out


def atom_pair(a: Atom, b: Atom) -> Pair:
    return tuple(sorted((a, b)))


def pair_audit(k: int) -> dict:
    n, vv = species_vectors(k)
    bins: dict[tuple[int, int], list[Pair]] = defaultdict(list)
    for t in range(k):
        for s in range(t+1, k):
            for a in range(2):
                for b in range(2):
                    for e in (-1, 1):
                        for f in (-1, 1):
                            v, w = vv[a][t], vv[b][s]
                            key = ((e*v[0]+f*w[0]) % n, (e*v[1]+f*w[1]) % n)
                            bins[key].append(((t,a,e),(s,b,f)))
    histogram = Counter(map(len, bins.values()))
    if k >= 11:
        assert (0,0) not in bins
        assert max(histogram) == 2
        assert histogram[2] == 4*k
        assert histogram[1] == 8*k*(k-2)
        expected = set()
        for j in range(k):
            q = (j+1) % k
            for e in (-1,1):
                # w_(j+1)-w_j = u_(j+1)+u_j
                expected.add(frozenset((atom_pair((q,1,e),(j,1,-e)),
                                        atom_pair((q,0,e),(j,0,e)))))
                # w_(j+1)-u_j = u_(j+1)+w_j
                expected.add(frozenset((atom_pair((q,1,e),(j,0,-e)),
                                        atom_pair((q,0,e),(j,1,e)))))
        observed = {frozenset(v) for v in bins.values() if len(v) == 2}
        assert observed == expected
    return {'K':k, 'N':str(n), 'term_count':8*k*(k-1),
            'unique_keys':len(bins), 'multiplicity_histogram':{str(m):v for m,v in sorted(histogram.items())},
            'structural_classification_checked':k >= 11,
            'zero_key_present':(0,0) in bins}


def phase_audit(k: int) -> dict:
    n, vv = species_vectors(k)
    with mp.workdps(max(80,len(str(n))+20)):
        aa = []
        for j in range(k):
            values = []
            for a in range(2):
                for b in range(2):
                    v, w = vv[a][0], vv[b][j]
                    omega = (v[0]*w[1]-v[1]*w[0]) % n
                    omega = min(omega, n-omega)
                    values.append(2*abs(mp.sin(mp.pi*mp.mpf(omega)/n)))
            aa.append(max(values))
        assert all(abs(aa[j]-aa[-j % k]) < mp.mpf('1e-50') for j in range(k))
        l1 = sum(aa)
        weighted = sum(abs(k-1-2*j)*aa[j]/2 for j in range(k))
        assert l1 < 128 and weighted < 128
        # Multiplicity-two bound, before the simpler 1024/K estimate.
        hs_bound_sq = 32*sum((k-j)*j*j*aa[j]**2 for j in range(1,k))/mp.mpf(k)**4
        assert hs_bound_sq <= mp.mpf(1024)/k
        return {'K':k, 'phase_l1':float(l1), 'K_weighted_phase_l1':float(weighted),
                'commutator_HS_squared_upper_bound':float(hs_bound_sq)}


def dense(k: int) -> list[dict]:
    if k > 7:
        raise ValueError('Dense reference is deliberately limited to K<=7')
    n, f, h = design(k)
    q, hi = -f % n, pow(h,-1,n)
    v, w = (q,1), (q*h % n, hi)
    def sym(z):
        a = weyl(n,z[0] % n,z[1] % n)
        return a+a.conj().T
    aa, dd = sym(v), sym(w)
    cc = sym((v[0]-w[0],v[1]-w[1]))-sym((v[0]+w[0],v[1]+w[1]))
    u0 = np.eye(n,dtype=complex)[(h*np.arange(n)) % n]
    assert np.max(abs(dd-u0@aa@u0.conj().T)) < 3e-11
    comm = aa@dd-dd@aa
    sn = math.sin(4*math.pi/n)
    assert np.max(abs(comm+2j*sn*cc)) < 3e-11
    cs = []
    for t in range(k):
        ht, hit = pow(h,t,n), pow(h,-t,n)
        minus = ((v[0]-w[0])*ht,(v[1]-w[1])*hit)
        plus = ((v[0]+w[0])*ht,(v[1]+w[1])*hit)
        cs.append(sym(minus)-sym(plus))
    av = sum(cs)/k
    gg = sum((k-1-2*t)*cs[t]/(2*k) for t in range(k))
    assert np.max(abs(gg-u0@gg@u0.conj().T-cc+av)) < 4e-11
    assert abs(np.trace(av@av).real/n-4/k) < 1e-10
    d = (n-1)//2
    proj = np.zeros((n,d))
    idx = np.arange(1,d+1)
    proj[idx,idx-1] = 1/math.sqrt(2)
    proj[n-idx,idx-1] = -1/math.sqrt(2)
    a, dmat, c, av, g, u = [proj.T@z@proj for z in (aa,dd,cc,av,gg,u0)]
    kcomm = a@dmat-dmat@a
    ka, kd = a@kcomm-kcomm@a, dmat@kcomm-kcomm@dmat
    kan = float(max(abs(np.linalg.eigvalsh(ka))))
    kdn = float(max(abs(np.linalg.eigvalsh(kd))))
    assert kan <= 32*sn*sn+1e-9 and kdn <= 32*sn*sn+1e-9
    xval = np.linalg.eigvalsh(math.sqrt(k)*av/2)
    rows = []
    for tau in (.25,1.,2.):
        eps = math.sqrt(tau/(2*math.sqrt(k)*sn))
        zeta = eps*eps*sn
        uk = hermitian_exponential(a-dmat,eps)@u
        gauge = hermitian_exponential(a,-eps)
        effective = hermitian_exponential(c,zeta)@u
        r = gauge@uk@gauge.conj().T-effective
        op_error = float(np.linalg.norm(r,2))
        exact_bound = eps**3*(kan/2+kdn/6)
        uniform_bound = (64/3)*eps**3*sn**2
        assert op_error <= exact_bound+2e-10 <= uniform_bound+4e-10
        jg = hermitian_exponential(g,-zeta)
        normal = hermitian_exponential(av,zeta)@u
        nf_error = float(np.linalg.norm(jg@effective@jg.conj().T-normal,'fro')/math.sqrt(d))
        # For K<11 this is an independent finite check, not an application
        # of the asymptotic-range support classification.
        assert nf_error <= 1000*zeta*zeta/math.sqrt(k)+1e-9
        for m in (1,2):
            actual = np.trace(np.linalg.matrix_power(uk,m*k))/d
            model = np.mean(np.exp(1j*m*tau*xval))
            assert abs(actual-model) <= m*k*(op_error+nf_error)+2e-9
            rows.append({'K':k,'N':n,'dimension':d,'tau':tau,'epsilon':eps,'zeta':zeta,'m':m,
                         'gauge_operator_error':op_error,'nested_commutator_error_bound':exact_bound,
                         'uniform_gauge_bound':uniform_bound,'effective_normal_HS_error':nf_error,
                         'actual_trace_real':float(actual.real),'actual_trace_imag':float(actual.imag),
                         'average_model_trace_real':float(model.real),'average_model_trace_imag':float(model.imag),
                         'Gaussian_limit':math.exp(-m*m*tau*tau/2),
                         'average_second_moment':float(np.mean(xval*xval)),
                         'average_fourth_moment':float(np.mean(xval**4))})
    return rows


def central_fourth_audit(k: int) -> dict:
    """Full trace of X^4 from Weyl convolution, without diagonalization.

    The odd trace lies in the displayed analytic band apart from numerical
    rounding in the evaluated central coefficients. This is not an interval
    arithmetic implementation.
    """
    import cmath
    n, vv = species_vectors(k)
    atoms = [((e*v[0] % n,e*v[1] % n),1 if a==0 else -1)
             for a in range(2) for v in vv[a] for e in (-1,1)]
    conv = defaultdict(complex)
    half = pow(2,-1,n)
    for v,cv in atoms:
        for w,cw in atoms:
            power = ((v[0]*w[1]-v[1]*w[0])*half) % n
            power = power if power <= n//2 else power-n
            phase = cmath.exp(2j*math.pi*(power/n))
            conv[((v[0]+w[0]) % n,(v[1]+w[1]) % n)] += cv*cw*phase/(4*k)
    assert abs(conv[(0,0)]-1) < 1e-12
    moment = sum(abs(x)**2 for x in conv.values())
    return {'K':k,'N':str(n),'full_second_moment':1,
            'full_fourth_moment':moment,
            'odd_fourth_center':n*moment/(n-1),
            'odd_fourth_noncentral_bound':(4*k)**2/(n-1),
            'method':'Weyl convolution, complex double precision; analytic odd-tail bound separate'}


def universal_loop_controls() -> dict:
    rng = np.random.default_rng(20260905)
    count = 0
    max_ratio = 0.0
    for dim in (2,3,6):
        raw = rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
        a=(raw+raw.conj().T)/4
        raw = rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
        d=(raw+raw.conj().T)/4
        q=a@d-d@a
        bound = np.linalg.norm(a@q-q@a,2)/2+np.linalg.norm(d@q-q@d,2)/6
        for eps in (-1.3,-.3,.03,.7,2.4):
            loop=hermitian_exponential(a,-eps)@hermitian_exponential(a-d,eps)@hermitian_exponential(d,eps)
            target=hermitian_exponential(1j*q,eps*eps/2)
            err=float(np.linalg.norm(loop-target,2))
            assert err <= abs(eps)**3*bound+3e-12
            max_ratio=max(max_ratio,err/(abs(eps)**3*bound))
            count+=1
    return {'seed':20260905,'cases':count,'largest_error_to_bound_ratio':max_ratio,
            'scope':'finite generic Hermitian numerical falsifiers, not a proof of the Duhamel lemma'}


def sampled_coboundary(k: int, tau: float, probes: int, seed: int) -> list[dict]:
    """Sparse exponential propagation of the ACTUAL residual kick.

    SciPy is an optional extended-experiment dependency. The stochastic RMS
    bound is not a deterministic interval or a floating-point error bound.
    """
    from scipy.sparse import csr_matrix
    from scipy.special import jv
    if probes < 2 or tau < 0:
        raise ValueError('need at least two probes and nonnegative tau')
    n,f,h=design(k)
    if n>50000:
        raise ValueError('extended reference limited to N<=50000')
    x=np.arange(n,dtype=np.int64)
    def sparse_weyl(a,b):
        power=(a*(x-b*pow(2,-1,n))) % n
        phase=np.exp(2j*np.pi*power/n)
        return csr_matrix((phase,(x,(x-b) % n)),shape=(n,n))
    w0=sparse_weyl(-f % n,1)
    w1=sparse_weyl((-f*h) % n,pow(h,-1,n))
    hh=w0+w0.conj().T-w1-w1.conj().T
    d=(n-1)//2
    rng=np.random.default_rng(seed)
    coefficients=(1j)**rng.integers(0,4,size=(d,probes))
    z=np.zeros((n,probes),dtype=complex)
    z[1:d+1]=coefficients/math.sqrt(2)
    z[n-np.arange(1,d+1)]=-coefficients/math.sqrt(2)
    initial=z.copy()
    eps=math.sqrt(tau/(2*math.sqrt(k)*math.sin(4*math.pi/n)))
    # Jacobi--Anger / Chebyshev series with a conservative analytic tail.
    # ||H||<=4. This bound controls truncation, not floating-point rounding.
    zz=4*eps
    degree=max(1,math.ceil(abs(zz)))
    if zz == 0:
        tail=0.0
    else:
        while True:
            j=degree+1
            log_bound=j*math.log(abs(zz)/2)-math.lgamma(j+1)+zz*zz/(4*(j+1))
            ratio=abs(zz)/(2*(degree+2))
            tail=2*math.exp(log_bound)/(1-ratio)
            if tail < 1e-15:
                break
            degree+=1
    coeff=np.array([jv(j,zz)*(1 if j==0 else 2)*(1j)**j for j in range(degree+1)])
    scaled=hh/4
    def kick(v):
        t0=v
        out=coeff[0]*t0
        t1=scaled@v
        out=out+coeff[1]*t1
        for j in range(2,degree+1):
            t2=2*(scaled@t1)-t0
            out+=coeff[j]*t2
            t0,t1=t1,t2
        return out
    rows=[]
    for step in range(1,2*k+1):
        z=kick(z[(h*x) % n])
        if step % k == 0:
            values=np.sum(initial.conj()*z,axis=0)/d
            norm_drift=float(max(abs(np.sum(abs(z)**2,axis=0)/d-1)))
            assert norm_drift<2e-8
            rows.append({'K':k,'N':n,'dimension':d,'tau':tau,'epsilon':eps,
                         'm':step//k,'trace_real':float(values.mean().real),
                         'trace_imag':float(values.mean().imag),
                         'Gaussian_limit':math.exp(-(step//k)**2*tau*tau/2),
                         'probes':probes,'seed':seed,'norm_drift':norm_drift,
                         'complex_RMS_bound':1/math.sqrt(d*probes),
                         'sample_standard_error':float(np.std(values,ddof=1)/math.sqrt(probes)),
                         'chebyshev_degree':degree,'one_step_series_tail_bound':tail,
                         'method':'sparse Chebyshev propagation, seeded fourth-root-of-unity odd probes; analytic series tail, no certified rounding bound'})
    return rows


def report(cpp: Path | None) -> dict:
    ks = (3,5,7,11,13,17,23,31,47,101)
    pairs = [pair_audit(k) for k in ks]
    if cpp:
        got = json.loads(subprocess.check_output([str(cpp.resolve())],text=True,timeout=60))
        assert [{k:v for k,v in r.items() if k in ('K','N','term_count','unique_keys','multiplicity_histogram')}
                for r in pairs] == got['checks']
    return {'producer':'computations/verification/pell_coboundary_regression.py',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite two-species collision classification plus floating-point finite operator identities; not a proof by simulation, microscopic universality, or a priority claim.',
            'status':'PASS','cpp_cross_check':bool(cpp), 'pair_checks':pairs,
            'phase_checks':[phase_audit(k) for k in ks],
            'universal_loop_controls':universal_loop_controls(),
            'fourth_checks':[central_fourth_audit(k) for k in (3,5,7,11,17,23,47,101)],
            'dense_checks':sum((dense(k) for k in (3,5,7)),[])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpp',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--arithmetic-only',action='store_true')
    parser.add_argument('--extended',action='store_true')
    parser.add_argument('--probes',type=int,default=16)
    args = parser.parse_args()
    if args.arithmetic_only:
        data = {'checks':[pair_audit(k) for k in (3,5,7,11,13,17,23)]}
    else:
        data = report(args.cpp)
        data['sampled_checks']=[]
        if args.extended:
            for k in (11,13):
                for tau in (.5,1.):
                    data['sampled_checks'].extend(sampled_coboundary(k,tau,args.probes,20260905+k))
    text = json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')

if __name__=='__main__':
    main()
