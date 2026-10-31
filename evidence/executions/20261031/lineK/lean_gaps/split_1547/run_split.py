import subprocess, resource, time, os, glob
L=os.path.expanduser('~/.elan/toolchains/leanprover--lean4---v4.33.1/bin/lean')
out=open('summary.txt','w')
for f in sorted(glob.glob('K3Gaps_split_*.lean')):
    t=time.time(); p=subprocess.run(['nice','-n','10',L,f],capture_output=True,text=True)
    ru=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    open('log_'+f[:-5]+'.txt','w').write(p.stdout+p.stderr)
    out.write('%s exit=%d sec=%.0f maxrss_children_so_far_MB=%d\n'%(f,p.returncode,time.time()-t,ru//1024)); out.flush()
out.write('DONE\n')
