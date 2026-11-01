# sensitivity of p1 to a relative increase of A_bad^KP (e.g. background-interplay renormalisation of bad activities)
import json
src=open('/workspace/audit/lineN21b/code/ref_crossover21b.py').read().split('out=[run')[0]
ns={}; exec(src,ns); run=ns['run']
DT=5.0313e-6; out=[]
for C,S0 in [(0.082,3.4456448504559267e-4),(8.8e-4,2.3797849269841034e-6)]:
    for f in (1.0,1.01,1.03,1.05,1.10,1.5,2.0):
        try: r=run(repr(DT+f*S0))
        except StopIteration: print(C,f,'p1 > 6000 (scan limit)'); out.append(dict(C=C,factor=f,first_int='>6000')); continue
        out.append(dict(C=C,factor=f,delta_eff=DT+f*S0,first_int=r['first_int_env'],first_prime=r['first_prime'],viol=r['viol']))
        print(C,f,out[-1]['delta_eff'],r['first_int_env'],r['first_prime'])
json.dump(out,open('../logs/sens22.json','w'),indent=1)
