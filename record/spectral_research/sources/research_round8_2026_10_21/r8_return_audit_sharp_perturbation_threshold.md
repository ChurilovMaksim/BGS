> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_sharp_perturbation_threshold.md`. Embedded SHA256: `5b7268f1e4f3dacad67a67a1a54bd3b8817bb284122a1077619cb0a2685fa9c4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit of the norm-threshold and spectral-rounding proof

21 October 2026. Reviewer: signed-return branch.

**Verdict on the core statements in Sections 1--8: proved by the supplied
argument, with no mathematical defect found.** The matching lemma,
uniform $o(1/N)$ Laplace bound, rounded-family bounded witness, and
fixed-test pair defect all check, including arbitrary multiplicities.

There was one logical qualification to the concluding terminology,
now explicitly resolved in Section 9 by the added link described below.
A sharp threshold for *uniform Laplace stability itself* needs a pair
with different Laplace limits, unless
the existence of a deterministic Sine-convergent base is separately
established. The rounded-family theorem alone says that every base
has a nearby non-Sine replacement; it does not itself prove that the
base and replacement have different laws. A separate explicit
two-clock addendum now fills this logical point without a Sine base.
No part of the core rounded-family theorem depends on that addendum.

## 1. Frozen proof and added clarification

The entire source was audited initially at SHA-256
`53594add2a626db1ceeb0b2f03ba8769aba6650c1f444a83bc05b54a7018c69e`.
The final audited source hash is:

- `root_sharp_microscopic_perturbation_threshold.md`:
  `ea39b0166a5308caa8c68d83ca4d744d2f404b0a9d5fe0eb2b98df5d5dc47ab0`.

The only addition between these versions is the paragraph in Section 9
linking the explicit two-clock addendum and explaining that it supplies
a direct different-Laplace comparison without a deterministic Sine
base. The mathematical statements and proofs in Sections 1--8 are
unchanged. The new paragraph was read and checked after insertion.

The exact direct counterexample needed for the concluding sharpness
interpretation is in:

- `r8_return_sharp_stability_clock_addendum.md`:
  `f77baf9f94d8ed92c3b83abe88e042e16db31864b80a070ac69db5082da67e08`.

Both files are in `research_round8_2026_10_21`. The addendum proves,
for every $C>0$, an explicit pair of diagonal unitary sequences
within $C/N$ for which a single fixed smooth nonnegative Laplace
test has a strictly positive limiting difference. It is independent
of the Sine-2 process and of the original family. The source may cite
this addendum when using the stronger sharpness terminology.

## 2. Cayley differentiation and order: all factors checked

Write $Z'=iHZ$ and $R=(I+Z)^{-1}$. The proposed Hermitian
Cayley transform can be rewritten as
$$
 A=i(I-Z)(I+Z)^{-1}=2iR-iI.
$$
Therefore
$$
 A'=-2iRZ'R=2RHZR=2RHR^*,
 \tag{2.1}
$$
where $ZR=(I+Z^*)^{-1}=R^*$. This verifies the factor order
in source (2.3), which is essential because $H$ need not commute
with $Z$.

For a scalar eigenvalue $z=e^{i\gamma}$ in the chosen cut,
$i(1-z)/(1+z)=\tan(\gamma/2)$. Thus
$$
 RR^*=(I+A^2)/4.
$$
Congruencing $-\eta I\le H\le\eta I$ by $R$ in (2.1)
gives exactly
$$
 -\frac\eta2(I+A^2)\le A'\le\frac\eta2(I+A^2).
$$
In particular neither inequality reverses its sign, and the factor
$1/2$ is correct.

The logarithm construction also checks. Since
$\|VU^*-I\|=\|V-U\|=\epsilon<2$, the eigenvalue $-1$
is excluded from $VU^*$. Its Hermitian principal logarithm has
norm at most $2\arcsin(\epsilon/2)=\eta$. The connecting path
$e^{itH}U$ has the required endpoints and derivative.

## 3. Eigenvalue collisions and global matching

On a local interval avoiding a chosen spectral cut, $A(t)$ is a
differentiable Hermitian matrix. The min--max inequality proves local
Lipschitz continuity of its ordered eigenvalues. The asserted bound
on the derivative at a repeated eigenvalue is valid.

Here is the block check in detail. Let $P$ be the spectral
projection for a fixed eigenvalue $\mu$ of $A(t)$. On its
complement, $A(t)-\mu I$ has a fixed nonzero spectral gap. For
small $h$, any unit eigenvector for an eigenvalue near $\mu$
has complementary component $O(h)$, obtained by solving the
complementary block of
$A(t+h)=A(t)+hA'(t)+o(h)$. The off-diagonal block is $O(h)$,
so its feedback into the $P$ block is $O(h^2)$. The remaining
first-order matrix on the eigenspace is $PA'(t)P$, with a
remainder $o(h)$. Its min--max bounds place every existing
eigenvalue derivative between the extreme Rayleigh quotients of
that compression. The same assertion is immediate when the whole
space is the eigenspace.

On this eigenspace $I+A^2$ is scalar, so the order inequality
implies $|\mu_j'|\le\eta(1+\mu_j^2)/2$ almost everywhere.
The angle $\beta+2\arctan\mu_j$ consequently has derivative
bounded in absolute value by $\eta$. Local Lipschitz continuity
makes it absolutely continuous.

A finite subdivision of $[0,1]$ subordinate to the local spectral
cuts gives a completely finite gluing argument. At each subdivision
endpoint, the two lists of eigenvalues match with multiplicities;
one can permute the outgoing labels and add multiples of $2\pi$
to match the real angle values continuously. Repeated values do not
prevent such a matching. Each resulting piecewise absolutely
continuous lift obeys the same derivative bound, and its total
endpoint displacement is at most $\eta$. Dividing by $2\pi$
proves the claimed matching lemma, with no simplicity assumption.

## 4. Laplace stability and the unfolding factors

After choosing the matched real lifts, the pointwise exponential
inequality bounds the Laplace difference by the integral of the sum
of absolute differences of the single-point tests. For each label,
the sum over all periodic copies unfolds exactly to
$$
 \frac1N\int_{\mathbb R}
   |f(x+N(\varphi_j-\theta_j))-f(x)|\,dx.
$$
The $1/N$ is correct. The translation bound multiplies this by
$N|\varphi_j-\theta_j|\|f'\|_1$; summing the labels then gives
$N\eta\|f'\|_1/(2\pi)$. This includes every copy and is valid
without a support-nonoverlap argument. Since
$\eta\sim\epsilon$ as $\epsilon\to0$, an $o(1/N)$
operator error indeed makes every fixed local Laplace difference
vanish. This proof has not asserted moment stability.

## 5. Rounding, lattice spacing, and the bounded witness

Nearest-root rounding changes an eigenangle by at most
$1/(2M_N)$, hence its eigenvalue by at most
$2\sin(\pi/(2M_N))$. The matrices share an eigenbasis, so this
is also an operator norm bound. With $a=C/\pi$,
$M_N=\lceil N/a\rceil$, it is at most $C/N$.

All unfolded rounded positions lie on a translate of
$a_N\mathbb Z$, $a_N=N/M_N$. The elementary inequalities
$$
 0\le a-a_N\le a^2/N,\qquad a_N\ge a/2
$$
are valid for all sufficiently large $N$. No occupancy assumption
enters either statement.

For the two chosen support intervals, every distance from the first
to the second is positive and less than $a/2\le a_N$. A
translated lattice cannot meet both. Coincident eigenvalues at a
single site cannot meet disjoint supports either. The product of
the two exponential bump observables is bounded and continuous for
the vague topology because each bump is continuous with compact
support. Its value is therefore identically zero for the rounded
family, as claimed.

For Sine-2, the strict positivity proof is correct. The kernel has
the Gram representation
$$
 K(x,y)=\int_{-1/2}^{1/2}e^{2\pi it(x-y)}\,dt,
$$
so its correlation determinants lie in $[0,1]$. For disjoint
intervals, $\mathbb E(n_1n_2)=\int\rho_2>0$ since
$|\sin(\pi u)|<\pi|u|$ whenever $u\ne0$.

Expanding
$n_1^2n_2^2=((n_1)_2+n_1)((n_2)_2+n_2)$, with
$(n)_2=n(n-1)$, yields four factorial-count terms of orders
four, three, three, and two. Their bounds from $\rho_k\le1$
sum to $\ell_1\ell_2(1+\ell_1)(1+\ell_2)$. Cauchy--Schwarz
then gives the stated positive lower probability for both intervals
to be occupied. The exponential factors have the claimed positive
lower bounds on that event. Thus the witness excludes weak Sine-2
convergence without any uniform-integrability premise.

## 6. The admissible tests and the autocorrelation identity

The bump construction gives $|u(x)|\le I_\phi$, hence
$0\le d\le1/8$. Its Fourier transform is a smooth compactly
supported convolution. Multiplication by
$1+\cos(2\pi x/a+\vartheta)$ preserves nonnegativity, gives
the bound $1/4<1$, and shifts that compact Fourier support only
by the fixed numbers $\pm1/a$. Every one of the five tests is
therefore in the exact allowed class.

For real Schwartz $b$, its autocorrelation is even and has
Fourier transform $|\widehat b|^2$. Averaging the four phases
makes each single cosine vanish and makes the product average equal
to $\cos(2\pi y/a)/2$. Consequently
$$
 \sum_{\vartheta}c_{b_\vartheta}(y)
       =(4+2\cos(2\pi y/a))c_d(y).
$$
The resulting identity
$F=3c_d-\tfrac12\sum c_{b_\vartheta}$ has the correct factor
$1/2$. Positivity of $F$, its zero values on $a\mathbb Z$,
and its nonzero values near the origin all follow as written.

## 7. Pair normalization and arbitrary multiplicities

Unfolding the two periodizations gives
$$
 \int_0^1 b_N(\theta_j-\alpha)b_N(\theta_k-\alpha)\,d\alpha
 =\frac1N\sum_{\ell\in\mathbb Z}
      c_b(N(\theta_j-\theta_k+\ell)).
$$
Evenness of the autocorrelation removes the possible opposite sign
from the chosen unfolding variable. The ordered distinct-label sum
and its factor $1/2$ therefore give exactly
$M_{2,N}(b)=\langle c_b,\mathcal R_N\rangle/2$.
This identity includes equal angles with distinct indices.

The global cosine inequality, valid even for large $k$, gives
$$
 1-\cos(2\pi a_Nk/a)\le 2\pi^2a^2k^2/N^2.
$$
Schwartz decay then bounds $F(a_Nk)$ by the displayed summable
sequence of order $N^{-2}$. Each ordered pair contributes a
single residue class modulo $M_N$; positivity permits replacing
its sum by the sum over the whole integer lattice. Thus each pair
contributes at most $D_a/N^2$, regardless of occupancies. The
ordered-pair count and the normalization in $\mathcal R_N$ give
$$
 \frac1N N(N-1)\frac{D_a}{N^2}\le\frac{D_a}{N}.
$$
The infinite periodization tail is controlled by the same summable
majorant. No terms at large $k$, no coincident levels, and no
power of $N$ have been dropped.

## 8. CUE limit and fixed-test subsequence

Direct summation over the diagonals of $T_{N,b}^2$ gives
$$
 \operatorname{Tr}T_{N,b}^2
  =\frac1N\sum_{|m|<N}(1-|m|/N)|\widehat b(m/N)|^2.
$$
This converges to the stated triangular-weight integral. The
triangle is the Fourier transform of the squared sinc kernel in
the prescribed convention. Also $\int c_b=(\int b)^2$.
These identities prove the asserted CUE limit without an additional
random-matrix theorem.

It follows that
$$
 3\Delta_{2,N}^{V}(d)
       -\frac12\sum_\vartheta\Delta_{2,N}^{V}(b_\vartheta)
            \longrightarrow-I_a/2.
$$
The absolute coefficient sum is $3+4/2=5$. For sufficiently
large $N$, the absolute value of the left side is at least
$I_a/4$, so at least one test has defect at least $I_a/20$.
The finite pigeonhole selection gives one fixed admissible test on
an infinite odd subsequence. The proof correctly does not identify
which test or its individual sign without further information.

## 9. Original-family scope

The perturbation bound for each fixed physical probability operator
is correct: telescoping gives $\|V^n-U^n\|\le n\|V-U\|$,
adjoint conjugation differs in Hilbert--Schmidt operator norm by at
most twice that amount, and coordinate compression is contractive.
The fixed-time compact limits and the uniform shrinking-window
theorem therefore persist for the replacements.

The rounded matrices and the two clocks in the additional note
remain auxiliary. Neither supplies an original-family spectral
counterexample. The source leaves the first original signed pair
estimate and all higher orders unproved, which is the correct
scope statement.

The reference to the explicit clock addendum is now present in the
concluding sharpness paragraph. No unresolved defect remains in the
full norm-threshold argument audited here.
