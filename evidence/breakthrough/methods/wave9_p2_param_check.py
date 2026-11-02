# Verify SNF parametrization for m=16: q=2^A, A=11, t=v2(e8)=3, s=4, Q=128
# Seeds: v1=16*T', T' in Z/128; v0-3*v1=128*S, S in Z/16; v0 = 3*v1+128*S mod 2048
# Sequence via recurrence mod 2048, check period 16 and that count = 2048, and multiset->Y holds.
import collections
def check(m, A, t):
    q=1<<A; s=t+1; Q=1<<(4+t)
    c=[0]*m; e=[0]*m
    c[0]=1; e[0]=0
    if m>1: c[1]=3; e[1]=1
    for i in range(2,m):
        c[i]=(6*c[i-1]-c[i-2])%q
        e[i]=(6*e[i-1]-e[i-2])%q
    seen=set(); bad_period=0
    # group by multiset, check Y orbit
    def d4_orbit(tup):
        orb=set()
        for b in range(4):
            orb.add(tuple(tup[(i+b)%4] for i in range(4)))
            orb.add(tuple(tup[(-i+b)%4] for i in range(4)))
        return orb
    groups={}
    for Tp in range(1<<(A-s)):  # T' in Z/2^{A-s} ? v1=2^s * Tp mod q, Tp in Z/2^{A-s}
        v1=(1<<s)*Tp % q
        for S in range(1<<(A-(4+t))):
            v0=(3*v1 + (1<<(4+t))*S) % q
            d=(v1-3*v0)%q
            seq=tuple((v0*c[i]+d*e[i])%q for i in range(m))
            # period check: next two terms after m should be v0,v1
            # recurrence extension: v_m = v0*c_m + d*e_m ; need v_m==v0, v_{m+1}==v1 mod q
            # compute c_m, e_m mod q via recurrence continuation
            # instead check seq satisfies recurrence cyclically: for i, seq[(i+1)%m] == (6*seq[i]-seq[(i-1)%m])%q
            ok=True
            for i in range(m):
                if seq[(i+1)%m] != (6*seq[i]-seq[(i-1)%m])%q:
                    ok=False; break
            if not ok:
                bad_period+=1
            Y=tuple(sum(seq[i] for i in range(m) if i%4==r)%q for r in range(4))
            ms=tuple(sorted(seq))
            groups.setdefault(ms, set()).add(Y)
            seen.add(seq)
    bad=0
    for ms,Ys in groups.items():
        y0=next(iter(Ys))
        if not Ys.issubset(d4_orbit(y0)):
            bad+=1
    print(f"m={m} q={q} A={A} t={t}: generated {len(seen)} seqs, bad_period={bad_period}, multisets={len(groups)}, bad_Y={bad}")
check(16, 11, 3)
check(12, 7, 1)
