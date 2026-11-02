"""Wave 27, task 1: test the single-C identity t1*(1 - c/t2) == 0 for
collapsed unit C at (108,3), and its digit form.
C collapsed unit: C mod 3 = (c,0), c in {1,2}.
t1 = T1' mod 3, T1 = Tr(C*u) mod 27, u = (3,1) mod 27.
t2 = T2 mod 3, T2 = Tr(C*u^2) mod 9.
Also record (c, t1, t2) distribution and the y1 + c*a0 form.
"""
from collections import Counter

def tr_mod(x, m):
    return (2*x[0]) % m

dist = Counter()
viol = []
n_coll_unit = 0
for X in range(81):
    for Y in range(81):
        if Y % 3 != 0:
            continue
        c = X % 3
        if c == 0:
            continue  # divisible C: induction case, skip here
        n_coll_unit += 1
        Cx, Cy = X % 27, Y % 27
        T1 = (2*(3*Cx + 2*Cy)) % 27
        assert T1 % 3 == 0
        t1 = (T1//3) % 3
        X9, Y9 = X % 9, Y % 9
        T2 = (2*(2*X9 + 12*Y9)) % 9
        t2 = T2 % 3
        dist[(c, t1, t2)] += 1
        if t2 == 0:
            continue  # degenerate: no vertex; handled separately
        # check t1*(1 - c/t2) == 0 mod 3
        if (t1 * (1 - c*pow(t2, -1, 3))) % 3 != 0:
            viol.append((X, Y, c, t1, t2))
print("collapsed unit C count:", n_coll_unit)
print("(c, t1, t2) distribution:", dict(sorted(dist.items())))
print("violations of t1*(1-c/t2)==0:", len(viol), viol[:10])
