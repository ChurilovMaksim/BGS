                a=Z4
                for r in range(4):a=cadd(a,cmul(coeff[r],zeta(2*r*x)))
                assert a==values[x]
            rows.append({'nu':nu,'Y_mod4':Y,'coefficients':[[str(x) for x in a] for a in coeff]})
    return {'arithmetic':'Q[zeta_8]/(zeta_8^4+1)','coefficient_count':64,
            'all_squared_moduli':'1/4','rows':rows}


# Gaussian rational arithmetic, represented by pairs (real, imaginary).
G0=(Q(0),Q(0))
def ga(a,b):return (a[0]+b[0],a[1]+b[1])
def gs(a,t):return (a[0]*t,a[1]*t)
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gc(a):return (a[0],-a[1])
def gp(a,n):
    b=(Q(1),Q(0))
    for _ in range(n):b=gm(b,a)
    return b
def norm2(a):return a[0]*a[0]+a[1]*a[1]
I=[(Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1))]
R={0:Q(1),1:Q(-1,2),-1:Q(-1,2),7:Q(1,2),-7:Q(1,2),
   6:Q(-1,4),-6:Q(-1,4),8:Q(-1,4),-8:Q(-1,4)}


def phase_checks():
    phase=(Q(-3,5),Q(-4,5));count=0;minimum=None
    for r,s,u,v in itertools.product(range(4),repeat=4):
        coeff={}
        def put(key,a):coeff[key]=ga(coeff.get(key,G0),a)
        for a,b,swapped in [(r,s,False),(u,v,True)]:
            diff=ga(I[a],gs(I[b],-1))
            for k,w in R.items():
                z=gs(gm(phase,diff),w/400)
                p=(4*k-3,1);m=(4*k+3,-1)
                if swapped:p=p[::-1];m=m[::-1]
                put(p,z);put(m,gc(z))
        coeff={k:a for k,a in coeff.items() if a!=G0}
        if r==s and u==v:
            assert not coeff
        else:
            key=(-3,1) if r!=s else (1,-3)
            value=coeff[key]
            assert norm2(value)>=Q(1,80000)
            minimum=norm2(value) if minimum is None else min(minimum,norm2(value))
            count+=1
    assert count==240
    return {'arithmetic':'Gaussian rationals, coefficient multiplied by pi',
            'nonzero_quadruples':count,'zero_quadruples':16,
            'minimum_selected_coefficient_squared_times_pi_squared':str(minimum)}


def conv(a,b):
    out=defaultdict(Q)
    for k,v in a.items():
        for j,w in b.items():out[k+j]+=v*w
    return dict(out)


def exact_leading_constant():
    r4={0:Q(1)}
    for _ in range(4):r4=conv(r4,R)
    assert r4[-2]==Q(245,32) and r4[4]==Q(-189,128)
    z=(Q(-3,5),Q(4,5));z4=gp(z,4);z8=gp(z,8)
    assert z8[0]==Q(164833,390625)>Q(1,4)
    matrix={}
    for k in range(-35,36):
        c=Q(k**4,2400000000)*r4.get(k-3,Q(0))
        if c:matrix[(k,1)]=gs(z4,c)
    for (k,l),v in list(matrix.items()):matrix[(-k,-l)]=gc(v)
    # Independent bridge to the previously proved low-observable coefficient T1.
    assert matrix[(2,1)]==gs(z4,Q(-49,480000000))
    trace=G0
    for (k,l),a in matrix.items():trace=ga(trace,gm(a,matrix.get((l,k),G0)))
    expected=Q(6890365153,737280000000000000000000000)
    assert trace==(expected,Q(0))
    assert expected*3**8>Q(1,10**14)
    eta=Q(1,10**6);rho=Q(1,900)
    assert 22*eta<rho/4 and 1300*eta<Q(1,2)
    assert 1300*eta/(1-1300*eta)<Q(2,1000)
    assert 154*eta/4<Q(5,10**5)
    assert Q(7,5)/(400*Q(22,7))>Q(1,1000)
    assert Q(4*10**55,10**72)<Q(1,2*10**14)
    assert 27*10**8*(7*10**25)*10**20<2*10**55
    assert 2*10**10+4*eta*10**56<10**60
    return {'arithmetic':'exact Gaussian rational finite Fourier matrix',
            'R4_minus2':str(r4[-2]),'R4_plus4':str(r4[4]),'cos_8alpha':str(z8[0]),
            'L_div_pi8':str(expected),'L_approx':float(expected)*math.pi**8,
            'L_lower_using_pi_gt_3':str(expected*3**8),'nonzero_matrix_entries':len(matrix)}


def kernel_reconstruction():
    rows=[]
    for N in [5,7,9,11,17,31]:
        inv8=pow(8,-1,N);nu=(8*inv8-1)//N
        error=period_error=0.
        for x in range(4*N):
            q=x/N
            for Y in range(N):
                y=Y/N
                exact=np.exp(-2j*np.pi*inv8*((3*x*x-2*x*Y+3*Y*Y)%N)/N)/math.sqrt(N)
                coeff=np.array([sum(np.exp(-2j*np.pi*nu*(3*j*j-2*j*Y+3*Y*Y)/8)*np.exp(-2j*np.pi*r*j/4)
                                    for j in range(4))/4 for r in range(4)])
                S0=-(3*q*q-2*q*y+3*y*y)/8
                approx=sum(coeff[r]*np.exp(2j*np.pi*N*(S0+r*q/4)) for r in range(4))/math.sqrt(N)
                error=max(error,abs(exact-approx))
                wrapped=np.exp(-2j*np.pi*inv8*((3*(x%N)**2-2*(x%N)*Y+3*Y*Y)%N)/N)/math.sqrt(N)
                period_error=max(period_error,abs(exact-wrapped))
        assert max(error,period_error)<2e-10
        rows.append({'N':N,'nu':nu,'initial_kernel_error':error,'N_periodicity_error':period_error})
    return {'arithmetic':'floating reconstruction of exact initial identities','rows':rows}


def local_shift_taylor():
    q=np.linspace(.03,.97,61);alpha=math.atan2(4,-3)
    def RR(x,n=0):return sum(float(c)*(2j*np.pi*k)**n*np.exp(2j*np.pi*k*x) for k,c in R.items()).real
    def SS(x):return .13*x-.3*x*x+.017*np.sin(2*np.pi*x)
    p=.13-.6*q+.017*2*np.pi*np.cos(2*np.pi*q)
    s2=-.6-.017*(2*np.pi)**2*np.sin(2*np.pi*q)
    s3=-.017*(2*np.pi)**3*np.cos(2*np.pi*q)
    def amp(x):return 1+.2*np.cos(2*np.pi*x)
    a=amp(q);a1=-.2*2*np.pi*np.sin(2*np.pi*q);a2=-.2*(2*np.pi)**2*np.cos(2*np.pi*q)
    rr=RR(q);r1=RR(q,1);r2=RR(q,2);th=2*np.pi*p-alpha
    L0=rr*np.cos(th)*a/100
    L1=1j*(rr*np.sin(th)*a1+r1*np.sin(th)*a/2+np.pi*rr*np.cos(th)*s2*a)/100
    L2=np.cos(th)*(rr*a2/2+r1*a1/2+r2*a/8-np.pi**2*rr*s2**2*a/2)/100
    L2-=np.sin(th)*(np.pi*s2*(rr*a1+r1*a/2)+np.pi*rr*s3*a/3)/100
    rows=[]
    for h in [.02,.01,.005,.0025,.00125]:
        exact=(RR(q+h/2)*np.exp(-1j*alpha)*amp(q+h)*np.exp(2j*np.pi*(SS(q+h)-SS(q))/h)
              +RR(q-h/2)*np.exp(1j*alpha)*amp(q-h)*np.exp(2j*np.pi*(SS(q-h)-SS(q))/h))/200
        error=float(np.max(abs(exact-(L0+h*L1+h*h*L2))))
        rows.append({'h':h,'second_order_error':error,'error_div_h3':error/h**3})
    assert 5<rows[-2]['second_order_error']/rows[-1]['second_order_error']<12
    assert max(x['error_div_h3'] for x in rows)<1000
    return {'arithmetic':'floating local expansion fixture, not a propagated asymptotic solution','rows':rows}


def grid_normalization():
    rows=[];eps=.001
    for N in [31,101,301,1001]:
        for residue in range(4):
            x=np.arange(residue,N,4)
            direct=np.sum(np.exp(2j*np.pi*eps*x))
            ratio=np.exp(8j*np.pi*eps)
            formula=np.exp(2j*np.pi*eps*residue)*(1-ratio**len(x))/(1-ratio)
            assert abs(direct-formula)<1e-10
            assert abs(direct)<=2/abs(1-ratio)+1e-10
            rows.append({'N':N,'residue':residue,'geometric_identity_error':abs(direct-formula),
                         'normalized_1D_sum':abs(direct)/N})
    return {'scope':'constant nonzero derivative toy phase; nonlinear dephasing is proved in text','rows':rows}


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path('trace005_intensity_limit_checks.json'));args=parser.parse_args()
    script=Path(__file__).resolve();report=script.with_name('TRACE005_intensity_limit.md');inputs=[script,report]
    before={p.name:sha(p) for p in inputs};started=datetime.now(timezone.utc).isoformat();start=time.perf_counter()
    result={'claim_id':'TRACE005-FOUR-BRANCH-INTENSITY-20261025','status':'completed',
            'assertion_tested':'Finite exact branch, phase and leading-coefficient identities; separately floating shift and reconstruction fixtures.',
            'branches':four_branch_exact(),'phases':phase_checks(),'leading':exact_leading_constant(),
            'kernel':kernel_reconstruction(),'local_Taylor':local_shift_taylor(),'grid':grid_normalization(),
            'non_claims':['No numerical confirmation of the actual-tau limit.',
                          'No solution or counterexample to the original coherent pair law or Sine_2.',
                          'The universal error and limit estimates are proved in text.']}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert all(sha(p)==before[p.name] for p in inputs)
    elapsed=time.perf_counter()-start
    manifest={'schema_version':2,'claim_id':result['claim_id'],'repository':{'commit':'standalone research task','dirty':False},
              'command':[sys.executable,*sys.argv],
              'environment':{'software':[{'name':'Python','version':platform.python_version()},{'name':'NumPy','version':np.__version__}],
                             'hardware':platform.machine()},
              'mathematics':{'assertion_tested':result['assertion_tested'],
                             'coefficient_domain':'Q[zeta_8] and Gaussian rationals; separately complex128',
                             'conventions':'h=1/N; four-period cover; original modular inverse8 kernel',
                             'inputs':[p.name for p in inputs],
                             'bounds':{'exact_branch_coefficients':64,'cross_phase_quadruples':240,
                                       'kernel_N':[5,7,9,11,17,31],'local_h':[.02,.01,.005,.0025,.00125]},
                             'non_claims':result['non_claims']},
              'randomness':{'used':False,'generator':'','seed':None},
              'run':{'status':'completed','started_at':started,'runtime_seconds':elapsed,'exit_status':0,
                     'resource_limits':{'memory_bytes':None,'cpu_seconds':None,'max_cores':None,'max_threads':None}},
              'outputs':[{'path':args.output.name,'sha256':sha(args.output),'kind':'result'}],
              'checks':['All exact quadratic Fourier coefficients','All exact first phase coefficients',
                        'Exact fourth-order intensity trace','Small-time constants','Original kernel reconstruction',
                        'Local shift expansion','Residue-grid normalization'],
              'result':'Finite assertions passed; all-N conclusions remain analytic proof obligations audited separately.',
              'residual_risks':['Self-review only','Finite numerical fixtures are not proofs of convergence'],
              'input_artifacts':[{'path':p.name,'sha256':before[p.name],'sha256_after':sha(p)} for p in inputs],
              'declared_results':[args.output.name]}
    mp=args.output.with_name('trace005_intensity_limit_manifest.json');mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'completed','seconds':elapsed,'L_div_pi8':result['leading']['L_div_pi8'],
                      'phase_quadruples':result['phases']['nonzero_quadruples'],'output':str(args.output)},ensure_ascii=False))
```


### XI.7. trace005_intensity_operator_verify.py

```python
#!/usr/bin/env python3
"""Exact finite certificates for O1--O4, with separate complex128 fixtures.

The all-odd-N operator limit and uniform-time bounds are proved in the text.
No finite-size extrapolation or computation of U_N at tau=1e-80 is used.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
import time
import numpy as np


def conv(a, b):
    out = defaultdict(Q)
    for k, v in a.items():
        for l, w in b.items():
            out[k+l] += v*w
    return {k: v for k, v in out.items() if v}


R = conv({0: Q(1), 7: Q(1, 2), -7: Q(1, 2)},
         {0: Q(1), 1: Q(-1, 2), -1: Q(-1, 2)})
assert R == {0: Q(1), 1: Q(-1, 2), -1: Q(-1, 2),
             7: Q(1, 2), 8: Q(-1, 4), 6: Q(-1, 4),
             -7: Q(1, 2), -6: Q(-1, 4), -8: Q(-1, 4)}


def ga(a, b):
    return (a[0]+b[0], a[1]+b[1])


def gs(a, t):
    return (a[0]*t, a[1]*t)


def gm(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def gc(a):
    return (a[0], -a[1])


def gp(a, n):
    v = (Q(1), Q(0))
    for _ in range(n):
        v = gm(v, a)
    return v


def gnorm(a):
    return a[0]**2+a[1]**2


G0 = (Q(0), Q(0))
I4 = [(Q(1), Q(0)), (Q(0), Q(1)),
      (Q(-1), Q(0)), (Q(0), Q(-1))]


def exact_fourier():
    r4 = {0: Q(1)}
    for _ in range(4):
        r4 = conv(r4, R)
    binomial = defaultdict(Q)
    for u in range(-4, 5):
        for v in range(-4, 5):
            binomial[7*u+v] += Q((-1)**abs(v)*math.comb(8, 4+u)
                                 * math.comb(8, 4+v), 256)
    binomial = {k: v for k, v in binomial.items() if v}
    assert r4 == binomial

    # Independent Lie walk. Divide D_g by its common factor 2*pi/200.
    # Reaching p-frequency 0 in four steps from (3,4) forces four -1 steps.
    walk_domains = []
    for sign in (1, -1):
        states = {(3*sign, 4*sign): Q(1)}
        for step in range(4):
            after = defaultdict(Q)
            for (bq, bp), w in states.items():
                for k, rk in R.items():
                    ap = -sign
                    after[(bq+k, bp+ap)] += w*rk*(k*bp-ap*bq)
            states = {a: w for a, w in after.items() if w}
        expected = {k: Q(k**4)*r4.get(k-3*sign, Q(0))
                    for k in range(-35, 36)}
        actual = {k: states.get((k, 0), Q(0)) for k in range(-35, 36)}
        assert actual == expected
        assert all(bp == 0 for bq, bp in states)
        walk_domains.append(len(states))

    ss = sum(Q(k**8)*r4.get(k-3, Q(0))**2
             for k in range(-35, 36))
    tt = sum(Q(k**8)*r4.get(k-3, Q(0))*r4.get(k+3, Q(0))
             for k in range(-35, 36))
    assert ss == Q(51070772446899241, 16384)
    assert tt == Q(-10035589461979669, 8192)
    assert ss+abs(tt) == Q(71141951370858579, 16384)
    z = gp((Q(-3, 5), Q(4, 5)), 4)
    assert z == (Q(-527, 625), Q(336, 625))
    a, b = r4[-2], r4[4]
    tr = 2*a*z[0]
    det = a*a-b*b
    discr = a*a*z[1]**2-b*b
    assert tr == Q(-25823, 2000)
    assert det == Q(924679, 16384)
    assert discr == Q(3778872111, 256000000)
    assert tr*tr-2*det == Q(6890365153, 128000000)
    assert (tr*tr-2*det)/2400000000**2 == Q(
        6890365153, 737280000000000000000000000)
    assert tr/2400000000 == Q(-25823, 4800000000000)

    # All numerical inequalities here are instead checked with rational pi bounds.
    c_lo, c_hi = Q(3**4, 2400000000), Q(22, 7)**4/2400000000
    assert c_hi*c_hi*(ss+abs(tt)) < Q(1, 100)
    assert c_lo*c_lo*(ss+abs(tt)) > Q(1, 400)
    assert c_lo*c_lo*det > Q(25, 10**8)**2
    assert 4*c_lo*c_lo*discr > Q(25, 10**8)**2
    assert c_hi*(abs(a)+abs(b)) < Q(4, 10**7)
    assert c_hi*c_hi*det < Q(16, 10**14)
    return {
        'domain': 'exact rationals and Gaussian rationals',
        'nonzero_R4_coefficients': len(r4),
        'independent_Lie_walk_nonzero_outputs': walk_domains,
        'S0': str(ss), 'T0': str(tt), 'sigma_squared_div_pi8':
            str((ss+abs(tt))/2400000000**2),
        'trace_Q_div_pi4': str(tr/2400000000),
        'rank_two_matrix_trace_div_C': str(tr),
        'rank_two_matrix_determinant_div_C2': str(det),
        'imaginary_part_squared_div_C2': str(discr),
        'trace_Q2_div_pi8': str((tr*tr-2*det)/2400000000**2),
        'sigma_float_illustration':
            math.pi**4/2400000000*math.sqrt(float(ss+abs(tt))),
    }


def phase_coefficients():
    phase = (Q(-3, 5), Q(-4, 5))
    count = 0
    minimum_mixed = minimum_diagonal = None
    for r in range(4):
        for s in range(4):
            if r == s:
                continue
            diff = ga(I4[r], gs(I4[s], -1))
            coeff = defaultdict(lambda: G0)
            for k, rk in R.items():
                value = gs(gm(phase, diff), rk/400)
                p, m = (4*k-3, 1), (4*k+3, -1)
                coeff[p] = ga(coeff[p], value)
                coeff[m] = ga(coeff[m], gc(value))
            mixed = coeff[(-3, 1)]
            assert gnorm(mixed) >= Q(1, 80000)
            diagonal = G0
            for (k, l), value in coeff.items():
                if k+l == 34:
                    diagonal = ga(diagonal, value)
            expected = gs(gc(gm(phase, diff)), Q(-1, 1600))
            assert diagonal == expected
            assert gnorm(diagonal) >= Q(1, 1280000)
            minimum_mixed = (gnorm(mixed) if minimum_mixed is None
                             else min(minimum_mixed, gnorm(mixed)))
            minimum_diagonal = (gnorm(diagonal) if minimum_diagonal is None
                                else min(minimum_diagonal, gnorm(diagonal)))
            count += 1
    assert count == 12
    assert Q(7, 5)/(1600*Q(22, 7)) > Q(1000, 10**8)
    return {'all_offdiagonal_ordered_branch_pairs': count,
            'coefficient_convention': 'coefficients multiplied by pi',
            'minimum_mixed_squared': str(minimum_mixed),
            'minimum_diagonal_squared': str(minimum_diagonal)}


def fourth_trace_fixture():
    """Only the finite normalization identity, with smooth surrogate amplitudes."""
    largest_error = 0.0
    count = 0
    for N in (3, 5, 7):
        q = np.arange(N)/N
        qq, yy = q[:, None], q[None, :]
        rr = sum(float(v)*np.exp(2j*np.pi*k*qq) for k, v in R.items()).real
        beta = 2*np.pi*(-3*qq/4+yy/4)
        for r in range(4):
            for s in range(4):
                if r == s:
                    continue
                ar = 1+.02*(r+1)*np.cos(2*np.pi*qq)+.01*np.sin(2*np.pi*yy)
                ass = 1+.02*(s+1)*np.cos(2*np.pi*qq)+.01*np.sin(2*np.pi*yy)
                amp = ar*ass
                phi = .001*rr*(np.cos(beta+r*np.pi/2)
                               - np.cos(beta+s*np.pi/2))
                tensor_phase = (phi[:, None, :, None]-phi[None, :, :, None]
                                + phi[None, :, None, :]-phi[:, None, None, :])
                tensor_amp = (amp[:, None, :, None]*amp[None, :, :, None]
                              * amp[None, :, None, :]*amp[:, None, None, :])
                quadruple = np.sum(tensor_amp*np.exp(2j*np.pi*N*tensor_phase))
                quadruple /= 256*N**4
                assert abs(quadruple.imag) < 1e-12
                for nu in (1, 3, 5, 7):
                    coeff = []
                    for j in (r, s):
                        values = []
                        for Y in range(N):
                            values.append(sum(
                                np.exp(-2j*np.pi*nu*(3*x*x-2*x*Y+3*Y*Y)/8)
                                * np.exp(-2j*np.pi*j*x/4)
                                for x in range(4))/4)
                        coeff.append(np.array(values))
                    cprod = coeff[0]*np.conj(coeff[1])
                    E = (amp*np.exp(2j*np.pi*N*((r-s)*qq/4+phi))
                         * cprod[None, :]/N)
                    gram = E@E.conj().T
                    direct = np.trace(gram@gram)
                    error = float(abs(direct-quadruple))
                    largest_error = max(largest_error, error)
                    assert error < 1e-11
                    count += 1
    assert count == 144
    return {'domain': 'complex128, finite algebra fixture',
            'N': [3, 5, 7], 'nu': [1, 3, 5, 7],
            'ordered_branch_pairs': 12, 'fixtures': count,
            'maximum_absolute_error': largest_error,
            'non_claim': 'Not a computed asymptotic phase or actual-tau spectrum'}


def mmul(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def rotational_fixtures():
    rows = []
    for N, max_m in ((3, 6), (5, 5)):
        den = N*(N+1)//2
        P = [[Q((x-y) % N+1, den) for y in range(N)] for x in range(N)]
        assert all(sum(row) == 1 for row in P)
        assert all(sum(P[x][y] for x in range(N)) == 1 for y in range(N))
        power = [[Q(i == j) for j in range(N)] for i in range(N)]
        for m in range(1, max_m+1):
            power = mmul(power, P)
            direct = repeated = mass = Q(0)
            for word in itertools.product(range(N), repeat=m):
                weight = Q(1)
                for i in range(m):
                    weight *= P[word[i]][word[(i+1) % m]]
                ell = len({word[i:]+word[:i] for i in range(m)})
                direct += ell*weight
                repeated += (m-ell)*weight
                mass += weight
            trace = sum(power[i][i] for i in range(N))
            assert mass == trace
            assert direct == m*trace-repeated
            bound = 2*m*m*Q(2, N)**((m+1)//2) if m >= 2 else Q(0)
            assert 0 <= repeated <= bound
            rows.append({'N': N, 'm': m, 'words': N**m,
                         'repeat_remainder': str(repeated)})
    # Exact tail constant in the trace telescoping argument.
    r = Q(1, 2)
    series = (r*(1+r)/(1-r)**3-r-4*r*r)/r**3
    assert series == 36
    a = Q(1, 4)
    assert (4+9*a)*(1+a)/(1-a)**3 < 100
    return {'domain': 'exact rationals, exhaustive finite words',
            'rows': rows, 'trace_tail_constant': str(series)}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path('trace005_intensity_operator_checks.json'))
    args = parser.parse_args()
    script = Path(__file__).resolve()
    report = script.with_name('TRACE005_intensity_operator.md')
    prior = script.with_name('TRACE005_intensity_limit.md')
    inputs = [script, report, prior]
    before = {p.name: sha(p) for p in inputs}
    started = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    assertion = ('Exact finite Fourier/Lie, all 12 phase coefficients, '
                 'and exhaustive rotational identities; separate complex128 '
                 'fourth-trace normalization fixtures.')
    result = {
        'claim_id': 'TRACE005-INTENSITY-OPERATOR-20261026',
        'status': 'completed', 'assertion_tested': assertion,
        'fourier': exact_fourier(), 'phase_coefficients': phase_coefficients(),
        'fourth_trace': fourth_trace_fixture(),
        'rotations': rotational_fixtures(),
        'non_claims': [
            'Finite checks do not prove the all-odd-N limit.',
            'No calculation of U_N at tau=1e-80.',
            'No solution or counterexample to coherent pair test or Sine_2.',
            'Operator-limit and all-time estimates are proved in the text.',
        ],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    manifest = {
        'schema_version': 2, 'claim_id': result['claim_id'],
        'repository': {'commit': 'standalone task, no git revision', 'dirty': True},
        'command': [sys.executable, str(script), '--output', str(args.output)],
        'environment': {'software': [
            {'name': 'Python', 'version': platform.python_version()},
            {'name': 'NumPy', 'version': np.__version__}],
            'hardware': platform.machine()},
        'mathematics': {
            'assertion_tested': assertion,
            'coefficient_domain': 'Q and Gaussian rationals; separately complex128',
            'conventions': 'P_xy=|U_xy|^2; H=L^2(T); original four-branch cover',
            'inputs': [p.name for p in inputs],
            'bounds': {'Fourier_support_R4': [-32, 32],
                       'Lie_orders': 4, 'offdiagonal_branch_pairs': 12,
                       'fourth_trace_N': [3, 5, 7], 'fourth_trace_fixtures': 144,
                       'rotation_N_maxm': [[3, 6], [5, 5]]},
            'non_claims': result['non_claims']},
        'randomness': {'used': False, 'generator': '', 'seed': None},
        'run': {'status': 'completed', 'started_at': started,
                'runtime_seconds': time.perf_counter()-start, 'exit_status': 0,
                'resource_limits': {'memory_bytes': None, 'cpu_seconds': None,
                                    'max_cores': None, 'max_threads': None}},
        'outputs': [{'path': args.output.name, 'sha256': sha(args.output),
                     'kind': 'result'}],
        'checks': ['Two independent exact Fourier expansions',
                   'Two independently enumerated four-step Lie walks',
                   'Rank-two Gram and eigenvalue invariants',
                   'All 12 mixed and diagonal first phase coefficients',
                   '144 direct fourth-trace normalization fixtures',
                   'Exhaustive finite rotational-word identities',
                   'Exact uniform-tail constants'],
        'result': 'Finite assertions passed; limiting theorems are separately proved.',
        'residual_risks': ['Self-review only',
                           'Floating fixtures do not certify an asymptotic limit'],
        'input_artifacts': [
            {'path': p.name, 'sha256': before[p.name], 'sha256_after': sha(p)}
            for p in inputs],
        'declared_results': [args.output.name],
    }
    assert all(p['sha256'] == p['sha256_after']
               for p in manifest['input_artifacts'])
    mp = args.output.with_name('trace005_intensity_operator_manifest.json')
    mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({
        'status': result['status'], 'claim_id': result['claim_id'],
        'sigma_float': result['fourier']['sigma_float_illustration'],
        'fourth_trace_fixtures': result['fourth_trace']['fixtures'],
        'max_float_error': result['fourth_trace']['maximum_absolute_error'],
        'manifest': str(mp)}, ensure_ascii=False))
```


### XI.8. trace005_algebraic_parameter_verify.py

```python
#!/usr/bin/env python3
"""Finite exact certificates for the algebraic-parameter theorem E1--E6.

The transcendence theorem, absence of all projective periods and all-N scope
are proved in the report. The script checks finite algebra and separately
floating original-matrix derivative normalizations.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, itertools, json, math, platform, sys, time
import numpy as np

Z=(Q(0),Q(0))
ONE=(Q(1),Q(0))


def ga(a,b): return (a[0]+b[0],a[1]+b[1])
def gs(a,t): return (a[0]*t,a[1]*t)
def gm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gc(a): return (a[0],-a[1])
def norm(a): return a[0]*a[0]+a[1]*a[1]


def formal_mul(a,b):
    out=defaultdict(lambda:Z)
    for k,v in a.items():
        for l,w in b.items(): out[k+l]=ga(out[k+l],gm(v,w))
    return {k:v for k,v in out.items() if v!=Z}


def pconv(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): out[i+j]+=v*w
    return out


def ppow(a,n):
    out=[Q(1)]
    for _ in range(n): out=pconv(out,a)
    return out


def auxiliary(H,a,p):
    s=len(H)-1
    D=(s+1)*p-1
    f=[Q(0)]*(p-1)+[Q(a**D)*v/math.factorial(p-1) for v in ppow(H,p)]
    assert len(f)==D+1
    G=[sum(f[k]*Q(math.factorial(k),math.factorial(j))
           for k in range(j,D+1)) for j in range(D+1)]
    # Exact differential identity G' = G-f.
    for j in range(D+1):
        gp=(j+1)*G[j+1] if j<D else Q(0)
        assert gp-G[j]+f[j]==0
    return f,G,D


def evaluate(poly,x):
    out=Z
    for value in reversed(poly): out=ga(gm(out,x),(value,Q(0)))
    return out


def exact_auxiliary_certificates():
    # L=Q(i), sigma(i)=-i; indicators k encode formal exponent i*k.
    c=(Q(-3,5),Q(4,5))
    F={1:ONE,0:gs(c,-1)}
    conjugate={-k:gc(v) for k,v in F.items()}
    P=formal_mul(F,conjugate)
    assert P=={0:(Q(2),Q(0)),1:gs(gc(c),-1),-1:gs(c,-1)}
    P2=formal_mul(P,P)
    assert P2[0]==(Q(6),Q(0))
    assert P2[0][0]==sum(norm(v) for v in P.values())
    b={k:gs(v,Q(25)) for k,v in P2.items()}
    expected={0:(Q(150),Q(0)),1:(Q(60),Q(80)),
              -1:(Q(60),Q(-80)),2:(Q(-7),Q(24)),
              -2:(Q(-7),Q(-24))}
    assert b==expected
    assert all(b[-k]==gc(v) for k,v in b.items())
    H=[Q(4),Q(0),Q(5),Q(0),Q(1)]
    rows=[]
    for p in [7,11,13,17]:
        f,G,D=auxiliary(H,1,p)
        f0=G[0]
        assert f0.denominator==1 and f0.numerator%p==4**p%p
        S=Z
        for k,bk in b.items():
            value=evaluate(G,(Q(0),Q(k)))
            if k:
                assert all(x.denominator==1 and x.numerator%p==0 for x in value)
            S=ga(S,gm(bk,value))
        assert S[1]==0 and S[0].denominator==1
        assert S[0].numerator%p==150*f0.numerator%p!=0
        rows.append({'p':p,'degree':D,'G0_mod_p':f0.numerator%p,
                     'S_mod_p':S[0].numerator%p,'S_integer':str(S[0])})

    # A nonmonic H and non-integral roots test the denominator factor a^D.
    Hn=[Q(1),Q(0),Q(5),Q(0),Q(4)]
    bn={0:(Q(4),Q(0)),1:ONE,-1:ONE,2:ONE,-2:ONE}
    nonmonic=[]
    for p in [3,5,7]:
        f,G,D=auxiliary(Hn,4,p)
        assert G[0].denominator==1 and G[0].numerator%p==pow(4,D,p)
        S=Z
        for k,bk in bn.items():
            value=evaluate(G,(Q(0),Q(k,2)))
            if k:
                assert all(x.denominator==1 and x.numerator%p==0 for x in value)
            S=ga(S,gm(bk,value))
        assert S[1]==0 and S[0].denominator==1
        assert S[0].numerator%p==4*pow(4,D,p)%p!=0
        nonmonic.append({'p':p,'a':4,'degree':D,
                         'S_mod_p':S[0].numerator%p})
    _,G_bad,_=auxiliary(Hn,1,3)
    bad=evaluate(G_bad,(Q(0),Q(1,2)))
    assert any(x.denominator!=1 for x in bad)

    # Exact feasible choice for the integral error condition (not an asymptotic fit).
    p=503
    assert all(p%j for j in range(2,math.isqrt(p)+1))
    assert math.gcd(p,150*4)==1
    remainder=Q(300*80**p,math.factorial(p-1))
    assert remainder<Q(1,2)
    D=5*p-1
    G_upper=math.factorial(D)//math.factorial(p-1)*10**p
    assert G_upper>0
    return {
        'domain':'exact Gaussian rationals and integers',
        'formal_norm_coefficients':{str(k):[str(x) for x in v] for k,v in P.items()},
        'cleared_square_coefficients':{str(k):[str(x) for x in v] for k,v in b.items()},
        'positive_constant_coefficient':150,'monic_H':[4,0,5,0,1],
        'monic_rows':rows,'nonmonic_H':[1,0,5,0,4],'nonmonic_rows':nonmonic,
        'negative_fixture_without_aD':[str(x) for x in bad],
        'effective_bound_fixture':{'p':p,'K':80,'B':300,
             'remainder_less_than_half':True,'G_upper_bit_length':G_upper.bit_length(),
             'lower_bound_formula':'1 / (2 * sqrt(50 * (2514! / 502!) * 10^503))'},
    }


def original_coefficients():
    rr={0:Q(1),1:Q(1,2),-1:Q(1,2),7:Q(-1,2),-7:Q(-1,2),
        6:Q(-1,4),-6:Q(-1,4),8:Q(-1,4),-8:Q(-1,4)}
    c=defaultdict(lambda:Z)
    def put(key,v): c[key]=ga(c[key],v)
    put((0,7),(Q(1,2),Q(0)));put((0,-7),(Q(1,2),Q(0)))
    for k,v in rr.items():
        put((0,k),(v/10,Q(0)))
        put((0,k+1),(Q(0),-v/200));put((0,k-1),(Q(0),v/200))
        put((1,k),(-3*v/1000,-4*v/1000))
        put((-1,k),(-3*v/1000,4*v/1000))
    put((0,0),(Q(-1,10),Q(0)))
    return {k:v for k,v in c.items() if v!=Z}


def S(v,N): return ((3*v[0]+4*v[1])%N,(2*v[0]+3*v[1])%N)


def cat_order(N):
    x=(1,0);y=(0,1)
    for d in range(1,N*N*2+1):
        x=S(x,N);y=S(y,N)
        if x==(1,0) and y==(0,1):return d
    raise RuntimeError('Order cap reached; no interpretation as a failed theorem.')


def folded_coefficients(c,N):
    out=defaultdict(lambda:Z)
    for (a,b),v in c.items():
        key=(a%N,b%N);out[key]=ga(out[key],v)
    return {k:v for k,v in out.items() if v!=Z}


def orbit_norm(c,N,d):
    average=defaultdict(lambda:Z)
    for label,v in c.items():
        w=(label[0]%N,label[1]%N)
        for _ in range(d):
            average[w]=ga(average[w],gs(v,Q(1,d)));w=S(w,N)
        assert w==(label[0]%N,label[1]%N)
    assert average[(0,0)]==Z
    answer=sum(norm(v) for v in average.values())
    assert answer>=Q(961,5000*d)
    return answer


def A_matrix(c,N,galois_power=1):
    out=np.zeros((N,N),complex);inv2=pow(2,-1,N)
    for (a,b),v in c.items():
        cv=complex(float(v[0]),float(v[1])*(1 if galois_power%4==1 else -1))
        for x in range(N):
            out[x,(x+a)%N]+=cv*np.exp(
                2j*np.pi*((galois_power*b*(x+inv2*a))%N)/N)
    return out


def original_fixtures():
    c=original_coefficients()
    assert folded_coefficients(c,7)=={(0,0):(Q(9,10),Q(0))}
    galois_rows=[];max_galois_error=0.
    for N in [3,5,7,9,11,15,19]:
        count=0
        for s in range(1,4*N):
            if math.gcd(s,4*N)!=1:continue
            A=A_matrix(c,N,s)
            error=float(np.linalg.norm(A-A.conj().T))
            max_galois_error=max(max_galois_error,error)
            assert error<1e-11
            count+=1
        galois_rows.append({'N':N,'all_cyclotomic_automorphisms':count})

    rows=[]
    for N in [19,21,25,27,29,33,35]:
        d=cat_order(N);b2=orbit_norm(c,N,d)
        assert folded_coefficients(c,N).get((0,0),Z)==Z
        A=A_matrix(c,N)
        x=np.arange(N)[:,None];y=np.arange(N)[None,:]
        M=np.exp(2j*np.pi*((-pow(8,-1,N)*(3*x*x-2*x*y+3*y*y))%N)/N)/np.sqrt(N)
        Md=np.linalg.matrix_power(M,d);zeta=np.trace(Md)/N
        assert np.linalg.norm(Md-zeta*np.eye(N))<1e-10
        U1=1j*N*A@M;U2=-Q(1,2)*N*N*(A@A@M)
        U2=np.asarray(U2,dtype=complex)
        P0=np.eye(N,dtype=complex);P1=np.zeros_like(P0);P2=np.zeros_like(P0)
        for _ in range(d):
            P0,P1,P2=P0@M,P1@M+P0@U1,P2@M+P1@U1+P0@U2
        T0=np.trace(P0);T1=np.trace(P1);T2=2*np.trace(P2)
        expected=-N**3*d*d*float(b2)*zeta
        err=float(abs(T2-expected)/(1+abs(expected)))
        q2=2*(T2*np.conj(T0)).real+2*abs(T1)**2
        expected_q2=-2*N**4*d*d*float(b2)
        qerr=float(abs(q2-expected_q2)/(1+abs(expected_q2)))
        assert err<2e-10 and qerr<2e-10
        assert abs(T1)/(1+N*N*d)<1e-10
        rows.append({'N':N,'d_N':d,'exact_normalized_average_norm_squared':str(b2),
                     'trace_second_derivative_relative_error':err,
                     'form_factor_second_derivative_relative_error':qerr})
    return {'exact_N7_exception':'A_7=(9/10)I',
            'galois_Hermitian':galois_rows,'max_galois_float_error':max_galois_error,
            'original_resonant_derivatives':rows,
            'non_claim':'No original spectrum or form factor is computed at tau=1e-80.'}


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path('trace005_algebraic_parameter_checks.json'))
    args=parser.parse_args()
    script=Path(__file__).resolve()
    inputs=[script,script.with_name('TRACE005_algebraic_parameter.md'),
            script.with_name('TRACE005_resonance_analysis.md')]
    before={p.name:sha(p) for p in inputs}
    started=datetime.now(timezone.utc).isoformat();start=time.perf_counter()
    assertion=('Exact formal Galois norm, positive constant, auxiliary polynomial '
               'congruences and a denominator negative fixture; exact original '
               'finite Weyl averages; separate floating conjugate-Hermitian '
               'and ordered derivative normalization checks.')
    result={'claim_id':'TRACE005-ALGEBRAIC-PARAMETER-20261026','status':'completed',
            'assertion_tested':assertion,'auxiliary':exact_auxiliary_certificates(),
            'original':original_fixtures(),
            'non_claims':['Finite checks do not establish transcendence.',
                          'No numerical test at the actual tau.',
                          'No uniform microscopic trace estimate.',
                          'Sine_2 and the coherent pair test remain unresolved.']}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    manifest={'schema_version':2,'claim_id':result['claim_id'],
              'repository':{'commit':'standalone research task; no git revision','dirty':True},
              'command':[sys.executable,str(script),'--output',str(args.output)],
              'environment':{'software':[{'name':'Python','version':platform.python_version()},
                                          {'name':'NumPy','version':np.__version__}],
                             'hardware':platform.machine()},
              'mathematics':{'assertion_tested':assertion,
                  'coefficient_domain':'Gaussian rationals and integers; separately complex128',
                  'conventions':'Formal X^(ik); original T_N(a,b) and S=(3,4;2,3)',
                  'inputs':[p.name for p in inputs],
                  'bounds':{'auxiliary_primes_monic':[7,11,13,17],
                            'auxiliary_primes_nonmonic':[3,5,7],
                            'integral_error_prime':503,'galois_N':[3,5,7,9,11,15,19],
                            'derivative_N':[19,21,25,27,29,33,35]},
                  'non_claims':result['non_claims']},
              'randomness':{'used':False,'generator':'','seed':None},
              'run':{'started_at':started,'runtime_seconds':time.perf_counter()-start,
                     'status':'completed','exit_status':0,
                     'resource_limits':{'memory_bytes':None,'cpu_seconds':None,
                                        'max_cores':None,'max_threads':None}},
              'outputs':[{'path':args.output.name,'sha256':sha(args.output),'kind':'result'}],
              'checks':['Formal Gaussian-rational Galois norm and positive constant',
                        'Four monic and three nonmonic exact auxiliary constructions',
                        'Missing-denominator negative fixture','Exact p=503 error bound',
                        'Exact finite original orbit norms','All selected field automorphisms',
                        'Independent ordered matrix-product second derivatives'],
              'result':'Finite assertions passed; theorem is separately proved in text.',
              'residual_risks':['Self-review only','No quantitative asymptotic estimate'],
              'input_artifacts':[{'path':p.name,'sha256':before[p.name],
                                  'sha256_after':sha(p)} for p in inputs],
              'declared_results':[args.output.name]}
    assert all(x['sha256']==x['sha256_after'] for x in manifest['input_artifacts'])
    target=args.output.with_name('trace005_algebraic_parameter_manifest.json')
    target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'completed','auxiliary_primes':7,
                      'original_derivative_N':len(result['original']['original_resonant_derivatives']),
                      'max_galois_error':result['original']['max_galois_float_error'],
                      'manifest':str(target)},ensure_ascii=False))
```


### XI.9. trace005_soft_modes_verify.py

```python
"""Finite checks of the paired phase calculation; never a test of Sine_2."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad


def verify():
    eigen_checks = []
    for m in (5, 7, 9, 11):
        adjacency = []
        for step in (1, 2):
            mat = np.zeros((m, m))
            for j in range(m):
                mat[j, (j + step) % m] += 1
                mat[j, (j - step) % m] += 1
            adjacency.append(mat)
        b = 0.25
        hessian = b * (adjacency[0] - adjacency[1])
        max_error = 0.0
        for k in range(m):
            vector = np.exp(2j * np.pi * k * np.arange(m) / m)
            eigenvalue = 2 * b * (
                np.cos(2 * np.pi * k / m) - np.cos(4 * np.pi * k / m)
            )
            max_error = max(
                max_error, float(np.max(np.abs(hessian @ vector - eigenvalue * vector)))
            )
        assert max_error < 2e-14
        assert np.max(np.abs(hessian.sum(axis=1))) == 0.0
        predicted_nullity = 3 if m % 3 == 0 else 1
        nullity = int(np.count_nonzero(np.abs(np.linalg.eigvalsh(hessian)) < 1e-12))
        assert nullity == predicted_nullity
        # A sign-reversed or half-sized answer must fail the Fourier check.
        v = np.exp(2j * np.pi * np.arange(m) / m)
        lam = 4 * b * np.sin(3 * np.pi / m) * np.sin(np.pi / m)
        assert np.max(np.abs(hessian @ v + lam * v)) > 0.01
        assert np.max(np.abs(hessian @ v - lam * v / 2)) > 0.005
        eigen_checks.append({
            "m": m, "max_fourier_error": max_error, "nullity": nullity,
            "m_squared_soft_eigenvalue": float(m * m * lam),
        })

    def profile(t):
        return 0.31 + 0.04 * np.cos(2 * np.pi * t) + 0.012 * np.sin(4 * np.pi * t + 0.37)

    def velocity(t):
        return -0.08 * np.pi * np.sin(2 * np.pi * t) + 0.048 * np.pi * np.cos(4 * np.pi * t + 0.37)

    cubic_quad, _ = quad(lambda t: float(velocity(t) ** 3), 0, 1, epsabs=1e-14)
    cubic_exact = -3 * (0.08 * np.pi) ** 2 * (0.048 * np.pi) * np.cos(0.37) / 4
    assert abs(cubic_quad - cubic_exact) < 1e-14
    continuum_checks = []
    eta = 1 / 17
    for epsilon in (0.0, 0.003, -0.003):
        def metric(t):
            q = profile(t)
            return 0.25 - 4 * np.pi ** 2 * epsilon * np.cos(2 * np.pi * q) * np.sin(2 * np.pi * q)

        energy, quad_error = quad(
            lambda t: float(metric(t) * velocity(t) ** 2), 0, 1,
            epsabs=1e-13, epsrel=1e-13,
        )
        next_coefficient = -7 * (8 * np.pi ** 3 * epsilon + 4 * eta) * cubic_exact / 12
        rows = []
        for m in (9, 33, 129, 513):
            q = profile(np.arange(m) / m)
            q1 = np.roll(q, -1)
            q2 = np.roll(q, -2)
            # Stable difference for S0, then differences of the nonlinear terms.
            quadratic = np.sum((q2 - q) ** 2 - (q1 - q) ** 2) / 8
            nonlinear = epsilon * np.sum(
                np.sin(2 * np.pi * q) * (np.cos(2 * np.pi * q1) - np.cos(2 * np.pi * q2))
            )
            oriented = eta * np.sum(q * q * (q1 - q2) - q * (q1 * q1 - q2 * q2))
            phase = float(quadratic + nonlinear + oriented)
            leading = 3 * energy / (2 * m)
            remainder = phase - leading
            # A deliberately coarse proven C^3 bound, not a fitted rate.
            assert abs(remainder) <= 2000 / (m * m)
            rows.append({
                "m": m, "phase": phase,
                "m_phase": m * phase, "target": 3 * energy / 2,
                "m_squared_remainder": m * m * remainder,
                "next_coefficient": float(next_coefficient),
            })
        # Discriminates an erroneous coefficient 1/2 or 3 from the correct 3/2.
        assert abs(rows[-1]["m_phase"] - 3 * energy / 2) < abs(energy) / 1000
        # The asymmetric fixture has a genuine m^-2 term.
        # The raw coefficient still has an O(1/m) discretization term.
        # Eliminate that term before checking the independent third-order coefficient.
        left, right = rows[-2:]
        extrapolated = (
            right["m"] * right["m_squared_remainder"]
            - left["m"] * left["m_squared_remainder"]
        ) / (right["m"] - left["m"])
        assert abs(extrapolated - next_coefficient) < 2e-5
        assert abs(next_coefficient) > 1e-5
        continuum_checks.append({
            "epsilon": epsilon, "eta": eta, "energy": energy,
            "quadrature_reported_error": quad_error, "rows": rows,
            "extrapolated_second_coefficient": extrapolated,
        })

    m, n, amplitude = 101, 100003, 0.02
    q = 1 / 3 + amplitude * np.cos(2 * np.pi * np.arange(m) / m)
    rounded = np.rint(n * q) / n
    doubled = rounded[(2 * np.arange(m)) % m]
    harmonic = np.exp(-2j * np.pi * np.arange(m) / m)
    old_coefficient = abs(np.mean(rounded * harmonic))
    new_coefficient = abs(np.mean(doubled * harmonic))
    assert old_coefficient >= amplitude / 2 - 1 / (2 * n)
    assert new_coefficient <= 1 / (2 * n) + 1e-14
    assert old_coefficient > new_coefficient
    return {
        "assertion_tested": "Finite Fourier/Hessian normalizations; nonlinear continuum phase fixture; nonrotation witness after rounding.",
        "coefficient_domain": "complex128, float64; exact symbolic identities separately checked with Wolfram",
        "software": [
            {"name": "Python", "version": platform.python_version()},
            {"name": "NumPy", "version": np.__version__},
            {"name": "SciPy", "version": scipy.__version__},
        ],
        "eigen_checks": eigen_checks,
        "continuum_checks": continuum_checks,
        "rounding_fixture": {
            "m": m, "N": n, "original_first_harmonic": float(old_coefficient),
            "permuted_first_harmonic": float(new_coefficient),
        },
        "non_claims": [
            "The nonlinear fixture is not the original U_N or its phase S_t.",
            "No finite computation at actual tau=10^-80.",
            "No contribution estimate for the full coherent sum.",
            "No proof or refutation of Sine_2 or of the full pair moment.",
        ],
        "development_note": "A first raw m=513 coefficient test used an unjustified 2e-4 tolerance before removing its O(1/m) term and failed. The final test uses the displayed Richardson extrapolation; the mathematical claim was not changed.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = verify()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "fourier_dimensions": len(result["eigen_checks"]),
        "continuum_fixtures": len(result["continuum_checks"]),
        "status": "finite checks passed",
    }, ensure_ascii=False))
```


### XI.10. trace005_critical_gaussian_verify.py

```python
"""Finite normalization checks for CG1--CG4, not a numerical Sine_2 test."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.integrate import quad


ZERO = (Q(0),) * 4
ONE = (Q(1), Q(0), Q(0), Q(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zpower(k):
    k %= 8
    ans = [Q(0)] * 4
    ans[k % 4] = Q(1 if k < 4 else -1)
    return tuple(ans)


def mul(a, b):
    ans = ZERO
    for j in range(4):
        for k in range(4):
            ans = add(ans, tuple(a[j] * b[k] * v for v in zpower(j + k)))
    return ans


def conjugate(a):
    ans = ZERO
    for j, v in enumerate(a):
        ans = add(ans, tuple(v * x for x in zpower(-j)))
    return ans


def frames():
    rows = []
    for nu in (1, 3, 5, 7):
        c = []
        for r in range(4):
            line = []
            for s in range(4):
                value = ZERO
                for x in range(4):
                    exponent = -nu * (3*x*x - 2*x*s + 3*s*s) - 2*r*x
                    value = add(value, tuple(v / 4 for v in zpower(exponent)))
                line.append(value)
            c.append(line)
        for s in range(4):
            for t in range(4):
                value = ZERO
                for r in range(4):
                    value = add(value, mul(conjugate(c[r][s]), c[r][t]))
                assert value == (ONE if s == t else ZERO)
        rows.append({"nu": nu, "exact_unitarity": True})
    return rows


def gaussian_mask(nsize, kappa):
    n = np.arange(nsize, dtype=np.int64)
    n = np.where(n <= nsize // 2, n, n - nsize)
    images = int(np.ceil(12 * kappa / np.sqrt(nsize))) + 2
    ans = sum(np.exp(-(n + j*nsize)**2 / (2*kappa*kappa*nsize))
              for j in range(-images, images+1))
    normalizer = sum(np.exp(-j*j*nsize / (2*kappa*kappa))
                     for j in range(-images, images+1))
    return ans / normalizer


def spectral_filter(nsize, mask):
    t = np.arange(nsize, dtype=np.int64)
    p = np.fft.fft(mask) / nsize
    chirp = np.exp(2j*np.pi*((2*t*t) % nsize) / nsize)
    return nsize * np.fft.ifft(p * chirp)


def cat(nsize):
    x = np.arange(nsize, dtype=np.int64)
    f = 3*x[:, None]**2 - 2*x[:, None]*x[None, :] + 3*x[None, :]**2
    return np.exp(2j*np.pi*((-pow(8, -1, nsize)*f) % nsize) / nsize) / np.sqrt(nsize)


def weyl(nsize, a, b):
    x = np.arange(nsize)
    result = np.zeros((nsize, nsize), complex)
    result[x, (x+a) % nsize] = np.exp(
        2j*np.pi*((b*(x + pow(2, -1, nsize)*a)) % nsize) / nsize)
    return result


def generator(nsize):
    q = np.arange(nsize) / nsize
    r = lambda u: (1 - np.cos(14*np.pi*u)) * (1 + np.cos(2*np.pi*u))
    d = np.cos(14*np.pi*q) + r(q)/10 + r(q)*np.sin(2*np.pi*q)/100 - .1
    z = (-3+4j)/5
    ans = np.diag(d.astype(complex))
    for x in range(nsize):
        coefficient = r(q[x] + .5 + 1/(2*nsize)) * np.conj(z) / 200
        ans[x, (x+1) % nsize] += coefficient
        ans[(x+1) % nsize, x] += np.conj(coefficient)
    assert np.max(np.abs(ans-ans.conj().T)) < 1e-14
    return ans


def arctan_partial(z, count):
    return sum(((-1)**j * z**(2*j+1) / (2*j+1) for j in range(count)), Q(0))


def verify():
    exact_frames = frames()
    p_lower = 16*arctan_partial(Q(1, 5), 10) - 4*(
        arctan_partial(Q(1, 239), 2) + Q(1, 5*239**5))
    p_upper = 16*(arctan_partial(Q(1, 5), 10)+Q(1, 21*5**21)) - 4*arctan_partial(Q(1, 239), 2)
    rational_lower = 2*p_lower/3-p_upper**3/21+p_lower**5/660-p_upper**7/37800
    assert rational_lower > Q(1001, 1000)
    # Exact tangent check for the Machin branch, using rational inputs only.
    tan2 = 2*Q(1, 5)/(1-Q(1, 5)**2)
    tan4 = 2*tan2/(1-tan2*tan2)
    assert tan4 == Q(120, 119)
    assert (tan4-Q(1, 239))/(1+tan4*Q(1, 239)) == 1

    matrix_checks = []
    for nsize in (9, 11, 13, 15):
        m = cat(nsize)
        v = weyl(nsize, -4, 2)
        z = np.diag(np.exp(2j*np.pi*np.arange(nsize)/nsize))
        identity_error = 0.
        for ell in (1, 2, -3):
            zl = np.linalg.matrix_power(z, ell)
            lhs = m.conj().T @ zl @ m @ zl.conj().T
            rhs = np.exp(2j*np.pi*((2*ell*ell) % nsize)/nsize) * np.linalg.matrix_power(v, ell)
            identity_error = max(identity_error, float(np.max(abs(lhs-rhs))))
        assert identity_error < 3e-13
        mask = gaussian_mask(nsize, 1)
        x = np.arange(nsize)
        direct = np.linalg.svd(m*mask[(x[:,None]-x[None,:]) % nsize], compute_uv=False)[0]
        via_weyl = np.max(abs(spectral_filter(nsize, mask)))
        assert abs(direct-via_weyl) < 3e-14
        matrix_checks.append({"N":nsize, "nu":(8*pow(8,-1,nsize)-1)//nsize,
                              "weyl_identity_error":identity_error,
                              "direct_norm":float(direct), "weyl_norm":float(via_weyl)})

    scale_checks = []
    for nsize in (63, 255, 1023, 4095, 16383):
        n = np.arange(nsize)
        centered = np.where(n <= nsize//2, n, n-nsize)
        for kappa in (.5, 1., 2., 4.):
            gaussian = gaussian_mask(nsize, kappa)
            value = np.max(abs(spectral_filter(nsize, gaussian)))
            target = (1+4/(np.pi**2*kappa**4))**(-.25)
            beta = np.pi**2*kappa**2/(2*(np.pi**2*kappa**4+4))
            alias_bound = 2*np.exp(-beta*nsize/4)/(1-np.exp(-beta*nsize))
            assert value <= target*(1+alias_bound) + 3e-13
            hard = (abs(centered) <= int(np.floor(2*np.sqrt(nsize)))).astype(float)
            hard_values = spectral_filter(nsize, hard)
            scale_checks.append({"N":nsize, "kappa":kappa,
                "gaussian_norm":float(value),"gaussian_limit":float(target),
                "hard_kappa2_norm":float(np.max(abs(hard_values))),
                "hard_kappa2_center":float(abs(hard_values[0]))})
    for row in scale_checks:
        if row["N"]==16383:
            assert abs(row["gaussian_norm"]-row["gaussian_limit"]) < 3e-12
            assert row["hard_kappa2_center"] > 1.25

    normal_form_checks = []
    for b in (.2, .25, 1/3):
        for xi in (0., .25, .5):
            integrand = lambda u: np.sqrt(b)*np.exp(-(.5+1j*np.pi*b)*u*u-2j*np.pi*xi*u)
            real = quad(lambda u: float(integrand(u).real),-12,12,epsabs=1e-13,epsrel=1e-13)[0]
            imag = quad(lambda u: float(integrand(u).imag),-12,12,epsabs=1e-13,epsrel=1e-13)[0]
            expected = np.sqrt(np.pi*b/(.5+1j*np.pi*b))*np.exp(-np.pi**2*xi**2/(.5+1j*np.pi*b))
            error = abs(real+1j*imag-expected)
            assert error < 1e-12
            normal_form_checks.append({"b":b,"xi":xi,"quadrature_error":float(error)})

    positive_time_checks = []
    for nsize in (19, 21, 31):
        a = generator(nsize)
        values, vectors = np.linalg.eigh(a)
        aux_time = 1e-6
        u = ((vectors*np.exp(1j*aux_time*nsize*values)) @ vectors.conj().T) @ cat(nsize)
        mask = gaussian_mask(nsize, 1)
        x = np.arange(nsize)
        filtered = u*mask[(x[:,None]-x[None,:]) % nsize]
        norm = np.linalg.svd(filtered, compute_uv=False)[0]
        assert norm < .96
        assert np.max(abs(u.conj().T@u-np.eye(nsize))) < 1e-12
        positive_time_checks.append({"N":nsize,"auxiliary_time":aux_time,"filtered_norm":float(norm)})

    return {
        "assertion_tested":"Exact Q(zeta_8) frame unitarity and rational sine certificate; finite Weyl identity; Gaussian/hard filter norms; constant-coefficient integral normalization; finite original matrix definitions at auxiliary time.",
        "software":[{"name":"Python","version":platform.python_version()},
                    {"name":"NumPy","version":np.__version__},
                    {"name":"SciPy","version":scipy.__version__}],
        "exact_frames":exact_frames,
        "rational_certificate":{"pi_lower":str(p_lower),"pi_upper":str(p_upper),
                                "sine_lower":str(rational_lower),"sine_lower_float":float(rational_lower)},
        "matrix_checks":matrix_checks,"scale_checks":scale_checks,
        "normal_form_checks":normal_form_checks,"positive_time_checks":positive_time_checks,
        "non_claims":["No computation tests original tau=10^-80 at asymptotic N.",
                      "Finite norms do not prove a norm limit.",
                      "CG1-CG4 have separate analytical proofs.",
                      "The Gaussian weighted sum is not the original coherent sum.",
                      "Sine_2 and the original pair moment remain unresolved."],
        "development_note":"An initial quadrature check failed its 1e-12 comparison because SciPy's default relative tolerance was left active; diagnostics showed reported quadrature errors above that threshold. Final quadrature explicitly sets both tolerances to 1e-13.",
    }


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    result=verify()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"finite checks passed","exact_frames":len(result["exact_frames"]),
                      "matrix_cases":len(result["matrix_checks"]),
                      "scale_cases":len(result["scale_checks"]),
                      "normal_form_cases":len(result["normal_form_checks"]),
                      "auxiliary_positive_time_cases":len(result["positive_time_checks"])}))
```


### XI.11. Независимый пересчёт определителей сертификатов

```python
from fractions import Fraction as Q
import json
from pathlib import Path


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i + 1, len(a)):
            factor = a[j][i] / value
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return result

checks = json.loads(Path("trace005_checks.json").read_text())
count = 0
for rows in checks["orbit_certificates"].values():
    for row in rows:
        assert determinant(row["T"]) in (Q(-1), Q(1))
        count += 1
assert count == 18
print("18 exact determinants are +1 or -1")
```


## XII. Происхождение и протокол проверки


Исходный математический источник: `TRACE005_prompt_GPT6.pdf`. Его исходные байты не изменялись. Все последующие файлы — результаты текущего диалога, а не новые внешние математические входы.


| Файл | SHA-256 |
|---|---|
| `TRACE005_prompt_GPT6.pdf` | `493a89935673fbd09f4f8903f0cfa3073d173229dd0b0b0f4936208e41299516` |
| `TRACE005_research_result.md` | `ac8399af055d77be1fb8e16526fee49bb010556cf8e418baab1846cc18905790` |
| `TRACE005_positive_tau_reflections.md` | `83285fd3c2dcc885cf272be5b549aca5579543272df0d874ac324ab29f6a2d16` |
| `TRACE005_global_method_audit.md` | `88fd9b5bb268c09a9ca9d5b5cbc59b1cc6bbd1cf1fea353232417bd0805cd359` |
| `TRACE005_resonance_analysis.md` | `c5215e6d5523410e6df5f5907bd6076e5179f9866bf9fd8a937003b1ac1e191d` |
| `TRACE005_twirl_bounds.md` | `efbe05e1b3d7dc5016352a20c8a99246d1f502a5ba1b560374f3ae638d7a6404` |
| `TRACE005_moment_criterion_audit.md` | `cb0163dd2235cfd847c02ce84b2868f5f0903ac86bf34ec29de397debfe79353` |
| `TRACE005_intensity_limit.md` | `c3d2278dd4d3bd8879a507207995a6afefff051c20b5054eeeeee1a740c46105` |
| `TRACE005_intensity_operator.md` | `8e2d66b589894a8bcbd2030ead590aba35c7483298407be0152fe92824675e14` |
| `TRACE005_algebraic_parameter.md` | `81d800f5ed33ee0c804616772f07b99633a8ee888ab5bd2377e3fd232f499c76` |
| `TRACE005_central_mechanism_attempt.md` | `7a27b8c68064fc2d24b8db6df1fd9c5d917f06d7553a7e5f49925d3dd0a7dd1b` |
| `TRACE005_soft_modes.md` | `5eb46f1c0aba75c36ebff76a7392d4abe8d61d3bf0879fea46f95377d1ea8086` |
| `TRACE005_critical_gaussian.md` | `95ef5ee1e7a2cb56d5771425370fe2437e25293592dbd08edad6ba9a084cbfd9` |
| `TRACE005_weight_reconstruction_attempt.md` | `355b41b2f8ffad39a3bbee545811abe9bdbfd1034f6624386a2df2e01d0aa70e` |
| `TRACE005_observation_frame_and_secular_test.md` | `82b98a19b7965f93d857e5a88caefdb61e72f8bbef10ef7ec65fd56388be8fe0` |
| `TRACE005_local_arithmetic_spectral_ratios.md` | `d00ac61b86d6a9b5e5ea4b1220e2181d27d448e39b105db8834f62f6d528cf27` |
| `TRACE005_quantitative_arithmetic.md` | `6e6632ff0f4789bbb803fe37c10b07919e6e316ea0c53365e9582b19ad0095a3` |
| `TRACE005_log_dispersion_and_ward.md` | `2109935e43bbaa7422d26a7fc63468dd97e66eb0377a7f96160473887d6c65ae` |
| `TRACE005_spectral_coupling_profile.md` | `2c264fc13cbcc63f6c6100c59d8172668db6793d47f7bc8f57602f7295851e9f` |
| `TRACE005_profile_whitening.md` | `fea2a2607e8bb3fb11aa2ec904e2073508cc863cde774b1a944c75cec6b8ac16` |
| `TRACE005_isospectral_gauge.md` | `4417f6b9e3d42825ca95b383f8713fc69f3121382cfd377c9865c1e749e0a119` |
| `TRACE005_positive_pair_resolvent.md` | `9fa7c93ef7ee008b57124fcd167465e1d4e362b4d102c849828fc72ee24028b8` |
| `TRACE005_full_classical_symmetry.md` | `71caa09b2c7b9bc68f1c4d505c4fdec688c37eefddb385ab01c512d007f0881a` |
| `TRACE005_quantum_resolution.md` | `4f463d37653f88d538e657f404ba25c0e1826471a5f7e9f95d93c804449be77f` |
| `trace005_verify.py` | `610a5aa18535d4e5b31fbff031e168af4510a90b98f14688b8f9bee90b1ac7a3` |
| `trace005_positive_tau_verify.py` | `803d135d511d5d658950822d8c6bbfd2f4dfa69c806efd42e962f87736dc78a5` |
| `trace005_resonance_verify.py` | `f0f0394519dce11cff9ef842df1a9a1eb7e615e7f6fff5b7873f7b02f41f813b` |
| `trace005_resonance_checks.json` | `e066d991d439cf3132770bfbd92ed00852909c142acada38117cd1a84cb0caf1` |
| `trace005_twirl_verify.py` | `ac92cc23a19216cf6f331642ddc72e3ae8ed40199ecd5a9f92320d95135f5e09` |
| `trace005_twirl_checks.json` | `1e92e1e1cc85993e1d6b6181fa4331b039b15f361a743c15fa6958d87df14ceb` |
| `trace005_twirl_self_review.json` | `23f0ec79c5644af06e20b2aa4b08d90a7cd99871622445b7bf89767bdba36483` |
| `trace005_moment_audit_verify.py` | `27a1a4dec706b1907cc6c3e7bc3c425aaf42ed9a05ba2d68f34202219705ef55` |
| `trace005_moment_audit_checks.json` | `64b4ead8f0d53450a11df6deb0714649a0f1c640c92bbd215a8f02064e3cfa3f` |
| `trace005_moment_audit_self_review.json` | `488aeb777f1da35c0c30193c547ac93cb88187379eb998b32b1ac822a008fba0` |
| `trace005_intensity_limit_verify.py` | `da401e1658bad9fc5efce92c4c734869da83d3dff074ced78d3fe45da394d789` |
| `trace005_intensity_limit_checks.json` | `a31c118f91f3251872160e1b4b505303a2a4c7168f571d7fd1c79090098054ac` |
| `trace005_intensity_limit_self_review.json` | `f07438da8be2ec4e9e72e81af747823bfe8db3e224c2e1c2be7b789bf609e07e` |
| `trace005_intensity_operator_verify.py` | `04fb7762fc8649b50c208389c255394168b85eea109b6bdb331300b9f8ab83f2` |
| `trace005_intensity_operator_checks.json` | `4ed1266487e239a0bc44f37ecdd762927ff0b9659d44c4f7a588a2ce45353412` |
| `trace005_intensity_operator_manifest.json` | `fd117e97ff30d1753d554d15f4b8598798949b31454c00eac42d8f8d409346e4` |
| `trace005_intensity_operator_self_review.json` | `20f3209cff8ba3001e9b7aa536f4b1f38bc13e506cbee12868ff943e0847e244` |
| `trace005_algebraic_parameter_verify.py` | `68002332c2c064f4bf2e0ca7ed7a33a96ef8e5d4f86cc93378c4cde48302a7ca` |
| `trace005_algebraic_parameter_checks.json` | `51fbf0e8c5a3159c85e6c4dc5573fbc1e1bcebee2028f8206a2d3a7e349355b4` |
| `trace005_algebraic_parameter_manifest.json` | `f63d1abc566afc492697df0b1a90939219569b5930c68aee9ec859516aae7271` |
| `trace005_algebraic_parameter_self_review.json` | `4f6e3c5a92387b46f22b6e9f6faf97afe89d12155dec5f7c8c8a7245d43ec7de` |
| `trace005_central_mechanism_checks.json` | `ea64df858d896e6e531adacd8e56f07a2b34c930e5b494914cb0fb12218096be` |
| `trace005_central_mechanism_self_review.json` | `8055a8600bdc26be51d50d4397714bf23f65f1a220dcaa2eac726fa5f9070e8b` |
| `trace005_soft_modes_verify.py` | `3894f303b51817710f52ecf0abf903d5fc340605e9a8b0f6afb2aecba17cc015` |
| `trace005_soft_modes_checks.json` | `938a3758fc1336ad94a887eb417579d3ca56c6254ea63aeb5f8e5eaa767b85f0` |
| `trace005_soft_modes_manifest.json` | `abbbfd980849149dbc77cbebac92d407bbee80946572f097f3ddfe07f9cbb9f2` |
| `trace005_soft_modes_wolfram.json` | `1e503f40bef30ed31b112b301bb4db57af94487089b574a8113e76477ff0f048` |
| `trace005_soft_modes_self_review.json` | `b529bcd8415a6cf4ab6e46f61561b4b950107a1ae8bc1f679d9493de4eaf18ca` |
| `trace005_critical_gaussian_verify.py` | `cf38ff629a931511c4ecaf2a0d5583c5445df90cccecec6b8605ad8a9d7fa707` |
| `trace005_critical_gaussian_checks.json` | `d31d8a0356c4cb6819cd003f9005b020a7a06271fa62fbe9c499960f0eeb4193` |
| `trace005_critical_gaussian_manifest.json` | `a70acc0d918534581624cfa9c28bc553530a5c68e08409c0a456394f0276f026` |
| `trace005_critical_gaussian_wolfram.json` | `a1c37886a1ecf908c085a5323b791f47118cef631499f74867c03b21bed58ad0` |
| `trace005_critical_gaussian_self_review.json` | `e1dd9e0817923b56660d4582ae11b255bd2e945866986951d49166d728be5642` |
| `trace005_weight_reconstruction_checks.json` | `83c4181bf0faef89e59327bbc9266408c7d4cf3463c22abf434065c3aa3a490b` |
| `trace005_weight_reconstruction_self_review.json` | `39cddcc717aed0ea4a446e100d04f8f07fc5551580fd3e4b07edf54afd539785` |
| `trace005_observation_frame_checks.json` | `ea50cd75014d7f04d3a77f0bedb8bd83f9bc8aebd296027a38df6e3ae98e4412` |
| `trace005_observation_frame_self_review.json` | `15f11186e04323b60f91515035ed9f10f3a87673c0e91804bdb6ad511d316e5a` |
| `trace005_local_arithmetic_checks.json` | `9ea658ad1567a7dc112ecedd8586f2a3d525adca18f2b10b6eb370442defdc42` |
| `trace005_local_arithmetic_self_review.json` | `13736d22ad5138fea1d1468ec44438c674eca4f8675c10bd7d03fa3abd02d398` |
| `trace005_quantitative_arithmetic_checks.json` | `ea770a6c39249ec947e85100e5fc12201d42e72eda9865576ac8c3c041764fcc` |
| `trace005_quantitative_arithmetic_self_review.json` | `672c969998e5ea27036b964bd41dfabf6f30ee58978ecb06798479d5f4e8350f` |
| `trace005_log_dispersion_checks.json` | `f75ea6d813e91b8c99a74af12b5cc7393608407c8f0828d328361b5c6df95f14` |
| `trace005_log_dispersion_self_review.json` | `0efc4af312cb22b0b715794b860fea2e45246f77cba3b565b0a63a75e41d7f6d` |
| `trace005_spectral_coupling_checks.json` | `b130d596fcb9efc3a4b9df6f932d56d8da4eebd503519416d4070f0882e7d877` |
| `trace005_spectral_coupling_self_review.json` | `62459ed84639a0b4c774b64fafbb2063b8947f1127d6c00b681358a833ca8cbf` |
| `trace005_profile_whitening_checks.json` | `b8de2d98e78dad25c96d1d5dfdbccb17ca56ed2f49c93eddadfb776bbc349fbe` |
| `trace005_profile_whitening_self_review.json` | `d91440c60beb6aa26218c95396a7156103d1f1b77cb02308e2f238614e4a66e3` |
| `trace005_isospectral_gauge_checks.json` | `3ef07c062b3ee168c8411eed7257c8d17446aa8ca3f3dd3cb6b683376eaaa033` |
| `trace005_isospectral_gauge_self_review.json` | `38c380cd3a102ed07f35a8e27d95a5b9276284bf93dfecaf8abb24898fe06c39` |
| `trace005_positive_pair_resolvent_checks.json` | `af92e2d14f84649615c5813fc636829526ee0da21441c264c3a6d0b884da734a` |
| `trace005_positive_pair_resolvent_self_review.json` | `997e547602b3b8008c9fbcc01efa584a188c83e27f4f69b44059bf8806a2b8f0` |
| `trace005_checks.json` | `45d2c7cea55b679e0ca034033ed0cd9495453baf25e5e36e7465bc6499138f5c` |
| `trace005_positive_tau_checks.json` | `1c44d4aa7a250406172e09775587aa16d3970e17fa2888427c848fc7aaad980b` |
| `trace005_final_self_review.json` | `0634790a737c7ddc8cf186124407e285e2cb0fab74f10561855feb03948db30c` |
| `trace005_periodic_symmetry_verify.py` | `6df7b0754037e73f9c4f5d6fb85171a23f79a8929fa51890c955af24758d5df0` |
| `trace005_full_classical_symmetry_checks.json` | `8951fb1e4d77d330240fd5a573c12bb6f7a93bef34460a6356a6fc7d7b37206c` |
| `trace005_full_classical_symmetry_manifest.json` | `3ace34935e595df1f928d5358cc512f1abd21c7ba1e1ec024ea10ac5a8049b90` |
| `trace005_full_classical_symmetry_self_review.json` | `140dcb1b428d5b5dd2c07cdc7d0aa2baa38da820a4485399a8ab5c95d511f0b7` |
| `trace005_quantum_resolution_checks.json` | `e43354a94b5189bfb7e8e94038ad9764ee8452e98861f118a7b92790fb4c8cc9` |
| `trace005_quantum_resolution_self_review.json` | `80b83fb03244c264ae2abafe5283aebfb3053bcbbb4fe1b9ee491b274b741c20` |


Для восьми первых основных вычислительных запусков сохранён статус `completed`, Python 3.12.14 и NumPy 2.3.5. Проверка манифестов с хешами завершилась успешно. Дополнительный аудит определителей охватил 2 сертификата при m=4, 4 при m=5 и 12 при m=6. В новом этапе точные циклические проекции проверены в 14 размерах; подстановка Кронекера и иллюстрация расщепления спектра проверены отдельно. Конечные Weyl-тождества нового этапа проверены в размерах 5, 9, 15; константы и первые 12 чисел ветвей классического отображения проверены точно. Новый аудит проверил 99 точных разбиений на цепочки, семь матричных размеров и конечные формулы парной энергии с исходным весом. В интенсивностном этапе точно проверены 64 арифметических коэффициента в поле восьмых корней из единицы и все 240 ненулевых первых фазовых коэффициентов. Все вычисления детерминированы; случайные семена не использовались. В доказательстве существования Z3 применяется вспомогательный вероятностный выбор другой семьи; исходная спектральная модель не рандомизируется.


Новый операторный этап проверен двумя независимыми конечными Fourier-выкладками и двумя четырёхшаговыми Lie-проходами; все 12 смешанных и диагональных первых фазовых коэффициентов проверены точно. Отдельно проверены 144 нормировочных тождества четвёртого следа в complex128 и полный перебор вращательных слов при N=3, m≤6 и N=5, m≤5. Предельный переход и теорема O5 следуют из приведённых аналитических и размерностных доказательств. Wolfram подтвердил рациональные S₀, T₀, след, определитель, квадрат следа и норму ведущего оператора.


Арифметический этап проверен точной гауссовой рациональной арифметикой: формальное произведение Галуа, положительный постоянный коэффициент, четыре монических и три немонических вспомогательных многочлена. Отрицательная проверка без множителя a^D действительно оставляет знаменатель. Условие интегрального остатка при p=503 проверено точно. Дополнительно проверены 108 циклотомических автоморфизмов и нормировки вторых производных исходных матриц в семи размерах. Трансцендентность и кванторы по всем N,m доказываются текстом; конечный запуск их не заменяет.


Попытка центрального механизма в VIIIc не привела к новой оценке исходной знаковой суммы. Общие утверждения VIIIc проверены линейно-алгебраически; отдельные конечные примеры подтверждены символьным вычислением в Wolfram. Код вызова приведён полностью в VIIIc.5; версия удалённого ядра сервисом не сообщена, и эта иллюстративная проверка не объявляется самостоятельным доказательством по всем N.


В новом этапе VIIId отдельно проверены Fourier-нормировки в четырёх нечётных длинах, дополнительные нулевые моды при m=9, три нелинейные контрольные фазы и округлённый невращательный профиль. Девятый Python-запуск завершился со статусом completed; его манифест проверен с хешами. Wolfram 15.0.1 независимо подтвердил точный парный гессиан; все входы и ответы, включая диагностические ошибки, сохранены в VIIId.5. SP4 и SP5 доказываются аналитически: почти совпадающие ветвевые фазы не отождествляются с фазами полных слов и не дают макроскопического веса.


Этап VIIIe проверен точной арифметикой Q(zeta_8) для четырёх рамок и рациональным сертификатом синусной нижней границы. Четыре конечных Weyl-тождества независимо сопоставлены с матрицами; 20 масштабных примеров, девять гауссовых квадратур и три исходные матрицы при вспомогательном времени проверяют нормировки. Десятый Python-запуск имеет статус completed и проверенный манифест. Предельная операторная оценка и все времена для взвешенного сектора доказываются текстом. Полные символьные входы и ответы, включая диагностические сообщения, сохранены в VIIIe.5.


Этап VIIIf не дал новой оценки исходного парного теста. Его конечные символьные проверки подтверждают точное восстановление и нормовые тождества в рациональном примере, оба направления изменения сглаженных следов в трёхмерных примерах и четыре целых размера Пелля. Все три Wolfram-входа и ответы приведены полностью. Для этих удалённых проверок не заявляется новый локальный манифест v2; общие выводы опираются на явные доказательства, а не на конечные значения.


Этап VIIIg проверен двумя исправленными hosted-вызовами Wolfram 15.0.1. Проекционные и крюковые формулы сопоставлены с рациональной матрицей; отсутствие корня проверено в трёх размерах. Конечнополевые формулы, Egorov, антисимметричная производная и гауссова норма проверены точно при p=5,7,11. Два диагностических запуска не используются как подтверждение; все четыре входа и ответа приведены полностью. Локальный v2-manifest для них не заявляется. OF2 и SC3 доказываются равномерными оценками, а не конечными проверками. Основной исходный парный тест остаётся открытым.


Этап VIIIh имеет десять сохранённых hosted-вызовов Wolfram 15.0.1: шесть текущих успешных конечных проверок, три диагностических входа без доказательной роли и один заменённый усиленной проверкой первоначальный вход. Исходная цепочка проверена точно при N=3,5,9,11; N=7 проверяет нарушение гипотезы. Разветвление простого 5 и баланс Вандермонда проверены в отдельных порядках и на 3200 наборах строк при N=15,25. В исходном N=3 ненулевость диагональных сжатий дополнительно подтверждена точным результантом. Все временные формулы TV1 проверены при p=3,5,7 до времени 2p. Общие утверждения AP1–AP6 и TV1 следуют из текста. Независимого рецензирования, нового локального v2-manifest для hosted-вызовов и доказательства основного парного предела не заявляется.


Этап VIIIi имеет шесть сохранённых hosted-вызовов Wolfram 15.0.1. Два текущих точных входа проверяют знаменатель 4000, десять произведений всех ненулевых связей, пять общих кофакторов и все семь непустых миноров отдельной трёхмерной модели. Проекторная формула независимо сопоставлена с явным ортонормированным собственным базисом, симметрические целые произведения вычислены точно. Три диагностических входа не используются как подтверждение; один промежуточный вход заменён усиленным. Самопроверка AQ1–AQ6 прошла 26 обязательств и явно оставила два исходных вопроса нерешёнными. Локальный v2-manifest не заявляется; универсальные оценки следуют из текста, а не конечных вызовов.


В VIIIj выполнены семь hosted-вызовов Wolfram 15.0.1: четыре первоначальных и три полных повтора. Первоначальная неполнота записи обнаружена до сохранения, все текущие корректные проверки повторены с сохранением полных входов и ответов; исходные записи с отсутствующим MCP-объектом помечены по протоколу диалога. Проверены пять тождеств Фейера, 1568 диагональных Weyl-элементов в четырёх нечётных модулях, Ward-формулы и спектральный якобиан в рациональных моделях размеров 2 и 3, а также два отрицательных случая. Нецентральные плоские степени в трёх конечных полях проверены до половины периода; центральное неплоское время отдельно отвергнуто. Самопроверка LD1–LD6 прошла 29 обязательств и оставила два главных вопроса открытыми. Новый локальный v2-manifest не заявляется. Универсальные оценки дисперсии и собственных векторов доказываются явными неравенствами по всем нечётным N.


В VIIIk выполнены два полных hosted-вызова Wolfram 15.0.1, каждый вход и ответ записан непосредственно после выполнения. Fourier-масса, семь линейных корреляций и два перекрытия проверены в Weyl-правиле; независимый расчёт исходных T-коэффициентов выполнен в восьми нечётных размерах. Общий диапазон утверждался только при N≥41; N=7 отдельно подтверждает нарушение наивного расширения. Самопроверка CW1–CW4 прошла 19 обязательств, основной парный тест и высшие порядки оставлены открытыми. Новый локальный v2-manifest не заявляется; универсальные выводы следуют из текста.


В VIIIl выполнены четыре hosted-вызова Wolfram 15.0.1: один диагностический заменён исправленным, три текущих корректных сохранены с полными входами и ответами. Проверены частотная диагонализация, точный Tr S^18, рациональные константы, ряд обратного квадратного корня и отрицательный случай с одним множителем фильтра. Рациональная трёхмерная модель подтверждает девять весов, пять свёрток и пять базисных следов. Самопроверка PW1–PW5 прошла 28 обязательств; три главных микроскопических обязательства оставлены открытыми. Новый локальный v2-manifest не заявляется. Все классические времена и бесконечный фильтр доказываются текстом, конечные ответы их не подменяют.


В VIIIm выполнены четыре полных hosted-вызова Wolfram 15.0.1. Проверены 24 рациональных сравнения констант, точный след S^18, девять фильтрованных элементов, по три тождества ускорения и кривизны и три проецированных коммутаторных равенства. Фактический Weyl-символ проверен по 32 меткам; классификация всех аффинных матриц доказывается по поддержке. Отрицательная рациональная модель запрещает точное общее удаление производной и не противоречит специальной асимптотической оценке SG6. Самопроверка прошла 40 обязательств, три главных вопроса оставлены открытыми. Новый локальный v2-manifest не заявляется; все равномерные кванторы, нормальная форма и сила 1/(10N) следуют из текста. Контрольный движущийся параметр на исходной линейно-резонансной подпоследовательности использует доказанную проектную периодичность; фиксированный tau им не заменяется.


В VIIIn выполнены шесть полных hosted-вызовов Wolfram 15.0.1, пять текущих корректных и один диагностический с предупреждениями, заменённый чистым рациональным расчётом. Проверены три одинаковых резольвентных следа в пяти моделях размеров 1,2,3, размеры ядра, 12 положительных полиномиальных сертификатов, два разложения избытка, точная верхняя огибающая и случаи её равенства. CUE-ряд, Cauchy-керн и обратная хордовая энергия проверены символьно. Самопроверка прошла 38 обязательств, три главных вопроса оставлены открытыми. Новый локальный v2-manifest не заявляется; все универсальные утверждения и прямая оценка исходной суммы порядка N/log N доказываются текстом. Представление положительным оператором не подменяет недоказанный резольвентный предел.


В VIIIo выполнены пять полных hosted-вызовов Wolfram 15.0.1: три текущих чистых, синтаксически ошибочный третий и четвёртый с предупреждениями оставлены диагностическими и заменены пятым. Прямое дифференцирование исходного Weyl-символа проверяет 16 обращающих классов, 16 коммутирующих классов, 11 точных периодических значений и константы. Самостоятельный локальный точный скрипт проверяет все 32 и 196 точек двух периодов в циклотомических полях; текущий v2-manifest со статусом completed валидирован с проверкой хешей. Python-скрипт и полный результат встроены в VIIIo. Самопроверка прошла 34 обязательства; три главных спектральных вопроса не закрыты. C¹-классификация и равномерный по t остаток следуют из текстового доказательства. Она не объявляется доказательством квантового Sine₂.


В VIIIp выполнены четыре полных чистых hosted-вызова Wolfram 15.0.1. Проверены HS-производные по двум формулам, положительное некоммутирующее сравнение рациональных форм, сжатие интенсивностей, конечные диадические различия, константа повторных слов, контрольный компактный вес и нечётные димерные конфигурации. Две неунитарные модели проверяют прямые следовые и Cauchy-границы. Самопроверка прошла 45 обязательств, три главных вопроса не закрыты. Нового локального научного численного запуска и v2-manifest не заявляется. Все универсальные масштабы, исходный O(N⁻²)-перенос и вспомогательная семья с тем же фиксированным F_tau доказываются текстом; основная квантовая матрица не заменяется при выводе статуса цели.


Внешние научные источники для доказательств не привлекались. Wolfram использован как дополнительная символическая проверка; результаты предельных переходов опираются на приведённые оценки, а не на ответ вычислительного сервиса.


Формат Markdown: формулы вынесены в явные математические фрагменты, полученные из исходных LaTeX-границ. В итоговом файле проверены 5475 таких фрагментов. Их количество сверено с деревом Markdown; математический синтаксис проверен компилятором XeLaTeX с жёстким завершением при ошибке. Отдельная намеренно испорченная формула проверяет, что эта проверка действительно отклоняет ошибку. Встроенные блоки Python проверены синтаксическим анализатором. Это проверка исходного Markdown и TeX-синтаксиса, а не подтверждение отображения в конкретном интерфейсе KaTeX; экран целевого приложения не инспектировался.


Итоговый статус основной задачи остаётся: **не доказана и не опровергнута**. Полный свод содержит как положительные результаты, так и точные причины, по которым они пока не образуют общего решения.
