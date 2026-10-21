> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_all_odd_sparse_cat_history_removal.md`. Embedded SHA256: `ebe8550d0a1598d0d90b1ecf66d1640b23b9e9151f7b67eac0eadf89707a62dd`.
> [Thematic guide](../../topics/histories.md).

# All-odd, all-time removal of a fixed density of sparse cat histories in the exact Weyl adjoint

21 October 2026. New result for the prescribed fixed family, with
$\tau=10^{-80}$. No average over N, the kick, or an independent random
parameter is introduced.

This theorem removes a specific collection of coherent paths from the complete
pair-trace functional with a proved error $O(N^{-1/16})$. The admissible
deviation density is a fixed positive constant, independent of N. The theorem
does not evaluate the remaining paths and does not establish $H_{\rm diag}$.

## 1. Established inputs and exact statement

The exact-kick translation echo representation used below is proved in
`counter_one_step_pinching_hs.md`, SHA-256
`a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`,
Sections 1--5, and independently audited in
`audit_one_step_pinching_hs.md`, SHA-256
`7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.
It follows from the exact finite-shift equation, with all modular aliases
retained, and a proved normalized Hilbert--Schmidt remainder.

Its explicit finite-type exponent is proved in
`audit_explicit_symbol_finite_type16.md`, SHA-256
`1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`,
and independently checked in
`dual_audit_explicit_finite_type16.md`, SHA-256
`34ecf87576cb73990458a656200d9b6e41016f0082796beacea247106c4ed90e`.
The exact echo, its orientation, and the specific consequences needed here
are stated and verified in Section 2 below. None of the quantitative
Lindemann--Weierstrass bounds from the earlier Markov branch are used.

Use the original modular Weyl basis
$$
W_N(k,l)=T_N(l,k)
$$
with inner product $N^{-1}\operatorname{Tr}(X^*Y)$. Set
$$
\Lambda_N=(\mathbb Z/N\mathbb Z)^2\setminus\{0\},\qquad M=N^2-1,
$$
$$
C_{u,v}=\frac1N\operatorname{Tr}
 \bigl(W_N(u)^*U_NW_N(v)U_N^*\bigr),\qquad u,v\in\Lambda_N.
\tag{1.1}
$$
Thus C is the M by M unitary adjoint matrix on the traceless space. The scalar
identity mode is excluded throughout. Let
$$
S=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
d_v=C_{Sv,v},\qquad
D e_v=d_ve_{Sv},\qquad R_N=C-D.
\tag{1.2}
$$
The label map S is a permutation for every N since its determinant is one.
D retains exactly the cat-permutation entry in each column, including its
complex phase. Every other entry of C is retained in R_N, and
$(R_N)_{Sv,v}=0$. We do not square entry magnitudes or replace C by a
stochastic matrix.

Section 2 gives fixed $C_0\ge1$, $N_e$, with $\epsilon=1/16$, such that
$$
|d_v|\le C_0(1+|Sv|_N)^{-\epsilon}+C_0/N
\tag{1.3}
$$
for every odd $N\ge N_e$ and every nonzero v. Here $|w|_N$ is the
Euclidean norm of the centered integer representative of w. Fix once and for
all
$$
R_0=\left\lceil(4C_0)^{16}\right\rceil,\qquad
\lambda=3+2\sqrt2,
$$
$$
L=\left\lceil\frac{\log(8R_0^2)}{\log\lambda}\right\rceil+2,
\qquad \kappa=\frac{\log2}{L},\qquad
\boxed{\delta=\frac{\kappa^2}{32}>0.}
\tag{1.4}
$$
All logarithms are natural. These quantities depend only on the exact fixed
family and are independent of N. Enlarge a fixed $N_0$ so that
$$
N_0\ge N_e,\quad N_0\ge3,\quad N_0\ge16R_0,\quad N_0\ge4C_0.
\tag{1.5}
$$

For each positive n, let $B_{n,N}$ be the sum of all words of length n in
the two noncommuting letters D and R_N containing at most
$\lfloor\delta n\rfloor$ copies of R_N. For example, the sum at n=1 is D.
The exact expansion of C to the nth power splits as
$$
C^n=B_{n,N}+(C^n-B_{n,N}).
\tag{1.6}
$$
In matrix-entry language, B contains precisely the Weyl paths with at most
$\lfloor\delta n\rfloor$ steps deviating from the map $v\mapsto Sv$.
This is a disjoint classification: D and R_N have disjoint entry supports.

**Theorem F.** For every odd $N\ge N_0$, every positive integer n, and
$\eta=e^{-3\kappa/4}<1$,
$$
\boxed{\|B_{n,N}\|_{2\to2}\le2\eta^n,}
\tag{1.7}
$$
$$
\boxed{\frac{|\operatorname{Tr}B_{n,N}|}{M}
 \le4e^\kappa\frac{\|D\|_{\rm HS}}{\sqrt M}\eta^n,
\qquad
\frac{\|D\|_{\rm HS}}{\sqrt M}\le5C_0N^{-1/16}.}
\tag{1.8}
$$
Here HS denotes the ordinary Hilbert--Schmidt norm of the M by M coefficient
matrix, distinguished from the original N by N matrices used in the echo.
Consequently
$$
\boxed{
\frac1{N^2}\sum_{n=1}^{\infty}|\operatorname{Tr}B_{n,N}|
\le K_0N^{-1/16},\qquad
K_0=\frac{20e^\kappa C_0}{e^{3\kappa/4}-1}.
}
\tag{1.9}
$$
This covers early times as well as times of order N and arbitrarily late times.
There is no gap between two time ranges and no hidden N-dependent transient
factor in the final estimate.

## 2. Exact orientation of the Weyl echo

First, the original quadratic kernel gives
$$
M_NW_N(v)M_N^*=W_N(Sv).
\tag{2.1}
$$
One can verify the orientation directly in the kernel. With v=(k,l), the
phase of $M_NW_N(k,l)$, after replacing the summation variable y by z-l,
is the original quadratic phase in (x,z) plus
$$
-\frac{xl}{4}+\left(k+\frac{3l}{4}\right)z
-\frac{kl}{2}-\frac{3l^2}{8}.
$$
The phase of $W_N(3k+2l,4k+3l)M_N$ has exactly these additional terms.
All halves and quarters in this verification are modular inverses, valid for
the odd N in the question. This proves (2.1) without changing the Weyl convention.

Write $E_N=e^{i\tau NA_N}$ and put $w=Sv$. By (1.1), (2.1), and a
cyclic trace permutation,
$$
d_v=\frac1N\operatorname{Tr}
 \bigl(W_N(w)^*E_NW_N(w)E_N^*\bigr)
=\frac1N\operatorname{Tr}
 \bigl(E_N^*W_N(-w)E_NW_N(w)\bigr).
\tag{2.2}
$$
For w=(k,l), the Weyl operator in the positive translation position of this
echo is $W_N(-w)=T_N(-l,-k)$. The exact translation convention of the
ordinary-half symbol is therefore
$$
\boxed{z=(-l/N,k/N)=-Jw/N,
\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.}
\tag{2.3}
$$
Indeed the Weyl commutator multiplies the symbol Fourier mode u by
$e_N(\omega(-w,u))=\exp(2\pi i u\cdot(-Jw/N))$.
The scalar sign relating the original Weyl matrices to the ordinary-half ones
cancels in conjugation. In particular,
$$
N\operatorname{dist}(z,\mathbb Z^2)=|w|_N.
\tag{2.4}
$$

The established exact-kick echo representation, with the fixed analytic center
action $S_t$, the fixed smooth amplitude $b_t$, and
$t=\tau/(2\pi)$, is
$$
d_v=\int_{\mathbb T^2}b_t(x)b_t(x+z)
 e^{i(2\pi N)(S_t(x+z)-S_t(x))}\,dx+O(N^{-1}),
\tag{2.5}
$$
uniformly in v. Specifically, the normalized HS approximation to E_N has
error O(N^{-1}); the exact trace pairing retains the half-period alias terms;
their nonzero Fourier modulations have a phase derivative bounded away from
zero and sum to a uniform error of arbitrarily high inverse-polynomial order.
These are the proved statements of Sections 4--5 of the first cited source,
not a classical mixing assumption.

The explicit finite-type-16 lemma applies to the exact S_t and to the uniformly
C1-bounded amplitudes $b_t(x)b_t(x+z)$. It bounds the integral in (2.5) by
$C(1+N\operatorname{dist}(z,0))^{-1/16}$. Equation (2.4) gives (1.3),
after increasing a fixed constant C0. At the same time, unitarity of C gives
the exact elementary bound
$$
|d_v|\le1.
\tag{2.6}
$$

## 3. The normalized HS estimate for the weighted permutation

Since D has exactly one possible nonzero entry per column,
$$
\|D\|_{\rm HS}^2=\sum_{v\in\Lambda_N}|d_v|^2.
$$
The map v to Sv permutes the nonzero labels. In centered integer coordinates,
the shell $\max(|w_1|,|w_2|)=j$ has 8j points for
$1\le j\le(N-1)/2$, and $|w|_N\ge j$. Squaring (1.3), using
$(a+b)^2\le2a^2+2b^2$, and putting $\epsilon=1/16$, gives
$$
\|D\|_{\rm HS}^2
\le16C_0^2\sum_{j\le(N-1)/2}j(1+j)^{-2\epsilon}
 +\frac{2C_0^2M}{N^2}
\le16C_0^2 N^{2-2\epsilon}+\frac{2C_0^2M}{N^2}.
\tag{3.1}
$$
The final sum estimate follows simply by bounding at most N summands by
$N^{1-2\epsilon}$. Since $M\ge(8/9)N^2$ for $N\ge3$, division by M
yields
$$
\frac{\|D\|_{\rm HS}^2}{M}
\le18C_0^2N^{-2\epsilon}+2C_0^2N^{-2}
\le20C_0^2N^{-2\epsilon}<25C_0^2N^{-2\epsilon}.
\tag{3.2}
$$
This proves the HS bound in (1.8). It is a deterministic complete sum over the
Weyl basis for a single N, not an extra randomness or a parameter average.

## 4. Uniform escape from a fixed frequency box

The chosen R0 and N0 ensure that if the centered representative of w has
$\|w\|_\infty\ge R_0$, then (1.3) gives
$$
|d_{S^{-1}w}|
\le C_0(1+R_0)^{-1/16}+C_0/N\le\frac14+\frac14=\frac12.
\tag{4.1}
$$
We next prove that every nonzero modular S orbit leaves the fixed box
$\|w\|_\infty\le R_0$ in every L consecutive labels, uniformly in odd
$N\ge N_0$.

Suppose the contrary for a segment $w_0,\ldots,w_{L-1}$. Take its centered
integer lifts. Whenever $\|w_j\|_\infty\le R_0$,
$\|Sw_j\|_\infty\le7R_0<N/2$ by (1.5). Thus no modular wrap occurs and
the lifted segment satisfies $w_j=S^jw_0$ as an identity of integer vectors.

The integer quadratic form
$$
Q(k,l)=2k^2-l^2
$$
is preserved by S, as direct expansion shows. For a nonzero integer vector it
is nonzero: otherwise $l^2=2k^2$, and parity followed by infinite descent
forces k=l=0. Hence $|Q(w_0)|\ge1$.

Define
$$
a_j=k_j+l_j/\sqrt2,\qquad b_j=k_j-l_j/\sqrt2.
$$
Then $2a_jb_j=Q(w_j)$, $a_j=\lambda^ja_0$, and
$|a_j|,|b_j|\le2R_0$ on the assumed segment. In particular
$|a_0|\ge1/(4R_0)$. The last label therefore implies
$$
\lambda^{L-1}\le8R_0^2.
\tag{4.2}
$$
But the definition of L gives $\lambda^{L-1}>8R_0^2$, a contradiction.
This proves the escape assertion over every modulus in the stated range,
including all composite and squarefree moduli. The scalar zero label would
invalidate the argument, which is why it was removed at the definition of C.

## 5. Every power of D has a fixed exponential bound

The exact weighted-permutation formula is
$$
D^m e_v=
 \left(\prod_{j=0}^{m-1}d_{S^jv}\right)e_{S^mv}.
\tag{5.1}
$$
Because $S^m$ is a permutation, these output columns are orthogonal, and
$\|D^m\|$ is the maximum modulus of the displayed products.
The relevant frequency for the jth factor is $S^{j+1}v$; these still form
consecutive nonzero S-orbit labels. In each disjoint block of L factors, the
escape lemma gives a factor bounded by one half using (4.1). All other factors
are bounded by one using (2.6). Therefore, for every $m\ge0$,
$$
\boxed{\|D^m\|\le2^{-\lfloor m/L\rfloor}
 \le2e^{-\kappa m}.}
\tag{5.2}
$$
The m=0 case is included. The prefactor two, the window L, and the exponent
kappa are all independent of N. In particular every eigenvalue of D has
modulus at most $e^{-\kappa}$: apply (5.2) to an eigenvector and let m tend
to infinity. No such spectral contraction is claimed for the full unitary C.

## 6. Words with deviations: transient factors and one HS factor

By unitarity and (2.6), $\|C\|=1$, $\|D\|\le1$ and
$\|R_N\|\le2$. A word with j copies of R_N can be grouped into j+1
possibly empty consecutive D runs. Their lengths sum to n-j. Applying (5.2)
to each run gives
$$
\|\mathrm{word}\|
\le2^{j+1}2^j e^{-\kappa(n-j)}
=2e^{-\kappa n}(4e^\kappa)^j.
\tag{6.1}
$$
This accounts for the prefactor of every D run, including empty runs.

If j is less than n, choose one D factor and use its HS norm. Splitting its
original run at that factor leaves at most j+2 possibly empty D runs, whose
total length is n-j-1. The Hilbert--Schmidt ideal inequality gives
$$
\|\mathrm{word}\|_{\rm HS}
\le2^{j+2}2^j e^{-\kappa(n-j-1)}\|D\|_{\rm HS}
=4e^\kappa\|D\|_{\rm HS}
 e^{-\kappa n}(4e^\kappa)^j.
\tag{6.2}
$$
The ideal inequality follows, for example, by applying the ordinary operator
norm to the columns on one side and to the adjoint on the other; it is valid
regardless of the positions or commutators of the letters. Finally
$|\operatorname{Tr}X|\le\sqrt M\|X\|_{\rm HS}$, by Cauchy--Schwarz against
the identity, proves
$$
\frac{|\operatorname{Tr}(\mathrm{word})|}{M}
\le4e^\kappa\frac{\|D\|_{\rm HS}}{\sqrt M}
 e^{-\kappa n}(4e^\kappa)^j.
\tag{6.3}
$$
Since $\delta<1$, all words selected in B have j<n. Thus (6.3) applies
also at the earliest positive times; no auxiliary early-time estimate is needed.

## 7. An explicit fixed deviation fraction closes the binomial sum

For $0<\delta<1/2$, let
$$
H(\delta)=-\delta\log\delta-(1-\delta)\log(1-\delta).
$$
For every n,
$$
\sum_{j\le\lfloor\delta n\rfloor}\binom nj\le e^{nH(\delta)}.
\tag{7.1}
$$
To prove this with the stated rounding, put $x=\delta/(1-\delta)<1$.
For j at most $\lfloor\delta n\rfloor$, $x^j\ge x^{\delta n}$, so the
sum is at most $x^{-\delta n}(1+x)^n=e^{nH(\delta)}$.
Also $H(\delta)\le\delta\log(e/\delta)$, since
$-(1-\delta)\log(1-\delta)\le\delta$.

Here $0<\kappa<1$ and $\delta=\kappa^2/32<1/2$. With
$B=4e^\kappa>1$,
$$
H(\delta)+\delta\log B
\le\frac{\kappa^2}{32}
 \left[\log128+1+\kappa+2\log(1/\kappa)\right]
<\frac\kappa4.
\tag{7.2}
$$
For the final strict bound, $\log128<5$, $\kappa\le1$, and
$\kappa\log(1/\kappa)\le1/e<1/2$. The bracket multiplied by kappa is
therefore strictly below $7\kappa+1\le8$. The elementary maximum
$u\log(1/u)\le1/e$ on $(0,1]$ follows by differentiating it. The
constant inequality $\log128<5$ follows from $e^5>128$, which already
holds for the Taylor sum of $e^5$ through degree seven.

Using $B^j\le B^{\delta n}$ in (7.1), and summing (6.1), (6.3) over the
$\binom nj$ possible placements of the j letters, gives
$$
\|B_{n,N}\|\le2e^{-3\kappa n/4},
$$
$$
\frac{|\operatorname{Tr}B_{n,N}|}{M}
\le4e^\kappa\frac{\|D\|_{\rm HS}}{\sqrt M}
 e^{-3\kappa n/4}.
\tag{7.3}
$$
Thus all phases and all interference are included in the exact word sum being
bounded. Summing the geometric sequence and using (3.2), with $M/N^2<1$,
proves (1.9) with its displayed K0.

## 8. Consequence for the complete signed pair-trace functional

For the original unitary, the full adjoint eigenvalues are
$e^{2\pi i(\theta_j-\theta_k)}$. Removing the scalar identity mode gives
the exact identity
$$
\operatorname{Tr}C^n=|\operatorname{Tr}U_N^n|^2-1.
\tag{8.1}
$$
For any complex array of weights with $\sup_{n,N}|w_{n,N}|\le W$, (1.9)
therefore yields
$$
\boxed{
\left|\frac1{N^2}\sum_{n\ge1}w_{n,N}\operatorname{Tr}B_{n,N}\right|
\le W K_0N^{-1/16}.
}
\tag{8.2}
$$
The correction series is absolutely convergent, uniformly bounded as stated.
For a finite sum this is the exact change in the complete pair-trace functional
when all the designated sparse dual histories are removed:
$$
\begin{aligned}
&\frac1{N^2}\sum_nw_{n,N}
 \bigl[|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr]\\
&\quad-
\frac1{N^2}\sum_nw_{n,N}
 \bigl[\operatorname{Tr}(C^n-B_{n,N})-(\min(n,N)-1)\bigr]
=\frac1{N^2}\sum_nw_{n,N}\operatorname{Tr}B_{n,N}.
\end{aligned}
\tag{8.3}
$$
In particular, the result is uniform over every window $1\le n\le BN$,
with no restriction on the fixed B, and over the original pair-test weights
$|\widehat b(n/N)|^2$. It also applies to every infinite Abel window
$w_{n,N}=e^{-2sn/N}$, $s>0$, with a correction bound independent of s.
Both original Abel series converge at each fixed N; no uncontrolled infinite
tail is hidden in the comparison. For general bounded weights whose full
series need not converge separately, (8.2) still defines the correction and
bounds every finite truncation uniformly.

For completeness the traces of B are real, although absolute values above do
not require this. The original Weyl matrices obey $W_N(v)^*=W_N(-v)$, so
$C_{-u,-v}=\overline{C_{u,v}}$. D and R_N inherit this identity because
$S(-v)=-Sv$; so does every selected word sum. Taking the trace pairs the
conjugate nonzero labels. This confirms the interpretation as a signed real
contribution for real pair-test weights.

No cross-term between a removed and a retained original eigenphase amplitude
has been omitted: (8.1)--(8.3) operate directly on the exact adjoint trace that
already equals the complete squared original trace minus one. The retained
quantity is not asserted to be the squared trace of another unitary, nor to be
nonnegative on its own.

## 9. The remaining unproved estimate

This theorem eliminates every dual Weyl history whose non-cat steps have
density at most the fixed $\delta>0$ in (1.4), for all sufficiently large
odd N. Prime, squarefree and arbitrary composite dimensions are all covered.
The use of the original fixed tau is essential to choosing R0, L, kappa and
delta independently of N; they may be numerically very unfavorable constants.

The first still-unproved pair estimate is now precisely
$$
\frac1{N^2}\sum_{1\le n\le BN}|\widehat b(n/N)|^2
\left[\operatorname{Tr}(C^n-B_{n,N})-(\min(n,N)-1)\right]
\longrightarrow0
\tag{9.1}
$$
for every admissible fixed b with Fourier support in $[-B,B]$.
The surviving histories have more than $\delta n$ departures from the exact
cat permutation. No decorrelation or sign cancellation among those histories
has been proved here, and no higher-order factorial-statistics conclusion is
being inferred from this removal theorem.
