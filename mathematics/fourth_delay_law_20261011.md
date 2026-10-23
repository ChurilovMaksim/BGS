# Fourth delay law and concentration of the diagonal squares

**Stable claim:** BGS-TRACE-060, further conditional extension.
**State:** CONDITIONAL on the all-time entry-flatness event below.
**Review:** independent internal reconstruction completed on 11 October 2026,
from main `b126cfb18f445b82358fc156632873082ac22503`. This proof reconstructs
the preserved 8 October derivation. It is not an unconditional clock law,
a microscopic eigenphase law or a solution of BGS. World priority is not
established; the endpoint numbers are known in the random-matrix delay model.

Use the exact process of [the first bootstrap](delay_bootstrap_20261011.md)
and the killed hierarchy of [the all-fixed-moment proof](all_moment_delay_bootstrap_20261011.md).
The [review packet](../archive/evidence/executions/20261011/fourth-delay/README.md)
fixes the input, reconstruction and finite-control scope.

## Claim and scope

Use the fresh independent phase and uniform-coordinate Schur process fixed in those two proofs. Initially T_N=Q_N=I, and Q_u=S_u T_u S_u*. Fix kappa>0, ell=log(2N), m=ceil(ell^(1+kappa)), m<N. Let A be all-time entry flatness max |(S_u)_ij|²≤K ell/u for u≥m.

The claim is that, there is a deterministic epsilon_N tending to zero such that the probability of a violation of any following uniform bound by more than epsilon_N, intersected with A, tends to zero:

max_(j alive,u≥m) |u²(T_u²)_jj/N²−(2−u/N)|≤epsilon_N,
max_(j alive,u≥m) |u²(Q_u²)_jj/N²−(2−u/N)|≤epsilon_N,

and uniformly for u≥m,

u Tr T_u²/N² = 2−u/N+o(1),
u² Tr T_u³/N³ = 6−6u/N+(u/N)²+o(1),
u³ Tr T_u⁴/N⁴ = 22−32u/N+12(u/N)²−(u/N)³+o(1).           (1)

In particular the fourth normalized clock tends to 22 at a polylogarithmic endpoint, on this high-probability intersection. If P(A^c)→0 is separately established, these are convergence-in-probability statements for the actual process. Corresponding killed moments are uniformly integrable by the all-fixed-moment bounds, so their expectations then have the same limits. No all-time entry-flatness probability, full delay distribution, scalar CUE law, or deterministic BGS is supplied by this claim.

## 1. The holomorphic cross-clock is a compressed martingale

Put Gamma=S T. The exact relations S' K*=J* S and T'=K*TK give S'T'=J* Gamma K. For surviving j,k,

Gamma'_jk=Gamma_jk+q[S_je Gamma_ek+S_ek Gamma_je]+q² S_je S_ek Gamma_ee.       (2)

Thus E_w Gamma'_jk=Gamma_jk because E q=E q²=0. This identity is exact for arbitrary noncommuting S,T and for nonzero S_ee.

Normalize g_jk=u Gamma_jk/N and freeze a pair when either label is deleted, retaining the full crossing state at the global stop. Its conditional drift is −(u-r)g_jk/u², r=|{j,k}|. It has no forcing. On the joint first-diagonal and p-th clock cap, its complex centered increments, including the complete crossing step, have

jump≤C sqrt(ell/u),
conditional second moment≤C ell B_u^(1/p)/u^(2−1/p).     (3)

For the latter, use sum_e |Gamma_ek|²=(T²)_kk and sum_e |Gamma_je|²=(Q²)_jj; the q² term is bounded using |Gamma_ee|²≤T_ee Q_ee and entry flatness. Real and imaginary parts satisfy the same bounds.

Apply blockwise Freedman to the at most v² pairs alive at the start of a block, exactly as in all_moment_delay_bootstrap.md. The number v² only changes a fixed log coefficient. The negative diagonal drift does not amplify the noise. With B_u=B(u/m)^zeta and 0<zeta<p−1 this gives a size-dependent bound

max_jk |g_jk(u)|≤g(u),
g(u)=C[sqrt(K ell/N)
 +sqrt(ell B^(1/p) m^(−zeta/p) log(2u)/u^((p−1−zeta)/p))
 +sqrt(ell/u) log(2u)].                                (4)

Constants can be enlarged to cover truncated dyadic blocks. The sum of earlier block costs is bounded by the same expression; u-dependent powers decay geometrically. Pair freezing applies only to the coordinates that cease to be live. The mean drift need not be used inside a future-dependent martingale transform.

## 2. Exact diagonal-square phase identity

Write a=S_ee, d=1−|a|², t=T_ee, and gamma=Gamma_ee. For j≠e,

E_w (T'^2)_jj=(T²)_jj
 +[|S_ej|²(T²)_ee+2t Re(conj(S_ej)Gamma_ej)]/d
 +2|S_ej|² t Re(conj(a)gamma)/d².                      (5)

A direct expansion gives the complete polynomial, with b=S_ej and h=T_je:

(T'^2)_jj=(T²)_jj+2 Re[q b (T²)_je]+|q|² |b|²(T²)_ee
 +2 Re[q h Gamma_ej+q² h b gamma
        +|q|² conj(b) t Gamma_ej+q|q|² |b|² t gamma].    (5a)

Here gamma=Gamma_ee. To average (5a), use E q=E q²=0,
E|q|²=1/d and E[q|q|²]=conj(a)/d². Sum_j≠e (5) to recover exactly E TrT'^2=TrT²+2ts/d, an internal consistency check. The outgoing formula follows by replacing S with S*, T with Q and Gamma with Gamma*: the conjugated feedback phase is still uniform.

For x2_j=u²(T²)_jj/N², averaging a uniformly selected e and freezing j on deletion gives drift

A2 x2 + 2 k2 x1 + error,
k2=(u−1)²/u³,
(A2 x2)_j=d0 x2_j+k2 sum_(e≠j) c_ej x2_e,
d0=−2/u+3/u²−1/u³,
c_ej=|S_ej|²/(1−|S_ee|²).                              (6)

If x1_j=uT_jj/N is within epsilon1 of 1, then on a fixed diagonal-square cap (say x2≤3), the absolute error in (6) is at most

C[epsilon1+delta_u+sqrt(delta_u)g(u)]/u.

For the main coherent sum use sum_e conj(S_ej)Gamma_ej=T_jj and Cauchy–Schwarz; replacing T_ee by N/u costs at most epsilon1 sqrt((T²)_jj)N/u before normalization. Denominator errors cost delta_u. The omitted e=j term and the final term of (5) cost sqrt(delta_u)g(u).

The nonnegative homogeneous update I+A2 has each live-row sum at most 1−c/u for sufficiently large N: its exact reference sum is 1−1/u+1/u², with error O(delta_u/u). Frozen rows are identity rows. The reference f2(u)=2−u/N is frozen at its old value if its label is
eliminated. Its conditional increment is (u−1)/(uN), rather than 1/N.
With nominal transport row sum one, its exact drift residual is

(d0+k2)f2(u/N)+2k2−(u−1)/(uN)=−2/u²+2/u³.             (6a)

Thus the residual is O(1/u²), including the random reference freeze.

A constant supersolution therefore absorbs the bounded drift error at cost O(epsilon1+delta_*+sqrt(delta_*)g(m)+1/m), rather than accumulating it over log(N/m). This is a pathwise maximum principle on the fixed set of labels, with rows turned off only after the transition deleting them.

## 3. The diagonal-square noise closes

The joint stop includes the first violation of the deterministic Gamma
envelope (4), the first diagonal-square deviation, the first-delay and p-th
moment caps, and flatness. Before this stop x2 and its outgoing counterpart
are bounded by 3. The estimates below are deterministic bounds conditional
on the past. They are not conditioned on the future Gamma good event. Expand the polynomial K* T (KK*) T K without assuming independence of its terms. The potentially unsuppressed term is q T_je Gamma_ej. Its normalized conditional variance is at most C g(u)²/u by (4). Every T²_je term has a factor S_ej; using

(T⁴)_jj≤||T||²(T²)_jj≤C N⁴ B_u^(2/p)/u^(4−2/p)

gives the remaining bound

E[xi2_(u,j)² | past]
 ≤C[1/u²+ell B_u^(2/p)/u^(2−2/p)+g(u)²/u],
|xi2_(u,j)|≤C[sqrt(ell/u)+g(u)].                        (7)

Terms containing q² or q|q|² are bounded by the same quantities using |q|≤2, |T_je|²≤T_jjT_ee, and (4). The variance also includes coordinate selection and the frozen reference increment; both are O(1/u²) on the stopped state.

Choose fixed zeta=1/4, p sufficiently large compared with 1/kappa, B=ell^(kappa/64), epsilon1=ell^(−kappa/64). A permissible example is p−1>64(1+kappa)/kappa. The all-moment proof remains valid with these parameters. Apply Freedman conditionally on each starting block to at most 2v live diagonals. The total endpoint noise cost from (7) is at most

C[sqrt(ell B^(2/p) log(2m)/m^(1−2/p))
  +g(m)log(2m)+sqrt(ell/m)log(2m)] = o(ell^(−kappa/128)).  (8)

Initial x2=1=f2(N). The supersolution and blockwise pathwise noise propagation imply the first two statements in (1), with tolerance ell^(−kappa/128), outside the cap and martingale exceptional events. All processes include their crossing state; additional stops only lower the killed high moments used for the variance bounds.

## 4. Global trace-moment noise and deterministic curves

For each fixed k≤4, before the joint stop, a rank-word expansion and moment interpolation give

E[|centered normalized trace increment|² | past]
 ≤ C_k[1+M_(2k−1)(u)]/u².                              (9)

One way to check (9) is to square each cyclic word before applying the same positivity/weighted-AM–GM bound used for (4) in all_moment_delay_bootstrap.md. Normalize H=uT/N, whose first incoming and outgoing diagonal moments are bounded. A product of spectral moments of total degree at most 2k can then be bounded by one first moment and a moment of order at most 2k−1; averaging the selected e produces the normalized M_(2k−1). The deterministic scaling part contributes M_k²/u²≤A0 M_(2k−1)/u² by scalar moment interpolation.

For a frozen trace martingale the killed hierarchy bounds the EXPECTED
sum of predictable variations by C_k/m, since only survival before the
transition appears. The crossing value is frozen permanently with its
crossing normalization. Scalar Doob L2 gives E(max partial noise)^2≤4C_k/m;
no deterministic variation bound is inferred from this expectation.
Auxiliary stops M2≤4, M3≤10, M4≤30 close by the stable equations below,
including the complete first crossing and simultaneous exits. In (9) the
fourth trace needs only the killed seventh moment.

The exact square identity, first-diagonal barriers and delta_*=K ell/m→0 give the stable trace equation

E M2(u−1)=(1−1/u) M2(u)+2(u−1)/u²+O((epsilon1+delta_*)/u).

Its reference curve is f2(r)=2−r up to O(1/u²) residual. The exact cubic identity gives

E M3(u−1)=((u−1)/u)² M3(u)
 +6(u−1)²/u³ M2(u)+O((epsilon1+sqrt(delta_*))/u),

on the additional bounded lower-trace stops. Its reference is f3(r)=6−6r+r², again up to O(1/u²).

For the fourth moment first set a=0 (then q is a uniform phase). The exact phase average is

E_w Tr(T'^4)=Tr(T⁴)
 +4[t(Q³)_ee+(T²)_ee(Q²)_ee+s(T³)_ee]
 +2t²s²+4ts|Gamma_ee|².                               (10)

This follows by expanding Tr[(T(I+qev*+conj(q)ve*))⁴]. Quadratic balanced words give the three displayed products. Among the six words with two factors of each orientation, two are alternating and four have identical neighbors, giving respectively 2t²s² and 4ts|Gamma_ee|². Odd mixed words average to zero.

For completeness the exact nonzero-a average is also available. Put
tr=(T^r)_ee, sr=(Q^r)_ee, t=t1, s=s1, gamma=(ST)_ee,
beta=(ST²)_ee. Direct cyclic expansion and phase integration give

E_w Tr(T'^4)=Tr(T⁴)+4(t s3+t2 s2+s t3)/d
 +8 Re[conj(a){gamma(s t2+t s2)+ts beta}]/d²
 +(1+|a|²)(2t²s²+4ts|gamma|²)/d³
 +8ts Re[conj(a)² gamma²]/d³.                          (10a)

The quadratic balanced words give the first correction. The cubic words
use E[q² conj(q)]=conj(a)/d²; the balanced quartic words use
E|q|⁴=(1+|a|²)/d³; the remaining quartic orientations use
E[q³ conj(q)]=conj(a)²/d³. Linear terms have exactly zero mean and
therefore do not introduce an uncontrolled fourth-power coefficient.

At nonzero |a|≤sqrt(delta_*), balanced phase moments differ from their a=0 values by O(delta_*), and fixed-degree unbalanced moments are O(sqrt(delta_*)). The fixed-word bounds make the normalized increment error O(sqrt(delta_*)/u) on the bounded lower-trace stops. Equation (4) makes the final term in (10) negligible. The uniform diagonal-square law makes the average product (T²)_ee(Q²)_ee equal (N/u)^4[f2(u/N)²+o(1)]. First-diagonal barriers identify the other products. Consequently

E M4(u−1)=((u−1)/u)³ M4(u)
 +(u−1)³/u⁴ [8 M3(u)+4f2(u/N)²+2+o(1)].                (11)

Its reference f4(r)=22−32r+12r²−r³ satisfies

−r f4'(r)=−3f4(r)+8f3(r)+4f2(r)²+2,  f4(1)=1.

The stable scalar comparison for (11), the trace-noise bounds, and the closed lower moments prove the final statement in (1).

## Proof and execution boundaries

The separate internal reviewer reconstructed the full Gamma compression,
(5a) and (10a) at nonzero a, the frozen-reference residual, the deterministic
pre-exit variance bounds, the live-pair dyadic union, the closed auxiliary
caps and the fourth trace comparison. The upstream killed-moment argument
was used with its maintained review boundary; it was not reaudited in full.

The finite verifier now evaluates phase moments by exact residues and checks
Gaussian-rational unitary examples with nonzero deleted diagonals, in addition
to its preceding energy and word-bound controls. The execution packet states
what was actually run. A separately executed historical C++ verifier checks
only its zero-diagonal examples; it is not advertised as checking (10a).
There is no new Lean formalization of this stochastic argument.

The sequence 1,2,6,22,90,... is a prior random-matrix proper-delay sequence;
see [the exact source comparison](../literature/cavity_sources_20261011.md).
The project proof concerns this conditional random-Schur process. Neither
that comparison nor the number 22 is a novelty claim. The later [all-fixed-order proof](conditional_clock_universality_20261011.md)
closes the equality induction after two substantive word repairs. P(A^c),
the physical microscopic cavity law, signed TRACE-005 and deterministic BGS
remain unresolved. This fourth-order proof retains its narrower standalone scope.
