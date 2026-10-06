#!/usr/bin/env python3
"""Fresh exact audit. No author-verifier or FM-009 code is imported.

Definitions transcribed from fixed_model_symmetry_theorem.md, Section 1.
Cyclotomics use integer divisor-product recursion, not the author's prime
recursion. Matrix controls use directly evaluated Jacobi entries in the
cyclotomic field Q(zeta_(4N)), not a finite-field specialization.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math, platform, sys, time

AUTHOR = None
OUTPUTS = {}

def require(c, msg):
    if not c:
        raise ValueError(msg)

def save(name, value):
    OUTPUTS[name] = value

def trim(p):
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p

def pdiv(a, b, binary=False):
    a, b = trim(list(a)), trim(list(b))
    require(b[-1] == 1, 'monic divisor')
    q = [0] * max(1, len(a)-len(b)+1)
    for k in range(len(a)-len(b), -1, -1):
        c = a[k+len(b)-1]
        q[k] = c
        if c:
            for j, x in enumerate(b):
                a[k+j] -= c*x
                if binary:
                    a[k+j] %= 2
    return trim(q), trim(a)

def pmul(a,b):
    p = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                p[i+j] += x*y
    return trim(p)

PHI = {}
def cyclo(n):
    if n in PHI:
        return PHI[n]
    p = [-1]+[0]*(n-1)+[1]
    # X^n-1 = product_{d|n} Phi_d, independently in Z[X].
    for d in range(1,n):
        if n%d == 0:
            p,r = pdiv(p,cyclo(d))
            require(r == [0], f'integer cyclotomic exact division {n}/{d}')
    PHI[n] = p
    return p

def gadd(z,w):
    return z[0]+w[0], z[1]+w[1]

def gmul(z,w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def sadd(*polys):
    ans = defaultdict(lambda:(F(0),F(0)))
    for p in polys:
        for v,z in p.items():
            ans[v] = gadd(ans[v],z)
    return {v:z for v,z in ans.items() if z != (0,0)}

def sscale(p,z):
    return {v:gmul(a,z) for v,a in p.items() if gmul(a,z)!=(0,0)}

def smul(p,q):
    ans = defaultdict(lambda:(F(0),F(0)))
    for (a,b),z in p.items():
        for (c,d),w in q.items():
            ans[a+c,b+d] = gadd(ans[a+c,b+d],gmul(z,w))
    return {v:z for v,z in ans.items() if z != (0,0)}

def raw_from_trigonometry():
    # Keys are directly (p frequency, q frequency), hence T_N(a,b).
    one = {(0,0):(F(1),F(0))}
    cos1 = {(0,1):(F(1,2),F(0)),(0,-1):(F(1,2),F(0))}
    cos7 = {(0,7):(F(1,2),F(0)),(0,-7):(F(1,2),F(0))}
    sin1 = {(0,1):(F(0),F(-1,2)),(0,-1):(F(0),F(1,2))}
    cos_p_alpha = {(1,0):(F(-3,10),F(-2,5)),
                   (-1,0):(F(-3,10),F(2,5))}
    r = smul(sadd(one,sscale(cos7,(-1,0))),sadd(one,cos1))
    a = sadd(cos7,sscale(r,(F(1,10),0)),
             sscale(smul(r,sin1),(F(1,100),0)),
             sscale(smul(r,cos_p_alpha),(F(1,100),0)),
             sscale(one,(F(-1,10),0)))
    d = sscale(a,(4000,0))
    require(all(x.denominator==1 for z in d.values() for x in z),'integer coefficients')
    return {v:tuple(map(int,z)) for v,z in d.items()}

def quadratic(v):
    a,b = v
    return 2*b*b-a*a

def independent_polynomial(d):
    p = defaultdict(lambda:(0,0))
    for (a,b),z in d.items():
        for (c,e),w in d.items():
            u = gmul(z,w)
            # Direct completion of the raw T_v T_w M exponent, scaled by 4.
            e1 = 2*(b+e)**2-(a+c)**2+2*(a*e-b*c)
            e2 = 2*b*b-a*a+2*e*e-c*c
            p[e1] = gadd(p[e1],u)
            p[e2] = gadd(p[e2],(-u[0],-u[1]))
    require(all(z[1]==0 for z in p.values()),'real integer P')
    return {k:z[0] for k,z in sorted(p.items()) if z!=(0,0)}

def cadd(a,b,m,scale=1):
    r = dict(a)
    for k,v in b.items():
        k %= m
        r[k] = r.get(k,0)+scale*v
        if not r[k]:
            del r[k]
    return r

def cmul(a,b,m):
    r = defaultdict(int)
    for i,x in a.items():
        for j,y in b.items():
            r[(i+j)%m] += x*y
    return {i:x for i,x in r.items() if x}

def mon(e,m,c=1):
    return {e%m:c} if c else {}

def reduce_c(a,n):
    p = [0]*(4*n)
    for k,v in a.items():
        p[k%(4*n)] += v
    return pdiv(p,cyclo(4*n))[1]

def matrix_control(n, d, p):
    """Exact identities over Q[X]/Phi_(4N), X mapped to zeta_(4N)."""
    m=4*n
    h=pow(2,-1,n)
    inv8=pow(8,-1,n)
    inv4=pow(4,-1,n)
    def root(a,c=1): return mon(4*a,m,c)
    def kernel(x,y): return root(-inv8*(3*x*x-2*x*y+3*y*y))
    def r4(x):
        # 4r(x/N) = (2-zeta^(7x)-zeta^(-7x))(2+zeta^x+zeta^(-x)).
        a=cadd(cadd({0:2},root(7*x),m,-1),root(-7*x),m,-1)
        b=cadd(cadd({0:2},root(x),m),root(-x),m)
        return cmul(a,b,m)
    def row(x):
        r=r4(x)
        diag=cadd(root(7*x,2000),root(-7*x,2000),m)
        diag=cadd(diag,r,m,100)
        sine=cadd(root(x),root(-x),m,-1)
        diag=cadd(diag,cmul(cmul(r,sine,m),mon(n,m,-5),m),m)
        diag=cadd(diag,{0:-400},m)
        plus=cmul(cadd({0:-3},mon(n,m,-4),m),r4(x+h),m)
        minus=cmul(cadd({0:-3},mon(n,m,4),m),r4(x-h),m)
        ans={}
        for y,v in ((x,diag),((x+1)%n,plus),((x-1)%n,minus)):
            ans[y]=cadd(ans.get(y,{}),v,m)
        return ans
    B=[row(x) for x in range(n)]
    k0,k1,k2={},{},{}
    for x in range(n):
        k0=cadd(k0,kernel(x,x),m)
        for y,bxy in B[x].items():
            k1=cadd(k1,cmul(bxy,kernel(y,x),m),m)
            for z,byz in B[y].items():
                k2=cadd(k2,cmul(cmul(bxy,byz,m),kernel(z,x),m),m)
    lhs=cadd(cmul(k0,k2,m),cmul(k1,k1,m),m,-1)
    evalp={}
    for k,v in p.items():
        evalp=cadd(evalp,root(inv4*k,v),m)
    rhs=cmul(cmul(k0,k0,m),evalp,m)
    rem=reduce_c(cadd(lhs,rhs,m,-1),n)
    require(rem==[0],f'direct Jacobi matrix contraction N={n}')
    # Independently verify every raw Weyl character with actual kernel entries.
    for (a,b) in d:
        tr={}
        for x in range(n):
            tr=cadd(tr,cmul(root(b*(x+h*a)),kernel((x+a)%n,x),m),m)
        predicted=cmul(k0,root(inv4*(2*b*b-a*a)),m)
        require(reduce_c(cadd(tr,predicted,m,-1),n)==[0],f'raw character {n} {a,b}')
    # Full row equality to raw Weyl assembly (includes every modular alias).
    for x in range(n):
        raw={}
        for (a,b),(u,v) in d.items():
            coeff=cadd(mon(0,m,u),mon(n,m,v),m)
            entry=cmul(coeff,root(b*(x+h*a)),m)
            y=(x+a)%n
            raw[y]=cadd(raw.get(y,{}),entry,m)
        for y in set(raw)|set(B[x]):
            require(reduce_c(cadd(raw.get(y,{}),B[x].get(y,{}),m,-1),n)==[0],f'raw/Jacobi mismatch N={n}')
    # Weyl-cocycle phase checked at all x and all raw ordered mode pairs.
    for a,b in d:
        for c,e in d:
            for x in range(n):
                direct=b*(x+h*a)+e*(x+a+h*c)
                predicted=(b+e)*(x+h*(a+c))+h*(a*e-b*c)
                require((direct-predicted)%n==0,f'cocycle {n}')
    # Characteristic-zero negative control: adding 2 at exponent zero cannot pass.
    corrupt_difference=reduce_c(cmul(k0,k0,m),n)
    require(corrupt_difference!=[0],f'negative control N={n}')
    hn=reduce_c(lhs,n)
    require((hn==[0])==(n==7),f'H direct nonvanishing N={n}')
    if n==7:
        for x in range(n):
            for y,v in B[x].items():
                require(reduce_c(cadd(v,{0:3600} if x==y else {},m,-1),n)==[0],'A7 exact')
    return {'N':n,'field':'Q(zeta_(4N))','field_degree':len(cyclo(4*n))-1,
            'raw_jacobi_equal':True,'all_32_characters':True,
            'all_1024_cocycles_at_every_row':True,'trace_variance_identity':True,
            'direct_H_zero':hn==[0],'coefficient_corruption_rejected':True,
            'H_unnormalized_remainder_ascending':hn}

def main():
    started=time.time()
    d=raw_from_trigonometry()
    require(len(d)==32,'raw mode count')
    require(all(d[-a,-b]==(u,-v) for (a,b),(u,v) in d.items()),'Hermitian coefficients')
    raw=[{'mode':list(v),'scaled_coefficient':list(z)} for v,z in sorted(d.items())]
    require(raw==json.loads((AUTHOR/'raw_coefficients.json').read_text()),'author coefficient mismatch')
    save('raw_coefficients.json',raw)
    p=independent_polynomial(d)
    require([[k,v] for k,v in p.items()]==json.loads((AUTHOR/'polynomial_sparse.json').read_text()),'author P mismatch')
    save('polynomial_sparse.json',list(map(list,p.items())))
    lo,hi=min(p),max(p)
    content=math.gcd(*p.values())
    R=[p.get(k,0)//content for k in range(lo,hi+1)]
    require(R==json.loads((AUTHOR/'primitive_polynomial_ascending.json').read_text()),'author R mismatch')
    save('primitive_polynomial_ascending.json',R)
    require((lo,hi,content,len(p),sum(map(abs,p.values())))==(-36,648,2,143,40256624),'polynomial constants')
    bound=(len(R)-1)*F(17017,6144)
    require(math.floor(bound)==1894,'integer bound')
    # Full gcd enumeration of totient at every odd n <= the proved bound.
    screens=[]
    R2=[v%2 for v in R]
    require(len(trim(list(R2)))==685,'mod2 degree')
    for n in range(1,1895,2):
        phi=sum(math.gcd(k,n)==1 for k in range(1,n+1))
        c=cyclo(n)
        require(len(c)-1==phi,f'Phi degree n={n}')
        if phi<=684:
            _,r=pdiv(R2,[x%2 for x in c],binary=True)
            bits=sum(v<<j for j,v in enumerate(r))
            screens.append({'order':n,'totient':phi,'remainder_F2_hex':hex(bits)})
    require(screens==json.loads((AUTHOR/'all_odd_order_F2_remainders.json').read_text()),'full author screen mismatch')
    require(len(screens)==446,'eligible order count')
    survivors=[v['order'] for v in screens if v['remainder_F2_hex']=='0x0']
    require(survivors==[1,7],'cyclotomic survivors')
    save('all_odd_order_F2_remainders.json',screens)
    divisions={}
    for n in survivors:
        cur=list(R); qs=[]
        while True:
            q,r=pdiv(cur,cyclo(n))
            if r != [0]:
                break
            require(pmul(q,cyclo(n))==cur,'quotient product')
            qs.append(q);cur=q
        require(len(qs)==2,'multiplicity')
        divisions[str(n)]={'multiplicity':len(qs),'quotients_ascending':qs,'next_remainder_ascending':r}
    save('integer_cyclotomic_division.json',divisions)
    require(divisions['1']['next_remainder_ascending']==[101317436416],'Phi1 remainder')
    require(divisions['7']['next_remainder_ascending']==[-15043392,2469131168,-5071846528,1851639440,1156209488,-612458448],'Phi7 remainder')
    V,rem=pdiv(R,[1]+[0]*6+[-2]+[0]*6+[1])
    require(rem==[0] and len(V)==671 and sum(V)==2067702784,'factor (z7-1)^2')
    require(V==json.loads((AUTHOR/'quotient_by_z7_minus1_squared_ascending.json').read_text()),'author V mismatch')
    save('quotient_by_z7_minus1_squared_ascending.json',V)
    alias=defaultdict(lambda:(0,0))
    for (a,b),z in d.items(): alias[a%7,b%7]=gadd(alias[a%7,b%7],z)
    alias={v:z for v,z in alias.items() if z!=(0,0)}
    require(alias=={(0,0):(3600,0)},'N7 alias')
    dims=[3,5,7,9,21,25,27,35,45,49,63,77,105,121,125]
    controls=[]
    print('Independent raw symbol, complete Laurent polynomial, 446 screens, and exact divisions passed.',flush=True)
    for n in dims:
        controls.append(matrix_control(n,d,p))
        print(f'Exact characteristic-zero raw/Jacobi/kernel control N={n} passed.',flush=True)
    save('characteristic_zero_matrix_controls.json',controls)
    summary={'status':'passed','python':platform.python_version(),
             'independence':'No author code imported or called. Rational trig expansion; integer divisor-product cyclotomics; characteristic-zero direct Jacobi matrices.',
             'modes':len(d),'pairs':len(d)**2,'support':[lo,hi],'degree':hi-lo,
             'terms':len(p),'content':content,'coefficient_l1':sum(map(abs,p.values())),
             'root_bound':1894,'eligible_orders':len(screens),
             'eligible_orders_divisible_by_7':sum(s['order']%7==0 for s in screens),
             'surviving_orders':survivors,'multiplicities':{'1':2,'7':2},
             'matrix_dimensions':dims,'runtime_seconds':time.time()-started,
             'non_claims':['No higher-power trace result','No spectral simplicity','No quantitative lower bound','No BGS result','No formalization']}
    save('summary.json',summary)
    print(json.dumps(summary,indent=2))

def run(inputs):
    global AUTHOR, OUTPUTS
    AUTHOR = inputs
    OUTPUTS = {}
    main()
    return OUTPUTS

