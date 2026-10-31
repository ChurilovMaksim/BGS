import json,math
for f in ['logs/iso_survey.jsonl','logs/iso_trunc_21_239_L10K40.json']:
  try:
    for l in open('/workspace/bgs-lineL/L2/'+f):
      r=json.loads(l); a=r['lines']['1']; b=r['lines']['-1']; m=r['m']; q=r['q']
      print(f[5:9],m,q,'r',a['r'],'|Z|/q %.3g'%(r['absZ']/q),'t8^m %.3g'%r['target8_m'],'|D| %.4g %.4g'%(a['absD'],b['absD']),
        'D^(1/m) %.4f'%(a['absD']**(1/m)),'msq %.3g'%a['meansq'],'msq^(1/2m) %.4f'%(a['meansq']**(1/(2*m))),'max^(1/m) %.4f'%(max(a['maxZ'],b['maxZ'])**(1/m)),'Dpb %.2g'%a['Dpb'],'sec',r['sec'])
  except FileNotFoundError: pass
