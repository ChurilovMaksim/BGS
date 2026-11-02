"""Wave 35, task 5, exploration part 2: m=6 landscape.

Q1: For every kernel vector mod 49, do even/odd class multisets coincide?
Q2: For every kernel vector mod 25, what are the class multisets?
Q3: Over ALL fiber pairs at m=6, how many are dihedrally related?
Q4: In the a=b subcase, is each fiber exactly one dihedral orbit?
"""
from collections import Counter, defaultdict
import sys
sys.path.insert(0, '.')
from wave35_G2odd1_explore import kernel_mod, crt_combine_all, dihedral_orbit, pi_set, Dm


def main():
    m = 6
    # Q1/Q2: component kernels
    for q in (25, 49):
        k = kernel_mod(m, q)
        eq = sum(1 for v in k
                 if Counter(v[i] % q for i in range(m) if i % 2 == 0)
                 == Counter(v[i] % q for i in range(m) if i % 2 == 1))
        print(f"mod {q}: kernel {len(k)} pts, M_E == M_O for {eq} of them")
    # Q3/Q4: full enumeration
    kernels = [(q, kernel_mod(m, q)) for q in (32, 25, 49)]
    pts = crt_combine_all(kernels)
    fibers = defaultdict(list)
    for y in pts:
        fibers[tuple(sorted(y))].append(y)
    tot_pairs = 0
    dih_pairs = 0
    ab_fibers = 0
    ab_fiber_eq_orbit = 0
    ab_fiber_sizes = Counter()
    for key, members in fibers.items():
        if len(members) < 2:
            continue
        base = members[0]
        base32 = tuple(v % 32 for v in base)
        is_ab = len(set(base32)) == 1
        orb = dihedral_orbit(base, m)
        for other in members[1:]:
            tot_pairs += 1
            if other in orb:
                dih_pairs += 1
        if is_ab:
            ab_fibers += 1
            ab_fiber_sizes[len(members)] += 1
            if set(members) == orb:
                ab_fiber_eq_orbit += 1
    print(f"total fiber pairs: {tot_pairs}, dihedrally related: {dih_pairs}")
    print(f"a=b fibers: {ab_fibers}, exactly one dihedral orbit: "
          f"{ab_fiber_eq_orbit}")
    print(f"a=b fiber sizes: {dict(sorted(ab_fiber_sizes.items()))}")


if __name__ == "__main__":
    main()
