import sys, json
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon

m, q2, qred, half = 128, 131072, 32768, 64
pts = snf_kernel_i32(m, q2)
red = (pts % qred)[:, :half]
# periodicity check on all points
per = np.all((pts % qred)[:, half:] == red)
print("periodicity mod qred for all points:", per)
# image size: distinct reduced sequences
_, inv = np.unique(red, axis=0, return_inverse=True)
print("image size:", inv.max() + 1, " kernel size:", len(pts),
      " implied |ker rho|:", len(pts) // (inv.max() + 1))
# reduced orbits
rba, rbb = orbit_canon(red[:, :2].astype(np.int64), half, qred)
rgam = group_ids(np.stack([rba, rbb], axis=1))
print("distinct reduced orbits in image:", rgam.max() + 1)
# which m=64 split fibers' orbits appear in the image?
d64 = json.load(open("wave36_2part_m64.json"))
img_canons = {(int(rba[i]), int(rbb[i])) for i in range(len(pts))}
for fi, f in enumerate(d64["fibers"]):
    own = {tuple(c) for c in f["own_orbit_canons"]}
    print(f"m64 fiber {fi} size={f['size']} orbits={f['n_orbits']} "
          f"orbits_in_image={len(own & img_canons)}/{len(own)}")
