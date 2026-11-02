# Explore Fix-block class multisets: x-residues, M-equality, pair-union vs pair-profile.
from collections import Counter
def blocks(L):
    Q = 2**(L+3); P = 2**L
    c=[1,3]; e=[0,1]
    for _ in range(P):
        c.append((6*c[-1]-c[-2])%Q); e.append((6*e[-1]-e[-2])%Q)
    out=[]
    for T in range(Q):
        for D in range(0,Q,8):
            B=tuple((T*c[s]+D*e[s])%Q for s in range(P))
            out.append((T,D,B))
    return out,Q,P
def classes(B,P):
    return tuple(tuple(sorted(B[j] for j in range(P) if j%4==r)) for r in range(4))
for L in [2,3,4,5]:
    bl,Q,P = blocks(L)
    print(f"=== L={L} Q={Q} P={P} nblocks={len(bl)}")
    # x tuple = B[0..3] mod 32
    # pair-union -> profile test
    bad_pair=0; tot_pair=0; examples=[]
    # For each block, check all pair unions: if M_r+M_s == M_r'+M_s' (as multisets) then profile equal?
    for (T,D,B) in bl:
        M=classes(B,P)
        pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
        unions={}
        for pr in pairs:
            u=tuple(sorted(M[pr[0]]+M[pr[1]]))
            unions.setdefault(u,[]).append(pr)
        for u,prs in unions.items():
            for i in range(len(prs)):
                for j in range(i+1,len(prs)):
                    tot_pair+=1
                    prof1=tuple(sorted([M[prs[i][0]],M[prs[i][1]]]))
                    prof2=tuple(sorted([M[prs[j][0]],M[prs[j][1]]]))
                    if prof1!=prof2:
                        bad_pair+=1
                        if len(examples)<5: examples.append((T,D,prs[i],prs[j]))
    print(f"  pair-union collisions: {tot_pair}, profile-mismatch: {bad_pair}, ex={examples}")
    # M-equality partition vs x-equality partition
    from collections import Counter as C
    cntM=C(); cntX=C()
    for (T,D,B) in bl:
        M=classes(B,P)
        x=tuple(B[r]%32 for r in range(4))
        # partition signature: tuple of group ids
        def sig(t):
            m={}; out=[]
            for v in t:
                if v not in m: m[v]=len(m)
                out.append(m[v])
            return tuple(out)
        cntM[sig(M)]+=1; cntX[sig(x)]+=1
    print(f"  M-eq partitions: {dict(cntM)}")
    print(f"  x-eq partitions: {dict(cntX)}")
