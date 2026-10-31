"""N12b certified-in-form k=1 bound [CA-float via N12 stepnorm table + Lip add-on; symmetry N_H(-t)=N_H(t) checked numerically only]:
Gamma_out(theta) <= MU * exp(max cycle mean of log w(c)) on the GxG pseudo-orbit graph of twist pairs (cell c -> every cell meeting F(c)),
w(c) = max_{table points in the t-range of c} N_H + Lip_H/(2NG) (cell add-on).  Cells kept if they meet the complement of the closed box.
usage: c_graph1.py G TH"""
import sys, json, numpy as np
G=int(sys.argv[1]); TH=float(sys.argv[2]); MU=1.9154732
tab=json.load(open('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45_stepnorm_NG4096.json')); NG=tab['NG']; NH=np.array(tab['N_H']); add=tab['cell_add']
full=np.concatenate([NH,NH[-2:0:-1]])   # t=j/NG, j=0..NG-1 via symmetry
assert len(full)==NG
r=NG//G
wcol=np.array([full[np.arange(i*r,(i+1)*r+1)%NG].max() for i in range(G)])+add   # sup over [i/G,(i+1)/G]
lo=np.arange(G)/G; hi=lo+1/G
def dist_int(l,h):  # min torus distance of interval [l,h] to 0
    if l<=0<=h or l<=1<=h: return 0.0
    return min(abs(l),abs(1-h))
dmin=np.array([dist_int(l,h) for l,h in zip(lo,hi)])
keep=~((dmin[:,None]<=TH)&(dmin[None,:]<=TH)&False)   # placeholder
# cell (i,j) meets complement of closed box iff max over cell of max(d0,d1) > TH: max distance in an interval
def dmax_int(l,h):
    xs=[l,h]+([0.5] if l<=0.5<=h else []); return max(min(x%1,1-x%1) for x in xs)
dmx=np.array([dmax_int(l,h) for l,h in zip(lo,hi)])
keep=(dmx[:,None]>TH)|(dmx[None,:]>TH)
I,Jx=np.nonzero(keep); n=len(I); id_=-np.ones((G,G),int); id_[I,Jx]=np.arange(n)
# successors: F(i,j) cell image: first coord = y1 (cell j), second = 6y1-y0 in [6j-i-1, 6j-i+7]/G... exact range of 6y1-y0 over cell
src=[];dst=[]
for k in range(n):
    i,j=I[k],Jx[k]
    a=6*j-(i+1); b=6*(j+1)-i      # (6y1-y0)*G ranges over [a,b]
    for m in range(a,b):
        t=id_[j,m%G]
        if t>=0: src.append(k); dst.append(t)
src=np.array(src); dst=np.array(dst); lw=np.log(wcol[I])
V=np.zeros(n); hist=[]
for it in range(400):
    Vn=np.full(n,-np.inf); np.maximum.at(Vn,src,V[dst]); Vn=Vn+lw  # V(c) = log w(c) + max_{succ} V
    m=Vn.max(); hist.append(m); V=Vn-m
rate=np.exp(np.mean(hist[-50:]))
res=dict(G=G,TH=TH,cells=int(n),edges=int(len(src)),bound=float(MU*rate),max_w=float(wcol.max()),note='Gamma_out <= MU*rate; rigorous modulo table symmetry + IEEE rounding')
print(json.dumps(res)); json.dump(res,open(f'logs/c_graph1_G{G}_th{TH}.json','w'))
