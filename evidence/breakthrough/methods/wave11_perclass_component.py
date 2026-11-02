"""Wave 11, task 2, search A: exact per-class multisets mod q, single component.

For each (m, q) with q = p^e || D_m (q <= 400000, plus (64,32768)):
 enumerate ALL Fix_m mod q sequences (length m, recurrence y_{n+1}=6 y_n - y_{n-1}
 mod q, period m) by solving (M^m - I)(x0,x1) = 0 mod q for x0, then x1 via
 two congruences + CRT combination. Self-check: number of solutions == q
 and every generated sequence satisfies the period condition (checked in
 numpy for the full array, not just samples).
 Group by sorted full multiset; within each group check that the D_t-canonical
 form of the per-class tuple is constant. A non-constant group is a component
 counterexample: its CRT lift (other components zero) is a global exact
 per-class counterexample (reduction mod q preserves D_t-relation).
 t = gcd(m,4); classes O_r = {i : i % t == r}; D_t perms: r -> r+b, r -> -r+b.
"""
import math, sys, time
import numpy as np
from collections import defaultdict

def mat_pow(M, n):
    # 2x2 integer matrix power, M as tuple (a,b,c,d)
    a,b,c,d = 1,0,0,1
    x1,x2,x3,x4 = M
    while n:
        if n & 1:
            a,b,c,d = a*x1+b*x3, a*x2+b*x4, c*x1+d*x3, c*x2+d*x4
        x1,x2,x3,x4 = x1*x1+x2*x3, x1*x2+x2*x4, x3*x1+x4*x3, x3*x2+x4*x4
        n >>= 1
    return (a,b,c,d)

def solve_cong(a, rhs, q):
    """Solutions of a*x == rhs (mod q) as (residue, step) with x == residue mod step,
    step dividing q; None if unsolvable. Trivial congruence -> (0,1)."""
    a %= q; rhs %= q
    if a == 0:
        return (0,1) if rhs == 0 else None
    g = math.gcd(a, q)
    if rhs % g:
        return None
    m1 = q // g
    inv = pow(a//g, -1, m1)
    return ((rhs//g * inv) % m1, m1)

def combine_cong(c1, c2, q):
    """Combine x == a1 (mod m1), x == a2 (mod m2) into (residue, lcm) mod q,
    or None. Solutions mod q: residue + k*lcm."""
    a1,m1 = c1; a2,m2 = c2
    g = math.gcd(m1,m2)
    if (a2-a1) % g:
        return None
    l = m1//g*m2
    # solve m1*t == a2-a1 (mod m2): t = ((a2-a1)//g * inv(m1//g mod m2//g)) mod m2//g
    inv = pow(m1//g, -1, m2//g)
    t = ((a2-a1)//g * inv) % (m2//g)
    return ((a1 + m1*t) % l, l)

def fix_mod_q(m, q):
    A11,A12,A21,A22 = mat_pow((6,-1,1,0), m)
    A11-=1; A22-=1  # M^m - I
    X0=[]; X1=[]
    for x0 in range(q):
        c1 = solve_cong(A12, -A11*x0, q)
        if c1 is None: continue
        c2 = solve_cong(A22, -A21*x0, q)
        if c2 is None: continue
        comb = combine_cong(c1, c2, q)
        if comb is None: continue
        res, step = comb
        k = 0
        while res + k*step < q:
            X0.append(x0); X1.append(res + k*step); k += 1
    X0=np.array(X0, dtype=np.int64); X1=np.array(X1, dtype=np.int64)
    assert len(X0)==q, f"m={m} q={q}: solutions {len(X0)} != q"
    # generate sequences, chunked
    seqs = np.empty((q, m), dtype=np.int64)
    CH=50000
    for s in range(0, q, CH):
        e=min(q, s+CH)
        chunk=np.empty((e-s, m), dtype=np.int64)
        chunk[:,0]=X0[s:e]
        if m>1: chunk[:,1]=X1[s:e]
        for i in range(2, m):
            chunk[:,i]=(6*chunk[:,i-1]-chunk[:,i-2])%q
        # period self-check on this chunk: next two terms must return to (x0,x1)
        nxt=(6*chunk[:,m-1]-chunk[:,m-2])%q
        nxt2=(6*nxt-chunk[:,m-1])%q
        assert np.array_equal(nxt, chunk[:,0]) and np.array_equal(nxt2, chunk[:,1]), \
            f"period check failed m={m} q={q} chunk {s}"
        seqs[s:e]=chunk
    return seqs

def d_t_perms(t):
    out=[]
    for b in range(t):
        out.append(tuple((i+b)%t for i in range(t)))
        out.append(tuple((-i+b)%t for i in range(t)))
    return list(dict.fromkeys(out))

def check(m, q):
    t0=time.time()
    seqs=fix_mod_q(m,q)
    t=math.gcd(m,4)
    perms=d_t_perms(t)
    # class index lists
    cls_idx=[[i for i in range(m) if i%t==r] for r in range(t)]
    groups={}  # sorted-key bytes -> [canon bytes, example seq, set of canons]
    bad=[]
    CH=50000
    for s in range(0, len(seqs), CH):
        chunk=seqs[s:s+CH]
        srt=np.sort(chunk, axis=1).astype(np.int32)
        # per-class sorted arrays: shape (n, t, m//t)
        pc=np.empty((len(chunk), t, m//t), dtype=np.int32)
        for r,idx in enumerate(cls_idx):
            pc[:,r,:]=np.sort(chunk[:,idx], axis=1)
        # canon: lex-min over perms of flattened permuted pc
        best=None
        for pi in perms:
            cand=pc[:, list(pi), :].reshape(len(chunk), m)
            if best is None:
                best=cand.copy(); continue
            # lex compare cand < best row-wise
            lt=np.zeros(len(chunk), dtype=bool); eq=np.ones(len(chunk), dtype=bool)
            for c in range(m):
                lt |= eq & (cand[:,c] < best[:,c])
                eq &= (cand[:,c] == best[:,c])
            best[lt]=cand[lt]
        for j in range(len(chunk)):
            key=srt[j].tobytes(); can=best[j].tobytes()
            ent=groups.get(key)
            if ent is None:
                groups[key]=(can, chunk[j].copy(), {can})
            else:
                if can not in ent[2]:
                    ent[2].add(can)
                    if len(ent[2])==2:
                        bad.append((key, ent[1], chunk[j].copy(), ent[0], can))
    print(f"m={m} q={q} t={t} n={len(seqs)} groups={len(groups)} BAD_GROUPS={len(bad)} time={time.time()-t0:.1f}s", flush=True)
    for key, ex1, ex2, can1, can2 in bad[:3]:
        print(f"  BAD example seq1={tuple(ex1)} seq2={tuple(ex2)}", flush=True)
    return len(bad)

def main():
    import sympy as sp
    cases=[]
    # m list with all prime powers q<=400000
    for m in [4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,28,36]:
        x,y=1,0
        for _ in range(m):
            x,y=3*x+8*y, x+3*y
        D=2*(x-1)
        for p,e in sp.factorint(D).items():
            q=p**e
            if q<=400000:
                cases.append((m,q))
    cases.append((32,8192)); cases.append((32,9)); cases.append((32,289)); cases.append((32,332929))
    cases.append((64,32768))
    # deduplicate, keep order
    cases=list(dict.fromkeys(cases))
    total_bad=0
    for m,q in cases:
        try:
            total_bad+=check(m,q)
        except Exception as ex:
            print(f"m={m} q={q} ERROR {type(ex).__name__}: {ex}", flush=True)
    print(f"TOTAL_BAD_GROUPS={total_bad}")

if __name__=="__main__":
    main()
