> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_rational_split_affine_reversal.md`. Embedded SHA256: `a92061a005e3b219b7564b0714ef469b3fb066da0274e73ebdd1faf411d9d36c`.
> [Thematic guide](../../topics/symmetry.md).

# Weyl-normalizing antiunitary reversal under rational kick splitting

Date: 21 October 2026.

## 1. Result

Let $A_N,M_N$ be the exact matrices in the question and put
$$
 U_{c,N}(z)=e^{icNzA_N}M_N e^{i(1-c)NzA_N}.
 \tag{1.1}
$$

**Theorem 1.** For every odd $N\geq75$, every rational $c\in[0,1]$,
and every nonzero real algebraic $z_0$, there is no antiunitary normalizer
$D$ of the finite modular Weyl group such that
$$
 D U_{c,N}(z_0)D^{-1}=\eta U_{c,N}(z_0)^{-1}
 \tag{1.2}
$$
for any scalar $\eta$.

In particular, the symmetric split $c=1/2$ has no affine
anti-symplectic or Weyl-normalizing time reversal. This is a theorem
about a specified operator class, not a deduction of spectral
universality from a symmetry classification.

The proof uses the exact Fourier coefficients of the original
modular quantization and a necessary condition from a single derivative
of the matrix identity. It includes all translations and metaplectic
linear transformations in the Weyl normalizer, in every sufficiently
large odd composite dimension.

The restriction $c\in\mathbb Q$ in this theorem is deliberate. The
coefficient-field step below uses $\mathbb Q(i)\cap\mu_N=\{1\}$.
No extension of this particular theorem to arbitrary real algebraic
$c$ is claimed. The distinct arbitrary-phase monomial theorem in
the companion manuscript does hold for all real algebraic $c$.

## 2. Exact normalizer and analytic facts

Write $A=A_N,\ M=M_N$, and use the original frequency-indexed
modular Weyl basis
$$
 W(k,l)=T_N(l,k).
$$
The exact covariance, checked directly from the quadratic kernel, is
$$
 M W(v)M^{-1}=W(Sv),\qquad
 S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
 \tag{2.1}
$$
Also $M^T=M$ and $\overline M=M^{-1}$.

An antiunitary normalizer $C$ acts by
$$
 C W(v)C^{-1}=\chi(v)W(Rv),\qquad
 \det R=-1\pmod N,\quad \chi(v)\in\mu_N.
 \tag{2.2}
$$
Here $R$ is a linear automorphism of $(\mathbb Z/N\mathbb Z)^2$,
and $\chi$ is an additive character. These statements hold over
composite moduli as well. To see this, take the quotient of the Weyl
group by its scalar center. Its automorphism is an automorphism of
the additive group $(\mathbb Z/N\mathbb Z)^2$, hence is linear.
The central commutator is conjugated by an antiunitary, giving the
determinant sign. Substitution in the exact Weyl multiplication law,
with its modular half, then makes the remaining scalar a character.
Finally $W(v)^N=I$, so $\chi(v)^N=1$.

Every such normalizer conjugation has an algebraic matrix representative
up to an irrelevant scalar. Indeed, write $C=JK$, where $K$ is
coordinate conjugation. Since $K W(k,l)K=W(-k,l)$, equation (2.2)
is a homogeneous linear system for $J$ with algebraic coefficients.
Its solution space is one dimensional: if $J_0$ is the given
invertible solution and $X$ is any solution, then $J_0^{-1}X$
commutes with all the Weyl matrices. These matrices span the full
matrix algebra, by trace orthogonality, so $J_0^{-1}X$ is scalar.
Gaussian elimination therefore produces an algebraic nonzero
solution. It is a scalar times a unitary matrix. Dividing by
the positive square root of
$\operatorname{Tr}(J^*J)/N$, which is algebraic, makes the
representative unitary without changing its conjugation action.

We use the following already proved lemma from the companion source
arithmetic_monomial_reversal_closure.md, SHA-256
38462ab5c59f850c507b578b9b63092c452e427b48cdf3812a863434bb3a72f9:

> A finite exponential polynomial
> $\sum_j a_j e^{\lambda_j z}$, with all $a_j,\lambda_j$
> algebraic, which vanishes at a nonzero algebraic $z_0$,
> vanishes identically.

This is a direct application of the Lindemann--Weierstrass theorem
after equal $\lambda_j$ are combined; the remaining
$\lambda_jz_0$ are distinct algebraic numbers. The published reference
and its exact hypotheses are recorded in that source, Section 3.
For a standalone reference, see S. A. Popescu, Theorem 3.2 in the
[author's version](https://arxiv.org/pdf/2306.14352) of
*A Simple and Self-contained Proof for the Lindemann--Weierstrass
Theorem*, published in *New Frontiers in Number Theory and Applications*,
Springer, 2024, pp. 349--366,
DOI [10.1007/978-3-031-51959-8_16](https://doi.org/10.1007/978-3-031-51959-8_16).

The applicability here is exact. The entries of $A,M$ are algebraic.
The eigenvalues of the Hermitian $A$ are real algebraic, and their
spectral projections are polynomial expressions in $A$ with
algebraic coefficients. Thus every entry of $U_c(z)$, its inverse,
and the analytic continuation of its complex conjugate is such a
finite exponential polynomial when $c$ is algebraic.

Furthermore
$$
 \operatorname{Tr}U_c(z)=\operatorname{Tr}(e^{iNzA}M)
$$
is nonzero at every nonzero algebraic $z$. It is nonzero at zero,
because
$$
 |\operatorname{Tr}M|^2
 =N^{-1}\left|\sum_x e_N(-\overline2x^2)\right|^2=1.
$$
The last equality follows by the invertible change
$(x,y)\mapsto(x-y,x+y)$ and character orthogonality; it does not
require $N$ to be prime. The exponential-polynomial lemma then
proves the claimed nonvanishing. Taking traces in (1.2) gives
$\eta=1$, using unitarity for real $c,z_0$.

Choose the algebraic representative of $D$. Every entry of
$$
 D U_c(z)D^{-1}-U_c(z)^{-1}
$$
has the stated exponential-polynomial interpretation, where on the
left one analytically continues the complex conjugation from real
$z$. The lemma therefore makes (1.2), with $\eta=1$, an identity
in $z$. In particular
$$
 DMD^{-1}=M^{-1}.
 \tag{2.3}
$$

## 3. A necessary Hamiltonian symmetry

Set $A_D=DAD^{-1}$. Differentiating the analytic identity at zero
gives
$$
 cA_D M^{-1}+(1-c)M^{-1}A_D
 =(1-c)AM^{-1}+cM^{-1}A.
$$
Multiplication on the left by $M$ yields
$$
 c\,\operatorname{Ad}_M A_D+(1-c)A_D
 =cA+(1-c)\operatorname{Ad}_M A.
 \tag{3.1}
$$
Define
$$
 H_c=cA+(1-c)\operatorname{Ad}_M A,\qquad C=MD.
 \tag{3.2}
$$
The operator $C$ is an antiunitary Weyl normalizer. It satisfies
$$
 C A C^{-1}=\operatorname{Ad}_M A_D,\qquad
 C(\operatorname{Ad}_M A)C^{-1}=A_D,
$$
where the second equality uses (2.3). Equation (3.1) is therefore
precisely
$$
 C H_c C^{-1}=H_c.
 \tag{3.3}
$$
The rest of the proof excludes (3.3).

## 4. Exact Fourier support, without modular aliases

Let $a_v$ be the ordinary Fourier coefficients of $f-1/10$, so
$$
 A=\sum_v a_vW(v).
$$
They are the coefficients of the original modular Weyl basis. The
pure-$q$ coefficients at positive frequencies are exactly
$$
 \begin{array}{c|rrrrrrr}
 k&1&2&5&6&7&8&9\\ \hline
 a_{(k,0)}
 &\dfrac1{20}-\dfrac{i}{200}
 &-\dfrac{i}{400}
 &-\dfrac{i}{800}
 &-\dfrac1{40}-\dfrac{i}{400}
 &\dfrac9{20}
 &-\dfrac1{40}+\dfrac{i}{400}
 &\dfrac{i}{800}.
 \end{array}
 \tag{4.1}
$$
Negative coefficients are complex conjugates, and all other
pure-$q$ coefficients vanish, including the constant term. To
verify the sine contribution directly, one may use
$$
 r(q)\sin(2\pi q)
 =\sin(2\pi q)
 +\frac{\sin(4\pi q)+\sin(12\pi q)-\sin(16\pi q)}2
 +\frac{\sin(10\pi q)-\sin(18\pi q)}4.
$$
The mixed coefficients are
$$
 a_{(k,1)}=\gamma r_k,\qquad
 a_{(k,-1)}=\overline\gamma r_k,\qquad
 \gamma=\frac{-3-4i}{1000},
 \tag{4.2}
$$
with
$$
 r_0=1,\quad r_{\pm1}=\frac12,\quad r_{\pm7}=-\frac12,\quad
 r_{\pm6}=r_{\pm8}=-\frac14.
 \tag{4.3}
$$
All omitted coefficients vanish.

Write $F=\{v:a_v\ne0\}$. It has 32 elements. The support of
$\operatorname{Ad}_M A$ is $SF$, and
$$
 F\cap SF=\{(1,1),(-1,-1)\}.
 \tag{4.4}
$$
For a direct check, if $(k,l)\in F$ and $S(k,l)\in F$, then
$l=0,\pm1$ and $4k+3l=0,\pm1$. With $l=0$ this gives
$k=0$, which is absent. With $l=1$ the only integer solution
is $k=-1$; with $l=-1$ it is $k=1$. These give exactly
the two points in (4.4).

The union $F\cup SF$ has 62 elements, all with
$$
 |k|\leq27,\qquad |l|\leq36.
$$
For $N\geq75$, two different indices in this rectangle cannot be
congruent modulo $N$, since their coordinate differences have
absolute values at most 54 and 72. Thus (4.1)--(4.4) remain exact
and unaliased in the modular Weyl expansion.

Put
$$
 u=\frac1{20}-\frac{i}{200},\qquad
 e_1=(1,0),\quad e_2=(0,1).
$$
For $0<c<1$, the coefficients $h_c(v)$ of $H_c$ satisfy
$$
 h_c(e_1)=cu,\qquad h_c(e_2)=c\gamma.
 \tag{4.5}
$$
The transformed support does not contain these two indices.

## 5. Complete coefficient collision table

For $0<c<1$, the full list of targets whose coefficient equals
$c\overline u$ or $c\overline\gamma$ is
$$
 \begin{array}{c|c|c}
 \text{target coefficient}&\text{index}&\text{condition}\\ \hline
 c\overline u&-e_1&\text{every }c\\
 c\overline u&-Se_1=(-3,-4)&c=1/2\\ \hline
 c\overline\gamma&-e_2&\text{every }c\\
 c\overline\gamma&-Se_2=(-2,-3)&c=1/2\\
 c\overline\gamma&S(-1,-1)=(-5,-7)&c=1/3.
 \end{array}
 \tag{5.1}
$$
There are no other targets, including at the overlap indices.

Here is a direct verification of completeness. Outside the two
overlaps, every coefficient is either $ca_v$ or
$(1-c)a_v$. Inspection of (4.1)--(4.3) shows that the only
original coefficient on the positive real ray through
$\overline u$ is $\overline u$ itself, at $-e_1$.
The pure-$q$ coefficients with that ratio of imaginary to real
part and negative real part lie on the opposite ray and cannot
match a positive multiple when $0<c<1$. The mixed coefficients
have imaginary-to-real ratios $4/3$ or $-4/3$, whereas that
ratio for $\overline u$ is $1/10$. The two allowed possibilities
are consequently $cu$-conjugate at $-e_1$ and, only if
$1-c=c$, at $-Se_1$.

For the positive ray through $\overline\gamma$, the original
coefficients are $\overline\gamma r_k$ with $r_k>0$.
Equation (4.3) leaves $r_0=1$ and $r_{\pm1}=1/2$.
In the original support, matching $c\overline\gamma$ requires
$r_k=1$. In the transformed support, it requires
$(1-c)r_k=c$. These give $c=1/2$ at $k=0$, and
$c=1/3$ at $k=\pm1$.
The transformed image $S(-1,-1)=(-5,-7)$ is not an overlap,
whereas $S(1,-1)=(1,1)$ is.

The two overlap coefficients are explicitly
$$
 \begin{split}
 h_c(1,1)&=\frac{c\gamma+(1-c)\overline\gamma}{2},\\
 h_c(-1,-1)&=\frac{c\overline\gamma+(1-c)\gamma}{2}.
 \end{split}
 \tag{5.2}
$$
Their real part is always $-3/2000$, so they cannot equal
$c\overline u$, whose real part is positive. For equality to
$c\overline\gamma$, the real part forces $c=1/2$;
at that value (5.2) is real, while $c\overline\gamma$ has
nonzero imaginary part. Thus neither overlap supplies a target.
This proves (5.1).

The exact script arithmetic_split_symmetry_check.py independently
constructs all coefficients using rational pairs, solves each of
the 62 complex linear collision equations, and checks (5.1).
The preceding argument proves completeness and the uniform
no-alias passage in $N$; no asymptotic claim is inferred from a
finite numerical experiment.

## 6. Determinant obstruction and conclusion

For odd $N$,
$$
 \mathbb Q(i)\cap\mu_N=\{1\}.
 \tag{6.1}
$$
For an elementary proof, if $\xi=a+ib\in\mathbb Q(i)$ is a root of
unity then $2a=\xi+\xi^{-1}$ is a rational algebraic integer,
so is an integer in $[-2,2]$. This can also be seen from the
monic recurrence polynomial for $\xi^n+\xi^{-n}$, followed by
the rational root theorem. The options $a=\pm1/2$ would force
irrational $b=\pm\sqrt3/2$; the others give only
$\xi\in\{1,-1,i,-i\}$. Odd order leaves $\xi=1$.

Suppose $C$ in (3.3) exists and let its index map and character
be $R,\chi$ as in (2.2). Since $c$ is rational, every $h_c(v)$
belongs to $\mathbb Q(i)$. Comparing Weyl coefficients gives
$$
 h_c(Rv)=\chi(v)\overline{h_c(v)}.
 \tag{6.2}
$$
For $0<c<1$, equation (4.5) is nonzero at $e_1,e_2$.
The ratio in (6.2) consequently puts $\chi(e_j)$ in
$\mathbb Q(i)\cap\mu_N$, so both values equal one.
They determine the character on the whole index group; hence
$\chi\equiv1$.

The two columns $Re_1,Re_2$ must now be chosen from (5.1).
If $c\notin\{1/2,1/3\}$, they are $-e_1,-e_2$, so
$\det R=1$. At $c=1/2$, the four possible pairs of columns
give determinant $1$ or $3$. At $c=1/3$, they give
determinant $1$ or $7$. None of these values can be congruent
to $-1$ modulo an odd $N\geq75$, since this would require
$N\mid2$, $N\mid4$, or $N\mid8$. This contradicts (2.2).

The endpoints $c=1$ and $c=0$ are also excluded. For $c=1$,
$H_c=A$; the coefficient table (4.1)--(4.3) makes $u$ and
$\gamma$ unique at $e_1,e_2$, with their conjugates unique
at $-e_1,-e_2$. The same field argument yields
$\chi\equiv1$ and $R=-I$, whose determinant is $1$.
For $c=0$, $H_c=MAM^{-1}$; conjugating the hypothetical
antiunitary normalizer preserving it by $M^{-1}$ would give
one preserving $A$, which was just excluded.
This proves Theorem 1.

## 7. Exact scope for the original kicked matrix

Define $E^s:=e^{isNz_0A}$ for every real $s$; this is a specified
exponential and not a branch choice for a fractional matrix power.
Then
$$
 U_c(z_0)=E^{c-1}U_1(z_0)E^{1-c}.
$$
Consequently, for rational $c\in[0,1]$, the original $U_1(z_0)$
has no reverser of the explicitly dressed form
$$
 E^{1-c}D E^{c-1}
$$
with $D$ an antiunitary Weyl normalizer. The case $c=1/2$
includes the natural half-kick dressing used with a symmetric
Floquet splitting.

Together with the companion arbitrary-phase monomial theorem,
this closes these two specified geometric symmetry mechanisms.
It does not exclude an arbitrary antiunitary written in an
eigenbasis, prove a random-matrix symmetry class for the spectrum,
or estimate the signed weighted trace sums required by
$H_{\rm diag}$. Those spectral estimates remain unproved.
