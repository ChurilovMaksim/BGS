# Independent reconstruction of the Haar feedback candidate

Date: 12 October 2026. Scope: independent internal mathematical review, with
read-only access to the repository and the input candidate. This report is a
separate scratch artifact. No external peer review, numerical certification,
world-priority claim, Lean formalization, or BGS claim is made.

## 1. Frozen input and verdict

Reviewed input:
`/workspace/scratch/06745ba532e4/research_session/haar_feedback_candidate_20261012.md`.

Input SHA256:
`7a717c01207e12cf8c7ac6c2cc2f0ac95b625d36a0b3e5bdfd30ae72554b8c22`.

Repository HEAD at review:
`6bd6c3129b0b69eeb4ec5243a7e6e2eba75865f7`.

**Verdict: PASS in the stated scope.** The finite-dimensional joint law,
inverse-Jacobi spectrum, all-time Haar flatness estimate, and unconditional
fixed-order clock laws for the independent-initial-law class
`D(nu_N || Haar_N)=O(log N)` follow. The required uniformity is present in the
canonical deterministic-sequence theorem and can be extracted without a new
probabilistic premise. No substantive missing step or counterexample to the
stated claims was found.

The reconstruction below fills out two compressed passages useful in a
maintained proof: the rectangular singular-value Jacobian and the uniform
finite-moment criterion for empirical weak convergence. The microscopic-gap
obstruction can also be stated using a continuous compactly supported test
function, to avoid relying on convergence of unbounded counting variables.
These expansions change no hypothesis or conclusion of the candidate.

The maintained dependencies used as already reviewed inputs have SHA256:

| File in `BGS/mathematics` | SHA256 |
| --- | --- |
| `conditional_clock_universality_20261011.md` | `8517456f3c4b7b5e6243d6f644b705ea80e4267e92b6e0ab157db0bc7c1d08dc` |
| `full_depth_clock_measure_20261011.md` | `d7d13458f1c5a7a31ed3632bb6e54668dca3b85610ea0f48b28e84dbd5f0e3e2` |
| `delay_bootstrap_20261011.md` | `fdf990b240f70e4433e6b8a0e1f424718cbbc5f08b60d326e1fdbe931b527027` |
| `all_moment_delay_bootstrap_20261011.md` | `18b82c616d2eba73f08e55cb80d01775029db7bbd7d14dfa2fdd495db933c2ac` |

Their quantified initial-matrix scope and process definitions were checked;
this report does not re-audit the full upstream finite-word induction. In
particular, the canonical clock theorem starts with an arbitrary deterministic
unitary sequence, has a tolerance depending only on fixed `L,K,kappa`, and
estimates an intersection event rather than conditioning on a future flatness
event. No communicated computation or prior verdict was used as a substitute
for a proof of the new claims.

## 2. Phase absorption, graph identity and the delay convention

Let the retained ports be first, with sizes `u` and `q=N-u`. With feedback
condition `x_E=W_E output_E`, where the phases in the diagonal unitary `W_E`
are held constant as the spectral parameter varies, the original system
`output=zU input` gives

\[
x_E=(I-zW_EU_{EE})^{-1}zW_EU_{ER}v,
\qquad output_R=zU_{RR}v+zU_{RE}x_E.
\]

Thus the candidate's **left** multiplication
`V=diag(I_u,W_E)U` is correct. It changes only eliminated output rows and
gives exactly its `X(z)` and `F_u(z)`. Successive scalar eliminations solve
the same linear feedback equations, so they agree with this block elimination
whenever the relevant inverses exist. This establishes compatibility with the
canonical sequential process; an independent complete phase/order realization
may be fixed for this marginal-distribution argument.

For any fixed phase/order realization independent of the initial Haar matrix,
`V` is Haar. A Haar unitary has no eigenvalue 1 almost surely. If `V_EE x=x`,
unitarity and equality of norms force `V_RE x=0`; consequently `[0;x]` would
be a fixed vector of `V`. Hence `I-V_EE` is invertible almost surely. At any
finite `N`, the finitely many predetermined cuts are simultaneously regular
almost surely. The case `q=0` gives `F_N(z)=zU`, `T=I` directly.

Write `L(z)=[I;X(z)]` and `M(z)=[F_u(z);X(z)]`. On the unit circle,
`M=zVL`. Norm preservation first shows `F_u(z)^*F_u(z)=I`. With a dot denoting
the angular derivative,

\[
\dot M=iM+zV\dot L,
\qquad M^*zV=L^*,
\qquad M^*\dot M=iL^*L+L^*\dot L.
\]

The `X^* dot X` terms cancel, leaving

\[
-iF_u(z)^*\dot F_u(z)=I+X(z)^*X(z).
\]

At `z=1`, `dot F_u=iF_u'(1)`, so the candidate's analytic-derivative convention
is precisely

\[
T=S^*F_u'(1)=I+X^*X\ge I.
\]

There is no missing angular factor or derivative of a feedback phase.
This statement would require modification for spectral-parameter-dependent
feedback phases, which are not part of the hypothesis.

## 3. Cayley order and the complete real Jacobian

Set

\[
C=i(I+V)(I-V)^{-1}=
\begin{pmatrix}A&B^*\\B&D\end{pmatrix},
\qquad V=(C-iI)(C+iI)^{-1}.
\]

For Hermitian congruence `H -> L H L^*` in dimension `n`, reduce `L` by a
singular-value decomposition to positive singular values `s_j`. The real
diagonal coordinates contribute `s_j^2`, and each complex off-diagonal pair
contributes `(s_j s_k)^2`. The determinant is therefore
`prod_j s_j^(2n)=|det L|^(2n)`. The Cayley differential is

\[
-iV^*dV=2(C-iI)^{-1}dC(C+iI)^{-1}.
\]

Its real Jacobian, apart from the constant `2^(N^2)`, is
`det(I+C^2)^(-N)`. This derives the Haar Cauchy density, rather than importing
it as an unverified theorem.

The graph equation `V[I;X]=[S;X]`, multiplied on the left by `C+iI`, gives
`(A+iI)S=A-iI` in the top block and `B(I-S)=2iX` in the bottom block. Thus

\[
S=(A-iI)(A+iI)^{-1},\qquad X=B(A+iI)^{-1}.
\]

Only functions of `A` commute in this calculation. The inverse multiplying
`B` is on the right; moving it through `B` is not justified and is not done.

Put `G=I_q+XX^*`, and use the change of variables

\[
B=X(A+iI),\qquad
D=XAX^*+G^{1/2}YG^{1/2},\qquad Y=Y^*.
\]

This is globally bijective and smooth: first recover `A`, then `X`, then `Y`.
Complex right multiplication on `q` rows has real Jacobian
`|det(A+iI)|^(2q)=det(I+A^2)^q`; Hermitian congruence in dimension `q` gives
`det(G)^q`. The full derivative is block triangular in `(A,X,Y)`, so the
derivatives of `G^(1/2)` with respect to `X` contribute only below the diagonal
and supply no further determinant.

The lower Schur factor of `I+iC` is

\[
I+iD+B(I+iA)^{-1}B^*
 =G+i(D-XAX^*)=G^{1/2}(I+iY)G^{1/2},
\]

because `B(I+iA)^(-1)B^*=X(I-iA)X^*`. Consequently

\[
\det(I+iC)=\det(I+iA)\det(G)\det(I+iY).
\]

Combining the squared modulus of this identity with both Jacobian factors
gives exactly

\[
\det(I+A^2)^{-u}\det(G)^{-(N+u)}
\det(I+Y^2)^{-N}\,dA\,dX\,dY.
\]

The exponent on `G` is `-2N+q=-(N+u)`. Positivity, bijectivity and finite
original total mass show by Tonelli that each separate factor has a finite
positive integral. Hence `A` and `X` are independent, `S` is Haar in dimension
`u`, and `X` has the asserted rectangular density. Sylvester's identity gives
`det G=det(I_u+X^*X)`.

Right unitary invariance of this density implies conjugation invariance of
`T=I+X^*X`. Since `S` and `T` are independent, conditional on `S=s` the law of
`sTs^*` is the same as that of `T`. This proves that `Q=STS^*` has the same
law as `T` and is independent of `S`. It does not prove independence of
the pair `(T,Q)` from `S`, or any independence between retained sizes.

## 4. Gaussian ratio, singular Jacobi branch and finite moments

Let `Y_0` be a `2u`-by-`u` standard complex Gaussian matrix and set
`W=Y_0^*Y_0`. Its density is proportional to `det(W)^u exp(-Tr W)` on the
positive Hermitian cone. This exponent follows, for example, directly from
Gaussian QR and the Cholesky Jacobian: for an `m`-by-`u` Gaussian matrix the
QR diagonal powers are `r_jj^(2(m-j)+1)`, whereas the Cholesky map to the Gram
matrix contributes `r_jj^(2(u-j)+1)`. Their ratio is `det(W)^(m-u)`.

Independently take Gaussian `G_0` of size `q`-by-`u`. Under
`G_0=XW^(1/2)`, complex right multiplication contributes `det(W)^q`, so the
joint `(X,W)` density is

\[
\det(W)^{u+q}\exp[-\operatorname{Tr}((I+X^*X)W)].
\]

For `A_0=I+X^*X`, substitute `W=A_0^(-1/2) Z A_0^(-1/2)`. The determinant
power gives `det(A_0)^(-(u+q))`, and the Hermitian-congruence Jacobian gives
the additional `det(A_0)^(-u)`. Integrating `Z` yields exponent
`-(q+2u)=-(N+u)`. Thus `X` has exactly the law
`G_0 W^(-1/2)` claimed in (7).

With `B_0=G_0^*G_0`,

\[
T^{-1}=W^{1/2}(W+B_0)^{-1}W^{1/2}.
\]

This matrix and `(W+B_0)^(-1/2) W (W+B_0)^(-1/2)` are the two Gram matrices
`MM^*` and `M^*M` for `M=W^(1/2)(W+B_0)^(-1/2)`; their spectra coincide.
They need not be equal as matrices. This is the exact finite Jacobi ratio
with Wishart degrees `2u` and `q`.

Here is a direct derivation covering the singular `q<u` branch. Let
`r=min(q,u)`. For `q>=u`, use local singular-value coordinates
`X=U[diag(sigma_j);0]V^*`, away from repeated or zero singular values.

* Each diagonal radial/phase pair gives the factor `sigma_j`.
* Each of the `q-u` extra complex row directions gives `sigma_j^2`, for a
  total `sigma_j^(2(q-u))`.
* For `j<k`, the two complex angular directions map to the pair
  `(dX_jk, conjugate(dX_kj))` by the complex matrix
  `[[sigma_k,-sigma_j],[-sigma_j,sigma_k]]`. Its real determinant is
  `(sigma_k^2-sigma_j^2)^2`.

Gauge directions and invariant angular volumes contribute only a constant.
For `q<u`, apply the same computation to `X^*`, a real isometry. Thus the
radial Jacobian is

\[
\prod_{j=1}^r\sigma_j^{2|q-u|+1}
\prod_{j<k}(\sigma_j^2-\sigma_k^2)^2\,d\sigma_1\cdots d\sigma_r.
\]

With `t_j=sigma_j^2`, the positive eigenvalues of `X^*X` have density

\[
c\prod_j t_j^{|q-u|}(1+t_j)^{-(N+u)}\Delta(t)^2\,dt.
\]

Setting `y_j=1/(1+t_j)` gives a power
`N+u-|q-u|-2r=u` on each `y_j`: the Vandermonde supplies
`y_j^(-2(r-1))` and the scalar change of variables supplies `y_j^(-2)`.
The resulting density is precisely

\[
c\prod_j y_j^u(1-y_j)^{|q-u|}\Delta(y)^2\,dy,
\qquad 0<y_j<1.
\]

No nonsingular Wishart density for `B_0` was assumed. Gaussian rank is
exactly `r` almost surely; therefore `T` has exactly `u-r=max(u-q,0)`
eigenvalues 1. The empirical law of `H=uT/N` has the exact atom at `u/N`
of weight `max(0,2-N/u)`, saturating the pathwise rank lower bound only
for this Haar law.

For `q>0` and `k>0`, `Tr T^k` equals the fixed eigenvalue contribution plus
`sum_j y_j^(-k)`. Sufficiency for `k<u+1` follows by bounding the Vandermonde
and `(1-y_j)^{|q-u|}` on the unit cube and integrating `y_j^(u-k)`.
Necessity follows by sending one `y_j` to zero while the others remain
distinct in a compact subinterval of `(0,1)`. Thus

\[
\mathbb E\operatorname{Tr}T^k<\infty
\quad\Longleftrightarrow\quad k<u+1\qquad(q>0).
\]

For `q=0`, `T=I` and all moments are finite. An exact low-dimensional check
of the sharp threshold is `N=2,u=q=1`: `t=|X|^2` has density
`2(1+t)^(-3)`, so `T` has density `2T^(-3)` for `T>=1`. It has mean 2
but infinite second moment. This analytic example also rules out a spurious
finite-N compact support or a finite-N edge bound.

Finally, the Schur complement of a column in `W` shows that a diagonal entry
of `W^(-1)` is the inverse of a Gamma variable of shape
`2u-(u-1)=u+1`, with mean reciprocal `1/u`. Phase invariance makes the
off-diagonal expectations vanish; their integrability follows from positivity
and Cauchy-Schwarz. Hence `E W^(-1)=I/u`. Independence and `E B_0=qI` give

\[
\mathbb ET=I+(q/u)I=(N/u)I,
\qquad\mathbb E(uT/N)=I.
\]

## 5. All-time Haar flatness and deterministic uniformity

For each predetermined retained size `u`, conditional on the entire fresh
phase vector and coordinate order, the Haar initial matrix still produces a
Haar `S_u` in the retained coordinates. This is a distribution calculation,
not future-event conditioning inside the clock martingale. It does not assert
a Haar law at an adaptively chosen size depending on the initial matrix.

A Haar entry in dimension `u>=2` has squared modulus `Beta(1,u-1)`, as is
seen by normalizing an independent Gaussian column. With
`ell=log(2N)`, `m=ceil(ell^(1+kappa))` and fixed `K,kappa>0`, the union bound
over entries and retained sizes therefore yields

\[
\begin{aligned}
q_N(K)&=\mathbb P_{\rm Haar}(A_m(K)^c)\\
&\le\sum_{u=m}^N u^2\exp[-K\ell(u-1)/u]\\
&\le N^3(2N)^{-K(1-1/m)}=:b_N(K).
\end{aligned}
\]

When the threshold is at least 1, the actual entry failure is zero, so the
same upper bound remains valid. No independence between sizes is used.
For fixed `K>3`, `ell/m ->0`, and consequently
`b_N(K)=2^(-K)N^(3-K)(1+o(1))`. In particular `K=4` gives
`(1+o(1))/(16N)`.

For fixed `L,K,kappa`, let `epsilon_N` be the canonical tolerance, common to
all initial matrices, and define

\[
g_N(U)=\mathbb P_{\rm phases,order}
\bigl(A_m(K)\cap\{\text{one stated clock error}>\epsilon_N\}\bigr).
\]

The canonical theorem states `g_N(U_N)->0` for every deterministic unitary
sequence `(U_N)`. If `sup_U g_N(U)` did not tend to zero, select approximate
maximizers at a subsequence with values at least a fixed positive constant,
and arbitrary unitaries elsewhere. This deterministic sequence contradicts
that theorem. Hence `sup_U g_N(U)->0`.

This step needs both quantified facts: every deterministic initial sequence,
and a tolerance depending only on `L,K,kappa`. Both are present in the
reviewed maintained statement and its process definitions. Integrating this
uniform intersection bound over initial Haar measure and adding `b_N(K)`
proves all the fixed clock conclusions in probability, simultaneously over
`u>=m`: input/output diagonal powers, vanishing input/output off-diagonal
powers, vanishing mixed entries, and normalized empirical moments. `L` is
fixed before `N` tends to infinity.

## 6. Uniform empirical weak law from finitely many fixed moments

The reviewed reference measures `mu_x`, `0<=x<=1`, have common support in
`[0,b_0]`, `b_0=3+2sqrt(2)`, and moments `f_r(x)` polynomial in `x`.
Consequently `x -> mu_x` is weakly continuous: a convergent sequence of
parameters has every subsequential measure limit with the specified moments
on this common compact interval, which determine the measure.

The needed uniform deterministic lemma is the following. For every `eta>0`
there exist a **fixed** integer `L` and `delta>0` such that, for every
probability measure `lambda` on `[0,infinity)` and every `x in [0,1]`,

\[
\left|\int h^r\,d\lambda-f_r(x)\right|<\delta
\quad(1\le r\le L)
\quad\Longrightarrow\quad
d_{\rm BL}(\lambda,\mu_x)<\eta.
\]

If not, choose `lambda_n,x_n` with moment errors less than `1/n` through
order `n`, yet distance at least `eta`. Extract `x_n -> x`. Bounded first
moments imply tightness of `lambda_n`. For every fixed `r`, bounded
`(r+1)`-st moments give uniform integrability of `h^r`; every weak limit then
has moments `f_r(x)`. These moments force support in `[0,b_0]` by applying
Markov's inequality with arbitrarily high moments to `[b_0+epsilon,infinity)`.
Polynomial density on the compact interval identifies the limit as `mu_x`.
Together with `mu_(x_n) -> mu_x`, this contradicts the distance lower bound.

Apply the lemma to the empirical spectral law of `H_u=uT_u/N`, whose
positivity is exact. The canonical fixed-order moment estimate controls the
single finite set of moments selected by this lemma for every `u>=m`.
Therefore the unconditional Haar statement is

\[
\max_{m\le u\le N}
d_{\rm BL}(\operatorname{emp}(uT_u/N),\mu_{u/N})
\ \xrightarrow{\mathbb P}\ 0.
\]

The same argument applies to `uQ_u/N`, which has the same spectrum. It uses
neither a growing moment order nor an infinite union of probabilistic events.
Compact support of the reference family is not a compact-support assertion
for a finite-N random delay matrix.

## 7. Entropy transfer, including the order of limits

Let the initial law `nu_N` be independent of the same fresh phase/order
randomness and have finite `D_N=D(nu_N || Haar_N)`. The joint product laws
have relative entropy exactly `D_N`. For an event with probabilities
`p_N` under the first law and `q_N` under the Haar law, Jensen on the event
and its complement gives

\[
D_N\ge p_N\log(p_N/q_N)
 +(1-p_N)\log((1-p_N)/(1-q_N))
 \ge p_N\log(1/q_N)-\log2.
\]

If `q_N=0`, absolute continuity implies `p_N=0`. For the flatness failure
event, `q_N<=b_N(K)<1` for large `N`, hence

\[
p_N\le\frac{D_N+\log2}{\log(1/b_N(K))},
\quad
\log(1/b_N(K))=(K-3)\log N+K\log2-K\ell/m.
\]

Thus `D_N=o(log N)` gives high-probability all-time flatness for each fixed
`K>3`. For the larger `O(log N)` class, put
`C=limsup_N D_N/log N<infinity`. For a fixed clock tolerance `eta>0` and
fixed `L,kappa,K>3`, eventually `epsilon_N(K)<eta`, and the clock failure
probability is at most `sup_U g_N(U)+p_N`. It follows that

\[
\limsup_{N\to\infty}\mathbb P_{\nu_N}
(\text{one fixed clock error}>\eta)
\le C/(K-3).
\]

Now let `K` tend to infinity **after** taking that limsup. Each invocation
of the canonical theorem has fixed `K`; no estimate uniform in a growing
`K_N` is needed or asserted. The resulting upper bound is zero. The uniform
finite-moment lemma in Section 6 yields the same empirical weak law uniformly
over all `u>=m` for this entropy class.

The proof does not yield high-probability flatness for one prescribed finite
`K` in the full `O(log N)` class. It also does not transfer unrestricted
expectations of high delay moments on exceptional events. Both restrictions
are stated correctly in the candidate.

## 8. Prescribed-origin microscopic obstruction

Fix `0<c<1` and an arc of length `2pi c/N` centered at a prescribed origin.
Rotation invariance and exactly `N` eigenangles give expected Haar count `c`.
Markov's inequality implies that the gap event `E_N` has probability at least
`1-c`. Conditioning Haar on that event gives the exact entropy

\[
D(\operatorname{Haar}_N(\,\cdot\mid E_N)\Vert\operatorname{Haar}_N)
=-\log\mathbb P_{\rm Haar}(E_N)
\le-\log(1-c)=O(1).
\]

This law, with independent fresh phase/order randomness, satisfies Section 7.
At the initial size `u=N`, however, its rescaled eigenangle point process
has no points in a fixed prescribed interval of length `c`, with probability
one. To exclude convergence to intensity-one Sine_2 rigorously, take a
nonzero continuous nonnegative test function compactly supported inside that
interval. Every prelimit integral of this function is zero. Any local vague
point-process limit would therefore have the same zero integral almost surely.
An intensity-one Sine_2 process instead has positive expected integral equal
to the Lebesgue integral of that function, so its integral is positive with
positive probability. The claimed prescribed-origin implication is false.

This demonstrates no failure of a Haar spectral theorem: the initial law has
been conditioned and is no longer Haar. It makes no claim about convergence
after averaging the observation origin, any deterministic quantizer, or an
actual deterministic BGS family.

## 9. Source comparison and exact boundaries of the verdict

The primary-source locator
[Bourgade, Najnudel and Nikeghbali, arXiv:1102.2633v1](https://arxiv.org/pdf/1102.2633v1)
was checked: the introduction gives the Cayley/principal-corner formulation
and Schur projection, and Proposition 3.2 states Haar compatibility of these
projections. This supports the candidate's prior-object attribution. None of
the new delay identities or Jacobian powers above is accepted solely from that
locator.

[Neretin, arXiv:1411.2110v2](https://arxiv.org/pdf/1411.2110), Section 2.2,
equation (2.3), page 4, covers the determinant beta-integrals; Section 2.3,
pages 5-6, gives eigenvalue and rectangular singular-value integration. The
direct tangent calculation above supplies the exact needed rectangular power
and Vandermonde independently, including both dimension orderings. This is
reference checking, with no novelty assessment.

The proven conclusion concerns the feedback process starting from `F_N=zU_N`
and `T_N=Q_N=I`, with independent original uniform feedback phases and uniform
coordinate order, and an independent initial law of relative entropy
`O(log N)` against Haar. For any fixed `kappa>0`, all finitely many fixed clock
orders and their empirical weak law hold in probability simultaneously down
to `m=ceil(log(2N)^(1+kappa))`. Marginal finite-N statements also allow
arbitrary deterministic feedback phases and fixed retained sets.

Not covered: adaptive retained-set/size selection depending on the initial
matrix; spectral-parameter-dependent feedback phases; independence between
different sizes; growing-order, finite-N edge or exceptional-event expectation
laws; a high-probability flatness theorem for one specified finite `K` for all
`O(log N)` initial laws; an entropy-to-microscopic-universality implication;
deterministic point-mass initial laws; dynamical entropy in place of relative
entropy; any deterministic-map trajectory theorem, BGS, priority or formal
verification claim. A deterministic initial matrix has infinite relative
entropy against continuous Haar and is outside the entropy transfer class.

Repository files and the frozen candidate were not changed. No new agents,
numerical regression, or computational evidence were used in this review.
