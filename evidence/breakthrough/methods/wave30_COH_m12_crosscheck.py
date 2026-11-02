"""Independent brute-force cross-check for wave30_COH_m12.cpp.

Samples genuine A mod D_12 (random + structured: big-class A_81,
zero components) and, per A, enumerates ALL valid sigma by
backtracking (sigma(0), sigma(1) + joint recurrence + per-component
genuine-sequence membership), then checks the Shadow-aware COH
criterion directly: exists dihedral tau with sigma(S_q) == tau(S_q)
for q != 81 and sigma(S_81) - tau(S_81) in ShiftSet. Any sigma
failing that is a COH counterexample. This does NOT use patterns,
classes-vs-dihedral, or the phase decomposition: it is a direct
per-A check, so agreement with the C++ result corroborates it.
"""
import random
from collections import defaultdict

def mul(a,b,q): return ((a[0]*b[0]+2*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def pw(a,n,q):
    r=(1,0)
    for _ in range(n): r=mul(r,a,q)
    return r
def tr(a,q): return (2*a[0])%q
ALPHA=(3,2); M=12; QS=[128,81,25,49,121]; D=1536796800
DIH=[]
for k in range(12):
    DIH.append(tuple((i+k)%12 for i in range(12))); DIH.append(tuple((-i+k)%12 for i in range(12)))
DIH=sorted(set(DIH))

def seq_of(A,q):
    out=[]; b=A
    for _ in range(M):
        out.append(tr(b,q)); b=mul(b,ALPHA,q)
    return tuple(out)

comp={}
for q in QS:
    d=pw(ALPHA,M,q); d=((d[0]-1)%q,d[1])
    G=[(x,y) for x in range(q) for y in range(q) if mul(d,(x,y),q)==(0,0)]
    seqdict=defaultdict(list); seqs={}
    for A in G:
        s=seq_of(A,q); seqs[A]=s; seqdict[s].append(A)
    comp[q]=(G,seqs,seqdict)
shifts=set()
for a in range(3):
    for b in range(3):
        shifts.add(seq_of((27*a%81,27*b%81),81))

def crt(pairs):
    x=0; Mc=1
    for (r,q) in pairs:
        inv=pow(Mc%q,-1,q)
        t=((r-x)%q)*inv%q
        x+=Mc*t; Mc*=q
    return x%D

def check_A(Aq):
    # Aq: dict q -> A_q ; returns list of failing sigmas
    Ss={q:comp[q][1][Aq[q]] for q in QS}
    # joint tuples
    T=[tuple(Ss[q][i] for q in QS) for i in range(12)]
    tindex={}
    for j,t in enumerate(T): tindex.setdefault(t,[]).append(j)
    fails=[]
    used=[False]*12; sig=[None]*12
    P={q:[None]*12 for q in QS}
    def rec(i):
        if i==12:
            for q in QS:
                Pq=tuple(P[q])
                if (6*Pq[11]-Pq[10])%q!=Pq[0]: return
                if (6*Pq[0]-Pq[11])%q!=Pq[1]: return
                if Pq not in comp[q][2]: return
            sigma=tuple(sig)
            # COH check
            for tau in DIH:
                ok=True
                for q in QS:
                    sq=tuple(Ss[q][sigma[j]] for j in range(12))
                    tq=tuple(Ss[q][tau[j]] for j in range(12))
                    if q==81:
                        diff=tuple((sq[j]-tq[j])%81 for j in range(12))
                        if diff not in shifts: ok=False; break
                    else:
                        if sq!=tq: ok=False; break
                if ok: return
            fails.append(sigma)
            return
        if i<2:
            for j in range(12):
                if not used[j]:
                    used[j]=True; sig[i]=j
                    for q in QS: P[q][i]=Ss[q][j]
                    rec(i+1); used[j]=False
            return
        need=tuple((6*P[q][i-1]-P[q][i-2])%q for q in QS)
        for j in tindex.get(need,[]):
            if not used[j]:
                used[j]=True; sig[i]=j
                for q in QS: P[q][i]=Ss[q][j]
                rec(i+1); used[j]=False
    rec(0)
    return fails

random.seed(12345)
G81=comp[81][0]
# big-class A81: those whose sequence class has 36 distinct seqs
seqs81=comp[81][1]
classes=defaultdict(set)
for A in G81: classes[tuple(sorted(seqs81[A]))].add(seqs81[A])
bigseqs=[v for v in classes.values() if len(v)==36][0]
bigA=[A for A in G81 if seqs81[A] in bigseqs]
print(f"big-class A81 count={len(bigA)}")
n_test=0; n_fail=0
def run_case(Aq,label):
    global n_test,n_fail
    n_test+=1
    f=check_A(Aq)
    if f:
        n_fail+=1
        print(f"FAIL {label}: Aq={Aq} sigmas={f[:3]}")
for trial in range(1200):
    Aq={q:random.choice(comp[q][0]) for q in QS}
    run_case(Aq,f"random{trial}")
for trial in range(600):
    Aq={q:random.choice(comp[q][0]) for q in QS}
    Aq[81]=random.choice(bigA)
    run_case(Aq,f"big81-{trial}")
for trial in range(300):
    Aq={q:random.choice(comp[q][0]) for q in QS}
    # zero out 1-2 random components
    for q in random.sample(QS,random.choice([1,2])):
        Aq[q]=(0,0)
    Aq[81]=random.choice(bigA)
    run_case(Aq,f"big81-zero-{trial}")
print(f"tested={n_test} failing_As={n_fail}")
