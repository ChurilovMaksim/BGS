> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/affine_reversal_and_crt_obstructions.md`. Embedded SHA256: `856f7e0d7373e1b3c260b20477969a12e3e78886836b11fd4eac9ddd9cc7642c`.
> [Thematic guide](../../topics/symmetry.md).

# Exact obstructions to geometric reversal and CRT factorization

Date: 20 October 2026.

Base proof packet: odd_trace_and_algebraic_rigidity.md, SHA-256
42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b.

## 1. Results and scope

For the original matrix family
$$
 U_N(z)=e^{izNA_N}M_N,\qquad z=\tau=10^{-80},
$$
the following statements are proved below.

**Theorem A: absence of Weyl-normalizing reversal.** For every odd $N\geq3$, $N\neq7$, and every nonzero real algebraic $z$, no antiunitary normalizer of the finite Weyl group satisfies
$$
 C U_N(z)C^{-1}=\eta U_N(z)^{-1}
$$
for any scalar $\eta$. Thus there is no time-reversal operator in the extended Clifford group for these dimensions, even projectively.

In the same group, there is no unitary projective reverser, no antiunitary projective commuter, and the only unitary projective commuters are scalar operators. These stronger conclusions follow from the same coefficient argument.

**Theorem B: the real Jacobi gauge supplies no common reversal.** For every odd $N\geq3$, $N\neq7$, there is no monomial antiunitary, even with arbitrary diagonal phases, that both preserves $A_N$ and reverses $M_N$. This specifically rules out obtaining a common reversal of the kick and cat factors from the one-path or seven-path real gauge.

**Theorem C: no exact canonical CRT tensor factorization.** If $N=rs$, with coprime odd integers $r,s>1$, then $U_N(z)$ is not a tensor product under the canonical CRT identification $\mathbb C^N=\mathbb C^r\otimes\mathbb C^s$, for any nonzero algebraic $z$. The bare matrix $M_N$ does factor under this identification; the kick does not.

When $7\mid N$, the seven coordinate path projections of $A_N$ are not even permuted by $U_N(z)$. This removes the direct block-permutation mechanism associated with the zeros of $r$.

The exception $N=7$ is necessary: $A_7=(9/10)I$, and ordinary coordinate conjugation is a geometric antiunitary reverser of $U_7(z)$ for real $z$.

These theorems concern specified geometric or tensor-product structures. Every finite unitary matrix has an abstract antiunitary reverser obtained by conjugating coordinate conjugation from an eigenbasis. Theorem A does not deny that fact. Nor do these absence results prove simple spectrum, CUE statistics, or Hdiag.

## 2. Exact objects

For odd $N$, let
$$
 e_N(x)=e^{2\pi ix/N},\qquad
 (T_N(a,b)u)(x)=e_N[b(x+\overline2a)]u(x+a),
$$
with all indices interpreted modulo $N$. Write the frequency-indexed Weyl basis as
$$
 W_N(k,l)=T_N(l,k).
$$
The plus shift is intentional. The finite cat matrix is
$$
 (M_N)_{xy}=N^{-1/2}e_N[-\overline8(3x^2-2xy+3y^2)].
 \tag{2.1}
$$
It is symmetric and unitary, so
$$
 \overline M_N=M_N^{-1}.
 \tag{2.2}
$$
Its exact Egorov action is
$$
 M_NT_N(a,b)M_N^{-1}=T_N(3a+4b,2a+3b).
 \tag{2.3}
$$

Set
$$
 r(q)=(1-\cos14\pi q)(1+\cos2\pi q),
 \qquad e^{i\alpha_0}=(-3+4i)/5,
$$
and
$$
 f(q,p)=\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}
 +\frac{r(q)\cos(2\pi p-\alpha_0)}{100}.
$$
If
$$
 f-\frac1{10}=\sum_{k,l}c_{kl}e^{2\pi i(kq+lp)},
$$
then
$$
 A_N=\sum_{k,l}c_{kl}W_N(k,l).
 \tag{2.4}
$$
The sum is finite. All its coefficients lie in $\mathbb Q(i)$.

After aliasing modulo $N$, let $c_N(v)$ be its Weyl coefficients. Remove its scalar part:
$$
 H_N=A_N-\frac{\operatorname{Tr}A_N}{N}I.
 \tag{2.5}
$$
For $v\neq0$, the coefficient of $H_N$ is still $c_N(v)$; its zero coefficient is zero. This centering matters at $N=3$, where $\operatorname{Tr}A_3/3=-1/20$.

The exact coordinate form of $A_N$ has diagonal
$$
 V(x/N)=\cos(14\pi x/N)+\frac{r(x/N)}{10}
 +\frac{r(x/N)\sin(2\pi x/N)}{100}-\frac1{10}
$$
and upper nearest-neighbor coefficient
$$
 (A_N)_{x,x+1}
 =\frac{e^{-i\alpha_0}}{200}\,
 r\!\left(\frac{x+\overline2}{N}\right).
 \tag{2.6}
$$
The opposite coefficient is its Hermitian conjugate. The argument in (2.6) is a modular grid point.

## 3. Two identifiable Fourier coefficients

The following elementary lemma is the main rigidity input. It includes all aliasing in small odd dimensions.

**Lemma 3.1.** For every odd $N\geq3$, $N\neq7$, put
$$
 e_1=(1,0),\qquad e_2=(0,1).
$$
Both $c_N(e_1)$ and $c_N(e_2)$ are nonzero. Among the nonzero-frequency coefficients of $H_N$:

1. $c_N(e_1)$ occurs only at $e_1$, and its conjugate occurs only at $-e_1$.
2. Neither $-c_N(e_1)$ nor $-\overline{c_N(e_1)}$ occurs.
3. $c_N(e_2)$ occurs only at $e_2$, and its conjugate occurs only at $-e_2$.

### 3.1. Uniform proof for $N\geq11$

The Fourier coefficients of $r$ are
$$
 \widehat r(0)=1,\quad
 \widehat r(\pm1)=\frac12,\quad
 \widehat r(\pm7)=-\frac12,\quad
 \widehat r(\pm6)=\widehat r(\pm8)=-\frac14.
 \tag{3.1}
$$
All omitted coefficients vanish. In particular,
$$
 4000c_N(e_1)=200-20i,\qquad
 4000c_N(e_2)=-12-16i
 \tag{3.2}
$$
for $N\geq11$. The $e_1$ coefficient has no alias because the largest $q$-frequency of the full symbol is $9$.

Before aliasing, the real parts of the pure-$q$ coefficients, multiplied by $4000$, are:
$$
 200\text{ at }k=\pm1,\qquad
 1800\text{ at }k=\pm7,\qquad
 -100\text{ at }k=\pm6,\pm8.
 \tag{3.3}
$$
All other real parts vanish. For odd $N\geq11$, the only aliases between two of the nonzero real coefficients in the set $\{\pm6,\pm7,\pm8\}$ occur at $N=13$ or $15$. They merge $1800$ with $-100$, producing $1700$. No alias touches $k=\pm1$. Hence the only pure-$q$ coefficients with real part $200/4000$ are the two at $\pm e_1$; their imaginary parts are respectively $-20/4000$ and $20/4000$. There is no pure-$q$ coefficient with real part $-200/4000$.

The mixed coefficients, after aliasing in $q$, are
$$
 4000c_N(k,1)=(-12-16i)\widehat r_N(k),\qquad
 4000c_N(k,-1)=(-12+16i)\widehat r_N(k),
 \tag{3.4}
$$
where $\widehat r_N(k)$ is the real aliased coefficient from (3.1). Its absolute value is at most the original Fourier mass $4$. Thus every mixed coefficient has real part of modulus at most $48/4000$, and cannot interfere with the $e_1$ uniqueness or negative-coefficient statements.

For $N\geq11$, $\widehat r_N(0)=1$. At a nonzero residue there is at most one positive coefficient $1/2$ from (3.1), with every other possible contribution nonpositive. Therefore
$$
 \widehat r_N(k)\leq\frac12\quad(k\neq0).
 \tag{3.5}
$$
This is a signed upper bound; at $N=13,15$ some coefficients are $-3/4$. Equation (3.5) makes the $e_2$ coefficient unique in its own $p$-row. It cannot equal a coefficient in the opposite row: that would require a real number to equal
$$
 e^{-2i\alpha_0}=\frac{-7+24i}{25},
$$
which is nonreal. It cannot equal a pure-$q$ coefficient either, since their real parts are integer multiples of $100/4000$, whereas its real part is $-12/4000$. Conjugation gives uniqueness at $-e_2$. This proves the lemma for $N\geq11$.

### 3.2. The three remaining dimensions

All entries in the next table are multiplied by $4000$. Only nonzero pure-$q$ frequencies are listed; centering removes the scalar coefficient.

| $N$ | Pure-$q$ coefficients in the order $k=1,\ldots,N-1$ | $4000c_N(e_2)$ |
|---|---|---|
| 3 | $1900-15i,\ 1900+15i$ | $-6-8i$ |
| 5 | $100-35i,\ 1700-20i,\ 1700+20i,\ 100+35i$ | $-12-16i$ |
| 9 | $100-30i,\ 1800-10i,\ -100+10i,\ 5i,\ -5i,\ -100-10i,\ 1800+10i,\ 100+30i$ | $-12-16i$ |

These are finite additions using (3.1). The corresponding aliased $r$-coefficients, in residue order starting at zero, are
$$
 \begin{array}{c|l}
 3 &(1/2,-1/4,-1/4),\\
 5 &(1,1/4,-3/4,-3/4,1/4),\\
 9 &(1,1/4,-1/2,-1/4,0,0,-1/4,-1/2,1/4).
 \end{array}
 \tag{3.6}
$$
Equation (3.4) then gives all mixed coefficients. Their real parts have modulus at most $48/4000$, below the real part of the $e_1$ coefficient in each case. In the $N=9$ row, the pure-$q$ coefficients with real part $-100/4000$ have imaginary parts $\pm10/4000$, not the $\pm30/4000$ required for either forbidden negative. Uniqueness of $c_N(e_2)$ follows from the explicit $r$-rows and the nonreal ratio between the two mixed phases. This completes the proof of Lemma 3.1.

At $N=7$, every value of $r$ on the grid vanishes and $A_7=(9/10)I$; the lemma intentionally excludes this case.

## 4. Complete rigidity inside the extended Clifford group

A unitary or antiunitary Weyl normalizer $D$ acts on the Weyl basis by
$$
 D W_N(v)D^{-1}=\chi(v)W_N(Cv).
 \tag{4.1}
$$
Here $C$ is a linear automorphism of $(\mathbb Z/N\mathbb Z)^2$. For a unitary normalizer, $\det C=1$; for an antiunitary normalizer, $\det C=-1$. The scalar $\chi$ is a character with values in the $N$-th roots of unity.

These facts follow from the Weyl multiplication law. The quotient of the Weyl group by its center is the additive group $(\mathbb Z/N\mathbb Z)^2$, so its automorphism is linear. Preservation, or complex conjugation, of the central commutator gives the determinant sign. The exact modular half in the Weyl product then makes the remaining scalar a character. Also $W_N(v)^N=I$, so $\chi(v)^N=1$.

The elementary field fact needed below is
$$
 \mathbb Q(i)\cap\mu_N=\{1\}\quad\text{for odd }N.
 \tag{4.2}
$$
For an elementary proof, write such a root of unity as $\xi=a+ib$, with rational $a,b$. Then $\xi+\xi^{-1}=2a$ is a rational algebraic integer, hence an integer. This can be seen without a field-integrality theorem: the recurrence $P_0=2$, $P_1=X$, $P_j=XP_{j-1}-P_{j-2}$ gives a monic integer polynomial $P_N(X)-2$ vanishing at $X=2a$. A rational root of a monic integer polynomial is an integer. Thus $a$ is one of $-1,-1/2,0,1/2,1$. The choices $a=\pm1/2$ would give irrational $b=\pm\sqrt3/2$; the others give precisely $1,-1,i,-i$. Odd order leaves only $1$.

**Theorem 4.1.** For every odd $N\geq3$, $N\neq7$:

* a unitary Weyl normalizer preserving $H_N$ is scalar;
* no unitary Weyl normalizer sends $H_N$ to $-H_N$;
* no antiunitary Weyl normalizer sends $H_N$ to either $H_N$ or $-H_N$.

**Proof.** Suppose $D H_ND^{-1}=\epsilon H_N$, where $\epsilon\in\{1,-1\}$. Comparing the coefficient at $Cv$ in (4.1) gives
$$
 \chi(v)c_N(v)=\epsilon c_N(Cv)
 \tag{4.3}
$$
for a unitary $D$, and
$$
 \chi(v)\overline{c_N(v)}=\epsilon c_N(Cv)
 \tag{4.4}
$$
for an antiunitary $D$.

At each of $v=e_1,e_2$, the coefficient is nonzero by Lemma 3.1, and the target coefficient must also be nonzero. All these coefficients lie in $\mathbb Q(i)$, so (4.3) or (4.4) makes $\chi(e_1),\chi(e_2)$ elements of $\mathbb Q(i)$. By (4.2), both equal $1$. Since $e_1,e_2$ generate the index group, $\chi\equiv1$.

For unitary $D$ and $\epsilon=1$, the two uniqueness statements force $Ce_j=e_j$ for $j=1,2$. Thus $C=I$, and $D$ commutes with every Weyl matrix. They span the entire matrix algebra, so $D$ is scalar.

For antiunitary $D$ and $\epsilon=1$, uniqueness of the conjugate coefficients forces $Ce_j=-e_j$ for both basis indices. Thus $C=-I$, which has determinant $1$, contrary to the required determinant $-1$. Since $N$ is odd and at least $3$, these determinants are distinct modulo $N$.

For $\epsilon=-1$, either (4.3) or (4.4) would require a coefficient equal to $-c_N(e_1)$ or $-\overline{c_N(e_1)}$. Both are absent by Lemma 3.1. This excludes both types of normalizer. $\square$

This proof is uniform in odd $N$, including arbitrary composite dimensions. It does not infer a universal result from a finite normalizer search.

## 5. Transfer to the actual kicked matrix at the algebraic parameter

The parameter dependence in this section is essential. A matrix-dependent abstract antiunitary need not have algebraic entries and is not covered by the argument.

### 5.1. Algebraic representatives

Every Weyl-normalizer conjugation has a representative with algebraic matrix entries, up to an irrelevant scalar. For a unitary representative, the intertwining equations
$$
 D W_N(v)=\chi(v)W_N(Cv)D
$$
are linear equations over algebraic numbers. Their nonzero solution space is one-dimensional by irreducibility of the Weyl representation, and a basis solution can be chosen algebraic. It is a scalar multiple of the given invertible representative and can be normalized using an algebraic positive square root.

For an antiunitary representative, write $D=J K$, where $K$ is coordinate conjugation, and apply the same argument to the linear intertwining equations for $J$. The matrices $W_N(v)$, their conjugates, and the characters $\chi(v)$ have algebraic entries. Thus $J$ can again be chosen algebraic.

### 5.2. Eliminate the unknown projective scalar before using transcendence

Work with the centered family
$$
 \widetilde U(z)=e^{izNH_N}M_N.
$$
It differs from $U_N(z)$ only by a scalar, so projective symmetry questions are unchanged.

Let $D$ be a unitary or antiunitary Weyl normalizer, and put
$$
 s=\begin{cases}1,&D\text{ unitary},\\-1,&D\text{ antiunitary},\end{cases}
 \quad H_D=DH_ND^{-1},\quad M_D=DM_ND^{-1}.
$$
Define the holomorphic matrix family
$$
 F(z)=e^{is zN H_D}M_D.
 \tag{5.1}
$$
For real $z$, (5.1) is exactly $D\widetilde U(z)D^{-1}$. For nonreal $z$, it is the specified analytic continuation, not a literal conjugation by an antiunitary.

Every entry of $F(z)$, $\widetilde U(z)$, and $\widetilde U(z)^{-1}$ is a finite exponential polynomial with algebraic coefficients and algebraic frequencies. This follows by using the algebraic spectral projectors of the Hermitian algebraic matrices $H_N,H_D$.

Suppose, at a nonzero real algebraic $z_0$,
$$
 F(z_0)=\eta\,\widetilde U(z_0)^r,\qquad r\in\{1,-1\},
 \tag{5.2}
$$
with unknown scalar $\eta$. Eliminate $\eta$ by taking every $2\times2$ minor of the two flattened matrix columns $F(z)$ and $\widetilde U(z)^r$. These minors are finite algebraic exponential polynomials and vanish at $z_0$.

Lindemann–Weierstrass implies that each such polynomial vanishes identically: after equal frequencies are combined, evaluation at any nonzero algebraic number is injective. Thus the matrices are proportional for every complex $z$:
$$
 F(z)=\eta(z)\widetilde U(z)^r.
 \tag{5.3}
$$
Both matrices are invertible. The scalar $\eta(z)$, obtained for example by tracing their quotient and dividing by $N$, is holomorphic and nonzero.

The exact external theorem used is Lindemann–Weierstrass in the form stated in Theorem 3.2 of Sever Angel Popescu, *A simple and self-contained proof for the Lindemann–Weierstrass theorem*, arXiv:2306.14352v2, 17 September 2023, https://arxiv.org/pdf/2306.14352 . The exact statement was independently checked in the base audit.

### 5.3. Differentiate the projective identity

At $z=0$, equation (5.3) gives $M_D=\eta(0)M_N^r$. Right-multiplying the derivative by the inverse of the value at zero gives, when $r=1$,
$$
 isNH_D=\frac{\eta'(0)}{\eta(0)}I+iNH_N.
$$
When $r=-1$, it gives
$$
 isNH_D=\frac{\eta'(0)}{\eta(0)}I
             -iNM_N^{-1}H_NM_N.
$$
Taking traces kills the scalar term, since both Hamiltonians are centered. Therefore:
$$
 \begin{array}{c|c}
 r=1 & H_D=sH_N,\\
 r=-1 & (M_ND)H_N(M_ND)^{-1}=-sH_N.
 \end{array}
 \tag{5.4}
$$
The product $M_ND$ is still a Weyl normalizer by exact Egorov, and has the same unitary or antiunitary type as $D$.

Apply Theorem 4.1 to (5.4):

| Type of $D$ | Proposed projective relation | Consequence |
|---|---|---|
| Unitary | $DUD^{-1}=\eta U$ | $D$ is scalar, and $\eta=1$ |
| Antiunitary | $DUD^{-1}=\eta U$ | Impossible |
| Unitary | $DUD^{-1}=\eta U^{-1}$ | Impossible |
| Antiunitary | $DUD^{-1}=\eta U^{-1}$ | Impossible |

This proves Theorem A for every odd $N\geq3$, $N\neq7$, at every nonzero real algebraic $z$, including the original $\tau=10^{-80}$.

At $N=7$, $A_7=(9/10)I$ and $K M_7 K=M_7^{-1}$. For real $z$, coordinate conjugation also conjugates the scalar kick to its inverse, so
$$
 K U_7(z)K=U_7(z)^{-1}.
$$
The excluded dimension really has a Weyl-normalizing reverser.

## 6. Why the real Jacobi gauge does not reverse the split dynamics

The real gauge of a Hermitian path matrix provides an antiunitary preserving that one matrix. A common reversal of the cat and kick factors is a stronger condition.

### 6.1. Classify all monomial antiunitary reversers of the bare cat

Let
$$
 C=DPK,
$$
where $D$ is any diagonal unitary matrix, $K$ is coordinate conjugation, and $P$ is a permutation matrix with $(Pu)(x)=u(\pi(x))$. Suppose
$$
 C M_NC^{-1}=\eta M_N^{-1}.
 \tag{6.1}
$$
No algebraicity assumption on the entries of $D$ is needed here.

By (2.2), equation (6.1) is
$$
 D_xD_y^{-1}\overline{M_{N,\pi(x)\pi(y)}}
 =\eta\,\overline{M_{N,xy}}.
$$
Take a four-entry cross ratio to cancel $D$ and $\eta$. The quadratic kernel gives
$$
 (\pi(x)-\pi(x'))(\pi(y)-\pi(y'))
 \equiv(x-x')(y-y')\pmod N.
 \tag{6.2}
$$
Set $x'=y'=0$ and $g(x)=\pi(x)-\pi(0)$. With $a=g(1)$, equation (6.2) implies $a^2=1$ and $ag(x)=x$, hence
$$
 \pi(x)=ax+b,\qquad a^2=1\pmod N.
 \tag{6.3}
$$
In particular $a$ is a unit, including when $N$ is composite.

On diagonal entries the permutation changes the conjugate kernel by the factor
$$
 e_N\!\left(abx+\overline2b^2\right).
$$
It must be independent of $x$, so $ab=0$, hence $b=0$. The same diagonal entries then give $\eta=1$. Since $a^2=1$, the entire quadratic kernel is unchanged by $x,y\mapsto ax,ay$, so the remaining equation forces $D_x/D_y=1$ for every pair. Thus $D$ is scalar.

Consequently every monomial projective antiunitary reverser of $M_N$ has, up to scalar, the form
$$
 C=P_aK,\qquad (P_au)(x)=u(ax),\qquad a^2=1\pmod N.
 \tag{6.4}
$$

### 6.2. None of these preserves the Hamiltonian outside $N=7$

For odd $N\geq3$, $N\neq7$, at least one nearest-neighbor coefficient in (2.6) is nonzero. For instance,
$$
 r(1/N)>0:
$$
the first factor could vanish only if $N\mid7$, and the second factor is positive on an odd grid. Since the modular midpoint is a bijective function of the edge index, some edge has this positive value.

Under $P_aK$, a nonzero nearest-neighbor entry has displacement $\pm a$. To preserve the nearest-neighbor support, $a$ must be $1$ or $-1$ modulo $N$.

If $a=1$, preservation would require the nonzero hopping coefficient $e^{-i\alpha_0}$ to equal its conjugate, which is false.

If $a=-1$, preservation would require $V(-x/N)=V(x/N)$. But
$$
 V(-q)-V(q)=-\frac{r(q)\sin2\pi q}{50},
$$
which is nonzero at $q=1/N$ for the stated dimensions. This excludes $a=-1$.

Thus no monomial antiunitary simultaneously preserves $A_N$ and reverses $M_N$, proving Theorem B.

This theorem is strictly about a common symmetry of the two factors. On its own it does not exclude an arbitrary monomial antiunitary reversing only $U_N(\tau)$, with diagonal entries chosen transcendently from that particular matrix. Theorem A concerns the actual product and is stronger within the Weyl-normalizer class because algebraic representatives make the parameter argument available.

There is a further precise corollary: an actual-product monomial antiunitary reverser whose entries are algebraic up to a scalar is also impossible. In that case the projective-minor argument of Section 5 applies before imposing a normalizer assumption. At zero parameter it gives a projective reverser of $M_N$, so Section 6.1 forces it to be $P_aK$, up to scalar. This operator is a Weyl normalizer because $a^2=1$, and Theorem A then applies. The algebraicity condition in this corollary cannot be discarded by the parameter argument.

### 6.3. The classical affine common-factor check

The corrected plane symbol is
$$
 a(q,p)=V(q)+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
$$
Its exact affine symmetry group on the torus contains only the identity and
$$
 J_\alpha(q,p)=(q,-p+\alpha_0/\pi).
 \tag{6.5}
$$
Here is a direct coefficient proof of the scope of this assertion.

The Newton polygon of the Fourier support has vertices
$$
 (9,0),(8,1),(-8,1),(-9,0),(-8,-1),(8,-1).
$$
The two long edges have lattice length $16$, whereas the other four have lattice length $1$. An integer linear map preserving the polygon must preserve its long-edge direction, and their centers then exclude a shear. Its linear part on Fourier indices is therefore diagonal with signs $\pm1$. The same holds for its coordinate linear part.

The pure-$q$ coefficient at frequency $1$ excludes a nontrivial translation of $q$. A reflection $q\mapsto-q+u$ would have to preserve the purely imaginary nonzero coefficients at frequencies $2$ and $9$. It would require both
$$
 2u\equiv1/2\pmod1,\qquad9u\equiv1/2\pmod1,
$$
which is impossible: the first gives $u=1/4$ or $3/4$, neither satisfying the second. Thus $q$ is fixed. The single cosine in $p$ then gives exactly the identity and (6.5).

The linear momentum flip $J_0=\operatorname{diag}(1,-1)$ reverses
$$
 L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
$$
However, with $\delta=\alpha_0/\pi$, the affine map (6.5) gives
$$
 J_\alpha L J_\alpha(z)
 =L^{-1}z+(-4\delta,-2\delta).
$$
To reverse $L$ on the torus would require $2\delta\in\mathbb Z$, and hence $e^{2i\alpha_0}=\pm1$. In fact
$$
 e^{2i\alpha_0}=(-7-24i)/25,
$$
so the condition fails.

Accordingly there is no affine antisymplectic involution that both preserves this Hamiltonian and reverses the cat factor. This is a common-factor statement. It does not classify every conceivable affine symmetry of the full classical nonlinear map at one isolated time. The exact quantum product statement is instead Theorem A.

## 7. CRT does not factor the perturbed matrix

Let $N=rs$, where $r,s>1$ are coprime odd integers. Under the canonical CRT coordinate permutation,
$$
 |x\bmod N\rangle\longleftrightarrow
 |x\bmod r\rangle\otimes|x\bmod s\rangle,
$$
one has
$$
 W_N(k,l)
 =W_r(\overline s\,k,l)\otimes W_s(\overline r\,k,l).
 \tag{7.1}
$$
The inverses $\overline s,\overline r$ in (7.1) are taken in their respective moduli. The identity follows from
$$
 e_N(u)=e_r(\overline s\,u_r)e_s(\overline r\,u_s)
$$
and the modular-half Weyl definition.

The same calculation factors the bare quadratic kernel:
$$
 M_N=M_r^{(\overline s)}\otimes M_s^{(\overline r)},
 \tag{7.2}
$$
where
$$
 (M_d^{(c)})_{xy}
 =d^{-1/2}e_d[-c\,\overline8(3x^2-2xy+3y^2)].
$$
The factors are unitary because $c$ is a unit. Equation (7.2) does not identify either factor with the original $M_d$ without its displayed arithmetic unit.

Because $r,s>1$ are coprime and odd, $N\geq15$. The frequency $(k,l)=(1,0)$ therefore has no alias from another original frequency, and
$$
 c_N(1,0)=\frac1{20}-\frac{i}{200}\neq0.
 \tag{7.3}
$$
By (7.1), the corresponding Weyl tensor is nonidentity in both factors. The map from finite $N$-indices to pairs of CRT Weyl indices is bijective, so no other finite coefficient can cancel it. It follows that
$$
 A_N\neq X\otimes I+I\otimes Y
 \tag{7.4}
$$
for all matrices $X,Y$ of the factor dimensions.

Suppose that the kick
$$
 E(z)=e^{izNA_N}
$$
were a tensor product at some nonzero algebraic $z_0$. Tensor rank one in
$$
 \operatorname{End}(\mathbb C^r)\otimes
 \operatorname{End}(\mathbb C^s)
$$
is characterized by all $2\times2$ minors of the corresponding realigned matrix vanishing. These minors of $E(z)$ are algebraic exponential polynomials. Lindemann–Weierstrass therefore makes them vanish for every $z$.

Since $E(0)=I\otimes I$, its factors can be chosen holomorphically near zero, with $X(0)=I$, $Y(0)=I$. For example, if $E$ has tensor rank one, use
$$
 X(z)=s^{-1}\operatorname{Tr}_{\mathbb C^s}E(z),\qquad
 Y(z)=s\,\frac{\operatorname{Tr}_{\mathbb C^r}E(z)}
                     {\operatorname{Tr}E(z)} .
$$
Their product is $E(z)$, and their denominators do not vanish near zero. Differentiating yields
$$
 iNA_N=X'(0)\otimes I+I\otimes Y'(0),
$$
contradicting (7.4).

Thus $E(z_0)$ is not a tensor product. Multiplication by the inverse of the product in (7.2) preserves tensor-product structure, so $U_N(z_0)=E(z_0)M_N$ cannot be a tensor product either. This proves Theorem C.

The theorem includes a split $N=7k$ whenever $(7,k)=1$ and $k>1$. For a pure prime power such as $7^a$, there is no coprime CRT split into two nontrivial factors, and no such split is asserted. For more general $N$, the theorem applies to each nontrivial coprime CRT partition separately.

## 8. The seven Jacobi blocks are mixed by the cat step

Suppose $N=7k$ is odd. The $N$-point grid has exactly seven zeros of $r$. The modular midpoint in (2.6) permutes that grid, so the cyclic nearest-neighbor graph has seven zero edges, equally spaced. It decomposes into seven coordinate paths, each with $k$ vertices.

Let $P_j$ be their coordinate projections. They commute with $A_N$, and hence with $E(z)$. But flatness of the cat kernel gives
$$
 (M_NP_jM_N^{-1})_{xx}
 =\sum_{y\text{ in block }j}|M_{N,xy}|^2
 =\frac{k}{N}=\frac17
$$
for every $x$. No coordinate projection $P_l$ has that diagonal: its entries are zero or one. Hence $M_N$ does not permute the path projections.

If $U_N(z)$ permuted them, say
$$
 U_N(z)P_jU_N(z)^{-1}=P_l,
$$
commutation of $E(z)$ with $P_l$ would imply
$$
 M_NP_jM_N^{-1}=P_l,
$$
which has just been excluded. Thus neither the cat factor nor the full product permutes these seven coordinate blocks.

This argument excludes these specific block projections and their direct permutation mechanism. It does not claim that a finite matrix has no reducing subspaces in an eigenbasis.

## 9. Verification, provenance, and branch disposition

The uniform proof uses exact finite coefficient identities, the Weyl group relations, and the stated Lindemann–Weierstrass theorem. It uses no statistical experiment or floating-point threshold.

The exact verification script verify_affine_symmetry.py reconstructs the Fourier polynomial in Gaussian integers after multiplying by $4000$, reduces all frequencies modulo each odd $N$ between $3$ and $99$ except $7$, and checks Lemma 3.1. It also enumerates every possible pair of images of the two basis Weyl indices, filters for determinant $1$ or $-1$, and checks both signs of the centered Hamiltonian symmetry with trivial character. The character restriction is proved in Section 4, not inferred by the script.

The enumerator is exhaustive in the stated finite range: a symmetry must map each of the two nonzero basis coefficients to a nonzero support coefficient, so its two columns occur among the enumerated support pairs. It checks 48 dimensions and 5600 candidate linear maps. The only surviving positive unitary action is the identity; no other sign/type survives. The uniform theorem comes from Sections 3–5, not from extrapolating this finite range.

The coordinator independently recomputed the small coefficient tables and checked the coefficient uniqueness argument, including the signed nature of (3.5), the exceptional mean at $N=3$, and the analytic continuation convention in (5.1). A separate end-to-end review of this final file has not been claimed.

| Research route | Exact result | Disposition |
|---|---|---|
| Extended-Clifford antiunitary reversal of the actual $U_N(\tau)$ | Impossible for every odd $N\geq3,\ N\neq7$, even projectively | This mechanism excluded |
| Common monomial reversal of $A_N,M_N$ | Impossible for the same dimensions, with arbitrary diagonal phases | The real Jacobi gauge does not supply it |
| Common affine classical reversal of $a,L$ | The unique nonidentity affine symmetry of $a$ fails the cat translation condition | Common-factor mechanism excluded |
| Canonical coprime CRT tensor product | Impossible for the kicked matrix at nonzero algebraic parameter | Exact decoupling mechanism excluded |
| Seven coordinate Jacobi blocks | Not permuted by the full matrix | Direct block mechanism excluded |
| Arbitrary non-Clifford antiunitary for a fixed unitary | Exists abstractly in an eigenbasis | No absence claim |
| CUE/Hdiag | None of the above establishes the required correlations | Unresolved |

The branch closes the specified geometric and CRT mechanisms. An extension beyond this scope would need a concrete additional symmetry class or an actual invariant decomposition to test, rather than a generic statement about quantum chaos.
