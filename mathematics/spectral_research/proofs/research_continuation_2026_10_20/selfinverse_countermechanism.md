> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/selfinverse_countermechanism.md`. Embedded SHA256: `5eaa20f8d1c3621ac69c526db33ba41eed761cbbbd637a8ed77a12bcdedeaf42`.
> [Thematic guide](../../topics/closure.md).

# What self-inversiveness and an exact all-time orbit formula do not force

Independent research pass, 2026-10-20.

## Result and its precise scope

There is a rigorous obstruction to deriving the requested Heisenberg-time plateau from the following information alone: unitarity, exact Newton and self-inversive identities, an exact orbit expansion at every integer time, and a same-orbit sum rule of the form D_m = m + O(m^2 theta^m).

The obstruction is constructive. Two sequences of deterministic unitary matrices can have:

* identical traces at every time m < L_N, where L_N/N tends to 1/2;
* identical determinants, and therefore the same global phase in the self-inversive identity;
* simple spectra, no scalar returns at any positive integer time, and no vanishing power traces;
* exact closed-word orbit expansions for every m, with zero remainder;
* same-orbit diagonals D_m = m + O(m^2 theta^m), with constants independent of both m and N;

yet their weighted form-factor defects differ in the limit by a strictly positive constant. Their local point processes also have different limits detected by a fixed bounded continuous Laplace observable.

These are matrix closed-word dynamics, not quantizations of the fixed two-dimensional Anosov map in the original problem. Thus this is not a counterexample to the original H_diag or Sine_2 conjecture. It disproves the proposed general algebraic mechanism for obtaining that conjecture from the already established ingredients. The extra information must use the particular action correlations of the original map, rather than exactness or self-inversiveness alone.

## 1. The fixed test and the exact algebraic identities

Let

$$
\varphi(x)=\begin{cases}e^{-1/(1-x^2)},&|x|<1,\\0,&|x|\ge1,\end{cases}
\quad I=\int\varphi,
\quad \widehat b_*(u)=\frac{(\varphi*\varphi)(u)}{2I^2},
\quad w(u)=|\widehat b_*(u)|^2.
$$

Then w is continuous, is supported in [-2,2], vanishes at 2, and is strictly positive on (-2,2). Strict positivity follows by integrating the positive product over the nonempty overlap of (-1,1) and (u-1,u+1).

For an N-dimensional unitary U put

$$
p_m=\operatorname{Tr}U^m,\qquad
\Delta_N(U)=\frac1{N^2}\sum_{m\ge1}w(m/N)
\bigl(|p_m|^2-\min(m,N)\bigr).
\tag{1}
$$

The benchmark term converges by a Riemann sum:

$$
\frac1{N^2}\sum_{m\ge1}w(m/N)\min(m,N)
\longrightarrow C_w:=\int_0^2w(u)\min(u,1)\,du.
\tag{2}
$$

If

$$
P_U(z)=\det(I-zU)=\sum_{j=0}^Nc_jz^j,
$$

unitarity gives

$$
c_{N-j}=c_N\overline{c_j},\qquad |c_N|=1.
\tag{3}
$$

Indeed, this follows directly by replacing each eigenvalue by the reciprocal of its conjugate in the product defining P_U. Newton's identities are

$$
jc_j=-\sum_{r=1}^jp_rc_{j-r},\quad 1\le j\le N,
\tag{4}
$$

and the trace recurrence for m > N is

$$
p_m=-\sum_{j=1}^Nc_jp_{m-j}.
\tag{5}
$$

For odd N, exact traces through (N-1)/2 and the determinant determine the full characteristic polynomial. This is an algebraic reconstruction statement, not a statistical estimate. In particular, a proof must not infer that data through an Ehrenfest-scale cutoff determine the missing coefficients near N/2, or that first and second moments of shorter traces control the nonlinear products in (4)-(5).

## 2. Two polygon blocks with an arbitrary common deterministic block

Take odd N and odd integers d_N with d_N = o(N), and set

$$
L=L_N=(N-d_N)/2.
$$

Let Q_N be any prescribed d_N-dimensional unitary matrix. No averaging over Q_N is used. Define

$$
C_L=\operatorname{diag}(e^{2\pi ij/L})_{0\le j<L},
$$

$$
V_N(\vartheta)=Q_N\oplus e^{i\vartheta/L}C_L
\oplus e^{-i\vartheta/L}C_L.
\tag{6}
$$

Its characteristic polynomial is exactly

$$
P_{V_N(\vartheta)}(z)
=P_{Q_N}(z)\left(1-2\cos\vartheta\,z^L+z^{2L}\right).
\tag{7}
$$

Its determinant is det Q_N, independent of vartheta. If q_m = Tr Q_N^m, then

$$
p_m(\vartheta)=q_m+2L\,\mathbf1_{L\mid m}
\cos(m\vartheta/L).
\tag{8}
$$

Consequently all traces for 1 <= m < L, and all secular coefficients of degree less than L, are independent of vartheta. Every pseudo-orbit expression formed algebraically from those traces is also identical between the examples. The first potentially different coefficient has degree L, asymptotically half the Heisenberg time.

Choose two sequences of nonzero rational phases

$$
\vartheta_N^{A}\longrightarrow0,
\qquad
\vartheta_N^{B}\longrightarrow\pi/2.
\tag{9}
$$

For example, vartheta_N^A = N^(-2) and a positive rational approximation to pi/2 with error less than N^(-2) suffice. They remain algebraic and are never zero or a nonzero integer multiple of pi.

### 2.1 A weighted defect gap independent of the common block

Write

$$
S_N(\vartheta)=N^{-2}\sum_{m\ge1}w(m/N)|p_m(\vartheta)|^2,
\quad B_N(Q)=N^{-2}\sum_{m\ge1}w(m/N)|q_m|^2.
$$

For all sufficiently large N, only r = 1,2,3,4 occur among m = rL in the support of the sum. Expanding (8) gives

$$
S_N(\vartheta)=B_N(Q)
+\frac{4L^2}{N^2}\sum_{r=1}^4w(rL/N)\cos^2(r\vartheta)
$$

$$
\hspace{35mm}
+\frac{4L}{N^2}\sum_{r=1}^4w(rL/N)
\cos(r\vartheta)\operatorname{Re}q_{rL}.
\tag{10}
$$

The last term is O(d_N/N), since |q_m| <= d_N. The common term B_N(Q) cancels when the two examples are subtracted. As 2L/N tends to 1 and w(2)=0, equations (9)-(10) imply

$$
\boxed{
\Delta_N(V_N(\vartheta_N^A))-
\Delta_N(V_N(\vartheta_N^B))
\longrightarrow\delta_w:=w(1/2)+w(3/2)>0.
}
\tag{11}
$$

This holds for every common deterministic block with d_N=o(N), regardless of its spectrum. Thus both defects cannot tend to zero. More quantitatively,

$$
\liminf_N\max\left\{
|\Delta_N(V_N(\vartheta_N^A))|,
|\Delta_N(V_N(\vartheta_N^B))|\right\}\ge\delta_w/2.
\tag{12}
$$

If d_N=o(sqrt(N)), then B_N(Q) <= 2||w||_infinity d_N^2/N tends to zero. Individual limits are then explicit:

$$
\Delta_N(V_N(\vartheta_N))\longrightarrow
\sum_{r=1}^3w(r/2)\cos^2(r\vartheta)-C_w
\quad\text{if }\vartheta_N\to\vartheta.
\tag{13}
$$

The stronger size restriction is needed for these individual limits for arbitrary Q_N, but is not needed for (11) or the bounded-observable argument below.

## 3. A bounded point-process observable distinguishes the examples

Use the same microscopic scaling and sole center shift as in the original problem:

$$
\Xi_{N,\alpha}=\sum_{j=1}^N\sum_{k\in\mathbb Z}
\delta_{N(\eta_j-\alpha+k)},\qquad \alpha\sim\operatorname{Unif}[0,1),
$$

where the eigenvalues are exp(2 pi i eta_j). Put a_N = vartheta_N/(2 pi) and s_N=N/L. The polygon part is exactly, in distribution,

$$
\sum_{j\in\mathbb Z}\left[
\delta_{s_N(j+a_N-T)}+
\delta_{s_N(j-a_N-T)}\right],\qquad T\sim\operatorname{Unif}[0,1).
\tag{14}
$$

To see this, note that L alpha modulo 1 is uniform. Since s_N tends to 2, coupling by the same T proves local vague convergence to

$$
\Xi_a=\sum_{j\in\mathbb Z}\left[
\delta_{2(j+a-T)}+\delta_{2(j-a-T)}\right]
\quad\text{if }a_N\to a.
\tag{15}
$$

The common Q_N block disappears locally in probability when d_N=o(N). For every compact interval J its expected number of points in J is (d_N/N)|J|. More directly, for F >= 0 continuous with compact support, the change in its Laplace functional on adding the common block is at most

$$
\frac{d_N}{N}\int F(x)\,dx\longrightarrow0.
\tag{16}
$$

The two limits from (9) are therefore:

* A: a doubled lattice of spacing 2, with a uniform translation;
* B: an ordinary lattice of spacing 1, with a uniform translation.

Both have intensity 1. The first has double points in the limit even though the finite spectra may be simple.

Choose any fixed, nonzero F in C_c^infinity(R), F >= 0, whose support lies in an interval of length ell < 1. Put h_F=1-exp(-F) and H=integral h_F. The ordinary lattice has at most one point in that interval, while the doubled lattice has at most one occupied site. Thus their limiting Laplace functionals are exactly

$$
\mathcal L_B(F)=1-H,
\qquad
\mathcal L_A(F)=1-H+\frac12\int h_F(x)^2\,dx.
\tag{17}
$$

In particular,

$$
\boxed{\mathcal L_A(F)-\mathcal L_B(F)
=\frac12\int(1-e^{-F(x)})^2\,dx>0.}
\tag{18}
$$

This is a difference detected by a fixed bounded continuous observable of the point process. It is not a failure caused solely by nonuniform integrability of a second moment.

One can also compare both limits directly with Sine_2. Its two-point density is 1-sinc^2(pi(x-y)), which is positive off the diagonal and at most 1. The first two Bonferroni inequalities therefore give

$$
1-H<\mathcal L_{\mathrm{Sine}_2}(F)
\le1-H+\frac{H^2}{2}.
$$

The strict lower bound follows because there is positive probability of two points where F is positive, and the union-bound inequality for the product is then strict. By Cauchy-Schwarz, integral h_F^2 >= H^2/ell > H^2. Hence

$$
\boxed{\mathcal L_B(F)<\mathcal L_{\mathrm{Sine}_2}(F)<\mathcal L_A(F).}
\tag{19}
$$

### 3.1 A variant with two fixed nonzero rational phases

The obstruction does not require a phase tending to a resonant value. One may instead take the fixed phases vartheta^A=1/10 and vartheta^B=1/2 for every N. Equation (10) then gives the strictly positive defect gap

$$
\delta'_w=\sum_{r=1}^3w(r/2)
\left[\cos^2(r/10)-\cos^2(r/2)\right]>0.
\tag{19a}
$$

Every summand is positive because cos^2 is strictly decreasing on [0,pi/2] and 3/2<pi/2. The limiting process at a fixed phase has alternating gaps 2 vartheta/pi and 2-2 vartheta/pi.

For the two fixed phases the short gaps are respectively 1/(5 pi) and 1/pi. Choose the explicit smooth function F(x)=exp(-1/[x(1/5-x)]) for 0<x<1/5 and F(x)=0 otherwise, and put h_F=1-exp(-F). It is positive throughout (0,1/5), so its overlap with its translate by 1/(5 pi) has positive length. Process B has at most one point in this support. Process A can contain precisely the two points of a short pair, whose occupied pairs have density 1/2. Therefore the fixed-phase limiting Laplace gap is exactly

$$
\mathcal L_A(F)-\mathcal L_B(F)
=\frac12\int h_F(x)h_F(x+1/(5\pi))\,dx>0.
\tag{19b}
$$

All the simplicity, nonreturn, exact word-expansion, and uniform diagonal arguments below apply to these fixed rational phases as well.

## 4. Simplicity, nonzero traces, and absence of all scalar returns

These properties can be imposed without changing the preceding limits. Here is one explicit deterministic choice with d_N tending to infinity: take odd d_N=o(sqrt(N)) and

$$
Q_N=\operatorname{diag}(e^{i\beta_1},\ldots,e^{i\beta_{d_N}}),
\qquad \beta_j=\sqrt{\ell_j},
$$

where ell_j is the j-th prime. Use the rational nonzero phases in (9).

The only external number-theoretic fact used here is Lindemann-Weierstrass: exponentials of distinct algebraic numbers are linearly independent over the algebraic numbers; see reference [3], Theorem 3.2.

The Q_N eigenvalues are distinct. Equality of two would make exp(i(beta_j-beta_k))=1 with a nonzero algebraic exponent. A Q_N eigenvalue cannot coincide with a polygon eigenvalue: such equality would imply exp(i(L beta_j minus or plus vartheta_N))=1; this exponent is nonzero algebraic because beta_j is irrational and vartheta_N is rational. The two polygon blocks are disjoint, since exp(2i vartheta_N)=1 would have the same impossible form. Thus the whole spectrum is simple.

If a positive power of V_N were scalar, the eigenvalues at j=0 in its two polygon blocks would have equal m-th powers. Their ratio would give exp(2im vartheta_N/L)=1, again impossible. Thus there are no scalar returns at any positive integer time.

For m not divisible by L the trace is sum_j exp(im beta_j), which is nonzero by Lindemann-Weierstrass. For m=rL it is

$$
\sum_j e^{im\beta_j}+L e^{ir\vartheta_N}+L e^{-ir\vartheta_N},
$$

also a nonzero linear combination of exponentials of distinct algebraic exponents. All traces are therefore nonzero. In particular p_1 is nonzero, excluding nontrivial global rotational invariance of the spectrum.

For an even simpler version take d_N=1 and Q_N=[1]. Then N=2L+1, every trace below L equals 1, and the same three properties follow by the identical argument.

## 5. Realization with a mixing classical transition matrix

The preceding spectra can be realized by unitaries whose matrix closed-word expansion has the same uniform diagonal sum rule as that invoked in the proposed argument. The following lemma applies to any unimodular numbers lambda_1,...,lambda_N satisfying

$$
\left|\sum_j\lambda_j\right|^2\le N.
\tag{20}
$$

For the examples with d_N=o(sqrt(N)), (20) follows simply from |p_1| <= d_N.

### Lemma

For all sufficiently large N there is a permutation pi such that, for

$$
U=\mathcal F_N\operatorname{diag}(\lambda_{\pi(0)},\ldots,
\lambda_{\pi(N-1)})\mathcal F_N^*,
\qquad P_{ab}=|U_{ab}|^2,
$$

the circulant bistochastic matrix P has eigenvalues nu_0=1 and nu_k, 1 <= k < N, obeying

$$
\max_{k\ne0}|\nu_k|\le\frac12,
\qquad \sum_{k\ne0}|\nu_k|^2\le16.
\tag{21}
$$

The permutation can be chosen deterministically as the first satisfactory one in lexicographic order. Randomness is used only to prove existence.

### Proof of the lemma: the eigenvalues and concentration

Fourier inversion gives

$$
\nu_k=\frac1N\sum_{j=0}^{N-1}
\lambda_{\pi(j)}\overline{\lambda_{\pi(j+k)}},
\tag{22}
$$

with cyclic indices. For a uniform permutation and k != 0,

$$
\mathbb E\nu_k=
\frac{|p_1|^2-N}{N(N-1)},\qquad
|\mathbb E\nu_k|\le\frac1{N-1}.
\tag{23}
$$

Swapping two entries of a permutation affects at most four summands of (22). Each changes by at most 2, so the total change is at most 8/N. Expose the permutation one entry at a time. Two choices at the next position can be coupled by swapping those two labels in the unexposed completion, so each real or imaginary Doob-martingale increment is bounded by 8/N. The exponential martingale bound yields

$$
\Pr\{|\nu_k-\mathbb E\nu_k|>t\}
\le4e^{-Nt^2/256}.
\tag{24}
$$

For completeness, the bound follows by applying the conditional estimate E exp(s X) <= exp(s^2 b^2/2) to each mean-zero real increment |X| <= b, multiplying these bounds over N increments, optimizing s, and then taking a union bound over real and imaginary parts. Thus no independence of the exposed increments is being assumed.

For N large, (23), (24), and a union bound give

$$
\Pr\{\max_{k\ne0}|\nu_k|>1/2\}
\le4N e^{-N/4096}=o(1).
\tag{25}
$$

### Proof of the lemma: the bounded sum of squares

Expanding |nu_k|^2 gives N^2 pairs of summands. At most 3N pairs have overlapping indices among j,j+k,l,l+k. Their total contribution in absolute value to the expectation is at most 3/N.

For a pair with four distinct positions, the expectation is the uniform average over four distinct spectral indices of lambda_a lambda_b overline(lambda_c lambda_d). Its numerator is

$$
S_4=|p_1|^4-2\operatorname{Re}(p_2\overline{p_1}^{\,2})
-4N|p_1|^2+|p_2|^2+2N^2+8|p_1|^2-6N.
\tag{26}
$$

This identity follows by inclusion-exclusion on coincident indices, or by expanding the unrestricted fourfold sum and grouping equality patterns. Assumption (20) and |p_2| <= N give |S_4| <= 24N^2. Since (N)_4 >= N^4/16 for N >= 6, the distinct-index expectation has absolute value at most 384/N^2. It follows that

$$
\mathbb E|\nu_k|^2\le\frac3N+\frac{384}{N^2},
\qquad
\mathbb E\sum_{k\ne0}|\nu_k|^2\le3+\frac{384}{N}\le4
\tag{27}
$$

for N sufficiently large. Markov's inequality gives probability at least 3/4 that the sum is at most 16. Together with (25), this proves that (21) holds for at least one permutation.

### Consequences needed for repeated words

The matrix P is normal and circulant. Fourier inversion and (21) imply

$$
\max_{a,b}P_{ab}\le\frac12+\frac1{2N}\le\frac23
\tag{28}
$$

for N >= 3. Also

$$
\operatorname{Tr}P=|p_1|^2/N\le1,
$$

$$
|\operatorname{Tr}P^d-1|
\le\sum_{k\ne0}|\nu_k|^d
\le16(1/2)^{d-2}=64\,2^{-d},\qquad d\ge2.
\tag{29}
$$

In particular Tr P^d <= 17 for every positive d. Both the maximum-entry bound and this uniform trace bound are required in the next step; a spectral gap alone would not supply the latter with a constant independent of N.

## 6. An exact all-time orbit expansion with the same diagonal rule

For this U, a primitive closed word p of length d is a cyclic word on the N matrix indices with least period d. Let

$$
t_p=\prod_{r=0}^{d-1}U_{i_{r+1},i_r},\qquad
W_p=|t_p|^2,
$$

where the index sequence is cyclic. Grouping the exact matrix product by primitive words gives, for every positive m,

$$
\operatorname{Tr}U^m
=\sum_{d\mid m}d\sum_{p\text{ primitive},\ |p|=d}t_p^{m/d}.
\tag{30}
$$

This is a finite exact identity at each m, with no semiclassical or other remainder. Its same-orbit diagonal is

$$
D_m^{\rm word}
=\sum_{d\mid m}d^2\sum_{|p|=d}W_p^{m/d}.
\tag{31}
$$

The corresponding positive closed-word sum is

$$
\operatorname{Tr}P^m
=\sum_{d\mid m}d\sum_{|p|=d}W_p^{m/d}.
\tag{32}
$$

Thus

$$
0\le m\operatorname{Tr}P^m-D_m^{\rm word}
=\sum_{\substack{d\mid m\\d<m}}(m-d)d\sum_{|p|=d}W_p^{m/d}.
\tag{33}
$$

Let q=2/3. By (28), W_p <= q^d and therefore W_p^(m/d) <= q^(m-d) W_p. Moreover d sum_{|p|=d} W_p <= Tr P^d <= 17. Every proper divisor d of m is at most m/2, and there are at most m such divisors. Hence

$$
0\le m\operatorname{Tr}P^m-D_m^{\rm word}
\le17m^2q^{m/2}.
\tag{34}
$$

Combining this with (29), and handling m=1 by Tr P <=1, yields the uniform estimate

$$
\boxed{
|D_m^{\rm word}-m|
\le81m^2\left(\sqrt{2/3}\right)^m,
\qquad m\ge1.
}
\tag{35}
$$

All constants are independent of N and m once N exceeds the fixed threshold in the existence lemma.

Apply this construction separately to the two spectra in Section 2 with d_N=o(sqrt(N)). Unitary conjugation preserves every trace, determinant, spectral simplicity, and return property. We have therefore obtained two deterministic sequences satisfying exact all-time orbit identities, a uniform same-orbit rule (35), and identical short traces, but violating any common conclusion Delta_N -> 0 by (11).

If O_m^word=|p_m|^2-D_m^word, then (35) gives

$$
N^{-2}\sum_mw(m/N)D_m^{\rm word}
\longrightarrow\int_0^2u w(u)\,du.
$$

The two weighted off-diagonal limits, when d_N=o(sqrt(N)), are

$$
\sum_{r=1}^3w(r/2)\cos^2(r\vartheta)
-\int_0^2u w(u)\,du.
\tag{36}
$$

They differ by delta_w. They cannot both equal the CUE-required value

$$
-\eta_*,\qquad
\eta_*:=\int_1^2(u-1)w(u)\,du>0.
\tag{37}
$$

The signed mechanism can be seen pointwise in the version d_N=1, Q_N=[1]. At nonmultiples of L one has

$$
O_m^{\rm word}=1-m+O(m^2(\sqrt{2/3})^m).
$$

At a multiple m=rL with fixed positive r, one instead has

$$
O_{rL}^{\rm word}=4L^2\cos^2(r\vartheta)+O(N).
$$

Thus the exact cross-word sum contains a negative background at most times and coherent spikes of order N^2 at a few Heisenberg-scale times. Changing a fixed rational phase changes those spikes while leaving all the stated short-time and same-orbit information intact. This is the concrete cancellation mechanism missed by the proposed algebraic inference.

## 7. Why Riemann-Siegel resummation does not close this gap

Self-inversiveness is useful: it replaces coefficients beyond N/2 by conjugates of coefficients before N/2. But those retained coefficients are

$$
c_j=\sum_{\substack{v_1,v_2,\ldots\ge0\\\sum r v_r=j}}
\prod_{r\ge1}\frac{(-p_r)^{v_r}}{r^{v_r}v_r!}.
\tag{38}
$$

At j comparable to N this involves products of increasing degree and total orbit length comparable to N. A first-order or second-order short-trace estimate does not control their correlations. Taking a logarithmic derivative or using (5) creates further nonlinear products; self-inversiveness does not assign their values or signs.

Nor does the single random center shift supply action averaging. Under that shift p_m is multiplied by exp(-2 pi i m alpha), so |p_m|^2 is unchanged. In products of several traces the shift imposes conservation of total Fourier degree, not pairwise matching of the component actions.

The two examples exhibit the missing information exactly: the coefficients below L and the determinant agree, but a coefficient at L changes the Heisenberg-scale answer. Their exact long/short identities incorporate that change faithfully. Nothing in those identities cancels it.

For the original map, an all-time exponentially accurate trace formula is stronger than a formal asymptotic formula because it permits exact reconstruction and rigorous error control. Nevertheless, once it is used only to identify traces and to evaluate the diagonal, it does not add a sign or phase-correlation estimate for the remaining terms. The matrix examples have an even smaller remainder, namely zero. A successful argument for the original family must exploit additional properties of its fixed two-dimensional dynamics, its action differences, or its pseudo-orbit correlations that the matrix-word examples do not possess.

One concrete place where such new information is required is the Gram-type family arising from the squared recurrence:

$$
|p_m|^2=\sum_{j,k=1}^N
c_j\overline{c_k}\,p_{m-j}\overline{p_{m-k}},\qquad m>N.
\tag{39}
$$

Equation (3) relates some entries algebraically, but supplies neither their weighted cancellation nor a bound adequate for (1). Replacing these products by diagonal or Gaussian contractions is an additional hypothesis, not a consequence of self-inversiveness.

## 8. Primary-source check

Braun and Haake [1] provide the exact finite-dimensional Riemann-Siegel decomposition. Their generating function also introduces a second offset-window average (Section 3). Section 4.2 explicitly applies a diagonal approximation to multinomial products of traces; Section 4.3 separately addresses off-diagonal corrections. Thus the word “exact” in the title and in the finite-dimensional algebra does not turn that approximation into a theorem for the present deterministic family.

Waltner, Gnutzmann, Tanner, and Richter [2] give exact subdeterminant identities and exact matrix-orbit expansions. They distinguish these identities from the remaining problem of understanding cancellations in spectral correlation sums. This distinction is realized concretely by Sections 5-6 above.

## 9. Optional deterministic insertion of prescribed short trace data

The common block need not have artificial prescribed traces. The following elementary completion lemma shows that any sufficiently moderate finite trace vector can be inserted exactly.

Let a_1,...,a_K be complex numbers and S=sum_{m=1}^K |a_m|/m. If

$$
d>2K,\qquad d\ge8K(K+1)S,
\tag{40}
$$

there is a d-dimensional unitary Q with Tr Q^m=a_m for 1<=m<=K. Its determinant can also be prescribed arbitrarily on the unit circle.

To prove this, start at the d-th roots of unity with x_j=2 pi j/d. For a vector b define the real perturbations

$$
\delta_j(b)=\frac1{id}\sum_{n=1}^K
\left(\frac{b_n}{n}e^{-inx_j}-\frac{\overline{b_n}}n e^{inx_j}\right).
$$

For s(b)=sum |b_n|/n, one has max_j |delta_j| <= 2s(b)/d. The power traces of the perturbed points exp(i(x_j+delta_j)) equal b_m+R_m(b), because d>2K makes the linear Fourier map exactly the identity. The real exponential remainder bound gives

$$
s(R(b))\le K(K+1)s(b)^2/d.
$$

On the ball s(b)<=2S, the map b -> a-R(b) maps into that ball and has Lipschitz constant at most 4K(K+1)S/d<=1/2. The latter bound follows from the derivative estimate for exp(ix)-1-ix and the same Fourier bound on delta. Its fixed point gives the desired traces.

The perturbing trigonometric function has derivative bounded by 4KS/d<1, so the perturbed eigenangles remain distinct. Its average over the roots is zero; hence the determinant is the original clock determinant. To impose a different determinant, rotate the whole block by exp(i gamma/d) and apply the construction to a_m exp(-im gamma/d); the value of S is unchanged.

For example, with a logarithmic time cutoff K and exponentially bounded short traces, one can choose a sufficiently small positive constant in K=c log N and a block dimension d=N^beta with beta<1/2 so that (40) holds. This observation does not presume such bounds beyond their verified range in the original problem. It shows precisely how any data satisfying (40) can be shared by the counterexamples.

## 10. Conclusion for the fixed research target

The signed off-diagonal assertion for the actual family remains unproved:

$$
\frac1{N^2}\sum_{m\ge1}w(m/N)O_{m,N}\longrightarrow-\eta_*.
$$

This pass establishes a substantive negative result about the proposed proof mechanism, rather than another conditional reformulation: even exact all-time orbit identities, a uniform diagonal sum rule, unitarity, identical traces almost through half the Heisenberg time, and strong nonresonance properties do not generally force that limit. The missing information is dynamical control of the signed cross-orbit correlations at total length proportional to N. No such estimate for the original fixed Anosov family is supplied by self-inversiveness.

## References

1. P. Braun and F. Haake, *Chaotic maps and flows: Exact Riemann-Siegel lookalike for spectral fluctuations*, arXiv:1206.4222v1. Sections 2, 3, 4.2, 4.3. https://arxiv.org/html/1206.4222v1
2. D. Waltner, S. Gnutzmann, G. Tanner, K. Richter, *A sub-determinant approach for pseudo-orbit expansions of spectral determinants in quantum maps and quantum graphs*, arXiv:1209.3131v2; Physical Review E 87, 052919 (2013). https://arxiv.org/pdf/1209.3131
3. S. A. Popescu, *A simple and self-contained proof for the Lindemann-Weierstrass theorem*, arXiv:2306.14352v2, Theorem 3.2. https://arxiv.org/html/2306.14352v2
