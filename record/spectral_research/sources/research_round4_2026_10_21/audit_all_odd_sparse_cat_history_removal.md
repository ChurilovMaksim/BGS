> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_all_odd_sparse_cat_history_removal.md`. Embedded SHA256: `f46c404d78344f4bfa71c0c657abd9119afc78d4fb90a79b6452fdf7cf8989e0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: fixed-density sparse histories in the exact Weyl adjoint

21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

## 1. Frozen statement and verdict

Audited source: `dual_all_odd_sparse_cat_history_removal.md`, SHA-256
`ebe8550d0a1598d0d90b1ecf66d1640b23b9e9151f7b67eac0eadf89707a62dd`.
The full source was read and its hash checked. It was not modified.

**Verdict: Theorem F and its exact signed pair-functional consequence are
proved as written.** The proof covers every sufficiently large odd N,
including arbitrary composites, with the original fixed tau. The deviation
fraction is a positive constant independent of N. The all-time correction
is $O(N^{-1/16})$, with exactly the displayed constant $K_0$.

This audit concerns the frozen statement above. Later suggestions involving
two or more Schatten factors are separate claims and are not silently being
inserted into it. No estimate of the retained histories, or of higher-order
factorial statistics, follows from this verdict.

## 2. Dimensions and the exact cat orientation

The modular matrices $W_N(k,l)=T_N(l,k)$ form an orthonormal basis under
$N^{-1}\operatorname{Tr}(X^*Y)$. Distinct shift coordinates give zero
trace; at equal shift coordinate, orthogonality of additive characters
handles the remaining modulation coordinate. Adjoint action by $U_N$
is unitary for this inner product and fixes the scalar basis vector. Thus
its restriction to the orthogonal complement has dimension
$M=N^2-1$ and is unitary. Only the scalar identity vector is removed;
other fixed vectors of the adjoint action are not being removed.

The kernel calculation in Section 2 has the correct orientation. To check
it independently, write
$\Phi(x,y)=-(3x^2-2xy+3y^2)/8$, with modular fractions.
Replacing $y$ by $z-l$ in $M_NW_N(k,l)$ changes its phase by
$$
-xl/4+(k+3l/4)z-kl/2-3l^2/8.
$$
For $k'=3k+2l$, $l'=4k+3l$, the phase in
$W_N(k',l')M_N$ changes by
$$
(k'-3l'/4)x+(l'/4)z+k'l'/2-3l'^2/8.
$$
Substitution gives the same expression term by term, including the constant
term $-kl/2-3l^2/8$. This proves
$M_NW_N(v)M_N^*=W_N(Sv)$ exactly, without a residual scalar sign.
The determinant of S is one, so S permutes all nonzero labels modulo
every N in question.

Consequently, with $w=Sv$,
$$
d_v=N^{-1}\operatorname{Tr}(E_N^*W_N(-w)E_NW_N(w)).
$$
The Weyl commutator applied to a Fourier mode u multiplies it by
$\exp(2\pi i u\cdot(-Jw/N))$. Thus the translation in the echo is
$z=-Jw/N=(-l/N,k/N)$, exactly as stated. The scalar sign changing
ordinary-half Weyl matrices to the modular ones cancels in conjugation.
For centered representatives and odd N,
$N\operatorname{dist}(z,\mathbb Z^2)=|w|_N$.

## 3. Echo input and what was independently checked

The exact-kick representation and the finite-type-16 estimate were already
proved and independently reconstructed in the following frozen sources:

* `audit_one_step_pinching_hs.md`, SHA-256
  `7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`;
* `audit_explicit_symbol_finite_type16.md`, SHA-256
  `1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`;
* its independent audit `dual_audit_explicit_finite_type16.md`, SHA-256
  `34ecf87576cb73990458a656200d9b6e41016f0082796beacea247106c4ed90e`.

The necessary raw input is the uniform echo formula
$$
d_v=\int b_t(x)b_t(x+z)
 e^{2\pi iN(S_t(x+z)-S_t(x))}\,dx+O(N^{-1}).
$$
Its error is uniform in every discrete translation. In the underlying
proof, the exact finite-grid alias identity supplies a bound on normalized
Hilbert--Schmidt norm from a supremum norm. Unitary Duhamel therefore
compares the exact kick with $Q_N(b_t e^{iS_t/h})$ in normalized
Hilbert--Schmidt norm with error $O(N^{-1})$. Pairing two factors costs
at most $\eta(2+\eta)$, for approximation error $\eta$, and does not
require an operator-norm bound for the oscillatory quantization. Nonzero
half-period aliases have a nonstationary phase after their integer Fourier
modulation is retained, and their summable remainder is uniform in z.
These were the points reconstructed in the cited audit; no classical
mixing statement is being used as a substitute.

The exact phase, not its first-order expansion, satisfies the uniform
finite-type-16 bound. The amplitudes $b_t(x)b_t(x+z)$ have a common C1
bound. Applying the proved localized oscillatory estimate at frequency
$2\pi N$, and absorbing fixed constants, gives
$$
|d_v|\le C_0(1+|Sv|_N)^{-1/16}+C_0/N.
$$
All constants depend only on the fixed family. Separately, unitarity of
the adjoint matrix gives the exact bound $|d_v|\le1$. The latter is
needed for all unmarked factors along an orbit.

## 4. The complete Weyl sum and its normalization

D is a weighted permutation, so its singular values are precisely
$|d_v|$. The centered shell of sup norm j has exactly $8j$ points,
for $1\le j\le(N-1)/2$. These shell counts sum to $N^2-1=M$,
confirming the normalization rather than only its asymptotic size.

Squaring the echo bound and applying $(a+b)^2\le2a^2+2b^2$ gives
$$
\|D\|_{\rm HS}^2
\le16C_0^2\sum_{j\le(N-1)/2}j(1+j)^{-1/8}
 +2C_0^2M/N^2.
$$
There are at most N summands and each is at most $N^{7/8}$.
Since $M\ge(8/9)N^2$,
$$
\frac{\|D\|_{\rm HS}^2}{M}
\le18C_0^2N^{-1/8}+2C_0^2N^{-2}
\le20C_0^2N^{-1/8}<25C_0^2N^{-1/8}.
$$
This proves the stated $5C_0N^{-1/16}$ normalized Hilbert--Schmidt
bound. The summation is over one exact finite matrix; it is not an average
of the original spectral statistic over an added parameter.

## 5. Fixed cutoff, no wrap, and the quadratic invariant

The definition $R_0=\lceil(4C_0)^{16}\rceil$, together with
$N\ge4C_0$, gives $|d_{S^{-1}w}|\le1/2$ whenever
$\|w\|_\infty\ge R_0$. Both contributions, including the exact-kick
remainder, are accounted for in the two quarters of this bound.

If all centered labels in an orbit segment lie in the box
$\|w_j\|_\infty\le R_0$, then
$\|Sw_j\|_\infty\le7R_0<N/2$, because $N\ge16R_0$.
Thus the ordinary integer vector $Sw_j$ is already the centered lift
of the next label. There is no wrap, and the segment is an exact integer
orbit of S.

Direct expansion verifies preservation of
$Q(k,l)=2k^2-l^2$. For a nonzero integer vector, this Q cannot be zero:
$l^2=2k^2$ would successively force both integers to be divisible by
arbitrarily high powers of two. Hence $|Q|\ge1$. This is an integer
assertion on the lifted segment, not the false assertion that Q must be
nonzero modulo N.

For $a=k+l/\sqrt2$, $b=k-l/\sqrt2$, one has
$2ab=Q$, and S multiplies a by $\lambda=3+2\sqrt2$.
The low-box bounds imply $|a_j|,|b_j|\le2R_0$, and so
$|a_0|\ge1/(4R_0)$. A segment of L low labels would therefore imply
$\lambda^{L-1}\le8R_0^2$. The chosen
$L=\lceil\log(8R_0^2)/\log\lambda\rceil+2$ makes this impossible.
The spare integer in L handles equality and rounding strictly.

This proves that every length-L segment of every nonzero orbit has a high
label. No field property, prime factorization, or order estimate for S
appears. The zero orbit really would be an obstruction; excluding the
scalar Weyl coordinate was therefore necessary.

## 6. Powers and the cost of every run

The exact formula
$$
D^m e_v=\left(\prod_{j=0}^{m-1}d_{S^jv}\right)e_{S^mv}
$$
has orthogonal output columns. Each disjoint length-L block in a product
contains a factor at most $1/2$, since its echo label is
$S^{j+1}v$, still a consecutive nonzero orbit label. All other factors
are at most one. Consequently
$$
\|D^m\|\le2^{-\lfloor m/L\rfloor}\le2e^{-\kappa m},
\qquad \kappa=\log2/L.
$$
This also holds at m=0. The prefactor two is independent of N.

Since $\|R_N\|\le\|C\|+\|D\|\le2$, a word with j R factors
has j+1 possibly empty D runs and satisfies
$$
\|\text{word}\|
\le2^{j+1}2^j e^{-\kappa(n-j)}
=2e^{-\kappa n}(4e^\kappa)^j.
$$
For the Hilbert--Schmidt version, choose one D factor. Removing it splits
one run into two, leaving at most j+2 runs, with total D length n-j-1.
The ideal inequality
$\|AXB\|_{\rm HS}\le\|A\|\|X\|_{\rm HS}\|B\|$
then gives exactly
$$
\|\text{word}\|_{\rm HS}
\le4e^\kappa\|D\|_{\rm HS}e^{-\kappa n}(4e^\kappa)^j.
$$
Using a prefactor two even for empty runs overestimates their norm one and
is legitimate. This explicitly accounts for the extra run; it does not
assume commuting generators or cyclic rearrangement of the matrix norm.
The trace bound loses precisely $\sqrt M$, by Cauchy--Schwarz against
the M dimensional identity. After division by M the remaining factor is
$\|D\|_{\rm HS}/\sqrt M$, as in (1.8).

## 7. Entropy estimate with the prescribed fixed density

The finite constant $0<\kappa<1$ gives
$0<\delta=\kappa^2/32<1/2$. Hence every selected positive-length word
has at least one D. The binomial estimate with
$x=\delta/(1-\delta)<1$ is valid for the actual integer cutoff,
because $x^j\ge x^{\delta n}$ whenever $j\le\lfloor\delta n\rfloor$.
It gives
$\sum_{j\le\lfloor\delta n\rfloor}\binom nj\le e^{nH(\delta)}$.

Also $H(\delta)\le\delta\log(e/\delta)$. With $A=4e^\kappa$,
$$
H(\delta)+\delta\log A
\le\frac{\kappa^2}{32}
 [\log128+1+\kappa+2\log(1/\kappa)]<\kappa/4.
$$
Indeed, $\log128<5$, $\kappa\le1$, and
$2\kappa\log(1/\kappa)\le2/e<1$; multiplying the bracket by kappa
gives a number strictly smaller than eight. The elementary assertion
$\log128<5$ is also correctly certified in the source: the Taylor
polynomial of $e^5$ through degree seven already exceeds 128.

Since $A^j\le A^{\delta n}$, the sum of the word bounds is at most
the corresponding prefactor times $e^{-3\kappa n/4}$. This proves
both (1.7) and (1.8), uniformly for every positive n. In particular there
is no early/late cutoff, and no N-dependent transient factor has been
hidden in the word count.

The positive-time geometric sum equals
$(e^{3\kappa/4}-1)^{-1}$. Inserting the normalized Hilbert--Schmidt
bound and $M/N^2<1$ gives exactly
$$
N^{-2}\sum_{n\ge1}|\operatorname{Tr}B_{n,N}|
\le\frac{20e^\kappa C_0}{e^{3\kappa/4}-1}\,N^{-1/16}.
$$

## 8. Exact passage to the original squared trace

The full adjoint eigenvalues are the pairwise eigenvalue quotients of
$U_N$, so its nth trace is $|\operatorname{Tr}U_N^n|^2$. Excluding
just the scalar identity subtracts exactly one, giving (8.1). Inserting
$C^n=B_{n,N}+(C^n-B_{n,N})$ therefore gives the source's exact finite
identity (8.3), including the CUE centering term $\min(n,N)-1$.

The correction sum is absolutely convergent by the theorem. Multiplication
by any bounded complex weights costs at most their common bound W. For
the original finite Fourier window this gives an error $O(N^{-1/16})$
at every fixed bandwidth. For positive-s Abel weights, the two separate
series also converge for each fixed N: the original squared trace is
bounded by $N^2$, and the retained adjoint trace is bounded by M plus
the exponentially decaying trace of B. The correction bound is uniform in
s because the weights have modulus at most one. No claim of uniform smallness
of the original Abel tail is made.

Finally $C_{-u,-v}=\overline{C_{u,v}}$ follows by taking adjoints inside
the trace and cyclically permuting. D and R inherit this symmetry since S
commutes with label negation, and so does each word. Thus the selected
traces are real. The absolute estimates do not require this additional
observation, but it confirms the interpretation for real pair weights.

## 9. Precise remaining gap

No gap was found in Theorem F. Its sparse path sector is classified in the
original complex adjoint matrix, not in a matrix of probabilities. Thus
the correction already includes the complete squared original trace; no
cross term from that representation is missing.

The exact first unproved pair estimate after this removal is (9.1) of the
source: the weighted, signed sum of the retained adjoint traces, centered
by $\min(n,N)-1$, must tend to zero on every fixed window of order N.
The retained paths have more than $\delta n$ deviations from S. The
present proof does not control their coherent cancellation, and it does
not prove the higher-order estimates required by $H_{\rm diag}$.
