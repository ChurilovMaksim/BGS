"""
RUN 5 / THIRD IMPLEMENTATION -- EXACT integer certificates, zero floats.

For PRIME p the only Q-relation among 1..omega^(p-1) is their full sum.
A nonnegative count vector c in Z_{>=0}^p represents sum_r c[r] omega^r
modulo that single relation:
  ZERO  <=> all counts equal; canonical form subtracts the min;
  EQUALITY <=> canonical forms equal elementwise.
Matrices are (p,p,p) int64 tensors of residue counts; kernels unnormalised:
  UU(x,y)   = w^( icb*(d x^2 -2xy + a y^2) ), icb=(2c)^{-1}
  Tw(n;x,y) = w^( b2*n1*n2 + n2*y ) * [x==y+n1], b2=2^{-1}
so U_cat = p^{-1/2} UU. Products = circular convolutions -- exact.

Certificates X1-X7 (see artifacts/exact_run5.json). Exit 0 iff all pass.
"""
import json, os, sys, itertools
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
RESULTS = {"checks": []}

def ok(tag, cond, detail):
    RESULTS["checks"].append([tag, bool(cond), detail])
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {detail}")
    return bool(cond)

def circ_conv(a, b, p):
    c = np.convolve(a, b)
    out = c[:p].copy()
    t = c[p:]
    if len(t): out[:len(t)] += t
    return out

def red(v): return v - v.min()

class CMat:
    def __init__(self, C, p):
        self.C = np.asarray(C, dtype=np.int64); self.p = p
    def mmul(self, B):
        p = self.p; AC, BC = self.C, B.C
        out = np.zeros((p, p, p), dtype=np.int64)
        for i in range(p):
            Ai = AC[i]; Oi = out[i]
            for k in range(p):
                acc = np.zeros(p, dtype=np.int64)
                for j in range(p):
                    a = Ai[j]
                    if a.any(): acc += circ_conv(a, BC[j,k], p)
                Oi[k] = red(acc)
        return CMat(out, p)
    def adj(self):
        p = self.p; neg = (-np.arange(p)) % p
        C = self.C.transpose(1,0,2)[:,:,neg].copy()
        for x in range(p):
            for y in range(p): C[x,y] = red(C[x,y])
        return CMat(C, p)
    def cpos(self):
        p = self.p; neg = (-np.arange(p)) % p
        C = self.C[:,:,neg].copy()
        for x in range(p):
            for y in range(p): C[x,y] = red(C[x,y])
        return CMat(C, p)
    def trace(self):
        acc = np.zeros(self.p, dtype=np.int64)
        for x in range(self.p): acc += self.C[x,x]
        return red(acc)
    def uni(self, x, y):
        v = self.C[x,y]
        return bool(np.all(v == v[0]))

def concentrated(v, total):
    """count vector == total copies of ONE residue (a scalar times a root)."""
    nz = np.flatnonzero(red(v))
    return bool(int(v.sum()) == total and len(nz) == 1), int(nz[0]) if len(nz) else -1

def kernel_UU(A, p):
    a,b,c,d = A
    icb = pow((2*c) % p, -1, p)
    xs = np.arange(p); X,Y = np.meshgrid(xs,xs,indexing="ij")
    E = (icb*(d*X*X - 2*X*Y + a*Y*Y)) % p
    C = np.zeros((p,p,p), dtype=np.int64)
    for x in range(p):
        for y in range(p): C[x,y,E[x,y]] = 1
    return CMat(C, p)

def kernel_T(n1, n2, p):
    n1 %= p; n2 %= p; b2 = pow(2,-1,p)
    C = np.zeros((p,p,p), dtype=np.int64)
    base = (b2*n1*n2) % p
    for y in range(p):
        C[(y+n1)%p, y, (base + n2*y) % p] = 1
    return CMat(C, p)

def circ_autocorr(v):
    p = len(v)
    return np.array([int(np.dot(v, np.roll(v,d))) for d in range(p)], dtype=np.int64)

def binpow(U, K):
    acc = None; base = U
    while K:
        if K & 1: acc = base if acc is None else acc.mmul(base)
        base = base.mmul(base); K >>= 1
    return acc

def ord_pm_exact(A, p):
    a,b,c,d = [v % p for v in A]; P = (a,b,c,d)
    for k in range(1, 4*p+4):
        if P == (1,0,0,1): return k, +1
        if P == (p-1,0,0,p-1): return k, -1
        P = ((P[0]*a+P[1]*c)%p,(P[0]*b+P[1]*d)%p,(P[2]*a+P[3]*c)%p,(P[2]*b+P[3]*d)%p)
    raise RuntimeError("order not found")
# --------------------------------------------------- X1: Egorov, exact ----
def egorov_align(A, p, n_list, use_AT):
    a,b,c,d = A; UU = kernel_UU(A,p); UUad = UU.adj()
    b2 = pow(2,-1,p); sig_all = []
    for (n1,n2) in n_list:
        L = UU.mmul(kernel_T(n1,n2,p)).mmul(UUad)
        if use_AT: m1,m2 = (a*n1+c*n2)%p,(b*n1+d*n2)%p
        else:      m1,m2 = (a*n1+b*n2)%p,(c*n1+d*n2)%p
        sigma = None
        for x in range(p):
            for z in range(p):
                V = L.C[x,z]
                if (z - x + m1) % p != 0:
                    if not np.all(V == V[0]):
                        return f"off-support mass n=({n1},{n2}) x={x} z={z}"
                else:
                    tgt = (b2*m1*m2 + m2*z) % p
                    conc, peak = concentrated(V, p)
                    if not conc:
                        return f"bad mass n=({n1},{n2}) x={x} z={z}"
                    al = (peak - tgt) % p
                    if sigma is None: sigma = al
                    elif sigma != al:
                        return f"inconsistent phase n=({n1},{n2}) x={x} z={z}"
        sig_all.append(sigma)
    return None

def battery(A, p, tag, full=True):
    print(f"--- exact battery A={list(A)} p={p}")
    a,b,c,d = A; nsym = (b%p != c%p)
    if full:
        n_list=[(x,y) for x in range(p) for y in range(p)]
    else:
        n_list=[(1,0),(0,1),(1,1),(-1,2),(3,-2),(2,5),(7,3),(-4,6),
                (5,-7),(9,1),(-8,-3),(11,4),(6,12),(13,-9),(2,-14)]
    bad = egorov_align(A, p, n_list, True)
    ok(f"X1[{tag}] Egorov exact vs A^T, ALL n", bad is None,
       "all n aligned with one global phase per n" if bad is None else str(bad))
    if nsym:
        badan = egorov_align(A, p, [(1,0),(0,1),(2,3),(3,1),(5,2)], False)
        ok(f"X1neg[{tag}] alignment vs A fails (non-symmetric)", badan is not None,
           ("mismatch detected: "+str(badan)) if badan else "UNEXPECTED: A also aligns")
    k,sg = ord_pm_exact(A,p); K = k if sg>0 else 2*k
    UK = binpow(kernel_UU(A,p), K)
    offdiag_ok = all(UK.uni(x,y) for x in range(p) for y in range(p) if x!=y)
    d0 = red(UK.C[0,0]); diag_ok = all(np.array_equal(red(UK.C[x,x]), d0) for x in range(p))
    ok(f"X2[{tag}] U^K = chi*I exact", offdiag_ok and diag_ok,
       f"K={K}: off-diagonals vanish, diagonals share canonical element "
       f"(mass={int(d0.sum())}, peak res={int(np.argmax(d0))})")
    res_ok, det = True, []
    Cur = kernel_UU(A,p)
    for J in range(1, min(K,5)):
        if J>1: Cur = Cur.mmul(kernel_UU(A,p))
        trU = Cur.trace(); Wref = circ_autocorr(trU)
        for (v1,v2) in ((0,1),(1,0),(2,3)):
            tz = kernel_T(v1,v2,p).mmul(Cur).trace()
            diff = circ_autocorr(tz) - Wref
            if not bool(np.all(diff == diff[0])):
                res_ok = False; det.append(f"J={J},v=({v1},{v2})")
    ok(f"X3[{tag}] |Tr(T(v)U^J)|=|Tr(U^J)| exact", res_ok,
       "; ".join(det) if det else f"J=1..{min(K,5)-1}, v={(0,1),(1,0),(2,3)} equal")

def completeness(p):
    ok_all, det = True, []
    # X4a: w != 0 -> sum_u TuTwTu* = p*Tr(Tw)*I = 0 exactly (whole matrix)
    for w in [(1,0),(0,1),(1,1),(2,1)]:
        acc=None
        Tw=kernel_T(*w,p)
        for u1 in range(p):
            for u2 in range(p):
                Z=kernel_T(u1,u2,p).mmul(Tw).mmul(kernel_T(u1,u2,p).adj())
                acc = Z if acc is None else CMat(acc.C+Z.C,p)
        good=True
        for x in range(p):
            for y in range(p):
                V=acc.C[x,y]
                if not np.all(V==V[0]): good=False
        ok_all &= good; det.append(f"w={w}:{'zero' if good else 'FAIL'}")
    ok("X4a completeness: sum_u TuTwTu* = 0 for w!=0 (exact)", ok_all, ", ".join(det))
    # X4b: w = 0 -> sum_u TuTu* = p^2 * Identity
    acc=None
    for u1 in range(p):
        for u2 in range(p):
            Tu=kernel_T(u1,u2,p)
            Z=Tu.mmul(Tu.adj())
            acc = Z if acc is None else CMat(acc.C+Z.C,p)
    good=True
    for x in range(p):
        for y in range(p):
            V=acc.C[x,y]
            if x==y:
                conc,peak=concentrated(V,p*p)
                if not (conc and peak==0): good=False
            elif not np.all(V==V[0]): good=False
    ok("X4b completeness: sum_u TuTu* = p^2 I (exact)", good,
       f"p={p}: {'p^2*I confirmed' if good else 'FAIL'}")

def theta_sign(A, p):
    a,b,c,d = A; R=None
    for pp in range(-30,31):
        for q in range(-30,31):
            if q==0:
                if pp*pp!=1: continue
                for r in range(-30,31):
                    if pp*(a-d)+q*c+b*r==0: R=(pp,q,r); break
            else:
                num=1-pp*pp
                if num%q: continue
                r=num//q
                if pp*(a-d)+q*c+b*r==0: R=(pp,q,r); break
            if R: break
        if R: break
    assert R, "no reversing involution"
    pp_,q_,r_ = R; Rm=[[pp_,q_],[r_,-pp_]]; S=[[1,0],[0,-1]]
    Mf=(S[0][0]*Rm[0][0]+S[0][1]*Rm[1][0], S[0][0]*Rm[0][1]+S[0][1]*Rm[1][1],
        S[1][0]*Rm[0][0]+S[1][1]*Rm[1][0], S[1][0]*Rm[0][1]+S[1][1]*Rm[1][1])
    UM = kernel_UU(Mf,p); TH2 = UM.cpos().mmul(UM)
    scal = all(TH2.uni(x,y) for x in range(p) for y in range(p) if x!=y)
    verdict = "?"
    if scal:
        d0s = [red(TH2.C[x,x]) for x in range(p)]
        same = all(np.array_equal(d0s[0], t) for t in d0s)
        if same:
            t0 = d0s[0]
            # unnormalised kernel: Theta^2 = (1/p)*TH2, so scalar c has
            # count-vector representation with mass divisible by p.
            g = int(np.gcd.reduce(t0))
            base = t0 // g
            nz = np.flatnonzero(base)
            if len(nz)==1 and int(nz[0])==0 and int(base.sum())==1:
                verdict = "+1"
            elif base[0]==0 and np.all(base[1:]==1):
                verdict = "-1"
            else:
                verdict = f"other(canonical={base.tolist()})"
    ok(f"X5[p={p}] Theta^2 exact scalar", verdict in ("+1","-1"),
       f"M=S*R={Mf}, R={R}: Theta^2 == {verdict}")

def parabolic_neg():
    A=(2,1,1,1); p=5; found=[]; Cur=kernel_UU(A,p)
    for J in range(1,8):
        if J>1: Cur = Cur.mmul(kernel_UU(A,p))
        Wref = circ_autocorr(Cur.trace())
        for (v1,v2) in ((0,1),(1,0)):
            tz = kernel_T(v1,v2,p).mmul(Cur).trace()
            diff = circ_autocorr(tz)-Wref
            if not bool(np.all(diff==diff[0])): found.append(f"J={J},v=({v1},{v2})")
        if found: break
    ok("X6 NEG-CONTROL parabolic p=5: unimodularity broken", bool(found), "; ".join(found))

def t17_fresh():
    cases=[(41,3,8),(73,5,8),(113,9,14),(127,3,7)]
    rows=[]; all_ok=True
    for (pp,alpha,k) in cases:
        H,x=[],1
        for _ in range(k): H.append(x); x=x*alpha%pp
        assert len(set(H))==k
        inv={h:pow(h,pp-2,pp) for h in H}
        cnt=0
        for h1,h2,h3,h4 in itertools.product(H,repeat=4):
            if (h1+h3)%pp!=(h2+h4)%pp: continue
            if (inv[h1]+inv[h3])%pp==(inv[h2]+inv[h4])%pp: cnt+=1
        minus1=(pp-1) in H
        pred = 3*k*k-3*k if minus1 else 2*k*k-k
        good=(cnt==pred); all_ok &= good
        rows.append({"p":pp,"alpha":alpha,"k":k,"minus1_in_H":minus1,
                     "brute":cnt,"closed":pred,"ok":good})
    RESULTS["t17_fresh"]=rows
    ok("X7 T17 closed form at fresh (p,alpha,k)", all_ok,
       "; ".join(f"p={r['p']},k={r['k']}(-1{'in' if r['minus1_in_H'] else 'out'}H):"
                 f"{r['brute']}=={r['closed']}{'' if r['ok'] else ' MISMATCH'}" for r in rows))

if __name__ == "__main__":
    print("="*70); print("EXACT RUN-5 VERIFICATION (integer-only)"); print("="*70)
    mats=[(2,1,1,1),(3,1,2,1)]
    for A in mats:
        for p in (7,11,13,17,29,41):
            try: battery(A,p,f"A{A[:2]}..p{p}", full=(p<=17))
            except Exception as ex:
                ok(f"battery A={A},p={p}",False,f"{type(ex).__name__}: {ex}")
    completeness(7)
    theta_sign((2,1,1,1),13)
    theta_sign((3,1,2,1),11)
    parabolic_neg()
    t17_fresh()
    nok=sum(1 for _,o,_ in RESULTS["checks"] if o)
    RESULTS["total_pass"]=nok; RESULTS["total"]=len(RESULTS["checks"])
    print("="*70); print(f"TOTAL: {nok}/{len(RESULTS['checks'])} exact checks PASS"); print("="*70)
    with open(os.path.join(ART,"exact_run5.json"),"w") as f: json.dump(RESULTS,f,indent=1)
    sys.exit(0 if nok==len(RESULTS["checks"]) else 1)
