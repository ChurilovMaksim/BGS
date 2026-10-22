#!/usr/bin/env python3
"""Characteristic-zero N7 multiplicity/commutant consequence.
Underlying raw-kernel identities are independently checked by integer phase
histograms, not transferred from a residue-field commutant computation.
"""
if not __debug__:raise RuntimeError('Assertions required')
from pathlib import Path
import json
from independent_check import n7_check
raw=n7_check()
# H=G/T with T=tr G: T^2=-7, hence T^3=-7T and H^3=I, tr H=1.
# X^3-1 is square-free over C, so H diagonalizes with roots 1,w,w^2.
# Linear independence of 1,w over Q and w^2=-1-w give the next constraints.
possible=[(m0,m1,m2) for m0 in range(8) for m1 in range(8) for m2 in range(8) if m0+m1+m2==7 and m0-m2==1 and m1-m2==0]
assert possible==[(3,2,2)]
commutant=sum(m*m for m in possible[0]);assert commutant==17
result={'status':'passed','N':7,'field':'complex numbers, characteristic zero','raw_kernel':'G_xy=zeta_7^(-(3x^2-2xy+3y^2))','identity_verification':raw,'normalization':'T=trace(G), H=G/T','identities':['T^2=-7','T!=0','G^3=T^3 I','H^3=I','trace(H)=1'],'square_free_annihilator':'X^3-1','multiplicity_labels':['1','omega','omega^2'],'multiplicity_constraints':['m0+m1+m2=7','m0-m2=1','m1-m2=0'],'unique_multiplicities':possible[0],'complex_commutant_dimension':commutant,'same_commutant_for':['G','M_7=G/sqrt(7)','U_7(t)=exp(9it/10)G/sqrt(7), every real t'],'boundary':'Exact characteristic-zero consequence of independently verified raw identities. No residue-to-characteristic-zero commutant transfer; no sign choice for T/sqrt(7).'}
(Path(__file__).resolve().parent/'n7_multiplicity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
