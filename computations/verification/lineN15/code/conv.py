"""N15 (2b) composite core->true conversion [CA-fp, given the N6/N8 conversion lemma in operator norms].
For every window (1560 replay jobs of N14 c2_mid; 5109 classes of N14 a_enum/a_cert): true window weight r_true satisfies
 |r_true - r~| <= rad_c2 + |r~| scale + (err_proj + err_pert)(1+scale) + err_tail     (N8 n8_cert.excursion, num_err replaced by rad_c2)
 with  GA <= sqrt(cond_H) * prod_t Nbar_H(d_t)   (all N_H >= 1, so the full product bounds every contiguous sub-product; ||P||_2 <= sqrt(c_hi/c_lo)||P||_H,
       cond_H = 21.103 [CA] N13 b_arb V1);  Nbar_H: [CA] quadratic bound for |d|<=1/256, else [CA-fp] table nh_table_2048 (max of cell and neighbours).
 GT = GA(1+Xn/|s|); er,el = RA * residuals of the npz Phi~, psi~/||psi~|| (binary64 + rounding bounds); dPi, RA, normPi(T), Pert, Xn, N1, Cpow,
 mu-s from N8 n8_cert_fam.json [CA].  usage: conv.py replay|classes"""
import sys, json, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N12/code')
import a_ops as A, digits as Dg
import mpmath as mp
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s']); Phi=z['Phi'].astype(complex); psi=z['psi'].astype(complex)
N8=json.load(open('/workspace/bgs-lineN/N8/logs/n8_cert_fam.json'))
RA=N8['RA_Gamma']; dPi=N8['dPi']; normPi=N8['normPi']; normPiT=normPi-dPi; Pert=N8['Pert']; Xn=N8['Xn']; N1=N8['N1']; Cpow=N8['Cpow']; mus=N8['mu_minus_s']
condH=21.103088312483127; sq=math.sqrt(condH)*(1+1e-12)
tab=json.load(open('/workspace/bgs-lineN/N15/logs/nh_table_2048.json')); TB=tab['bound']; NC=tab['NC']
def Nbar(d):
    if abs(d)<=1/256: return 1+1.01e-12+4260*d*d
    k=int(math.floor((d+0.5)*NC)); k=min(max(k,0),NC-1)
    return max(TB[k],TB[min(k+1,NC-1)],TB[max(k-1,0)])
u=2.0**-53; D=A.D
A0=A.Amat(0.0); gam=1.05*(D+4)*2*u*math.sqrt(2)
dA0=float(np.sum(np.abs(A.COEF0)))*A.RAD*D
psiN=psi/np.linalg.norm(psi); PhiN=Phi/np.linalg.norm(Phi)
def res(M,v,l): return np.linalg.norm(M@v-l*v)*1.01+gam*np.linalg.norm(np.abs(M)@np.abs(v))*1.01+dA0*np.linalg.norm(v)+u*abs(l)*2*np.linalg.norm(v)
er=RA*res(A0,PhiN,s); el=RA*res(A0.T,psiN,s)
den0=psiN@PhiN; den=abs(den0)-er
Fs=Pert/abs(s)
def conv(ds,tail,rt,rad):
    n=len(ds); G=1.0
    for d in ds: G*=Nbar(d)
    GA=sq*G; GT=GA*(1+Xn/abs(s))
    err_proj=(el*GA+GA*er+el*GA*er)/den+abs(rt)*er/den
    prodL=GT*(1+GT*Fs)**n
    err_pert=2*dPi*prodL+normPiT*GT*((1+GT*Fs)**n-1)
    eps=math.expm1(Cpow*2*math.pi*N1*tail/(abs(s)-mus))
    scale=(1+mus/(abs(s)-mus))**n-1
    err_tail=normPi*prodL*(1+scale)*((1+eps)**2-1)
    E=rad+abs(rt)*scale+(err_proj+err_pert)*(1+scale)+err_tail
    return E,dict(GA=GA,err_pert=err_pert,err_proj=err_proj,err_tail=err_tail,scale=scale)
def tails(zz,KK=18):
    e1=zz[0]+zz[1]*Dg.S2; e2=zz[0]-zz[1]*Dg.S2
    L1=max(0,int(mp.ceil(mp.log(abs(e1)+1)/mp.log(Dg.LAM)))); L2=max(0,int(mp.ceil(mp.log(abs(e2)+1)/mp.log(Dg.LAM))))
    return float(abs(e1)*Dg.LAM**(-(KK+L1+1))/(1-1/Dg.LAM)+abs(e2)*Dg.LAM**(-(KK+L2+1))/(1-1/Dg.LAM))
def window_conv(ea,eb,rts,rads):
    return [conv(Dg.core(zz,18),tails(zz),rt,rad) for zz,rt,rad in zip(Dg.seeds(ea,eb),rts,rads)]
if __name__=='__main__':
    print('er',er,'el',el,'den',den,'dPi',dPi,'normPiT',normPiT,flush=True)
    if sys.argv[1]=='replay':
        rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/c2_mid.jsonl')]
        with open('/workspace/bgs-lineN/N15/logs/conv_replay.jsonl','w') as f:
            for r in rows:
                rts=[complex(sum(r[W]['re'])/2,sum(r[W]['im'])/2) for W in 'AB']; rads=[r[W]['rad'] for W in 'AB']
                for W,m,(E,info) in zip('AB',rts,window_conv(r['e'][0],r['e'][1],rts,rads)):
                    r[W]['re']=[m.real-E,m.real+E]; r[W]['im']=[m.imag-E,m.imag+E]; r[W]['rad']=E; r[W]['conv']=info
                f.write(json.dumps(r)+'\n')
    else:
        rows=[json.loads(l) for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl')]
        rc={}
        for l in open('/workspace/bgs-lineN/N14/logs/a_cert.jsonl'): q=json.loads(l); rc[(q['a'],q['b'])]=q['rad']
        with open('/workspace/bgs-lineN/N15/logs/conv_classes.jsonl','w') as f:
            for r in rows:
                rts=[complex(*r['rA']),complex(*r['rB'])]; cv=window_conv(2*r['a'],2*r['b'],rts,rc[(r['a'],r['b'])])
                upA=abs(rts[0])+cv[0][0]; upB=abs(rts[1])+cv[1][0]
                f.write(json.dumps(dict(j=r['j'],a=r['a'],b=r['b'],zr=r['zr'],absw_true_up=(upA*upB)**3,EA=cv[0][0],EB=cv[1][0],GA=[cv[0][1]['GA'],cv[1][1]['GA']]))+'\n')
    print('done')
