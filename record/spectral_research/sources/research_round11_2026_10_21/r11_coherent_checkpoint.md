> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round11_2026_10_21/r11_coherent_checkpoint.md`. Embedded SHA256: `04d220ec857e51de1aa141504a71d69dee3e84b8329fb72d01f864aa97225770`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Round 11: coherent Weyl resummation and the attempted Schur extension

Date: 21 October 2026. Branch: `/root/r11_coherent`.

## 1. Outcome and exact scope

**This branch has not obtained a new estimate of the original pair
functional.** In particular it has not proved or disproved
$H_{\rm diag}$, even for the fixed test $b_*$ below. The statements
verified in this note are earlier results, explicitly identified as such.
The present contribution is an attempt record: it prevents several exact
resummations and norm estimates, which were investigated again, from
being misreported as a new advance.

The frozen base and the working master had the same SHA-256 when checked:

`fe0812b16e1e559d596e8e848dea5d21cea6cf81aec05f39da7d44fc4bb6d45a`.

The family throughout the attempted argument is exactly

$$
 U_N=\exp(i10^{-80}N A_N)M_N,
 \qquad N\geq3\text{ odd}.
$$

No replacement of the fixed kick by a dimension dependent parameter,
averaging over matrices, or numerical spectrum at zero kick was used.

The fixed detector is

$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\qquad
 I=\int\phi,\qquad u=\mathcal F^{-1}\phi,\qquad
 b_*=\frac{|u|^2}{2I^2},\qquad w=|\widehat b_*|^2.
$$

The first still missing estimate is

$$
 \boxed{
 \frac1{N^2}\sum_{1\leq m<2N}w(m/N)
 \left(
  |\operatorname{Tr}[(e^{i10^{-80}N A_N}M_N)^m]|^2
  -\min(m,N)
 \right)\longrightarrow0
 }
 \tag{1}
$$

along **all** odd dimensions. Its proof would still fall short of the
all orders, all fixed Fourier bands criterion in the question.

## 2. What the full Weyl resummation already does

The three original Round 8 sources listed in Section 6 were read in
full. Their conventions are

$$
 W_N(k,l)=T_N(l,k),\qquad
 \omega((k,l),(k',l'))=lk'-kl',\qquad
 S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

The exact multiplication and covariance are

$$
 W(u)W(v)=e_N(\overline2\,\omega(u,v))W(u+v),\qquad
 M W(v)M^{-1}=W(Sv).
$$

The raw terminal trace identity, valid over every odd modulus, is

$$
 g_m(\lambda)\overline{g_m(\lambda+\Gamma)}
 =\sum_{v:(S^m-I)v=\Gamma}
 e_N\!\left(
  \omega(\lambda,v+\overline2\Gamma)
  +\overline2\omega(\Gamma,v)
 \right),
 \quad g_m(\lambda)=\operatorname{Tr}(W(\lambda)M^m).
 \tag{2}
$$

After summing every background path with its full kick coefficients,
the sector of relative endpoint $\Gamma$ is exactly

$$
 \mathcal S_m(\Gamma)
 =\sum_{v:(S^m-I)v=\Gamma}
       ((\operatorname{Ad}U_N)^m)_{v,v}.
 \tag{3}
$$

Thus neither noninvertible $S^m-I$ nor a missing scalar area phase is
the gap. Formula (3) retains the original coherent adjoint evolution.
Replacing its entries by their modulus squares changes the operator.

The intermediate Weyl index also does not give a contraction. For a
unitary matrix $C$,

$$
 |(C^m)_{v,v}|
 \leq\sum_a |(C^r)_{v,a}|\,|(C^{m-r})_{a,v}|
 \leq
 \left(\sum_a|(C^r)_{v,a}|^2\right)^{1/2}
 \left(\sum_a|(C^{m-r})_{a,v}|^2\right)^{1/2}=1.
 \tag{4}
$$

The two sums in the last expression are a row norm and a column norm;
they are exactly one. This step was already isolated in Round 10. A
small bound on a single entry cannot replace it without paying for the
remaining indices. On the $N^2$-dimensional Weyl space, their
$\ell^1$ norm can be $N$. No stronger original matrix input was
found in this pass that compensates this loss in (1).

## 3. Attempted change of route: exact elimination of disagreement runs

The next candidate was to retain the coherent matrix, use a block
decomposition, and eliminate long parts of paths between successive
agreements of the two physical coordinates. The hope was that the
already proved mixing of physical transition probabilities could
control the complementary propagator after the elimination.

This candidate was compared with the raw Round 2, Round 6, and Round 7
sources before assigning any new result to it. The relevant exact
identities already hold for every finite unitary matrix.

Write $W=\operatorname{Ad}U$ on matrices with the Hilbert--Schmidt
inner product. Let $\Pi$ be the orthogonal projection onto coordinate
diagonal matrices, and let $O=I-\Pi$. In this orthogonal splitting,

$$
 W=\begin{pmatrix}P&B\\C&S_0\end{pmatrix},
 \qquad P_{xy}=|U_{xy}|^2,
 \qquad S_0=OWO|_{\operatorname{ran}O}.
$$

Here $S_0$ is a compressed coherent unitary. It is not the classical
transition matrix $P$. Define exact first return matrices

$$
 F_1=P,\qquad F_r=B S_0^{r-2}C\quad(r\geq2),\qquad
 \mathfrak F(z)=\sum_{r\geq1}F_rz^r.
$$

Block elimination and a formal logarithm give

$$
 \det(I-zW)=\det(I-zS_0)\det(I-\mathfrak F(z)),
 \tag{5}
$$

$$
 |\operatorname{Tr}U^n|^2
 =\operatorname{Tr}S_0^n
  +n\sum_{\ell=1}^n\frac1\ell
    \sum_{\substack{r_1,\ldots,r_\ell\geq1\\
                    r_1+\cdots+r_\ell=n}}
       \operatorname{Tr}(F_{r_1}\cdots F_{r_\ell}).
 \tag{6}
$$

The proof of (6) is finite coefficient extraction: use
$-\log\det(I-zA)=\sum_{n\geq1}z^n\operatorname{Tr}(A^n)/n$
as a formal power series on the two sides of (5). The coefficient of
each degree contains finitely many terms. Finally
$\operatorname{Tr}(\operatorname{Ad}U)^n=|\operatorname{Tr}U^n|^2$,
as is seen in a basis of matrix units in an eigenbasis of $U$.
Thus there is no passage to a random or positive process in (6).

This is the exact cycle identity proved in
`r7_return_schur_discriminant_identity.md`; it is not a Round 11 result.
It shows precisely what a successful extension would have to estimate:
the full signed complementary trace and the signed first return cycle
sum on the scale $n\asymp N$.

### 3.1. The contraction discriminator and its outcome

The candidate inference

> mixing of the observed diagonal block permits a norm bound strictly
> below one for the complementary propagator on times much shorter than
> $N$

fails an exact dimension test. Here is the complete test, reproduced
from the earlier compression argument to specify the failed step.

Restrict $W$ to the traceless matrix space $\mathcal H_0$, of
dimension $N^2-1$. The projection onto its coordinate diagonal part
has rank $N-1$; call it $P_0$, and write $Q_0=I-P_0$. For
$0\leq m<N$, define

$$
 \mathcal E_m=\bigcap_{j=0}^m W^{-j}\operatorname{ran}Q_0.
$$

Each intersection imposes at most $N-1$ linear conditions. Therefore

$$
 \dim\mathcal E_m
 \geq N^2-1-(m+1)(N-1)
 =(N-1)(N-m)>0.
 \tag{7}
$$

For $X\in\mathcal E_m$, all $W^jX$, $0\leq j\leq m$,
belong to $\operatorname{ran}Q_0$. Induction gives

$$
 (Q_0WQ_0)^jX=W^jX\quad(0\leq j\leq m).
$$

The latter vectors have norm $\|X\|$, since $W$ is unitary.
As $Q_0WQ_0$ is a contraction, this proves

$$
 \|S_0^m\|_{\rm op}=1\quad(0\leq m<N),\qquad
 \|S_0^m\|_{\rm HS}^2\geq(N-1)(N-m).
 \tag{8}
$$

For the Hilbert--Schmidt assertion choose an orthonormal basis of
$\mathcal E_m$, extend it to an orthonormal basis of
$\operatorname{ran}Q_0$, and sum squared norms of the images. Each
vector in the first basis contributes one. This proof uses only
unitarity and is therefore valid for the original matrix at its exact
fixed kick, with no asymptotic approximation or prime modulus
restriction.

Equations (7)--(8) are the outcome of the discriminator: the proposed
norm gain is false. They do **not** disprove the possibility of a
trace-sensitive cancellation in (6). The latter is precisely the
unproved step, and replacing it by (8) does not advance (1).

### 3.2. The previously established stronger inputs do not repair this step

The older work already controls the full signed class with bounded
disagreement run lengths, and proves exact first return energy and
first moment identities. The raw Round 7 material also extends
physical kernel analysis to every fixed power. The present attempt
found no argument converting those statements into a bound on the
cycles of (6) that contain runs growing with $N$.

In particular, the exact first return mean is not a uniform tail
bound. The countermodel and microperturbation sources cited in the
read-scope list below explicitly warn against that inference. They
were not used as counterexamples to the original family.

## 4. A second candidate that was already resolved in the history

The contribution of cyclic rotations of a physical path supplies the
diagonal ramp. Trying to extract this ramp from the Weyl expansion
would not have been new: the full physical cycle calculation and its
audit were completed in Round 5.

That calculation also fixes a sign which a proposed cancellation must
respect. After the controlled forward and reversed classes are removed,
the remaining signed class $Z_{n,N}$ satisfies

$$
 \sum_{n\geq1}
 \big||\operatorname{Tr}U_N^n|^2-n-Z_{n,N}\big|=O(1).
$$

Thus for the fixed detector the value required from the remaining
class is

$$
 \frac1{N^2}\sum_{1\leq n<2N}w(n/N)Z_{n,N}
 \longrightarrow -\int_1^2(t-1)w(t)\,dt<0.
 \tag{9}
$$

The integral is strictly positive before its minus sign because
$\widehat b_*=(\phi*\phi)/(2I^2)>0$ on $(-2,2)$.
Consequently, proving that *all* remaining coherent contributions are
negligible would be incompatible with the desired plateau in this
band. This warning was explicitly present in the Round 5 audit; it
is not a new obstruction theorem from the current pass.

## 5. First gap after the checks

No phase error was found in the full all odd endpoint identity (2).
No replacement of the coefficient products by a positive path measure
was justified. No cancellation estimate for the complete right side of
(6), or equivalently the complete fiber sum in (3), was proved at
times of order $N$.

The earliest quantitative statement still lacking a proof in this
branch is exactly (1). One can equally describe the missing quantity
using (9), but that does not turn it into a result. This pass supplies
no new conditional criterion and no claim of a fundamental advance.

## 6. Raw inputs and verification scope

The following files were read in full in this branch. Hashes were
recomputed from the actual bytes after the investigation.

| File | SHA-256 |
|---|---|
| `research_round10_2026_10_21/r10_weyl_route_ledger.md` | `c3c8d7b3bd9d3fdfe2a3390f8cc793ed6ad48b57ff84bbd98ea4cbb904586a2d` |
| `research_round8_2026_10_21/r8_weyl_full_weight_relative_path_cancellation.md` | `038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109` |
| `research_round8_2026_10_21/r8_weyl_all_odd_endpoint_fiber_identity.md` | `ec36b997ef3a38dd464d468833f78a3934b45bdc57dbc36f54987aa42a649b70` |
| `research_round8_2026_10_21/r8_weyl_three_time_resonance_and_exact_recursion.md` | `8f6a660d4bb776c769aa7e96e7a4607609c7a44c06addb494764189e3ef1fbf2` |
| `research_round9_2026_10_21/r9_sector_route_ledger.md` | `ad07baa0fae652ea65f15e41dc931840a7d6046ebf30abac9a62d819e80b41e2` |
| `research_round2_2026_10_20/adversarial_pair_schur_memory.md` | `a9811e26f0aaa15a3f94c61760da7f83446621057b65299c9107d2de1eab2c01` |
| `research_round6_2026_10_21/r6_dense_renewal_long_return_obstruction.md` | `95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2` |
| `research_round6_2026_10_21/r6_dense_bounded_runs_raw49.md` | `631663c9639c286510125df4806b833d4cfb8344a7a9d0fc36d6c647e83bc9e8` |
| `research_round7_2026_10_21/root_original_intensity_at_prescribed_phase.md` | `deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63` |
| `research_round7_2026_10_21/r7_return_schur_discriminant_identity.md` | `fc36418d779397802e481ad4383ee40460e19d27916f5b21b5da0f9ced9b9a33` |
| `research_round5_2026_10_21/dual_audit_physical_cycle_classes.md` | `953578dbba89c8aa86994c63a9289ffe26803795f2dac7055e3f306bad9d79ae` |

The following additional reads were partial; they are **not** asserted
to be full independent audits:

- `research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md`,
  lines 1--125 and the section headings;
- `research_round7_2026_10_21/root_unipotent_flat_clock.md`, lines 1--150;
- `research_round7_2026_10_21/r7_return_generic_microperturbation.md`,
  lines 1--140;
- `research_round8_2026_10_21/r8_weyl_sublinear_polynomial_obstruction.md`,
  lines 1--280;
- portions and search matches of other earlier files, used only to
  identify already investigated routes.

A web query returned primary source leads concerning trace formulas and
supersymmetry. No theorem from those search snippets is used here. No
numerical spectrum was substituted for a mathematical estimate.

Only this Round 11 branch file was created; the frozen master and all
older sources were left unchanged.
