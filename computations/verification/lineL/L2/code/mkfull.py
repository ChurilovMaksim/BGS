import json
print('| res | m | q | \\|Z\\| | 1.28359^m | \\|D_iso\\| | max_t\\|E_b\\|/q | max_t\\|D_iso − E_b/q\\| | rate^{1/m} | max non-iso \\|Ẑ\\|^{1/m} | Σ_c\\|A(c)\\|² − \\|Z\\|²/q² |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for l in open('/workspace/bgs-lineL/L2/logs/full_level.jsonl'):
    r=json.loads(l); q=r['q']
    print(f"| {r['res']} | {r['m']} | {q} | {r['absZ']:.3g} | {r['target8_m']:.3g} | {r['absDiso']:.3g} | {r['max_absEb_over_q']:.3g} | {r['max_comb']:.3g} | {r['comb_rate']:.4f} | {r['max_noniso_rate']:.4f} | {(format(r['l2_level']-r['absZ']**2/q**2,'.4g') if r['absZ']**2/q**2<1e13 else '— (fp)')} |")
