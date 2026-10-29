if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from d4_d6 import *
dat, W, B = setup(6); D = dat['D']
for s in units_lifts(dat)[::16]:
    ph, Ws = supp_data(dat, s, W, B)
    print(f"m=6 K=1 s={s} (mod g' {s % dat['gp']}): Psi_inf={psi_inf(ph, Ws, D, [1]):.6f}   K={{1,2}}: {psi_inf(ph, Ws, D, [1,2]):.6f}", flush=True)
