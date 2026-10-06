#!/usr/bin/env python3
"""Independent exact algebra checks for the selected-coefficient interfaces.
No asymptotic, weighted-equidistribution, quantum-integral or BGS verification.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path('/workspace/shared')
OUT=Path(__file__).resolve().parent

def mv(M,v):return (M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1])
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def plus(v,w):return (v[0]+w[0],v[1]+w[1])
def neg(v):return (-v[0],-v[1])
def mod(v):return tuple(x%1 for x in v)
def om(v,w):return v[0]*w[1]-v[1]*w[0]
def integral(x):return x.denominator==1
S=((3,4),(2,3)); A=((1,0),(0,1)); rows=[]; checks=0
for m in range(1,65):
    A=mm(S,A)
    B=((A[0][0]-1,A[0][1]),(A[1][0],A[1][1]-1))
    det=B[0][0]*B[1][1]-B[0][1]*B[1][0]
    Bi=((F(B[1][1],det),F(-B[0][1],det)),(F(-B[1][0],det),F(B[0][0],det)))
    pulse=mv(Bi,(0,1)); D=-det
    assert pulse[1]==F(-1,2)
    assert pulse[0]==F(A[0][1],D)
    def Q(z):
        n=mv(B,z); assert all(integral(x) for x in n)
        return (om(z,n)-n[0]*n[1])/2
    def bil(z,d):return om(z,mv(B,d))
    assert Q(pulse)==pulse[0]/2
    pos=set(); z=pulse
    for j in range(m):pos.add(mod(z)); z=mv(S,z)
    assert mod(z)==mod(pulse)
    nega={mod(neg(z)) for z in pos}; union=pos|nega
    assert len(union)<=2*m and (0,0) not in union
    for N in (1,3,5,7,9,15,21,35):
        assert all(mod((N*z[0],N*z[1]))!=(0,0) for z in union)
    for nq in range(-3,4):
      for np in range(-3,4):
        z=mv(Bi,(nq,np)); Sz=mv(S,z)
        exact=-3*nq*nq-8*nq*np-6*np*np
        assert Q(Sz)-Q(z)==exact
        candidate=-3*nq*nq-10*nq*np-6*np*np
        assert integral(Q(Sz)-Q(z)-candidate)
        assert integral(Q(plus(z,pulse))-Q(z)-Q(pulse)-bil(z,pulse))
        assert integral(Q(neg(pulse))+bil(plus(z,pulse),neg(pulse))+Q(pulse)+bil(z,pulse))
        assert integral(bil(Sz,mv(S,pulse))-bil(z,pulse))
        assert integral(bil(z,pulse)-z[0])
        checks+=6
    rows.append({'m':m,'D':D,'positive_count':len(pos),'negative_overlap':len(pos&nega),'union_count':len(union),'pulse_q':str(pulse[0])})

manifest=ROOT/'bgs_paired_box_cancellation/selected_weighted_sources.json'
entries=json.loads(manifest.read_text())['files']; mismatches=[]
for entry in entries:
    path=ROOT/entry['path']; digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest!=entry['sha256']:mismatches.append({'path':str(path),'expected':entry['sha256'],'actual':digest})
assert not mismatches
res={'arithmetic':'exact integer/Fraction; independent implementation',
     'scope':'m=1..64; 49 lifted label samples per m; all cyclic/negative pulse orbit points; odd-N test list is finite',
     'identities_checked':checks,'manifest_entries_verified':len(entries),'mismatches':mismatches,'rows':rows,
     'editorial_note':'Real-lift Q(Sz)-Q(z) has mixed coefficient -8; candidate -10 remains congruent modulo integers.',
     'nonclaims':'Not exhaustive over all label pairs, not analytic or asymptotic verification.'}
(OUT/'combined_interface_results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'passed':True,'identities_checked':checks,'manifest_entries_verified':len(entries),'m_range':[1,64]}))
