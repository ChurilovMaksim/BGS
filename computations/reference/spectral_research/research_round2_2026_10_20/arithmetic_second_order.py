#!/usr/bin/env python3
"""Exact second-order splitting certificates for the specified U_N family.

Only integer finite-field operations are used. The original first-order
implementation is imported read-only after checking its SHA-256.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

BASE = Path('/workspace/scratch/e111873eea6c/research_continuation_2026_10_20')
INPUT_SHA = 'add99347a674298335226dccb58b87c35a7343a33c97053bd2310f69c07bd6cf'
SOURCE = BASE / 'verify_spectral_simplicity.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == INPUT_SHA
INITIAL_CERTIFICATES = BASE / 'spectral_simplicity_certificates.json'
INITIAL_CERTIFICATES_SHA = '9b35dbce426538d275574c484be5519d14f69399dbad3c14eaaeb5e44390024b'
assert hashlib.sha256(INITIAL_CERTIFICATES.read_bytes()).hexdigest() == INITIAL_CERTIFICATES_SHA
spec = importlib.util.spec_from_file_location('first_order_exact', SOURCE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def determinant_mod(a, p):
    """Gaussian elimination, used only on small Sylvester matrices."""
    a = np.asarray(a, dtype=np.int64).copy() % p
    n = len(a)
    result = 1
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k, j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[[j, pivot]] = a[[pivot, j]]
            result = -result % p
        value = int(a[j, j])
        result = result * value % p
        inv = pow(value, -1, p)
        for k in range(j + 1, n):
            factor = int(a[k, j]) * inv % p
            a[k, j:] = (a[k, j:] - factor * a[j, j:]) % p
    return result


def polynomial_discriminant(coefficients, p):
    """Discriminant of a monic polynomial via its Sylvester resultant."""
    d = len(coefficients) - 1
    assert coefficients[0] == 1
    if d <= 1:
        return 1
    derivative = [(d-j) * coefficients[j] % p for j in range(d)]
    sylvester = np.zeros((2*d-1, 2*d-1), dtype=np.int64)
    for j in range(d-1):
        sylvester[j, j:j+d+1] = coefficients
    for j in range(d):
        sylvester[d-1+j, j:j+d] = derivative
    return pow(-1, d*(d-1)//2, p) * determinant_mod(sylvester, p) % p


def reduced_leading_coefficient(sectors, p):
    """Coefficient of t^nu in the reduced characteristic discriminant."""
    result = 1
    for j, record in enumerate(sectors):
        d, lam = record['dimension'], record['lambda']
        if d > 1:
            key = 'first_characteristic' if record['order'] == 1 else 'second_characteristic'
            disc = polynomial_discriminant(record[key], p)
            assert disc
            record['splitting_polynomial_discriminant'] = disc
            result = result * pow(lam, d*(d-1), p) * disc % p
        for previous in sectors[:j]:
            exponent = 2*d*previous['dimension']
            result = result * pow((lam-previous['lambda']) % p, exponent, p) % p
    assert result
    return result


def exact_certificate(n, p=None, g=None):
    initial = next(d for d in json.loads(INITIAL_CERTIFICATES.read_text())['dimensions'] if d['N']==n)
    r = old.cat_order(n)
    if p is None:
        p, g = initial['field_prime'], initial['primitive_root']
    assert old.is_prime(p) and p > n and (p-1) % (4*n)==0 and (p-1) % (8*r)==0
    assert 0 < g < p and all(pow(g,(p-1)//q,p)!=1 for q in old.prime_factors(p-1))
    assert n*(p-1)**2 < 2**63-1
    mm = lambda a,b: old.matmul(a,b,p)
    a,m,embedding = old.exact_matrices(n,p,g)
    eye=np.eye(n,dtype=np.int64)
    powers=[]; current=eye.copy()
    for j in range(r):
        powers.append(current.copy()); current=mm(current,m)
    scalar=int(current[0,0]); assert np.array_equal(current,scalar*eye%p)
    root8r=pow(g,(p-1)//(8*r),p)
    gamma=next(pow(root8r,k,p) for k in range(8) if pow(pow(root8r,k,p),r,p)==scalar)
    gi=pow(gamma,-1,p); ri=pow(r,-1,p); half=pow(2,-1,p)
    powers=[powers[j]*pow(gi,j,p)%p for j in range(r)]
    xi=pow(g,(p-1)//r,p)
    sectors=[]; dimsum=0; totalvaluation=0; success=True
    projector_sum=np.zeros((n,n),dtype=np.int64)
    for k in range(r):
        weights=[pow(xi,(-k*j)%r,p)*ri%p for j in range(r)]
        proj=np.zeros((n,n),dtype=np.int64)
        for j in range(r): proj=(proj+weights[j]*powers[j])%p
        dim=int(np.trace(proj))%p
        assert dim<=n
        projector_sum=(projector_sum+proj)%p
        dimsum+=dim; totalvaluation+=dim*(dim-1)
        if dim==0: continue
        lam=gamma*pow(xi,k,p)%p
        assert np.array_equal(mm(proj,proj),proj)
        assert np.array_equal(mm(m,proj),lam*proj%p)
        if dim==1:
            sectors.append({'k':k,'dimension':dim,'lambda':lam,'order':0,'certified':True}); continue
        columns=old.pivot_columns(proj,p); assert len(columns)==dim
        basis=proj[:,columns]; rows=old.pivot_columns(basis.T,p); assert len(rows)==dim
        left=old.inverse(basis[rows,:],p)
        ab=mm(a,basis)
        c=mm(left,mm(proj,ab)[rows,:])
        char1=old.characteristic_polynomial(c,p)
        gcd1=old.squarefree_gcd(char1,p)
        record={'k':k,'dimension':dim,'lambda':lam,'basis_columns':columns,'basis_rows':rows,
                'first_matrix':c.tolist(),'first_characteristic':char1,'first_gcd':gcd1}
        if len(gcd1)==1:
            record.update({'order':1,'certified':True}); sectors.append(record); continue
        first_scalar=int(np.trace(c))*pow(dim,-1,p)%p
        is_scalar=np.array_equal(c,first_scalar*np.eye(dim,dtype=np.int64)%p)
        record.update({'first_scalar':first_scalar,'first_is_scalar':is_scalar})
        if not is_scalar:
            success=False; record.update({'certified':False,'reason':'repeated nonscalar first coefficient'}); sectors.append(record);continue
        x=(m-lam*eye+proj)%p
        resolvent=(old.inverse(x,p)-proj)%p
        q=(eye-proj)%p
        assert not np.any(mm(proj,resolvent)) and not np.any(mm(resolvent,proj))
        assert np.array_equal(mm((m-lam*eye)%p,resolvent),q)
        h_action=(half*mm(proj,mm(a,ab))-mm(proj,mm(a,mm(m,mm(resolvent,ab)))))%p
        h=mm(left,h_action[rows,:])
        char2=old.characteristic_polynomial(h,p); gcd2=old.squarefree_gcd(char2,p)
        ok=len(gcd2)==1
        if ok: totalvaluation+=dim*(dim-1)
        else: success=False
        record.update({'order':2,'second_matrix':h.tolist(),'second_characteristic':char2,
                       'second_gcd':gcd2,'certified':ok})
        sectors.append(record)
    assert dimsum==n
    assert np.array_equal(projector_sum,eye)
    if success: assert totalvaluation<p
    leading = reduced_leading_coefficient(sectors,p) if success else None
    return {'N':n,'p':p,'primitive_root':g,'cat_order':r,**embedding,'gamma':gamma,'xi':xi,
            'input_code_sha256':INPUT_SHA,'sectors':sectors,
            'certificate':success,'discriminant_valuation':totalvaluation if success else None,
            'discriminant_leading_coefficient':leading,
            'valuation_scope':'valuation over F_p only; certifies a nonzero characteristic-zero coefficient',
            'factorials_invertible_for_required_jet':totalvaluation<p if success else None,
            'arithmetic':'exact F_p, int64 overflow bound checked before products'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--dimensions',nargs='+',type=int,default=[49,147])
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('arithmetic_second_order_results.json'))
    args=parser.parse_args()
    out={'method':'finite-field second-order Schur complement and discriminant-jet lifting','dimensions':[]}
    for n in args.dimensions:
        result=exact_certificate(n);out['dimensions'].append(result)
        args.output.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({'N':n,'certificate':result['certificate'],'valuation':result['discriminant_valuation'],
                          'leading_coefficient':result['discriminant_leading_coefficient'],
                          'second_order':[s for s in result['sectors'] if s['order']==2]},separators=(',',':')),flush=True)


if __name__=='__main__': main()
