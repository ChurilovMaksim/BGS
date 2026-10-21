> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_dual_weyl_primitivity_quantitative.md`. Embedded SHA256: `fee116da2d8d0611ac624b3815212803c223774edcf4a5ec1997efc058e95dac`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exact dual Weyl primitivity and its effective rate

Date: 21 October 2026.

## 0. Verdict and frozen scope

**Primary verdict: Theorems A, B, and C are proved as written.** The all-odd-dimensional claims, their explicit exception `N=7`, the uniform anchor transition, and the displayed effective stochastic gap survive independent reconstruction. No first missing estimate was found in those three theorems.

There is one notation clarification in the auxiliary discussion of §8: the recurrence using the matrix `P` from (1.1) is a recurrence on the nonzero-label set `Lambda_N`. The trace identity immediately before it refers to the full adjoint matrix. The latter trace equals one plus the trace of its restriction. Keeping these two dimensions explicit resolves the notation; this does not affect Theorems A–C. The author confirmed this intended restriction after the issue was raised. The frozen text is unchanged.

The audited primary files are:

- `research_round4_2026_10_21/dual_weyl_primitivity_and_quantitative_limits.md`, SHA-256 `90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`;
- `research_round4_2026_10_21/dual_exact_coefficient_check.py`, SHA-256 `568c2cf3f5c20f181b06a1ac0e98fdd44da8a95a7c2734adf71633972e9ac908`.

Both hashes were independently checked on disk. The full manuscript and script were read. The script was run and all its exact checks passed. The all-`N` proof below does not rely on extrapolating those finite checks or on another agent's preliminary agreement.

The sole external input is the qualitative Lindemann–Weierstrass theorem and the explicit version in Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, DOI [10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170). The [primary author's PDF](https://arxiv.org/pdf/2112.05004) was opened independently. The typeset Theorem 1.2 on PDF page 2 and the logarithmic-height definition on PDF page 3 were inspected visually, as well as the text extraction. Theorem 1.1 on page 1 supplies the exact qualitative statement used here.

No claim of `H_diag`, a fixed-test counterexample, useful Heisenberg-time stochastic mixing, or control of coherent interference follows from this audit.

## 1. The exact dual convention and covariance

Here, in contrast to the ordinary real-half quantization used in the character-comb argument, the Weyl basis is the original modular basis

$$
W_N(k,l)=T_N(l,k).
$$

Direct composition gives, for integer representatives,

$$
W_N(\kappa)W_N(v)
=e_N(\overline2\,\omega(\kappa,v))W_N(\kappa+v),
\qquad
\omega(\kappa,v)=\kappa_l v_k-\kappa_kv_l.
\tag{1.1}
$$

Taking `overline2=(N+1)/2` gives the exact generator coefficient

$$
-2N c_\kappa(-1)^{\omega(\kappa,v)}
\sin(\pi\omega(\kappa,v)/N).
\tag{1.2}
$$

The modular sign is present. Changing an integer lift changes `omega` by an integer multiple of the odd `N`; the sign and sine each acquire the same sign. Thus (1.2) is lift independent. Aliased increments must be added before deciding whether a coefficient vanishes.

The exact kernel covariance has no omitted phase. For example, compare `T(a,b)M` with `MT(a',b')`. Relative to the common original quadratic kernel, the left exponent has coefficients

$$
x:\ b-3a/4,\qquad y:\ a/4,\qquad
\text{constant}:\ ab/2-3a^2/8.
$$

The right exponent has coefficients

$$
x:\ -a'/4,\qquad y:\ 3a'/4+b',\qquad
\text{constant}:\ -3a'^2/8-b'a'/2.
$$

Substitution `a'=3a-4b`, `b'=-2a+3b` makes all three agree. All displayed fractions here are modular inverses, valid because `N` is odd. On inverting this covariance and converting `(a,b)` to frequency order `(k,l)=(b,a)`, one obtains

$$
M_NW_N(v)M_N^{-1}=W_N(Sv),\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\tag{1.3}
$$

Therefore the exact adjoint matrix is

$$
C_N(z)=e^{zG_N}\mathsf P_S,\qquad
G_N=iN\operatorname{ad}_{A_N}.
\tag{1.4}
$$

For real `z`, this matrix is unitary in the normalized Hilbert–Schmidt inner product. The identity vector is an isolated one-dimensional block; its orthogonal complement is the traceless space. The entrywise squared modulus on that complement is consequently doubly stochastic.

## 2. Algebraic evaluation preserves every nonidentically-zero entry

Every original coefficient lies in `Q(i)`, since `exp(i alpha_0)=(-3+4i)/5`; no algebraicity of the angle itself is needed. The entries of `A_N` lie in `Q(i,zeta_N)`. Its eigenvalues are real algebraic, and its spectral projectors are algebraic even when eigenvalues repeat: use the product over the distinct other eigenvalues.

Every entry in (1.4) is thus a finite sum

$$
\sum_{\lambda,\mu}\beta_{\lambda,\mu}
e^{iNz(\lambda-\mu)}.
$$

Combine equal slopes and omit zero coefficients. For nonzero algebraic `z`, the remaining exponents are distinct algebraic numbers and their coefficients are algebraic and nonzero. This verifies exactly the hypotheses of Huang's stated qualitative Lindemann–Weierstrass theorem. Such a sum cannot vanish. Equivalently, an analytic entry that has one nonzero Taylor coefficient cannot vanish at the specified nonzero algebraic kick.

In particular, the permutation edge `v -> Sv` survives because its entry equals one at zero. If a generator entry from `w` to `w+kappa` is nonzero, the corresponding adjoint entry from `S^-1 w` to `w+kappa` has nonzero derivative at zero and also survives. This argument supplies support, not a quantitative size for a high-frequency transition.

## 3. Fourier coefficients and the small-modulus aliases

Writing `r_k` for the ordinary Fourier coefficients of the polynomial `r`, direct multiplication gives

$$
r_0=1,\quad r_{\pm1}=1/2,\quad r_{\pm7}=-1/2,
\quad r_{\pm6}=r_{\pm8}=-1/4.
$$

The pure-`q` coefficient is the cosine coefficient plus `r_k/10`, with sine contribution

$$
-\frac{i}{200}(r_{k-1}-r_{k+1}).
$$

This yields precisely the seven positive coefficients in source (3.3), their conjugate negatives, and no constant coefficient. The mixed coefficients are `gamma r_k` at `l=1` and `conjugate(gamma) r_k` at `l=-1`, with `gamma=(-3-4i)/1000`. There are fourteen pure and eighteen mixed terms, for a total of thirty-two, all of support radius at most nine. Their denominators divide `4000`, and their coefficient one-norm is less than two.

The exceptional table was reconstructed from these coefficients, rather than assumed from the script. For example:

- At `N=3`, the residue `1` pure coefficient is `c_1+c_7+conjugate(c_2)+conjugate(c_5)+conjugate(c_8)=19/40-3i/800`. The mixed residue-zero `q` sum is `r_0+r_6+r_-6=1/2`. The residue `2` pure coefficient is the conjugate of the residue `1` coefficient.
- At `N=5`, the residue `1` coefficient is `c_1+c_6+conjugate(c_9)=1/40-7i/800`; the residue `2` coefficient is `c_2+c_7+conjugate(c_8)=17/40-i/200`.
- At `N=9`, they are `c_1+conjugate(c_8)=1/40-3i/400` and `c_2+conjugate(c_7)=9/20-i/400`.
- At `N=11`, only the additional frequency `-9` aliases into `2`, giving `-3i/800` there.
- For every odd `N>=13`, none of the three marked coefficients has an additional possible lift in the finite support. This proves the entire remaining infinite row of the table, not just its finite checks.

At `N=7`, all residue sums of `r` vanish: the residue zero sum is `1-1/2-1/2=0`, and the residue `±1` sums are `1/2-1/4-1/4=0`. Hence the mixed terms and the terms involving `r` all vanish in the modular Weyl polynomial. The cosine frequencies `±7` become the identity, leaving

$$
A_7=9I/10.
\tag{3.1}
$$

Thus the stated exception is necessary. For every other odd `N>=3`, all of `c_N(1,0)`, `c_N(0,1)`, and `c_N(2,0)` are nonzero.

The companion script independently rebuilds the polynomial with exact rational pairs, verifies the alias table through odd `N=201`, verifies (3.1), and checks the guaranteed support graph and order bound through odd `N=65`. Its run returned `all_checks_passed: true`. These checks agree with the derivation but are not the proof of the infinite range.

## 4. Composite connectivity and a uniform primitivity exponent

The elementary generator moves are

$$
(k,l)\longleftrightarrow(k+1,l)\quad(l\ne0),
\qquad
(k,l)\longleftrightarrow(k,l+1)\quad(k\ne0).
\tag{4.1}
$$

The coefficient vanishes exactly when its symplectic pairing is zero modulo `N`. A nonzero residue need not be a unit. This is why (4.1) remains valid over all odd composite rings.

Let `h_N` be the order of `S` modulo `N`. Each move (4.1) can be implemented in the actual support of `C` by `h_N-1` forward permutation edges followed by the surviving adjusted generator edge. This takes exactly `h_N` steps and never leaves the nonzero labels.

There is an explicit path to the anchor `v_*=(1,-2)` of at most `2N-2` elementary moves. If `l` is nonzero, move horizontally to `k=1`, then vertically to `l=-2`. If `l=0`, then `k` is nonzero: first move vertically to `-2`, then horizontally to `1`. The conditions in (4.1) remain satisfied along each leg. Reverse moves give a path of the same length from the anchor to any target.

The order estimate is valid at every odd prime power. At an odd prime `p`, the characteristic polynomial of `S` has discriminant `32`, hence distinct roots `3±2sqrt(2)` in `F_(p^2)`. Their product is one. If `2` is a square modulo `p`, the roots have order dividing `p-1`; otherwise Frobenius interchanges them and their order divides `p+1`. Thus

$$
\operatorname{ord}_p(S)\mid p-(2/p).
$$

The binomial expansion of `(I+p^aB)^p`, for odd `p`, increases the power of `p` in the remainder by at least one. Iteration gives

$$
\operatorname{ord}_{p^a}(S)\mid p^{a-1}(p-(2/p)).
\tag{4.2}
$$

All displayed upper multiples are even. The least common multiple of `s` positive even integers is at most their product divided by `2^(s-1)`. Applying the Chinese remainder theorem and (4.2) therefore gives

$$
h_N\le2N\prod_{p\mid N}\frac{p-(2/p)}{2p}
\le2N\prod_{p\mid N}\frac{p+1}{2p}
\le4N/3.
\tag{4.3}
$$

The final inequality uses at least one odd prime factor, each factor at most one, and every individual factor at most `2/3`. It does not assume squarefreeness.

The anchor also has an actual one-step loop. Its permutation image is `Sv_*=(-1,-2)` and their difference is `(2,0)`, with pairing four. Every odd `N>=3` fails to divide four, and the alias table gives the nonzero coefficient except at `N=7`. Hence the loop survives the algebraic kick.

Combining both anchor paths costs at most

$$
(4N-4)h_N\le\frac{16}{3}(N^2-N)<6N^2.
$$

Insert anchor loops to obtain exactly `6N^2` steps between every pair of nonzero labels. Every selected probability is positive, so `P^(6N^2)` is entrywise positive. This proves Theorem A, including aperiodicity without a separate period argument.

A coordinate invariant subspace cannot have an outgoing edge. Strong connectedness on the nonzero labels leaves only the four listed possibilities after adjoining or omitting the scalar line. Likewise a diagonal commuting matrix obeys `(d_u-d_v)C_(u,v)=0`; connectedness forces all its nonzero-label entries to be equal. These deductions do not require the diagonal entries to be algebraic.

## 5. The uniform anchor bound is valid even for large `tau N`

Expand powers of `G` using original integer increments before aliasing. From (1.2) and `N|sin(pi omega/N)|<=pi|omega|`, the outgoing coefficient sum from an integer lift `w` is at most `36pi|w|_1`. Every additional increment increases this lift norm by at most nine. Thus

$$
\|G^je_w\|_1\le(36\pi)^j\prod_{q=0}^{j-1}(|w|_1+9q).
\tag{5.1}
$$

This counts all lifted paths; collisions after modular reduction can only decrease the triangle-inequality bound.

For the fixed lift `w=(-1,-2)`, use `3+9q<=9(q+1)` and `324pi<1200` to obtain `||G^je_w||_1<=1200^j j!`. The constant term of the anchor entry is zero, so the Taylor tail after its linear term is at most

$$
\frac{(1200\tau)^2}{1-1200\tau}.
\tag{5.2}
$$

Its first derivative has magnitude

$$
2N|c_N(2,0)|\,|\sin(4\pi/N)|.
$$

For `N>=11`, `|c_N(2,0)|>=1/400` and `sin(4pi/N)>=8/N`, giving at least `1/25`. The explicit coefficients at `N=3,5,9`, with the elementary sine lower bounds in the source, give the same safe lower bound. At the fixed `tau=10^-80`, (5.2) is less than `tau/50`. Therefore

$$
|C(\tau)_{v_*,v_*}|\ge\tau/50,
$$

which proves Theorem B.

The estimate is local in the starting integer label, not local in `tau N`. For general `w`, summing the rising-factorial majorant in (5.1) gives exactly the upper bound `(1-324pi|z|)^(-|w|_1/9)`. At labels of order `N`, this bound can be exponential in `|z|N`. The source correctly refrains from turning the nonzero derivative argument into a uniform lower bound at every large label.

## 6. Field degree and logarithmic height: all factors checked

The matrix-height inequalities follow place by place from the maximum of one and the entry norms. Matrix multiplication costs at most `log N` at the archimedean places, matrix addition at most `log 2`, and scalar multiplication adds the scalar height. Normalized archimedean weights sum to one. The same argument gives `h(Tr B)<=h_mat(B)+log N`.

The base field `K_0=Q(i,zeta_N)` has degree at most `2N`. The matrix `4000A` has integral entries. Under every embedding of this field, a Weyl matrix remains a permutation matrix with root-of-unity entries, hence remains unitary; every coefficient has the same absolute value as before. Thus each embedded `A` has operator norm less than two. At finite places the denominator contributes at most `log 4000`, and at the archimedean places the entries contribute at most `log 2`. This proves

$$
h_{\rm mat}(A)\le\log8000<9.
\tag{6.1}
$$

For each eigenvalue, `4000lambda` is an algebraic integer: it is a root of the monic characteristic polynomial of `4000A`, whose coefficients are algebraic integers, and integrality is transitive. Every conjugate of `lambda` is an eigenvalue of an embedded matrix and has modulus at most two. The same finite and infinite place bounds give `h(lambda)<9`.

The splitting field over `K_0` of the characteristic polynomial has degree at most `N!`. Repeated roots are harmless: its Galois group embeds in permutations of the distinct roots, whose number is at most `N`. Consequently all eigenvalues, projectors, exponents, and grouped coefficients lie in one field of degree at most

$$
D_N=2N\,N!.
\tag{6.2}
$$

No square root from the kernel of `M` enters this coefficient field, because the exact covariance has already replaced its conjugation by the Weyl permutation.

For a spectral-projector factor, `h_mat(A-nu I)<18+log 2` and `h((lambda-nu)^-1)=h(lambda-nu)<18+log 2`. Their sum is less than 38. At most `N-1` factors therefore give

$$
h_{\rm mat}(\Pi_\lambda)\le(N-1)(38+\log N).
$$

Weyl matrices and their adjoints have matrix height zero. For the coefficient consisting of `N^-1 Tr(W* Pi_lambda W Pi_mu)`, three matrix products cost `3log N`, the trace costs `log N`, and the scalar `N^-1` costs `log N`. This checks the precise safe bound

$$
h(\beta_{\lambda,\mu})
\le2(N-1)(38+\log N)+5\log N.
\tag{6.3}
$$

Equal-exponent grouping adds at most `N^2` such coefficients. Successive additions are bounded by the sum of the heights plus `(N^2-1)log 2`. An exponent `iN tau(lambda-mu)` has height at most `80log 10+log N+18+log 2`. These bounds are all dominated, for `N>=3`, by

$$
H_N=100N^3(1+\log N)+80\log10.
\tag{6.4}
$$

These are absolute logarithmic heights, not multiplicative heights and not polynomial coefficient heights. They remain valid when eigenvalues repeat or when equal eigenvalue differences have to be grouped.

## 7. Check of the published quantitative input and the stochastic bound

Huang's Theorem 1.2 accepts distinct algebraic exponents and nonzero algebraic coefficients, with a bound on every individual degree and absolute logarithmic height. The preceding section puts all of them in a single field of degree at most `D_N` and bounds their heights by `H_N`. There are at most `N^2` surviving grouped terms. Zero exponents are allowed, and grouped zero coefficients are omitted.

The full expression `mathfrak L(m,d,h)` in source (7.1) was compared with the typeset theorem. In particular, its repeated factor is the power `m^delta`, not the product `m delta`; its `delta=d^(2m)`, `mu=m d^(6m)(2h/d+3)`, the three terms of `R`, the factors in `r,r',r''`, and the coefficient `39/164` agree with the primary PDF. The paper's definition on page 3 confirms the logarithmic convention for `h`.

Replacing the actual term count, degree, and height by upper bounds is legitimate. All terms are nondecreasing for integers `m,d>=1` and `h>=0`. The apparently decreasing factor `2h/d` in `mu` causes no problem after writing `mu=2mh d^(6m-1)+3m d^(6m)`. Every other factor is positive and nondecreasing on the stated range.

Thus every nonzero adjoint entry at the frozen kick has modulus at least `exp(-F_N)`, with the explicit source function

$$
F_N=\mathfrak L(N^2,D_N,H_N).
$$

Squaring amplitudes, and using the exact-length paths proved above, yields

$$
(P^{L_N})_{u,v}\ge e^{-2L_NF_N},\qquad L_N=6N^2.
$$

Let `q=N^2-1` and `a_N=q exp(-2L_NF_N)`. Then `0<a_N<1`; for example, the explicit formula already has `F_N>1`, making `q exp(-12N^2F_N)<1`. Entrywise subtraction gives

$$
P^{L_N}=a_N\Pi+(1-a_N)Q
$$

with a nonnegative doubly stochastic `Q`. On zero-sum column vectors, its `l^1` contraction is at most `1-a_N`. Iteration, with the remaining powers of `P` having norm one and `||I-Pi||_(1->1)<=2`, proves exactly

$$
\|P^n-\Pi\|_{1\to1}\le2(1-a_N)^{\lfloor n/L_N\rfloor}.
\tag{7.1}
$$

Every eigenvector with eigenvalue different from one has coordinate sum zero. Hence `|lambda|^(L_N)<=1-a_N`; no diagonalizability assumption is needed. The same contraction gives uniqueness of the stationary law. Concavity of `x^(1/L_N)` gives

$$
1-\max_{\lambda\ne1}|\lambda|
\ge a_N/L_N
=\frac{N^2-1}{6N^2}e^{-12N^2F_N}.
\tag{7.2}
$$

This proves Theorem C as an actual explicit positive lower bound. It is not a useful rate at the original spectral scale. If `n` is proportional to `N`, the exponent in (7.1) is eventually zero because `L_N` is quadratic; the extremely small `a_N` would cause an additional problem even at larger times.

## 8. Coherent evolution and the remaining obstruction

The original target is determined by the full adjoint trace, which equals `|Tr U_N^n|^2`. On the nonzero-label block this is one plus its trace. For that restricted block, if `Z_n=|C^n|^(circ 2)`, direct expansion of the square gives

$$
Z_{n+1}=PZ_n+\mathcal E_n,
$$

with the off-diagonal-in-path-label interference sum written in source (8.1). Both `Z_(n+1)` and `PZ_n` are doubly stochastic, so the row and column sums of the difference vanish. This identity provides no small norm for the difference.

The only clarification needed in the source's discussion is to identify explicitly when `C` has been restricted to `Lambda_N`. The same recurrence can alternatively be written for the full matrices by adjoining the isolated identity block to `P`. It is not valid to multiply the restricted `P` by a full `N^2`-dimensional `Z_n` without making one of these conventions. This is a dimension convention in the auxiliary explanation, not a missing ingredient of the proved primitivity or gap theorem.

The first original-family pair discrepancy is still not evaluated. Effective positivity of the auxiliary stochastic dynamics and the uniform anchor transition do not control the signed products of quantum traces through times proportional to `N`. The source makes that limitation explicit, and the present audit retains it.

## 9. Provenance of the verdict

The argument checked here uses the exact modular kernel and Fourier coefficients, elementary finite graph and prime-power arguments, a convergent local matrix series, placewise height bounds, and the precisely identified published transcendence theorem. The finite companion script confirms only its stated finite arithmetic and graph instances. No random-phase replacement, numerical spectral extrapolation, field-degree assumption of a simple spectrum, or unproved quantitative inference from qualitative nonvanishing is used.

The scope of the positive verdict is exactly Theorems A–C. The full spectral-statistics problem remains unresolved.
