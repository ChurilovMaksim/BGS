"""Bounded rerun, preserving the earlier cap-limited source and receipt."""
import importlib.util
import itertools
import json
from pathlib import Path
import time
import sympy as sp
import exact_ordered_check as exact

out=Path('checks/completed_run/results.json')
result={'status':'in progress','exact_literal_rows':[],'complex_rational_rows':[],'non_claims':['No finite range proves the asymptotic bound.','No actual fixed-tau numerical approximation.','No full balanced or decorated extension.']}

def save():out.write_text(json.dumps(result,indent=2)+'\n')

def full_support_four():
    n,m=3,4
    words=list(itertools.product(range(n),repeat=m))
    permutations=list(itertools.permutations(range(m)))
    def ncycles(p):
        left=set(range(m)); count=0
        while left:
            a=next(iter(left));count+=1
            while a in left:left.remove(a);a=p[a]
        return count
    def overlap(p,q):
        inv=[p.index(j) for j in range(m)]
        return n**ncycles([inv[q[j]] for j in range(m)])
    gram=sp.Matrix([[overlap(p,q) for q in permutations] for p in permutations])
    selected=gram.rref()[1]
    zperms=[permutations[j] for j in selected]
    gz=gram.extract(selected,selected)
    local=[[1,-1,0],[1,1,-2]]
    labels=list(itertools.product(range(2),repeat=m))
    def prod(xs):
        a=1
        for x in xs:a*=x
        return a
    b=sp.Matrix([[sum(prod(local[label[j]][word[j]] for j in range(m)) for word in words if all(word[j]==word[p[j]] for j in range(m))) for label in labels] for p in zperms])
    mass=sp.diag(*[prod(2 if j==0 else 6 for j in label) for label in labels])
    h=mass.inv()*b.T*gz.inv()*b
    vals=h.eigenvals()
    exact.require(all(v.is_rational and 0<=v<=sp.Rational(1,n+1) for v in vals),'ordered fourth moment bound')
    ix={v:i for i,v in enumerate(labels)}
    symmetric=sp.zeros(2**m)
    for p in permutations:
        for j,label in enumerate(labels):symmetric[ix[tuple(label[p[k]] for k in range(m))],j]+=sp.Rational(1,24)
    exact.require(h.rank()==3,'unexpected full ordered H4 rank')
    exact.require((symmetric*h).rank()==1,'unexpected symmetric H4 rank')
    exact.require((sp.eye(16)-symmetric)*h!=sp.zeros(16),'test accidentally restricted to Sym4')
    exact.require((mass*(sp.eye(16)-h)).det()!=0,'fourth Gram singular')
    return {'N':3,'m':4,'arithmetic':'exact rational physical-permutation Gram contractions','Haar_rank':len(selected),'full_support_dimension':16,'H4_rank':h.rank(),'symmetric_H4_rank':(symmetric*h).rank(),'H4_spectrum':{str(k):v for k,v in vals.items()},'full_End_dimension':3**8}

def complex_case(n,m):
    words,labels,dim,basis,z,gz,diag,mass,overlap,h,g,cycle,r=exact.objects(n,m)
    a=sp.Matrix(range(1,n+1)); b=sp.Matrix([2*j*j+1 for j in range(n)])
    ha=sp.eye(n)-2*a*a.T/a.dot(a);hb=sp.eye(n)-2*b*b.T/b.dot(b)
    phases=[sp.Integer(1)]*(n-1)+[sp.Rational(3,5)+sp.I*sp.Rational(4,5)]
    u=(ha*sp.diag(*phases)*hb).applyfunc(sp.expand)
    exact.require((u*u.conjugate().T).applyfunc(sp.simplify)==sp.eye(n),'complex fixture not unitary')
    p=u.multiply_elementwise(u.conjugate()).applyfunc(sp.simplify)
    big=exact.tensor([u]*m)
    f=sp.Matrix.hstack(*[exact.flat(sp.diag(*diag[:,j])) for j in range(len(labels))])
    y=f-z*gz.inv()*overlap
    rc=[]
    for j in range(y.cols):
        x=sp.Matrix(dim,dim,list(y[:,j]))
        rc.append(exact.flat(cycle*big*x*big.conjugate().T*cycle.T))
    direct=sp.simplify(sp.trace(g.inv()*y.T*sp.Matrix.hstack(*rc)))
    actual=mass.inv()*diag.T*exact.tensor([p]*m)*diag
    expected=sp.trace(r*(sp.eye(len(labels))-h).inv()*(actual-h))
    exact.require(sp.simplify(direct-expected)==0,'complex direct/reduced mismatch')
    exact.require(sp.im(direct)==0,'complex trace not real')
    return {'N':n,'m':m,'arithmetic':'exact Q(i)','trace':str(direct),'genuinely_complex':any(sp.im(x)!=0 for x in u),'nonnormal_P':p*p.T!=p.T*p}

start=time.monotonic()
for n,m in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2)]:
    t=time.monotonic(); row=exact.check(n,m)
    result['exact_literal_rows'].append(row);save()
    print('literal passed',n,m,'seconds',time.monotonic()-t,flush=True)
result['full_ordered_fourth_moment']=full_support_four();save()
print('ordered N3 m4 Gram passed',flush=True)
for n,m in [(2,3),(3,2)]:
    result['complex_rational_rows'].append(complex_case(n,m));save()
    print('complex passed',n,m,flush=True)
result['product_trace_controls']=exact.low_dimension_products();save()
source=Path('frozen/bgs_ordered_diagonal_route/check_ordered.py')
spec=importlib.util.spec_from_file_location('author_floating',source)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
oldrows=json.loads(Path('frozen/bgs_ordered_diagonal_route/checks.json').read_text())
replay=[]
for old in oldrows:
    row=module.check(old['N'],old['m'])
    for key,value in row.items():
        exact.require(abs(value-old[key])<=2e-10,('floating replay discrepancy',key))
    replay.append(row)
Path('checks/completed_run/author_floating_replay.json').write_text(json.dumps({'arithmetic':'IEEE double with tolerance 2e-10; separate replay of author code','rows':replay},indent=2)+'\n')
result['status']='all finite assertions passed';result['elapsed_seconds']=time.monotonic()-start;save()
print(json.dumps(result,indent=2),flush=True)
