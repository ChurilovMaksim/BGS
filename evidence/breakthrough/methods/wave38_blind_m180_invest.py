from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
m = 180
sf729 = split_fibers(m, 729)
sf625 = split_fibers(m, 625)
a625 = sf625[0][1][0]
pts361 = kernel_points(m, 361)
o = next(x for x in pts361 if any(v != 0 for v in x))
print(f"o period: {period(o)}")
# fibers of (a625, o)
fib = defaultdict(list)
for i in range(m): fib[(a625[i], o[i])].append(i)
print(f"#(a,o)-fibers: {len(fib)}, sizes: {sorted(Counter(len(v) for v in fib.values()).items())}")
# 729 fiber 0 reps
reps = sf729[0][1]
b0, b1 = reps[0], reps[1]
print(f"b0 period {period(b0)}, b1 period {period(b1)}")
print(f"b0[:36]: {b0[:36]}")
print(f"b1[:36]: {b1[:36]}")
print(f"b0/27 first 36: {[v//27 for v in b0[:36]]}")
print(f"b1/27 first 36: {[v//27 for v in b1[:36]]}")
print(f"all b0 divisible by 27: {all(v % 27 == 0 for v in b0)}, b1: {all(v % 27 == 0 for v in b1)}")
# check agreement on every (a,o)-fiber
bad = 0
for v, idxs in fib.items():
    if sorted(b0[i] for i in idxs) != sorted(b1[i] for i in idxs):
        bad += 1
        if bad <= 3:
            print(f"  disagreeing fiber {v}: idxs={idxs} b0={[b0[i] for i in idxs]} b1={[b1[i] for i in idxs]}")
print(f"disagreeing fibers for reps 0,1: {bad}/{len(fib)}")
# is b1 = b0 composed with a simple map?
for s in range(m):
    if all(b1[i] == b0[(i+s) % m] for i in range(m)):
        print(f"b1 = shift {s} of b0"); break
else:
    print("b1 is NOT a shift of b0")
if all(b1[i] == b0[(-i) % m] for i in range(m)): print("b1 = reversal of b0")
else: print("b1 is NOT a reversal of b0")
# check all rep pairs of fiber 0 for this o
for x in range(len(reps)):
    for y in range(x+1, len(reps)):
        agree = all(sorted(reps[x][i] for i in idxs) == sorted(reps[y][i] for i in idxs) for idxs in fib.values())
        if agree: print(f"colliding pair in fiber0 for this o: ({x},{y})")
# w-sequences: does w^{(k)} depend only on i mod something?
w0 = [v//27 for v in b0]
print(f"w0 period: {period(tuple(w0))}, w0[:36]={w0[:36]}")
# C-structure: C=27*(14+k sqrt2); print k values and check k-map
Cs = [recover_C(r, 729) for r in reps]
print(f"fiber0 C's: {Cs}")
print(f"k values (y/27): {[C[1]//27 for C in Cs]}, x/27: {[C[0]//27 for C in Cs]}")
# fiber 1
reps1 = sf729[1][1]
Cs1 = [recover_C(r, 729) for r in reps1]
print(f"fiber1 C's: {Cs1}, divisible by 81: {[C[0]%81==0 and C[1]%81==0 for C in Cs1]}")
for x in range(len(reps1)):
    for y in range(x+1, len(reps1)):
        agree = all(sorted(reps1[x][i] for i in idxs) == sorted(reps1[y][i] for i in idxs) for idxs in fib.values())
        if agree: print(f"colliding pair in fiber1 for this o: ({x},{y})")
