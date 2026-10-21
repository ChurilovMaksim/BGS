> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round10_2026_10_21/r10_mixed_isospectral_twirl_obstruction.md`. Embedded SHA256: `673a8fbbe93cb26db469b7c7dd13b5960352e3ec2cdbf9e248aa4d7f2be1d9b9`.
> [Thematic guide](../../topics/closure.md).

# An isospectral average, its exact memory, and the scale of the missing form factor

21 October 2026. Branch `/root/r10_mixed`.

## 0. Scope

This note proves an exact discriminator for a proposed mixed-determinant
method. It does **not** prove or refute the prescribed original
`H_diag`. In particular, the Haar conjugations below are auxiliary
mathematical probes; they are not additional randomness in the problem.

The new point is that an ensemble which preserves every spectral
observable can have a perfectly mixing averaged adjoint, although its
actual microscopic statistics are non-CUE. The exact quantity lost by
replacing powers of one sample by powers of the averaged operator is
computed. Even within CUE, that replacement has operator error
`O(1/N)` uniformly at every time, but loses a strictly positive limiting
weighted form factor. Thus a generic `o(1)` comparison of averaged
operators cannot justify the required signed microscopic trace sum.

The deleted-clock spectral defect used for the first illustration was
proved in Round 9. No new original-family counterexample is claimed.

## 1. Exact conjugacy averaging of one adjoint

Let `N >= 2`, let `U` be an arbitrary unitary matrix, and give
`M_N(C)` the Hilbert--Schmidt inner product. Set

$$
 \mathcal C_U(X)=UXU^*,\qquad
 P(X)=\frac{\operatorname{Tr}X}{N}I,\qquad Q=I-P.
$$

Here `I` in `Q=I-P` denotes the identity on matrix space. Let `G` have
normalized Haar distribution on `U(N)` and put `Y_G=GUG^*`. Then

$$
 \boxed{\mathbb E_G\mathcal C_{Y_G}
       =P+a_1(U)Q,\qquad
 a_1(U)=\frac{|\operatorname{Tr}U|^2-1}{N^2-1}.}
 \tag{1.1}
$$

### Proof without an irreducibility assumption

Write `T=E_G C_{Y_G}`. Haar invariance implies that `T` commutes with
conjugation by every fixed unitary. Let `E_{ij}` denote matrix units.
Conjugation by a diagonal unitary multiplies `E_{ij}`, `i != j`, by
the character `exp(i(t_i-t_j))`. All these nontrivial characters are
distinct, so commuting with every diagonal conjugation forces
`T(E_{ij})=a_{ij}E_{ij}`. Permutation conjugations force all the
`a_{ij}`, `i != j`, to equal one number `a`.

The zero-character space consists of diagonal matrices. Permutations
fixing `i`, followed by permutations carrying `i` to another index,
show that there are numbers `c,d`, independent of `i`, with

$$
 T(E_{ii})=cE_{ii}+d\sum_{k\ne i}E_{kk}.
$$

A real rotation by angle `pi/4` in the `i,j` coordinate plane
conjugates `E_{ii}-E_{jj}` to plus or minus `E_{ij}+E_{ji}`.
Commutation with this rotation gives `c-d=a`. Consequently, on all
matrix units, and hence on all matrices,

$$
 T(X)=aX+d\operatorname{Tr}(X)I.
$$

Each conjugation fixes `I`, so `a+Nd=1`. This gives `T=P+aQ`.
The trace of a conjugation as an operator on matrix space is

$$
 \operatorname{Tr}_{\rm HS}\mathcal C_U
 =\sum_{i,j}U_{ii}\overline{U_{jj}}
 =|\operatorname{Tr}U|^2.
$$

Conjugating `U` does not change its trace. Since `P` has rank one
and `Q` has rank `N^2-1`, taking the operator trace of `T=P+aQ`
determines `a` and proves (1.1). All steps apply also when `U` has
repeated eigenvalues. $\square$

## 2. Powers of one sample and powers after independent resampling

For each integer `m >= 1`, define

$$
 a_m(U)=\frac{|\operatorname{Tr}U^m|^2-1}{N^2-1}.
$$

Since `Y_G^m=GU^mG^*`, applying (1.1) to `U^m` gives

$$
 \boxed{\mathbb E_G\mathcal C_{Y_G}^{\,m}=P+a_m(U)Q.}
 \tag{2.1}
$$

The same `G` is retained throughout the power on the left. In
contrast, orthogonality of `P,Q` gives

$$
 \boxed{\bigl(\mathbb E_G\mathcal C_{Y_G}\bigr)^m
       =P+a_1(U)^mQ.}
 \tag{2.2}
$$

The latter operator is the expected product when the conjugation is
independently resampled at every step. Subtracting yields the exact
memory term

$$
 \boxed{
 \mathbb E_G\mathcal C_{Y_G}^{\,m}
 -\bigl(\mathbb E_G\mathcal C_{Y_G}\bigr)^m
 =\bigl(a_m(U)-a_1(U)^m\bigr)Q.}
 \tag{2.3}
$$

There is no reason for (2.3) to be small on times proportional to `N`.
In fact it contains exactly the original unknown trace modulus.

## 3. The averaging preserves the entire mixed source

Define `D_U(z)=det(I-zU)` and `D_U^\#(z)=det(I-zU^*)`. For
`|a|,|b|<1` and arbitrary complex `c,d`, the full mixed source is

$$
 \Omega_U(a,c;b,d)=\int_0^{2\pi}
 \frac{D_U(ce^{it})D_U^\#(de^{-it})}
      {D_U(ae^{it})D_U^\#(be^{-it})}
 \,\frac{dt}{2\pi}.
 \tag{3.1}
$$

Its denominator is nonzero on the integration circle. For every
`G`, each of the four determinants is unchanged under
`U -> GUG^*`. Hence

$$
 \boxed{\mathbb E_G\Omega_{Y_G}(a,c;b,d)
                 =\Omega_U(a,c;b,d).}
 \tag{3.2}
$$

The same statement holds for every factorial statistic and every
bounded local Laplace observable: all depend only on the spectrum.
Thus (3.2) is an exact average which does not alter the target, but
using only its one-step averaged adjoint (1.1) discards (2.3).

For comparison, the actual allowed center rotation has an even
simpler action on adjoints:

$$
 \mathcal C_{e^{it}U}=\mathcal C_U.
 \tag{3.3}
$$

It introduces no contraction of this operator at all.

To see exactly where the pair statistic sits in (3.1), differentiate
both numerator sources and then match them to the denominators.
The absolutely convergent series

$$
 \frac{D'_U(z)}{D_U(z)}
     =-\sum_{m\ge1}\operatorname{Tr}(U^m)z^{m-1},\qquad |z|<1,
$$

and Fourier orthogonality give

$$
 \boxed{
 \left.\partial_c\partial_d\Omega_U(a,c;b,d)\right|_{c=a,d=b}
 =\sum_{m\ge1}(ab)^{m-1}|\operatorname{Tr}U^m|^2.}
 \tag{3.4}
$$

Every series and derivative here is justified on closed smaller
disks by uniform absolute convergence. In particular the mixed
source contains all the `a_m`, not only `a_1`.

## 4. Perfect mixing of the averaged adjoint is compatible with a non-CUE local law

Take the Round 9 deleted clock

$$
 Z_N=\operatorname{diag}(e^{2\pi i j/(N+1)}:1\le j\le N).
$$

The geometric sum gives

$$
 p_m(Z_N)=
 \begin{cases}N,&N+1\mid m,\\-1,&N+1\nmid m.\end{cases}
 \tag{4.1}
$$

In particular `a_1(Z_N)=0`, so

$$
 \mathbb E_G\mathcal C_{GZ_NG^*}=P
 \tag{4.2}
$$

exactly. On the trace-zero matrix space the averaged adjoint is zero:
its contraction is as strong as possible. Nevertheless, every member
of this ensemble has the deleted-clock spectrum.

For a self-contained fixed-test comparison, choose the nonnegative
even smooth bump

$$
 \phi_0(\xi)=e^{-1/(1-16\xi^2)}\mathbf1_{|\xi|<1/4},\qquad
 I_0=\int\phi_0,\qquad
 b_0=|\mathcal F^{-1}\phi_0|^2/(2I_0^2).
$$

Integration by parts and the Fourier product formula show that
`b_0` is an admissible Schwartz test with `0 <= b_0 <= 1/2`,
and `bhat_0` is supported in `[-1/2,1/2]` and positive in its
interior. The exact pair identity in the question gives

$$
 \Delta_{2,N}^{Z}(b_0)
 =\frac1{N^2}\sum_{1\le m<N/2}
     |\widehat b_0(m/N)|^2(1-m)
 \longrightarrow
 -\int_0^{1/2}u|\widehat b_0(u)|^2\,du<0.
 \tag{4.3}
$$

Here the CUE value `E|p_m|^2=min(m,N)` is proved in Section 5.
The two factors in the pair test have Fourier indices `m,-m`;
their equal contributions cancel its factor `1/2`, which verifies
the normalization in (4.3).

Equations (4.2)--(4.3) prove that exact mixing of this averaged
adjoint, even for an isospectral ensemble, is insufficient for
microscopic CUE statistics. More specifically, for `1 <= m < N+1`
both sides of (2.2) and (2.1) equal `P`, and therefore supply no CUE
ramp. At `m=N+1`, the actual power average is the identity and the
resampled power is `P`, giving maximal memory. These are distinct
features; the small-band defect in (4.3) does not require the
resonance at `N+1`.

This example does not have the prescribed original dynamics and is
not a counterexample to the original question. It rejects the stated
inference about averaging operators, not every method using a
carefully controlled average.

## 5. Even CUE loses its whole ramp under an `O(1/N)` operator error

Let `V` be a single Haar unitary in `U(N)`. Then

$$
 \mathbb E_V\mathcal C_V=P,\qquad
 \mathbb E_V\mathcal C_V^{\,m}
 =P+\frac{\min(m,N)-1}{N^2-1}Q.
 \tag{5.1}
$$

To prove the second formula, the same commutant calculation as in
Section 1 applies because the law of `V^m` is invariant under fixed
conjugations. Its operator trace is `E|Tr(V^m)|^2`. We now verify
that value explicitly.

The Haar eigenangle density, with respect to normalized angular
measure, is

$$
 \frac1{N!}\left|\det(e^{ir\theta_j})_{{j=1,\ldots,N}\atop{r=0,\ldots,N-1}}\right|^2.
 \tag{5.2}
$$

For completeness, the eigenvalue Jacobian follows by writing a
simple-spectrum unitary as `W diag(lambda_j) W^*`: each independent
off-diagonal complex tangent coordinate is multiplied in the
invariant metric by `|lambda_i-lambda_j|^2`. Their product is the
squared Vandermonde in (5.2). The repeated-spectrum strata have
smaller dimension, and hence zero invariant volume. Expanding the
two Vandermondes and integrating characters leaves `N!` equal
permutation pairs, which fixes the normalization. The invariant
volume normalized to mass one is Haar measure.

Integrating (5.2) in all but two variables and using orthogonality
of `1,e^{it},...,e^{i(N-1)t}` gives the factorial density

$$
 \rho_{2,N}(t,s)
 =N^2-\left|\sum_{r=0}^{N-1}e^{ir(t-s)}\right|^2.
 \tag{5.3}
$$

This last integration can also be seen directly by expanding both
determinants: after integration in the remaining `N-2` variables,
the two unintegrated row choices are either in the same order or
interchanged. Their sums are respectively `N^2` and the squared
kernel in (5.3); equal row choices cancel. The diagonal contribution
to `E|p_m|^2` is `N`. For `m >= 1`, the `N^2` term in (5.3)
integrates to zero against `e^{im(t-s)}`. The squared kernel term
counts pairs `0 <= r,s < N` with `r-s=-m`, of which there are
`(N-m)_+`. Thus

$$
 \mathbb E|p_m(V)|^2=N-(N-m)_+=\min(m,N).
 \tag{5.4}
$$

For `m=1`, (5.4) and Section 1 give the first formula of (5.1).
Since `Q` is an orthogonal projection, (5.1) implies the uniform
operator-norm bound

$$
 \boxed{
 \left\|\mathbb E\mathcal C_V^{\,m}
       -(\mathbb E\mathcal C_V)^m\right\|_{\rm HS\to HS}
 =\frac{\min(m,N)-1}{N^2-1}
 \le\frac1{N+1}.}
 \tag{5.5}
$$

Let `w` be any continuous nonnegative, nonzero function of compact
support in `[0,B]`, with `B>0`. Equation (5.1) also gives

$$
 \begin{aligned}
 &\frac1{N^2}\sum_{m\ge1}w(m/N)
 \operatorname{Tr}_{\rm HS}
 \left(\mathbb E\mathcal C_V^{\,m}
       -(\mathbb E\mathcal C_V)^m\right)\\
 &\hspace{12mm}
 =\frac1{N^2}\sum_{m\ge1}w(m/N)(\min(m,N)-1)\\
 &\hspace{12mm}
 \longrightarrow \int_0^B w(u)\min(u,1)\,du>0.
 \end{aligned}
 \tag{5.6}
$$

The limit follows from the Riemann sum for the term `min(m,N)`;
the constant `1` contributes `O(1/N)`. Positivity follows because
a continuous nonzero nonnegative `w` is positive on an interval
containing positive values of `u`.

This is a precise rate obstruction: a uniform `O(1/N)` error
acting on `N^2` matrix directions and summed over `O(N)` times
can retain an order-one normalized contribution. In general the
elementary estimate is

$$
 \left|\frac1{N^2}\sum_{m\le BN}w(m/N)
                  \operatorname{Tr}_{\rm HS}R_{m,N}\right|
 \le\sum_{m\le BN}|w(m/N)|\,\|R_{m,N}\|.
 \tag{5.7}
$$

Thus `sup ||R_{m,N}||=o(1/N)` would suffice by this norm argument;
`o(1)` does not, and (5.6) shows that `O(1/N)` cannot replace
`o(1/N)` in a generic assertion. A weaker norm rate could still
suffice if the actual full trace sum had additional cancellation.
Proving such cancellation is precisely the kind of missing input
required for the original family.

## 6. Original-family consequence and first unresolved estimate

All identities in Sections 1--3 apply to the original `U_N` without
changing its fixed kick or its dimensions. They supply no bound on
`a_m(U_N)` for `m` proportional to `N`. Replacing that unknown
quantity by `a_1(U_N)^m`, or by its Haar value, is not licensed by
the identities or by an averaged spectral gap.

The first original open test therefore remains exactly

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0,
$$

where `b_*` is fixed in the Round 10 checkpoint. No `o(1)` bound
for this expression and no original countersequence are obtained.

## 7. Actual inputs and provenance

The elementary proofs above introduce no external universality
theorem. The following raw local proofs were read to fix scope and
avoid re-presenting old determinant or resolvent reductions as new.
The hashes are for the actual bytes read on 21 October 2026.

| Input | SHA-256 |
|---|---|
| Frozen master, byte-verified checkpoint | `e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777` |
| `round10_target_checkpoint.md` | `a35e09d5678b1f718f7deaa1c726afa5c692886010eb41f748e8f9f1624378f0` |
| `r9_determinant_exact_cue_detdet_counterexample.md` | `4fd909b04e8ccc1a000930e46e6efe23b520e8d41400d8f923e3aa7911623b7f` |
| `r9_determinant_nonzero_minors_addendum.md` | `69233cc4b5d5772bafbf7d95aceb792f7e4a2f5f579500120984c4bf1693cc79` |
| `r9_determinant_braun_haake_and_contraction_audit.md` | `979cdac97772c3a10d6b186c13f066677d8d4bcf2f0bc05f4a300609f5af67f9` |
| `phase_commutant_integration_discriminator.md` | `df3c9b16210c64341f804ff28a0dd30beb366a0610016168edcb72fab5f0052a` |
| `fermionic_resolvent_frame.md`, used Sections 1--5 | `1e88189aa0192786ad4947091079efa93079aad8fe9a7194a00692c0fccb184f` |

Only a new `r10_mixed_*` branch file was written. No historical proof
or shared master was edited.
