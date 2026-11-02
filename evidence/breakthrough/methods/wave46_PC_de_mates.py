#!/usr/bin/env python3
"""Wave 46, task 7, step 3 (revised): slice mates via (d, e) enumeration.

Mod-p lemma (wave 12 s3a): two recurrence sequences mod p with the same
multiset are dihedral images. So every slice mate (C', D') of base (C, D)
has t' = t o d, s' = s o e for dihedral d, e in D_24, and the pair
multiset condition is {(t[d(i)], s[e(i)])} = {(t[i], s[i])}.
Enumerating all 48x48 (d, e) gives ALL slice mates exactly (modulo s3a).
A mate is a dihedral image of base iff some single d' gives both t' and s'.
"""
from collections import Counter

def trace_seq(a, b, p):
    s = []
    ca, cb = a, b
    for _ in range(24):
        s.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(s)

D24 = []  # (kind, k): kind 0 = shift i -> i+k, 1 = reflection i -> -i+k
for k in range(24):
    D24.append((0, k))
    D24.append((1, k))

def apply(d, i):
    kind, k = d
    return (i + k) % 24 if kind == 0 else (-i + k) % 24

def name_d(d):
    kind, k = d
    return f"shift{k}" if kind == 0 else f"refl{k}"

C0, D0 = (1, 2), (3, 5)
t0 = trace_seq(*C0, 17)
s0 = trace_seq(*D0, 1153)
base_pairs = sorted(zip(t0, s0))

# sequences t o d, s o e for all d, e (as tuples); mate C', D' recovered
# from first two coordinates: C' determined by (t'[0], t'[1]) etc.
# Instead of recovering C', D', report (d, e) and check dihedral-image
# status directly on sequences.
def seq_of_t(d):
    return tuple(t0[apply(d, i)] for i in range(24))

def seq_of_s(e):
    return tuple(s0[apply(e, i)] for i in range(24))

t_by_d = {d: seq_of_t(d) for d in D24}
s_by_e = {e: seq_of_s(e) for e in D24}

hits = []
for d in D24:
    td = t_by_d[d]
    for e in D24:
        se = s_by_e[e]
        if sorted(zip(td, se)) == base_pairs:
            hits.append((d, e))
print(f"(d,e) hits: {len(hits)}")

# dihedral image test: exists d' with t o d' == td and s o d' == se
def is_dihedral_image(td, se):
    for dp in D24:
        if t_by_d[dp] == td and s_by_e[dp] == se:
            return True, dp
    return False, None

non_di = []
for (d, e) in hits:
    td, se = t_by_d[d], s_by_e[e]
    dih, dp = is_dihedral_image(td, se)
    tag = "DIH" if dih else "NONDIH"
    print(f"  {tag} d={name_d(d)} e={name_d(e)}" +
          (f" via {name_d(dp)}" if dih else ""))
    if not dih:
        non_di.append((d, e, td, se))
print(f"non-dihedral mates: {len(non_di)}")

# Recover (C', D') for non-dihedral mates from (t'[0], t'[1]) and
# (s'[0], s'[1]): t'[0] = 2a mod p, t'[1] = (6a+8b) mod p.
def recover(seq, p):
    inv2 = pow(2, -1, p)
    inv8 = pow(8, -1, p)
    a = (seq[0] * inv2) % p
    b = ((seq[1] - 3 * seq[0]) * inv8) % p
    return (a, b)

with open("wave46_PC_slicemates.log", "w") as f:
    for (d, e, td, se) in non_di:
        C = recover(td, 17)
        D = recover(se, 1153)
        # verify recovery reproduces sequences
        assert trace_seq(*C, 17) == td, "C recovery failed"
        assert trace_seq(*D, 1153) == se, "D recovery failed"
        f.write(f"MATE C=({C[0]},{C[1]}) D=({D[0]},{D[1]}) d={name_d(d)} e={name_d(e)}\n")
        print(f"MATE C={C} D={D} d={name_d(d)} e={name_d(e)}")
print("mates written to wave46_PC_slicemates.log")
