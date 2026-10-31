"""Referee N11: phase check of N11's magnitude-only completeness matching (g_model2.py window 0.5..2x |candidate|).
For every class N11 'explains', test whether the complex weight matches a gas product (either the product or its conjugate,
up to the sign/orientation ambiguity) within 25% in complex distance; report the weight that matches by magnitude only."""
import json, math, collections
ws=complex(3.43579708677916e-4,1.9579583160123678e-4); c0=complex(2.9868592945521465e-05,-6.606363627303442e-06)
c4=complex(1.0445006903993471e-06,-3.1194465556049058e-06); c8=complex(1.3823269841170871e-08,1.1106723814121258e-08)
C={'w*^2':ws**2,'w*c0':ws*c0,'w*c4':ws*c4,'c0^2':c0**2,'w*^2c0':ws**2*c0,'w*^3':ws**3,'c0c4':c0*c4,'w*c8':ws*c8}
d=json.load(open('/workspace/bgs-lineN/N11/logs/t_classes_p47_N2000.json'))
MODEL0={(1,0),(0,1),(2,0),(0,2)}
mag_only=collections.defaultdict(float); phase_ok=collections.defaultdict(float); cnt=collections.Counter(); tot=0
for r in d['res']:
    a=tuple(map(abs,r['alpha']))
    if (r['bg']=='q' and a==(1,0)) or (r['bg']=='0' and a in MODEL0): continue
    z=complex(*r['r']); m=abs(z); tot+=m
    hit=[k for k,v in C.items() if 0.5*abs(v)<=m<=2*abs(v)]
    if not hit: continue
    k=hit[0]; v=C[k]
    ok=min(abs(z-v),abs(z-v.conjugate()),abs(z+v),abs(z+v.conjugate()))<=0.25*abs(v)
    (phase_ok if ok else mag_only)[k]+=m; cnt[(k,ok)]+=1
out=dict(total_nonmodel_weight=tot,phase_ok={k:v for k,v in phase_ok.items()},magnitude_only={k:v for k,v in mag_only.items()},
         counts={f'{k}|{ok}':c for (k,ok),c in cnt.items()})
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_match.json','w'),indent=1)
