"""Referee lineN15: empirical check of the libm <=1 ulp assumption for the exact numpy call used in c3_mid (np.exp(2j*np.pi*NS*d))
and of the phase-argument rounding bound |fl(arg)-arg| <= 4u|arg| (vs exact 2*pi*n*d in mpmath), |n|<=30, |d|<=1/2."""
import numpy as np, mpmath as mp, json
mp.mp.dps=40; rng=np.random.default_rng(1); u=2.0**-53
N=60000; n=rng.integers(-30,31,N).astype(float); d=rng.uniform(-0.5,0.5,N)
z=np.exp(2j*np.pi*n*d); argf=(2j*np.pi*n*d).imag
mx_ulp=0; mx_arg=0; mx_tot=0
for i in range(N):
    th=mp.mpf(float(argf[i])); c=mp.cos(th); s=mp.sin(th)
    for got,ex in ((z[i].real,c),(z[i].imag,s)):
        if ex!=0:
            ulp=float(np.spacing(abs(float(ex)))); mx_ulp=max(mx_ulp,float(abs(mp.mpf(float(got))-ex))/ulp)
    thx=2*mp.pi*mp.mpf(float(n[i]))*mp.mpf(float(d[i]))
    if thx!=0: mx_arg=max(mx_arg,float(abs(th-thx)/(u*abs(thx))))
    ex=mp.expj(thx); mx_tot=max(mx_tot,float(abs(mp.mpc(complex(z[i]))-ex))/u)
out=dict(samples=N,max_ulp_cos_sin=mx_ulp,max_arg_err_over_u_absarg=mx_arg,max_total_abs_err_over_u=mx_tot,
         bound_used_eps_c_over_u=(4*2*np.pi*30*0.5+16), np_version=np.__version__)
print(out); json.dump(out,open('logs/ref_ulp.json','w'),indent=1)
