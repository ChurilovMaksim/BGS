"""Shape-space (SL2(Z)\\SL2(R)) view: each unit nu -> lattice Lambda_nu=(2h)^-1/2 {(a,b): b nu≡a mod 2h}; coords tau=w/v in F, phi=arg v mod pi.
Reports (1) unweighted counts vs Haar (3/pi dx dy/y^2 dphi/pi), (2) weighted local mean x=|Z|^2/RMT per cell (nonres)."""
import sys, numpy as np, json
from base import get
out={}
for spec in sys.argv[1:]:
    k,m=spec.split(':'); m=int(m); D=get(k,m); Z=D['Z']; RMT=float(D['RMT']); nr=~D['res']&~D['dil']; phi=len(Z); h=int(D['h'])
    v=D['a']+1j*D['b']; w=D['a2']+1j*D['b2']; tau=w/v; s=np.imag(tau)<0; tau=np.where(s,-tau,tau)
    X=np.real(tau); Y=np.imag(tau); ph=np.mod(np.angle(v),np.pi); x=Z/RMT
    ybins=[np.sqrt(3)/2,1.0,1.5,3,10,1e9]; xb=np.linspace(-.5,.5,5); pb=np.linspace(0,np.pi,13)
    # Haar mass of cell (x in [x0,x1], y in [y0,y1]) ∩ F, times dphi/pi; integrate dx dy/y^2 numerically over F
    def haar(x0,x1,y0,y1,p0,p1):
        xs=np.linspace(x0,x1,201); xm=(xs[1:]+xs[:-1])/2; dx=xs[1]-xs[0]
        ylo=np.maximum(y0,np.sqrt(np.maximum(1-xm**2,0))); val=np.where(ylo<y1,1/ylo-1/y1,0)
        return 3/np.pi*np.sum(val)*dx*(p1-p0)/np.pi
    rows=[]; cnt_dev=[]; print(f'== {k} m={m}: cells (y-band, x-quarter, phi/15deg): count/expected and weighted mean x')
    for i in range(len(ybins)-1):
        line=f'  y[{ybins[i]:.2f},{ybins[i+1]:.0f}):'
        for j in range(len(xb)-1):
            for l in range(len(pb)-1):
                c=(Y>=ybins[i])&(Y<ybins[i+1])&(X>=xb[j])&(X<xb[j+1])&(ph>=pb[l])&(ph<pb[l+1])
                e=haar(xb[j],xb[j+1],ybins[i],ybins[i+1],pb[l],pb[l+1])*phi
                cn=c.sum(); cnt_dev.append((cn-e)/np.sqrt(max(e,1)))
                rows.append(dict(i=i,j=j,l=l,n=int(cn),exp=float(e),x=float(x[c&nr].mean()) if (c&nr).sum() else None))
        xs_=[r['x'] for r in rows if r['i']==i and r['x'] is not None]; ns_=[r['n'] for r in rows if r['i']==i]
        print(line+f' n={sum(ns_):8d} cells x: min={min(xs_):.3f} max={max(xs_):.3f} sd={np.std(xs_):.3f}')
    print(f'  unweighted count z-scores vs Haar: rms={np.sqrt(np.mean(np.square(cnt_dev))):.2f} max={np.max(np.abs(cnt_dev)):.1f} (y<3 cells only meaningful)')
    # phi-profile in band y in [1.5,3) and [3,10): average over x
    for i in (2,3):
        prof=[]
        for l in range(len(pb)-1):
            c=nr&(Y>=ybins[i])&(Y<ybins[i+1])&(ph>=pb[l])&(ph<pb[l+1]); prof.append(x[c].mean())
        print(f'  phi-profile y[{ybins[i]},{ybins[i+1]}) (15deg bins from 0): '+' '.join(f'{p:.3f}' for p in prof))
    out[spec]=rows
json.dump(out,open('../logs/shape.json','w'))
