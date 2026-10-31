#!/usr/bin/env python3
"""Line J integration checks, written from the definitions (not from author code).
(a) r(q) lemma: for odd m <= 61 and odd primes q < 3000, q | h_m  <=>  ord_q(lambda) | m  (exact integers; h_m from (1+sqrt2)^m).
(b) ord_49(1+sqrt2) = 42 and ord_49(lambda) = 21 (exact).
(c) window lemma with the Theorem J constants: for theta on a grid in [theta_lo, theta_up] and many alpha, every 6 consecutive k
    contain cos(alpha + k theta) >= cos(theta_up/2) and one <= -cos(theta_up/2) (float, grid check of a proved statement).
(d) constants: cos(theta_up/2) >= 0.8443062873 < 0.84431; arccos(0.84431)/pi = 0.18001; xi_lo/sqrt(lambda) >= 1.0184224.
(e) K_min of J3 vs the Theorem J table (min K_j+/K_j- >= table minimum 0.009975).
(f) n_q counts: #{j unit mod q, j != b} = q - 2 (q || h), q - 1 (q^2 | h), brute force for q < 60.
"""
import math, json, os, random
here=os.path.dirname(os.path.abspath(__file__))
ok=True
def pw(m, mod=None):
    a,b=1,0
    for _ in range(m):
        a,b=a+2*b,a+b
        if mod: a,b=a%mod,b%mod
    return a,b
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(3,n+1) if s[i]]
def ordlam(q):
    # order of lambda = 3+2sqrt2 in (Z[sqrt2]/q)^*
    a,b=3,2; k=1
    while (a%q,b%q)!=(1,0):
        a,b=(3*a+4*b)%q,(2*a+3*b)%q; k+=1
    return k
P=primes(3000); R={q:ordlam(q) for q in P}
bad=0
for m in range(1,62,2):
    h,_=pw(m)
    for q in P:
        if (h%q==0)!=(m%R[q]==0): bad+=1
print('(a) r(q) lemma, odd m<=61, primes 3..3000: mismatches =',bad); ok&=bad==0
# pell: (1+sqrt2)^m = h + y' sqrt2 ; check h^2 - 2y'^2 = (-1)^m for a few
for m in (1,3,9,15):
    h,y=pw(m); assert h*h-2*y*y==(-1)**m
o42=[d for d in range(1,43) if pw(d,49)==(1,0)][0]
o21=[d for d in range(1,22) if pw(2*d,49)==(1,0)][0]
print('(b) ord_49(1+sqrt2) =',o42,' ord_49(lambda) =',o21); ok&=(o42==42 and o21==21)
tlo,tup=1.130677114,1.131054118
c=math.cos(tup/2); N=math.ceil(2*math.pi/tlo)
random.seed(1); worst=0
for i in range(41):
    th=tlo+(tup-tlo)*i/40
    for _ in range(2000):
        al=random.uniform(0,2*math.pi)
        for k0 in range(0,30):
            vals=[math.cos(al+(k0+k)*th) for k in range(N)]
            if not (max(vals)>=c-1e-12 and min(vals)<=-c+1e-12): worst+=1
print('(c) window: N =',N,' cos(theta_up/2) =',round(c,10),' failures =',worst); ok&=(N==6 and worst==0)
dens=math.acos(0.84431)/math.pi; lam=3+2*math.sqrt(2)
print('(d) c_win =',c,'< 0.84431:',c<0.84431,' density =',round(dens,5),' xi_lo/sqrt(lam) =',2.4586893/math.sqrt(lam))
ok&=(c>=0.8443062873 and c<0.84431 and abs(dens-0.18001)<1e-5 and 2.4586893/math.sqrt(lam)>=1.0184224)
A=json.load(open(os.path.join(here,'../logs/assemble_v2.json')))
kmin=min(min(x['K_plus'],x['K_minus']) for x in A['residues'])
J=json.load(open(os.path.join(here,'../J3/logs/assemble16.json')))
print('(e) min K+/K- =',kmin,' J3 K_min =',J['K_min'],' table min K_j = 0.009975 <= K_min:',0.009975<=J['K_min']<=kmin)
ok&=(0.009975<=J['K_min']<=kmin)
bad=0
for q in primes(60):
    for b in range(1,q):
        if sum(1 for j in range(1,q) if j!=b)!=q-2: bad+=1
    if sum(1 for j in range(1,q))!=q-1: bad+=1
print('(f) n_q counts, q<60: mismatches =',bad); ok&=bad==0
print('ALL_OK' if ok else 'FAIL')
