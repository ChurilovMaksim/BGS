"""B1 second-reader driver: runs the referee's independent directed-rounding certifier (audit/derand23/code/t9_cert.py,
unmodified) on all 93 phase-4 intervals with EXACT float endpoints (shared between neighbours, so the closed intervals
cover [1, 81.57406988332305] with no gaps).  Parameter map (referee normalisation, as in REPORT.md 8.11):
beta=0.1/(4 sqrt2), kappa=beta/2, R1=Kmid*4 sqrt2 with Kmid=min(20,8+round(e1/4)), x2=min(50,25+round(e1/2)).
Resumable: one result file per interval out/iv_XXX.jsonl (written atomically, mirrored to /home/box/derand_backup).
Usage: runner.py <worker-name> <mode: light|heavy|any> [Rsplit]"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, os, json, math, time, socket, shutil, resource
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','independent_replay','code'))
import t9_cert as T
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(HERE,'..','logs','b1','out'); CL=os.path.join(HERE,'..','logs','b1','claims'); os.makedirs(CL,exist_ok=True)
MIR=os.environ.get('B1_MIRROR',OUT)   # box run mirrored to /home/box/derand_backup/b1_full_mirror/out
iv=json.load(open(os.path.join(HERE,'b1_intervals.json')))
name,mode=sys.argv[1],sys.argv[2]; Rsplit=float(sys.argv[3]) if len(sys.argv)>3 else 1000.0
B=0.1/(4*math.sqrt(2)); K=B/2
def params(e1):
    Kmid=min(20,8+round(e1/4)); x2=min(50,25+round(e1/2)); R1=Kmid*4*math.sqrt(2)
    return R1,x2,T.LAM*(R1+T.CC*x2)*(1+1e-12)+1.0
def done(i):
    for d in (OUT,MIR):
        f=os.path.join(d,f'iv_{i:03d}.jsonl')
        if os.path.exists(f):
            try:
                L=[json.loads(l) for l in open(f)]
                if L and L[-1].get('summary'): 
                    if d==MIR and not os.path.exists(os.path.join(OUT,f'iv_{i:03d}.jsonl')): shutil.copy(f,OUT)
                    return True
            except Exception: pass
    return False
def claim(i):
    c=os.path.join(CL,f'{i:03d}')
    try: os.mkdir(c)
    except FileExistsError:
        try: pid=int(open(os.path.join(c,'pid')).read())
        except Exception: return False
        try: os.kill(pid,0); return False          # owner alive
        except ProcessLookupError: pass
        except PermissionError: return False
        shutil.rmtree(c,ignore_errors=True)
        try: os.mkdir(c)
        except FileExistsError: return False
    open(os.path.join(c,'pid'),'w').write(str(os.getpid())); return True
order=list(range(93))
if mode=='heavy': order=[i for i in reversed(order) if params(iv[i][1])[2]>=Rsplit]
elif mode=='light': order=[i for i in order if params(iv[i][1])[2]<Rsplit]
print(f'[{name}] start pid={os.getpid()} mode={mode} Rsplit={Rsplit} queue={len(order)}',flush=True)
for i in order:
    if done(i) or not claim(i): continue
    e0,e1=iv[i]; R1,x2,R=params(e1)
    need=4.5 if R>=1200 else 2.5      # GB: do not start a run unless this much is available (shared box)
    while True:
        avail=int([l for l in open('/proc/meminfo') if l.startswith('MemAvailable')][0].split()[1])/2**20
        if avail>=need: break
        print(f'[{name}] waiting for memory: {avail:.1f} GB available < {need} GB',flush=True); time.sleep(60)
    t=time.time()
    print(f'[{name}] {time.strftime("%H:%M:%S")} iv {i} [{e0},{e1}] R1={R1:.4f} x2={x2} R={R:.2f}',flush=True)
    res=T.run(e0,e1,B,K,R1,x2)
    rho=max(r['rho'] for r in res); C=sum(r['C'] for r in res); valid=all(r['valid'] for r in res) and rho<1
    summ=dict(summary=True,idx=i,e0=e0,e1=e1,beta=B,kappa=K,R1=R1,x2=x2,valid=valid,rho=rho,C=C,secs=round(time.time()-t),
              maxrss_GB=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20,2),worker=name,
              finished=time.strftime('%Y-%m-%dT%H:%M:%S%z'))
    tmp=os.path.join(OUT,f'.iv_{i:03d}.tmp')
    with open(tmp,'w') as f:
        for r in res: f.write(json.dumps(dict(idx=i,**r))+'\n')
        f.write(json.dumps(summ)+'\n')
    os.replace(tmp,os.path.join(OUT,f'iv_{i:03d}.jsonl'))
    try: shutil.copy(os.path.join(OUT,f'iv_{i:03d}.jsonl'),MIR)
    except Exception as ex: print('mirror fail',ex,flush=True)
    print(f'[{name}] RESULT iv {i} valid={valid} rho={rho:.7f} C={C:.3e} secs={summ["secs"]} rss={summ["maxrss_GB"]}GB',flush=True)
print(f'[{name}] DONE',flush=True)
