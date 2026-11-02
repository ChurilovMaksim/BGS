"""Independent FFT cross-check of Qnum(z) = D * z^T H^{-1} z at m=12.

H is circulant with first row (6, -1, 0, ..., 0, -1); its eigenvalues are
lam_k = 6 - 2*cos(2*pi*k/12).  Using numpy FFT (complex doubles), compute
H^{-1} z by FFT division and round D * (z . H^{-1} z) to the nearest
integer; compare with the exact sympy-solve values from the main test.
This is a check only -- the reported Qnum values are the exact ones.
"""
import json, numpy as np

m = 12
D = 1536796800
res = json.load(open("/home/hatch/workspace/bgs-breakthrough/methods/oprime_m12_counterexample_result.json"))
lam = np.array([6 - 2*np.cos(2*np.pi*k/m) for k in range(m)])
assert np.all(np.abs(lam) > 1e-9)
ok = True
for z, q_exact in zip(res["tors_z"], res["tors_Q"]):
    zf = np.fft.fft(np.array(z, dtype=float))
    hinv_z = np.fft.ifft(zf / lam).real
    q_fft = D * float(np.dot(np.array(z, dtype=float), hinv_z))
    q_round = int(round(q_fft))
    match = (q_round == q_exact)
    ok &= match
    print(f"z={z} Q_exact={q_exact} Q_fft={q_fft:.3f} rounded={q_round} match={match}")
print("ALL FFT CHECKS MATCH:", ok)
assert ok
