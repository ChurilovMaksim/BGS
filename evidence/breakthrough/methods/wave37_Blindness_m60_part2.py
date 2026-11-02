"""Wave 37, task 1 (retry), part 2: large components, slice grouping,
joint test for {625}, supported 2-fiber count at (60,128)."""
import math, sys
import numpy as np
from collections import defaultdict
sys.path.insert(0, ".")
exec(open("wave37_Blindness_m60.py").read().split("# ---------- small components")[0])

# ---------- slice grouping: pairs (a,b) in F81 x F625-fiber ----------
pts81 = kernel_points(M, 81)
fib81 = defaultdict(list)
for p in pts81: fib81[tuple(sorted(p))].append(p)
split81 = [v for v in fib81.values() if len(gamma_orbits(v, M)) > 1]
assert len(split81) == 1
F81 = split81[0]
orb81_of = {}
for oi, orb in enumerate(gamma_orbits(F81, M)):
    for p in orb: orb81_of[p] = oi
pts625 = kernel_points(M, 625)
fib625 = defaultdict(list)
for p in pts625: fib625[tuple(sorted(p))].append(p)
split625 = [v for v in fib625.values() if len(gamma_orbits(v, M)) > 1]
print(f"slice: F81={len(F81)} pts, split625 fibers={len(split625)} sizes={[len(v) for v in split625]}", flush=True)
for fi, F in enumerate(split625):
    groups = defaultdict(list)
    for a in F81:
        for b in F:
            groups[tuple(sorted(a[i]*625 + b[i] for i in range(M)))].append((a, b))
    norb = sorted({len({orb81_of[a] for a, b in g}) for g in groups.values()})
    print(f"  625-fiber {fi}: {len(groups)} joint fibers, 81-orbits per fiber set={norb}, "
          f"sizes={sorted(len(g) for g in groups.values())}", flush=True)

# ---------- large components: seeds, cyclicity, level reps ----------
def large_seeds(q, p):
    Mm = mat_pow([6, q-1, 1, 0], M, q)
    a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
    y0 = np.arange(q, dtype=np.int64)
    g = math.gcd(a, q)
    mask = (b*y0) % g == 0
    y0m = y0[mask]
    a1, q1 = a//g, q//g
    inv = pow(a1, -1, q1) if q1 > 1 else 0
    y1_0 = ((-(b*y0m)//g) * inv) % q1
    step = q//g
    total = 0; gen = None
    for k in range(g):
        y1 = y1_0 + k*step
        ok = np.nonzero((c*y1 + d*y0m) % q == 0)[0]
        total += len(ok)
        if gen is None and len(ok):
            for idx in ok:
                s0, s1 = int(y0m[idx]), int(y1[idx])
                if s0 % p != 0 or s1 % p != 0:
                    gen = (s0, s1); break
            if gen is not None: pass
    return total, gen

large = [(1681, 41), (3481, 59), (72361, 269), (361201, 601), (923521, 31), (5202961, 2281)]
large_results = {}
for q, p in large:
    total, gen = large_seeds(q, p)
    assert total == q, (q, total)
    e = round(math.log(q, p))
    reps = []
    if gen is not None:
        cur = gen
        for _ in range(e):
            reps.append(cur)
            cur = ((cur[0]*p) % q, (cur[1]*p) % q)
    reps.append((0, 0))
    print(f"q={q} (p={p}, e={e}): kernel={total} cyclic={gen is not None} gen={gen}", flush=True)
    for (s0, s1) in reps:
        o = seq_from(s0, s1, M, q)
        c625_any = any(triple_collides(a, fib, o, q, 625) for a in a_reps for fib in reps625)
        c625_all = all(triple_collides(a, fib, o, q, 625) for a in a_reps for fib in reps625)
        c81_any = any(triple_collides(b, reps81[0], o, q, 81) for b in b_reps)
        print(f"   seed=({s0},{s1}): blind625 any={c625_any} all={c625_all} blind81 any={c81_any}", flush=True)
    large_results[q] = dict(cyclic=gen is not None, gen=gen)
print("LARGE DONE", flush=True)

# ---------- joint test for {625}: pairs (o49, o121), rest zero ----------
pts49 = kernel_points(M, 49)
pts121 = kernel_points(M, 121)
def pack4(a, b, o1, o2):
    return [((a[i]*625 + b[i])*121 + o2[i])*49 + o1[i] for i in range(M)]
joint_any = joint_all = 0
per_a = defaultdict(int)
for o49 in pts49:
    for o121 in pts121:
        colls = []
        for a in a_reps:
            for fib in reps625:
                ms = set()
                hit = False
                for b in fib:
                    key = tuple(sorted(pack4(a, b, o49, o121)))
                    if key in ms: hit = True; break
                    ms.add(key)
                colls.append(hit)
        if any(colls): joint_any += 1
        if all(colls): joint_all += 1
        for ai, c in enumerate(colls):
            if c: per_a[ai] += 1
print(f"JOINT {{625}}: pairs total={len(pts49)*len(pts121)} any={joint_any} all={joint_all} "
      f"per-a-rep (any over fibers) counts={[per_a[i] for i in range(len(a_reps))]}", flush=True)

# ---------- supported 2-fibers at (60,128) ----------
from wave16_d1a_targeted import Dm, snf_kernel, torsion_data, comp_supported, group_ids
D = Dm(60)
q2 = 128
Z, Qmod = torsion_data(60, D)
pts = snf_kernel(60, q2)
assert len(pts) == q2
fib = group_ids(np.sort(pts, axis=1))
sup = comp_supported(pts, Z, Qmod, q2)
sizes, partial = [], 0
for f in range(int(fib.max()) + 1):
    idx = np.where(fib == f)[0]
    s = int(sup[idx].sum())
    if s > 0: sizes.append(int(len(idx)))
    if 0 < s < len(idx): partial += 1
print(f"2-PART: q2={q2} |Z|={len(Z)} supported_pts={int(sup.sum())} "
      f"supported_fibers={len(sizes)} max_size={max(sizes)} partial={partial}", flush=True)
print("PART2 DONE", flush=True)
