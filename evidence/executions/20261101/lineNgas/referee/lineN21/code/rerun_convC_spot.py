# referee lineN21: re-run the author's Lemma C chain (conv_c.window, unmodified, current dps=160 code) on sampled stored rows; compare r,E
import sys, json, glob, time, random
sys.path.insert(0,'/workspace/bgs-lineN/N21/code')
import conv_c as CC
rows=[json.loads(l) for f in sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_replay_p*.jsonl'))+sorted(glob.glob('/workspace/bgs-lineN/N21/logs/convC_ext_16_60_p*.jsonl')) for l in open(f)]
random.seed(21)
pick=[]
for G in (0,3,15,16,36,44):
    cand=[r for r in rows if r['G']==G and r['kind'] in ('single','pair')]
    pick+=random.sample(cand,min(2,len(cand)))
out=[]
for r in pick:
    t=time.time(); w=CC.window(*r['e'])
    for W,(rr,E,inf) in zip('AB',w):
        st=r[W]; dm=max(abs(rr.real-st['mid'][0]),abs(rr.imag-st['mid'][1])); dE=E-st['rad']
        out.append(dict(k=r['k'],G=r['G'],kind=r['kind'],name=r['name'],h=r['h'],s=r['s'],W=W,dmid=dm,E=E,E_stored=st['rad'],relE=dE/st['rad'],Erel=E/abs(rr)))
        print(out[-1],round(time.time()-t,1),flush=True)
json.dump(out,open('../logs/rerun_convC_spot.json','w'),indent=1)
