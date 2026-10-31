"""[N] prime level q || h: |W_{q,beta}| <= 2/q^2 if N(beta) != 0 mod q, = n_q/q^2 if N(beta) = 0 (isotropic); m=15, q=41 (and q=31, q^2|h)."""
import numpy as np, json, sys
exec(open("code/inherit7q.py").read().split("res={}")[0])
out={}
for m,a,q,prop in ((15,2,41,[1]),(15,2,31,[1])):
    g=np.arange(q); GX,GY=np.meshgrid(g,g,indexing='ij'); N=(GX*GX-2*GY*GY)%q
    ts=members(m,a,q,prop); mx_non=0; iso=[]
    G0={t:np.exp(-2j*np.pi*((t*N)%q)/q).sum() for t in ts}
    for bx in range(q):
        for by in range(q):
            if bx==0 and by==0: continue
            W=sum(np.conj(G0[t])*np.exp(-2j*np.pi*((t*N+2*(bx*GX+2*by*GY))%q)/q).sum() for t in ts)/q**4
            if (bx*bx-2*by*by)%q: mx_non=max(mx_non,abs(W)*q*q)
            else: iso.append(abs(W)*q*q)
    out[f'{m},{a},{q}']=dict(n_members=len(ts),max_q2W_noniso=float(mx_non),q2W_iso=[float(min(iso)),float(max(iso))],n_iso=len(iso))
    print(out[f'{m},{a},{q}'],flush=True)
json.dump(out,open('logs/primelevel_W.json','w'),indent=1)
