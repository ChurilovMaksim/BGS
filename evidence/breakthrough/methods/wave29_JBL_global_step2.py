import math
from collections import defaultdict
ALPHA=(3,2)
def mul(a,b,M): return ((a[0]*b[0]+2*a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0])%M)
def pw(a,n,M):
    r=(1,0)
    for _ in range(n): r=mul(r,a,M)
    return r
def tr(a,M): return (2*a[0])%M
def genuine(M,m):
    d=pw(ALPHA,m,M); d=((d[0]-1)%M,d[1])
    return [(x,y) for x in range(M) for y in range(M) if mul(d,(x,y),M)==(0,0)]
def seqs_of(G,M,m):
    out={}
    for A in G:
        b=A; s=[]
        for i in range(m):
            s.append(tr(b,M)); b=mul(b,ALPHA,M)
        out[A]=tuple(s)
    return out

# --- per-component-only insufficiency at m=12 (128,81) ---
m=12; t=4; S=3
G2,Gq=genuine(128,m),genuine(81,m)
S2=seqs_of(G2,128,m); Sq=seqs_of(Gq,81,m)
perms=[tuple((eps*r+b)%t for r in range(t)) for eps in (1,-1) for b in range(t)]
def sig_of(s2,sq):
    z=list(zip(s2,sq)); sig=[]
    for r in range(t):
        sig.append(tuple(sorted(z[r+t*s] for s in range(S))))
    return tuple(sig)
# group by per-component multisets only
pcgroups=defaultdict(list)
for a2 in G2:
    for aq in Gq:
        pcgroups[(tuple(sorted(S2[a2])),tuple(sorted(Sq[aq])))].append((a2,aq))
print(f"m=12 per-component groups={len(pcgroups)}",flush=True)
# find a per-component group containing two joint-global groups with incompatible signatures
found=None
for key,members in pcgroups.items():
    # split by joint global multiset
    joint=defaultdict(list)
    for A in members:
        joint[tuple(sorted(zip(S2[A[0]],Sq[A[1]])))].append(A)
    if len(joint)<2: continue
    reps=[v[0] for v in joint.values()]
    # check pairwise signature compatibility between reps
    sigs=[sig_of(S2[A[0]],Sq[A[1]]) for A in reps]
    bad=False
    for i in range(len(reps)):
        for j in range(i+1,len(reps)):
            if not any(all(sigs[j][r]==sigs[i][p[r]] for r in range(t)) for p in perms):
                bad=True; found=(key,reps[i],reps[j],sigs[i],sigs[j]); break
        if bad: break
    if bad: break
print("per-component insufficiency found:", found is not None,flush=True)
if found:
    print("  rep1",found[1],"rep2",found[2],flush=True)
    print("  sig1",found[3],flush=True)
    print("  sig2",found[4],flush=True)

# --- m=36 (128,243) joint global -> JBL ---
m=36; t=4; S=9
G2,Gq=genuine(128,m),genuine(243,m)
print(f"m=36 |G128|={len(G2)} |G243|={len(Gq)}",flush=True)
S2=seqs_of(G2,128,m); Sq=seqs_of(Gq,243,m)
groups=defaultdict(list)
for a2 in G2:
    s2=S2[a2]
    for aq in Gq:
        z=tuple(zip(s2,Sq[aq]))
        groups[tuple(sorted(z))].append((a2,aq,z))
print(f"m=36 global-groups={len(groups)} multi={sum(1 for v in groups.values() if len(v)>1)} maxsize={max(len(v) for v in groups.values())}",flush=True)
def sig_of_z(z):
    return tuple(tuple(sorted(z[r+t*s] for s in range(S))) for r in range(t))
bad=0; checked=0
for g in groups.values():
    if len(g)<2: continue
    s0=sig_of_z(g[0][2])
    for A in g[1:]:
        checked+=1
        sA=sig_of_z(A[2])
        if not any(all(sA[r]==s0[p[r]] for r in range(t)) for p in perms):
            bad+=1
            if bad<=3: print("  JBL bad:",g[0][:2],A[:2],flush=True)
print(f"m=36 JBL-bad pairs={bad} checked={checked}",flush=True)
