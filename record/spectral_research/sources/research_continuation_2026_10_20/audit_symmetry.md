> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_continuation_2026_10_20/audit_symmetry.md`. Embedded SHA256: `9b47c3dbdf5a9a00b9e57a7723e80ddf280b4e8d932d495f1998010788658404`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: Weyl symmetries and exact CRT nonfactorization

Date: 20 October 2026.

Audited source: `affine_reversal_and_crt_obstructions.md`, SHA-256
`856f7e0d7373e1b3c260b20477969a12e3e78886836b11fd4eac9ddd9cc7642c`.

The exact matrix definitions were checked against
`odd_trace_and_algebraic_rigidity.md`, SHA-256
`42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b`.

## 1. Verdict and scope

The packet's stated theorems pass this independent audit. The modular signs,
the character reduction, the treatment of composite odd dimensions, the
antiunitary continuation, and the CRT argument are valid. No correction to
the source is needed.

In particular, for every odd $N\geq3$, $N\neq7$, and every nonzero real
algebraic $z$, the original family

$$
U_N(z)=e^{izNA_N}M_N
$$

has only scalar unitary projective commuters within the Weyl normalizer. It
has no antiunitary projective commuter and no unitary or antiunitary
projective reverser in that group. For every nontrivial coprime odd CRT
partition $N=rs$, its matrix is not a tensor product in the canonical CRT
coordinates at any nonzero algebraic parameter, including complex ones.

The proof below reconstructs the claims from the exact matrices. It does
not use another audit's verdict or extrapolate a finite computation. Two
useful refinements are proved explicitly:

1. For the centered family, the projective scalar obtained after analytic
   continuation is constant, by the determinant identity.
2. CRT nonfactorization has a single explicit realignment-minor witness:
   its derivative at zero is $iN c_N(1,0)\neq0$.

These are exact exclusion results for the specified structures. They do
not imply a quantitative separation from a symmetry or a tensor product,
simple spectrum, the desired signed orbit cancellation, or Hdiag. An
arbitrary finite unitary still has an antiunitary reverser in an eigenbasis.

## 2. Derivation of the Weyl signs

All indices in this section are in $\mathbb Z/N\mathbb Z$, with $N$ odd.
Put $h_2=2^{-1}\pmod N$, and use the packet's exact convention

$$
(W_N(k,l)u)(x)=e_N\bigl(k(x+h_2l)\bigr)u(x+l),
\qquad e_N(a)=e^{2\pi ia/N}.
$$

For $v=(k,l)$, $w=(k',l')$, set

$$
\omega(v,w)=kl'-lk'.
$$

Multiplying the two operators directly gives

$$
W_N(v)W_N(w)
=e_N\bigl(-h_2\omega(v,w)\bigr)W_N(v+w).
\tag{2.1}
$$

Indeed, the phase left after removing that of $W_N(v+w)$ is

$$
k'l-h_2(kl'+k'l)=-h_2(kl'-lk').
$$

Consequently

$$
W_N(v)W_N(w)W_N(v)^{-1}W_N(w)^{-1}
=e_N(-\omega(v,w))I.
\tag{2.2}
$$

Also $W_N(v)^j=W_N(jv)$, so $W_N(v)^N=I$. The modular-half convention
makes $W_N(k,l)$ exactly periodic in each integer index modulo $N$.
There is no extra sign upon aliasing the Fourier coefficients. Replacing
the modular half by a real half at this point would change the problem.

The trace and orthogonality formulas are

$$
\operatorname{Tr}W_N(v)=N\mathbf1_{v=0},\qquad
\operatorname{Tr}(W_N(v)^*W_N(w))=N\mathbf1_{v=w}.
\tag{2.3}
$$

For the first identity, a nonzero shift has no diagonal entries, while a
nontrivial clock has a zero geometric sum. The second follows from (2.1).
Thus the Weyl matrices form a basis of the full matrix algebra for every
odd $N$, whether prime or composite.

Suppose $D$ is a unitary or antiunitary normalizer and write its action as

$$
D W_N(v)D^{-1}=\chi(v)W_N(Cv).
$$

The quotient by the scalar center is the additive group $(\mathbb Z/N\mathbb Z)^2$. Its induced automorphism is additive and hence linear over $\mathbb Z/N\mathbb Z$, so $C$ is an invertible $2\times2$ matrix over that ring. Let $s=1$
for unitary $D$, and $s=-1$ for antiunitary $D$. Conjugating (2.2)
gives

$$
\omega(Cv,Cw)=s\omega(v,w).
$$

Taking the two basis vectors shows

$$
\det C=s\pmod N.
\tag{2.4}
$$

Now conjugate (2.1). Its central phase becomes

$$
e_N\bigl(-s h_2\omega(v,w)\bigr),
$$

which is exactly the phase from multiplying $W_N(Cv)$ and $W_N(Cw)$,
by (2.4). Therefore

$$
\chi(v+w)=\chi(v)\chi(w).
\tag{2.5}
$$

Thus the character assertion is a consequence of the exact multiplication
law; it is not an additional assumption on the normalizer. From

$$
D W_N(v)^N D^{-1}=I
$$

we get $\chi(v)^N=1$. This argument also applies if the normalizer is
initially described as preserving the Weyl operators only up to arbitrary
unit-modulus scalars: those scalars are forced to lie in $\mu_N$.

For completeness the bare cat is indeed such a normalizer. Put

$$
\phi(x,y)=-\overline8(3x^2-2xy+3y^2),\qquad
(M_N)_{xy}=N^{-1/2}e_N(\phi(x,y)).
$$

The row inner product is a geometric sum with frequency $\overline4(x-x')$, so $M_N$ is unitary. Symmetry of its kernel then gives

$$
\overline M_N=M_N^{-1}.
$$

In plus-shift $T_N(a,b)=W_N(b,a)$ coordinates, direct comparison of

$$
(M_NT_N(a,b))_{x,w}\quad\hbox{and}\quad
(T_N(A,B)M_N)_{x,w}
$$

gives the same relative phase when

$$
A=3a+4b,\qquad B=2a+3b.
$$

For the first product that phase is

$$
-\overline4 ax+(3\overline4a+b)w
-3\overline8a^2-\overline2ab.
$$

For the second it is

$$
(-3\overline4A+B)x+\overline4Aw
-3\overline8A^2+\overline2AB,
$$

which agrees after substitution. In particular there is no Egorov scalar
to lose when replacing $D$ by $M_ND$ later.

## 3. Independent coefficient reconstruction and all odd dimensions

Write $R_N(k)$ for the aliased Fourier coefficients of

$$
r(q)=(1-\cos14\pi q)(1+\cos2\pi q).
$$

Before aliasing their nonzero values are

$$
R(0)=1,\quad R(\pm1)=\tfrac12,\quad
R(\pm7)=-\tfrac12,\quad R(\pm6)=R(\pm8)=-\tfrac14.
\tag{3.1}
$$

These follow by expanding the two cosines and their product. Using $e^{i\alpha_0}=(-3+4i)/5$, the coefficients of the finite Hamiltonian obey the following complete
formulas, where all residues are modulo $N$:

$$
\begin{aligned}
4000c_N(k,0)
={}&2000\bigl(\mathbf1_{k=7}+\mathbf1_{k=-7}\bigr)
   +400R_N(k)-400\mathbf1_{k=0}\\
 &-20i\bigl(R_N(k-1)-R_N(k+1)\bigr),\\
4000c_N(k,1)&=(-12-16i)R_N(k),\\
4000c_N(k,-1)&=(-12+16i)R_N(k).
\end{aligned}
\tag{3.2}
$$

There are no other $p$-rows. Since $N\geq3$ is odd, the rows $0,1,-1$
are distinct. Formula (3.2) includes all small-dimension aliasing and proves
that every coefficient belongs to $\mathbb Q(i)$. Centering removes only
the coefficient at $(0,0)$, by (2.3).

For $N\geq11$, no frequency in the support $[-9,9]$ other than $1$
is congruent to $1$, nor can another frequency alias with $-1$.
Consequently

$$
4000c_N(1,0)=200-20i,\qquad
4000c_N(0,1)=-12-16i.
\tag{3.3}
$$

The pure-$q$ real parts before aliasing, on the same scale, are $200$
at $\pm1$, $1800$ at $\pm7$, and $-100$ at $\pm6,\pm8$.
For odd $N\geq11$, two real-bearing frequencies can merge only at $N=13$
or $15$, and the resulting nonzero merger is $1800-100=1700$.
This can be checked just by taking their pairwise differences; no prime
modulus hypothesis is involved. The real parts $200$ occur only at $(1,0)$ and $(-1,0)$, with opposite nonzero imaginary parts. No pure-$q$ real part equals $-200$. The original Fourier mass of $r$ is $4$, so every mixed-row real part
has absolute value at most $48$ on this scale. Hence mixed coefficients
cannot interfere with either the uniqueness of $c_N(1,0)$ and its
conjugate, or the absence of their negatives.

For the other basis coefficient, $R_N(0)=1$. At a nonzero residue there
is at most one positive summand $1/2$ from (3.1); any other contribution
is nonpositive. Thus $R_N(k)\leq1/2$ for $k\neq0$. This is a signed
bound and allows the actual negative mergers $-3/4$. It makes $c_N(0,1)$ unique in its own row. Equality with the opposite row would require a real
number to equal a nonreal phase ratio, since

$$
\frac{-12-16i}{-12+16i}
=e^{-2i\alpha_0}=\frac{-7+24i}{25}\notin\mathbb R.
$$

The pure-$q$ real parts are integer multiples of $100$ on the chosen
scale and cannot equal the mixed basis real part $-12$. The conjugate
coefficient is therefore unique at $(0,-1)$ as well.

The remaining nonexceptional odd dimensions are $3,5,9$. Substitution
in (3.2) gives the following complete pure-$q$ rows, on scale $4000$:

| $N$ | $c_N(k,0)$, $k=1,\ldots,N-1$, multiplied by $4000$ | $4000c_N(0,1)$ |
|---|---|---|
| 3 | $1900-15i,1900+15i$ | $-6-8i$ |
| 5 | $100-35i,1700-20i,1700+20i,100+35i$ | $-12-16i$ |
| 9 | $100-30i,1800-10i,-100+10i,5i,-5i,-100-10i,1800+10i,100+30i$ | $-12-16i$ |

Their $R_N$ rows, beginning with residue zero, are respectively

$$
\begin{aligned}
N=3:&\quad(1/2,-1/4,-1/4),\\
N=5:&\quad(1,1/4,-3/4,-3/4,1/4),\\
N=9:&\quad(1,1/4,-1/2,-1/4,0,0,-1/4,-1/2,1/4).
\end{aligned}
$$

These rows and (3.2) verify the same uniqueness conclusions. At $N=9$,
the only coefficients with real part $-100$ have imaginary parts $\pm10$, so neither negative of the basis coefficient $100-30i$, with or without
conjugation, occurs. This is the small-dimension sign check that a real-part
argument alone would not establish. At $N=3$, the scalar coefficient is $-200/4000=-1/20$, and is correctly removed before the centered symmetry argument.

At $N=7$, every grid value of $r$ is zero, while $\cos(14\pi x/7)=1$. The mixed rows vanish and $A_7=(9/10)I$. The exception is necessary.

We have therefore independently obtained, for all stated dimensions,

$$
\begin{array}{ll}
c_N(e_1)\text{ occurs only at }e_1,
 &\overline{c_N(e_1)}\text{ only at }-e_1,\\
-c_N(e_1),-\overline{c_N(e_1)}\text{ never occur},&\\
c_N(e_2)\text{ occurs only at }e_2,
 &\overline{c_N(e_2)}\text{ only at }-e_2.
\end{array}
\tag{3.4}
$$

## 4. The character is eliminated without a hidden phase assumption

The only roots of unity in $\mathbb Q(i)$ are $1,-1,i,-i$. One elementary
way to see this is to write a root as $a+ib$, with rational $a,b$.
Then $2a=\xi+\xi^{-1}$ is a rational algebraic integer, hence an integer
between $-2$ and $2$. The choices $a=\pm1/2$ give irrational $b=\pm\sqrt3/2$, and the other choices give the four listed roots. As $N$ is odd,

$$
\mathbb Q(i)\cap\mu_N=\{1\}.
\tag{4.1}
$$

Let $H_N=A_N-(\operatorname{Tr}A_N/N)I$ and suppose

$$
D H_ND^{-1}=\epsilon H_N,\qquad \epsilon\in\{1,-1\}.
$$

Coefficient comparison at $Cv$ gives

$$
\begin{array}{ll}
\chi(v)c_N(v)=\epsilon c_N(Cv),&D\text{ unitary},\\
\chi(v)\overline{c_N(v)}=\epsilon c_N(Cv),&D\text{ antiunitary}.
\end{array}
\tag{4.2}
$$

Both basis coefficients are nonzero. Their target coefficients must also
be nonzero by (4.2), and all these numbers are Gaussian rationals.
Therefore $\chi(e_j)\in\mathbb Q(i)\cap\mu_N$, hence

$$
\chi(e_1)=\chi(e_2)=1.
$$

Because these two indices generate the group, (2.5) gives $\chi\equiv1$.
There is no residual displacement character available to compensate a
coefficient mismatch.

If $D$ is unitary and $\epsilon=1$, (3.4) forces $Ce_j=e_j$, hence $C=I$. Then $D$ commutes with the whole Weyl basis and is scalar. If $D$ is
antiunitary and $\epsilon=1$, its coefficient conjugation instead forces

$$
Ce_j=-e_j\quad(j=1,2).
$$

Thus $C=-I$, whose determinant is $+1$, contradicting the antiunitary
determinant $-1$. These residues are distinct for every odd $N\geq3$.
Finally, for either type and $\epsilon=-1$, the equation at $e_1$ would
require one of the two forbidden negative coefficients in (3.4).

This proves the full four-case rigidity statement for $H_N$. In
particular the antiunitary contradiction uses conjugation of both basis
coefficients. It does not treat antiunitary conjugation as a complex-linear
operation on the expansion of $H_N$.

## 5. From a symmetry at the actual parameter to an identity in $z$

### 5.1. Why the candidate normalizer may be chosen algebraic

Fix its action $(C,\chi)$. The intertwining equations

$$
XW_N(v)=\chi(v)W_N(Cv)X
$$

are linear over the algebraic numbers. Given an invertible unitary
solution, any other solution differs from it by a scalar: their quotient
commutes with the Weyl basis. Thus the complex solution space has dimension
one and has a nonzero algebraic basis vector, obtained by Gaussian
elimination over the algebraic numbers. This vector is a scalar multiple
of the given invertible normalizer. Its positive normalization factor is
an algebraic square root, so an algebraic unitary representative exists.

For an antiunitary write $D=JK$, with $K$ coordinate conjugation. The
corresponding linear equations are

$$
J\overline{W_N(v)}=\chi(v)W_N(Cv)J.
$$

The same argument gives an algebraic unitary $J$. Multiplying a unitary
or antiunitary by a scalar does not change its conjugation of linear
operators. Thus no algebraicity restriction has been silently imposed on
the projective Weyl-normalizer class. This argument would fail for an
arbitrary matrix-dependent antiunitary, and no such extension is made.

### 5.2. Exponential-polynomial evaluation and projective minors

The only transcendence input is Lindemann–Weierstrass: exponentials of
distinct algebraic numbers are linearly independent over the algebraic
numbers. Its precise form was checked independently in Theorem 3.2 of
Sever Angel Popescu, *A simple and self-contained proof for the
Lindemann–Weierstrass theorem*, arXiv:2306.14352v2, printed pp. 14–15:
<https://arxiv.org/pdf/2306.14352>.

It gives the following elementary corollary. If

$$
p(z)=\sum_{j=1}^J a_j e^{\beta_jz},\qquad
a_j,\beta_j\in\overline{\mathbb Q},
$$

then $p(z_0)=0$ at a nonzero algebraic $z_0$ implies $p\equiv0$.
To prove this, first combine equal frequencies. Distinct $\beta_j$
remain distinct after multiplication by $z_0\neq0$, and the theorem
forces every combined coefficient to vanish.

Use the centered family

$$
\widetilde U(z)=e^{izNH_N}M_N.
$$

Centering changes the original family only by a scalar and therefore
preserves the existence of a projective relation. For an algebraic
representative $D$, put

$$
H_D=DH_ND^{-1},\qquad M_D=DM_ND^{-1},
\qquad F(z)=e^{is zNH_D}M_D,
$$

where $s=1$ in the unitary case and $s=-1$ in the antiunitary case.
For real $z$, $F(z)=D\widetilde U(z)D^{-1}$. For nonreal $z$, this
formula defines the holomorphic continuation. Literal antiunitary
conjugation would involve $\overline z$; it is not used off the real
axis. Antiunitary conjugation preserves product order, so $M_D$ remains
on the right.

The matrices $H_N,H_D$ have algebraic eigenvalues and algebraic spectral
projectors. For example, for distinct eigenvalues $\lambda_j$, a
projector is

$$
P_j=\prod_{k\neq j}\frac{H_N-\lambda_kI}{\lambda_j-\lambda_k}.
$$

Therefore every entry of $F(z)$, $\widetilde U(z)$, and

$$
\widetilde U(z)^{-1}=M_N^{-1}e^{-izNH_N}
$$

is an algebraic exponential polynomial. This remains true with repeated
eigenvalues, since the product is over distinct eigenvalues only.

Suppose at a nonzero real algebraic $z_0$ that

$$
F(z_0)=\eta\widetilde U(z_0)^r,
\qquad r\in\{1,-1\}.
$$

The scalar $\eta$ need not be algebraic. Eliminate it by every minor

$$
F_{ij}(z)(\widetilde U(z)^r)_{kl}
-F_{kl}(z)(\widetilde U(z)^r)_{ij}.
\tag{5.1}
$$

Each is an algebraic exponential polynomial vanishing at $z_0$, hence
identically zero. Because both matrices are invertible for all complex $z$, their flattened columns are nonzero and (5.1) implies proportionality at
every $z$. A global holomorphic proportionality factor is

$$
\eta(z)=\frac1N\operatorname{Tr}
 \bigl(F(z)\widetilde U(z)^{-r}\bigr).
$$

It is nowhere zero.

In fact this factor is constant. The centered matrices have zero trace,
so

$$
\det F(z)=\det M_D,\qquad
\det\widetilde U(z)=\det M_N.
$$

Thus

$$
\eta(z)^N=\frac{\det M_D}{(\det M_N)^r}
$$

is a nonzero constant. A holomorphic function on the connected plane with
values in this finite set is constant. This independently justifies the
vanishing scalar derivative used in the source.

### 5.3. The derivative signs and the original product

At zero,

$$
M_D=\eta(0)M_N^r.
$$

Taking right logarithmic derivatives at zero gives

$$
\begin{array}{ll}
isNH_D=iNH_N,&r=1,\\
isNH_D=-iNM_N^{-1}H_NM_N,&r=-1.
\end{array}
$$

The order in the inverse family is responsible for the conjugation by $M_N^{-1}$. Equivalently,

$$
\begin{array}{ll}
H_D=sH_N,&r=1,\\
(M_ND)H_N(M_ND)^{-1}=-sH_N,&r=-1.
\end{array}
\tag{5.2}
$$

By exact Egorov, $M_ND$ remains a Weyl normalizer with the same unitary or
antiunitary type. Applying Section 4 gives:

| Type of $D$ | Relation to $U_N(z_0)$ | Required Hamiltonian relation | Result |
|---|---|---|---|
| Unitary | Projective commute | $DH_ND^{-1}=H_N$ | $D$ scalar |
| Antiunitary | Projective commute | $DH_ND^{-1}=-H_N$ | Impossible |
| Unitary | Projective reverse | $(M_ND)H_N(M_ND)^{-1}=-H_N$ | Impossible |
| Antiunitary | Projective reverse | $(M_ND)H_N(M_ND)^{-1}=H_N$ | Impossible |

A scalar unitary commutes exactly, so its original projective factor is $\eta=1$. This proves the asserted actual-parameter statements, including $z_0=\tau=10^{-80}$. At $N=7$, $A_7=(9/10)I$, and coordinate conjugation obeys

$$
K U_7(z)K=e^{-iz7(9/10)}M_7^{-1}=U_7(z)^{-1}
$$

for real $z$. This checks the claimed exception directly.

## 6. Canonical CRT: exact phases and a single nonzero minor

Let $N=rs$, where $r,s>1$ are coprime odd integers. Identify coordinates
by $x\mapsto(x\bmod r,x\bmod s)$. Write $\bar s=s^{-1}\pmod r$
and $\bar r=r^{-1}\pmod s$. The exact character identity is

$$
e_N(u)=e_r(\bar s\,u_r)e_s(\bar r\,u_s).
$$

Reducing the shift and the modular half in the Weyl formula yields

$$
W_N(k,l)
=W_r(\bar s k,l)\otimes W_s(\bar r k,l).
\tag{6.1}
$$

Reduction of $2^{-1}\pmod N$ is $2^{-1}$ in either factor; it supplies
no sign or extra scalar. The map of Weyl indices in (6.1) is bijective,
since CRT is bijective and both displayed units are invertible.

The same calculation, together with $N^{-1/2}=r^{-1/2}s^{-1/2}$, gives

$$
M_N=M_r^{(\bar s)}\otimes M_s^{(\bar r)},
\quad
(M_d^{(c)})_{xy}=d^{-1/2}e_d[-c\overline8(3x^2-2xy+3y^2)].
\tag{6.2}
$$

Each factor is unitary: its row orthogonality uses the invertible frequency $c\overline4(x-x')$. The arithmetic units in (6.2) must be retained. The source does retain
them.

Here $N\geq15$. The Hamiltonian coefficient at $v=(1,0)$ has no alias
and equals

$$
c_N(1,0)=\frac1{20}-\frac{i}{200}\neq0.
\tag{6.3}
$$

Its tensor indices are

$$
a=(\bar s,0)\in(\mathbb Z/r\mathbb Z)^2,\qquad
b=(\bar r,0)\in(\mathbb Z/s\mathbb Z)^2.
$$

Both are nonzero. Because (6.1) is a bijection, this is an uncancelled
coefficient of $W_r(a)\otimes W_s(b)$. Thus $A_N$ cannot equal a
Kronecker sum $X\otimes I+I\otimes Y$, whose nonzero Weyl coefficients
always have at least one zero factor index.

There is a direct certificate that the kick fails to factor at every
nonzero algebraic parameter. Expand

$$
E(z)=e^{izNA_N}
=\sum_{u,v} e_{uv}(z) W_r(u)\otimes W_s(v).
$$

Every $e_{uv}(z)$ is an algebraic exponential polynomial, since

$$
e_{uv}(z)=\frac1N\operatorname{Tr}
 \bigl((W_r(u)^*\otimes W_s(v)^*)E(z)\bigr).
$$

Tensor-product structure is equivalent to rank one of the coefficient
matrix $(e_{uv}(z))$. This is the usual realignment criterion in a
different local operator basis; changing either local basis preserves its
rank.

Take the particular minor

$$
\Delta(z)=e_{00}(z)e_{ab}(z)-e_{a0}(z)e_{0b}(z).
\tag{6.4}
$$

At $z=0$, $E(0)=I\otimes I$, so $e_{00}(0)=1$ and every other
coefficient is zero. From $E'(0)=iNA_N$ we get

$$
\Delta'(0)=e_{ab}'(0)=iN c_N(1,0)\neq0.
\tag{6.5}
$$

Hence $\Delta$ is a nonzero algebraic exponential polynomial. The
evaluation lemma of Section 5 implies

$$
\Delta(z_0)\neq0
\quad\text{for every }z_0\in\overline{\mathbb Q}\setminus\{0\}.
$$

This one minor already proves that $E(z_0)$ is not a tensor product.
Using (6.2), a tensor product for $U_N(z_0)=E(z_0)M_N$ would imply one
for $E(z_0)=U_N(z_0)M_N^{-1}$, a contradiction.

The source's alternative tangent argument is also valid. If all realignment
minors vanished identically, then near zero its proposed factors

$$
X(z)=s^{-1}\operatorname{Tr}_{\mathbb C^s}E(z),\qquad
Y(z)=s\frac{\operatorname{Tr}_{\mathbb C^r}E(z)}{\operatorname{Tr}E(z)}
$$

are holomorphic, satisfy $X(0)=I_r$, $Y(0)=I_s$, and give

$$
X(z)\otimes Y(z)=E(z).
$$

To check the identity, write any rank-one tensor as $A\otimes B$.
The two displayed factors become $(\operatorname{Tr}B/s)A$ and $(s/\operatorname{Tr}B)B$, whenever $\operatorname{Tr}E\neq0$. This denominator is nonzero near
zero, where it equals $rs$. Differentiation would give the forbidden
Kronecker sum for $iNA_N$. Thus there is no unproved choice of analytic
tensor factors in the source either.

The result concerns each nontrivial coprime CRT partition separately. It
does not assert a nonexistent coprime split of a prime-power dimension,
and it does not concern an arbitrary globally chosen tensor identification.

## 7. The auxiliary reversal and block claims

### 7.1. Arbitrary diagonal phases in a common monomial reversal

Let $C=DPK$, with $D$ diagonal unitary and $(Pu)(x)=u(\pi(x))$.
Suppose $CM_NC^{-1}=\eta M_N^{-1}$. Since $\overline M_N=M_N^{-1}$, the entrywise equation is

$$
D_xD_y^{-1}\overline{M_{N,\pi(x)\pi(y)}}
=\eta\overline{M_{N,xy}}.
$$

Taking a four-entry cross ratio cancels the arbitrary phases and yields

$$
(\pi(x)-\pi(x'))(\pi(y)-\pi(y'))=(x-x')(y-y')\pmod N.
$$

Set $g(x)=\pi(x)-\pi(0)$ and $a=g(1)$. The cases $x=y=1$ and $y=1$ give $a^2=1$ and $ag(x)=x$, hence $\pi(x)=ax+b$. This does not
assume $N$ prime. In particular $a$ is a unit even in composite
dimensions.

On diagonal entries, the ratio of conjugate cat kernels is

$$
e_N(abx+\overline2b^2).
$$

Its independence of $x$ forces $ab=0$, hence $b=0$; then $\eta=1$. Since $a^2=1$, the full quadratic kernel is unchanged, and the remaining
entrywise equation makes $D$ scalar. Thus every such common candidate is $P_aK,\qquad a^2=1$, up to scalar.

For the stated nonexceptional dimensions $r(1/N)>0$, so a nonzero
nearest-neighbor edge exists. Its displacement is sent to $\pm a$, which
forces $a=\pm1$ if $A_N$ is preserved. The choice $a=1$ would
conjugate a nonreal hopping phase to itself. The choice $a=-1$ would
require the diagonal to be even, whereas

$$
V(-q)-V(q)=-\frac{r(q)\sin2\pi q}{50}
$$

is nonzero at $q=1/N$. These contradictions prove the common-factor
statement without any algebraicity assumption on the original diagonal
phases.

The source correctly distinguishes it from a statement about every
monomial reverser of the actual product. Its additional corollary for
actual-product monomial reversers with algebraic entries up to scalar is
also valid: the projective-minor argument first gives a bare-cat reverser
at zero, the classification just proved makes it $P_aK$, and this is a
Weyl normalizer. Section 5 then excludes it.

### 7.2. Classical affine common-factor statement

For the corrected plane symbol, the support polygon has vertices

$$
(9,0),(8,1),(-8,1),(-9,0),(-8,-1),(8,-1).
$$

Its two horizontal edges have lattice length $16$; all other edges have
lattice length $1$. An invertible integer linear map preserving it must
preserve the horizontal direction. The two long-edge centers exclude a
shear, leaving only diagonal sign changes. A positive $q$-sign permits
no nontrivial $q$-translation, by the nonzero frequency-one coefficient.
A negative $q$-sign would require the purely imaginary nonzero
coefficients at frequencies $2$ and $9$ to obey

$$
2u=1/2\pmod1,\qquad9u=1/2\pmod1.
$$

The first gives $u=1/4$ or $3/4$, and neither solves the second. Hence
the only nonidentity affine symmetry is

$$
J_\alpha(q,p)=(q,-p+\alpha_0/\pi).
$$

With $\delta=\alpha_0/\pi$ and

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
$$

direct multiplication gives

$$
J_\alpha L J_\alpha(z)=L^{-1}z+(-4\delta,-2\delta).
$$

The required torus translation is zero only if $2\delta\in\mathbb Z$,
which would give $e^{2i\alpha_0}=\pm1$. Its actual value is $(-7-24i)/25$. Thus this symmetry does not reverse the bare cat. This proves the claimed
common-factor assertion; it is not a classification of all full nonlinear
classical maps at isolated times.

### 7.3. Seven coordinate paths

When $N=7k$ is odd, exactly seven grid values of $r$ vanish. The second
factor $1+\cos2\pi q$ has no zeros on an odd grid, so there are no
additional ones. The modular midpoint permutes the grid, giving exactly
seven zero hopping edges separated by $k$ sites. The coordinate graph
therefore has seven paths of $k$ vertices, including singleton paths
when $N=7$.

Their projections $P_j$ commute with $A_N$ and $E(z)$, while cat
flatness gives

$$
(M_NP_jM_N^{-1})_{xx}=k/N=1/7
$$

for every $x$. No coordinate path projection has that diagonal. Thus

$$
M_NP_jM_N^{-1}\neq P_l
$$

for all $j,l$. If $U_N(z)P_jU_N(z)^{-1}=P_l$, commutation of $E(z)$
with $P_l$ would imply that very equality for $M_N$, a contradiction.
This is exact for all $z$ and excludes permutation of these particular
coordinate blocks.

## 8. Verification record and remaining quantitative barrier

The source's exact Gaussian-integer checker was rerun successfully, and
its freshly generated result agrees exactly with the saved JSON. It
checks 48 odd dimensions $3\leq N\leq99$, $N\neq7$, and 5600
candidate Weyl-index maps. The checker source hash is

`ded7875ca635745da21bbaef9d523cc24c2d57a3985965f84b82caee1a51626e`.

This computation is a consistency check. The universal conclusion follows
from Sections 2–6, including the independent closed coefficient formula
(3.2), the explicit small-dimension analysis, and the field argument.

The exact nonvanishing of the minor (6.4), or the impossibility of the
projective minors (5.1) all vanishing, supplies no uniform lower bound on
their absolute values as $N$ grows. Lindemann–Weierstrass is used only as
an injectivity statement at nonzero algebraic parameters. In particular,
these results give no estimate of the scale needed to exclude approximate
tensor structure, near symmetries, near eigenvalue clusters, or correlated
orbit phases at times comparable with $N$.

For an arbitrary unitary $U=V\operatorname{diag}(e^{i\theta_j})V^*$,
the antiunitary $VKV^*$ always satisfies

$$
(VKV^*)U(VKV^*)^{-1}=U^{-1}.
$$

Its matrix entries generally have no reason to be algebraic or to
normalize the specified Weyl group. The audit therefore closes precisely
the geometric and canonical CRT mechanisms claimed in the source. The
signed off-diagonal sum and Hdiag remain open.
