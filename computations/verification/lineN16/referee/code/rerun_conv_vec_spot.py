"""lineN16: re-run the authors' conv_vec.window on a deterministic sample of replay rows; compare r and E with conv_vec_replay.jsonl.
Writes only to /workspace/audit/lineN16/logs."""
import sys, json, time
sys.argv=['conv_vec.py','test_import_only']
sys.path.insert(0,'/workspace/bgs-lineN/N16/code')
src=open('/workspace/bgs-lineN/N16/code/conv_vec.py').read().split("if __name__=='__main__':")[0]
g={'__name__':'cv'}; exec(compile(src,'conv_vec.py','exec'),g)
rep=[json.loads(l) for l in open('/workspace/bgs-lineN/N16/logs/conv_vec_replay.jsonl')]
idx=[0,1,5,9,10,57,300,777,1001,1350,1400,1559]
out=[]; t0=time.time()
for i in idx:
    rw=rep[i]; res=g['window'](*rw['e'])
    for W,(r,E,inf) in zip('AB',res):
        x=rw[W]; rr=complex(sum(x['re'])/2,sum(x['im'])/2)
        out.append(dict(i=i,kind=rw['kind'],G=rw['G'],W=W,dr=abs(r-rr),E=E,E_log=x['rad'],relE=abs(E-x['rad'])/x['rad']))
    print(i,round(time.time()-t0,1),out[-1],flush=True)
json.dump(dict(rows=out,max_relE=max(o['relE'] for o in out),max_dr=max(o['dr'] for o in out)),open('/workspace/audit/lineN16/logs/rerun_conv_vec_spot.json','w'),indent=1)
print('max_relE',max(o['relE'] for o in out),'max_dr',max(o['dr'] for o in out))
