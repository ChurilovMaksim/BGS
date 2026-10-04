#!/usr/bin/env python3
"""Independent finite controls for TRACE-012, not an asymptotic map estimate.

Integer/Fraction convex counts; SymPy series and matrix powers; complex128
Fourier vs direct Gaussian sums and discrete convolution inequalities.
Caps: <=81 phases in direct sums, <=6561 in strict-family occupancies,
<=419904 FFT cells, no Monte Carlo, no kick rounded to I.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
A, B = 1/8, 1/4


def norm2(f):
    return float(np.mean(np.abs(f)**2))**.5


def bump(x, lo=A, hi=B):
    u = (2*np.asarray(x)-lo-hi)/(hi-lo)
    z = 1-u*u
    out = np.zeros_like(z, dtype=float)
    mask = z > 0
    out[mask] = np.exp(-1/z[mask])
    return out


def modes(cells):
    return np.rint(np.fft.fftfreq(cells)*cells).astype(np.int64)


def project(f, d):
    assert len(f)%d == 0
    freq = modes(len(f))
    return np.fft.ifft(np.fft.fft(f)*(freq%d == 0))


def convolution(f, g):
    return np.fft.ifft(np.fft.fft(f)*np.fft.fft(g))/len(f)


def close(x, y, tol=3e-10):
    assert abs(x-y) <= tol*(1+abs(x)+abs(y)), (x, y)


def direct_density(phases, n, cells):
    x = np.arange(cells)/cells
    rho = np.zeros(cells)
    for phase in phases:
        # Centered circular distance; all omitted images have |N*t|>=2N.
        dist = (x+phase+.5)%1-.5
        for image in (-2,-1,0,1,2):
            rho += np.sqrt(np.pi)*np.exp(-np.pi**2*(n*(dist+image))**2)
    return rho


def finite_fourier_controls():
    rows = []
    for n in (17,31,81):
        for d in (1,2,3,7):
            for variant in (0,1):
                cells = 32*n*d
                x = np.arange(cells)/cells
                if variant == 0:
                    j = np.arange(n)
                    phases = (j/n+.11*np.sin(2*np.pi*j/n)/n)%1
                else:
                    phases = np.r_[np.arange(n-5)/(n-5), np.zeros(5)]
                rho = direct_density(phases,n,cells)
                freq = modes(cells)
                # Direct traces only at relevant frequencies; Gaussian
                # density coefficients are independently obtained in space.
                rhohat = np.fft.fft(rho)/cells
                active = np.arange(math.ceil(A*n),math.floor(2*B*n)+1)
                traces = np.exp(2j*np.pi*np.outer(active,phases)).sum(axis=1)
                err = float(np.max(np.abs(rhohat[active]-
                            np.exp(-(active/n)**2)*traces/n)))
                assert err < 3e-12
                E = float(np.sum(np.abs(traces[active%d == 0])**2)/n**2)
                Q = float(np.sum(np.abs(traces)**2)/n**2)
                square = rho*rho
                psquare = project(square,d)
                G = norm2(psquare)**2
                allm = np.arange(-8*n,8*n+1)
                alltraces = np.exp(2j*np.pi*np.outer(allm,phases)).sum(axis=1)
                gaussian_coeff = np.exp(-(allm/n)**2)*alltraces/n
                squared_coeff = np.convolve(gaussian_coeff,gaussian_coeff)
                squared_modes = np.arange(-16*n,16*n+1)
                G_from_traces = float(np.sum(np.abs(squared_coeff[squared_modes%d == 0])**2))
                close(G,G_from_traces)
                shifts = sum(np.mean(square*np.roll(square,-h*cells//d))
                             for h in range(d))/d
                close(G,shifts)
                direct_p = sum(np.roll(square,-h*cells//d)
                               for h in range(d))/d
                assert np.max(np.abs(psquare-direct_p)) < 1e-10
                assert 1-1e-9 <= np.mean(rho*rho)**2 <= G+1e-8
                assert G <= np.mean(rho**4)+1e-8
                assert Q <= math.exp(8*B*B)*G**.5+1e-9

                # Separable smooth complex weights, with nonzero phase
                # modulations. The constant uses actual discrete kernel L1.
                w = [bump(freq/n)*np.exp(2j*np.pi*.37*freq/n),
                     bump(freq/n)*np.exp(-2j*np.pi*.23*freq/n),
                     bump(freq/n,A,2*B)*np.exp(2j*np.pi*.19*freq/n)]
                F, kernels, constants, probs = [], [], [], []
                for filt in w:
                    multiplier = np.zeros(cells,dtype=complex)
                    support = filt != 0
                    multiplier[support] = filt[support]*np.exp((freq[support]/n)**2)
                    ker = np.fft.ifft(cells*multiplier)
                    const = float(np.mean(np.abs(ker)))
                    prob = np.abs(ker)/const
                    f = np.fft.ifft(cells*multiplier*rhohat)
                    close(norm2(f-convolution(ker,rho)),0)
                    major = const**2*convolution(prob,square).real
                    assert np.min(major-np.abs(f)**2) > -2e-10
                    F.append(f);kernels.append(ker);constants.append(const);probs.append(prob)
                P = [project(f,d) for f in F]
                c1,c2,c3 = constants
                for u,v in ((0,1),(0,2),(1,2)):
                    assert norm2(project(F[u]*np.conj(F[v]),d)) <= constants[u]*constants[v]*G**.5+1e-9
                    assert norm2(P[u]*np.conj(P[v])) <= constants[u]*constants[v]*G**.5+1e-9
                strips = [np.mean(P[0]*F[1]*np.conj(F[2])),
                          np.mean(F[0]*P[1]*np.conj(F[2])),
                          np.mean(F[0]*F[1]*np.conj(P[2]))]
                intersection = np.mean(P[0]*P[1]*np.conj(P[2]))
                via_integral = sum(strips)-2*intersection
                I = np.arange(math.ceil(A*n),math.floor(B*n)+1)
                direct = 0j
                absolute_sum = 0.
                for m in I:
                    for j in I:
                        flags = (m%d == 0,j%d == 0,(m+j)%d == 0)
                        assert int(any(flags)) == sum(flags)-2*int(all(flags))
                        if any(flags):
                            val = w[0][m]*w[1][j]*np.conj(w[2][m+j])
                            val *= traces[m-active[0]]*traces[j-active[0]]*np.conj(traces[m+j-active[0]])/n**3
                            direct += val;absolute_sum += abs(val)
                close(via_integral,direct)
                constant = (3*np.max(np.abs(w[0]))*c2*c3+
                            np.max(np.abs(w[1]))*c1*c3+
                            np.max(np.abs(w[2]))*c1*c2)
                assert abs(direct) <= constant*(E*G)**.5+1e-9
                rows.append({'N':n,'d':d,'variant':variant,'cells':cells,
                             'E':E,'G':G,'G_from_direct_trace_convolution':G_from_traces,
                             'density_fourier_max_error':err,
                             'signed_union':[direct.real,direct.imag],
                             'absolute_summand_sum':absolute_sum,
                             'proved_grid_bound':constant*(E*G)**.5})
    return rows


def density_from_traces(n,d,trace_function,cells):
    assert cells%d == 0
    freq = modes(cells)
    coeff = np.exp(-(freq/n)**2)*trace_function(freq)/n
    rho = np.fft.ifft(cells*coeff).real
    assert np.min(rho) > -1e-9
    return rho


def strict_family():
    rows = []
    for L in (3,5,7,9):
        n,d,K = L**4,L**3,L**2
        H = n-K
        rho = density_from_traces(n,d,lambda m:K+H*(m%H == 0),64*n)
        G = norm2(project(rho*rho,d))**2
        lo,hi = math.ceil(A*n),math.floor(2*B*n)
        count = hi//d-(lo-1)//d
        E = Fraction(count*K*K,n*n)
        occ = np.zeros(n,dtype=np.int64)
        np.add.at(occ,np.arange(H,dtype=np.int64)*n//H,1)
        occ[0] += K
        M4 = Fraction(sum(int(v)**4 for v in occ),n)
        assert M4 >= Fraction(K**4,n)
        clock = density_from_traces(n,d,lambda m:H*(m%H == 0),64*n)
        kernel = density_from_traces(n,d,lambda m:np.ones_like(m),64*n)
        # A bound derived from positivity and the triangle inequality,
        # rather than fitting an unproved universal constant to these rows.
        major_bound = (2*np.max(clock)**2+2*K*K*norm2(project(kernel**2,d)))**2
        assert G <= major_bound+1e-8
        I = np.arange(math.ceil(A*n),math.floor(B*n)+1)
        m,j = I[:,None],I[None,:]
        union = (m%d == 0)|(j%d == 0)|((m+j)%d == 0)
        weight = bump(m/n)*bump(j/n)
        Z = float(np.sum(weight*union)*K**3/n**3)
        Y = float(np.sum(weight*union*(K**3-3*K*K+2*(m+j)))/n**3)
        rows.append({'L':L,'N':n,'d':d,'K':K,'E':str(E),'M4':str(M4),
                     'E_M4':str(E*M4),'G':G,'E_G':float(E)*G,
                     'positive_kernel_bound':float(major_bound),
                     'signed_cubic':Z,'factorial_cubic':Y})
    assert rows[-1]['E_G'] < rows[0]['E_G']
    return rows


def same_block_lifts():
    rows = []
    c4 = math.pi**1.5/2
    for n,d in ((81,3),(625,5),(2401,7)):
        cells = 64*n
        concentrated = density_from_traces(n,d,lambda m:np.full_like(m,n),cells)
        balanced = density_from_traces(n,d,lambda m:n*(m%d == 0),cells)
        Gc = norm2(project(concentrated**2,d))**2
        Gb = norm2(project(balanced**2,d))**2
        close(Gc,c4*n**3/d)
        close(Gb,c4*n**3/d**3)
        close(Gc/Gb,d*d)
        # Exact density-fold identity with C=I and R=N/d.
        folded = np.zeros(cells)
        dist = ((d*np.arange(cells)+cells//2)%cells-cells//2)/cells
        for v in (-2,-1,0,1,2):
            folded += (n/d)*np.sqrt(np.pi)*np.exp(-np.pi**2*(n/d)**2*(dist+v)**2)
        assert np.max(np.abs(project(concentrated,d)-folded)) < 2e-9
        centered = ((np.arange(cells)+cells//2)%cells-cells//2)/cells
        positive_concentrated = np.zeros(cells)
        for image in (-2,-1,0,1,2):
            positive_concentrated += n*np.sqrt(np.pi)*np.exp(-np.pi**2*(n*(centered+image))**2)
        assert np.max(np.abs(concentrated-positive_concentrated)) < 2e-9
        root_branches = np.array([np.roll(positive_concentrated,-h*cells//d)
                                  for h in range(d)])
        imbalance = d*np.sum(root_branches**2,axis=0)/np.maximum(np.sum(root_branches,axis=0)**2,1e-300)
        # Skip Gaussian underflow cells; the energy identity itself has
        # no division and is checked on every cell.
        close(np.mean((np.mean(root_branches**2,axis=0))**2),Gc)
        live = np.sum(root_branches,axis=0) > 1e-100
        assert np.max(imbalance[live]) <= d+1e-10
        assert np.min(imbalance[live]) >= 1-1e-10
        rows.append({'N':n,'d':d,'G_concentrated':Gc,'G_balanced':Gb,
                     'ratio':Gc/Gb,'same_block':'C=I exactly; distinct root allocations'})
    return rows


def compositions(k,d):
    if d == 1:
        yield (k,)
    else:
        for j in range(k+1):
            for rest in compositions(k-j,d-1):
                yield (j,)+rest


def scalar_phase_controls():
    rows = []
    for n,d in ((17,3),(31,7)):
        cells = 32*n*d
        phases = np.arange(n)/n+.071*np.cos(np.arange(n))/n
        scalar_turns = .137
        rotated = (phases-scalar_turns/d)%1
        rho = direct_density(phases,n,cells)
        rotated_rho = direct_density(rotated,n,cells)
        G = norm2(project(rho*rho,d))**2
        rotated_G = norm2(project(rotated_rho**2,d))**2
        close(G,rotated_G)
        x = np.arange(cells)/cells
        folded = np.zeros(cells)
        R = n/d
        for phase in rotated:
            centered = (d*x+d*phase+.5)%1-.5
            for image in (-2,-1,0,1,2):
                folded += np.sqrt(np.pi)*np.exp(-np.pi**2*(R*(centered+image))**2)/d
        error = float(np.max(np.abs(project(rotated_rho,d)-folded)))
        assert error < 2e-10
        active = np.arange(math.ceil(A*n),math.floor(2*B*n)+1)
        active = active[active%d == 0]
        orig = np.exp(2j*np.pi*np.outer(active,phases)).sum(axis=1)
        new = np.exp(2j*np.pi*np.outer(active,rotated)).sum(axis=1)
        close(float(np.sum(abs(orig)**2)),float(np.sum(abs(new)**2)))
        rows.append({'N':n,'d':d,'scalar_turns':scalar_turns,'G':G,
                     'rotated_G':rotated_G,'block_fold_max_error':error})
    return rows


def falling(k,r):
    return math.prod(range(k-r+1,k+1)) if k >= r else 0


def exact_crowding():
    allocation_cases = 0
    minima = []
    for d in range(1,5):
        for K in range(15):
            allocs = list(compositions(K,d))
            for r in range(2,6):
                t,s = divmod(K,d)
                balanced = (d-s)*falling(t,r)+s*falling(t+1,r)
                vals = [sum(falling(k,r) for k in row) for row in allocs]
                assert min(vals) == balanced
                lower = Fraction(max(K-(r-1)*d,0)**r,d**(r-1))
                assert balanced >= lower
                allocation_cases += len(vals)
                minima.append({'d':d,'K':K,'r':r,'minimum':balanced,'Jensen':str(lower)})
    S = sp.Matrix([[3,4],[2,3]])
    s7 = S**7
    assert sp.isprime(239) and s7.applyfunc(lambda x:x%239) == sp.eye(2)
    assert S.applyfunc(lambda x:x%239) != sp.eye(2)
    balanced = 6*falling(34,3)+falling(35,3)
    assert balanced == 254694
    eps = Fraction(13*239**2,25*10**80)
    finite_cue_bound = Fraction(3,5)*Fraction(22,7)**6*eps**8
    assert finite_cue_bound < Fraction(1,10**600)
    return {'allocation_cases':allocation_cases,'balanced_minimum_cases':len(minima),
            'scope':'All K=0..14, d=1..4, r=2..5, all weak compositions.',
            'actual_prime_certificate':{'p':239,'d':7,'S7':[list(map(int,row)) for row in s7.tolist()],
                'exact_balanced_cubic_lower':str(Fraction(balanced,239)),
                'Jensen_cubic_lower':str(Fraction(225**3,239*49)),
                'epsilon_upper':str(eps),
                'finite_CUE_cubic_upper_less_than':'10**(-600)',
                'finite_CUE_bound_certificate':'(3/5)*(22/7)**6*epsilon**8 < 10**(-600), exact Fraction',
                'method':'Analytic operator-norm telescope at the actual tau; no floating-point kick.'}}


def sine_reference():
    z,u,v,t = sp.symbols('z u v t',real=True)
    def truncated(x):
        return sum((-1)**k*(sp.pi*x*z)**(2*k)/sp.factorial(2*k+1) for k in range(4))
    aa,bb,cc = truncated(u),truncated(v),truncated(u-v)
    expression = 1-aa**2-bb**2-cc**2+2*aa*bb*cc
    expanded = sp.expand(expression)
    assert all(expanded.coeff(z,k) == 0 for k in range(6))
    leading = sp.factor(expanded.coeff(z,6))
    assert sp.simplify(leading-sp.pi**6*u*u*v*v*(u-v)**2/135) == 0
    integral = sp.integrate(u*u*v*v*(u-v)**2,(u,-1,1),(v,-1,1))
    assert integral == sp.Rational(8,15)
    gram = sp.Matrix(3,3,lambda i,j:sp.integrate(t**(i+j),(t,-sp.Rational(1,2),sp.Rational(1,2))))
    assert gram.det() == sp.Rational(1,2160)
    points = np.linspace(-2,2,33)
    cases = 0
    for x in points:
        for y in points:
            pos = np.array([0.,x,y])
            determinant = float(np.linalg.det(np.sinc(pos[:,None]-pos[None,:])))
            bound = 9/8*math.pi**6*x*x*y*y*(x-y)**2
            assert -1e-12 <= determinant <= bound+1e-12
            cases += 1
    finite_cases = 0
    for h in (2,3,7,17):
        frequencies = (np.arange(h)-(h-1)/2)/h
        for x in points[::2]:
            for y in points[::2]:
                pos = np.array([0.,x,y])
                vectors = np.exp(2j*np.pi*np.outer(pos,frequencies))
                finite_gram = vectors@vectors.conj().T/h
                determinant = np.linalg.det(finite_gram)
                assert abs(determinant.imag) < 1e-12
                bound = 9/8*math.pi**6*x*x*y*y*(x-y)**2
                assert -1e-12 <= determinant.real <= bound+1e-12
                finite_cases += 1
    return {'leading_density':str(leading),'cube_vandermonde_integral':str(integral),
            'moment_determinant':str(gram.det()),'global_cube_coefficient':'3*pi**6/5',
            'numeric_Gram_bound_cases':cases,'finite_CUE_Gram_cases':finite_cases}


def duhamel_controls():
    identity = np.eye(2,dtype=complex)
    pauli_z = np.diag([1.,-1.]).astype(complex)
    pauli_x = np.array([[0.,1.],[1.,0.]],dtype=complex)
    rows = []
    for count in (2,3,5):
        generators = [np.cos(.7*j)*pauli_z+np.sin(.7*j)*pauli_x for j in range(count)]
        for t in (.1,.7):
            exact = identity.copy()
            for gen in generators:
                exact = exact@(math.cos(t)*identity+1j*math.sin(t)*gen)
            for degree in (0,1,2,4):
                coeffs = [identity.copy()]+[np.zeros((2,2),dtype=complex) for _ in range(degree)]
                for gen in generators:
                    factors = [((1j*t)**k/math.factorial(k))*np.linalg.matrix_power(gen,k)
                               for k in range(degree+1)]
                    coeffs = [sum((coeffs[k-j]@factors[j] for j in range(k+1)),
                                  np.zeros((2,2),dtype=complex)) for k in range(degree+1)]
                error = float(np.linalg.norm(exact-sum(coeffs),ord=2))
                bound = (count*t)**(degree+1)/math.factorial(degree+1)
                assert error <= bound+1e-12
                rows.append({'kicks':count,'t':t,'degree':degree,'error':error,'unitary_remainder_bound':bound})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    paths = ['mathematics/folded_quadratic_resonance_control.md',
             'computations/verification/folded_quadratic_audit.py']
    data = {'schema':'bgs-folded-quadratic-audit-v1','status':'PASS',
            'arithmetic':['integer/Fraction','SymPy exact algebra','complex128 FFT and Gaussian sums'],
            'runtime':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'Fourier_product_controls':finite_fourier_controls(),
            'strict_improvement':strict_family(),'same_block_root_controls':same_block_lifts(),
            'common_scalar_phase_controls':scalar_phase_controls(),
            'crowding':exact_crowding(),'sine_reference':sine_reference(),
            'noncommuting_Duhamel_controls':duhamel_controls(),
            'non_claims':['finite checks establish an asymptotic theorem',
                          'actual-map E or G asymptotic estimates','BGS solution',
                          'weak-process counterexample from factorial mass',
                          'external referee, Lean analytic certification or priority']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS folded quadratic:',len(data['Fourier_product_controls']),
          'Fourier/product cases;',data['crowding']['allocation_cases'],'exact allocations')


if __name__ == '__main__':
    main()
