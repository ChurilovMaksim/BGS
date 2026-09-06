#!/usr/bin/env python3
"""Exact symbolic and finite-field checks; not an asymptotic energy proof."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sympy as s

def invariants(p, r, t):
    den = pow(r*(t-1)**2 % p, -1, p)
    return (t*(r-1)**2*den % p, 4*(t-r)**2*den % p)

def coefficients(p, r, t):
    return tuple(x % p for x in (t*(r-1), r*(1-t), 2*(t-r), 1-t, r-1))

def symbolic():
    r,t,u,v,x,y = s.symbols('r t u v x y')
    I=t*(r-1)**2/(r*(t-1)**2); J=4*(t-r)**2/(r*(t-1)**2)
    z=(t-r)/(t-1); c0=1-I+J/4
    G=lambda r,t,u,v: t*(r-1)*u**2*v**2+r*(1-t)*u**2+2*(t-r)*u*v+(1-t)*v**2+r-1
    expressions=[z*z-J*r/4, c0*r-(r+1)*z,
                 J*(r+1)**2-4*c0*c0*r,
                 I.subs({r:1/r,t:1/t}, simultaneous=True)-I,
                 J.subs({r:1/r,t:1/t}, simultaneous=True)-J,
                 I.subs({r:t,t:r}, simultaneous=True)-1/I,
                 J.subs({r:t,t:r}, simultaneous=True)-J/I,
                 G(1/x**2,1/y**2,u,v)+G(x*x,y*y,u/(x*y),v*x/y)/(x*x),
                 G(t,r,u,v)+v*v*G(r,t,u,1/v),
                 s.discriminant(G(r,t,u,v),u)+4*(r-1)*(t-1)*(r-t*v*v)*(v*v-1)]
    for e in expressions: assert s.cancel(e)==0, e
    return len(expressions)

def main():
    if not __debug__: raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime-limit',type=int,default=101)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.prime_limit<5: ap.error('prime-limit must be at least 5')
    identities=symbolic(); pairs=fibres=toric_classes=subgroup_scalings=fields=0
    for p in s.primerange(5,args.prime_limit+1):
        p=int(p); fields+=1; buckets=defaultdict(list); tb=defaultdict(list)
        for r in range(2,p-1):
            ri=pow(r,-1,p)
            for t in range(2,p-1):
                if r==t: continue
                ij=invariants(p,r,t); buckets[ij].append((r,t))
                I,J=ij; Ii=pow(I,-1,p)
                tb[min(ij,(Ii,J*Ii % p))].append((r,t)); pairs+=1
        for group in buckets.values():
            r,t=group[0]
            assert set(group)=={(r,t),(pow(r,-1,p),pow(t,-1,p))}
            fibres+=1
        for group in tb.values():
            r,t=group[0]; ri,ti=pow(r,-1,p),pow(t,-1,p)
            assert set(group)=={(r,t),(ri,ti),(t,r),(ti,ri)}
            toric_classes+=1
        K=p-1
        while K%2==0: K//=2
        gen=pow(int(s.primitive_root(p)),(p-1)//K,p)
        H={pow(gen,j,p) for j in range(K)}
        for r in H-{1}:
            for t in H-{1,r}:
                alpha=pow(pow(r*t % p,-1,p),(K+1)//2,p)
                beta=r*alpha % p; scalar=-pow(r,-1,p) % p
                a,b,c,d,e=coefficients(p,r,t)
                scaled=tuple(scalar*w % p for w in
                             (a*alpha**2*beta**2,b*alpha**2,c*alpha*beta,d*beta**2,e))
                assert alpha in H and beta in H
                assert scaled==coefficients(p,pow(r,-1,p),pow(t,-1,p))
                subgroup_scalings+=1
    data={'status':'PASS','scope':'finite exact checks of the proved equivalence classification',
          'symbolic_identities':identities,'prime_limit':args.prime_limit,
          'prime_fields':fields,'ordered_parameter_pairs':pairs,'invariant_fibres':fibres,
          'toric_classes':toric_classes,'odd_subgroup_inverse_scalings':subgroup_scalings,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__': main()
