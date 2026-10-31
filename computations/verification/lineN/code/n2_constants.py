# Line N [P-arith]: explicit ranges for Theorem W+ from Line L certified constants (final_constants.jsonl).
# Budget: Theorem W needs sup_{x nondeg}|avg_i e(Tr(x lam^i)/q)| * A_k <= 2*eta (T_k <= eta for q >= q0).
# eps_F := 2 eta_F / A_k^F.  Line L used the stricter eta/3 (c_F=(eta/(6A))^2); both reported.
import json, math
from mpmath import mp, mpf, log10, power
mp.dps=40
rows=[json.loads(l) for l in open('/workspace/bgs-lineL/logs/final_constants.jsonl')]
L3=mpf(3)**(mpf(4)/3)*4          # 4*3^{4/3}
def CF(tau_log10):                 # F <= C_F tau^{11/3} for q >= tau^2, tau >= 10^tau_log10
    tau=mpf(10)**tau_log10
    return L3*mpf('1.0001') + mpf('15.01')*tau**(-mpf(2)/3)
out=[]
for r in rows:
    eta=mpf(r['eta']); A=mpf(10)**mpf(r['log10_Ak'])
    for budget,eps in (("full 2eta/A",2*eta/A),("LineL eta/3A",eta/(3*A))):
        C=CF(25)
        # Weil: 2 sqrt(q)/p <= eps  -> q <= (eps p/2)^2
        lw=2*log10(eps/2)
        # (3,3): C^{1/9} (q/p^{7/3})^{1/9} <= eps -> q <= eps^9 p^{7/3}/C
        l33=9*log10(eps)-log10(C)
        # (2,3): (2C)^{1/12} q^{1/6} p^{-13/36} <= eps -> q <= eps^6 p^{13/6}/(2C)^{1/2}
        l23=6*log10(eps)-log10(2*C)/2
        # (2,2): (2q/p^2)^{1/4} <= eps -> q <= eps^4 p^2/2   (never beats Weil)
        l22=4*log10(eps)-log10(2)
        # isotropic (Cochrane-Pinner Thm 1.1): 1.51967 q^{1/8} p^{-3/8} <= eps -> q <= (eps/1.51967)^8 p^3
        liso=8*log10(eps/mpf('1.5196713713'))
        # crossover p where (3,3) range exceeds Weil range: l33 + 7/3 x >= lw + 2x -> x >= 3(lw-l33)
        x33=3*(lw-l33); x23=6*(lw-l23); x_33_23=6*(l23-l33)
        rec=dict(fam=r['fam']+r['typ'],k=r['k'],budget=budget,log10_eps=float(log10(eps)),
                 log10_cWeil=float(lw),log10_c33=float(l33),log10_c23=float(l23),log10_c22=float(l22),
                 log10_ciso_p3=float(liso),log10_p_33_beats_Weil=float(x33),log10_p_23_beats_Weil=float(x23),
                 log10_p_33_beats_23=float(x_33_23),C_F=float(C))
        out.append(rec); print(json.dumps(rec))
json.dump(out,open('/workspace/bgs-lineN/logs/n2_constants.json','w'),indent=1)
