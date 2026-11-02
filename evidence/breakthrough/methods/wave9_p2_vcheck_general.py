# General v2 check: Q=2^{3+v2}, block size N=2^{v2}, c_s,e_s mod Q via recurrence, B_s = T c_s + D e_s mod Q
# S_r = sum_{s=r mod4} B_s mod Q; group by multiset of B, check S tuples in one D4 orbit.
import sys
def d4_orbit(tup):
    orb=set()
    for b in range(4):
        orb.add(tuple(tup[(i+b)%4] for i in range(4)))
        orb.add(tuple(tup[(-i+b)%4] for i in range(4)))
    return orb
def check(v2):
    Q=1<<(3+v2); N=1<<v2
    # c,e mod Q via recurrence
    c=[0]*N; e=[0]*N
    c[0]=1; e[0]=0
    if N>1:
        c[1]=3; e[1]=1
    for i in range(2,N):
        c[i]=(6*c[i-1]-c[i-2])%Q
        e[i]=(6*e[i-1]-e[i-2])%Q
    groups={}
    for T in range(Q):
        for D in range(0,Q,8):
            block=tuple((T*c[s]+D*e[s])%Q for s in range(N))
            S=tuple(sum(block[s] for s in range(N) if s%4==r)%Q for r in range(4))
            ms=tuple(sorted(block))
            groups.setdefault(ms, set()).add(S)
    bad=0
    for ms,Ss in groups.items():
        s0=next(iter(Ss))
        if not Ss.issubset(d4_orbit(s0)):
            bad+=1
    print(f"v2={v2} Q={Q} N={N} params={Q*(Q//8)} multisets={len(groups)} bad={bad}", flush=True)
    return bad
for v2 in [4,5,6]:
    check(v2)
