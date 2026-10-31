"""N12 (1c) [CA*-float]: ALL ordered two-bump merged types up to centre distance Gmax (p-independent):
types T = {odd(e=2), sq2(2sqrt2), two(4), 2sq2(4sqrt2), four(8)}, composite e = e_i + s * e_j * eps^h * lam^G, s=+-1, h in {0,1}.
Per type: window weights rA,rB (Line F sector-4 Galerkin operator, float), ratio (R_A R_B)^3 vs singles.
usage: d_merged.py i_type_list Gmax   (i_type_list comma-separated; j runs over all types)"""
import sys, json
sys.argv_saved=list(sys.argv)
sys.argv=['c_pairs.py','A','0']
src=open('/workspace/bgs-lineN/N12/code/c_pairs.py').read().split('pairset=sys.argv')[0]
exec(src)
sys.argv=sys.argv_saved
ilist=sys.argv[1].split(','); Gmax=int(sys.argv[2])
EPS=(1,1)
rows=[]
for ti in ilist:
    for tj in TYPES:
        for h in (0,1):
            for sg in (1,-1):
                for G in range(1 if h==0 else 0, Gmax+1):
                    ej=mulq(TYPES[tj],lamp(G))
                    if h: ej=mulq(ej,EPS)
                    e=(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])
                    rA,rB=win(e)
                    sjA,sjB=(win(mulq(TYPES[tj],EPS)) if h else single[tj])
                    RA=rA/(single[ti][0]*sjA); RB=rB/(single[ti][1]*sjB)
                    ratio=(RA*RB)**3
                    rows.append(dict(i=ti,j=tj,h=h,s=sg,G=G,cls=[ratio.real,ratio.imag],dev=abs(ratio-1),RA=abs(RA-1),RB=abs(RB-1)))
    print(ti,'done',len(rows),flush=True)
json.dump(dict(Gmax=Gmax,rows=rows,single={k:[[v[0].real,v[0].imag],[v[1].real,v[1].imag]] for k,v in single.items()}),
          open(f'/workspace/bgs-lineN/N12/logs/d_merged_{sys.argv[1].replace(",","_")}.json','w'))
