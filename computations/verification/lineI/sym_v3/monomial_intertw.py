"""EXACT search (integer arithmetic mod 8) for monomial intertwiners between finite factors of the G2 (±2,8) cases.
A family is {(t_n, p_n)}: A_n e_s = e(-p_n(s)/8) e_{t_n(s)}, n mod 8.  X e_s = e(-c_s/8) e_{pi(s)} intertwines F -> F' iff
  pi(t_n(s)) = t'_n(pi(s))  and  c_{t_n(s)} + p_n(s) ≡ c_s + p'_n(pi(s))  (mod 8)   for all s, n.
Such X is unitary (monomial with unimodular entries).  Families:
  F(m,a)            : the case itself;
  Fconj(m,a)        : (-1)^n conj(A_n)  -> exponents (-p_n + 4n) mod 8   (antilinear relation via complex conjugation K);
  Fneg(m,a)         : A_{-n}  (reflection s -> -s on the disc lattice).
Prints, for every target case, whether F(9,2) [or its conj/neg variants] is monomially equivalent, with the witness."""
import sys, json, hashlib, os
# DF2 (delta review): no absolute paths; gstates/law are imported from ../cert_v2 (R2 version, imports law from
# its own directory) relative to this script, and the JSON is written next to this script.
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','cert_v2'))
from gstates import g2params, reach, finite
def fam(m,a,mode='id'):
    P=g2params(m,a,8); idx,tg=reach(P,8); F={}
    for n in range(8):
        nn=(-n)%8 if mode=='neg' else n
        t={}; p={}
        for (o,i,ph8,tw) in finite(P,idx,tg,nn,None):
            t[i]=o; p[i]=ph8%8 if mode!='conj' else (-ph8+4*n)%8
        F[n]=(t,p)
    return F
def search(F,G):
    S=range(16)
    for s0 in S:
        pi={0:s0}; c={0:0}; fr=[0]; ok=True
        while fr and ok:
            s=fr.pop()
            for n in range(8):
                t,p=F[n]; t2,p2=G[n]
                ts=t[s]; target=t2[pi[s]]; cs=(c[s]+p2[pi[s]]-p[s])%8
                if ts in pi:
                    if pi[ts]!=target or c[ts]!=cs: ok=False; break
                else: pi[ts]=target; c[ts]=cs; fr.append(ts)
        if ok and len(pi)==16 and len(set(pi.values()))==16:
            # full verification
            for s in S:
                for n in range(8):
                    t,p=F[n]; t2,p2=G[n]
                    assert pi[t[s]]==t2[pi[s]] and (c[t[s]]+p[s]-c[s]-p2[pi[s]])%8==0
            return dict(pi=[pi[s] for s in S],c=[c[s] for s in S])
    return None
base=fam(9,2); out={}
for m in (9,15,21,27):
    for a in (2,-2):
        G=fam(m,a)
        r=dict(lin=search(base,G),conj=search(fam(9,2,'conj'),G))
        out[f'{m},{a}']=r
        print(m,a,'linear:', 'YES' if r['lin'] else 'no', ' antilinear(conj):','YES' if r['conj'] else 'no',flush=True)
r=search(fam(9,2,'neg'),base); out['neg_9_2']=r; print('reflection  A_{-n} ~ A_n in case (9,2):','YES' if r else 'no')
out['code_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
json.dump(out,open(os.path.join(HERE,'monomial_intertw.json'),'w'),indent=1)
