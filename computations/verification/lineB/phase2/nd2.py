"""ND^(2) check: for supported Gamma-orbits o (one representative each), are the pair sums S(o1)+S(o2) (o1<=o2)
pairwise distinct except trivially? Reports non-trivial coincidences, separating those induced by ND^(1) failures.
Also prints the predicted joint (nu, Bohr-eta) 4th moment under ND^(1),ND^(2):  M4 = 2 - sum_o |o|^4 /(D_eff^2 B_sym^2)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from p2lib import *
import sys, time
TOL=float(sys.argv[1]); import mpmath; mpmath.mp.dps=40
CKm={k:mpmath.mpc(c.real,c.imag) for k,c in CK.items()}
# exact rational coefficients (x800) to avoid float input error
from fractions import Fraction as Fr
sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common')); from audit46_core import cEx
CKm={k:mpmath.mpc(mpmath.mpf(cEx(k,0)[0].numerator)/cEx(k,0)[0].denominator, mpmath.mpf(cEx(k,0)[1].numerator)/cEx(k,0)[1].denominator) for k in range(-9,10) if cEx(k,0)!=(0,0)}
def Smp(thetas_num,d2):
    return mpmath.re(sum(c*mpmath.expjpi(2*mpmath.mpf(k*t)/d2) for t in thetas_num for k,c in CKm.items()))
for m in [int(a) for a in sys.argv[2:]]:
    t0=time.time(); O,supp=support_data(m); d1,d2=O.d1,O.d2; Deff=int(supp.sum())
    X1=O.T[0]; X2=O.T[1] if m>1 else O.T[0]
    code=lambda a,b: a.astype(np.int64)*d2+b
    lab=code(X1,X2); a,b=X1.copy(),X2.copy(); ra,rb=X1.copy(),(6*X1-X2)%d2
    for j in range(m):
        lab=np.minimum(lab,np.minimum(code(a,b),code(ra,rb))); a,b=b,(6*b-a)%d2; ra,rb=rb,(6*rb-ra)%d2
    L=lab[supp]; S=O.S[supp]
    uniq,first,size=np.unique(L,return_index=True,return_counts=True)
    So=S[first]; n=len(So)
    o1=np.argsort(So); gaps1=np.diff(So[o1]); nd1_fail=int((gaps1<=TOL).sum())
    Bsym=float((size.astype(float)**2).sum())/Deff
    M4pred=2-float((size.astype(float)**4).sum())/(Deff**2*Bsym**2)
    I,J=np.triu_indices(n)
    P=So[I]+So[J]; o=np.argsort(P,kind='stable'); Ps=P[o]; g=np.diff(Ps)
    hits=np.flatnonzero(g<=TOL)
    nontriv=0; induced=0; examples=[]; nearmiss=[]; ords=set()
    for h in hits:
        p,q=o[h],o[h+1]; A={int(I[p]),int(J[p])}; B={int(I[q]),int(J[q])}
        if A==B: continue
        if A&B:
            x=list(A-B) or list(A); y=list(B-A) or list(B)
            if abs(So[x[0]]-So[y[0]])<=TOL: induced+=1; continue
        # exact (40-digit) recheck of the 4 orbit sums
        reps=[int(np.flatnonzero(supp)[first[z]]) for z in (list(A)*2)[:2]+(list(B)*2)[:2]]
        vals=[Smp([int(O.T[j].ravel()[r]) for j in range(m)],d2) for r in reps]
        diff=abs(vals[0]+vals[1]-vals[2]-vals[3])
        if diff>mpmath.mpf(10)**-30: nearmiss.append(float(diff)); continue
        nontriv+=1
        for r in reps: ords.add(int(d2//math.gcd(d2,math.gcd(*[int(O.T[j].ravel()[r]) for j in range(m)]))))
        if len(examples)<3: examples.append((sorted(A),sorted(B),float(Ps[h])))
    mingap=g[g>TOL].min() if (g>TOL).any() else np.nan
    print(f'm={m} orbits={n} pair-sums={len(P)} ND1-coincident adjacent={nd1_fail} pair-sum coincidences: induced-by-ND1={induced} '
          f'NONTRIVIAL(exact to 1e-30)={nontriv} float-tol hits that are NOT exact={len(nearmiss)} (min |diff|={min(nearmiss) if nearmiss else float('nan'):.2e}) min nonzero pair-sum gap={mingap:.2e}  B_sym={Bsym:.6f}  predicted joint M4={M4pred:.8f}  t={time.time()-t0:.0f}s',flush=True)
    if ords: print('   orders of points involved in exact non-trivial pair-sum coincidences:',sorted(ords))
    for ex in examples: print('   example (orbit idx pairs, sum)',ex)
