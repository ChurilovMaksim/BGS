"""Search for monomial matrices (permutation x 56th-root phases) commuting with all A_n. Exact integer arithmetic.
A_n given as (out,in,ph8,tw) -> entry e(-ph8/8 + n tw/7) = e((-7 ph8 + 8 n tw)/56)."""
import sys, itertools, json
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach, taus7, finite
m=int(sys.argv[1]); a=int(sys.argv[2]); cls=sys.argv[3]
P=g2params(m,a,8); idx,tg=reach(P,60); cyc=None if cls=='none' else taus7(*[int(t) for t in cls.split(':')])
NS=len(idx)*(1 if cyc is None else 3)
A={}
for n in range(56):
    mp={}
    for (o,i,ph8,tw) in finite(P,idx,tg,n,cyc):
        assert i not in mp; mp[i]=(o,(-7*ph8+8*n*tw)%56)
    A[n]=mp   # column i -> (row, phase exp)
# monomial Y: column i -> (sigma(i), phi(i)).  Y A = A Y:  Y A e_i = Y (ph_A(i) e_{A(i)}) = ph_A(i) ph_Y(A(i)) e_{sY(A(i))}
#   A Y e_i = ph_Y(i) ph_A(sY(i)) e_{A(sY(i))}.  Need sY(A(i)) = A(sY(i)) and phA(i)+phY(A(i)) = phY(i)+phA(sY(i)) mod 56.
sols=[]
for s0 in range(NS):
    # determine sigma from sigma(0)=s0 by connectivity, phases from phi(0)=0 (overall scalar free)
    sig={0:s0}; phi={0:0}; fr=[0]; ok=True
    while fr and ok:
        i=fr.pop()
        for n in range(56):
            j,pa=A[n][i]; sj=A[n][sig[i]][0]; pa2=A[n][sig[i]][1]
            # need sig(j)=A_n(sig(i)) and phi(j) = phi(i)+pa2-pa
            pj=(phi[i]+pa2-pa)%56
            if j in sig:
                if sig[j]!=sj or phi[j]!=pj: ok=False; break
            else: sig[j]=sj; phi[j]=pj; fr.append(j)
    if ok and len(sig)==NS and len(set(sig.values()))==NS: sols.append((s0,[sig[i] for i in range(NS)],[phi[i] for i in range(NS)]))
print('NS',NS,'monomial commuting (up to scalar):',len(sols))
for s in sols: print(s[0],s[1],s[2])
json.dump(sols,open(f'/workspace/bgs-lineJ/logs/monocomm_{m}_{a}_{cls.replace(":","")}.json','w'))
