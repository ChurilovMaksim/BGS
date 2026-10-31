# Line N, [N]: factor h_p and K_p = 4h_p^2+3 (so h_{3p} = h_p K_p) for primes p; record log_p of prime factors,
# check q = 1 mod 2p (split, r | q-1) and ranks; PARI factor with time cap; unfactored cofactors reported.
import sys, json, math, time
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
def hseq(M):
    x,y=1,1; out={1:1}
    for m in range(2,M+1):
        x,y=x+2*y,x+y
        if m%2: out[m]=x
    return out
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 150
TL=int(sys.argv[2]) if len(sys.argv)>2 else 60
PMIN=int(sys.argv[3]) if len(sys.argv)>3 else 5
TRIAL=10**9
H=hseq(3*PMAX+3)
out=open(f"/workspace/bgs-lineN/logs/n1_factor_P{PMIN}_{PMAX}.jsonl","w")
def lam_order_mod(q,cands):
    # order of lambda=3+2sqrt2 in (Z[sqrt2]/q)^*, tested on candidate divisors
    def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
    def pw(e):
        r=(1,0); b=(3,2)
        while e:
            if e&1: r=mul(r,b)
            b=mul(b,b); e>>=1
        return r
    for d in sorted(cands):
        if pw(d)==(1,0): return d
    return None
for p in [int(x) for x in pari(f"primes([{PMIN},{PMAX}])")]:
    rec={"p":p}
    for name,N in (("h_p",H[p]),("K_p",4*H[p]**2+3)):
        assert H[3*p]==H[p]*(4*H[p]**2+3)
        t=time.time()
        pari.default("factor_add_primes",0)
        try:
            F=pari(f"iferr(alarm({TL},factor({N})),E,0)")
            ok = F!=0
        except BaseException as e:
            ok=False
        facs=[]; cof=None
        if ok:
            for q,e in zip(F[0],F[1]):
                q=int(q); e=int(e)
                isp=bool(pari.ispseudoprime(q))
                facs.append((q,e,isp))
        else:
            # fallback: trial by q=1 mod 2p up to 1e9
            M=N; 
            for q in [7]:
                while M%q==0: facs.append((q,1,True)); M//=q
            k=1
            while 2*p*k+1<TRIAL:
                q=2*p*k+1
                if M%q==0:
                    e=0
                    while M%q==0: M//=q; e+=1
                    facs.append((q,e,True))
                k+=1
            if M>1: facs.append((M,1,bool(pari.ispseudoprime(M))))
        items=[]
        for q,e,isp in facs:
            it={"q":str(q) if q>2**63 else q,"e":e,"prime":isp,"log_p_q":math.log(q)/math.log(p),"digits":len(str(q))}
            if isp and q!=7:
                it["q_mod_2p"]=q%(2*p); it["q_mod_8"]=q%8
                if q<10**30: it["rank"]=lam_order_mod(q,[1,3,p,3*p])
            items.append(it)
        rec[name]={"digits":len(str(N)),"factors":items,"time":round(time.time()-t,2),
                   "complete":all(i["prime"] for i in items)}
    out.write(json.dumps(rec)+"\n"); out.flush()
    def summ(n):
        return " ".join(f"{i['log_p_q']:.2f}{'' if i['prime'] else 'C'}" for i in rec[n]["factors"])
    print(p, "h_p:",summ("h_p"),"| K_p:",summ("K_p"),flush=True)
