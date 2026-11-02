#!/usr/bin/env python3
"""Wave 46, task 7, step 7: exhaustive (81, 512) joint compatibility search.

A full pair with components only at 81 and 512 (rest zero) is exactly a
pair of joint sequences (y81, y512), (y81', y512') with equal multiset
of the 24 value-pairs (this is the common-sigma condition). Enumerate
all bases (81 x 512) and all fiber-mates, check joint multiset equality,
and test Pi_81 ∩ Pi_512. A failure is an exact full-PC counterexample
(slice and other components zero, hence full there).
"""
D4 = []
for b in range(4):
    D4.append(tuple((r + b) % 4 for r in range(4)))
    D4.append(tuple((-r + b) % 4 for r in range(4)))
D4 = sorted(set(D4))
D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

def name(pi):
    if all(pi[r] == (r + pi[0]) % 4 for r in range(4)):
        return f"s{pi[0]}"
    b = pi[0] % 4
    if all(pi[r] == (-r + b) % 4 for r in range(4)):
        return f"f{b}"
    return str(pi)

def kernel_small(q):
    out = []
    for y0 in range(q):
        for y1 in range(q):
            y = [0] * 26
            y[0], y[1] = y0, y1
            for n in range(24):
                y[n + 2] = (6 * y[n + 1] - y[n]) % q
            if y[24] == y0 and y[25] == y1:
                out.append(tuple(y[:24]))
    return out

def prof(y):
    return tuple(tuple(sorted(y[i] for i in range(24) if i % 4 == r))
                  for r in range(4))

def pi_set(p, pp):
    return frozenset(name(pi) for pi in D4
                     if all(pp[r] == p[pi[r]] for r in range(4)))

def fibers(K):
    by_mult = {}
    for y in K:
        by_mult.setdefault(tuple(sorted(y)), []).append(y)
    fib = {}
    for ys in by_mult.values():
        for y in ys:
            fib[y] = ys
    return fib

K81 = kernel_small(81)
K512 = kernel_small(512)
F81 = fibers(K81)
F512 = fibers(K512)
P81 = {y: prof(y) for y in K81}
P512 = {y: prof(y) for y in K512}
print(f"|ker81|={len(K81)} |ker512|={len(K512)}")

tot_mates = 0
joint_pairs = 0
dihedral_joint = 0
failures = []
for y81 in K81:
    for y512 in K512:
        base_key = tuple(sorted(zip(y81, y512)))
        for m81 in F81[y81]:
            for m512 in F512[y512]:
                if m81 == y81 and m512 == y512:
                    continue
                tot_mates += 1
                if tuple(sorted(zip(m81, m512))) != base_key:
                    continue
                joint_pairs += 1
                p81 = pi_set(P81[y81], P81[m81])
                p512 = pi_set(P512[y512], P512[m512])
                if p81 & p512:
                    if any(tuple(y81[d[i]] for i in range(24)) == m81 and
                           tuple(y512[d[i]] for i in range(24)) == m512
                           for d in D24):
                        dihedral_joint += 1
                else:
                    failures.append((y81, y512, m81, m512, p81, p512))
print(f"mate combos checked: {tot_mates}")
print(f"joint pairs (ordered, excl diagonal): {joint_pairs}")
print(f"dihedral joint pairs: {dihedral_joint}")
print(f"FAILURES (Pi81 ∩ Pi512 empty): {len(failures)}")
for (y81, y512, m81, m512, p81, p512) in failures[:10]:
    print(f"  FAIL base81={y81}")
    print(f"       base512={y512}")
    print(f"       mate81={m81}")
    print(f"       mate512={m512}")
    print(f"       Pi81={sorted(p81)} Pi512={sorted(p512)}")
