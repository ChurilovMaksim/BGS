import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path

def plus(a,b):
    out=dict(a)
    for q,v in b.items():out[q]=out.get(q,F(0))+v
    return {q:v for q,v in out.items() if v}
def times(a,b):
    out={}
    for q,x in a.items():
        for r,y in b.items():out[q+r]=out.get(q+r,F(0))+x*y
    return {q:v for q,v in out.items() if v}
def scale(a,c):return {q:v*c for q,v in a.items() if v*c}
def onecycle(p):
    x=0;seen=set()
    while x not in seen:seen.add(x);x=p[x]
    return len(seen)==len(p) and x==0

def main(destination):
    kernels=json.loads(Path('dependencies/full_port_reference.json').read_text())['summary'][1]['polynomials']
    u,v,vinv,t=[{int(q):F(a) for q,a in pol.items()} for pol in kernels];assert v==vinv
    order=[(0,1,2),(1,2,0),(2,0,1),(1,0,2),(2,1,0),(0,2,1)]
    shuffles=[]
    for rest in itertools.permutations(range(1,6)):
        word=(0,)+rest
        if tuple(x for x in word if x<3)!=(0,1,2):continue
        if tuple(x-3 for x in word if x>=3) not in ((0,1,2),(1,2,0),(2,0,1)):continue
        g=[0]*6
        for a,b in zip(word,word[1:]+word[:1]):g[a]=b
        shuffles.append(g)
    assert len(shuffles)==30
    matrix=[]
    for a in order:
        row=[]
        for b in order:
            pi=list(a)+[x+3 for x in b]
            row.append(sum(onecycle([g[pi[i]] for i in range(6)]) for g in shuffles))
        matrix.append(row)
    assert matrix==[list(row) for row in zip(*matrix)]
    p=[u,v,v,scale(t,F(1,3)),scale(t,F(1,3)),scale(t,F(1,3))]
    total={}
    for i in range(6):
        for j in range(6):total=plus(total,scale(times(p[i],p[j]),F(matrix[i][j],2)))
    compact=plus(plus(scale(times(plus(u,v),plus(u,v)),15),scale(times(v,v),3)),scale(times(t,t),5))
    assert total==compact
    assert sum(total.values())==0 and sum(q*a for q,a in total.items())==0
    jet=sum(F(q*(q-1),2)*a for q,a in total.items());assert jet==F(1061,8)
    assert total[6]==F(20,27) and total[9]==F(5,27)
    # Pure passive normalization, counted directly as partitions of six labels into two triples.
    partitions={tuple(sorted((tuple(sorted(s)),tuple(i for i in range(6) if i not in s)))) for s in itertools.combinations(range(6),3)}
    assert len(partitions)==10 and F(len(partitions),6)*F(2,3)**2==total[6]
    data={'status':'passed_exact_gluing_arithmetic','boundary_permutation_order':[list(p) for p in order],
          'gluing_matrix':matrix,'cyclic_shuffles':shuffles,'P42':{str(q):str(a) for q,a in sorted(total.items())},
          'double_zero':True,'quotient_value_at_one':str(jet),
          'compact_formula':'15*(P_identity+P_rho)^2+3*P_rho^2+5*P_transpositions_aggregate^2',
          'scope':'Exact gluing arithmetic and passive normalization; structural completeness is a separate proof.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='cyclic_shuffles'}))

if __name__=='__main__':main(sys.argv[1])
