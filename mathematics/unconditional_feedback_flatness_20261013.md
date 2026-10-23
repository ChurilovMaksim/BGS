# Unconditional feedback flatness and fixed-order clocks

**Stable claim:** BGS-TRACE-080. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 13 October 2026. This concerns an auxiliary random feedback trajectory,
not deterministic BGS universality.

## 1. Statement and parameters

Fix C0>=1 and kappa>0. Let S_N be ANY deterministic unitary with
max|S_Nij|²<=C0/N and ||P_N-J_N||<=1/100, P_N=|S_N|².
At each step choose a uniformly random retained port, then an independent
uniform circle phase, and form the exact survivor Schur unitary. Original
labels are preserved. Put ell=log(2N),

L=C0+7, g=1/10, C=1+g(L-1), T=C0+4C+3,
K0=32T, D=K0 ell, m=ceil ell^(4+kappa), p=2ceil ell.

For sufficiently large N the trajectory exists down to m and simultaneously
for all N>=u>=m has

max P_u<=D/u,
||P_u-J_u||<=g,
max_i sum_j P_uij² <=L/u, max_j sum_i P_uij²<=L/u,
max_(i,j) (P_u²)ij<=T/u,                                  (F1)

outside probability O_(C0,kappa)(ell^(-1-kappa)). All pairs include the
diagonal. More precisely the failure bound is the sum of F15 below.
No random initial-law assumption, future-flatness conditioning, effective
startup, deterministic spectral local law, TRACE-005 or BGS conclusion.
The actual odd-N fixed-coupling family supplies only named eventual
initial inputs FM-021 and initial WKB entry flatness.

## 2. Row-energy feedback: exact identities

For unitary S of size v, P=|S|² and delta=max P, define
R_i=sum_j P_ij², A_i=sum_j P_ij(P²)_ij.
Since PJ=JP=J and rho=||P-J||,

A_i=1/v+<row_i(P-J),row_i((P-J)²)>
   <=1/v+rho(R_i-1/v).                                    (F2)

No symmetry or normality is used. The column version is obtained by
transposing S and P; the Schur feedback rule commutes with transposition.

Fix a row label i. For a chosen e=i freeze R'_i=R_i for this transition;
for e!=i update the actual retained row. For j!=e let
x=P_ij, alpha=S_ie S_ej conjugate(S_ij), b=P_ie P_ej,
a=S_ee, d=1-P_ee, q=w/(1-aw). Then

E_w(P'_ij)²=x²+4xb/d+4Re(conjugate(a) alpha b)/d²
                  +(1+P_ee)b²/d³.                        (F3)

This follows from Eq=Eq²=0, E|q|²=1/d,
E(q|q|²)=conjugate(a)/d², E|q|⁴=(1+P_ee)/d³.
The base coordinate-averaged decrement is -R_i+P_ii².
The positive quadratic sum is at most 4A_i/(1-delta).
For the cubic sum, using sqrt(P_ee P_ej)<=delta,

sum_(e!=i,j!=e) |a alpha b|
 <=delta sum_e P_ie^(3/2) sqrt(sum_j P_ej P_ij)
 <=delta sqrt(R_i A_i)<=delta(R_i+A_i)/2.                  (F4)

The omitted terms are nonnegative in these majorants. The quartic sum
is bounded by delta(1+delta)R_i/(1-delta)³. Hence

v E DeltaR_i <=-(1-c(delta))R_i+d(delta)A_i+P_ii²,
c(delta)=2delta/(1-delta)²+delta(1+delta)/(1-delta)³,
d(delta)=4/(1-delta)+2delta/(1-delta)².                     (F5)

At delta<=1/16, c<=752/3375, d<=992/225<5. If rho<=1/10,
c+d rho<=448/675<2/3. Using F2 gives

E DeltaR_i <=-R_i/(3v)+5/v²+delta²/v.                     (F6)

## 3. Row-energy second moment and pointwise range

For e!=i, r_e=P_ie². Define sums over j!=e:
A_e=2sum x alpha, B_e=4sum x b, C_e=sum alpha²,
D_e=2sum alpha b, F_e=sum b².
The exact row-energy increment is

DeltaR_e=-r_e+2Re(q A_e)+|q|²B_e+2Re(q² C_e)
                   +2Re(q|q|²D_e)+|q|⁴F_e.               (F7)

Here A_i denotes the positive scalar in F2, whereas A_e is the complex
coefficient in F7. They are different objects.
Full coordinate squared sums (extend algebraically to e=i only for these
nonnegative majorants) satisfy

sum r_e²<=delta² R_i,
sum |A_e|²<=10delta² R_i,
sum B_e²<=16delta² A_i,
sum |C_e|²<=delta² A_i,
sum |D_e|²<=4delta³ A_i,
sum F_e²<=delta⁴ R_i.                                    (F8)

For A_e apply row Parseval to 2S_ie sum_j P_ij S_ej conjugate(S_ij).
Its full squared sum is <=4delta sum_j P_ij³<=4delta²R_i.
The omitted j=e coefficient is 2S_ee P_ie²; its squared sum is
<=4delta³R_i. Subtracting it costs factor two, giving <=10delta²R_i.
Let Bie=sum_j P_ij P_ej<=delta. Then B_e<=4P_ie Bie, while
|C_e|<=P_ie Bie. Each P_ie Bie<=delta² and its full port sum is A_i;
this proves the next two bounds. Weighted Cauchy gives
|D_e|²<=4P_ie³(sum_j P_ej²)(sum_j P_ej P_ij)
       <=4delta³ P_ie Bie, proving the D bound. Finally
F_e=P_ie² sum_(j!=e)P_ej²<=delta P_ie².

For delta<=1/4, |q|<=2. Six-group Cauchy in F7 gives

sum_(e!=i)(DeltaR_e)²
 <=6delta²[(161+256delta²)R_i+(320+1024delta)A_i]
 <=3500delta²(R_i+A_i).

Thus uniform coordinate choice (with frozen e=i) gives

E (DeltaR_i)²<=3500delta²(R_i+A_i)/v.                      (F9)

For every phase, direct Cauchy gives |A_e|<=2delta sqrt(R_i),
B_e<=4delta², |C_e|<=delta², |D_e|<=2delta^(5/2), F_e<=delta³.
If delta<=1/16, F7 therefore gives

|DeltaR_i|<=8delta sqrt(R_i)+34delta².                     (F10)

The column analogues F5--F10 hold by transpose, with column Parseval.
These are analytic identities/bounds, not numerical hypotheses.

## 4. A single joint stopping rule

Start at size N and stop at the first new full state violating ANY of

max P_u<=D/u,
||M_u||<=1/11, M_u=(I-P_u+J_u)^(-1)-I_u,
all row/column energies <=L/u,
all two-step entries (P_u²)ij<=T/u.                        (F11)

Include the full first violating state and simultaneous exits. Initially
all bounds hold for large N: M_N norm<=1/99, row/column energies and
two-step entries <=C0/N. A missing Green inverse is also a stop; its first
failure is excluded by the old-state Neumann argument below.
All active old states have delta<=D/v<=1/16 (m>=16D), and
rho<=||M||/(1-||M||)<=1/10. Phase denominators are nonzero.
For a scalar row or pair stop it additionally on endpoint removal, using
the frozen old value for that removing transition. Its artificial later
recurrence is only a bookkeeping scalar, never an intensity entry.

## 5. Green control on this jointly stopped prefix

Use the exact centered compression and fixed-N embedded martingale of
TRACE-077 G1--G8. The same linear and remainder bounds hold with the
smaller old M threshold 1/11, since it is below 1/2. The sharper old-state estimate is ||G^c||<=12/11. Since
||Xi||<=8delta<=1/2, ||G^cXi||<=6/11 and the new inverse exists
even at the first crossing, with ||G'||<=(12/11)/(1-6/11)=12/5<3.
These estimates justify the same constants 18 and 432 at delta<=1/16. The embedded linear increment
has conditional mean zero, norm<=18delta, remainder<=432delta².
Initial compressions are bounded by ||M_N||<=1/99. Set eta_G=1/40,
beta_G=432D²/m. If 1/99+eta_G+beta_G<1/11, the Green estimate excludes
a first M exit before or simultaneously with any other first exit,
except with probability

E_G=1296 N^(2/p)(p-1)D²/(m eta_G²).                       (F12)

No future joint-admissibility event is conditioned upon. Only the old-state
stop mask appears in the martingale increments. This is the same complete
first-crossing argument, with a smaller stopping threshold.

## 6. Row and column concentration at every depth

While active, let Y_v=v R_i. On a removing transition freeze R and stop
that scalar row. The uniform-port expectation includes that case. By F6,

E DeltaY <=-Y_v/v+F_R/v, F_R=5+D²/m.

Old joint bounds imply Y_v<=L and v A_i<=1+gL. F9--F10 give

Var(DeltaY|past)<=V_R/v², V_R=3500D²[(1+g)L+1],
|DeltaY-E DeltaY|<=16D sqrt(L)/sqrt(v)+68D²/v.

After scalar deactivation continue Y_(v-1)=(1-1/v)Y_v+F_R/v.
The centered increment is then zero. Deterministic products, with
nonpositive drift slack, give for fixed u

Y_u<=F_R+(u/N)(Y_N-F_R)+weighted martingale.

The weighted variance is <=V_R/u and every increment is bounded by
c_R(u)=16D sqrt(L)/sqrt(u)+68D²/u; weights are deterministic and <=1.
The elementary conditional Taylor-series estimate and scalar Bernstein
bound derived in the concentration candidate S13--S14 give, with eta=1,

E_R=2N² exp{-1/[2(V_R/m+c_R(m)/3)]}.                       (F13)

There are N original rows and N original columns, and at most N depths.
On the complement, every retained row/column through the first joint
crossing has u R_i<=max(C0,F_R)+1<L for large N. Thus there is no first
row/column exit, including an exit simultaneous with any other crossing.

## 7. Two-step concentration at every depth, without a burn-in

The old row and column bounds together with rho<=g give
max(P_v³)<=C/v by the correct singular bound
|(P³-J)ij|<=rho sqrt[(R_i-1/v)(column_energy_j-1/v)].
For the exact frozen two-step variable (including i=j), use the
concentration candidate S1,S2 and the complete coefficient expansion.
Its sharper pointwise bound when delta<=1/16 is

|DeltaKij|<=12delta sqrt(Kij)+18delta².

Indeed the expression before using Kij<=delta in S4 has coefficients
8+16sqrt(delta)<=12 for delta sqrt(Kij), and
9+32sqrt(delta)+16delta<=18 for delta².
On the old joint bounds v Kij<=T. For Y_v=v Kij, the same frozen-endpoint
and artificial continuation as S9 gives

E DeltaY<=-(4/3)Y_v/v+F_K/v, F_K=5C+2D²/m,
Var(DeltaY|past)<=V_K/v², V_K=2600D²(T+C),
|DeltaY-E DeltaY|<=24D sqrt(T)/sqrt(v)+36D²/v.

Initial Y_N<=C0. The deterministic integrating factor gives
Y_u<=beta_K+r_(N,u)(Y_N-beta_K)+weighted martingale,
beta_K=3F_K/4. Weights <=1 imply variance<=V_K/u and increment bound
c_K(u)=24D sqrt(T)/sqrt(u)+36D²/u. For all N² ordered pairs and N depths,

E_K=N³ exp{-1/[2(V_K/m+c_K(m)/3)]}.                        (F14)

Off this exception Y_u<=max(C0,beta_K)+1<T for large N, through the full
first joint crossing for every retained pair. Hence there is no first
K exit, also when simultaneous. The diagonal extension and killed/frozen
convention must be checked as part of the proof, not hidden in a distinct-
label theorem invocation.

## 8. Entry amplitudes and exclusion of the remaining first exit

For each original ordered pair let W_v=sqrt(v) S_vij while alive. At
endpoint removal freeze Sij for that transition, then continue artificially
W_(v-1)=sqrt((v-1)/v)W_v with no noise. At a joint crossing retain the
complete actual entry if its labels remain. At an active surviving port,
the amplitude increment is q S_ie S_ej; its conditional mean is zero.
With frozen endpoint cases included, its conditional second modulus moment
is at most (P²)ij/[v(1-delta)]<=T/[v²(1-delta)].
Thus for each fixed u,

W_u=sqrt(u/N)W_N+Z_u,

where Z_u is the chronological martingale sum of the predictable-old-mask
increments sqrt(u) q S_ie S_ej. All future weights depend only on sizes.
For real and imaginary parts and either sign,

sum conditional variances <=sigma²:=16T/15,
absolute increment <=c_A(u):=2D/sqrt(u).

The first follows from u sum_(v>u)v^-2<=1 and delta<=1/16; the second
from |q|<=2 and delta<=D/v. No future endpoint-survival conditioning.
The initial deterministic term has modulus <=sqrt(C0).
For D>C0 put t=sqrt(D)-sqrt(C0)>0. A deviation |W_u|>sqrt(D) implies
one of four signed real/imaginary martingale deviations greater than
or equal to t/sqrt(2). The elementary scalar Bernstein bound gives,
uniformly over all retained entries and all depths,

E_A=4N³ exp{-t²/[4(sigma²+c_A(m)t/(3sqrt(2)))]}.            (F15a)

Off this exception no first entry exit can occur, including simultaneously
with any of the other exits, because its complete new entry would obey
|W_u|<=sqrt(D). Combine the four unconditional exceptional events by an
ordinary union bound; do not condition any proof on the other future good
events. This excludes all exits of F11 to size m. Therefore F1 holds with
failure at most

E_G+E_R+E_K+E_A.                                         (F15)

## 9. Asymptotics and exact boundary

D=K0 ell, m=ceil ell^(4+kappa). The deterministic Green remainder tends
to zero, its margin condition eventually holds, and E_G=O(ell^(-1-kappa)).
The row and K variances V_R,V_K are O(ell²), increment bounds c_R(m),c_K(m)
are O(ell^(-1-kappa/2)); their exponents grow at least as const
ell^(1+kappa/2), so E_R,E_K are superpolynomially small in N.
For the entry term c_A(m)t=O(ell^(-1/2-kappa/2)) tends to zero and
t²=D(1+o(1)). K0=32T gives t²/(4sigma²)=(15/2+o(1))ell,
so E_A=N^(-9/2+o(1)). These bounds prove the stated failure rate.

The scalar Bernstein/Freedman and Schatten smoothness mechanisms are prior.
The analytic candidate's substantive chain is row/column fourth-power
energy control -> complete P³ forcing -> all-pair P² concentration ->
entry-amplitude concentration, all using one jointly stopped prefix and
retaining every first crossing. No numerical check proves this chain.
This is an unconditional random feedback theorem with explicit initial
unitary hypotheses. It does not say deterministic chaotic spectra have
random-matrix statistics, or identify the actual microscopic reference law.

## 10. Unconditional fixed-order clocks: a named-input corollary

Set F_N(z)=z S_N and T_N=I, and retain the original independent uniform
phases and independent uniform coordinate order. Revealing one unused
phase only when its uniformly selected port is eliminated gives exactly
the feedback process above. Let kappa_clock=3+kappa. The cutoff of
[TRACE-060](conditional_clock_universality_20261011.md) is then
ceil(ell^(1+kappa_clock))=m and its entry constant is K=K0.
The conditional intersection estimate of that theorem and F1 yield,
for every fixed integer order L_clock, all its diagonal, offdiagonal and
scattering-times-clock conclusions in probability, uniformly for u>=m:

P(clock error>epsilon_N)
 <=P(A_m^c)+P(A_m intersect {clock error>epsilon_N}) ->0.

This uses the named internal TRACE-060 theorem and its full-depth
[reference measure](full_depth_clock_measure_20261011.md); the fixed
polynomial moments f_r(u/N) and empirical weak law are therefore unconditional in this deterministic-start class on the stated
retained range. No matrix Haar or freeness assumption is added.
The reference measure atom and the pathwise rank lower bound retain
the scope of the named reference source; no equality of the actual finite-N
atom weight is asserted. The proof of the upstream clock induction is
not repeated or newly certified here. This corollary does not cover every smaller logarithmic
cutoff, growing orders, the bottom u<m, edge laws or an initial physical
microscopic point process. It does not solve TRACE-005 or BGS.

## 11. Reversal channel: an additional named-input corollary

Only for this corollary assume in addition that the initial Hermitian
channel B_N has entries (B_N)ij=(S_N)ij conjugate((S_N)ji) and
||B_N||op->0. This is not a hypothesis of F1 or the clock corollary.
For each fixed g_R>0, apply [TRACE-073 C9](schur_censoring_gap_20261011.md)
with K=K0, the same m, p=2ceil ell and initial bound rho_R,N=||B_N||.
Eventually N^(1/p)rho_R,N<g_R/2, so

P(max_(u>=m)||B_u||op>=g_R)
 <=P(A_m^c)+256 N^(2/p)(p-1)K0²ell²/(m g_R²) ->0.

The adapted-port hypothesis of C9 permits the uniform ports used here;
its phase process and entry-flatness event are exactly the same. Thus the
maximum channel norm tends to zero in probability on this retained range.
The actual odd-N fixed-coupling family supplies this extra initial input
through FM-022. This is an application of the named internal C9 theorem,
not a new audit of FM-022 or a complete symmetry/microscopic classification.

## 12. Verification and priority boundary

[Independent reconstruction and actual finite scope](../archive/evidence/executions/20261013/global-feedback-flatness/README.md) preserve the raw candidate and separate
clock-hypothesis check. The maintained Green paragraph spells out the
sharper estimate supplied by the old 1/11 threshold; all constants and
theorem hypotheses are unchanged. Row/column phase identities, complete
coefficient bounds and finite weighted recurrences have independent
controls, separate from the asymptotic proof. Scalar Bernstein/Freedman
and Schatten smoothness are credited as prior structures; no world
priority, external referee certification or new Lean/C++ certificate
is asserted. The exact prior comparison is
[recorded separately](../literature/stopped_feedback_concentration_prior_20261013.md).
