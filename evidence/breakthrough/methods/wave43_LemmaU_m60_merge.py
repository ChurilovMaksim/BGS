from collections import defaultdict

def cycles(p):
    out = {}
    for a in range(p):
        for b in range(p):
            s0 = (2*a) % p; s1 = (2*(17*a+24*b)) % p
            s = [s0, s1]
            for k in range(2, 30): s.append((34*s[-1] - s[-2]) % p)
            out[(a,b)] = tuple(s)
    return out
def mulR(x,y,p): return ((x[0]*y[0]+2*x[1]*y[1])%p, (x[0]*y[1]+x[1]*y[0])%p)
ALPHA=(3,2)
def conj(x,p): return (x[0], (-x[1])%p)
def neg(x,p): return ((-x[0])%p, (-x[1])%p)

def dihedral_orbit(A,B,pa,pb):
    seen=set(); stack=[(A,B)]
    while stack:
        a,b=stack.pop()
        if (a,b) in seen: continue
        seen.add((a,b))
        stack.append((mulR(ALPHA,a,pa), mulR(ALPHA,b,pb)))
        stack.append((conj(a,pa), conj(b,pb)))
    return seen

for (pa,pb) in [(9,19),(9,59)]:
    ca, cb = cycles(pa), cycles(pb)
    groups = defaultdict(list)
    for A, ta in ca.items():
        for B, tb in cb.items():
            b0 = tuple(sorted((ta[k]*pb+tb[k]) for k in range(30)))
            b1 = tuple(sorted(((-ta[k] % pa)*pb + (-tb[k] % pb)) for k in range(30)))
            P = tuple(sorted(b0 + b1))
            groups[P].append((A,B))
    ker = [(0,0),(0,3),(0,6)]
    from collections import Counter
    rel = Counter(); ex = {}
    for P, pts in groups.items():
        if len(pts) <= 120: continue
        S = set(pts)
        # kernel-quotient reps
        reps = set((((A[0], A[1]%3), B)) for (A,B) in pts)
        # dihedral orbits on quotient: lift rep to full A (b mod 9 = rep b + 0) then orbit, quotient
        orbits=[]; rem=set(reps)
        while rem:
            r = next(iter(rem))
            A0 = (r[0][0], r[0][1])  # b in 0..2, lift with +0
            orb = dihedral_orbit(A0, r[1], pa, pb)
            q = set((((a[0], a[1]%3), b)) for (a,b) in orb)
            orbits.append(q); rem -= q
        if len(orbits) < 2: continue
        # take reps o1, o2; test relations between some member of o1 and some member of o2
        o1, o2 = orbits[0], orbits[1]
        # for each candidate move, check if it maps o1 into o2 (as sets, up to kernel on a-side)
        def qmap(pts, fn):
            return set((((fn(a)[0], fn(a)[1]%3), fn(b)) for (a,b) in pts)) if False else None
        # moves act on full params; work with lifts: choose lift of o1 members with b in 0..2, apply move, quotient
        def apply_move(o, move):
            out=set()
            for (aq,bq) in o:
                A=(aq[0], aq[1]); B=bq
                A2,B2 = move(A,B)
                out.add(((A2[0], A2[1]%3), B2))
            return out
        moves = {
            'J_a (conj a only)': lambda A,B: (conj(A,pa), B),
            'J_b (conj b only)': lambda A,B: (A, conj(B,pb)),
            'neg_a only': lambda A,B: (neg(A,pa), B),
            'neg_b only': lambda A,B: (A, neg(B,pb)),
            'alpha_a only': lambda A,B: (mulR(ALPHA,A,pa), B),
            'alpha_b only': lambda A,B: (A, mulR(ALPHA,B,pb)),
        }
        found=[]
        for name, mv in moves.items():
            if apply_move(o1, mv) == o2: found.append(name)
        key = tuple(found) if found else ('NONE',)
        rel[key]+=1; ex.setdefault(key, (sorted(o1)[:2], sorted(o2)[:2]))
    print(f"pair ({pa},{pb}) merged-group relations:")
    for k,v in rel.items(): print("   ",k,"->",v," e.g.", ex[k])
