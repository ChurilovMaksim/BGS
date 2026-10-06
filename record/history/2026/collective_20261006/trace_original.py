#!/usr/bin/env python3
"""Exact ambient End-space checks of two-sided cycle, Haar subtraction and trace."""
import sys, json,time,itertools as it
from pathlib import Path
import sympy as s
sys.path.insert(0,str(Path(__file__).parent))
from ordered_space_check import parts,compositions,cycle_type,insertion

def run(N,m):
    words=list(it.product(range(N),repeat=m)); wi={w:i for i,w in enumerate(words)}; D=len(words)
    cs=list(parts(m)); operators={c:s.zeros(D) for c in cs}
    cyc=s.zeros(D)
    for j,w in enumerate(words):cyc[wi[w[1:]+w[:1]],j]=1
    for p in it.permutations(range(m)):
        A=operators[cycle_type(p)]
        for j,w in enumerate(words):A[wi[tuple(w[p[k]] for k in range(m))],j]+=1
    ops=list(operators.values()); gram=s.Matrix([[s.trace(a.T*b) for b in ops] for a in ops]); piv=gram.rref()[1]; ops=[ops[i] for i in piv]; gram=gram.extract(piv,piv)
    v=s.Matrix(range(1,N+1));w=s.Matrix([2]+[1]*(N-1)); U=(s.eye(N)-2*v*v.T/(v.T*v)[0])*(s.eye(N)-2*w*w.T/(w.T*w)[0]);assert U*U.T==s.eye(N)
    P=U.applyfunc(lambda x:x*x); T=P-s.ones(N)/N
    Un=U
    for _ in range(m-1):Un=s.kronecker_product(Un,U)
    assert s.trace(cyc*Un)**2==s.trace(U**m)**2
    bydegree=[]; Ys=[]
    for q in range(1,m+1):
        basis=list(compositions(q,N-1));Js=[s.diag(*[insertion(x,N).get(a,0) for x in words]) for a in basis]
        V=s.Matrix([[s.trace(op.T*j) for j in Js] for op in ops]); projection=gram.inv()*V
        Y=[j-sum((projection[a,b]*op for a,op in enumerate(ops)),s.zeros(D)) for b,j in enumerate(Js)]
        for y in Y:
            assert cyc*y*cyc.T==y
            assert all(s.trace(op.T*y)==0 for op in ops)
        G=s.Matrix([[s.trace(a.T*b) for b in Y] for a in Y])
        actual=[Un*y*Un.T for y in Y]
        A=s.Matrix([[s.trace(a.T*cyc*b*cyc.T) for b in actual] for a in Y])
        raw=s.Matrix([[s.trace(a.T*b) for b in Js] for a in Js]); inv=V.T*gram.inv()*V
        rawactual=s.Matrix([[s.trace(a.T*Un*b*Un.T) for b in Js] for a in Js])
        assert G==raw-inv and A==rawactual-inv
        sector=s.factor(s.trace(G.inv()*A))
        h=raw.inv()*inv; sym=raw.inv()*rawactual
        assert sector==s.trace((s.eye(len(basis))-h).inv()*(sym-h))
        # Independent symmetric-power action in the unnormalized distinct-tensor basis.
        diagonals=s.Matrix([[int(i==j)-int(i==N-1) for j in range(N-1)] for i in range(N)])
        Td=(P*diagonals)[:N-1,:]
        variables=s.symbols('x:'+str(N-1)); representation=s.zeros(len(basis))
        for j,b in enumerate(basis):
            polynomial=s.Poly(s.prod(sum(Td[i,k]*variables[i] for i in range(N-1))**b[k] for k in range(N-1)),*variables)
            mult_b=mathcomb_mult(q,b)
            for i,a in enumerate(basis):representation[i,j]=polynomial.coeff_monomial(s.prod(variables[k]**a[k] for k in range(N-1)))*s.Rational(mult_b,mathcomb_mult(q,a))
        assert sym==representation
        if q==1:assert sector==s.trace(T)
        if q==2:
            formula=((s.trace(T))**2+s.trace(T*T))/2+s.trace(T.T*T)/(N*(N-1))-s.Rational(1,N)
            assert sector==formula
        bydegree.append({'q':q,'trace_exact':str(sector)})
        Ys.extend(Y)
    # Haar contribution uses exact trace of the two-sided cycle on all permutation invariants.
    perms=[]
    for p in it.permutations(range(m)):
        op=s.zeros(D)
        for j,w in enumerate(words):op[wi[tuple(w[p[k]] for k in range(m))],j]=1
        perms.append(op)
    FG=s.Matrix([[s.trace(a.T*b) for b in perms] for a in perms]);fp=FG.rref()[1];perms=[perms[i] for i in fp];FG=FG.extract(fp,fp)
    Fcycle=s.Matrix([[s.trace(a.T*cyc*b*cyc.T) for b in perms] for a in perms]); haar=s.trace(FG.inv()*Fcycle)
    assert haar==min(N,m)
    rankcoll=sum(mathcomb(N+q-2,q) for q in range(1,m+1))
    rankQ=N**(2*m)-len(perms)-rankcoll
    return {'N':N,'m':m,'actual_trace_squared':str(s.trace(U**m)**2),'haar_cycle_trace':str(haar),'collective_trace':str(sum(s.Rational(x['trace_exact']) for x in bydegree)),'degree_traces':bydegree,'full_Haar_rank':len(perms),'collective_rank':rankcoll,'orthogonal_complement_rank':rankQ,'P_nonnormal':P*P.T!=P.T*P}
from math import comb as mathcomb, factorial
def mathcomb_mult(q,a):return factorial(q)//math.prod(factorial(x) for x in a)
import math
if __name__=='__main__':
    start=time.perf_counter(); rows=[]
    for pair in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)]:
        rows.append(run(*pair));print(f'passed {pair}',file=sys.stderr,flush=True)
    print(json.dumps({'arithmetic':'exact integer/rational SymPy matrix algebra','unitaries':'product of two rational Householder reflections','rows':rows,'runtime_seconds':time.perf_counter()-start,'non_claims':['Finite identities only','No literal tau evaluation','No limiting assertion']},indent=2))
