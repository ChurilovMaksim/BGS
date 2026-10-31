"""N14b pre-flight (D) [N]: g(0) = (sum_a |J_a(1.8)| e^{tau|a|})^2 (Prop E majorant at the slow twist, = its sup),
kappa = g(0)/(lam r2), predicted c_D = max(0, 1 + ln kappa / ln eps). Threshold for c_D<0.387: g(0) < 3.58."""
import mpmath as mp, math, json
lam=3+2*math.sqrt(2); eps=1+math.sqrt(2); r2=1.0529012
out={}
for tau in [0.0,0.01,0.05]:
    s=sum(abs(mp.besselj(a,1.8))*mp.e**(tau*abs(a)) for a in range(-60,61)); g0=float(s*s)
    k=g0/(lam*r2); out[tau]=dict(g0=g0,kappa=k,c_D=max(0,1+math.log(k)/math.log(eps)),avg_g=float(sum(mp.besselj(a,1.8)**2 for a in range(-60,61))))
print(json.dumps(out,indent=1)); json.dump(out,open('logs/b_g0.json','w'),indent=1)
