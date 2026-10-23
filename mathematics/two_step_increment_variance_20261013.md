# Second moment of the frozen two-step increment

**Stable claim:** BGS-TRACE-078. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 13 October 2026. The proof below is self-contained;
TRACE-075 gives its companion drift with the same frozen-label convention.
[Review and finite scope](../archive/evidence/executions/20261013/two-step-variance/README.md).
Let S be unitary of size u>=3, P=|S|², K=P², delta=max P<=1/4.
Fix distinct i,j. Choose e uniformly among all u labels and a fresh phase
w. Freeze K'ij=Kij when e=i or j; otherwise use exact Schur feedback.
Claim:

E[(K'ij-Kij)² | S] <=2600 delta² [Kij+(P³)ij]/u.             (V1)

The expectation bound does not require uniform phase: the stronger sum of
per-port bounds below holds for any choices of w_e on the unit circle.
This is a raw second moment, hence also bounds conditional variance.
It is not concentration, sustained decay, early entry survival or BGS.

## Expansion and notation
For each e not i,j and k not e let
x=Pik, y=Pkj, alpha=Sie Sek conjugate(Sik),
beta=Ske Sej conjugate(Skj), b=P_ie P_ek, d=P_ke P_ej.
r_e=P_ie P_ej. Define sums over k!=e:
A_e=sum(y alpha+x beta),
B_e=sum(x d+y b+2 Re(alpha conjugate(beta))),
C_e=sum(alpha beta),
D_e=sum(alpha d+beta b), F_e=sum(b d).
Write q_e=w_e/(1-S_ee w_e); |q_e|<=2 since delta<=1/4.
Then the exact real increment is

Delta_e=-r_e+q_e A_e+conj(q_e A_e)+|q_e|² B_e
        +q_e² C_e+conj(q_e² C_e)
        +q_e|q_e|² D_e+conj(q_e|q_e|² D_e)+|q_e|⁴ F_e.   (V2)

All estimates below may sum over all e; excluded e=i,j only reduce a
nonnegative sum. Definitions extended algebraically to these labels for
bounds only; their actual frozen increments are zero.

## Complete coordinate squared sums
1. sum r_e² <=delta² Kij.

2. For the full k sum in the first component of A_e, Parseval in the
unitary rows gives
sum_e |Sie sum_k Pkj Sek conjugate(Sik)|²
 <=delta sum_k Pkj² Pik <=delta² Kij.
The second component uses Parseval in the unitary columns and obeys the
same bound. Therefore sum|A_full|²<=4delta² Kij.
The omitted k=e term is 2 S_ee r_e; its squared sum <=4delta³ Kij.
By |a-b|²<=2|a|²+2|b|²,
sum |A_e|² <=(8+8delta)delta² Kij <=10delta² Kij.

3. Let T1_e=sum x d=P_ej sum_(k!=e)Pik Pke,
T2_e=sum y b=P_ie sum_(k!=e)Pkj Pek.
Each T1,T2<=delta², and each full coordinate sum <=(P³)ij.
Hence sum T1²,sum T2² <=delta²(P³)ij.
For H_e=sum alpha conjugate(beta), Cauchy gives
|H_e|²<=r_e [sum_(k!=e)Pek Pke][sum_(k!=e)Pik Pkj]
       <=r_e delta Kij.
Thus sum |H_e|²<=delta Kij²<=delta² Kij.
B_e=T1+T2+2Re H, so
sum B_e²<=6delta²(P³)ij+12delta² Kij.

4. The same Cauchy bound for C_e gives
sum |C_e|²<=delta Kij²<=delta² Kij.

5. For D1_e=sum alpha d, weighted Cauchy gives
|D1_e|²<=P_ie P_ej² [sum Pek Pke][sum Pik Pke]
        <=delta P_ie P_ej² K_ie.
Using P_ie,P_ej<=delta and sum_e P_ej K_ie=(P³)ij,
sum |D1|²<=delta³(P³)ij.
Similarly D2_e=sum beta b has squared sum<=delta³(P³)ij,
using sum_e P_ie K_ej=(P³)ij.
Therefore sum |D_e|²<=4delta³(P³)ij.

6. F_e=r_e sum_(k!=e)Pek Pke<=delta r_e,
so sum F_e²<=delta⁴ Kij.

## Combination
By (V2),
|Delta_e|<=r_e+4|A_e|+4|B_e|+8|C_e|+16|D_e|+16 F_e.
Cauchy for these six groups and the preceding squared sums yield

sum_(e!=i,j) Delta_e²
 <=6delta² [(1+160+192+64+256delta²)Kij
                  +(96+1024delta)(P³)ij]
 <=6delta² [433 Kij+352(P³)ij]
 <=2598delta² [Kij+(P³)ij].

Uniform coordinate averaging gives V1 with the rounded constant 2600.
No asymptotic limit, phase cancellation or Schatten estimate is used here.
The gain uses unitary Parseval before taking absolute values of the
complete coordinate sum. Independent reconstruction checked row/column indices, complex conjugations,
the omitted diagonal term, frozen labels and the exact phase product.
No concentration corollary has yet been accepted. Mathematical priority,
external referee certification and new Lean/C++ certification are not claimed.
