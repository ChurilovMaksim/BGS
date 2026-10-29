"""Markdown table of max_s |c_1| (G ensemble, a_k=1) from logs/c1_tables.out."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import re
d = {}
for l in open('../logs/c1_tables.out'):
    g = re.match(r'm=(\d+) K=(\d+) G eta= *([\d.]+):.*max\|c1\|= *([\d.]+)', l)
    if g: d[(int(g[1]), int(g[2]), float(g[3]))] = float(g[4])
etas = [1, 2, 4, 8, 16, 32, 64]
print('| m | K | ' + ' | '.join(f'η={e}' for e in etas) + ' | −2m² |'); print('|---|---|' + '---|'*len(etas) + '---|')
for m in sorted({k[0] for k in d}):
    for K in sorted({k[1] for k in d if k[0] == m}):
        print(f'| {m} | {K} | ' + ' | '.join((f'{d[(m,K,e)]:.3g}' if (m,K,e) in d else '–') for e in etas) + f' | {-2*m*m} |')
