"""N8: [P+CA] explicit constants for (i) sup_n ||L_4^n (I-Pi)|| <= R2' (Riesz-Dunford on |z|=1) and
(ii) other-sector absorption in Prop X / X'. Twist-independent operator-norm bound Bop >= ||L_{a,tau}|| for all a, tau:
||A_tau|| <= Frobenius( block-sum_n |w(n)| ||M_{c,n}||_F ) ; ||L|| <= ||A|| + ||X|| + ||Delta||.
All arb, upward. Reads Line F certificates read-only."""
import sys, json, math
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
import cert_core as C
from flint import arb
fro_entries={}
for (c2,n),(j2,Mx) in C.blocks.items():
    s=arb(0)
    for i in range(Mx.nrows()):
        for j in range(Mx.ncols()): s+=abs(Mx[i,j])**2
    key=(c2,j2); fro_entries[key]=fro_entries.get(key,arb(0))+C.W[n]*s.sqrt()
Aop=sum((v**2 for v in fro_entries.values()),arb(0)).sqrt()
Bop=Aop+C.Xn+C.Delta
nc=json.load(open('/workspace/bgs-lineN/N6/logs/n_cert.json')); Pert=arb(nc['Pert'])
LF='/workspace/bgs-lineF/logs/'
out={'Aop':float(Aop.upper()),'Bop':float(Bop.upper()),'Pert':float(Pert.upper()),'trace_norm':float(C.Tn.upper())}
for a in ['0','2','6']:
    s=json.load(open(LF+f'certV_eta2_a{a}.json'))['sectors'][a]
    FR2=arb(s['F_R2']); R2=FR2/Pert*arb('1.0000001'); R2p=R2/(1-FR2)
    out['sector'+a]=dict(R2=float(R2.upper()),R2p=float(R2p.upper()),Ap_root=s['Ap_root'])
s4=json.load(open(LF+'certV_eta2_a4_tight.json'))['sectors']['4']
F=arb(s4['b21'])+Pert; FR2=arb(s4['F_R2']); R2=FR2/F*arb('1.0000001'); out['sector4']=dict(R2p=float((R2/(1-FR2)).upper()))
# other-sector ratio bound: |Zhat_a| <= TN * Bop^(6*ncore) * (C_a exp(C_a*2pi*N1*S))^7 ;  |Z_8| >= (1/2)(1-lam^-m)(mu^m - 3012.3)
mu=arb('1.9154712'); N1=arb(nc['N1']); lam=C.lam; pi=arb.pi()
def ratio_bound(p, ncore=39, zmax=arb(2)**arb('0.5')/4, KK=18):
    m=3*p; S=2*zmax*lam**(-KK)*lam/(lam-1)
    Ca=max(arb(out['sector'+a]['R2p']) for a in ['0','2','6'])
    num=C.Tn*Bop**(6*ncore)*(Ca*(Ca*2*pi*N1*S).exp())**7
    den=(1-lam**(-m))*(mu**m-arb('3012.3'))/2
    return num/den
for p in [101,201,301,401,601,1165]:
    out[f'other_ratio_p{p}']=float(ratio_bound(p).upper())
# smallest p with 3 sectors * ratio <= 1e-6 * Re w*_lo
Rew=arb('2.8895e-4'); p=5
while not (3*ratio_bound(p) < Rew*arb('1e-6')): p+=2
out['p_other']=p
print(json.dumps(out,indent=1)); json.dump(out,open('/workspace/bgs-lineN/N8/logs/r_other.json','w'),indent=1)
