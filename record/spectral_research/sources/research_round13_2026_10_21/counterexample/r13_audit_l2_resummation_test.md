> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round13_2026_10_21/counterexample/r13_audit_l2_resummation_test.md`. Embedded SHA256: `4573710cbda410fdf27a33e17d7fd730375246089ee03f4e07f36f34e702cd8c`.
> [Thematic guide](../../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: coefficient-square-sum countertest

Date: 21 October 2026. Reviewer: `/root/r13_original_counterexample`.

## Claim and verdict

**Verdict: proved as written.** The audited claim is the auxiliary
countertest in `../signed_sum/r13_exact_l2_resummation_test.md`, SHA-256
`c92306e56c2559c052c0669cc6ee97a72049fb27bf4a91c0accef5dace7eb24f`.
The entire source was read and the critical calculations below were
independently reconstructed from the user-defined kernel. The reviewer
did not edit the source.

For every odd `N`, the auxiliary `K_N=M_N^*` has native Weyl coefficients
of constant modulus `1/N`, is exactly unitary, satisfies the twisted
coefficient identities, and has a globally Haar limiting empirical
spectrum. Nevertheless `K_N M_N=I`, and its tested pair defect grows
linearly with `N`. Thus those coefficient constraints and that global
single-factor limit cannot by themselves imply the proposed local
product statistic. This is not a counterexample for the prescribed
exponential kick and gives no new original-family estimate.

## 1. Native coefficient calculation: passed

Write `h=2^(-1)` and `W_(k,l)=T_N(l,k)`, with all fractions below taken
in `Z/NZ`. Directly from the diagonal entries of the product,

$$
\operatorname{Tr}(W_{(k,l)}M_N^*)
=N^{-1/2}\sum_{x\bmod N}
e_N\left(\frac{3(x+l)^2-2(x+l)x+3x^2}{8}
+k\left(x+\frac l2\right)\right).
$$

The exponent is

$$
\frac{x^2}{2}+\left(\frac l2+k\right)x
+\frac{3l^2}{8}+\frac{kl}{2}
=\frac12\left(x+\frac l2+k\right)^2
+\frac{l^2}{4}-\frac{k^2}{2}.
$$

Translation by `l/2+k` is a permutation of the residues. With
`G=sum_x e_N(x^2/2)` and `gamma=G/sqrt(N)`, this proves

$$
\operatorname{Tr}(W_{(k,l)}M_N^*)
=\gamma e_N(l^2/4-k^2/2).
$$

Since `W_(k,l)^*=W_(-k,-l)`, the quadratic expression is unchanged
when computing the coefficient of `W_(k,l)` in `M_N^*`. Division by
`N` gives exactly the source's coefficient formula, including its sign
and normalization.

For the Gauss modulus, the invertible change of variables
`u=x-y`, `v=x+y` gives

$$
|G|^2=\sum_{u,v\bmod N}e_N(uv/2)=N.
$$

For a fixed `u`, the inner additive-character sum is `N` if `u=0`
and zero otherwise, because `2` is a unit. This works for every odd
composite modulus as well as every odd prime; no Gauss-sum phase
evaluation or squarefree assumption is used. Therefore `|gamma|=1`
and all `N^2` coefficients have modulus `1/N`.

The identity

$$
\sum_v e(v)\overline{e(v-u)}
e_N\left(\tfrac12\sigma(v,u)\right)=\mathbf1_{u=0}
$$

is the coefficient of `W_u` in `EE^*`: the paired labels are `v`
and `-(v-u)`, whose symplectic product is `sigma(v,u)`. Its sign
therefore also agrees with the stated native convention.

## 2. Exact covariance and the fixed-power trace: passed

The covariance

$$
M_NT_N(a,b)M_N^*=T_N(3a+4b,2a+3b)
$$

follows by comparing its kernel with the original one. The resulting
constant terms agree because

$$
\frac12(3a+4b)(2a+3b)
-\frac38(3a+4b)^2
=-\frac38a^2-\frac12ab.
$$

This is a rational polynomial identity with denominator a power of two,
so it remains valid modulo every odd `N`. There is no remaining scalar
phase in this covariance. Consequently, in labels `v=(k,l)`, conjugation
permutes the Weyl basis by

$$
C=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

For any integer `j`, the trace of `Ad_(M_N^j)` in this basis is the
number of fixed residue labels of `C^j`. In an orthonormal eigenbasis
of the unitary `M_N^j`, its eigenvalues on matrix units are
`lambda_a conjugate(lambda_b)`. Taking the sum proves exactly

$$
|\operatorname{Tr}M_N^j|^2
=\#\ker(C^j-I\pmod N).
$$

For a fixed positive `j`, let `D_j=det(C^j-I)`. The eigenvalues
`3+2sqrt(2)` and `3-2sqrt(2)` imply `D_j != 0`. The adjugate identity
sends every vector in this kernel into the solutions of `D_j v=0`.
The latter set has `gcd(N,|D_j|)^2` elements. Thus

$$
\left|N^{-1}\operatorname{Tr}M_N^j\right|
\le |D_j|/N.
$$

This is a fixed-`j` assertion: its constant grows with `j`, and it is
not asserted to control Heisenberg times. Negative `j` follows by
unitarity. Since `K_N=M_N^*`, the same absolute trace bounds apply to
its fixed powers. Uniform approximation of continuous circle functions
by their Fejer convolutions then proves the claimed global Haar limit.
All composite odd dimensions are included.

## 3. Auxiliary defect asymptotic: passed

For the fixed `w=|bhat_*|^2`, one has `w>=0`, compact support in
`[-2,2]`, continuity, and `w(0)>0`. The exact identity `K_NM_N=I`
gives

$$
F_N^{\rm aux}
=\sum_{1\le m<2N}w(m/N)
-N^{-2}\sum_{1\le m<2N}w(m/N)\min(m,N).
$$

The second term is bounded by `2 ||w||_infinity`, uniformly in `N`.
Dividing the first term by `N` gives the Riemann sum for the integral
on `[0,2]`. Therefore

$$
F_N^{\rm aux}/N\longrightarrow\int_0^2w(t)\,dt>0.
$$

The endpoint choices `1<=m<2N` change that Riemann sum by at most
`O(1/N)`. Positivity of the integral follows from continuity and the
strictly positive value at zero. The normalization agrees with the
exact original pair formula after substituting this auxiliary kick.

## 4. Dependency boundary and remaining original gap

The audited countertest needs only the original kernel and finite Weyl
orthogonality, elementary additive-character orthogonality, elementary
linear algebra, and Fejer approximation. No probabilistic independence,
external universality theorem, numerical spectral calculation, or limit
exchange in growing word length is used.

The universal original statement is **not addressed by this countertest**:
the auxiliary `M_N^*` is not the fixed-generator exponential
`exp(i10^(-80)N A_N)`. Its complete coherence proves failure only of
the proposed norm/flatness-only implication. A successful original-family
argument still needs a quantitative correlation estimate for the actual
kick coefficients inside the full closed-product sum, or another proof
of the original weighted pair limit. Neither this audit nor the source
supplies that estimate.

This independent review is evidence from the calculations above, not
a formal proof certificate and not validation of unrelated earlier
project claims.
