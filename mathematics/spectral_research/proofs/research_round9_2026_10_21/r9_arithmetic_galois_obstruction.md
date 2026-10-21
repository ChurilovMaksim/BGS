> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round9_2026_10_21/r9_arithmetic_galois_obstruction.md`. Embedded SHA256: `19fc46287b04ee3dd88cfc16826b2e07e19f397b23d6e85a148844e12929ca27`.
> [Thematic guide](../../topics/algebra.md).

# Round 9: an exact test of cyclotomic transfer for the original family

Date: 21 October 2026.

Base master: `Spectral_research_master.md`, SHA-256
`b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20`.

## 1. Outcome and scope

This branch has not proved or disproved `H_diag`. It has not produced a
fixed-test microscopic countersequence. The new result below checks a
specific arithmetic route at the level of exact spectra, without restricting
the possible conjugating matrix to the Clifford group.

Let the cyclotomic automorphism send `zeta_N` to `zeta_N^2` and fix `i`.
It exists for every odd `N`: choose its exponent modulo `4N` to be `2`
modulo `N` and `1` modulo `4`. Define its explicit positive-normalization
companion matrices by

$$
 A_N^{[2]}=\sum_{k,l}c_{kl}\,T_N(l,2k),
 \qquad
 (M_N^{[2]})_{xy}=N^{-1/2}
 e_N[-2\overline8(3x^2-2xy+3y^2)],
 \tag{1.1}
$$
$$
 U_N^{[2]}(z)=e^{izNA_N^{[2]}}M_N^{[2]}.
 \tag{1.2}
$$

Both matrices in (1.1) use the original modular-half convention. In
particular, the second argument `2k` of the Weyl operator is reduced
modulo `N`; it does not represent a change of the kick parameter.

**Theorem 1.** For every odd `N>=75`,

$$
 \frac1N\operatorname{Tr}(A_N^3)
 -\frac1N\operatorname{Tr}((A_N^{[2]})^3)
 >\frac3{10000}.
 \tag{1.3}
$$

Consequently, for every unitary `Q`,

$$
 \|A_N-QA_N^{[2]}Q^*\|_{2,N}>\frac1{40000},
 \qquad
 \|A_N-QA_N^{[2]}Q^*\|_{\mathrm{op}}>\frac1{40000},
 \tag{1.4}
$$

where `||X||_(2,N)^2=N^(-1)Tr(X^*X)`. The same lower bound holds for
the 1-Wasserstein distance between the two empirical Hamiltonian spectral
measures.

**Theorem 2.** Suppose additionally that `7` does not divide `N`. At every
nonzero algebraic parameter `z`, the spectra of `U_N(z)` and
`U_N^[2](z)` are not equal even after multiplying the whole spectrum by
one nonzero scalar. In particular, at the prescribed
`tau=10^(-80)`, there is no projective unitary similarity between these
two matrices, with an arbitrary complex unitary conjugating matrix.

Theorem 1 is a quantitative statement about the Hamiltonians. Theorem 2
is an exact statement about the kicked matrices; it supplies no useful
lower bound for their microscopic spectral distance. Neither assertion
says that these two different families cannot have the same universal
local limit. The point is narrower: their exact cyclotomic relationship
does not give an identification of the physical spectrum with its
Galois companion, even under unrestricted changes of basis.

## 2. Exact cubic moment of the Hamiltonian

Write `v=(k,l)` and `W_v=T_N(l,k)`. Direct multiplication gives

$$
 W_uW_v=e_N(\overline2\omega(u,v))W_{u+v},
 \quad
 \omega((k,l),(k',l'))=lk'-kl'.
 \tag{2.1}
$$

The trace of `W_v` is `N` if `v=0` modulo `N`, and zero otherwise.
For the original coefficient support one has `|k|<=9`, `|l|<=1`.
For `N>=29`, a sum of three support labels that is zero modulo `N`
is therefore zero in `Z^2`. If `u+v+w=0`, the phase in the triple
product is just `e_N(overline2 omega(u,v))`, since
`omega(u+v,w)=0`. Thus

$$
 \frac1N\operatorname{Tr}A_N^3
 =\sum_{j\in\mathbb Z}d_j e_N(\overline2j),
 \quad
 d_j=\sum_{\substack{u+v+w=0\\\omega(u,v)=j}}c_uc_vc_w.
 \tag{2.2}
$$

Here the coefficient sum is a fixed finite rational calculation. Its
complete nonzero table is

| `j` | `d_j` |
|---|---|
| `0` | `-273/20000` |
| `1,-1` | `9/800000` |
| `6,-6` | `3/800000` |
| `7,-7` | `-81/800000` |
| `8,-8` | `3/800000` |

For reproducibility, the exact calculation can be reconstructed as
follows. The coefficients of `r` are

$$
 r_0=1,\quad r_{\pm1}=\tfrac12,
 \quad r_{\pm7}=-\tfrac12,
 \quad r_{\pm6}=r_{\pm8}=-\tfrac14.
 \tag{2.3}
$$

The pure coefficients are obtained by adding the frequency-seven
cosine, `r/10-1/10`, and `r sin(2pi q)/100`. The last summand adds
`-i r_k/200` at `k+1` and `i r_k/200` at `k-1`. The mixed coefficients
are

$$
 c_{k,1}=\frac{-3-4i}{1000}r_k,
 \qquad
 c_{k,-1}=\frac{-3+4i}{1000}r_k.
 \tag{2.4}
$$

These operations produce precisely 32 nonzero coefficients, with
`c_(0,0)=0`. Substituting them in (2.2) gives 414 ordered nonzero
triple contributions and the displayed nine-entry table. The supplied
`r9_arithmetic_galois_check.py` performs these operations using pairs
of rational numbers for Gaussian rational coefficients and verifies
the table exactly. No floating point operations or external algebra
packages enter that check.

For odd `N` the modular inverse of two is `(N+1)/2`. If `x=pi/N`,

$$
 e_N(\overline2j)+e_N(-\overline2j)
 =2(-1)^j\cos(jx).
 \tag{2.5}
$$

Consequently (2.2) is the exact formula

$$
 C_1(N):=\frac1N\operatorname{Tr}A_N^3
 =-\frac{273}{20000}
 +\frac{3\cos8x+81\cos7x+3\cos6x-9\cos x}{400000}.
 \tag{2.6}
$$

For (1.1), multiplication of the second Weyl coordinate by two
multiplies the symplectic area by two. Its nonaliased triple sum
therefore replaces `e_N(overline2j)` by `e_N(j)`. Hence

$$
 C_2(N):=\frac1N\operatorname{Tr}(A_N^{[2]})^3
 =-\frac{273}{20000}
 +\frac{3\cos16x-81\cos14x+3\cos12x+9\cos2x}{400000}.
 \tag{2.7}
$$

The change of sign in the odd-area terms is essential. Replacing
modular halves by ordinary real halves would miss precisely this
effect.

## 3. Uniform quantitative separation

Subtracting (2.7) from (2.6) gives

$$
\begin{split}
400000(C_1-C_2)
={}&3(\cos8x-\cos16x)
 +81(\cos7x+\cos14x)\\
&+3(\cos6x-\cos12x)
 -9(\cos x+\cos2x).
\end{split}
\tag{3.1}
$$

For `N>=75`, the first and third terms are nonnegative because their
arguments lie in `[0,pi]`, where cosine is decreasing. The last term
is at least `-18`. From `cos t>=1-t^2/2` and `pi^2<10`,

$$
 \cos7x+\cos14x
 >2-\frac{1225}{N^2}
 \ge2-\frac{1225}{75^2}.
 \tag{3.2}
$$

Thus

$$
 400000(C_1-C_2)
 >81\left(2-\frac{1225}{75^2}\right)-18
 =\frac{3159}{25}>120,
 \tag{3.3}
$$

which proves (1.3). The rational checker separately verifies the
two rational inequalities in (3.3).

For completeness, both Hamiltonian norms are less than two. The
Fourier coefficient one-norm of the cosine is one; that of
`r/10-1/10` is `3/10`; and each remaining product has coefficient
one-norm at most `4/100`. This gives the bound `69/50<2`.
Every original and transformed Weyl summand is unitary, so the same
bound applies to both matrices.

Put `B=Q A_N^[2] Q^*` and `D=A_N-B`. The exact identity

$$
 A_N^3-B^3=A_N^2D+A_NDB+DB^2
 \tag{3.4}
$$

and normalized Hilbert--Schmidt Cauchy--Schwarz imply

$$
 \left|N^{-1}\operatorname{Tr}(A_N^3-B^3)\right|
 \le (\|A_N^2\|_{2,N}+\|BA_N\|_{2,N}+\|B^2\|_{2,N})
       \|D\|_{2,N}
 <12\|D\|_{2,N}.
 \tag{3.5}
$$

This proves the first bound (1.4), and `||D||_(2,N)<=||D||_op`
proves the second. Finally `x -> x^3` is 12-Lipschitz on `[-2,2]`.
For any coupling of the two empirical spectral measures its cubic
moment difference is at most 12 times the mean transportation cost.
Taking the infimum proves the stated Wasserstein bound. None of
these estimates restricts `Q` to algebraic matrices or to a
geometrically distinguished class.

## 4. From a frozen algebraic parameter to an entire identity

We use only the following published qualitative theorem:

> If finitely many exponents are distinct algebraic numbers and their
> coefficients are nonzero algebraic numbers, their exponential
> linear combination is nonzero.

This is Lindemann--Weierstrass, stated as Theorem 1.1 in
Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the
Exponentials of Algebraic Numbers*, ISSAC 2022, pp. 371--379,
DOI `10.1145/3476446.3536170`. The typeset author version,
<https://arxiv.org/pdf/2112.05004v2>, page 1, was opened and its
statement checked during this branch. The preceding sentence is a
paraphrase, not an additional assumption.

In particular, if

$$
 F(z)=\sum_j\beta_j e^{\gamma_jz},
 \qquad\beta_j,\gamma_j\in\overline{\mathbb Q},
 \tag{4.1}
$$

then, for every nonzero algebraic `z_0`,

$$
 F(z_0)=0\quad\Longrightarrow\quad F\equiv0.
 \tag{4.2}
$$

To check this implication, combine all equal `gamma_j`, remove zero
coefficients, and apply the published theorem to the distinct
algebraic numbers `gamma_j z_0`. Multiplication by the nonzero
number `z_0` preserves distinctness.

All entries of the original and transformed Hamiltonians and cats
are algebraic. A Hermitian algebraic Hamiltonian has real algebraic
eigenvalues and algebraic spectral projectors: for a distinct
eigenvalue `lambda`, its projector is

$$
 P_\lambda=\prod_{\mu\ne\lambda}
             \frac{A-\mu I}{\lambda-\mu}.
 \tag{4.3}
$$

The formula is valid also if eigenspaces have multiplicity. Expanding
`exp(izNA)` using these projectors shows that every elementary
characteristic coefficient of either `U(z)` is a finite exponential
polynomial of the form (4.1).

## 5. The load-bearing principal-minor input and its Galois transfer

The frozen source
`research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md`,
SHA-256
`f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df`,
proves for every odd `N` with `7` not dividing `N`:

1. `A_N` has `N` distinct eigenvalues.
2. Every square minor of `M_N` in an orthonormal `A_N` eigenbasis
   is nonzero.

The source was read, including the valuation proof, rather than
treated as a theorem solely from its title. The proof uses the exact
single Jacobi path, the Gaussian valuation with `v(omega)=1`,
internal-edge bounds `0<=v(b_j)<=1/2`, extremal endpoint
eigenvector-minor bounds, the consecutive-index minimization of
Fourier Vandermonde valuations, and the unique least-valuation term
in double Cauchy--Binet. It includes `5|N`. The source explicitly
does not establish these two assertions for mixed components when
`7|N`; neither does this branch.

Only the principal-minor part is needed here. Its transfer under
the indicated automorphism is entirely algebraic, so no new
valuation theorem for the companion family is being assumed.

To see this carefully, extend the cyclotomic automorphism to an
algebraic closure containing the eigenvalues and projectors. The
transformed matrix `sigma(A_N)=A_N^[2]` is Hermitian: the original
coefficients have conjugate pairs, and on the base cyclotomic field
`sigma` commutes with complex conjugation. The transformed cat is
`sigma(M_N)=epsilon M_N^[2]`, where `epsilon` is `1` or `-1`
according to the image of `sqrt(N)`; both choices are harmless.

The nonzero discriminant of `A_N` stays nonzero under `sigma`.
Its transformed eigenvalues are therefore the distinct real
eigenvalues of `A_N^[2]`, and the transforms of (4.3) are its genuine
orthogonal spectral projectors.

Let `I` be any `k`-element subset of the original eigenvalues and
let `P_I` be the sum of their projectors. Its corresponding
principal overlap determinant can be expressed without making a
choice of eigenvector phases as

$$
 b_I=\operatorname{Tr}\left[(\wedge^kP_I)(\wedge^kM_N)\right].
 \tag{5.1}
$$

Indeed `wedge^k P_I` is the rank-one orthogonal projection onto the
exterior product of those eigenvectors. Its trace against
`wedge^k M_N` is the determinant of that principal compression.
Equation (5.1) is algebraic in the matrix entries. Thus

$$
 \sigma(b_I)=\epsilon^k
 \operatorname{Tr}\left[(\wedge^k\sigma(P_I))
                        (\wedge^kM_N^{[2]})\right]\ne0.
 \tag{5.2}
$$

Since `I` was arbitrary, every principal minor of the companion cat
in its Hamiltonian eigenbasis is nonzero as well. This argument
does not assert that an arbitrary extension of `sigma` commutes
with conjugation on the whole algebraic closure; that unnecessary
assertion has been avoided by using the projector identity (5.1).

## 6. Proof of projective non-isospectrality

Suppose, to obtain a contradiction, that at a nonzero algebraic
`z_0` the companion spectrum is `eta` times the original spectrum.
For `N>=75`, the trace of either Hamiltonian is zero, since every
nonzero Fourier label remains nonzero modulo `N`. Therefore

$$
 \det U_N(z)=\det M_N,
 \qquad
 \det U_N^{[2]}(z)=\det M_N^{[2]}.
 \tag{6.1}
$$

Both are nonzero algebraic numbers. Taking determinants of the
proposed spectral relation shows that `eta^N` is algebraic and
nonzero. Hence `eta` itself is algebraic and nonzero.

Let `e_k` denote the elementary spectral coefficient. The assumed
relation implies, for every `0<=k<=N`,

$$
 e_k(U_N^{[2]}(z_0))-\eta^k e_k(U_N(z_0))=0.
 \tag{6.2}
$$

Each left side is an algebraic exponential polynomial, as checked
in Section 4. Equation (4.2) implies the entire identity

$$
 e_k(U_N^{[2]}(z))=\eta^k e_k(U_N(z))
 \quad\text{for every complex }z.
 \tag{6.3}
$$

Order the original Hamiltonian eigenvalues strictly as
`a_1>...>a_N` and the companion eigenvalues as
`a_1^[2]>...>a_N^[2]`. Section 5 permits this strict ordering and
proves that the principal minors for every initial eigenvalue set
are nonzero. At the complex parameters `z=-it/N`, `t>0`, the
principal-minor expansion gives

$$
 e_k(e^{tA_N}M_N)
 =b_{[k]}\exp\left(t\sum_{j=1}^k a_j\right)(1+o(1))
 \quad(t\to+\infty),
 \tag{6.4}
$$

and the same formula for the companion. This uses only a finite
sum: the initial `k` eigenvalues uniquely maximize the sum of
`k` distinct eigenvalues, so all other exponentials have strictly
smaller real exponent. There is no asymptotic in `N` in this step.

Take the logarithm of the modulus in (6.3) along this ray, divide
by `t`, and let `t` tend to infinity. The nonzero constant factors
and `eta^k` disappear. It follows that

$$
 \sum_{j=1}^k a_j^{[2]}=\sum_{j=1}^k a_j
 \quad(1\le k\le N).
 \tag{6.5}
$$

Successive differences give `a_j^[2]=a_j` for every `j`. Their
cubic moments would then agree, contradicting (1.3). This proves
Theorem 2, including arbitrary projective similarities at the
specified real parameter. The argument does not impose any
algebraicity condition on a hypothetical similarity matrix.

## 7. Other arithmetic mechanisms checked before this result

The nearest old results were inspected before selecting the Galois
test. Their actual scope matters, because several earlier
checkpoints record gaps that were subsequently closed.

* Canonical coprime CRT factorization of the *matrix* is already
  excluded in `affine_reversal_and_crt_obstructions.md`, Section 7.
  Its proof uses the exact entangling `(1,0)` Weyl coefficient and
  Lindemann--Weierstrass applied to realignment minors. It does not
  by itself classify arbitrary spectral tensor products.
* The seemingly open canonical oldform tower `N=7^(4r)`,
  `d=7^r` in `arithmetic_flat_packet_obstruction_test.md`, Section 5,
  is superseded by `arithmetic_comb_rescaled_gap.md`. The latter
  gives the original full kick a numerical escape gap `1/64` from
  every character sector when `N=d^2m`, `m<=sqrt(N)`, at
  `N>=10^140`, and a signed all-time estimate for the corresponding
  single character itinerary.
* The growing-order extension has the exact hypotheses
  `log N>=C_0 r^3`, `d>=N^(1/r)` and covers
  `log d>=C(log N)^(2/3)`. Its completed independent audit confirms
  that result while explicitly not extending the old all-time trace
  estimate to an order depending on `N`. This is not a new result
  of the present branch.
* The already established common antiunitary and algebraic
  symmetry exclusions are substantially wider than the Clifford
  group. The present calculation does not repeat them under a
  different name: it compares exact spectra of two distinct
  cyclotomic families.

The residual small-divisor oldform regime remains a possible place
to look for coherent superpositions, but a single-character escape
estimate does not control these superpositions. No such spectral
packet was constructed here. Likewise, the pure-power identity
`ord_(7^r)(S)=3*7^(r-1)` is an identity for the bare cat; it does
not survive the full fixed kick through an `o(1/N)` matrix error.

## 8. What the modified route still fails to establish

The exact Galois comparison above is sufficient to reject the
proposed replacement of the physical spectrum by an *identical*
Galois orbit. It does not rule out equality of limiting local
statistics, and does not justify using any averaged conjugate
family as a surrogate for the physical one.

Trying to strengthen Theorem 2 to useful quantitative spectral
separation immediately encounters the same precise difficulty:
(4.2) is a nonvanishing theorem, with no microscopic scale. The
earlier `quantitative_transcendence_limits.md` already supplies
explicit effective lower bounds for the original family; its
published effective Lindemann--Weierstrass specialization is far
smaller than every inverse power of `N`. The current cubic
Hamiltonian gap cannot be passed through the exponential at
time `tau*N` by a reverse Lipschitz estimate, because eigenphases
wrap around the circle. No such invalid reverse estimate is used.

For the actual requested family, the first fixed-test estimate
still unproved is

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \bigl(|\operatorname{Tr}(U_N^m)|^2-\min(m,N)\bigr)=o(1),
 \tag{8.1}
$$

where

$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},
 \quad u=\mathcal F^{-1}\phi,
 \quad b_*=\frac{|u|^2}{2(\int\phi)^2}.
 \tag{8.2}
$$

No conclusion about the sign or a nonzero limsup of (8.1) follows
from (1.3). Even a proof of (8.1) would leave the other admissible
tests and higher fixed orders. This report leaves that boundary
explicit rather than inserting a Galois universality assumption.

## 9. Reproducibility and input hashes

The exact checker and its JSON record are
`r9_arithmetic_galois_check.py` and
`r9_arithmetic_galois_check.json`. The JSON includes actual hashes
computed from the bytes of the following unchanged inputs.

| Input | SHA-256 |
|---|---|
| `Spectral_research_master.md` | `b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20` |
| `r8_original_obstruction_audit.md` | `d14ac3f6ab63c08d5b89937a4caaddde84343d279a83cbcf96e7aa5d4aced854` |
| `arithmetic_banded_time_reversal.md` | `39d017750473ee6779fc52656613b06dee5cd5591e4dbd288c64c10904cae6dd` |
| `arithmetic_padic_jacobi_simplicity.md` | `f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df` |
| `arithmetic_seven_chain_discriminant_checkpoint.md` | `eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f` |
| `affine_reversal_and_crt_obstructions.md` | `856f7e0d7373e1b3c260b20477969a12e3e78886836b11fd4eac9ddd9cc7642c` |
| `quantitative_transcendence_limits.md` | `35a8399e59a1ff390031cab2be39c654d08acf095326dcbc160dadca23f9eae4` |
| `arithmetic_flat_packet_obstruction_test.md` | `58bcfa0d7db85583d23f16c8ab1e5327926e11221b102cb7c6d0128037abb1cc` |
| `arithmetic_comb_rescaled_gap.md` | `898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f` |
| `counter_subpolynomial_comb_quantitative.md` | `3b59bd021e393489cd709073e683a2dec137333e0e657849b0636a9f85f90def` |

No old source or master file was edited. This branch has an exact
rational coefficient check and a written proof. A separate agent's
end-to-end audit has not yet been asserted.
