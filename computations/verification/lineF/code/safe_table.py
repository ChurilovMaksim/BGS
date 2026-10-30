"""Line F: print every certified quantity in the safe direction (integration fix, referee report F.6.1):
lower bounds rounded DOWN, upper bounds rounded UP, enclosures outward. Reads logs/bounds_eta*.json and cert JSONs.
Usage: python3 safe_table.py  (from this directory) > ../logs/safe_table.md"""
import json, math, os
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
L='../logs/'
def r(x, digits, up, sig=True):
    d=Decimal(repr(float(x)))
    if sig:
        e=d.adjusted()-digits+1
        q=Decimal(1).scaleb(e)
    else:
        q=Decimal(1).scaleb(-digits)
    v=d.quantize(q, rounding=ROUND_CEILING if up else ROUND_FLOOR)
    if sig and abs(v)>=Decimal('1e5'):
        m,ex=('%.*e'%(digits-1,float(v))).split('e')
        # re-round mantissa in the same direction (float formatting is nearest)
        mm=Decimal(m); exv=int(ex)
        val=mm.scaleb(exv)
        if (not up and val>d) or (up and val<d):
            mm=mm-(Decimal(1).scaleb(-(digits-1))) if not up else mm+(Decimal(1).scaleb(-(digits-1)))
        return f"{mm}e{exv}"
    return format(v,'f')
lo=lambda x,dg=3: r(x,dg,False); hi=lambda x,dg=3: r(x,dg,True)
out=[]
out.append('## Safe-direction table (lower bounds floored, upper bounds ceiled, enclosures outward)\n')
out.append('| η | K0, r₂ | \\|μ*\\| ∈ (outward, 6 dp) | T_V ≤, T_E ≤ | μ_lo²/√λ ≥ | first odd m with Z>0 | F/2m ≥ at m=15 / 21 / 31 | W̃rest/m ≥ at m=15 / 21 / 31 | first odd m with W̃rest/m > 1 (and all larger) | closed form F/2m ≥ C·g^m/m: m ≥, C ≥, g ≥ |')
out.append('|---|---|---|---|---|---|---|---|---|---|')
for e in ['1.25','1.5','1.75','2','2.25','2.5']:
    d=json.load(open(L+f'bounds_eta{e}.json'))
    s=json.load(open(L+(f'certV_eta2_a4_tight.json' if e=='2' else f'certV_eta{e}_a4.json')))
    s4=s['sectors']['4']; R={x['m']:x for x in d['rows']}
    F=lambda m: lo(R[m]['F_over_2m'],4) if m in R else '—'
    W=lambda m: (lo(R[m]['Wrest_over_m'],4) if R[m]['Wrest_over_m']>0 else 'none') if m in R else '—'
    first=next(x['m'] for x in d['rows'] if x['Wrest_over_m']>1)
    g=d['mu_lo']**2/(3+2*2**.5)**.5
    cf=d['closed_form']
    out.append(f"| {e} | {s['K0']}, {float(d['r2'].split()[0].strip('[')):g} | [{r(s4['mu_abs_lower'],6,False,False)}, {r(s4['mu_abs_upper'],6,True,False)}] | {r(d['T_V'],2,True,False)}, {r(d['T_E'],2,True,False)} | {r(cf['g_lower'],4,False,False)} | {d['m0']} | {F(15)} / {F(21)} / {F(31)} | {W(15)} / {W(21)} / {W(31)} | {first} | {cf['m_from']}, {r(cf['C_lower'],3,False)}, {r(cf['g_lower'],4,False,False)} |")
d=json.load(open(L+'bounds_eta2.json')); s=json.load(open(L+'certV_eta2_a4_tight.json'))['sectors']['4']
R={x['m']:x for x in d['rows']}
out.append('\n## η = 2 (k1, full alphabet): |μ*| ∈ [%s, %s] (7 dp, outward); T_V ≤ %s, T_E ≤ %s, 4(T_V+T_E) ≤ %s\n'%(
    r(s['mu_abs_lower'],7,False,False), r(s['mu_abs_upper'],7,True,False), r(d['T_V'],2,True,False), r(d['T_E'],2,True,False), r(4*(d['T_V']+d['T_E']),2,True,False)))
ms=[13,15,17,19,21,25,31,41,61,101]
out.append('| m | '+' | '.join(map(str,ms))+' |'); out.append('|---'*(len(ms)+1)+'|')
out.append('| F_m/2m ≥ | '+' | '.join(lo(R[m]['F_over_2m']) for m in ms)+' |')
out.append('| W̃rest_m/m ≥ | '+' | '.join(lo(R[m]['Wrest_over_m']) for m in ms)+' |')
print('\n'.join(out))
