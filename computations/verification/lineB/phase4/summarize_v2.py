"""Summarise the G1/G2-fixed rerun (logs/grid_v2_w*.jsonl) against the original grid (logs/grid_s*.jsonl).
Writes logs/grid_v2_summary.json and prints a table.  Usage: python summarize_v2.py"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json, glob, math
new = {}
for f in sorted(glob.glob('logs/grid_v2_w*.jsonl')):
    for l in open(f):
        d = json.loads(l); new[d['e0']] = d
old = sorted([json.loads(l) for f in glob.glob('logs/grid_s*.jsonl') for l in open(f)], key=lambda d: d['e0'])
old = [d for d in old if d['ok']]
rows = []
for d in old:
    n = new.get(d['e0'])
    rows.append(dict(e0=d['e0'], e1=d['e1'], done=n is not None, ok=bool(n and n['ok']),
                     rho_old=max(d['rho']), rho_new=(max(n['rho']) if n else None),
                     C_new=(sum(n['C']) if n else None), C_old=sum(d['C']),
                     rem=(n['rem'] if n else None), tilted_tail=(n['trunc_tilted'] if n else None),
                     spill=(n['spill'] if n else None)))
done = [r for r in rows if r['done']]; ok = [r for r in done if r['ok']]
cov = all(abs(rows[i]['e1'] - rows[i+1]['e0']) < 1e-9 for i in range(len(rows)-1))
S = dict(intervals=len(rows), rerun_done=len(done), rerun_ok=len(ok),
         coverage=[rows[0]['e0'], rows[-1]['e1']], contiguous=cov,
         rho_new_min=min(r['rho_new'] for r in done) if done else None,
         rho_new_max=max(r['rho_new'] for r in done) if done else None,
         max_abs_rho_change=max(abs(r['rho_new']-r['rho_old']) for r in done) if done else None,
         max_rel_rho_change=max(abs(r['rho_new']-r['rho_old'])/r['rho_old'] for r in done) if done else None,
         C_new_max=max(r['C_new'] for r in done) if done else None,
         rem_max=max(r['rem'] for r in done) if done else None,
         tilted_tail_max=max(r['tilted_tail'] for r in done) if done else None,
         spill_max=max(r['spill'] for r in done) if done else None,
         failures=[(r['e0'], r['e1']) for r in done if not r['ok']])
json.dump(dict(summary=S, rows=rows), open('logs/grid_v2_summary.json', 'w'), indent=1)
for r in rows:
    if r['done']: print(f"{r['e0']:9.4f} {r['e1']:9.4f} ok={r['ok']} rho_old={r['rho_old']:.6f} rho_new={r['rho_new']:.6f} C={r['C_new']:.3g} rem={r['rem']:.2e} tail={r['tilted_tail']:.1e} spill={r['spill']:.1e}")
print(json.dumps(S, indent=1))
