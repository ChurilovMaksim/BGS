#!/usr/bin/env python3
"""Independent exact controls; finite cases only, no asymptotic inference.
Cyclotomic coefficients are integers, reduced by 1+z+...+z^(p-1)=0.
No assertion statement is used, so checks remain active under python -O.
"""
from collections import Counter, defaultdict
from itertools import product
from math import factorial
import argparse, hashlib, json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parent.parent

def require(condition, message):
    if not condition: raise RuntimeError(message)

def reduce_cyclotomic(v): return [x-v[-1] for x in v[:-1]]
def diff(a,b): return [x-y for x,y in zip(a,b)]
def correlation(hist,p):
    out=[0]*p
    for a,n in hist.items():
        for b,k in hist.items():out[(a-b)%p]+=n*k
    return out

def path_controls(p,m,full_pair_masks=False):
    cube=[pow(j,3,p) for j in range(p)]
    rows=[]; by_occupation=defaultdict(Counter); whole=Counter()
    for x in product(range(p),repeat=m):
        phase=sum(cube[x[j]]*cube[x[(j+1)%m]] for j in range(m))%p
        occ=tuple(sorted(x));rows.append((x,phase,occ))
        by_occupation[occ][phase]+=1;whole[phase]+=1
    total=correlation(whole,p);balanced=[0]*p
    for hist in by_occupation.values():
        balanced=[x+y for x,y in zip(balanced,correlation(hist,p))]
    # Ordered rooted words. Their amplitude-product normalization is p^(-m).
    expected=[(p*p if m%4==0 else 1)*p**m]+[0]*(p-2)
    require(reduce_cyclotomic(total)==expected,f'trace-square identity p={p},m={m}')
    off=diff(total,balanced)
    low_h=[0]*p;cutoff=49*m//100
    # These cases all have cutoff <=1. Enumerate just that literal mask.
    require(cutoff<=1,'low-H enumeration declared scope')
    phase_lookup={x:(f,o) for x,f,o in rows}
    if cutoff==1:
        for x,f,occ in rows:
            for j in range(m):
                for yj in range(p):
                    if yj==x[j]:continue
                    y=x[:j]+(yj,)+x[j+1:];g,o=phase_lookup[y]
                    if o!=occ:low_h[(f-g)%p]+=1
    require(reduce_cyclotomic(low_h)==[0]*(p-1),'exact low-H offcharge cancellation')
    result={'p':p,'m':m,'rooted_words':len(rows),'occupation_classes':len(by_occupation),
            'total_numerator_cyclotomic':reduce_cyclotomic(total),
            'balanced_numerator_cyclotomic':reduce_cyclotomic(balanced),
            'denominator':p**m,'low_h_cutoff':cutoff,'low_h_offcharge_exactly_zero':True}
    if full_pair_masks:
        # R=1: cyclic words cannot have exactly one switch; constant nonzero
        # differences are nonetheless retained in the low-switch subtraction.
        low_s_high_h=[0]*p; residual=[0]*p;off_direct=[0]*p
        for x,f,occ in rows:
            for y,g,o in rows:
                if o==occ:continue
                c=tuple((v-u)%p for u,v in zip(x,y))
                h=sum(t!=0 for t in c);s=sum(c[j]!=c[(j+1)%m] for j in range(m))
                a=(f-g)%p;off_direct[a]+=1
                if h>cutoff:(low_s_high_h if s<=1 else residual)[a]+=1
        require(off_direct==off,'exact direct offcharge occupation subtraction')
        require([a+b+c for a,b,c in zip(low_h,low_s_high_h,residual)]==off,'disjoint masks before cyclotomic reduction')
        result['mask_pair_enumeration']=len(rows)**2
        result['switch_cutoff']=1
        result['exact_mask_partition']=True
    return result

def finite_field_controls():
    out=[]
    for p in [5,11,17,23,29]:
        cube=[pow(j,3,p) for j in range(p)]
        require(len(set(cube))==p,'cubing permutation')
        # Direct exact V^2 character histograms, not a reused Fourier routine.
        for j,l in product(range(p),repeat=2):
            h=Counter((cube[j]*cube[k]+cube[k]*cube[l])%p for k in range(p))
            vec=[h[t] for t in range(p)]
            want=[p]+[0]*(p-2) if l==(-j)%p else [0]*(p-1)
            require(reduce_cyclotomic(vec)==want,'V^2 is reflection')
        # Every offdiagonal BB* phase is degree 2 or 3, never constant or linear.
        degree_counts=Counter()
        for c in range(1,p):
            for j,l in product(range(p),repeat=2):
                if j==l:continue
                a=(cube[j]-cube[l])%p;b=(cube[(j+c)%p]-cube[(l+c)%p])%p
                require(a!=0 and b!=0,'injectivity gives both nonzero')
                d=3 if (a-b)%p else 2
                require((-3*b*c)%p!=0,'nonzero quadratic coefficient')
                degree_counts[d]+=1
        out.append({'p':p,'v_square_reflection':True,'charge_phase_degree_counts':dict(degree_counts)})
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--inject-failure',action='store_true');a=parser.parse_args()
    if a.inject_failure:require(False,'injected failure proves fail-closed execution')
    man=json.loads((ROOT/'source_manifest.json').read_text());checked=[]
    for s in man['sources']:
        got=hashlib.sha256((ROOT/s['copy']).read_bytes()).hexdigest()
        require(got==s['sha256'],'source hash: '+s['copy']);checked.append(s['copy'])
    require(hashlib.sha256((ROOT/'cubic_offcharge_counterexample.md').read_bytes()).hexdigest()=='180e1c45acdf9f8c6db5a8c6b0fe8ebf3dfd4ddafd5b5307ea674823298077bb','candidate hash')
    cases=[path_controls(5,m,full_pair_masks=(m==4)) for m in range(1,5)]
    cases += [path_controls(11,m) for m in range(1,4)]
    cases += [path_controls(23,4)]
    print(json.dumps({'status':'passed','arithmetic':'exact integer cyclotomic coefficient vectors','source_hashes_verified':checked,'finite_fields':finite_field_controls(),'path_cases':cases,'nonclaims':['No numerical test establishes the universal gradient inequality, charge decay, or asymptotic divergence.','The family is not the fixed quantization and fails reverse-kernel decay.']},indent=2,sort_keys=True))
if __name__=='__main__':main()
