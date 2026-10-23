#!/usr/bin/env python3
"""Independent finite audit controls, not a probability or asymptotic proof.

Exact arithmetic: fractions on a 64 by 64 normalized Walsh unitary.
Floating arithmetic: numpy complex128 on two explicitly generated unitaries.
No repository proof/verifier is imported. Seed and coverage are fixed below.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parent
INPUTS = [
    ROOT / 'global_feedback_flatness_candidate_20261013.md',
    ROOT / 'two_step_stopped_concentration_candidate_20261013.md',
]


def exact_walsh():
    n = 64
    s = [[F((-1) ** ((i & j).bit_count()), 8) for j in range(n)] for i in range(n)]
    p = [[x*x for x in row] for row in s]
    delta = F(1, 64)
    row_results, pair_results = [], []
    row_expansion_count = pair_expansion_count = 0
    for i in [0, 13]:
        ri = sum(x*x for x in p[i])
        ai = F(1, n)
        sums = [F(0) for _ in range(6)]
        mean_sum = F(0)
        phase_squares = {1: F(0), -1: F(0)}
        for e in range(n):
            keep = [j for j in range(n) if j != e]
            r = p[i][e]**2
            aa = bb = cc = dd = ff = F(0)
            for j in keep:
                x = p[i][j]
                alpha = s[i][e]*s[e][j]*s[i][j]
                b = p[i][e]*p[e][j]
                aa += 2*x*alpha
                bb += 4*x*b
                cc += alpha**2
                dd += 2*alpha*b
                ff += b*b
            for k, value in enumerate([r, aa, bb, cc, dd, ff]):
                sums[k] += value*value
            if e == i:
                continue
            a = s[e][e]
            d = 1-a*a
            mean = -r + bb/d + 2*a*dd/d**2 + (1+a*a)*ff/d**3
            mean_sum += mean
            direct_mean = -r
            for j in keep:
                x = p[i][j]
                alpha = s[i][e]*s[e][j]*s[i][j]
                b = p[i][e]*p[e][j]
                direct_mean += 4*x*b/d + 4*a*alpha*b/d**2 + (1+a*a)*b*b/d**3
            assert direct_mean == mean
            for w in [1, -1]:
                q = F(w)/(1-a*w)
                direct = sum((s[i][j]+q*s[i][e]*s[e][j])**4 for j in keep)-ri
                expanded = -r+2*q*aa+q*q*bb+2*q*q*cc+2*q**3*dd+q**4*ff
                assert direct == expanded
                phase_squares[w] += direct*direct
                row_expansion_count += 1
        bounds = [delta**2*ri, 10*delta**2*ri, 16*delta**2*ai,
                  delta**2*ai, 4*delta**3*ai, delta**4*ri]
        assert all(a <= b for a, b in zip(sums, bounds))
        assert mean_sum/n <= -ri/F(3*n)+F(5,n*n)+delta**2/n
        assert all(v <= 3500*delta**2*(ri+ai) for v in phase_squares.values())
        row_results.append({'row': i, 'coefficient_squared_sum_ratios': [str(a/b) for a,b in zip(sums,bounds)],
                            'uniform_port_phase_mean': str(mean_sum/n)})
    for i, j in [(0, 0), (0, 13), (13, 13)]:
        kij = F(1,n)
        phase_squares = {1:F(0), -1:F(0)}
        for e in range(n):
            if e in [i,j]:
                continue
            keep = [k for k in range(n) if k != e]
            a = s[e][e]
            r = p[i][e]*p[e][j]
            aa = bb = cc = dd = ff = F(0)
            for k in keep:
                x, y = p[i][k], p[k][j]
                alpha, beta = s[i][e]*s[e][k]*s[i][k], s[k][e]*s[e][j]*s[k][j]
                b, d = p[i][e]*p[e][k], p[k][e]*p[e][j]
                aa += y*alpha+x*beta
                bb += x*d+y*b+2*alpha*beta
                cc += alpha*beta
                dd += alpha*d+beta*b
                ff += b*d
            for w in [1,-1]:
                q = F(w)/(1-a*w)
                direct = sum((s[i][k]+q*s[i][e]*s[e][k])**2
                             *(s[k][j]+q*s[k][e]*s[e][j])**2 for k in keep)-kij
                expanded = -r+2*q*aa+q*q*bb+2*q*q*cc+2*q**3*dd+q**4*ff
                assert direct == expanded
                phase_squares[w] += direct*direct
                pair_expansion_count += 1
        assert all(v <= 2600*delta**2*F(2,n) for v in phase_squares.values())
        pair_results.append({'pair':[i,j], 'per_phase_port_second_moment_ratios':
                             {str(w):str(v/(2600*delta**2*F(2,n))) for w,v in phase_squares.items()}})
    return {'dimension':n, 'row_expansions':row_expansion_count, 'pair_expansions':pair_expansion_count,
            'rows':row_results, 'pairs':pair_results, 'phase_choices':[1,-1]}


def fixtures():
    n=64
    ids=np.arange(n)
    fourier=np.exp(2j*np.pi*np.outer(ids,ids)/n)/8
    rng=np.random.default_rng(20261013)
    s=np.exp(1j*rng.uniform(0,2*np.pi,n))[:,None]*fourier*np.exp(1j*rng.uniform(0,2*np.pi,n))[None,:]
    yield 'fourier_with_left_right_phases', s.copy()
    for i,j in [(0,7),(1,33),(13,46),(2,63)]:
        theta=.19
        phi=float(rng.uniform(0,2*np.pi))
        left=s[i,:].copy()
        right=s[j,:].copy()
        s[i,:]=math.cos(theta)*left+math.sin(theta)*np.exp(1j*phi)*right
        s[j,:]=-math.sin(theta)*np.exp(-1j*phi)*left+math.cos(theta)*right
    for i,j in [(4,52),(8,35),(21,60)]:
        theta=.23
        phi=float(rng.uniform(0,2*np.pi))
        left=s[:,i].copy()
        right=s[:,j].copy()
        s[:,i]=math.cos(theta)*left+math.sin(theta)*np.exp(1j*phi)*right
        s[:,j]=-math.sin(theta)*np.exp(-1j*phi)*left+math.cos(theta)*right
    yield 'complex_rotated_fourier', s


def floating_controls():
    results=[]
    expansion_error=mean_error=0.0
    quadrature=1024
    ws=np.exp(2j*np.pi*np.arange(quadrature)/quadrature)
    for name,s0 in fixtures():
        n=len(s0)
        assert np.linalg.norm(s0.conj().T@s0-np.eye(n),2)<2e-13
        delta=float(np.max(abs(s0)**2))
        assert delta<=1/16
        records=[]
        for transposed in [False,True]:
            s=s0.T if transposed else s0
            p=abs(s)**2
            k=p@p
            p3=k@p
            rho=float(np.linalg.norm(p-np.ones((n,n))/n,2))
            assert rho<=1/10
            assert np.linalg.norm(p@p.T-p.T@p,2)>1e-9 or name=='fourier_with_left_right_phases'
            for i in [0,13,46]:
                ri=float(np.dot(p[i],p[i]))
                ai=float(np.dot(p[i],k[i]))
                assert ai<=1/n+rho*(ri-1/n)+1e-14
                sums=np.zeros(6)
                actual_squares=[]
                exact_mean=numerical_mean=0.0
                port_squares=[0.0,0.0,0.0]
                for e in range(n):
                    keep=np.array([z for z in range(n) if z!=e])
                    x=p[i,keep]
                    alpha=s[i,e]*s[e,keep]*s[i,keep].conj()
                    b=p[i,e]*p[e,keep]
                    r=p[i,e]**2
                    aa=2*np.sum(x*alpha)
                    bb=4*np.sum(x*b)
                    cc=np.sum(alpha**2)
                    dd=2*np.sum(alpha*b)
                    ff=np.sum(b*b)
                    sums+=np.array([r*r,abs(aa)**2,bb*bb,abs(cc)**2,abs(dd)**2,ff*ff])
                    if e==i:
                        continue
                    a=s[e,e]
                    d=1-abs(a)**2
                    exact=-r+bb/d+2*np.real(a.conjugate()*dd)/d**2+(1+abs(a)**2)*ff/d**3
                    exact_mean+=exact
                    q=ws/(1-a*ws)
                    feedback=s[i,keep][None,:]+q[:,None]*s[i,e]*s[e,keep][None,:]
                    increments=np.sum(abs(feedback)**4,axis=1)-ri
                    numerical_mean+=float(increments.mean())
                    mean_error=max(mean_error,abs(exact-float(increments.mean())))
                    for h,theta in enumerate([.17,1.71,3.9]):
                        w=np.exp(1j*(theta+.19*e))
                        q=w/(1-a*w)
                        actual=float(np.sum(abs(s[i,keep]+q*s[i,e]*s[e,keep])**4)-ri)
                        expanded=-r+2*np.real(q*aa)+abs(q)**2*bb+2*np.real(q*q*cc)+2*np.real(q*abs(q)**2*dd)+abs(q)**4*ff
                        expansion_error=max(expansion_error,abs(actual-expanded))
                        port_squares[h]+=actual*actual
                        assert abs(actual)<=8*delta*math.sqrt(ri)+34*delta**2+1e-14
                bounds=np.array([delta**2*ri,10*delta**2*ri,16*delta**2*ai,delta**2*ai,4*delta**3*ai,delta**4*ri])
                assert np.all(sums<=bounds+1e-15)
                assert max(port_squares)<=3500*delta**2*(ri+ai)+1e-15
                assert exact_mean/n<=-ri/(3*n)+5/n**2+delta**2/n+1e-14
                records.append({'transpose':transposed,'row':i,'mean':exact_mean/n,
                                'quadrature_mean':numerical_mean/n,
                                'max_coefficient_bound_ratio':float(np.max(sums/bounds)),
                                'max_raw_second_moment_bound_ratio':max(port_squares)/(3500*delta**2*(ri+ai))})
            for i,j in [(0,0),(0,13),(13,13),(13,46)]:
                means=0.0
                port_squares=[0.0,0.0,0.0]
                for e in range(n):
                    if e in [i,j]:
                        continue
                    keep=np.array([z for z in range(n) if z!=e])
                    a=s[e,e]
                    d0=1-abs(a)**2
                    q=ws/(1-a*ws)
                    row=s[i,keep][None,:]+q[:,None]*s[i,e]*s[e,keep][None,:]
                    col=s[keep,j][None,:]+q[:,None]*s[keep,e][None,:]*s[e,j]
                    means+=float((np.sum(abs(row)**2*abs(col)**2,axis=1)-k[i,j]).mean())
                    for h,theta in enumerate([.17,1.71,3.9]):
                        w=np.exp(1j*(theta+.19*e))
                        q=w/(1-a*w)
                        row=s[i,keep]+q*s[i,e]*s[e,keep]
                        col=s[keep,j]+q*s[keep,e]*s[e,j]
                        actual=float(np.dot(abs(row)**2,abs(col)**2)-k[i,j])
                        port_squares[h]+=actual*actual
                        assert abs(actual)<=12*delta*math.sqrt(k[i,j])+18*delta**2+1e-14
                assert means/n<=(-k[i,j]/2+5*p3[i,j]+2*delta*p[i,j])/n+1e-14
                assert max(port_squares)<=2600*delta**2*(k[i,j]+p3[i,j])+1e-14
                records.append({'transpose':transposed,'pair':[i,j], 'quadrature_mean':means/n,
                                'max_raw_second_moment_bound_ratio':max(port_squares)/(2600*delta**2*(k[i,j]+p3[i,j]))})
        results.append({'fixture':name,'delta':delta,'records':records})
    assert expansion_error<5e-15 and mean_error<5e-15
    return {'seed':20261013,'quadrature_nodes':quadrature,'float_dtype':'complex128',
            'max_expansion_absolute_error':expansion_error,'max_mean_quadrature_absolute_error':mean_error,
            'fixtures':results}


def exact_constants():
    delta=F(1,16)
    c=2*delta/(1-delta)**2+delta*(1+delta)/(1-delta)**3
    d=4/(1-delta)+2*delta/(1-delta)**2
    assert c==F(752,3375) and d==F(992,225)
    assert c+d/F(10)==F(448,675)<F(2,3)
    old_gc=F(12,11)
    xi=8*delta
    assert old_gc*xi==F(6,11)
    new_g=old_gc/(1-old_gc*xi)
    assert new_g==F(12,5)<3
    assert F(1,99)+F(1,40)<F(1,11)
    assert F(32,1)/(4*F(16,15))==F(15,2)
    return {'row_mean_coefficients':[str(c),str(d),str(c+d/10)],
            'green_product':str(old_gc*xi),'green_new_norm_bound':str(new_g),
            'green_deterministic_margin_without_remainder':str(F(1,11)-F(1,99)-F(1,40)),
            'entry_ell_exponent_coefficient':str(F(15,2))}


if __name__=='__main__':
    result={'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS},
            'exact_constants':exact_constants(), 'exact_walsh_controls':exact_walsh(),
            'floating_controls':floating_controls(),
            'boundary':'Finite algebra/complex128 controls only. Not exhaustive over unitaries or phases; not trajectory probability, asymptotics, clock identification, or BGS.'}
    output=ROOT/'global_feedback_flatness_independent_checks_20261013.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(output), 'exact_constants':result['exact_constants'],
                      'exact_expansions':result['exact_walsh_controls']['row_expansions']+result['exact_walsh_controls']['pair_expansions'],
                      'max_float_expansion_error':result['floating_controls']['max_expansion_absolute_error'],
                      'max_mean_quadrature_error':result['floating_controls']['max_mean_quadrature_absolute_error']},indent=2))
