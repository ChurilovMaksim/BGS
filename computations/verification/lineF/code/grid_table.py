import json, os
rows=["| η | K0, r₂ | \\|μ*\\| certified ∈ | T_V, T_E | μ²/√λ | first odd m with Z>0 | F/2m at m=15 / 21 / 31 | first m with F/2m ≥ 2.5 (all larger m) |","|---|---|---|---|---|---|---|---|"]
for e in ['1.25','1.5','1.75','2','2.25','2.5','2.75','3.0']:
    b=f'../logs/bounds_eta{e if e!="2" else "2"}.json'
    if not os.path.exists(b): rows.append(f'| {e} | — | not finished | | | | | |'); continue
    d=json.load(open(b)); a4=f'../logs/certV_eta{e}_a4_tight.json' if e=='2' else f'../logs/certV_eta{e}_a4.json'
    s=json.load(open(a4)); s4=s['sectors']['4']
    R={r['m']:r for r in d['rows']}
    f=lambda m: ('%.3g'%R[m]['F_over_2m']) if m in R else '—'
    first=next((r['m'] for r in d['rows'] if r['F_over_2m']>=2.5),None)
    rows.append(f"| {e} | {s['K0']}, {float(d['r2'].split()[0].strip('[')):.2f} | [{s4['mu_abs_lower']:.6f}, {s4['mu_abs_upper']:.6f}] | {d['T_V']:.1f}, {d['T_E']:.2f} | {(d['mu_lo']**2/(3+2*2**.5)**.5):.4f} | {d['m0']} | {f(15)} / {f(21)} / {f(31)} | {first} |")
print('\n'.join(rows))
