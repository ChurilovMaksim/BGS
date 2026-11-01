"""referee lineN20: independent arb re-check of Prop K numbers + finite part + C_cert, with old and new delta_true."""
import json, math, collections
from flint import arb, ctx
ctx.prec=200
lam=3+2*arb(2).sqrt()
def beta(rho): return 2*(1/arb(rho)).log()/lam.log()
q=(arb(2).log()*arb('1.5')*(1-beta('0.28'))).exp()
print('beta',beta('0.28').str(15),'q',q.str(15))
# finite part from logs, own aggregation (dedup by class, exclude model and zr>=4)
MODEL={(1,0),(0,1),(2,0),(0,2)}
span={}
for l in open('/workspace/bgs-lineN/N14/logs/a_enum.jsonl'):
    r=json.loads(l); span[(r['a'],r['b'])]=r['span']
rows={}
for l in open('/workspace/bgs-lineN/N15/logs/a_cert3.jsonl'):
    r=json.loads(l); rows[(r['a'],r['b'])]=(r['j'],r['zr'],r['rArB2_up'],r['absw_up'],span[(r['a'],r['b'])])
import glob
for f in glob.glob('/workspace/bgs-lineN/N20/logs/a_cert_ext*.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r.get('coded'): continue
        assert (r['a'],r['b']) not in rows
        rows[(r['a'],r['b'])]=(r['j'],r['zr'],r['rArB2_up'],r['absw_up'],r['span'])
S2=collections.defaultdict(lambda: arb(0)); Sw=collections.defaultdict(lambda: arb(0)); nb=collections.Counter()
for ab,(j,zr,s2,w,sp) in rows.items():
    if ab in MODEL or zr>=4: continue
    S2[j]+=arb(s2); Sw[j]+=arb(w); nb[j]+=1
Cc={}
for j in sorted(S2):
    for rho in ('0.2726','0.28'):
        Cc[(j,rho)]=(S2[j]/(arb(2)**(j*(1-beta(rho))))).upper()
    print(j,nb[j],S2[j].str(6),Sw[j].str(6),float(Cc[(j,'0.2726')]),float(Cc[(j,'0.28')]))
print('max C 0.2726',max(float(Cc[(j,'0.2726')]) for j in S2),'max C 0.28',max(float(Cc[(j,'0.28')]) for j in S2))
Abad=2*sum((Sw[j] for j in S2),arb(0)); print('A_bad fin j<=14',Abad.str(10))
# also check the l3<=l2 per shell on certified data: Sw <= S2^{3/2}
print('l3<=l2 holds per shell:',all(Sw[j]<=S2[j]**arb('1.5') for j in S2))
# span <= 2j + check for j>=5
print('max span/j (j>=5, bad):',max(sp/j for ab,(j,zr,s2,w,sp) in rows.items() if j>=5 and zr<4 and ab not in MODEL),
      'max span-0.787j:',max(sp-0.787*j for ab,(j,zr,s2,w,sp) in rows.items() if zr<4 and ab not in MODEL))
def fin(J0,a,g0=4):
    s0=arb(0); s1=arb(0)
    for ab,(j,zr,s2,w,sp) in rows.items():
        if j>J0 or ab in MODEL or zr>=g0: continue
        l=sp+g0; e=(arb(a)*l).exp(); s0+=2*arb(w)*e; s1+=2*arb(w)*l*e
    return s0,s1
def tail(C,J0,a,g0=4):
    r=q*(2*arb(a)).exp(); J=J0+1
    # direct partial sum + geometric remainder, independent of closed form
    g=arb(0); gj=arb(0)
    for jj in range(J,J+400): g+=r**jj; gj+=jj*r**jj
    rem=r**(J+400)/(1-r)**2*(J+400+1)   # crude bound for both remainders
    g+=arb(0,rem.upper()); gj+=arb(0,rem.upper())
    pref=2*arb(C)**arb('1.5')*(arb(a)*g0).exp()
    return pref*g, pref*(2*gj+g0*g)
RL=arb('6.234e-4')
for (J0,C,a) in [(12,0.082,2.6925e-03),(12,0.00088,8.2498e-06),(14,0.082,1.1273e-03)]:
    s0,s1=fin(J0,a); t0,t1=tail(C,J0,a); S0=s0+t0; S1=s1+t1; lhs=S0+S1/5
    print(J0,C,'a',a,'S0fin',s0.str(7),'T0',t0.str(5),'T1',t1.str(5),'S0',S0.str(7),'lhs',lhs.str(6),'KP',bool(lhs<arb(a)),
          'budget(old 2.470e-6)',float((RL-S0-arb('2.470e-6')).lower()),'budget(N21v2 5.0313e-6)',float((RL-S0-arb('5.0313e-6')).lower()))
for tg,name in ((arb('3.1117e-4'),'N20 tgt'),((arb('6.23397e-4')-arb('1e-6'))/2,'N14 conv (dint=1e-6)'),((RL-arb('5.0313e-6'))/2,'half of (ReL - delta_true v2)'),
                ((RL-arb('5.0313e-6')-arb('2.0316e-6'))/2,'half of (ReL - delta_true v2 - A_bad fin)')):
    g=q**13/(1-q); print(name, float(((tg/(2*g))**(arb(2)/3)).lower()))
