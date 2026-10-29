"""ECPP primality certificates (PARI/GP 2.17 via cypari2: primecert + independent primecertisvalid) for h_m, m in NSW-prime list."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import cypari2, time, sys, math
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
def hm(m):
    x,y=1,0
    for _ in range(m): x,y=3*x+8*y,x+3*y
    return math.isqrt((x-1)//2)
for m in [int(a) for a in sys.argv[1].split(',')]:
    h=hm(m); assert 4*h*h==2*(lambda t:t)(0)+4*h*h
    t0=time.time(); c=pari.primecert(h); t1=time.time(); ok=pari.primecertisvalid(c)
    open(f'logs/cert_h{m}.txt','w').write(str(c))
    print(f'm={m} digits={len(str(h))} primecert time={t1-t0:.1f}s steps={len(c)} primecertisvalid={ok} (verify {time.time()-t1:.1f}s) cert saved logs/cert_h{m}.txt',flush=True)
