"""N4 (B) [CA]: assemble the 8V arb cell certificate.  Recomputes every accepted cell interval EXACTLY from its label (Fractions),
checks that the accepted cells cover [0,1], takes the max cell bound (each already rigorous, divided by 1-||F||), then adds the
perturbation penalty with rigorous ||R||_2 <= ||R||_F and ||R^{-1}||_2 <= ||S||_F/(1-||F||_F) (from the 'pre' records, arb upper bounds)
and the Line F error terms (certV_eta2_a4.json).  usage: b_assemble.py NC0 certjson threshold r2 out.json log1 [log2 ...]"""
import sys, json
from fractions import Fraction as Fr
from flint import arb
NC0=int(sys.argv[1]); cj=json.load(open(sys.argv[2])); thr=float(sys.argv[3]); r2=arb(sys.argv[4]); outf=sys.argv[5]; logs=sys.argv[6:]
cells=[]; pre=None; done=0
for lf in logs:
    for line in open(lf):
        d=json.loads(line)
        if d['kind']=='pre': pre=d
        elif d['kind']=='cell': cells.append(d)
        elif d['kind']=='done': done+=1
def interval(lab):
    i=int(''.join(ch for ch in lab if ch.isdigit())); tc=Fr(2*i+1,2*NC0); h=Fr(1,2*NC0)
    for ch in lab[len(str(i)):]:
        h/=2; tc = tc+h if ch=='R' else tc-h
    return tc-h, tc+h
iv=sorted((interval(c['lab']),c['bound']) for c in cells)
pos=Fr(0); gaps=[]
for (a,b),_ in iv:
    if a>pos: gaps.append((float(pos),float(a)))
    pos=max(pos,b)
covered = (not gaps) and pos>=1
fmax=max(b for _,b in iv)
eps=arb(cj['delta1'])+arb(cj['delta2'])+arb(cj['Delta']); Xn=arb(cj['Xnorm'])
Fb=arb(pre['Fb']); nR=arb(pre['nRF']); nRi=arb(pre['nSF'])/(1-Fb); f=arb(fmax)
b=f/(Xn*(nRi+1)); pen=eps*max(nR,arb(1),b)*(nRi+1+1/b); L=f+pen
res=dict(workers_done=done,cells=len(cells),covered=covered,gaps=gaps[:5],f_cells_max=fmax,Fb=pre['Fb'],T0=pre['T0'],L2=pre['L2'],
  normR_F=pre['nRF'],normRinv_upper=float(nRi.upper()),eps=float(eps.upper()),Xnorm=float(Xn),b=float(b.mid()),penalty=float(pen.upper()),
  Lambda_free_upper=float(L.upper()),threshold=thr,unit_point_rate=float((L*r2).root(3).upper()),
  kappa=float((max(nR,arb(1),b)*(nRi+1+1/b)).upper()))
print(json.dumps(res,indent=1)); json.dump(res,open(outf,'w'),indent=1)
