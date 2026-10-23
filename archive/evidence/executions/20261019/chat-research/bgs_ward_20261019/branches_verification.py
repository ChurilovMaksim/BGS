import functools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from gluing_check import plus,times,scale
from dependencies.first_defect_verification import P1

def trim(a):
    while a and not a[-1]:a.pop()
    return a
def ay(a,b,sign=1):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=sign*x
    return trim(c)
def my(a,b):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def divide_one_minus_z(p):
    out={};running=F(0)
    for q in range(max(p)+1):
        running+=p.get(q,F(0))
        if running:out[q]=running
    assert running==0
    return out
def expectation(a,N,shift):
    a=[0]*shift+a;acc=F(0)
    for k in range(len(a)-1,-1,-1):acc=a[k]+F(2*k+1,2*N)*acc
    return acc

def main(destination):
    h2=json.loads(Path('dependencies/h2_core_table.json').read_text());polys22=[]
    for p in h2['primes']:
        pol={r['q']:F(r['histogram12'][2],12*r['q']) for r in h2['open_core_histograms'] if r['p']==p and r['histogram12'][2]}
        polys22.append(pol)
    assert all(p==polys22[0] for p in polys22)
    channels=json.loads(Path('dependencies/full_port_reference.json').read_text())['summary'][1]['polynomials']
    u,v=[{int(q):F(a) for q,a in p.items()} for p in channels[:2]]
    p42={int(q):F(a) for q,a in json.loads(Path('dependencies/gluing_reference.json').read_text())['P42'].items()}
    prim={2:polys22[0],3:scale(times(P1,plus(u,v)),3),4:p42};quot={};jets={}
    for j,p in prim.items():
        q=p
        for _ in range(j-2):q=divide_one_minus_z(q)
        quot[j]=q;jets[j]=sum(q.values(),F(0))
    assert jets=={2:F(23,12),3:F(-35,4),4:F(1061,8)}
    Ns=(49,169,625);ratios=(F(1,2),F(9,10));M=max(int(N*t) for N in Ns for t in ratios)
    Q=[[1],[-1],[0,1],[0,1],[0,1],[0,1]];denom=[[1]];recip={};prefix={}
    for k in range(1,7):
        new=[[] for _ in range(len(denom)+5)]
        for i,a in enumerate(denom):
            for d,b in enumerate(Q):new[i+d]=ay(new[i+d],my(a,b))
        denom=new
        if k<2:continue
        r=[[1]]
        for m in range(1,M+1):
            a=[]
            for d in range(1,min(m,len(denom)-1)+1):a=ay(a,my(denom[d],r[m-d]),-1)
            r.append(a)
        recip[k]=r
        if k in (2,4,6):
            pref=[];running=[]
            for a in r:running=ay(running,a);pref.append(running)
            prefix[k]=pref
    D={q:F(1) for q in range(2,6)};Dpow=[{0:F(1)}]
    for _ in range(3):Dpow.append(times(Dpow[-1],D))
    @functools.lru_cache(None)
    def gauss(k,m,b,is_prefix,N):
        if m<0:return F(0)
        return expectation((prefix if is_prefix else recip)[k][m],N,b)
    def rational(j,m,N):
        e=2*j-2;v=j-2;total=F(0)
        for b in range(v+1):
            c=(-1)**b*sum(math.comb(e,2*k)*math.comb(v-k,b-k) for k in range(b+1))
            for q,a in times(quot[j],Dpow[b]).items():
                if m>=q:total+=c*a*gauss(j+b,m-q,b,False,N)
        b=j-1
        for q,a in times(quot[j],Dpow[b]).items():
            if m>=q:total+=(-1)**b*a*gauss(e,m-q,b,True,N)
        return F(m,N**j)*total
    def direct(j,m,N):
        out=F(0)
        for n in range(max(0,(m-min(prim[j]))//2+1)):
            h=j+n;e=2*j-2;factor=F(math.factorial(e+2*n-1),math.factorial(e-1)*4**n*math.factorial(n)*N**h)
            power={2*n+4*g:F(math.comb(n,g)*(-1)**(n-g)) for g in range(n+1)}
            numerator=times(prim[j],power);den=2*h-2
            out+=m*factor*sum((a*math.comb(m-q+den-1,den-1) for q,a in numerator.items() if m>=q),F(0))
        return out
    identities=0
    for N in (7,19,101):
        for m in range(6,37):
            for j in (2,3,4):assert rational(j,m,N)==direct(j,m,N),(j,m,N);identities+=1
    def limit(j,t):
        r=1+4*t;c=float(jets[j])
        if j==2:return c*t/2*(1-r**(-.5))
        if j==3:return c*t/8*(F(2,3)-r**(-.5)+r**(-1.5)/3)
        return c*t/64*(F(8,15)-r**(-.5)+2*r**(-1.5)/3-r**(-2.5)/5)
    rows=[]
    for N in Ns:
        for target in ratios:
            m=int(N*target);t=float(F(m,N))
            for j in (2,3,4):
                value=rational(j,m,N);lim=float(limit(j,t))
                rows.append({'primitive_order':j,'N':N,'m':m,'target_ratio':str(target),'value_exact':str(value),'value_display':float(value),'limit_at_actual_ratio':lim,'difference':float(value)-lim})
    data={'status':'passed_exact_branch_identities','identity_cases':identities,
          'primitive_polynomials':{str(j):{str(q):str(a) for q,a in p.items()} for j,p in prim.items()},
          'quotient_values_at_one':{str(j):str(a) for j,a in jets.items()},'finite_values':rows,
          'scope':'Three specified families of delta=2, with primitive j=3 restricted to disconnected clusters. Analytic limits are proved separately.'}
    Path(destination).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('primitive_polynomials','finite_values')}))
    print(json.dumps([{k:v for k,v in r.items() if k!='value_exact'} for r in rows]))

if __name__=='__main__':main(sys.argv[1])
