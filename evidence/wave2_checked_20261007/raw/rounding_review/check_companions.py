#!/usr/bin/env python3
"""Bounded regression only. Exact Gaussian integers for masks; floating diagnostics for norms."""
import hashlib, itertools, json, math, platform, time
from pathlib import Path
import numpy as np
from scipy.linalg import schur
ROOT=Path('/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot')
OUT=Path(__file__).resolve().parent
SOURCE_MANIFEST=ROOT.parent/'source_manifest.json'
EXPECTED='d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba'
RAW='evidence/research_checkpoint_20261007/raw/bgs_astra_signed_boundary/'
PATHS=[RAW+x for x in ['rounding_offcharge_upgrade.md','simple_spectrum_companion.md','growing_period_counterexample.md','inputs/18_uniform_abel_bound.md','carry_review/growing_review/review.md','carry_review/growing_review/seal.json','carry_review/growing_review/imported_abel_review.md','radial_review/seal_manifest.json']]+[
'mathematics/microscopic_rounding_control.md','mathematics/fractional_hamming_cancellation.md','mathematics/global_switch_transfer.md','mathematics/onestep_charge_gap.md','mathematics/actual_charge_radial_shell.md','mathematics/actual_charge_radial_resolvent.md','mathematics/literal_fixed_word_freeness.md','mathematics/literal_growing_word_window.md','mathematics/fixed_map_path_model.md','mathematics/four_branch_parametrix.md','mathematics/position_chain_mixing.md','mathematics/reversed_path_decay.md','mathematics/phase_trace_checkpoint.md','evidence/research_checkpoint_20261007/raw/bgs_literal_extension_review/independent_extension_audit.md','record/claim_ledger.md','record/claims.json']
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(SOURCE_MANIFEST)==EXPECTED
manifest=json.loads(SOURCE_MANIFEST.read_text())
pins={p:digest(ROOT/p) for p in PATHS}
assert all(manifest['files'][p]==h for p,h in pins.items())

def ga(a,b): return (a[0]+b[0],a[1]+b[1])
def gm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gc(a): return (a[0],-a[1])
def gsum(xs):
    a=(0,0)
    for b in xs:a=ga(a,b)
    return a
A=[[(15,0),(-12,0),(16,0)],[(0,20),(0,9),(0,-12)],[(0,0),(20,0),(15,0)]]
assert all(gsum(gm(A[i][k],gc(A[j][k])) for k in range(3))==((625,0) if i==j else (0,0)) for i in range(3) for j in range(3))
# A/25 is a dense-coupled Gaussian-rational unitary. No symmetry quotient is used.
mask_rows=[]
for m in range(1,6):
    paths=list(itertools.product(range(3), repeat=m)); amp={}; occ={}
    for x in paths:
        a=(1,0)
        for j in range(m):a=gm(a,A[x[j]][x[(j+1)%m]])
        amp[x]=a; occ[x]=tuple(x.count(k) for k in range(3))
    tr=gsum(amp.values()); full=gm(tr,gc(tr)); balanced=(0,0); off=(0,0); by={}
    for x in paths:
        for y in paths:
            val=gm(amp[x],gc(amp[y]))
            if occ[x]==occ[y]: balanced=ga(balanced,val);continue
            off=ga(off,val)
            c=tuple((y[j]-x[j])%3 for j in range(m))
            h=sum(v!=0 for v in c); s=sum(c[j]!=c[(j+1)%m] for j in range(m))
            by[h,s]=ga(by.get((h,s),(0,0)),val)
    assert ga(balanced,off)==full
    assert full[1]==balanced[1]==off[1]==0
    cut=(49*m)//100
    for R in (0,1,2):
        lowh=gsum(v for (h,s),v in by.items() if h<=cut)
        lowsh=gsum(v for (h,s),v in by.items() if h>cut and s<=R)
        residual=gsum(v for (h,s),v in by.items() if h>cut and s>R)
        assert ga(ga(lowh,lowsh),residual)==off
        assert lowh[1]==lowsh[1]==residual[1]==0
    mask_rows.append({'N':3,'m':m,'ordered_pairs':len(paths)**2,'full_numerator':full[0],'balanced_numerator':balanced[0],'offcharge_numerator':off[0],'common_denominator':25**(2*m)})

def op(a):return float(np.linalg.norm(a,2))
def rev(u):return u*u.conj().T
def charge(u,c):
    n=len(u); idx=(np.arange(n)+c)%n
    return u*np.conj(u[np.ix_(idx,idx)])
RNG=np.random.default_rng(20261007)
norm_rows=[]
for n in (3,5,9):
    z=RNG.normal(size=(n,n))+1j*RNG.normal(size=(n,n));u=np.linalg.qr(z)[0]
    z=RNG.normal(size=(n,n))+1j*RNG.normal(size=(n,n)); mcat=np.linalg.qr(z)[0]
    t,z=schur(u,output='complex'); theta=np.angle(np.diag(t));k=max(2,n//2)
    phase=2*np.pi*np.rint(theta*k/(2*np.pi))/k
    w=(z*np.exp(1j*phase))@z.conj().T
    eps=op(w-u); q=u@mcat.conj().T; qhat=w@mcat.conj().T
    assert eps<=np.pi/k+1e-12
    assert op(np.linalg.matrix_power(w,k)-np.eye(n))<1e-11
    assert op(rev(w)-rev(u))<=2*eps+1e-12
    diffs=[op(charge(w,c)-charge(u,c)) for c in range(n)]
    assert max(diffs)<=2*eps+1e-12
    # Fixed and growing finite lengths here test the same telescoping inequality.
    max_ratio=0.0
    for ell in (1,2,3,7,17):
        aa=np.eye(n,dtype=complex);bb=aa.copy()
        for j in range(ell):
            symbol=j%4
            left=(q,q.conj().T,mcat,mcat.conj().T)[symbol]
            right=(qhat,qhat.conj().T,mcat,mcat.conj().T)[symbol]
            aa=aa@left;bb=bb@right
        error=abs(np.trace(aa-bb))/n
        assert error<=ell*eps+1e-12
        max_ratio=max(max_ratio,float(error/(ell*eps)))
    norm_rows.append({'N':n,'K':k,'epsilon':eps,'reverse_difference':op(rev(w)-rev(u)),'max_charge_difference':max(diffs),'max_word_error_over_bound':max_ratio})

split_rows=[]
for p in (5,11):
    n=p*p
    f=np.array([[(j%p)**3%p,(j//p)**3%p] for j in range(n)])
    amat=np.array([[1,2],[0,1]],dtype=int)
    v=np.exp(2j*np.pi*((f@amat@f.T)%p)/p)/p
    t,z=schur(v,output='complex'); theta=np.angle(np.diag(t)); period=2*p
    # Snap the known exact roots to remove Schur eigenphase roundoff; this is only a diagnostic realization.
    theta=2*np.pi*np.rint(theta*period/(2*np.pi))/period
    vref=(z*np.exp(1j*theta))@z.conj().T
    delt=np.arange(1,n+1,dtype=float)/n**4
    w=(z*np.exp(1j*(theta+delt)))@z.conj().T
    eps=op(w-vref);limit=n**-3
    assert op(v-vref)<2e-12
    assert eps<=limit+2e-12
    assert op(rev(w)-rev(vref))<=2*limit+4e-12
    assert op(abs(w)**2-np.ones((n,n))/n)<=2*limit+4e-12
    e0=np.exp(1j*theta);e1=np.exp(1j*(theta+delt))
    for power in range(1,2*n+1):
        err=abs(sum(e1**power)-sum(e0**power))
        assert err<=power*n*limit+1e-9
    split_rows.append({'p':p,'N':n,'epsilon':eps,'bound':limit,'root_reconstruction_error':op(v-vref),'reverse_norm':op(rev(w)),'P_centered_norm':op(abs(w)**2-np.ones((n,n))/n),'powers_tested':[1,2*n]})

def bump(t):return math.exp(4-1/((t-1)*(2-t))) if 1<t<2 else 0.0
L=256;cw=(2/3)*math.exp(4);return_sum=sum(bump(r/L) for r in range(1,2*L+1))
assert return_sum>cw+1
finite_returns=[]
for n in (1025,4097,16385):
    k=n//L
    value=sum(bump(r*k/n) for r in range(1,math.ceil(2*n/k)+1))
    finite_returns.append({'N':n,'K':k,'return_lower_bound':value})
result={'interpretation':'Exact finite mask identities verified; floating continuity/splitting diagnostics passed only in listed ranges. No finite test proves any asymptotic theorem or irrationality statement.', 'source_manifest_sha256':EXPECTED,'source_pins':pins,'exact_mask_controls':mask_rows,'floating_norm_controls':norm_rows,'floating_split_controls':split_rows,'smooth_band_control':{'a':1,'b':2,'L':L,'C_w':cw,'sum_w_r_over_L':return_sum,'finite_return_sums':finite_returns},'seed':20261007,'software':{'python':platform.python_version(),'numpy':np.__version__},'tolerance_note':'Norm controls use 1e-12 additive slack; trace telescoping checks allow 1e-9 Schur/power roundoff. Non-root-of-unity is proved algebraically in report, never numerically tested.'}
(OUT/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'passed','exact_mask_ordered_pairs':sum(x['ordered_pairs'] for x in mask_rows),'norm_dimensions':[3,5,9],'split_dimensions':[25,121],'smooth_band_L':L,'C_w':cw,'return_sum':return_sum,'source_pins':len(pins)},indent=2))
