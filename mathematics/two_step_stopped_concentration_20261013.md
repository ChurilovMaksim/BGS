# Simultaneous stopped two-step concentration

**Stable claim:** BGS-TRACE-079. **State:** PROJECT PROOF + INDEPENDENT
INTERNAL RECONSTRUCTION, 13 October 2026. It does not estimate early entry survival
or prove a deterministic microscopic law, TRACE-005 or BGS.

## 1. Exact one-step inputs, including diagonal endpoints

Let S in U(v), P=|S|², K=P², delta=max P<=1/16. The next port is
conditionally uniform among all v labels, then an independent uniform
circle phase is generated. For labels i,j, now ALLOW i=j. If e is in
{i,j}, freeze K'ij=Kij for this transition. Otherwise use the survivor
unitary S'kl=Skl+q S_ke S_el, q=w/(1-S_ee w), and compute K'ij
on the remaining labels.

The following three bounds hold:

E DeltaK <=[-Kij/2+5(P³)ij+2delta Pij]/v,                   (S1)
E (DeltaK)² <=2600delta²[Kij+(P³)ij]/v,                    (S2)
|DeltaK| <=32delta^(3/2) for every port and phase.           (S3)

For distinct i,j, S1 and S2 are precisely TRACE-075 and TRACE-078.
Here is the extra diagonal check, rather than invoking their distinct-label
statements outside scope. In the exact average (075 (10)), replace the
excluded two-element set with the one-element set {i}. The base decrement
becomes -Kii+Pii² <=-Kii+2delta Pii, instead of
-Kij+Pij(Pii+Pjj). Every other estimate (075 (13)--(20)) is a subsum of
the same full nonnegative sums and applies with j=i. The path swap need
not preserve the truncated domain, just as in the original proof.
Thus the same c(delta),d(delta) and their delta<=1/16 bounds give S1.
For S2 all six coefficient squared sums in 078 are unchanged when j=i.
The omitted linear coefficient remains 2S_ee P_ie P_ei; the algebraic
port extension and the row/column Parseval bounds still hold. Only the
single frozen port is removed from the nonnegative port sum. Uniform
selection still divides by v, not v-1.

To prove S3 use the six coefficients of 078 V2. At a surviving port,
with the sums over k!=e, direct Cauchy gives

|A_e|<=2delta sqrt(Kij),
|B_e|<=2delta²+2delta sqrt(delta Kij),
|C_e|<=delta sqrt(delta Kij),
|D_e|<=2delta^(5/2), F_e<=delta³, r_e<=delta².

For example the first component of A is bounded by
sqrt(P_ie)*sqrt(sum P_kj² P_ik)*sqrt(sum P_ek)
<=delta sqrt(Kij); the second uses columns. The D bounds use
|D1_e|²<=delta P_ie P_ej² K_ie<=delta^5, and likewise D2.
Since |q|<=2, V2 gives

|DeltaK|<=9delta²+8delta sqrt(Kij)+16delta^(3/2)sqrt(Kij)
          +32delta^(5/2)+16delta³
 <=delta^(3/2)[8+25sqrt(delta)+32delta+16delta^(3/2)]
 <=(61/2)delta^(3/2)<=32delta^(3/2),                         (S4)

using Kij<=delta and delta<=1/4. Frozen ports have DeltaK=0.

## 2. General finite-size stopped theorem

Fix integers b>m>=3, real D>0,C>0, with m>=16D. Start with any deterministic
unitary S_b satisfying delta_b<=D/b and max(P_b³)<=C/b. Original b labels
are kept throughout the process. At size v choose a uniform retained
port and a fresh independent uniform phase, eliminating it. Stop globally
at the first full new state with

delta_u>D/u or max(P_u³)>C/u.                               (S5)

Include the whole first-crossing transition, including simultaneous
crossings. All transitions through it exist: the old state has
|S_ee|<=sqrt(D/v)<=1/4. For any ordered original pair (i,j), allow i=j,
and stop its scalar process additionally when either endpoint is removed.
On that removing transition set K'=K as above; this is a scalar convention,
not an entry of a nonexistent retained matrix.

Define

a=4/3, F=5C+2D²/m, beta=F/a,
V=2600D²(D+C), R=64D^(3/2),
r_(b,u)=product_(v=u+1)^b(1-a/v).

For every eta>0, the probability that any surviving ordered pair at any
size b>=u>=m through the first global crossing violates

u(P_u²)ij <= beta + D r_(b,u) + eta                         (S6)

is at most

b³ exp{-eta²/[2(V/m+R eta/(3sqrt(m)))]}.                    (S7)

The bound is unconditional for this stopped prefix. Diagonal pairs are
included. It may exceed 1, in which case it is simply a valid upper bound.
It makes no assertion about matrices after the first global crossing.
The transient factor obeys

r_(b,u)<=[(u+1)/(b+1)]^(4/3).                               (S8)

The same theorem holds conditionally on any revealed admissible random
starting state and labels. No future survival event is conditioned upon.

## 3. Scalar processes and their conditional bounds

For each original ordered pair let Y_v=v Kij while that pair is alive and
the global stop has not occurred. At a removing transition use
Y_(v-1)=(v-1)Kij, then deactivate that pair. At a global crossing use the
full actual new K if endpoints survive, then deactivate. After deactivation
continue an ARTIFICIAL scalar recurrence

Y_(v-1)=(1-a/v)Y_v+F/v.                                    (S9)

This is only a bookkeeping scalar, never a claim about later intensities.
If the pair is active at the old state, its old Y_v<=D, and
DeltaY=(v-1)DeltaK-Kij. S1 gives

E DeltaY<=-[(3/2)-1/(2v)]Y_v/v+5C/v+2delta²
          <=-aY_v/v+F/v.                                  (S10)

S2 and S3 give

Var(DeltaY|past)<=(v-1)²E(DeltaK)²
               <=2600delta²[Y_v+C]<=V/v²,
|DeltaY-E DeltaY| <=64v delta^(3/2)<=R/sqrt(v).              (S11)

These bounds are for conditional expectation before the fresh port and
phase. Endpoint-removal randomness is included. Deactivated increments
in (S9) are deterministic given the past, so their centered increment is
zero and the same inequalities hold. Activity at the old state is a
predictable mask. The full first crossing is not discarded or clipped.

Let xi_v=Y_(v-1)-E[Y_(v-1)|past]. There is a predictable nonnegative
slack epsilon_v such that

Y_(v-1)=(1-a/v)Y_v+F/v+xi_v-epsilon_v.

For each FIXED final size u, deterministic products telescope. Since all
coefficients 1-a/v are positive,

Y_u<=beta+r_(b,u)(Y_b-beta)+sum_(v=u+1)^b w_(v,u) xi_v,
w_(v,u)=product_(r=u+1)^(v-1)(1-a/r), 0<w<=1.              (S12)

Y_b<=D gives S6 outside a positive deviation eta of this weighted sum.
The weights depend only on sizes; no future random projection or label
choice appears inside martingale increments. For fixed u it is a scalar
martingale in chronological elimination time, with total predictable
variance at most V/u and increment bound R/sqrt(u), by S11 and
sum_(v=u+1)^b v^-2<=1/u.

## 4. Elementary exponential estimate, derived here

For a real centered conditional increment X with |X|<=c, lambda>=0 and
lambda c<3, the Taylor series and k!>=2*3^(k-2) for k>=2 give

E[exp(lambda X)|past]
 <=exp{lambda² E[X²|past]/[2(1-lambda c/3)]}.                (S13)

Indeed absolute values bound each term of order k>=2 by
lambda^k c^(k-2)E X²/k!; conditional centering removes order one.
For a finite martingale with deterministic upper bounds sigma² on total
predictable variance and c on all increments, iterating S13 gives the
usual exponential-supermartingale bound. Markov with
lambda=eta/(sigma²+c eta/3) yields

P(sum X>=eta)<=exp{-eta²/[2(sigma²+c eta/3)]}.              (S14)

Use sigma²=V/u,c=R/sqrt(u) for the fixed weighted sum in S12. Take a union
bound over at most b² original ordered pairs and at most b depths, and
replace u>=m by m. This proves S7, without conditioning on later stops.
For S8, use log(1-a/v)<=-a/v and
sum_(v=u+1)^b1/v>=log[(b+1)/(u+1)]. Empty products at u=b cause no problem.
All scalar moments are finite because the active increments are bounded
and the bookkeeping continuation has finite deterministic length.

## 5. Combination with the Green-prefix theorem

Let S_N deterministic unitary, max|S_Nij|²<=C0/N with fixed C0>=1 and
rho_N=||P_N-J_N||<=1/5. Feedback ports are now uniform, phases fresh
uniform. Let ell=log(2N), fixed K0>0,kappa>0,
m=ceil ell^(7+kappa), b=floor(N/ell²), d=floor(b/ell).
Stop only at the first entry exit delta_u>K0 ell/u, keeping its full state.
For sufficiently large N all numerical hypotheses of TRACE-077 hold.
Its good event has failure O_(K0)(ell^-kappa). On this event, every reached
old entry-admissible size m<=u<=b has rho_u=O_(C0,K0)(ell^-2) and hence

max(P_u³)<= [1+rho_u(K0 ell-1)]/u<=2/u.                    (S15)

If the entry prefix does not reach b, the following conclusion is vacuous.
If it reaches an admissible b, define the past-measurable startup event Gamma_b by reaching b without
entry exit and satisfying BOTH delta_b<=K0 ell/b and max(P_b³)<=2/b.
Apply S6--S7 with D=K0 ell,C=2 to the process starting there, conditional
only on the past through b and on Gamma_b. The bound is uniform in that
starting matrix and its retained labels. Integrating this conditional bound
costs no inverse probability of Gamma_b.

Importantly, do NOT condition the martingale argument on the future
Green good event. Instead run the additional P³ stopping rule of S5, prove
S7, and combine its failure event with the Green failure by an ordinary
union bound. On the Green good event there can be no P³ exit before an
entry exit. Simultaneous entry/P³ exits are allowed and included. Thus the
core estimate applies through the entry crossing, provided b was reached
before it; it gives bounds only for pairs still present in the new state.

Now beta=15/2+o(1), eta=1 and, uniformly u<=d,
D r_(b,u)<=K0 ell[(d+1)/(b+1)]^(4/3)=o(1).
The S7 probability is at most

N³ exp{-1/[2(V/m+R/(3sqrt(m)))]},
V=2600(K0 ell)²(K0 ell+2), R=64(K0 ell)^(3/2),

which is superpolynomially small in N: its exponent grows at least as a
positive constant times ell^(2+kappa/2), faster than log N.
Therefore, except with probability O_(C0,K0,kappa)(ell^-kappa),

max_(i,j retained) (P_u²)ij <=9/u                           (S16)

simultaneously on every reached size m<=u<=d through the first entry
crossing, including that crossing if its depth lies in the range. All
ordered pairs, including the diagonal, are covered. No matrices after
that crossing, no probability of reaching b and no all-time flatness
conclusion are asserted.

The maintained fixed-coupling odd-N map supplies only the named eventual
initial conditions through FM-021 and initial WKB flatness. There is no
effective startup, deterministic spectral identification, TRACE-005 or BGS
conclusion. The scalar Bernstein/Freedman mechanism is prior; no priority
claim or external referee/formal certification is made.

## Review and exact verification scope

[Independent reconstruction and finite controls](../evidence/executions/20261013/stopped-concentration/README.md) preserve the frozen raw candidate. The maintained
version clarifies that Gamma_b contains both startup barriers; this was
already required by the stated finite theorem. Exact root controls check
three unitary-pair phase integrals, including two diagonals, and deterministic
weighted recurrences under three scalar stopping conventions. These do not
prove the analytic concentration theorem. The scalar Bernstein/Freedman
inequality is prior; [primary-source comparison](../literature/stopped_feedback_concentration_prior_20261013.md). No new Lean/C++ certificate is asserted.
