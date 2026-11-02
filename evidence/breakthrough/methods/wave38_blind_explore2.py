import math
from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

m = 60
sf625 = split_fibers(m, 625)
sf81 = split_fibers(m, 81)
a_fixed = sf81[0][1][0]
print(f"81 fiber: {len(sf81)} fiber(s), orbit counts {[len(r) for _, r in sf81]}")
for fi, (key, reps) in enumerate(sf81):
    print(f"--- 81 fiber {fi}: periods {[period(r) for r in reps]}")
    for r in reps:
        C = recover_C(r, 81)
        print(f"    rep C={C} check={check_C(r, C, 81)}")

# t_i = Tr(sqrt2 * alpha^i) mod 25, via recurrence: t_0 = 0, t_1 = 4 (Tr(sqrt2*(3+2sqrt2)) = Tr(2*2 + 3 sqrt2)= 4? check: sqrt2*(3+2sqrt2) = 3 sqrt2 + 4, trace = 8? No: Tr(a + b sqrt2) = 2a. 3 sqrt2+4 -> a=4 -> Tr=8. Hmm recompute below directly from C=(0,1) mod 25 sequence.)
def seq_from_C(C, q, m):
    x, y = C
    t = [(2*x) % q, (2*(3*x+4*y)) % q]
    for i in range(2, m): t.append((6*t[-1]-t[-2]) % q)
    return tuple(t)

t = seq_from_C((0, 1), 25, m)
print(f"t period: {period(t)}, t values multiset: {sorted(Counter(t).items())}")
print(f"t = {t[:30]}")
# units u mod 25 with u = +/-1 mod 5
units = [u for u in range(1, 25) if math.gcd(u, 25) == 1 and u % 5 in (1, 4)]
print(f"units = +/-1 mod 5: {units}")
for u in units:
    ut = tuple((u*v) % 25 for v in t)
    print(f"  u={u}: multiset preserved? {sorted(ut) == sorted(t)}")

# (a,o)-fibers and u-invariance on fibers
def fiber_agree(a, o, b, bprime):
    fib = defaultdict(list)
    for i in range(m): fib[(a[i], o[i])].append(i)
    bad = []
    for v, idxs in fib.items():
        if sorted(b[i] for i in idxs) != sorted(bprime[i] for i in idxs):
            bad.append(v)
    return bad

reps625 = sf625[0][1]
# b and b' as full mod-625 sequences; also their mod-25 parts w = b/25
def div25(seq):
    assert all(v % 25 == 0 for v in seq)
    return tuple(v // 25 % 25 for v in seq)

ws = [div25(r) for r in reps625]
print(f"w periods: {[period(w) for w in ws]}")
print(f"w0 = {ws[0][:30]}")
for j in range(1, 5):
    # find u with wj = u * w0 pointwise?
    us = [u for u in range(25) if all((u*ws[0][i]) % 25 == ws[j][i] for i in range(m))]
    print(f"  w{j} = u*w0 for u in {us}")

for q0 in [49, 121, 361, 841]:
    pts0 = kernel_points(m, q0)
    # take a nonzero o; test all o? just first few nonzero + report counts
    blind = 0; total = 0; examples = []
    for o in pts0:
        if all(v == 0 for v in o): continue
        total += 1
        # check agreement of reps625[0] vs reps625[1] on (a_fixed, o)-fibers
        bad = fiber_agree(a_fixed, o, reps625[0], reps625[1])
        if not bad:
            blind += 1
            if len(examples) < 2: examples.append((o, period(o)))
    print(f"q0={q0}: nonzero={total} blind-for-625move(rep0,rep1)={blind} ex={[(period(o)) for o, _ in examples]}")
    # fiber structure for one o
    o = next(o for o in pts0 if any(o))
    fib = defaultdict(list)
    for i in range(m): fib[(a_fixed[i], o[i])].append(i)
    print(f"   period(o)={period(o)} #fibers={len(fib)} sizes={sorted(Counter(len(v) for v in fib.values()).items())}")
