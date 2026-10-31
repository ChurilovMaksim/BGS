"""N15: cross-check c3_mid boxes (F14.1-fixed radii) against the partial N13 arb replay: every window must intersect; also tight-window
ratio |mid_arb - mid_c3| / rad_c3 (referee's check, there 2.2e-6 vs c2 radii)."""
import json
arb={json.loads(l)['k']:json.loads(l) for l in open('/workspace/bgs-lineN/N13/logs/c_replay.jsonl')}
c3={json.loads(l)['k']:json.loads(l) for l in open('/workspace/bgs-lineN/N15/logs/c3_mid.jsonl')}
bad=0;n=0;mx=0;tight=0
for k,a in arb.items():
    m=c3[k]; assert m['e']==a['e']
    for W in 'AB':
        n+=1
        for c in ('re','im'):
            if max(a[W][c][0],m[W][c][0])>min(a[W][c][1],m[W][c][1]): bad+=1
        if a[W]['rad']<m[W]['rad']:
            tight+=1
            ma=complex(sum(a[W]['re'])/2,sum(a[W]['im'])/2); mm=complex(sum(m[W]['re'])/2,sum(m[W]['im'])/2)
            mx=max(mx,abs(ma-mm)/m[W]['rad'])
out=dict(windows=n,disjoint_components=bad,arb_tighter_windows=tight,max_middiff_over_rad_c3=mx)
print(out); json.dump(out,open('/workspace/bgs-lineN/N15/logs/c3_vs_arb.json','w'),indent=1)
