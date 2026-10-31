import subprocess, resource, time, os
L=os.path.expanduser('~/.elan/toolchains/leanprover--lean4---v4.33.1/bin/lean')
f='K3Gaps_1547.lean'; t=time.time()
p=subprocess.run(['nice','-n','10',L,f],capture_output=True,text=True)
ru=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
open('log_K3Gaps_1547.txt','w').write(p.stdout+p.stderr)
open('summary.txt','a').write('RERUN (alone, after the sequential pass was OOM-killed under concurrent load) %s exit=%d sec=%.0f maxrss_MB=%d\n'%(f,p.returncode,time.time()-t,ru//1024))
