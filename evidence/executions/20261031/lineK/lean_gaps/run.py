import subprocess, resource, time, glob, re, sys, os
L=os.path.expanduser('~/.elan/toolchains/leanprover--lean4---v4.33.1/bin/lean')
fs=sorted(glob.glob('K3Gaps_*.lean'), key=lambda f:int(re.findall(r'\d+',f)[-1]))
fs=['K3Finite.lean']+fs
out=open('summary.txt','w')
for f in fs:
    t=time.time()
    p=subprocess.run(['nice','-n','10',L,f],capture_output=True,text=True)
    ru=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    open('log_'+f[:-5]+'.txt','w').write(p.stdout+p.stderr)
    out.write('%s exit=%d sec=%.0f maxrss_children_so_far_MB=%d\n'%(f,p.returncode,time.time()-t,ru//1024)); out.flush()
out.write('DONE\n')
