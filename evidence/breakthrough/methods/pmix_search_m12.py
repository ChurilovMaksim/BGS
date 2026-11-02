import itertools
from collections import defaultdict

m=12
t=4
# Dihedral perms on Z/4 as index perms pi: new[i] = v[pi(i)]
perms=[]
for b in range(4):
    for sgn in (1,-1):
        pi=tuple((sgn*i+b)%4 for i in range(4))
        if pi not in perms: perms.append(pi)
print("perms (index maps):", perms)
def apply(v, pi):
    return tuple(v[pi[i]] for i in range(len(v)))
def Yvec(y):
    Y=[0]*t
    for i,v in enumerate(y):
        Y[i%t]+=v
    return tuple(Y)
def pi_set(Y, Yp):
    return frozenset(idx for idx,pi in enumerate(perms) if apply(Y,pi)==Yp)

def fix_mod_q(q):
    # recurrence y_{i+1}=6 y_i - y_{i-1} mod q, y_{i+m}=y_i, determined by (y0,y1) with (M^m-I)(y0,y1)=0
    # brute force (y0,y1) in q^2, generate sequence, check periodicity
    res=[]
    for y0 in range(q):
        for y1 in range(q):
            seq=[y0,y1]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==y0 and seq[m+1]==y1:
                res.append(tuple(seq[:m]))
    return res

def component_pairs(q):
    vecs=fix_mod_q(q)
    print(f"q={q} |Fix|={len(vecs)} (expect {q})")
    groups=defaultdict(list)
    for v in vecs:
        groups[tuple(sorted(v))].append(v)
    pairs=[]
    for key, vs in groups.items():
        for a in range(len(vs)):
            for b in range(len(vs)):
                if a==b: continue
                z, zp = vs[a], vs[b]
                Y, Yp = Yvec(z), Yvec(zp)
                # Y mod q? Yvec sums are integers mod q? For component Lemma Y, Y mod q: reduce sums mod q
                Yq=tuple(x%q for x in Y); Ypq=tuple(x%q for x in Yp)
                pis=pi_set(Yq, Ypq)
                if pis:
                    pairs.append((z, zp, Yq, Ypq, pis))
                else:
                    print(f"  !! component Lemma Y FAILS mod {q}: {z} -> {zp} Y={Yq} Yp={Ypq}")
    print(f"  pairs (ordered, same multiset, pi nonempty): {len(pairs)}")
    # distribution of pi sets
    from collections import Counter
    print("  pi-set size distribution:", Counter(len(p[4]) for p in pairs))
    return pairs

pairs2=component_pairs(128)
pairs3=component_pairs(81)

# bipartite matching for common sigma: sigma(i)=j such that z2_j == z2p_i and z3_j == z3p_i
# left nodes i=0..11, right nodes j=0..11, edge if both hold
def has_common_sigma(z2, z2p, z3, z3p):
    adj=[]
    for i in range(m):
        allowed=[j for j in range(m) if z2[j]==z2p[i] and z3[j]==z3p[i]]
        adj.append(allowed)
    # Kuhn
    match_r=[-1]*m
    def try_k(u, seen):
        for v in adj[u]:
            if seen[v]: continue
            seen[v]=True
            if match_r[v]==-1 or try_k(match_r[v], seen):
                match_r[v]=u
                return True
        return False
    for u in range(m):
        seen=[False]*m
        if not try_k(u, seen):
            return False
    return True

def find_sigma(z2, z2p, z3, z3p):
    adj=[]
    for i in range(m):
        allowed=[j for j in range(m) if z2[j]==z2p[i] and z3[j]==z3p[i]]
        adj.append(allowed)
    match_r=[-1]*m
    def try_k(u, seen):
        for v in adj[u]:
            if seen[v]: continue
            seen[v]=True
            if match_r[v]==-1 or try_k(match_r[v], seen):
                match_r[v]=u
                return True
        return False
    for u in range(m):
        seen=[False]*m
        if not try_k(u, seen):
            return None
    sigma=[0]*m
    for j,u in enumerate(match_r):
        sigma[u]=j
    return tuple(sigma)

print("\nSearching for incompatible pi pairs with common sigma...")
found=[]
checked=0
for (z2,z2p,Y2,Y2p,pis2) in pairs2:
    for (z3,z3p,Y3,Y3p,pis3) in pairs3:
        if pis2 & pis3:
            continue
        checked+=1
        if has_common_sigma(z2,z2p,z3,z3p):
            sigma=find_sigma(z2,z2p,z3,z3p)
            print("FOUND MIXING CANDIDATE:")
            print(" z2 ", z2, " -> ", z2p, " Y2 ", Y2, " -> ", Y2p, " pis2 ", sorted(pis2))
            print(" z3 ", z3, " -> ", z3p, " Y3 ", Y3, " -> ", Y3p, " pis3 ", sorted(pis3))
            print(" sigma ", sigma)
            found.append((z2,z2p,z3,z3p,sigma))
            if len(found)>=5:
                break
    if len(found)>=5:
        break
print(f"\nincompatible pairs checked: {checked}, found: {len(found)}")
