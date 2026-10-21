> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round11_2026_10_21/r11_resolvent_ward_diagonal_route.md`. Embedded SHA256: `6868e41398755931045c322ccc18cd3400631d85596aadeaf1c743f34d4efb4f`.
> [Thematic guide](../../topics/dephasing.md).

# Round 11: exact test of a physical-diagonal resolvent bootstrap

Date: 21 October 2026. Branch: `/root/r11_resolvent`.

## 0. Status and the attempted implication

**No new asymptotic estimate for the prescribed family was obtained in
this branch.** This note proves neither the original pair limit nor a
nonzero original pair defect. It records an exact attempted estimate,
with its feedback coefficient and its uncontrolled denominator visible.

The proposal was to prove an averaged physical return bound, which
would imply boundedness of the positive pair functional. For a unitary
matrix $U$, put

$$
p_m=\operatorname{Tr}U^m,\qquad
T_m(U)=\sum_{x=1}^N|(U^m)_{xx}|^2.
$$

For a nonnegative compactly supported weight $w$, define

$$
S_N(U;w)=\frac1{N^2}\sum_{m\ge1}w(m/N)|p_m|^2,\qquad
\mathcal D_N(U;w)=\frac1N\sum_{m\ge1}w(m/N)T_m(U).
\tag{0.1}
$$

Cauchy--Schwarz on the physical diagonal gives, without approximation,

$$
\boxed{S_N(U;w)\le\mathcal D_N(U;w).}
\tag{0.2}
$$

Thus an actual estimate

$$
\mathcal D_N(e^{i10^{-80}NA_N}M_N;w)=O_w(1)
\tag{0.3}
$$

would be useful. Equation (0.3) is **not proved or assumed** here.
Sections 1--4 test whether the exact Ward, Haar, and first-return Schur
identities supply it. Even (0.3) would give boundedness, not the CUE
value, and would not establish $H_{\rm diag}$ at higher orders.

## 1. The mixed source reaches the original pair sum exactly

Write $D_U(z)=\det(I-zU)$. For $|a|,|b|<1$, let

$$
\Omega_U(a,c;b,d)=\int_0^{2\pi}
\frac{D_U(ce^{it})D_{U^*}(de^{-it})}
     {D_U(ae^{it})D_{U^*}(be^{-it})}\,\frac{dt}{2\pi}.
\tag{1.1}
$$

The four sources are independent complex variables. There are no
denominator zeros on the integration circle. The absolutely convergent
identity

$$
\frac{d}{dz}\log D_U(z)=-\sum_{m\ge1}z^{m-1}p_m
$$

and angular orthogonality give

$$
\left.\partial_c\partial_d\Omega_U(a,c;b,d)\right|_{c=a,d=b}
=\sum_{m\ge1}(ab)^{m-1}|p_m|^2.
\tag{1.2}
$$

In particular, set $r=e^{-s/N}$, $q=r^2$, and

$$
S_N(U;s)=\frac1{N^2}\sum_{m\ge1}q^m|p_m|^2.
\tag{1.3}
$$

Multiplying (1.2) by $r^2/N^2$, at $a=b=c=d=r$, gives exactly
(1.3). This finite identity is already in the R10 mixed-source record.
It is retained to keep the original observable fixed, not claimed as a
new result of this round.

The CUE reference is

$$
S_N^{\rm CUE}(s)
=\frac{q(1-q^N)}{N^2(1-q)^2}
\longrightarrow\frac{1-e^{-2s}}{4s^2}.
\tag{1.4}
$$

Indeed the CUE kernel $K_N(t)=\sum_{j=0}^{N-1}e^{2\pi ijt}$
has $|K_N|^2$-Fourier coefficient $(N-|m|)_+$.
Its two-point factorial density gives
$\mathbb E|p_m|^2=N-(N-|m|)_+=\min(|m|,N)$, for $m\ne0$.
Finally

$$
\sum_{m\ge1}q^m\min(m,N)
=\sum_{j=1}^N\sum_{m\ge j}q^m
=\frac{q(1-q^N)}{(1-q)^2}.
$$

No comparison of the prescribed $U_N$ to CUE is proved by this
calculation.

## 2. The exact unitary Ward identity and the missing factor

Let $R(z)=(I-zU)^{-1}$, $|z|=r<1$. Direct multiplication gives

$$
\boxed{R(z)+R(z)^*-I=(1-r^2)R(z)R(z)^*.}
\tag{2.1}
$$

To verify it, multiply on the left by $I-zU$, on the right by
$I-\bar zU^*$, and use

$$
(I-\bar zU^*)+(I-zU)
 -(I-zU)(I-\bar zU^*)=(1-r^2)I.
$$

The resolvent series has angular mean $I$. Taking the trace in
(2.1) and integrating therefore gives

$$
\boxed{\int\|R(re^{it})\|_{\rm HS}^2\,\frac{dt}{2\pi}
=\frac{N}{1-r^2}.}
\tag{2.2}
$$

This includes both matrix indices. The physical diagonal quantity is

$$
\begin{split}
\mathcal L_N(U;r)
&=\frac1N\sum_x\int|R(re^{it})_{xx}|^2\,\frac{dt}{2\pi}\\
&=1+\frac1N\sum_{m\ge1}r^{2m}T_m(U).
\end{split}
\tag{2.3}
$$

The second equality is Parseval. The zero-time term equals one.
Likewise,

$$
\frac1{N^2}\int|\operatorname{Tr}R(re^{it})|^2\,\frac{dt}{2\pi}
=1+S_N(U;s)
\tag{2.4}
$$

at $r=e^{-s/N}$. Cauchy--Schwarz gives

$$
1+S_N(U;s)\le\mathcal L_N(U;r).
\tag{2.5}
$$

However, (2.2) yields only

$$
\mathcal L_N(U;r)\le(1-r^2)^{-1}=O_s(N).
\tag{2.6}
$$

The bound sought is $O_s(1)$. The trace of the Ward identity does
not supply the missing factor $N$.

## 3. Exact Haar-basis feedback: a critical coefficient

Conjugation preserves every spectral source (1.1). It is consequently
legitimate as an identity-generating device, but creates no randomness
in the eigenvalues. For any fixed $A\in\mathbb C^{N\times N}$ and
Haar unitary $G$,

$$
\boxed{\mathbb E_G\sum_x|(GAG^*)_{xx}|^2
=\frac{\operatorname{Tr}(AA^*)+|\operatorname{Tr}A|^2}{N+1}.}
\tag{3.1}
$$

Here is a direct proof of the Haar moment being used. A row of $G$
is a uniform complex unit vector $v$. Coordinate phase invariance
forces

$$
\mathbb E[\bar v_i v_jv_k\bar v_l]
=\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}}{N(N+1)}.
\tag{3.2}
$$

To determine the coefficient, let
$a=\mathbb E|v_1|^4$ and
$b=\mathbb E|v_1|^2|v_2|^2$.
Invariance under $v_1\mapsto(v_1+v_2)/\sqrt2$, and phase invariance,
give $a=a/2+b$, hence $a=2b$.
Taking the expectation of $(\sum_i|v_i|^2)^2=1$ gives
$Na+N(N-1)b=1$. Thus $b=1/[N(N+1)]$, proving (3.2),
including coincident indices. The case $N=1$ is immediate.

Expand $|v^*Av|^2$ and contract the indices with (3.2). This gives

$$
\mathbb E|v^*Av|^2
=\frac{|\operatorname{Tr}A|^2+\operatorname{Tr}(AA^*)}{N(N+1)}.
$$

Summation over the $N$ identically distributed diagonal entries
proves (3.1). No independence of the rows is used.

For $A=U^m$, equation (3.1) becomes

$$
\boxed{\mathbb E_G T_m(GUG^*)=\frac{N+|p_m|^2}{N+1}.}
\tag{3.3}
$$

Define $W_N(w)=N^{-1}\sum_{m\ge1}w(m/N)$. Summation with the
normalizations in (0.1) gives

$$
\boxed{\mathbb E_G\mathcal D_N(GUG^*;w)
=\frac{N}{N+1}\bigl(W_N(w)+S_N(U;w)\bigr).}
\tag{3.4}
$$

The Cauchy inequality (0.2) holds in every conjugated basis, while
its left side is invariant. Therefore

$$
S_N(U;w)\le\frac{N}{N+1}(W_N(w)+S_N(U;w)),
$$

which solves to

$$
\boxed{S_N(U;w)\le NW_N(w)=\sum_{m\ge1}w(m/N).}
\tag{3.5}
$$

For a fixed compact band this is $O_w(N)$, exactly the elementary
unitarity bound. It is sharp for all unitaries since $U=I$ attains
equality. This last matrix is only a check on the inequality and is
not a counterexample for the original family.

The resolvent version, either by (3.1) directly or by (3.3), is

$$
\boxed{\mathbb E_G\mathcal L_N(GUG^*;r)
=1+\frac{q}{(N+1)(1-q)}+\frac{N}{N+1}S_N(U;s).}
\tag{3.6}
$$

Combined with (2.5), it yields only

$$
S_N(U;s)\le\frac{q}{1-q}.
\tag{3.7}
$$

The feedback coefficient is exactly $N/(N+1)$. Replacing it by
a constant uniformly below one changes the identity. Errors in the
resulting bootstrap can be amplified by $N+1$.

For CUE, even the physical return itself has the additional term

$$
\mathbb E_{\rm CUE}T_m(V_N)
=\frac{N+\min(m,N)}{N+1}.
\tag{3.8}
$$

This follows from (3.3) and conjugation invariance of CUE. At
$m\asymp N$ the additional term is order one. Removing it removes
the same form factor that the original problem asks to determine.

## 4. First-return Schur functions retain an uncontrolled denominator

For a coordinate $e_x$, group equal eigenvalues with nonzero
spectral weight at $e_x$. Let the resulting distinct eigenvalues be
$\lambda_1,\ldots,\lambda_d$, with positive weights $a_j$ summing
to one. Then

$$
R_x(z):=R(z)_{xx}=\sum_{j=1}^d\frac{a_j}{1-z\lambda_j}.
\tag{4.1}
$$

The function $2R_x-1$ has positive real part in the disc. Hence

$$
f_x(z)=1-\frac1{R_x(z)},\qquad
R_x(z)=\frac1{1-f_x(z)}
\tag{4.2}
$$

is a Schur function with $f_x(0)=0$. It is also the first-return
transfer function: if

$$
U=\begin{pmatrix}a&b\\c&D\end{pmatrix}
$$

in the decomposition $\mathbb Ce_x\oplus e_x^\perp$, scalar Schur
elimination in $I-zU$ gives

$$
f_x(z)=za+z^2b(I-zD)^{-1}c.
\tag{4.3}
$$

The degree and normalization statements have elementary finite proofs.
Set

$$
P(z)=\prod_{j=1}^d(1-z\lambda_j),\qquad
Q(z)=\sum_{j=1}^da_j\prod_{k\ne j}(1-z\lambda_k).
$$

Then $R_x=Q/P$, $\deg Q\le d-1$, and

$$
Q(\lambda_j^{-1})=a_j\prod_{k\ne j}(1-\lambda_k/\lambda_j)\ne0.
$$

Thus $P,Q$ are coprime, as are $Q-P,Q$.
In the open disc $\operatorname{Re}R_x>1/2$, so $Q$ has no
zero there. Away from the $d$ spectral points on the boundary,
$\operatorname{Re}R_x=1/2$, so $Q\ne0$ there too. At the
spectral points its nonvanishing follows from the displayed formula.
Consequently $f_x=(Q-P)/Q$ is analytic on a neighborhood of the
closed disc and has boundary modulus one.

Factoring the interior zeros of this rational function into a
Blaschke product leaves a zero-free inner quotient with analytic
reciprocal. The maximum principle for the quotient and its reciprocal
makes it a unimodular constant. Since the rational function is reduced
and its numerator has degree $d$, its Blaschke degree is exactly
$d$.

Write $f_x(z)=\sum_{n\ge1}f_{x,n}z^n$. Parseval and winding number
therefore give

$$
\sum_{n\ge1}|f_{x,n}|^2=1,\qquad
\sum_{n\ge1}n|f_{x,n}|^2=d\le N.
\tag{4.4}
$$

For completeness, the second identity follows by integrating
$\bar f_x(e^{it})\,i^{-1}d_tf_x(e^{it})$. Each Blaschke factor
contributes a Poisson kernel of integral one. Coefficient and derivative
series converge uniformly on the circle for each fixed matrix, because
the rational function has no pole on the closed disc. Thus termwise
integration is justified. This statement gives no uniform analytic
extension radius as $N$ varies.

The scalar Ward identity is

$$
\operatorname{Re}(2R_x(z)-1)
=\frac{1-|f_x(z)|^2}{|1-f_x(z)|^2}.
$$

Angular mean one gives

$$
\int\frac{1-|f_x(re^{it})|^2}{|1-f_x(re^{it})|^2}\,
\frac{dt}{2\pi}=1.
\tag{4.5}
$$

The needed diagonal integral is instead

$$
\begin{split}
\int|R_x(re^{it})|^2\,\frac{dt}{2\pi}
&=\int\frac1{|1-f_x(re^{it})|^2}\,\frac{dt}{2\pi}\\
&=1+\int\frac{|f_x(re^{it})|^2}{|1-f_x(re^{it})|^2}\,
\frac{dt}{2\pi}.
\end{split}
\tag{4.6}
$$

The final equality also follows by expanding $|R_x-1|^2$ and
using the angular mean of $R_x$. The numerator in (4.5) is
essential and cannot be dropped.

Every probability measure on $d$ distinct circle points with
positive weights produces (4.1)--(4.6). Degree and normalization
therefore leave the positions of those points unconstrained. To verify
failure of a scalar boundedness inference explicitly, take $d=N$,
equal weights, and

$$
\lambda_{j,N}=e^{ij/N^4},\qquad1\le j\le N.
\tag{4.7}
$$

These points are distinct. For $1\le m\le N$,

$$
c_{m,N}=\frac1N\sum_{j=1}^N\lambda_{j,N}^m,\qquad
|c_{m,N}-1|\le m/N^3\le N^{-2}.
$$

By Parseval, at $r=e^{-s/N}$,

$$
\int|R_x(re^{it})|^2\,\frac{dt}{2\pi}
\ge\sum_{m=1}^N e^{-2sm/N}(1-N^{-2})^2
\ge Ne^{-2s}(1-N^{-2})^2.
\tag{4.8}
$$

The exact degree-$N$ Kac normalizations (4.4) thus coexist with
linear growth of (4.6). These coordinate measures can be realized by
choosing the Fourier matrix as eigenbasis. This is only an elementary
discriminator for the scalar inference. It is not asserted to have the
additional physical properties of the original matrix and is not
presented as a new original countermodel.

The older R7 countermodel already has much stronger properties:
almost-flat physical powers in a growing range, no dark doubled sector,
exact first-return mean $N$, and a divergent fixed-test pair
functional. That prior result is not relabeled as a new result here.

For the original matrix, (4.1)--(4.6) hold at every odd $N$
without assuming simplicity or full cyclicity. The unresolved step is
the coordinate-averaged control of their denominator at
$r=e^{-s/N}$.

## 5. Published multi-resolvent input checked for applicability

The author PDF of Cipolloni--Erdős--Schröder, *Optimal multi-resolvent
local laws for Wigner matrices*, arXiv:2112.13693v2, was checked at
Definition 2.1 and Theorem 2.5, PDF pages 6--7. The published version
is *Electronic Journal of Probability* 27 (2022), article 117,
DOI [10.1214/22-EJP838](https://doi.org/10.1214/22-EJP838).

The matrix model has centered independent identically distributed
off-diagonal entries, Hermitian symmetry, variance $1/N$, and
uniform rescaled moment bounds. The displayed theorem assumes
$\min_j|\operatorname{Im}z_j|\ge N^{-1+\varepsilon}$, for fixed
$\varepsilon>0$, and concludes stochastic domination.
The prescribed deterministic unitary, its Cayley transform, and an
arbitrary isospectral Haar conjugate have not been proved to satisfy
those assumptions. No conclusion is imported from this theorem.
It does not supply (0.3).

Primary text inspected: <https://arxiv.org/pdf/2112.13693>.

The broader searches in this branch were discovery searches, not a
proof that no applicable theorem can exist. No uninspected paper is a
proof dependency.

## 6. Exact original gap retained

For the fixed admissible test from the main ledger, let

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
u=\mathcal F^{-1}\phi,\quad
b_*=\frac{|u|^2}{2(\int\phi)^2},\quad
w=|\widehat b_*|^2.
$$

Here $w$ is supported in $[-2,2]$. This branch does not prove

$$
\boxed{
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(
\left|\operatorname{Tr}[(e^{i10^{-80}NA_N}M_N)^m]\right|^2
-\min(m,N)
\right)\longrightarrow0
}
\tag{6.1}
$$

over all odd $N$, nor the weaker positive estimate (0.3), nor
the exponential-tail bound

$$
\frac1N\sum_{m\ge1}e^{-2sm/N}
\sum_x|[(e^{i10^{-80}NA_N}M_N)^m]_{xx}|^2=O_s(1).
\tag{6.2}
$$

The first failed implication in the tested route is passage from
(2.1), (4.4), or (4.5) to (6.2). Haar averaging does not repair it:
(3.4)--(3.7) retain the original unknown with coefficient
$N/(N+1)$.

The earlier actual-family Schur-memory obstruction also rules out
rapid operator-norm contraction for its compression almost up to time
$N$. This does not rule out a future integrated estimate. None is
inferred here.

No modulus has been moved inside the original signed spectral sum,
and no original subsequence with nonzero defect has been found.
These exact calculations test a proposed route; they are not a
solution or an asymptotic advance for the original family.

## 7. Read scope and hashes

The frozen master was checked by byte hash only, not reread in full by
this branch. The other listed artifacts were read in full; the
truncated segment of the R7 countermodel audit was reread separately.
Reading an audit artifact does not mean all older files it cites were
independently reread this round.

| Input | SHA-256 |
| --- | --- |
| `research_history_frozen/master_before_round11.md` | `fe0812b16e1e559d596e8e848dea5d21cea6cf81aec05f39da7d44fc4bb6d45a` |
| `research_round10_2026_10_21/r10_mixed_isospectral_twirl_obstruction.md` | `673a8fbbe93cb26db469b7c7dd13b5960352e3ec2cdbf9e248aa4d7f2be1d9b9` |
| `research_round10_2026_10_21/r10_mixed_shrinking_isospectral_noise.md` | `5c9265843ce9ad7037ca35b0b601bfed4cca9bd87a44d15405a30f68d22683fb` |
| `research_round9_2026_10_21/r9_determinant_exact_cue_detdet_counterexample.md` | `4fd909b04e8ccc1a000930e46e6efe23b520e8d41400d8f923e3aa7911623b7f` |
| `research_round6_2026_10_21/r6_occupation_rational_inner_kac.md` | `4bf2d0ef9ea39227cb0af38569df5432722799b32f322811a969a2ac85323e6a` |
| `research_round2_2026_10_20/fermionic_resolvent_frame.md` | `1e88189aa0192786ad4947091079efa93079aad8fe9a7194a00692c0fccb184f` |
| `research_round2_2026_10_20/adversarial_pair_schur_memory.md` | `a9811e26f0aaa15a3f94c61760da7f83446621057b65299c9107d2de1eab2c01` |
| `research_round2_2026_10_20/arithmetic_all_marker_domains_and_renewal_barrier.md` | `dc8bef986cae11bc1917805a02746cd0861ee06f74da1d853bcc82e25ba7deba` |
| `research_round6_2026_10_21/root_audit_rational_inner_and_dense_involution.md` | `424e57074b1fe33005be0b9efc9820a6cf4ef103e151c60900e9ba71250e1ca4` |
| `research_round7_2026_10_21/r7_audit_countermodel.md` | `6ebea61daab7c46fafa67d1212ecaee110cc08c348b933d1eda7ff5a5acd761a` |
| `research_round7_2026_10_21/r7_original_intensity_jacobian_audit.md` | `bfc2e7f0a36d0354bd7c859a364f4a21f9796fe5ba6f63659fcf2773f29a620c` |

The elementary proofs in Sections 0--4 are included in this file and
need no external theorem. The theorem inspected in Section 5 is
explicitly not applied to the prescribed matrix.

## 8. Exact finite checks and their scope

The Wolfram Language code in `r11_resolvent_exact_checks.wl` was
executed with exact rational complex arithmetic. For the explicitly
displayed three-dimensional rational unitary and $z=2/5+8i/15$,
the returned result was

```text
{True, {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}, 0, 0, 0}
```

The entries check, in order: unitarity; matrix Ward residual; physical
coordinate-1 Schur residual; scalar Ward residual; the fully expanded
four-index Haar-moment contraction against the matrix resolvent.
A separate direct two-dimensional rational rotation check also
returned the zero matrix for the Ward residual.

These exact examples check signs and normalizations. They do not
replace the general proofs above, verify the Haar law by sampling, or
test the prescribed $10^{-80}$ perturbation numerically.

For reproducibility, two attempted local SymPy checks stopped before
running because SymPy was unavailable in those Python environments.
An initial multi-dimension Wolfram batch returned `Null` and is not
counted as a successful check. The directly evaluated two- and
three-dimensional expressions above are the successful checks.
