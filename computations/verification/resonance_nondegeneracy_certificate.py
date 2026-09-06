#!/usr/bin/env python3
"""Generate exact real-algebra certificates, never infer positivity from sampling.

For T=((3,2),(4,3)), Gamma/pi^2=2 sum |Q_orbit(z,conj(z))|^2.
The real symbol is sum(z_v e_v+conj(z_v)e_-v), with arbitrary complex z_v.
No evenness or Fourier-phase restriction is imposed. Instructions are:
P row: a sole surviving cross monomial vanishes;
S row: a sole complex square, or a sign-definite sum of |z_i|^2, vanishes;
D i j: z_i != 0 and a zero product of z_i/z_j or their conjugates imply z_j=0;
F i child: refute z_i != 0 by the supplied child proof, then conclude z_i=0.
Only successfully checked deductions are emitted. Failure to finish is UNKNOWN.
The independent replay checker and quadratic-ring C++ constructor are separate.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import time
Vector = tuple[int, int]
Monomial = tuple[int, int]
def step(v: Vector) -> Vector:return 3*v[0]+2*v[1], 4*v[0]+3*v[1]
def back(v: Vector) -> Vector:return 3*v[0]-2*v[1], -4*v[0]+3*v[1]
def signed(v: Vector) -> Vector:return min(v, (-v[0], -v[1]))
def energy(v: Vector) -> int:return 2*v[0]*v[0]+v[1]*v[1]
@lru_cache(maxsize=None)
def orbit_key(v: Vector) -> tuple[Vector, int]:
    if v == (0, 0):raise ValueError('The zero frequency has no hyperbolic orbit.')
    r=signed(v);orientation=1 if r==v else -1
    while True:
        choices=[(r,orientation)]
        for w in (step(r),back(r)):
            k=signed(w);choices.append((k,orientation if k==w else -orientation))
        k,sg=min(choices,key=lambda item:(energy(item[0]),item[0]))
        if k==r:return r,orientation
        r,orientation=k,sg
def orbit_forms(radius: int) -> tuple[list[Vector], list[dict]]:
    if radius < 1:raise ValueError('A positive integer radius is required.')
    modes=[(a,b) for a in range(radius+1) for b in range(-radius,radius+1) if a>0 or b>0]
    bins: dict=defaultdict(lambda:defaultdict(int))
    for i,u in enumerate(modes):
        for j,v in enumerate(modes):
            w=step(v);det=u[0]*w[1]-u[1]*w[0]
            if det==0:continue
            for e in (-1,1):
                for f in (-1,1):
                    k,orientation=orbit_key((e*u[0]+f*w[0],e*u[1]+f*w[1]))
                    if orientation<0:continue
                    mon=tuple(sorted(((i,e),(j,f))))
                    bins[k][mon]-=e*f*det
    rows=[{'key':list(k),'terms':[[i,e,j,f,a] for ((i,e),(j,f)),a in sorted(q.items()) if a]} for k,q in sorted(bins.items()) if any(q.values())]
    return modes,rows
def canonical_bytes(value: object) -> bytes:return (json.dumps(value, separators=(',', ':'), sort_keys=True)+'\n').encode()
def propagate(rows: list[dict], zeros: set[int], products: set[Monomial],nonzero: set[int]) -> list:
    proof = []
    while True:
        changed = False
        for i,j in sorted(products):
            for pivot,target in ((i,j),(j,i)):
                if pivot in nonzero and target not in zeros:
                    zeros.add(target);proof.append(['D',pivot,target]);changed=True
                    if zeros & nonzero:return proof
        for index, row in enumerate(rows):
            remaining = [(i,e,j,f,a) for i,e,j,f,a in row['terms'] if i not in zeros and j not in zeros and (i,j) not in products]
            if not remaining:continue
            if len(remaining) == 1 and remaining[0][0] != remaining[0][2]:
                i,_,j,_,_ = remaining[0];products.add((i,j));proof.append(['P',index]);changed=True
            elif (len(remaining)==1 and remaining[0][0]==remaining[0][2]) or (all(i==j and e==-f for i,e,j,f,_ in remaining) and (all(a>0 for *_,a in remaining) or all(a<0 for *_,a in remaining))):
                zeros.update(i for i,*_ in remaining);proof.append(['S',index]);changed=True
                if zeros & nonzero:return proof
        if not changed:return proof
def prune(steps: list, rows: list[dict], initial_zeros: set[int],initial_products: set[Monomial], targets: set[tuple]) -> tuple[list, set]:
    zeros,products=set(initial_zeros),set(initial_products);origins={('z',i):None for i in zeros};origins.update({('p',i,j):None for i,j in products});entries=[]
    for ins in steps:
        op=ins[0];deps=set();outs=[];kept=ins
        if op in ('P','S'):
            rem=[]
            for i,e,j,f,a in rows[ins[1]]['terms']:
                options=[]
                if i in zeros:options.append(('z',i))
                if j in zeros:options.append(('z',j))
                if (i,j) in products:options.append(('p',i,j))
                if options:selected=min(options,key=lambda f: (-1 if origins[f] is None else origins[f], f));deps.add(selected)
                else:rem.append((i,e,j,f,a))
            if op=='P':i,_,j,_,_=rem[0];products.add((i,j));outs=[('p',i,j)]
            else:
                for i,e,j,f,a in rem:zeros.add(i);outs.append(('z',i))
        elif op=='D':
            i,j=ins[1:];deps.add(('p',min(i,j),max(i,j)));zeros.add(j);outs=[('z',j)]
        else:
            pivot=ins[1];child,external=prune(ins[2],rows,zeros,products,{('z',pivot)});deps.update(external);kept=['F',pivot,child];zeros.add(pivot);outs=[('z',pivot)]
        index=len(entries);entries.append((kept,deps))
        for f in outs:origins[f]=index
    needed=set();external=set();queue=list(targets)
    while queue:
        fact=queue.pop()
        if fact not in origins:raise RuntimeError('Proof slice asks for an unproved fact.')
        origin=origins[fact]
        if origin is None:external.add(fact)
        elif origin not in needed:needed.add(origin);queue.extend(entries[origin][1])
    return [ins for i,(ins,_) in enumerate(entries) if i in needed],external
def generate(radius: int) -> dict:
    started=time.monotonic();modes,rows=orbit_forms(radius);zeros:set[int]=set();products:set[Monomial]=set();instructions=propagate(rows,zeros,products,set());failed=0;rounds=0
    while len(zeros)<len(modes):
        rounds+=1;before=len(zeros)
        for i in range(len(modes)):
            if i in zeros:continue
            z,p=set(zeros),set(products);child=propagate(rows,z,p,{i})
            if i in z:instructions.append(['F',i,child]);zeros.add(i);instructions.extend(propagate(rows,zeros,products,set()))
            else:failed+=1
        if len(zeros)==before:break
    if len(zeros)==len(modes):
        instructions,external=prune(instructions,rows,set(),set(),{('z',i) for i in range(len(modes))})
        if external:raise RuntimeError('A root proof depends on an external assumption.')
    return {'schema':1,'matrix':[[3,2],[4,3]],'radius':radius,'basis':'complex_fourier','variables':len(modes),'dimension':2*len(modes),'orbit_equations':len(rows),'equation_sha256':hashlib.sha256(canonical_bytes(rows)).hexdigest(),'status':'CERTIFICATE' if len(zeros)==len(modes) else 'UNKNOWN','proof':instructions,'remaining':[i for i in range(len(modes)) if i not in zeros],'search':{'failed_trials':failed,'rounds':rounds,'elapsed_seconds':round(time.monotonic()-started,6)},'scope':'Exact real-algebra nondegeneracy of the specified real Fourier box, arbitrary phases; not positive BGS.'}
def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--radius',type=int,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();report=generate(args.radius);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(canonical_bytes(report));print(json.dumps({k:v for k,v in report.items() if k!='proof'},indent=2));
    if report['status']!='CERTIFICATE':raise SystemExit(2)
if __name__=='__main__':main()
