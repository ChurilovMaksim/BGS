> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/phase_audit_rational_split_affine_reversal.md`. Embedded SHA256: `8cb78834cfb92c2717a5aa782deaba956d30832a2019b014c07fd71405bfee8b`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: rationally split Weyl-normalizing reversal

Date: 21 October 2026.

## 1. Verdict and frozen inputs

**Verdict: passes as stated.** I found no load-bearing gap in the exclusion of antiunitary Weyl-normalizing reversal for rational $c\in[0,1]$, odd $N\ge75$, and nonzero real algebraic $z_0$. The support and coefficient comparisons are uniform over composite moduli. The proof does not use spectral universality or any long-time trace estimate.

Audited source:

- arithmetic_rational_split_affine_reversal.md  
  SHA-256: a92061a005e3b219b7564b0714ef469b3fb066da0274e73ebdd1faf411d9d36c.
- arithmetic_split_symmetry_check.py  
  SHA-256: 5fdf0566a529e904c706d2f60778f75231e5892e209046755968d74b15b10087.

The exact certificate was executed successfully. The verdict also rests on the independent mathematical reconstruction below; the finite coefficient script is not used to infer a result over infinitely many moduli.

The companion source arithmetic_monomial_reversal_closure.md was at SHA-256
38462ab5c59f850c507b578b9b63092c452e427b48cdf3812a863434bb3a72f9.
The present audit does not assume its main monomial-symmetry theorem. Its imported exponential-polynomial lemma and the needed Gauss-sum trace fact were checked independently.

No audited source was changed.

## 2. Normalizers and the passage from one algebraic parameter to an identity

The modular Weyl matrices $W(k,l)=T_N(l,k)$ satisfy
$W(v)^N=I$ and form an orthogonal basis of the full matrix algebra.
For an antiunitary normalizer, the induced map on labels is an automorphism of the additive group $(\mathbb Z/N\mathbb Z)^2$. It is therefore $\mathbb Z/N\mathbb Z$-linear, including for composite $N$. Its matrix $R$ has determinant $-1$ modulo $N$, because the central commutator is conjugated. Once that determinant sign is inserted in the modular-half multiplication law, the scalar multiplier is a character $\chi$, with values in $\mu_N$. There is no division by a nonunit of $\mathbb Z/N\mathbb Z$ in this argument.

The algebraic-representative argument is valid. After writing the antiunitary as $JK$, its action on Weyl generators is a homogeneous system for the entries of $J$, over algebraic numbers. Any two solutions differ by a scalar, because their quotient commutes with all Weyl matrices; the same assertion for a possibly singular solution follows by multiplying it by the inverse of one given invertible solution. Thus a nonzero algebraic solution exists and is a scalar multiple of a unitary. Its normalization uses the square root of a positive algebraic number. Scalar normalization does not change the conjugation action.

I checked the precise external theorem in the author's primary PDF:

S. A. Popescu, *A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem*, author's version, Theorem 3.2, printed page 14:
https://arxiv.org/pdf/2306.14352.

It gives linear independence over algebraic numbers of exponentials of distinct algebraic numbers. Consequently, after combining equal exponents, a finite exponential polynomial with algebraic coefficients and exponents cannot vanish at a nonzero algebraic parameter unless it is identically zero. Here $A,M$, their required algebraic representatives, and the spectral projections of $A$ all have algebraic entries; $c,z_0$ meet the stated hypotheses. The antiunitary side is analytically continued from real $z$, reversing the sign of the algebraic exponential frequencies. Hence the entrywise application is legitimate.

I also checked the publisher record:
https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16.
It confirms the chapter, pages 349--366, the 2024 bibliographic citation, and the DOI in the source. Its online publication date is 28 December 2023; this does not conflict with the 2024 book citation.

The elimination of the scalar $\eta$ is valid. Cyclicity gives
$$
\operatorname{Tr}U_c(z)=\operatorname{Tr}(e^{iNzA}M).
$$
At zero,
$$
|\operatorname{Tr}M|^2
=\frac1N\sum_{x,y}e_N(-\overline2(x^2-y^2))=1.
$$
The change $u=x-y,\ v=x+y$ is invertible for every odd modulus. Summing $e_N(-\overline2uv)$ first in $v$ leaves only $u=0$, proving the identity without primality. The exponential-polynomial theorem therefore makes the trace nonzero at every nonzero algebraic $z$. Taking traces of the proposed reversal gives
$\overline{\operatorname{Tr}U_c}=\eta\overline{\operatorname{Tr}U_c}$, hence $\eta=1$.

These checks make the proposed reversal an identity in $z$, with $DMD^{-1}=M^{-1}$.

## 3. The derivative preserves the correct Hamiltonian

A potentially important distinction is handled correctly in the source: the antiunitary preserving the effective Hamiltonian is $C=MD$, not necessarily $D$ itself.

With $A_D=DAD^{-1}$, differentiation at zero gives
$$
cA_DM^{-1}+(1-c)M^{-1}A_D
=(1-c)AM^{-1}+cM^{-1}A.
$$
Multiplication on the left by $M$ gives
$$
c\,\operatorname{Ad}_M A_D+(1-c)A_D
=cA+(1-c)\operatorname{Ad}_M A.
$$
Using $DMD^{-1}=M^{-1}$, the left-hand side is
$C H_c C^{-1}$, where
$$
H_c=cA+(1-c)MAM^{-1},\qquad C=MD.
$$
Thus the necessary condition $C H_c C^{-1}=H_c$ is exact. Since $M$ is a Weyl normalizer, so is $C$, with antiunitary determinant sign unchanged.

## 4. Fourier coefficients and modular aliases

I independently reconstructed the pure-$q$ coefficient formula from the original symbol:
$$
a_{(k,0)}
=\frac12\mathbf1_{|k|=7}+\frac{r_k}{10}
-\frac{i}{200}(r_{k-1}-r_{k+1})
-\frac1{10}\mathbf1_{k=0}.
$$
Together with
$$
r_0=1,\quad r_{\pm1}=\frac12,\quad
r_{\pm7}=-\frac12,\quad r_{\pm6}=r_{\pm8}=-\frac14,
$$
this gives the seven positive-frequency coefficients in source (4.1), with the stated conjugates at negative frequencies. In particular
$$
u=a_{(1,0)}=\frac1{20}-\frac{i}{200}.
$$
The mixed coefficients follow directly from
$e^{-i\alpha_0}=(-3-4i)/5$:
$$
a_{(k,1)}=\gamma r_k,\qquad
a_{(k,-1)}=\overline\gamma r_k,\qquad
\gamma=\frac{-3-4i}{1000}.
$$
These are the original modular-Weyl coefficients; no real-half conversion is made.

There are 14 pure-$q$ and 18 mixed nonzero frequencies, hence $|F|=32$. The covariance matrix
$$
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}
$$
has determinant one and sends the original Weyl coefficients to those of $MAM^{-1}$.

The overlap computation is complete. If $(k,l)\in F$ and $S(k,l)\in F$, then both $l$ and $4k+3l$ belong to $\{0,\pm1\}$. For $l=0$, the only candidate $k=0$ is absent. For $l=1$, only $k=-1$ works; for $l=-1$, only $k=1$ works. Their images give
$$
F\cap SF=\{(1,1),(-1,-1)\}.
$$
The union has 62 distinct integer frequencies and is contained in
$[-27,27]\times[-36,36]$. Differences of two frequencies have coordinates bounded by 54 and 72. Since $N\ge75$, reduction modulo $N$ is injective on this entire union. This single rectangle argument proves the alias exclusion for all permitted moduli; no enumeration of moduli is needed.

## 5. Root-of-unity factors and every collision exception

For $0<c<1$, the coefficients at $e_1=(1,0)$, $e_2=(0,1)$ are the nonzero numbers $cu,c\gamma$. Preservation by $C$ implies
$$
h_c(Rv)=\chi(v)\overline{h_c(v)}.
$$
All coefficients belong to $\mathbb Q(i)$ because $c$ is rational. Therefore each $\chi(e_j)$ belongs to $\mathbb Q(i)\cap\mu_N$.

The source's elementary proof that this intersection is $\{1\}$ for odd $N$ is correct: for a root of unity $a+ib$ with rational $a,b$, $2a$ is a rational algebraic integer, hence an integer. The candidates $a=\pm1/2$ give irrational $b$; the remaining possibilities yield $1,-1,i,-i$. Odd order leaves only $1$. Since $e_1,e_2$ generate the label group, $\chi$ is trivial. This does not require $N$ to be prime.

I independently checked collision completeness.

For the target $c\overline u$, the only original coefficient on its positive real ray is $\overline u$. The pure-$q$ coefficients with the same imaginary-to-real ratio but negative real part have the opposite sign and cannot match positive multiples. Mixed coefficients have ratios $\pm4/3$, which differ from $1/10$. Thus the only targets away from the overlaps are
$$
-e_1,\quad\hbox{and at }c=1/2,\quad -Se_1.
$$

For $c\overline\gamma$, only the coefficients
$\overline\gamma r_k$ with $r_k>0$ lie on the required ray. These have $r_0=1$ and $r_{\pm1}=1/2$. The original support yields only $-e_2$. The transformed support yields $-Se_2$ when $c=1/2$, and $S(-1,-1)=(-5,-7)$ when $c=1/3$. The other transformed candidate at $c=1/3$, namely $S(1,-1)=(1,1)$, lies in the overlap and must be checked with its additional coefficient.

At both overlaps the real part is fixed at $-3/2000$. Hence they cannot match $c\overline u$. Matching $c\overline\gamma$ first forces $c=1/2$ from the real part, but then the overlap coefficient is real and the target is not. Thus neither overlap creates an exception, including at $c=1/2$ or $c=1/3$.

The exact certificate independently returned precisely these five rows and no additional collision.

## 6. Exceptional parameters, endpoints, and composite determinants

For $c\notin\{1/2,1/3\}$, the two columns of $R$ must be $-e_1,-e_2$, giving determinant $1$.

For $c=1/2$, the possible column pairs are
$$
(-e_1,-e_2),\quad
(-e_1,-Se_2),\quad
(-Se_1,-e_2),\quad
(-Se_1,-Se_2).
$$
Their integer determinants are respectively $1,3,3,1$.

For $c=1/3$, the first column is $-e_1$, while the second is either $-e_2$ or $(-5,-7)$. The determinants are $1,7$.

None is $-1$ modulo a permitted odd modulus: the necessary divisibilities would be $N\mid2$, $N\mid4$, or $N\mid8$. No division by $3$ or $7$ occurs. When such a determinant is not a unit modulo a composite $N$, it is already excluded by invertibility; the argument does not assume otherwise.

At $c=1$, the coefficients $u,\gamma$ and their conjugate targets are individually unique in $A$. The same field argument forces $R=-I$, with determinant $1$. At $c=0$, conjugating a hypothetical normalizer preserving $MAM^{-1}$ by $M^{-1}$ gives one preserving $A$, reducing to the preceding case.

Thus every parameter in the stated rational interval is covered.

## 7. Scope of the verdict

The final dressing identity is exact:
$$
U_c(z_0)=E^{c-1}U_1(z_0)E^{1-c},\qquad E^s=e^{isNz_0A}.
$$
It uses the explicitly prescribed exponential, not an arbitrary branch of a matrix power. The transferred exclusion of dressed reversers therefore follows.

No correction to the theorem or its proof is required by this audit. The rationality condition is essential to the displayed coefficient-field argument and is not silently enlarged. The lower bound $N\ge75$ is safely sufficient and was not altered.

The verified conclusion excludes the specified geometric normalizer class. It does not exclude the antiunitary obtained from an arbitrary eigenbasis, prove simplicity or CUE statistics, or establish any missing $H_{\mathrm{diag}}$ estimate.

