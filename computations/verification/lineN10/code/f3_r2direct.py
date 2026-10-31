"""N8-F3 fix: R2(a) computed directly as Line F full_R(RA_r2, 1) = (RA_r2+1)(1+||X||)+1 (arb, upward), compared with N8's F_R2/Pert route."""
import sys, json
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb
LF='/workspace/bgs-lineF/logs/'; n8=json.load(open('/workspace/bgs-lineN/N8/logs/r_other.json')) if True else {}
out={}
for a,f in [('0','certV_eta2_a0.json'),('2','certV_eta2_a2.json'),('6','certV_eta2_a6.json'),('4','certV_eta2_a4_tight.json')]:
    s=json.load(open(LF+f))['sectors'][a]
    if 'RA_r2' not in s: out[a]=dict(note='no RA_r2 field',keys=list(s.keys())); continue
    RA=arb(s['RA_r2'])*arb('1.0000001'); R2=(RA+1)*(1+C.Xn)+1; FR2=arb(s['F_R2'])
    Pert_LF=FR2/R2   # implied Line F Pert
    out[a]=dict(RA_r2=s['RA_r2'],R2_direct=float(R2.upper()),R2p_direct_with_LineF_F=float((R2/(1-FR2)).upper()),
               N8_value=n8.get('sector'+a))
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N10/logs/f3_r2direct.json','w'),indent=1)
