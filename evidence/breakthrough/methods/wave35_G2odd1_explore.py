"""Wave 35, task 5, exploration: the t=2, a=b subcase at m=6.

Enumerate Fix_6 by CRT over (32, 25, 49). For fiber pairs whose
mod-32 component is constant (a=b subcase), compute:
  - Pi_25, Pi_49 (per-class multiset pi-sets mod 25, 49),
  - whether y' is in the dihedral orbit of y (global dihedral relation),
  - per odd q, the trace-model parameters B_q, B'_q in R/qR and the
    beta-orbit relation (id-type / swap-type / both).
"""
import itertools
from collections import Counter, defaultdict


def Dm(m):
    s0, s1 = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s0, s1 = s1, 6 * s1 - s0
    return s1 - 2


def kernel_mod(m, mod):
    """All sequences mod `mod` satisfying recurrence + m-periodicity."""
    out = []
    for a in range(mod):
        for b in range(mod):
            seq = [a, b]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m + 1] == b:
                out.append(tuple(seq[:m]))
    return out


def crt_pair(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    return tuple((x + mod_a * (((y - x) * inv) % mod_b)) % (mod_a * mod_b)
                 for x, y in zip(A, B))


def crt_combine_all(kernels):
    pts = kernels[0][1]
    cur = kernels[0][0]
    for q, k in kernels[1:]:
        pts = [crt_pair(p, cur, r, q) for p in pts for r in k]
        cur *= q
    return pts


def dihedral_orbit(y, m):
    orb = set()
    for eps in (1, -1):
        for k in range(m):
            orb.add(tuple(y[(eps * i + k) % m] for i in range(m)))
    return orb


def pi_set(y, yp, m, q, t=2):
    """pi in D_t with per-class multisets mod q of yp = those of y o pi."""
    def cls(v):
        return [Counter(v[i] % q for i in range(m) if i % t == r)
                for r in range(t)]
    C, Cp = cls(y), cls(yp)
    res = []
    for pi in [tuple(range(t)), tuple(reversed(range(t)))]:
        if all(Cp[r] == C[pi[r]] for r in range(t)):
            res.append('id' if pi == tuple(range(t)) else 'swap')
    return set(res)


def param_mod_q(seq_q, q):
    """Solve B = x + y*sqrt(2) in R/qR with Tr(B)=seq0, Tr(B*alpha)=seq1."""
    y0, y1 = seq_q[0] % q, seq_q[1] % q
    inv2 = pow(2, -1, q)
    inv8 = pow(8, -1, q)
    x = (y0 * inv2) % q
    y = ((y1 - 6 * x) * inv8) % q
    return (x, y)


def mul(p, r, q):
    return ((p[0] * r[0] + 2 * p[1] * r[1]) % q,
            (p[0] * r[1] + p[1] * r[0]) % q)


def conj(p, q):
    return (p[0], (-p[1]) % q)


def beta_orbit(B, q):
    beta = (17 % q, 12 % q)  # alpha^2 = 17 + 12 sqrt2
    orb = set()
    cur = (1 % q, 0)
    for _ in range(q * 2 + 10):
        orb.add(mul(cur, B, q))
        cur = mul(cur, beta, q)
        if cur == (1 % q, 0):
            break
    return orb


def rel_type(B, Bp, q):
    """'id' if Bp in <beta>-orbit of B or conj(B); 'swap' if in orbit of
    B*alpha or conj(B*alpha); 'both' if both; 'neither' otherwise."""
    alpha = (3 % q, 2 % q)
    orb_id = beta_orbit(B, q) | beta_orbit(conj(B, q), q)
    Ba = mul(B, alpha, q)
    orb_swap = beta_orbit(Ba, q) | beta_orbit(conj(Ba, q), q)
    i = Bp in orb_id
    s = Bp in orb_swap
    if i and s:
        return 'both'
    if i:
        return 'id'
    if s:
        return 'swap'
    return 'neither'


def main():
    m = 6
    mods = [32, 25, 49]
    kernels = [(q, kernel_mod(m, q)) for q in mods]
    for q, k in kernels:
        print(f"kernel mod {q}: {len(k)} points (expect {q})")
    pts = crt_combine_all(kernels)
    print(f"Fix_6 points: {len(pts)} (expect {Dm(m)})")
    D = Dm(m)

    fibers = defaultdict(list)
    for y in pts:
        fibers[tuple(sorted(y))].append(y)
    print(f"fibers: {len(fibers)}")

    # mod-32 component index: rebuild component decomposition
    # points were combined in order 32, then 25, then 49; recover mod32
    # directly from values mod 32.
    ab_pairs = 0
    stats = Counter()
    dihedral_yes = 0
    rel_mismatch = 0
    pi_patterns = Counter()
    examples = defaultdict(list)
    for key, members in fibers.items():
        if len(members) < 2:
            continue
        base = members[0]
        base32 = tuple(v % 32 for v in base)
        if len(set(base32)) != 1:
            continue  # not the a=b subcase
        for other in members[1:]:
            ab_pairs += 1
            p25 = pi_set(base, other, m, 25)
            p49 = pi_set(base, other, m, 49)
            common = p25 & p49
            pi_patterns[(tuple(sorted(p25)), tuple(sorted(p49)),
                         tuple(sorted(common)))] += 1
            if not common:
                print("COMMON-PI FAILURE", base, other, p25, p49)
            orb = dihedral_orbit(base, m)
            if other in orb:
                dihedral_yes += 1
            # parameter relations per odd q
            for q in (25, 49):
                sq = tuple(v % q for v in base)
                sp = tuple(v % q for v in other)
                B = param_mod_q(sq, q)
                Bp = param_mod_q(sp, q)
                rt = rel_type(B, Bp, q)
                want = 'both' if len(p25 if q == 25 else p49) == 2 else \
                    ('id' if 'id' in (p25 if q == 25 else p49) else 'swap')
                if rt != want and not (rt == 'both' and want in ('id', 'swap')) \
                        and not (want == 'both' and rt in ('id', 'swap')):
                    # tolerate 'both' vs singleton mismatches only if the
                    # other side also allows it; count strict mismatches
                    if rt != want:
                        rel_mismatch += 1
                        if len(examples['rel']) < 5:
                            examples['rel'].append((q, base, other, rt, want))
            stats['pairs'] += 1
    print(f"a=b fiber pairs: {ab_pairs}")
    print(f"dihedrally related: {dihedral_yes}")
    print(f"parameter-relation strict mismatches: {rel_mismatch}")
    for e in examples['rel']:
        print("  REL example:", e)
    print("pi patterns (Pi25, Pi49, common):")
    for k, v in sorted(pi_patterns.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
