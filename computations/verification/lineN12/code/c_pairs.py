"""N12 (1b) [CA*-float / N]: per-window two-bump interaction on the Line F sector-4 operator (p-independent window weights).
For seed e in Z[sqrt2] (k-even convention of n9_cert): zeta_A = e sqrt2/8, zeta_B = -e eps^{-1} sqrt2/8, window twists
d_j = red(e1 lam^j) (j<=0), red(-e2 lam^{-j}) (j>0), j in [-(KK+L1), KK+L2];  r = psi^T A(d_last)...A(d_first) Phi / s^n.
Pairs: composite seeds e = e_i + e_j lam^G (bump j shifted by G lam-steps).  Output per (pair type, G):
 r_A, r_B of composite and singles, R_win = r_ij/(r_i r_j) per window, class ratio (R_A R_B)^3, and
 the split-norm quantities for the analytic tail bound.  usage: c_pairs.py PAIRSET Gmax"""
import sys, json, math, numpy as np, mpmath as mp
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
mp.mp.dps=80
A0,s,Phi,psi=A.spectral(); D=A.D; Q=np.eye(D)-np.outer(Phi,psi)
S2=mp.sqrt(2); LAM=3+2*S2; KK=16
def red(x): 
    y=x-mp.floor(x+mp.mpf(1)/2); return float(y)
def mulq(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def lamp(G):
    r=(1,0)
    for _ in range(G): r=mulq(r,(3,2))
    return r
def seeds(e):
    ea,eb=e; zA=(mp.mpf(2*eb)/8, mp.mpf(ea)/8)
    fu=-ea+2*eb; fv=ea-eb; zB=(-mp.mpf(2*fv)/8,-mp.mpf(fu)/8)
    return zA,zB
def core(z):
    e1=z[0]+z[1]*S2; e2=z[0]-z[1]*S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(LAM))))
    ds=[red(e1*LAM**j) if j<=0 else red(-e2*LAM**(-j)) for j in range(-(KK+L1),KK+L2+1)]
    return ds
def weight(ds):
    v=Phi.astype(complex).copy()
    for d in ds: v=(A.Amat(d)@v)/s
    return complex(psi@v)
def weight_full(ds):  # also return row/col split norms at every cut
    vs=[Phi.astype(complex)]
    for d in ds: vs.append((A.Amat(d)@vs[-1])/s)
    return complex(psi@vs[-1]), vs
def win(e):
    zA,zB=seeds(e); return weight(core(zA)), weight(core(zB))
TYPES={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}   # single-bump seeds e (bg 1/4 for odd, bg0 for even)
single={k:win(v) for k,v in TYPES.items()}
pairset=sys.argv[1]; Gmax=int(sys.argv[2])
PAIRS={'A':[('odd','sq2'),('odd','two')],'B':[('odd','odd'),('sq2','sq2')],'C':[('sq2','two'),('odd','2sq2'),('odd','four')]}[pairset]
out=dict(single={k:[[v[0].real,v[0].imag],[v[1].real,v[1].imag]] for k,v in single.items()},rows=[])
for (ti,tj) in PAIRS:
    for sg in (1,-1):
        for G in range(1,Gmax+1):
            ej=mulq(TYPES[tj],lamp(G)); e=(TYPES[ti][0]+sg*ej[0],TYPES[ti][1]+sg*ej[1])
            rA,rB=win(e)
            RA=rA/(single[ti][0]*single[tj][0]); RB=rB/(single[ti][1]*single[tj][1])
            # sign of the shifted bump: (-1) on the bump flips r_j -> r_j for even? use measured ratio and its conj alternative
            ratio=(RA*RB)**3
            row=dict(pair=f'{ti}+{"" if sg>0 else "-"}{tj}',G=G,rA=[rA.real,rA.imag],rB=[rB.real,rB.imag],RA=abs(RA-1),RB=abs(RB-1),cls=[ratio.real,ratio.imag],cls_dev=abs(ratio-1))
            out['rows'].append(row); print(json.dumps(row),flush=True)
json.dump(out,open(f'/workspace/bgs-lineN/N12/logs/c_pairs_{pairset}.json','w'),indent=1)
