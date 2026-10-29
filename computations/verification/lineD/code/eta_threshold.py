"""From logs/regime1_tables_m*.log: smallest grid eta with max_s |Psi_m(s;K,eta) - B_m^sym| <= tol*2m (tol=1%), per ensemble."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import re, glob
tol = 0.01
for f in sorted(glob.glob('../logs/regime1_tables_m*.log')):
    L = open(f).read().splitlines(); B = float(re.search(r'B_sym=([\d.]+)', L[0]).group(1)); m = int(re.search(r'm=(\d+)', L[0]).group(1))
    res = {}; inf = {}
    for l in L[1:]:
        g = re.match(r'm=\d+ K=(\d+) (J0|G) +eta= *([\d.]+): Psi min= *([-\d.]+) mean= *([-\d.]+) max= *([-\d.]+)', l)
        if g:
            K, ens, eta, mn, mean, mx = int(g[1]), g[2], float(g[3]), float(g[4]), float(g[5]), float(g[6])
            dev = max(abs(mn-B), abs(mx-B)); res.setdefault((K, ens), []).append((eta, dev))
        h = re.match(r'm=\d+ K=(\d+) eta=inf: .*min=([\d.]+) mean=([\d.]+) max=([\d.]+)', l)
        if h: inf[int(h[1])] = (float(h[2]), float(h[4]))
    print(f'm={m} B_sym={B:.6f} 2m={2*m}')
    for (K, ens), v in sorted(res.items()):
        ok = [e for e, d in v if d <= tol*2*m]
        # require all larger grid etas also ok
        th = next((e for e, d in v if all(dd <= tol*2*m for ee, dd in v if ee >= e)), None)
        print(f'  K={K} {ens:2s}: Psi_inf(min,max)={inf.get(K)}  eta_1%={th}   devs: ' + ' '.join(f'{e:g}:{d:.3f}' for e, d in v))
