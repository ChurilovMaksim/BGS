> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_continuation_2026_10_20/exact_spectral_simplicity.md`. Embedded SHA256: `4aef0bf28965da0c359c01dff6e3bd330dd0cafdeb79118a5e84bd359d1ac2eb`.
> [Thematic guide](../../topics/algebra.md).

# Exact spectral simplicity: proved classes and the remaining obstruction

Independent research pass, 20 October 2026. Existing foundational reports are not modified.

## 1. Results and limits

For the actual matrices in the problem, the following statements are proved.

**Theorem A.** For every integer k >= 1, both M_(3^k) and M_(5^k) have simple spectrum. Consequently U_(3^k)(z) and U_(5^k)(z) have simple spectrum at every algebraic parameter z, including the specified tau = 10^(-80). No smallness estimate on tau is used.

**Theorem B.** More generally, let p be an odd prime for which 2 is a quadratic nonresidue and ord_p(S) = p+1. Then M_p is simple and U_p(z) is simple at every algebraic z. If additionally S^(p+1) = I+pB with B invertible modulo p, the same conclusion holds in every dimension p^k.

Theorem A supplies two explicit infinite families of actual dimensions. No assertion that infinitely many primes satisfy the maximal-order condition is needed or made. The lifting condition in Theorem B is substantive and must not be omitted.

**Theorem C.** Every eigenvalue of the actual A_N has multiplicity at most gcd(N,7), for every odd N. Thus A_N is simple when 7 does not divide N, and A_N has at least N/7 distinct eigenvalues uniformly. This does not give a multiplicity bound for U_N.

**Theorem D: complete classification of the bare cat matrix.** For an odd prime p, write r_p=ord_p(S) and s_p=v_p((S^(r_p))_(21)). For every odd N>1, M_N has simple spectrum if and only if

$$
N=p^a,\qquad r_p=p+1,\qquad
\bigl(a=1\ \text{or}\ s_p=1\bigr).
\tag{1.1}
$$

In all the dimensions (1.1), U_N(z) is simple at every algebraic z. Failure of (1.1) describes degeneracy of M_N at z=0; it does not assert degeneracy of the perturbed U_N at nonzero z. Dimension N=1 is trivially simple.

An exact finite-field certificate described in Section 7 additionally proves simplicity of U_N(z), for every nonzero algebraic z, in all odd dimensions 3 <= N <= 201 except 7, 49, and 147. The cases 49 and 147 are unproved by these certificates; failed reductions do not prove persistent degeneracy. Dimension 7 is genuinely exceptional: A_7 = (9/10)I and M_7 has repeated eigenvalues.

Universal simplicity for all other odd dimensions remains unproved. The first missing assertion in a complex-time route is identified in Section 5. Section 8 supplies a strict counterexample to replacing that assertion by simple A, a scalar joint commutant, nonzero traces, or absence of scalar returns.

## 2. Exact definitions and the algebraic transfer

Let N be odd, e_N(x) = exp(2 pi i x/N), and let modular fractions denote inverses modulo N. Put

$$
(T_N(a,b)u)(x)=e_N\bigl(b(x+\overline2 a)\bigr)u(x+a),
$$

$$
(M_N)_{xy}=N^{-1/2}e_N\bigl[-\overline8(3x^2-2xy+3y^2)\bigr],
\qquad S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
\tag{2.1}
$$

The Hamiltonian is the exact Hermitian matrix

$$
(A_N)_{xx}=V(x/N),
\qquad
(A_N)_{x,x+1}=\frac{e^{-i\alpha_0}}{200}
r\left(\frac{x+\overline2}{N}\right),
\tag{2.2}
$$

with the opposite entry its conjugate and

$$
r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\quad
e^{i\alpha_0}=\frac{-3+4i}{5},
$$

$$
V(q)=\cos14\pi q+\frac{r(q)}{10}
       +\frac{r(q)\sin2\pi q}{100}-\frac1{10}.
\tag{2.3}
$$

All entries of A_N and M_N are algebraic. Set

$$
U_N(z)=e^{izNA_N}M_N,
\qquad
\Delta_N(z)=\operatorname{disc}_X\det(XI-U_N(z)).
\tag{2.4}
$$

If lambda_j are the distinct eigenvalues of A_N, its spectral projectors are algebraic:

$$
P_j=\prod_{k\ne j}\frac{A_N-\lambda_kI}{\lambda_j-\lambda_k},
\qquad e^{izNA_N}=\sum_j e^{iN\lambda_jz}P_j.
$$

It follows that Delta_N is a finite exponential polynomial with algebraic coefficients and algebraic frequencies. After collecting equal frequencies, write it as sum_beta c_beta exp(beta z). For a nonzero algebraic z, the numbers beta z are distinct algebraic numbers. Lindemann-Weierstrass therefore implies

$$
\boxed{\Delta_N\not\equiv0\quad\Longrightarrow\quad
\Delta_N(z)\ne0\quad
\text{for every nonzero algebraic }z.}
\tag{2.5}
$$

The precise linear-independence statement used here is Theorem 3.2 of reference [1]. When Delta_N(0) is nonzero, (2.5) also covers z=0 by that direct evaluation. This transfer requires an actual proof that Delta_N is not identically zero; it is not a genericity assumption.

## 3. Prime-power simplicity of the cat matrix

### 3.1 Exact trace-square identity and the scalar phase

Direct substitution in (2.1) gives the exact Egorov identity

$$
M_N T_N(v)M_N^{-1}=T_N(Sv).
\tag{3.1}
$$

The normalized Weyl matrices form an orthonormal basis of End(C^N). Taking the trace of conjugation by M_N^m in this basis gives

$$
\boxed{|\operatorname{Tr}M_N^m|^2
=\#\ker(S^m-I:(\mathbb Z/N\mathbb Z)^2\to
                         (\mathbb Z/N\mathbb Z)^2).}
\tag{3.2}
$$

Indeed, the right side counts the Weyl basis vectors fixed by the permutation (3.1), while in an eigenbasis of M_N the trace of conjugation is sum_(j,k) lambda_j^m conjugate(lambda_k^m).

Let r be the order of S modulo N. Equation (3.1) implies that M_N^r commutes with every Weyl matrix, hence is scalar. This last implication is elementary: commuting with T_N(0,1) forces a matrix to be diagonal, and commuting with T_N(1,0) makes its diagonal constant. Write M_N^r=cI and choose a unit complex gamma with gamma^r=c. The matrix gamma^(-1) M_N has r-th roots of unity as its eigenvalues. Denote their multiplicities by n_0,...,n_(r-1). Finite Fourier orthogonality gives

$$
\sum_{j=0}^{r-1}n_j=N,
\qquad
\sum_{j=0}^{r-1}n_j^2
=\frac1r\sum_{m=0}^{r-1}|\operatorname{Tr}M_N^m|^2.
\tag{3.3}
$$

No asserted extra factor 4 or 8 in a metaplectic order is needed. The scalar phase is removed only after obtaining M_N^r=cI from exact Egorov. If the last quantity in (3.3) equals N, every n_j is 0 or 1 and M_N is simple.

### 3.2 A lifting lemma

Suppose p is odd, 2 is a nonresidue modulo p, and S modulo p has order r_0=p+1. Its eigenvalues in F_(p^2) are inverse primitive r_0-th roots. Thus S^m-I is invertible modulo p whenever r_0 does not divide m.

Assume further that

$$
S^{r_0}=I+pB,\qquad \det B\not\equiv0\pmod p.
\tag{3.4}
$$

For each j >= 0 and each positive u coprime to p,

$$
S^{r_0p^ju}-I=p^{j+1}C_{j,u},
\qquad C_{j,u}\equiv uB\pmod p.
\tag{3.5}
$$

Here is the valuation proof. If a >= 1, expanding (I+p^a C)^p shows that its first nonconstant term is p^(a+1)C. Every other term is divisible by p^(a+2): for 2 <= h <= p-1 its valuation is at least 1+ah >= a+2, and the h=p term has valuation ap >= a+2. Iteration proves (3.5) for u=1. Raising to u then leaves uC as the coefficient modulo p, since every quadratic or higher term has one extra factor p. In particular every C_(j,u) is invertible modulo p.

It follows that for N=p^k the order of S is exactly

$$
r=(p+1)p^{k-1}.
\tag{3.6}
$$

For 0 <= m < r, the fixed-point counts in (3.2) are now explicit:

| Class of m | Number of such m | Kernel size |
|---|---:|---:|
| r_0 does not divide m | p^k | 1 |
| m=r_0 p^j u, p does not divide u, 0 <= j <= k-2 | (p-1)p^(k-j-2) | p^(2j+2) |
| m=0 | 1 | p^(2k) |

For the middle row, multiplication by the invertible matrix C_(j,u) in (3.5) does not change the kernel. Each coordinate of a kernel vector of p^(j+1)I has p^(j+1) possible values modulo p^k. For k=1 the middle rows are absent.

Adding the last column with its multiplicities gives

$$
\begin{aligned}
\sum_{m=0}^{r-1}|\operatorname{Tr}M_{p^k}^m|^2
&=p^{2k}+p^k
 +(p-1)p^k\sum_{j=0}^{k-2}p^j\\
&=p^{2k-1}(p+1).
\end{aligned}
\tag{3.7}
$$

Dividing by (3.6) gives p^k=N. Equation (3.3) proves simplicity of M_(p^k). In the prime case k=1, assumption (3.4) is unnecessary: maximal nonsplit order alone gives the same conclusion. Equation (2.5) proves all the corresponding claims about U_N(z).

### 3.3 The explicit primes 3 and 5

For p=3, S modulo 3 has order 4: its square is -I. Also

$$
S^4=\begin{pmatrix}577&816\\408&577\end{pmatrix},
\qquad
\frac{S^4-I}{3}\equiv
\begin{pmatrix}0&2\\1&0\end{pmatrix}\pmod3,
$$

whose determinant is 1 modulo 3. For p=5, S modulo 5 has order 6: its cube is -I, and its square is not I. Moreover

$$
S^6=\begin{pmatrix}19601&27720\\13860&19601\end{pmatrix},
\qquad
\frac{S^6-I}{5}\equiv
\begin{pmatrix}0&4\\2&0\end{pmatrix}\pmod5,
$$

whose determinant is 2 modulo 5. The number 2 is a nonresidue for both primes. Thus every hypothesis of Section 3.2 is checked, proving Theorem A for every k >= 1.

For the particular S, a superficially parallel condition ord_p(S)=p-1 in the split case is empty. Its eigenvalue is 3+2 sqrt(2)=(1+sqrt(2))^2, a square in F_p when 2 is a residue. Its order therefore divides (p-1)/2. No nonexistent split maximal-order class is counted in Theorem B.

### 3.4 Complete classification for every odd N

The following extension was supplied by the root researcher and independently checked. Put

$$
J=\begin{pmatrix}0&2\\1&0\end{pmatrix},\qquad J^2=2I,
\qquad S^m=t_mI+u_mJ.
$$

For m>=1, t_m,u_m are positive integers and t_m^2-2u_m^2=1. Let p be any odd prime and r_p=ord_p(S). Since S^(r_p) is I modulo p, one has t_(r_p)=1 modulo p and u_(r_p)=0 modulo p. Set s_p=v_p(u_(r_p))>=1. The identity

$$
(t_{r_p}-1)(t_{r_p}+1)=2u_{r_p}^2
$$

and the fact that t_(r_p)+1 is a p-adic unit give v_p(t_(r_p)-1)=2s_p. Thus

$$
p^{-s_p}(S^{r_p}-I)
\equiv (u_{r_p}/p^{s_p})J\pmod p
\tag{3.8}
$$

is invertible modulo p. The binomial argument of Section 3.2 applies with starting valuation s_p and proves

$$
\operatorname{ord}_{p^a}(S)
=r_p p^{\max(0,a-s_p)}.
\tag{3.9}
$$

The characteristic polynomial of S modulo p is separable, since its discriminant is 32. Its eigenvalues lie either in F_p or in the norm-one subgroup of F_(p^2), so r_p divides p-1 or p+1 respectively. In particular r_p<=p+1 and, if r_p is not p+1, one has r_p<p. If a=1 and r_p<p+1, equation (3.9) is less than p. If a>=2 and either r_p<p+1 or s_p>=2, equation (3.9) is again strictly less than p^a: in the latter case it is at most (p+1)p^(a-2) when a>s_p, and at most p+1 when a<=s_p.

Because M_(p^a) has at most ord_(p^a)(S) distinct eigenvalues after removal of a scalar phase, all these cases are nonsimple. Conversely, the remaining cases r_p=p+1 and (a=1 or s_p=1) are precisely the cases proved simple by Sections 3.1-3.2. This establishes (1.1) for prime powers.

For completeness consider N with at least two distinct prime divisors, and write its pairwise coprime prime-power factors as n_j. Under the standard CRT basis permutation the explicit kernel (2.1) factors exactly as a tensor product of twisted kernels

$$
M_{n_j}^{(c_j)}(x,y)
=n_j^{-1/2}e_{n_j}\bigl[-c_j\overline8
       (3x^2-2xy+3y^2)\bigr],
\qquad c_j=(N/n_j)^{-1}\pmod{n_j}.
\tag{3.10}
$$

Indeed, the CRT identity for the additive character is e_N(z)=product_j e_(n_j)(c_j z_j); the quadratic form and inverse of 8 reduce componentwise, and N^(-1/2)=product_j n_j^(-1/2).

The exact Weyl covariance of the factor (3.10) has matrix

$$
S_{c_j}=\begin{pmatrix}3&4c_j^{-1}\\2c_j&3\end{pmatrix}
=\operatorname{diag}(1,c_j)S\operatorname{diag}(1,c_j)^{-1}.
\tag{3.11}
$$

Thus its modular orders and all fixed-point counts agree with those of S. The preceding prime-power classification applies unchanged to every twisted factor. If one factor is nonsimple, the tensor product is nonsimple.

If every factor is simple, its dimension and projective period are

$$
n_j=p_j^{a_j},\qquad
R_j=(p_j+1)p_j^{a_j-1}.
$$

The period R_j is even and n_j>R_j/2. After removal of a scalar phase, that factor's n_j distinct eigenvalues occupy more than half of the R_j-th roots of unity. Partitioning those roots into antipodal pairs shows that its spectrum contains both lambda_j and -lambda_j. Two different factors therefore produce the repeated tensor eigenvalue

$$
\lambda_1\lambda_2=(-\lambda_1)(-\lambda_2).
$$

The corresponding tensor eigenvectors are distinct. Extra factors do not remove the collision. Hence every odd N with at least two distinct prime factors has nonsimple M_N. This finishes the complete bare-cat classification, without extending its nonsimplicity conclusion to the perturbed family.

There is also a shorter proof of the composite assertion using only classical CRT, which gives a stronger count. Write N=product_(j=1)^h n_j with h>=2 prime-power factors, and R_j=ord_(n_j)(S). If R_j is even, (3.9) gives R_j/n_j <= (p_j+1)/p_j <= 4/3. If R_j is odd, r_(p_j) is an odd divisor of the even number p_j-1 or p_j+1, so R_j/n_j <= (p_j+1)/(2p_j) <= 2/3. Let e be the number of even R_j. Classical CRT gives R_N=lcm(R_1,...,R_h). If e>=1, their common factors 2 imply

$$
\frac{R_N}{N}
\le\frac{(4/3)^e(2/3)^{h-e}}{2^{e-1}}
=2(2/3)^h\le\frac89.
$$

If e=0, the bound is instead (2/3)^h <= 4/9. Therefore the number q(M_N) of distinct bare-cat eigenvalues satisfies the exact uniform estimate

$$
\boxed{q(M_N)\le\operatorname{ord}_N(S)\le\frac89N
\quad\text{whenever N has at least two distinct prime divisors}.}
\tag{3.12}
$$

The first inequality follows directly from M_N^(R_N) being scalar. This proof does not require the quantum CRT factorization (3.10), and the estimate concerns the bare matrix M_N only.

## 4. The exact Jacobi statement for A_N

On an odd N-grid, 1+cos(2 pi q) never vanishes. The remaining factor of r vanishes exactly when N divides 7x, giving g=gcd(N,7) grid zeros. The modular midpoint x+bar(2) permutes the grid, so (2.2) has exactly g zero edges. These cut the cyclic nearest-neighbor graph into g paths of equal length N/g.

Every remaining edge is nonzero. A diagonal unitary gauge along each path removes its hopping phases, giving an irreducible real symmetric Jacobi matrix. For an eigenvector, its value at the first vertex determines its value at the second by the first row and then all later values by recurrence. A zero first value forces the whole eigenvector to vanish. Every eigenspace of one path therefore has dimension at most one. Hermiticity turns this into algebraic simplicity.

The direct sum of g such paths has each eigenvalue with multiplicity at most g. This proves Theorem C, including N=7, when the paths have length one and A_7=(9/10)I. The argument uses the exact modular midpoint; replacing it by an ordinary half-integer grid would change the cut calculation.

## 5. What a complex-time argument would still have to prove

Here is a rigorous sufficient criterion. Suppose A has distinct eigenvalues a_1>...>a_N. In that ordered orthonormal eigenbasis let B be the matrix of M and set

$$
b_k=\det B[1{:}k,1{:}k],\qquad b_0=1.
$$

If every b_k is nonzero, e^(tA)M has simple eigenvalues for all sufficiently large positive real t, with asymptotics

$$
\lambda_k(t)=e^{ta_k}\left(\frac{b_k}{b_{k-1}}+o(1)\right).
\tag{5.1}
$$

To prove this, the coefficient of X^(N-k) in det(XI-e^(tA)M) is (-1)^k times the sum of principal minors det B[I,I] weighted by exp(t sum_(i in I) a_i). The unique largest exponential has I={1,...,k} and coefficient b_k. On the scale X=e^(ta_k)Y, exactly the k-1 and k terms dominate. After normalization their sum is a nonzero factor times Y^(N-k)(b_(k-1)Y-b_k). A small circle around b_k/b_(k-1), bounded away from zero, contains exactly one simple root by Rouche's theorem for all sufficiently large t. The N scales are disjoint because the a_k are strictly ordered. This proves (5.1).

For U_N(z), take z=t/(iN). Consequently this criterion would prove Delta_N not identically zero. The first unsupported assertion in this route is precisely

$$
\det M_N[1{:}k,1{:}k]\ne0
\quad\text{in the eigenbasis of }A_N
\quad\text{for every }k.
\tag{5.2}
$$

No proof of (5.2) for the specified family is supplied here. Flatness of M_N in the coordinate basis is not (5.2). Simplicity of A_N, or a scalar common commutant, does not replace it. At dimensions divisible by 7 even the prerequisite that A_N be simple requires additional analysis of coincidences between the seven path spectra. Theorem C gives a multiplicity bound, not their disjointness.

## 6. A first-order criterion that can actually be certified

Let M be unitary and P_lambda its spectral projections. If each Hermitian compression

$$
H_\lambda=P_\lambda A P_\lambda\big|_{\operatorname{ran}P_\lambda}
\tag{6.1}
$$

has simple spectrum, then e^(tA)M has simple spectrum for all sufficiently small nonzero complex t. Hence its discriminant is not identically zero.

For a direct proof, decompose into E=ran P_lambda and its complement. Near X=lambda the complementary block of XI-e^(tA)M is invertible. Its Schur complement on E is

$$
(X-\lambda)I_E-t\lambda H_\lambda
 +O(t^2+t|X-\lambda|).
$$

Substitute X=lambda+t lambda Y and divide its determinant by (t lambda)^(dim E). The resulting analytic function has value det(YI-H_lambda) at t=0. Each simple root continues by the implicit-function theorem to a distinct branch X=lambda+t lambda mu+O(t^2). Different original M-eigenvalues remain separated. This proves the criterion with no assertion about higher-order splitting when (6.1) has repetitions.

In particular, a proof of universal simplicity of all the compressions (6.1) would settle the universal nonidentity needed in (2.5). It has not been obtained here.

## 7. Exact finite certificates and their limits

The independent script `verify_spectral_simplicity.py` evaluates (6.1) by finite-field arithmetic. It does not compute an exponential or floating-point eigenvalue. Its main output is `spectral_simplicity_certificates.json`; two checks limited to N=49,147 are in `spectral_simplicity_exception_retry_1.json` and `spectral_simplicity_exception_retry_2.json`.

For a given N it computes r=ord_N(S) and a prime ell congruent to 1 modulo lcm(4N,8r), excluding denominators and with ell>N. A primitive root of F_ell supplies coherent reductions of i, e_N(1), and an r-th root of unity. A square root of N supplies the harmless normalization of M. The two square-root choices differ by a scalar sign, which does not change its eigenspaces. The code verifies that M^r=cI and chooses a residue gamma with gamma^r=c.

The corresponding characteristic-zero algebraic extension can be chosen with this residue of gamma: it is a root of X^r-c, whose reduction is separable because ell does not divide r. No unproved exact eighth-root phase convention for the original M is needed. Set M'=gamma^(-1)M. For xi of order r, form the exact projectors

$$
P_k=\frac1r\sum_{j=0}^{r-1}\xi^{-kj}(M')^j.
\tag{7.1}
$$

The characteristic-zero projector ranks are integers between 0 and N. Since ell>N, their reduced traces recover those ranks uniquely. For every nontrivial rank d, the code selects independent columns B of the reduced P_k and independent rows I of B, then computes

$$
C=(B_I)^{-1}(P_k A B)_I.
\tag{7.2}
$$

The selected invertible minor lifts to an invertible algebraic minor, so (7.2) really is a reduction of the characteristic-zero compression. The script computes its monic characteristic polynomial and its gcd with its derivative. A constant gcd proves its discriminant is nonzero modulo ell and therefore nonzero in characteristic zero. Section 6 followed by (2.5) proves simplicity at the actual algebraic parameter tau.

All arithmetic uses integers modulo ell. Before any NumPy matrix multiplication the script checks N(ell-1)^2 < 2^63-1, excluding signed-integer overflow. Modular inversions are exact. The characteristic-polynomial recursion is also checked by its terminal Cayley-Hamilton identity. The JSON records the prime, primitive root, embedding values, spectral sector ranks, selected minors, characteristic polynomials, and gcds, so the result is reproducible rather than an assertion of numerical eigenvalue separation.

The completed run covered the 100 odd dimensions from 3 through 201. It returned successful certificates in 97 dimensions, namely all except 7,49,147. These successes are exact finite conclusions. They include dimensions divisible by 7, for example 21 and 35.

Only the two unresolved nontrivial cases were retried, with the following primes:

| N | Original prime | First retry | Second retry | Repeated two-dimensional sectors in each reduction |
|---:|---:|---:|---:|---:|
| 49 | 3529 | 24697 | 47041 | 6 |
| 147 | 37633 | 108193 | 197569 | 3 |

Thus a change of the selected reduction prime did not remove these first-order degeneracies. This is evidence of a structural first-order obstruction, but several bad reductions are not a characteristic-zero proof: a nonzero algebraic discriminant can vanish modulo several primes. No statement that Delta_49 or Delta_147 is identically zero follows. Higher-order splitting has not been asserted or tested. The infinite prime-power theorem in Section 3 is independent of every computation in this section.

## 8. A counterexample with simple A and scalar joint commutant

The inference “simple A and scalar joint commutant imply a generically simple product family” is false, even in odd dimension with nonzero power traces and no scalar returns.

Let n=2d+1 with d>=3. Take

$$
A=\operatorname{diag}(-d,\ldots,-1,1/2,1,\ldots,d).
$$

Let J exchange each coordinate with exponent j and the one with exponent -j, and fix the central coordinate. Put

$$
v=n^{-1/2}(1,\ldots,1)^T,\qquad
M=J(I-2vv^*)=J-2vv^*.
\tag{8.1}
$$

Since Jv=v, M is a real rational symmetric orthogonal involution. Every entry is either -2/n or 1-2/n and is nonzero. The matrix A is simple. An operator commuting with A is diagonal; if it also commutes with M, every pair of its diagonal entries is equal because every M-entry is nonzero. Thus the joint commutant is precisely the scalars.

Nevertheless, on each pair of coordinates the matrix e^(izA)J has the block

$$
\begin{pmatrix}0&e^{-ijz}\\e^{ijz}&0\end{pmatrix},
$$

with eigenvalues +1 and -1 for every complex z. Each corresponding eigenspace has dimension d. The difference

$$
e^{izA}M-e^{izA}J=-2e^{izA}vv^*
$$

has rank one. Intersecting each d-dimensional eigenspace with ker v^* shows that +1 and -1 remain eigenvalues with geometric multiplicity at least d-1. In particular

$$
\boxed{(X^2-1)^{d-1}\text{ divides }
\det(XI-e^{izA}M)\quad\text{for every }z.}
\tag{8.2}
$$

For d>=3 the discriminant is identically zero. There are at most five distinct eigenvalues, regardless of n.

The factorization is explicit. With u_j=e^(ijz), w=e^(iz/2), and Q(z)=sum_(j=1)^d(u_j+u_j^(-1)), the matrix determinant lemma gives

$$
\det(XI-e^{izA}M)=(X^2-1)^{d-1}
\left[X^3+\frac{2Q-(n-2)w}{n}X^2
 +\frac{n-2-2wQ}{n}X-w\right].
\tag{8.3}
$$

For verification, the rank-one determinant lemma starts from (X^2-1)^d(X-w). A paired block contributes [X(u_j+u_j^(-1))+2]/(X^2-1) to the resolvent contraction, while the central coordinate contributes w/(X-w). Multiplication and collection give (8.3).

This family also satisfies the other stated rigidity properties. Since Tr M=1-2=-1 and M^2=I, every power trace is nonzero at z=0. Each trace is an algebraic exponential polynomial, so Lindemann-Weierstrass makes it nonzero at every nonzero algebraic z. If an odd power were scalar, the persistent eigenvalues +1 and -1 would contradict each other. An even scalar power would have to equal I; but its determinant is exp(izm/2), since det(M)^m=1. This cannot equal 1 at nonzero algebraic z. Thus no positive scalar return occurs there.

The leading-minor condition in Section 5 genuinely fails in this example. In the ordered A-eigenbasis, a two-by-two principal submatrix on two negative exponents is (-2/n) times the all-ones matrix and has determinant zero. Nonzero diagonal entries and a dense M do not prevent this failure.

This is a separate family, not the original cat quantization. Its role is to invalidate the proposed general inference, not to refute simplicity of U_N in any currently unproved original dimension.

## 9. What remains open for the actual family

The original universal target has not been replaced by the subsequences of Theorem A. For arbitrary odd N other than 7, one still needs an actual proof that Delta_N is not identically zero. Two specific sufficient obligations are now explicit: the ordered nonzero principal-minor chain (5.2), or simple first-order compressions (6.1), with a higher-order argument where first-order splitting fails. Neither is supplied uniformly by irreducibility, exact Clifford/CRT rigidity, or the Jacobi multiplicity bound for A_N.

The proven contribution is exact simplicity in the infinite actual families N=3^k and N=5^k, the complete bare-cat classification and its sufficient perturbed simplicity classes, the uniform bound on A_N multiplicities, and the finite certificates in Section 7. None provides a lower bound on eigenphase spacings or a microscopic-statistics limit.

## Reference

1. S. A. Popescu, *A simple and self-contained proof for the Lindemann-Weierstrass theorem*, arXiv:2306.14352v2, Theorem 3.2. https://arxiv.org/html/2306.14352v2
