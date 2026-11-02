import math
from collections import defaultdict

ALPHA=(3,2)
def mul(a,b,M): return ((a[0]*b[0]+2*a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0])%M)
def conj(a,M): return (a[0]%M,(-a[1])%M)
def pw(a,n,M):
    r=(1,0)
    for _ in range(n): r=mul(r,a,M)
    return r
def tr(a,M): return (2*a[0])%M
def genuine(M,m):
    d=pw(ALPHA,m,M); d=((d[0]-1)%M,d[1])
    return [(x,y) for x in range(M) for y in range(M) if mul(d,(x,y),M)==(0,0)]
def ann_m(M,m):
    pows=[pw(ALPHA,n,M) for n in range(m)]
    return {(x,y) for x in range(M) for y in range(M) if all(tr(mul((x,y),p,M),M)==0 for p in pows)}
def order(a,M):
    cur=(1,0)
    for j in range(1,1000000):
        cur=mul(cur,a,M)
        if cur==(1,0): return j
    raise RuntimeError

def run(m,q2,q,shadow_q):
    t=math.gcd(m,4); S=m//t
    G2,Gq=genuine(q2,m),genuine(q,m)
    A2,Aq=ann_m(q2,m),ann_m(q,m)
    # sequences: for each A, tuple over i of (tr mod q2, tr mod q)
    def seq(a2,aq):
        out=[]
        cur2,curq=(1,0),(1,0)  # alpha^i
        # we need A*alpha^i: iterate
        b2,bq=a2,aq
        for i in range(m):
            out.append((tr(b2,q2),tr(bq,q)))
            b2=mul(b2,ALPHA,q2); bq=mul(bq,ALPHA,q)
        return tuple(out)
    groups=defaultdict(list)
    seqs={}
    for a2 in G2:
        for aq in Gq:
            s=seq(a2,aq); seqs[(a2,aq)]=s
            groups[tuple(sorted(s))].append((a2,aq))
    # D_t perms: r -> eps*r+b mod t
    perms=[]
    for eps in (1,-1):
        for b in range(t): perms.append(tuple((eps*r+b)%t for r in range(t)))
    def signature(A):
        a2,aq=A
        sig=[]
        for r in range(t):
            pairs=[]
            # positions i=r+t*s
            sseq=seqs[A]
            for s in range(S):
                pairs.append(sseq[r+t*s])
            sig.append(tuple(sorted(pairs)))
        return tuple(sig)
    sigs={A:signature(A) for A in groups and []}  # placeholder
    # compute sigs lazily per group
    n_groups=len(groups); multi=[g for g in groups.values() if len(g)>1]
    print(f"m={m} params={len(G2)*len(Gq)} global-groups={n_groups} multi-groups={len(multi)} maxsize={max(len(g) for g in groups.values())}",flush=True)
    jbl_bad=[]; param_bad=[]; jbl_ok_param_bad=[]
    # parameter relation check: exists j,c with diff in Ann x (Ann+Shadow)
    # brute j over joint period L, c in {id,conj}
    o2,oq=order(ALPHA,q2),order(ALPHA,q); L=o2*oq//math.gcd(o2,oq)
    pow2=[(1,0)]
    for _ in range(L): pow2.append(mul(pow2[-1],ALPHA,q2))
    powq=[(1,0)]
    for _ in range(L): powq.append(mul(powq[-1],ALPHA,q))
    shadow_set=set(shadow_q)
    def param_related(A0,A):
        for c in (0,1):
            b2_0=conj(A0[0],q2) if c else A0[0]
            bq_0=conj(A0[1],q) if c else A0[1]
            for j in range(L):
                d2=((A[0][0]-mul(b2_0,pow2[j],q2)[0])%q2,(A[0][1]-mul(b2_0,pow2[j],q2)[1])%q2)
                if d2 not in A2: continue
                dq_raw=((A[1][0]-mul(bq_0,powq[j],q)[0])%q,(A[1][1]-mul(bq_0,powq[j],q)[1])%q)
                # dq must be in Ann_q + Shadow: Ann_q={0} in these cases, so dq in shadow
                if dq_raw in shadow_set: return True
                # general: dq - w in Aq for some w
                for w in shadow_set:
                    if ((dq_raw[0]-w[0])%q,(dq_raw[1]-w[1])%q) in Aq: return True
        return False
    for g in multi:
        A0=g[0]; s0=signature(A0)
        for A in g[1:]:
            sA=signature(A)
            ok_jbl=any(tuple(sA[r] for r in range(t))==tuple(s0[p[r]] for r in range(t)) for p in perms) if False else False
            # careful: signature'(r) should equal signature(pi(r)); pi as tuple mapping r->pi(r)
            ok_jbl=any(all(sA[r]==s0[p[r]] for r in range(t)) for p in perms)
            pr=param_related(A0,A)
            if not ok_jbl: jbl_bad.append((A0,A))
            if not pr: param_bad.append((A0,A))
            if ok_jbl and not pr: jbl_ok_param_bad.append((A0,A))
    print(f"  JBL-bad pairs={len(jbl_bad)} PARAM-bad pairs={len(param_bad)} JBL-ok-but-PARAM-bad={len(jbl_ok_param_bad)}",flush=True)
    for A0,A in jbl_bad[:3]: print("  JBL bad:",A0,A,flush=True)
    for A0,A in jbl_ok_param_bad[:3]: print("  JBL-ok PARAM-bad:",A0,A,flush=True)
    return jbl_bad,param_bad

shadow12={(27*a%81,27*b%81) for a in range(3) for b in range(3)}
run(12,128,81,shadow12)
shadow8={(3*a%9,3*b%9) for a in range(3) for b in range(3)}
run(8,512,9,shadow8)
