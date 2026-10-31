"""N8b [N]: effective excursion rate Gamma_eff = mu* |r|^{1/E}, E = m - s_forced, s_forced = W*max(0, log_lam(c/depth)),
W = 6 (consistent, c|h_p), 2 (consistent, c|K_p), 3 (inconsistent). Classes with |r| <= 3*floor skipped. Hypothesis G(Gamma) needs Gamma < T' = 1.4279."""
import json, math, sys
lam=3+2*math.sqrt(2); mu=1.9154712
def xy(n):
    x,y=1,0
    for _ in range(n): x,y=x+2*y,x+y
    return x
files=sys.argv[1:] or ['logs/b_cline.jsonl']
allg=[]; out=[]
for f in files:
  for l in open(f):
    d=json.loads(l); p=d['p']; c=d['c']; m=3*p; hp=xy(p)
    if c==hp and d['line']=='cons': continue        # the h_p line itself (gap (a)) excluded
    W=(6 if hp%c==0 else 2) if d['line']=='cons' else 3
    gs=[]
    for t in d['top']:
        if t['absr']<=3*t['floor'] or t['depth']==0: continue
        s=W*max(0.0,math.log(c/t['depth'],lam)); E=m-s
        g=mu*t['absr']**(1/E); gs.append((g,t['depth'],t['absr'],s))
    if gs:
        g=max(gs); allg.append(g[0])
        out.append('%3d %18d %-10s W=%d  Gamma_eff max %.4f (depth %s, |r| %.2e, s_forced %.1f of m=%d)'%(p,c,d['line'],W,g[0],g[1],g[2],g[3],m))
print('\n'.join(out)); print('OVERALL max Gamma_eff = %.4f  (T\'=1.4279, 1.233 = mu* lam^{-1/4})'%max(allg))
