> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_consolidated_report_audit.md`. Embedded SHA256: `19a23492cd0c34fa4db2832ee9320a1866692a5656042327b42ee3255727057c`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the consolidated spectral report

Date: 20 October 2026.

## 1. Versions and scope

The complete Sections 1--12 of Spectral_partial_results_2026-10-20.md
were read, initially at SHA-256
ede6b821a33f8a2862ee66cace7daf788076a51a82d48fa02046d9dcd61363c7,
and then with the added exact-sector bridge, finite shell theorem,
probability details, and explicit range at report (10.1), at the final
SHA-256
b8c5e2071d49394270006853ee8316f3900e84f1a7ae9b03e58e5c4eaf29a7cc.

**Verdict on the mathematical formulas: PASS in their stated ranges.**
The final requested range clarification has been incorporated:
report (10.1) is stated uniformly for $1\le m\le2N$,
or more generally $m\le BN$ with fixed $B$. The expansion of its
quantum error is not asserted at unbounded multiples of $N^2$.
This clarification does not change (10.2) or (10.3).

The following small clarifications found during this audit were
already incorporated in the second version:

- The detector visibility consequence in Section 9 is for sufficiently
  large $N$. The endpoint cyclicity theorem itself has its original
  all-odd-$7\nmid N$ range. The critical detector has a zero-dimensional
  window at $N=3$, so these two ranges must not be conflated.
- The exponentially decaying part after (10.1) is the classical error;
  the quantum error is the separately displayed $O(m^2/N^2)$.
- The weighted scalar product in (7.11) has been defined explicitly.
- The last passage from smooth Laplace tests to laws of point measures
  has been supplied through local tightness and uniqueness.

This audit verifies the report's use and combination of the detailed
proof inputs. It does not replace those inputs by assertions that
they are known, and does not certify $H_{\rm diag}$. The report
continues to state that neither the desired limit nor its negation
has been proved.

## 2. Exact pair test and the modular symbol

The fixed test is normalized consistently:
$$
 b_*(x)=|g(x)|^2/(2I^2),\qquad
 \phi(\xi)=e^{-1/(1-\xi^2)}1_{\{|\xi|<1\}},\quad
 g=\mathcal F^{-1}\phi,\quad I=\int\phi.
$$
The elementary bound $|g|\le I$ gives $\sup b_*\le1/2$.
The function is Schwartz and its Fourier transform is
$(\phi*\phi)/(2I^2)$, smooth and supported in $[-2,2]$.
It is positive in the interior of that Fourier interval.

For $m\ne0$, the distinct-index expression is
$|p_m|^2-N$. The $m=0$ terms agree between the given
matrix and CUE. The two ordered frequencies $m,-m$
cancel the factorial factor $1/2$. Therefore report (1.1)
has exactly the coefficient $N^{-2}$, with no extra factor
of two.

The CUE benchmark follows directly from its projection
kernel:
$$
 \mathbb E|\operatorname{Tr}V_N^m|^2
 =N-(N-m)_+=\min(m,N),\quad m\ge1.
$$
The zero Fourier mode has expectation $N^2$, and is handled
separately in the report.

The ordinary Weyl symbol includes the half-period shift of
$r$ in the momentum-dependent term. This is precisely the
sign $(-1)^{kl}$ from replacing the modular inverse of two
by a real half; it is not a modification of $A_N$.

At $z_*=(1/2,0)$, the reported nilpotent linearization,
$$
 D\Psi(z_*)=
 \begin{pmatrix}
 3&-4\\-2+3\tau\sigma&3-4\tau\sigma
 \end{pmatrix},
 \qquad \sigma=(12153/125)\pi,
$$
has determinant one and trace
$6-(48612/125)\pi\tau$.
Its multiplier and slope difference in (2.3) are consistent
with the off-diagonal entry $-4$. No real-fraction
replacement of a modular phase is made in this calculation.

## 3. What is exact in the orbit formula

The report distinguishes three objects:

1. the exact quantum trace $p_{m,N}$;
2. the exact principal scalar cocycle sum $\mathcal P_{m,N}$;
3. the residual $\mathcal E_{m,N}$, with
   $|\mathcal E_{m,N}|\le2(0.421)^m$.

Thus its use of an exact orbit formula does not silently
identify $p_{m,N}$ with its principal part.

For the detailed connection back to the exact sectors, the
complete additional input
arithmetic_exact_sector_three_cell_bridge_audit.md was read
at SHA-256
b7cf3ce194cffd8dac98ac85af5b9dcf9dbfbf8aaadd4d2089b8876088b539a7.
Its ordering of estimates is appropriate: the finite-iterate
sector identity is exact for each $(m,N)$, and only the
one-edge transverse contraction supplies the uniform error.
Bounds that may grow during the intermediate word expansion
are not used as uniform remainders.

The one-edge constants in the bridge give
$$
 |\mathcal E_{m,N}|
 \le\frac{.209}{.174}(.174\sqrt{3+2\sqrt2})^m
 <2(.421)^m.
$$
The lower bound for the scalar product is
$|\Gamma_h|\ge.9998^m$. These are the constants actually
used in the selected-sector transfer.

The principal Euler product satisfies
$$
 \log\mathcal Z_N=-\sum_{m\ge1}\mathcal P_{m,N}z^m/m,
 \qquad
 \log\det(I-zU_N)=-\sum_{m\ge1}p_{m,N}z^m/m
$$
near zero. Consequently
$$
 G_N(z)=\sum_{m\ge1}\mathcal E_{m,N}z^m/m,\qquad
 \mathcal Z_N=\det(I-zU_N)e^{G_N}.
$$
The sign of $G_N$ and the bound
$|e^{G_N(z)}|\le(1-.421|z|)^{-2}$ are correct.
A chosen subset of Euler terms is not transported through
this analytic convolution in the report.

## 4. The signed three-cell profile

The two independent length intervals have widths $m/24$
and $m/12$. Their integer count is
$m^2/288+O(m)$. The third interval is disjoint from both
for sufficiently large $N$, because $R_N=O(\log N)$.

The pointed pair factor is $2m^2$, not $m^2$ or $2m^3$:
two ordered directions and $m$ equal starting-point weights
on each primitive geometric orbit. The marker anchoring and
distinct length bands remove code rotations from the counting.
The same conditions imply primitivity.

For $x_N=N\Lambda^{-2R_N}$ in its fixed positive compact
interval, the endpoint comparison has uniformly bounded
rescaled Fourier frequency. The action difference is obtained
after stationary elimination; the shared cell action
constants cancel before summation. The error in that phase
is $o(1)$. The localized cocycle comparison has no factor
$m$ multiplying its endpoint error.

The renewal formula retains its noncommuting order:
$$
 (I-z^dJ^d)
 (I-zT+z^{d+1}(T-J)J^d)^{-1}.
$$
It gives the survival factor with the stated pole correction.
The endpoint laws are derived from finite cylinder areas,
not by conditioning on an infinite zero tail of probability zero.

The physical area constant is $c=\chi|I_S||I_U|$.
The probability Gram operator obeys
$$
 K_{2\pi\chi x}\simeq(cx)^{-1}\mathsf S_{cx}.
$$
In particular the length of the sine interval is $cx$;
there is no extra factor $2\pi$.

Combining the positive mass $c^3\varepsilon_N^3$, the
length count, the pointed factor, and
$\operatorname{Tr}K^3=(cx_N)^{-3}\operatorname{Tr}\mathsf S_{cx_N}^3$
gives
$$
 \frac{m^4}{144N^3}
 e^{-\kappa m\varepsilon_N}
 \operatorname{Tr}\mathsf S_{cx_N}^3.
$$
This verifies $1/144=2/288$, including the cancellation of
$c^3\varepsilon_N^3$ against $(cx_N)^3$.

Uniform $o(N)$ in the time band becomes $o(1)$ after the
weighted sum and division by $N^2$. Although $x_N$ need
not converge, it remains in a fixed compact interval;
the associated Riemann sums are uniform there.

## 5. The new exact-sector bridge

The exact primitive-sector weight $\widetilde u_p$ contains
the full transverse trace. The principal weight $u_p$
contains its scalar cocycle. Their relative difference is
$$
 \left|\frac{\widetilde u_p}{u_p}-1\right|
 \le C_0q_0^m,\qquad
 C_0=.209/.174,\quad q_0=.174/.9998<.175.
$$
The denominator is nonzero by $|\Gamma_h|\ge.9998^m$.

This relative estimate alone is not enough for a selected
double sum; the report correctly supplies the additional
absolute-mass bound. At fixed lengths, positivity permits
replacement of the three avoidance operators by unrestricted
powers of $T$. The six zero buffers give
$\Lambda^{-6R_N}=\varepsilon_N^3$. Open and periodic
weights have a bounded ratio by summable variations.
Cauchy--Schwarz and the modulus formula then give
$$
 \sum_{\text{fixed lengths}}|u_{123}u_{132}|
 \le C\varepsilon_N^3.
$$
After the length count and the factor $2m^2$, the entire
selected absolute mass is $O(m^4\varepsilon_N^3)=O(N)$.

It follows that the difference of the exact and principal
selected contributions is at most $CNq_0^m$.
This is a genuine transfer to a subset of the original
squared sector trace.

The report does not assert multiplicativity of full
transverse weights under repetitions. It explicitly
distinguishes $\operatorname{Tr}(K_p^r)$ from
$(\operatorname{Tr}K_p)^r$; the selected family only
uses primitive period $m$.

## 6. Six connections and between-class cancellation

For three labeled cells the Euler sign equals minus the
permutation sign. Among the 36 ordered pairs of permutations,
there are 6 identity relatives, 18 transpositions, and 12
three-cycles. The full local determinant square has expectation
$36e_3(K)$. Subtracting its diagonal $6$ gives
$$
 -18\operatorname{Tr}K^2+12\operatorname{Tr}K^3.
$$
This is strictly negative because $K\ge0$,
$\operatorname{Tr}K=1$, and
$0<\operatorname{Tr}K^3\le\operatorname{Tr}K^2$.
There is no pointed factor $m^2$ in these Euler coefficients.
The corresponding weight has order $N^{-1}$, as stated.

Section 6 uses a different complete coefficient functional.
Removing the zero orbit divides its positive generating
function by $1+\Lambda^{-1}z$, leaving limiting mass
$C_-=e^{H_F(1)}/(1+\Lambda^{-1})>0$.
The union bound for at least one marker is
$C_Bm\varepsilon_N$; no additional period factor is inserted
after the pointed marker count.

On $|z|=2$, unitarity gives
$$
 |\det(I-zU_N)|
 \le2^N\exp\left(\sum_{d\ge1}|p_{d,N}|/(d2^d)\right).
$$
The fixed exponential trace bound makes this last exponent
$o(N)$. Both the scalar correction and the removed zero
orbit factor are uniformly bounded there.
Cauchy's estimate gives $2^{N-m}e^{o(N)}$, exponentially
small uniformly for $m\ge6N/5$.
The diagonal mass of singleton marker-free classes remains
positive after choosing a sufficiently large fixed $R_0$.
The exact identity then forces a negative between-class sum.

The report confines this conclusion to that coefficient
functional and fixed marker offset. It does not apply it
to frequent markers or infer a failure of $H_{\rm diag}$.

## 7. Exact quantum returns and their constants

The colligation in Section 7 is unitary. Its two defects are
$I-DD^*=E$ and $I-D^*D=U^*EU$. The visible subspace is
reducing, while the orthogonal dark subspace is unitary
under $D$. No uniform decay rate is needed for telescoping
at each fixed $N$.

The two energy sums and the mixed identity
$$
 \sum_{m\ge1}m\operatorname{Tr}(F_m^*F_{m+k})
 =\operatorname{Tr}(D^k|_{\rm seen})
$$
have the correct ordering. Absolute convergence follows from
the weighted Hilbert--Schmidt Cauchy--Schwarz bound displayed
in the report.

For an invertible contraction with eigenvalue moduli
$e^{-d_j}$, positivity of the scalar Poisson kernel yields
the diagonal lower bound $\sum_j\coth(s/N+d_j)$.
Convexity of $\coth$ gives precisely
$$
 \frac12\left[N^{-1}\coth((s+c_D)/N)-1\right].
$$
This calculation uses eigenvalues with algebraic multiplicity
and does not require normality.

For the critical Fourier detector,
$\operatorname{Tr}E\le1/4$, so
$c_D\le\frac12\log(4/3)<1/6$.
At $s=1/4$, the inequality $\coth x>1/x$ gives the
strict lower bound $7/10$.
The full Abel tail is retained. This lower bound does not
determine the closed statistic, because the open-feedback
cross term is still present.

The determinant bridge, the logarithmic derivative, and
the ordered composition formula for $g_m$ all have
their correct signs and factor $m/j$.

## 8. Mesoscopic feedback and finite shell theorem

The exact inverse in report (8.3) is
$$
 (I-\Theta)^{-1}
 =\frac{I-W}{2}+c(I-zU)^{-1}c,
 \qquad E/4\le W\le E.
$$
The two lower bounds have constants $1/(4s)$ and $1/(32s)$.
For the Hilbert--Schmidt calculation, the exact constant term
before using $W^2\le W$ is
$N/4+\operatorname{Tr}W/2-\operatorname{Tr}W^2/4$.
This confirms the stated coarser $N/4+\operatorname{Tr}W/4$.

The full colligation determinant formula is valid for unequal
external and state dimensions. Deleting a dark unitary part
does not change the remaining inner degree. A lower number
of external channels does not by itself decrease that degree.

Under the explicitly unproved geometric premise
$\|D^T\|\le N^{-6}$, $T\le N$, the return tail is
$$
 z^{T+1}bUD^T(I-zD)^{-1}b.
$$
Its norm and derivative are bounded by $C_sNq$ and
$C_sN^2q$, respectively. The inverse difference is
$C_sN^3q$. After the derivative and the trace,
$C_sN^6q$ is a valid bound. Combining a bounded generating
function error with the a priori $O(N^{3/2})$ Hardy
$L^2$ norm gives normalized squared error $O(N^{-1/2})$.
No desired $O(N^2)$ trace energy estimate was used in this
budget.

The spatially constant absorber satisfies the short-memory
premise directly, but its exact transfer retains
$(I-zU)^{-1}$. Its full rank is explicitly acknowledged.

The new Section 8.4 agrees with the independently audited
finite theorem at SHA-256
76aa1ece063eea6b9e673d5fc592fa23ba72c541fee5c93916314a62da85ee6f.
Its complete audit is in
fermionic_finite_detector_shell_audit.md, SHA-256
c2ec38925db10f7c178d8e3d5e93acd757dddcaff29b53760d638a04eca5c849.
All modular, rounding, same-level sign, and deep-tail effects
are accounted for.

The report correctly separates a divergent coefficient or
logarithmic discrepancy from an absolute determinant
difference, which tends to zero. It also expressly declines
to extrapolate the critical-marker orbit expansion to the
growing mesoscopic Fourier parameter.

## 9. Arithmetic range

The endpoint cyclicity proof was checked against
arithmetic_endpoint_cyclicity.md, SHA-256
387243de3e23f5df546c999ef2d650a640e6b7c4d4488ea775765e3ae5362868.

The report does not infer endpoint observability merely
from total nonsingularity. It includes the separate
bordered-minor argument. The two conjugate valuations
handle the two endpoints with opposite signs of the
phase valuation.

The large-real-time root scale uses nonzero leading
principal minors; the limiting endpoint coordinates use
the additional bordered minors. This proves that the
finite exponential polynomials are not identically zero.
After equal frequencies are collected, their exponents
at nonzero algebraic $z$ are distinct algebraic numbers,
so the quoted Lindemann--Weierstrass statement applies.

The complex-parameter identity
$U_N(z)^*=U_N(\overline z)^{-1}$ has the correct order
of its factors. It transfers observability to cyclicity.

Only $7\nmid N$ is claimed. The local detector consequence
is now explicitly restricted to sufficiently large $N$.
For those $N$, the consecutive Fourier minor has full
coordinate-window rank, and the visible space is all of
$\mathbb C^N$. Formula (9.2) then follows exactly from
the mixed return identity and the open Abel lower bound.

## 10. The complete error budget in the remaining pair identity

This is the crucial quantitative combination in the report.
On $1\le m\le2N$, let the coinciding-geometric-orbit
contribution be
$$
 D^{\rm geom}_{m,N}
 =m+O(m^2/N^2)+O(m^2\vartheta^m).
$$
Its use is justified by the fixed-band theorem in
classical_trace_and_pair_diagonal.md, SHA-256
355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c.

The four summed errors are:

$$
 \frac1{N^2}\sum_{m<2N}O(m^2/N^2)=O(N^{-1}),
$$
$$
 \frac1{N^2}\sum_{m<2N}O(m^2\vartheta^m)=O(N^{-2}),
$$
$$
 \frac1{N^2}\sum_{m<2N}
   \big||p_m|^2-|\mathcal P_m|^2\big|=O(N^{-1}),
$$
because
$$
 \big||p_m|^2-|\mathcal P_m|^2\big|
 \le4N(.421)^m+4(.421)^{2m},
$$
and
$$
 \frac1{N^2}\sum_{m<2N}w(m/N)(m-\min(m,N))
 =\int_1^2(u-1)w(u)\,du+O(N^{-1}).
$$
The fixed smooth bounded weight preserves every estimate.
The last line is a Riemann sum for a Lipschitz function.

Thus report (10.2) has a genuinely proved $O(N^{-1})$
error; no uncontrolled infinite trace tail is present.

Subtracting exactly the selected family from the off-diagonal
sum, and inserting the uniform profile from (4.7), yields
(10.3) with its two negative terms. In particular
$\eta_*>0$, because $w>0$ on $(1,2)$.
The formula is necessary and sufficient for this one pair
test once the proved error estimates are used. Its truth is
not assumed anywhere in the partial results.

## 11. Closure and external statements

The Fourier coefficient of $b_N$, the partition-lattice
Möbius coefficients, the Haar determinant identity, and the
bound $e_k\le H^k/k!$ are consistent with the exact
normalizations in the question.

The Bonferroni comparison uses the CUE term at order $J$
as its one remainder. It does not require a deterministic
moment of order $J+1$. The approximation $b_B=h*K_B$
preserves nonnegativity, integral, and a strict supremum
below one. Periodization, telescoping, and exact intensity
give the stated $L^1$ error.

At the fixed support scale, the rescaled CUE kernel converges
uniformly, and Hadamard bounds all correlation determinants
by one. The Fredholm series is dominated by $H^k/k!$.
The parameters $B,J$ are fixed before $N$ tends to infinity.

The new probability paragraph gives a valid final route:
local mass tightness, subsequential vague limits, and
uniqueness from a countable separating smooth family.
Joint Laplace uniqueness can indeed be reduced to
polynomial density after the substitution $x\mapsto e^{-x}$.

The primary texts for Bowen--Ruelle, Popescu, and the two
modern comparison papers were independently reopened.
The actual Bowen--Ruelle input is a transitive $C^2$
hyperbolic suspension preserving smooth volume; its unit
roof need not make the flow mixing. The Lindemann--Weierstrass
hypotheses match the algebraic exponential polynomials.
The modern circuit paper explicitly treats its plateau
resummation as an assumption/conjectural extrapolation,
and the Dyatlov--Jézéquel paper concerns linear cat maps
and fixed observables. Neither is inserted as the missing
estimate for the nonlinear family.

Primary links checked:

- https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf
- https://arxiv.org/html/2306.14352v2
- https://arxiv.org/abs/1007.3984
- https://arxiv.org/html/2605.27052v1
- https://link.springer.com/article/10.1007/s00023-023-01309-x

The remaining obstruction is the one stated in report
(10.3), not a defect in its conditional Laplace closure.

