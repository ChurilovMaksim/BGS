"""Line B primality verifier (TRACE-168).  For the eleven NSW-prime m of Theorem N:
  * recompute h_m = sqrt(Tr S^m - 2)/2 from S = [[3,4],[2,3]] with exact integers;
  * m in {59,163,257,421,937,947,1493}: load the PARI ECPP certificate cert_h<m>.txt (this directory),
    check that it certifies exactly h_m, and validate it with PARI primecertisvalid;
  * m in {7,19,29,47}: prove primality with PARI isprime(h, 2) (APRCL, deterministic).
Exit code 0 iff everything passes.  Requires cypari2 (PARI/GP >= 2.15).
Usage: python verify_ecpp.py"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import os, sys, ast
from math import isqrt
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
HERE = os.path.dirname(os.path.abspath(__file__))
def hm(m):
    a, b, c, d = 1, 0, 0, 1
    for _ in range(m): a, b, c, d = 3*a + 2*b, 4*a + 3*b, 3*c + 2*d, 4*c + 3*d
    D = a + d - 2; r = isqrt(D); assert r*r == D and r % 2 == 0
    return r // 2
ok_all = True
for m in [7, 19, 29, 47]:
    h = hm(m); ok = bool(pari.isprime(h, 2))
    ok_all &= ok; print(f"m={m} h={h} digits={len(str(h))} APRCL_isprime={ok}")
for m in [59, 163, 257, 421, 937, 947, 1493]:
    h = hm(m)
    cert = ast.literal_eval(open(os.path.join(HERE, f"cert_h{m}.txt")).read().strip())
    same = int(cert[0][0]) == h
    valid = int(pari.primecertisvalid(pari(str(cert)))) == 1
    ok_all &= same and valid
    print(f"m={m} digits={len(str(h))} cert_N_equals_h={same} primecertisvalid={valid} steps={len(cert)}")
# controls: a tampered certificate and a certificate for h+2 must be rejected
c = ast.literal_eval(open(os.path.join(HERE, "cert_h163.txt")).read().strip())
c[0][2] = int(c[0][2]) + 1
ctl1 = int(pari.primecertisvalid(pari(str(c)))) == 0
ctl2 = int(hm(59) + 2) != int(ast.literal_eval(open(os.path.join(HERE, "cert_h59.txt")).read().strip())[0][0])
print(f"CONTROL tampered cert rejected={ctl1}; CONTROL h+2 mismatch detected={ctl2}")
ok_all &= ctl1 and ctl2
print("PASS" if ok_all else "FAIL"); sys.exit(0 if ok_all else 1)
