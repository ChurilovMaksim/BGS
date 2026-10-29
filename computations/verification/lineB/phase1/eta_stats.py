"""Distribution of the N-averaged fixed-kick form factor F_m(eta) over eta in [100,1000] (deterministic grid),
relative to the Bohr mean B_m; and 4th-moment ratio of Z_m(nu) (complex Gaussian: 2)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import dlib, numpy as np
B={5:9.399762,6:11.118367,7:13.795609,8:15.298683}
for m in [5,6,7,8]:
    O=dlib.Orbits(m); xs=np.linspace(100,1000,301); Fs=[];M4=[]
    for x in xs:
        F,Z=O.F(x); u=O.units(); Fs.append(F); M4.append(np.mean(np.abs(Z[u])**4)/F**2)
    Fs=np.array(Fs); M4=np.array(M4)
    print(f'm={m} B_m={B[m]} mean_F={Fs.mean():.3f} std_F/B={Fs.std()/B[m]:.3f} min/B={Fs.min()/B[m]:.3f} max/B={Fs.max()/B[m]:.3f} '
          f'frac(|F/B-1|>0.25)={np.mean(np.abs(Fs/B[m]-1)>0.25):.3f}  median M4={np.median(M4):.3f}',flush=True)
