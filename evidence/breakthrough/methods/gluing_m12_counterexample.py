"""Lift the mod-81 aff-bad fiber of Fix_12 to a GLOBAL counterexample to O*
(separation reading) at m=12, by putting all other prime-power components = 0.
CRT embedding phi: Z/81 -> Z/D, phi(t) = t*M*inv(M mod 81) mod D, M = D/81,
so phi(t) = t (mod 81) and 0 (mod M). If v, v' in Fix mod 81 have the same
sorted multiset but different affine canons, then y = phi(v), y' = phi(v')
are in Fix mod D, have the same sorted multiset (phi is injective), and are
not globally affine-equivalent (a global affine perm would reduce mod 81
to an affine perm of v to v', contradicting distinct canons).
"""
import sys, math
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod, aff_perms, canon
from collections import defaultdict

m = 12
D = 1536796800
q = 81
M = D // q
inv = pow(M % q, -1, q)
def phi(t):
    return (t * M * inv) % D

vecs = fix_mod(m, q)
perms = aff_perms(m)
by = defaultdict(list)
for v in vecs:
    by[tuple(sorted(v))].append(v)

# pick the unique aff-bad sorted class, and two vectors with different canons
target = None
for s, vs in by.items():
    cs = {canon(v, perms, m) for v in vs}
    if len(cs) > 1:
        target = (s, vs); break
assert target is not None
s, vs = target
v1 = vs[0]
v2 = next(v for v in vs if canon(v, perms, m) != canon(v1, perms, m))
print("sorted mod81:", s)
print("v1:", v1, "canon:", canon(v1, perms, m))
print("v2:", v2, "canon:", canon(v2, perms, m))

y  = tuple(phi(t) for t in v1)
y2 = tuple(phi(t) for t in v2)
print("y :", y)
print("y':", y2)

def check_H(vec):
    # (H vec)_i = 6 vec_i - vec_{i-1} - vec_{i+1} mod D
    return all((6*vec[i] - vec[(i-1) % m] - vec[(i+1) % m]) % D == 0 for i in range(m))
def check_mod81(vec):
    return tuple(x % q for x in vec)

print("H y  = 0 mod D:", check_H(y))
print("H y' = 0 mod D:", check_H(y2))
print("y mod 81 =", check_mod81(y), " == v1:", check_mod81(y) == v1)
print("y' mod 81 =", check_mod81(y2), " == v2:", check_mod81(y2) == v2)
print("sorted(y) == sorted(y'):", tuple(sorted(y)) == tuple(sorted(y2)))
print("global canon y :", canon(y, perms, m))
print("global canon y':", canon(y2, perms, m))
print("global canons distinct:", canon(y, perms, m) != canon(y2, perms, m))
# also: no global affine perm sends y to y' (canon test is exactly this)
print("y == y':", y == y2)
