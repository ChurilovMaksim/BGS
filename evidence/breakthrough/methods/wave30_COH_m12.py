"""Wave 30, task 3: COH at m=12 across ALL components -- exact test.

D_12 = 2*768398401 - 2 = 1536796800 = 2^7 * 3^4 * 5^2 * 7^2 * 11^2,
components q in {128, 81, 25, 49, 121}. Genuine parameters mod D_12
number 1536796800: direct grouping is infeasible.

Exact reduction. For genuine A, S(A) = (Tr(A alpha^i))_{i in Z/12}
(12-periodic by genuineness). A pair (A, A') shares the joint global
multiset iff some permutation sigma of Z/12 sends S(A) to S(A');
COH holds for the pair iff some DIHEDRAL tau (shift/reflect) does.
Key lemma: if some component q0 has distinct S_q0 values and every
genuine sequence that is a permutation of S_q0 is a dihedral image
of S_q0, then every valid sigma equals a dihedral tau (forced by
distinct values), so COH holds at A. Hence a COH failure forces
A_q in B_q for EVERY q, where B_q = {A_q : S_q has a repeat OR the
class of S_q contains a non-dihedral image sequence}. B_q are tiny
(checked below); enumerating tuples in prod(B_q) with a joint
sigma-backtrack (sigma(0), sigma(1) + recurrence + per-component
genuine-sequence membership) is exhaustive over all joint-global
groups. No Lean, repository untouched.
"""
import math
from collections import defaultdict

ALPHA = (3, 2)
M = 12
QS = [128, 81, 25, 49, 121]

def mul(a, b, q):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % q, (a[0]*b[1] + a[1]*b[0]) % q)

def pw(a, n, q):
    r = (1, 0)
    for _ in range(n):
        r = mul(r, a, q)
    return r

def conj(a, q):
    return (a[0] % q, (-a[1]) % q)

def tr(a, q):
    return (2*a[0]) % q

def genuine(q):
    d = pw(ALPHA, M, q)
    d = ((d[0]-1) % q, d[1])
    return [(x, y) for x in range(q) for y in range(q)
            if mul(d, (x, y), q) == (0, 0)]

def seq_of(A, q):
    out = []
    b = A
    for _ in range(M):
        out.append(tr(b, q))
        b = mul(b, ALPHA, q)
    return tuple(out)

def ann(q):
    pows = [pw(ALPHA, n, q) for n in range(M)]
    return {(x, y) for x in range(q) for y in range(q)
            if all(tr(mul((x, y), p, q), q) == 0 for p in pows)}

def shadow(q):
    if q == 81:
        return {(27*a % 81, 27*b % 81) for a in range(3) for b in range(3)}
    return {(0, 0)}

DIH = []
for k in range(12):
    DIH.append(tuple((i + k) % 12 for i in range(12)))
    DIH.append(tuple((-i + k) % 12 for i in range(12)))
DIH = sorted(set(DIH))
assert len(DIH) == 24

def apply_sigma(S, sigma):
    return tuple(S[sigma[i]] for i in range(12))

def main():
    comp = {}
    for q in QS:
        G = genuine(q)
        seqdict = defaultdict(list)
        seqs = {}
        for A in G:
            s = seq_of(A, q)
            seqs[A] = s
            seqdict[s].append(A)
        classes = defaultdict(list)
        for A in G:
            classes[tuple(sorted(seqs[A]))].append(A)
        # per-component rigidity (bonus check)
        Aq = ann(q)
        Sh = shadow(q)
        cur = (1, 0)
        ordq = None
        for j in range(1, 1000000):
            cur = mul(cur, ALPHA, q)
            if cur == (1, 0):
                ordq = j
                break
        powq = [(1, 0)]
        for _ in range(ordq):
            powq.append(mul(powq[-1], ALPHA, q))
        rigid_bad = 0
        for members in classes.values():
            A0 = members[0]
            for A in members[1:]:
                ok = False
                for c in (0, 1):
                    b0 = conj(A0, q) if c else A0
                    for j in range(ordq):
                        d = ((A[0]-mul(b0, powq[j], q)[0]) % q,
                             (A[1]-mul(b0, powq[j], q)[1]) % q)
                        if d in Aq:
                            ok = True
                            break
                        for w in Sh:
                            if ((d[0]-w[0]) % q, (d[1]-w[1]) % q) in Aq:
                                ok = True
                                break
                        if ok:
                            break
                    if ok:
                        break
                if not ok:
                    rigid_bad += 1
        # B_q: repeat in S_q, or class contains non-dihedral image
        B = []
        for A in G:
            S = seqs[A]
            has_repeat = len(set(S)) < 12
            dih_images = {apply_sigma(S, t) for t in DIH}
            class_seqs = {seqs[X] for X in classes[tuple(sorted(S))]}
            if has_repeat or not class_seqs <= dih_images:
                B.append(A)
        comp[q] = dict(G=G, seqs=seqs, seqdict=seqdict, B=B,
                       classes=classes, ord=ordq, Ann=Aq, Sh=Sh)
        print(f"q={q} |G|={len(G)} |Ann|={len(Aq)} |Shadow|={len(Sh)} "
              f"ord={ordq} classes={len(classes)} "
              f"maxclass={max(len(v) for v in classes.values())} "
              f"rigid_bad={rigid_bad} |B|={len(B)}", flush=True)

    total = math.prod(len(comp[q]['B']) for q in QS)
    print(f"prod |B_q| = {total}", flush=True)

    # joint sigma-backtrack over tuples in prod(B_q)
    def joint_sigmas(Ss):
        """All sigma with sigma(S_q) a genuine sequence for every q.
        Ss: dict q -> S_q. Backtrack sigma(0), sigma(1) + recurrence."""
        res = []
        used = [False]*12
        sig = [None]*12
        P = {q: [None]*12 for q in QS}

        def rec(i):
            if i == 12:
                for q in QS:
                    Pq = tuple(P[q])
                    if (6*Pq[11] - Pq[10]) % q != Pq[0]:
                        return
                    if (6*Pq[0] - Pq[11]) % q != Pq[1]:
                        return
                    if Pq not in comp[q]['seqdict']:
                        return
                res.append(tuple(sig))
                return
            if i < 2:
                for j in range(12):
                    if not used[j]:
                        used[j] = True
                        sig[i] = j
                        for q in QS:
                            P[q][i] = Ss[q][j]
                        rec(i+1)
                        used[j] = False
                return
            # candidates j unused with S_q[j] == need_q for all q
            cands = None
            for q in QS:
                need = (6*P[q][i-1] - P[q][i-2]) % q
                s = {j for j in range(12)
                     if not used[j] and Ss[q][j] == need}
                cands = s if cands is None else (cands & s)
                if not cands:
                    return
            for j in sorted(cands):
                used[j] = True
                sig[i] = j
                for q in QS:
                    P[q][i] = Ss[q][j]
                rec(i+1)
                used[j] = False

        rec(0)
        return res

    import itertools
    n_checked = 0
    n_sigmas = 0
    for tup in itertools.product(*[comp[q]['B'] for q in QS]):
        n_checked += 1
        Ss = {q: comp[q]['seqs'][A] for q, A in zip(QS, tup)}
        for sigma in joint_sigmas(Ss):
            n_sigmas += 1
            # dihedral-equivalent? exists tau with tau(S_q)==sigma(S_q) all q
            ok = False
            for tau in DIH:
                if all(apply_sigma(Ss[q], tau) ==
                       apply_sigma(Ss[q], sigma) for q in QS):
                    ok = True
                    break
            if not ok:
                print(f"*** COH FAILURE: tuple={tup} sigma={sigma}",
                      flush=True)
                # reconstruct A, A' via CRT and verify directly
                D = math.prod(QS)
                Aprime = []
                for q, A in zip(QS, tup):
                    Sp = apply_sigma(Ss[q], sigma)
                    Aprime.append(comp[q]['seqdict'][Sp][0])

                def crt1(rs):
                    x = 0
                    Mc = 1
                    for r, q in zip(rs, QS):
                        inv = pow(Mc % q, -1, q)
                        t = ((r - x) % q) * inv % q
                        x += Mc * t
                        Mc *= q
                    return x % D

                Aglob = (crt1([A[0] for A in tup]),
                         crt1([A[1] for A in tup]))
                Apglob = (crt1([A[0] for A in Aprime]),
                          crt1([A[1] for A in Aprime]))

                def globalseq(A):
                    out = []
                    b = A
                    for _ in range(12):
                        out.append(tr(b, D))
                        b = mul(b, ALPHA, D)
                    return tuple(out)

                sA = globalseq(Aglob)
                sAp = globalseq(Apglob)
                print(f"  A={Aglob} A'={Apglob}", flush=True)
                print(f"  joint multisets equal: "
                      f"{sorted(sA) == sorted(sAp)}", flush=True)
                print(f"  dihedral tau works: "
                      f"{any(apply_sigma(sA, t) == sAp for t in DIH)}",
                      flush=True)
                # direct (j,c) check with Ann+Shadow slack, per component
                slack = {}
                for q in QS:
                    s = set()
                    for z in comp[q]['Ann']:
                        for w in comp[q]['Sh']:
                            s.add(((z[0]+w[0]) % q, (z[1]+w[1]) % q))
                    slack[q] = s
                L = 1
                for q in QS:
                    L = L * comp[q]['ord'] // math.gcd(L, comp[q]['ord'])
                powq = {}
                for q in QS:
                    p = [(1, 0)]
                    for _ in range(L):
                        p.append(mul(p[-1], ALPHA, q))
                    powq[q] = p
                Aq_c = {q: (tup[i][0] % q, tup[i][1] % q)
                        for i, q in enumerate(QS)}
                Ap_c = {q: (Aprime[i][0] % q, Aprime[i][1] % q)
                        for i, q in enumerate(QS)}
                found_jc = None
                for c in (0, 1):
                    for j in range(L):
                        good = True
                        for q in QS:
                            b0 = conj(Aq_c[q], q) if c else Aq_c[q]
                            bj = mul(b0, powq[q][j], q)
                            d = ((Ap_c[q][0]-bj[0]) % q,
                                 (Ap_c[q][1]-bj[1]) % q)
                            if d not in slack[q]:
                                good = False
                                break
                        if good:
                            found_jc = (j, c)
                            break
                    if found_jc:
                        break
                print(f"  single (j,c) with Ann+Shadow slack exists: "
                      f"{found_jc}", flush=True)
                return
    print(f"tuples checked={n_checked} valid sigmas found={n_sigmas}",
          flush=True)
    print("COH HOLDS at m=12: every valid sigma over every candidate "
          "tuple is dihedral-equivalent; no failing joint-global group",
          flush=True)

if __name__ == '__main__':
    main()
