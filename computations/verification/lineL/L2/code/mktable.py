import json,math
rows={}
for l in open('/workspace/bgs-lineL/L2/logs/iso_survey.jsonl'):
    r=json.loads(l); rows[(r.get('res','(2,8)'),r['m'],r['q'])]=r
print('| res | m | q | log q / m | r | \\|Z\\|/q | 1.28359^m | \\|D_𝔮\\| | \\|D_𝔮\\|^{1/m} | msq^{1/2m} | max\\|Ẑ\\|^{1/m} | phase-blind D/(G^m/q) |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for k in sorted(rows,key=lambda k:(k[1],k[2],k[0])):
    r=rows[k]; a=r['lines']['1']; m=r['m']; q=r['q']
    print(f"| {k[0]} | {m} | {q} | {math.log(q)/m:.3f} | {a['r']} | {r['absZ']/q:.3g} | {r['target8_m']:.3g} | {a['absD']:.3g} | {a['absD']**(1/m):.4f} | {a['meansq']**(1/(2*m)):.4f} | {max(a['maxZ'],r['lines']['-1']['maxZ'])**(1/m):.4f} | {a['Dpb']/a['G_m_over_q']:.1e} |")
