> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_iterated_sector_covariance.md`. Embedded SHA256: `c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2`.
> [Thematic guide](../../topics/arithmetic.md).

# Every fixed iterate: arithmetic sector covariance and basis-independent quantum variance

Research pass, 20 October 2026. The parameter is the exact constant
tau=10^(-80). Previously frozen reports are not modified.

## 1. Results

Fix an odd d>=3. Let N=d^2m tend to infinity through all odd m, and write
G=(Z/dZ)^2. For g=(alpha,beta) in G set

$$
T_g=T_N(dm\alpha,dm\beta),\qquad
P_\chi=\frac1{d^2}\sum_{g\in G}\overline{\chi(g)}T_g,
\quad\chi\in\widehat G.
\tag{1.1}
$$

These are d^2 mutually orthogonal projections, each of rank N/d^2. Their
sum is the identity. The trivial character gives the canonical old
projector from the preceding report.

**Theorem A: covariance for every fixed nonzero iterate.** For every
fixed integer r!=0 and every pair of characters chi,eta,

$$
\boxed{\frac1N\operatorname{Tr}
(P_\chi U_N^{-r}P_\eta U_N^r)\longrightarrow\frac1{d^4}.}
\tag{1.2}
$$

All the limits use the actual U_N at the fixed tau. The assertion is
proved for every fixed r, not just for r in a finite range. It does not
assert convergence uniformly for r growing with N.

Let Pi_lambda denote the spectral projection of the actual unitary U_N
at its distinct eigenvalue lambda, and define the Hilbert-Schmidt
orthogonal projection onto its full commutant by

$$
\mathcal E_{U_N}(B)=\sum_\lambda\Pi_\lambda B\Pi_\lambda.
\tag{1.3}
$$

**Theorem B: basis-independent arithmetic quantum variance.** For every
fixed d and every character chi,

$$
\boxed{\frac1N\left\|\mathcal E_{U_N}(P_\chi)
                       -\frac1{d^2}I\right\|_{\rm HS}^2\longrightarrow0.}
\tag{1.4}
$$

No simplicity or gap assumption is imposed on the spectrum. Consequently,
for every choice of an orthonormal eigenbasis psi_(j,N),

$$
\frac1N\sum_{j=1}^N
\left|\langle\psi_{j,N},P_\chi\psi_{j,N}\rangle
                         -\frac1{d^2}\right|^2\longrightarrow0.
\tag{1.5}
$$

In particular, a positive fraction of almost-old eigenvectors is
impossible. If epsilon<1-d^(-2) is fixed, the proportion of vectors in
any orthonormal eigenbasis with old mass at least 1-epsilon tends to
zero. The simultaneous conclusion for every character follows because
d is fixed and the character set is finite.

The new input is a classical statement about every iterate, proved
quantitatively below: if Psi is the exact classical map appropriate to
the prescribed modular quantization, then

$$
\boxed{\Psi^r t_h\Psi^{-r}\text{ is a literal torus translation}
       \ \Longrightarrow\ h=0\text{ in }\mathbb T^2,
       \quad r\ge1.}
\tag{1.6}
$$

Here h may even be irrational. The proof of (1.6) uses a geometrically
discounted unstable-coordinate identity. It does not extrapolate an
error estimate growing exponentially with r.

## 2. Exact classical symbol and conventions

Use the ordinary Weyl operators

$$
(W_N(k,l)\psi)(x)=e^{2\pi ikx/N+\pi ikl/N}\psi(x+l),
\qquad\operatorname{Op}_N(b)=\sum\widehat b(k,l)W_N(k,l).
$$

For odd N, T_N(l,k)=(-1)^(kl) W_N(k,l). Thus the exact A_N is the
ordinary Weyl quantization of

$$
a(q,p)=V(q)+\frac1{100}r(q+\tfrac12)
                          \cos(2\pi p-\alpha_0),
\tag{2.1}
$$

where

$$
V(q)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}.
$$

The Fourier support lies in |k|<=9, |l|<=1, and

$$
\sum_{k,l}|\widehat a(k,l)|\le\frac{59}{50}.
\tag{2.2}
$$

One direct verification of (2.2) is to write
V=(9/10)cos(14pi q)+(1/10)(1-cos(14pi q))cos(2pi q)
+(1/100)r(q)sin(2pi q). Its Fourier norm is at most
9/10+2/10+4/100=57/50, and the p-dependent term adds at most 4/100.
Two particular coefficients are

$$
\widehat a(1,0)=\frac1{20}-\frac{i}{200},\qquad
\widehat a(0,1)=\frac{e^{-i\alpha_0}}{200}.
\tag{2.3}
$$

Let

$$
X=\frac1{2\pi}(a_p\partial_q-a_q\partial_p),
\qquad \Phi_s=\text{the time-s flow of }X,
\qquad S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
\qquad \Psi=S\circ\Phi_\tau.
\tag{2.4}
$$

We use the Egorov convention U Op(b) U*=Op(b composed with Psi)+o(1).
Reversing the physical forward-time convention replaces Psi by its
inverse and does not alter any covariance conclusion.

For completeness, the exact modular Egorov identity for M_N is

$$
M_NT_N(v)M_N^*=T_N(Sv),\qquad v=(l,k).
\tag{2.5}
$$

It follows directly by substituting z=y+l in M_NT_N(l,k). Relative to
the unshifted kernel, its exponent has x coefficient -l/4, z coefficient
3l/4+k, and constant -3l^2/8-lk/2, with modular fractions. The same
three coefficients arise in T_N(l',k')M_N for l'=3l+4k and k'=2l+3k.
This proves (2.5). Moreover l'k'-lk=6l^2+16lk+12k^2 is even, so (2.5)
becomes the exact ordinary identity

$$
M_N\operatorname{Op}_N(b)M_N^*
                         =\operatorname{Op}_N(b\circ S).
\tag{2.6}
$$

The fixed-time exponential Egorov estimate, proved from the sine Taylor
remainder and Duhamel in the preceding report, is

$$
e^{isNA_N}\operatorname{Op}_N(b)e^{-isNA_N}
               =\operatorname{Op}_N(b\circ\Phi_s)+O_{b,s}(N^{-2}).
\tag{2.7}
$$

Combining (2.6)-(2.7) and iterating a fixed number of times gives

$$
U_N^r\operatorname{Op}_N(b)U_N^{-r}
               =\operatorname{Op}_N(b\circ\Psi^r)+O_{b,r}(N^{-2}).
\tag{2.8}
$$

The constant in (2.8) is allowed to depend on r. The proof below never
requires a uniform Egorov estimate for unbounded r.

## 3. The discounted unstable-coordinate identity

Let

$$
\lambda=3+2\sqrt2>5,\qquad
\ell=\frac{(1,\sqrt2)}{\sqrt3}.
$$

Then ||ell||=1 and ell*S=lambda*ell. Define the periodic lifted kick
displacement delta=Phi_tau-Id and the equivariant lift of Psi by
Psi(x)=Sx+S delta(x). For every r>=1, the scalar function

$$
v_r(x)=\lambda^{-r}\ell\Psi^r(x)-\ell x
\tag{3.1}
$$

is periodic on R^2/Z^2. Telescoping the lift gives the exact identity

$$
\boxed{v_r(x)=\sum_{j=0}^{r-1}\lambda^{-j}
                              \ell\delta(\Psi^j(x)).}
\tag{3.2}
$$

The corresponding first variation is the periodic trigonometric sum

$$
w_r(x)=\tau\sum_{j=0}^{r-1}\lambda^{-j}\ell X(S^j x).
\tag{3.3}
$$

Each individual r is finite. The crucial estimate proved next is uniform
over every integer r>=1:

$$
\boxed{\|v_r-w_r\|_\infty\le3\cdot10^7\tau^2.}
\tag{3.4}
$$

This estimate compares only the discounted scalar coordinate. It does
not claim a uniformly accurate Taylor expansion of the full map Psi^r.

## 4. Proof of the uniform error estimate

By (2.2), the frequency length is less than 10 and the generous bounds

$$
\|X\|_\infty\le20,\qquad
\|\nabla X\|_\infty\le2000
\tag{4.1}
$$

hold. Indeed, the vector coefficient of X at (k,l) is
i(l,-k)*a_hat(k,l), and differentiating adds at most 2pi times the
frequency length. Integrating the bounded vector field along its flow
gives

$$
\|\delta\|_\infty\le20\tau,
\qquad
\|\delta-\tau X\|_\infty\le20000\tau^2.
\tag{4.2}
$$

For the second inequality, integrate
||X(Phi_s x)-X(x)||<=2000*20*s from 0 to tau.

Let D=diag(sqrt(2),1). The matrix D^(-1) S D is symmetric with
eigenvalues lambda and lambda^(-1). Hence

$$
\|S^j\|\le\sqrt2\lambda^j\quad(j\ge0).
\tag{4.3}
$$

Using only the bounded displacement in (4.2), the exact lift recursion
gives

$$
\begin{aligned}
\|\Psi^j-S^j\|_\infty
&\le20\tau\sum_{a=1}^{j}\|S^a\|\\
&\le20\sqrt2\tau\frac{\lambda(\lambda^j-1)}{\lambda-1}
\le50\tau\lambda^j.
\end{aligned}
\tag{4.4}
$$

No derivative of Psi^j was used. Although (4.4) grows, the vector field
is periodic and uniformly bounded. Therefore

$$
\|X\circ\Psi^j-X\circ S^j\|_\infty
\le\min(10^5\tau\lambda^j,40).
\tag{4.5}
$$

Equations (3.2)-(3.3) and (4.2)-(4.5) give

$$
\|v_r-w_r\|_\infty
\le\sum_{j=0}^{r-1}
\left[20000\tau^2\lambda^{-j}
          +\min(10^5\tau^2,40\tau\lambda^{-j})\right].
\tag{4.6}
$$

For the prescribed tau, split the sum at the fixed integer 200.
Since lambda>5 and 5^200>10^80=tau^(-1), one has
lambda^(-200)<tau. Also (1-lambda^(-1))^(-1)<5/4. Thus the right side
of (4.6), even extended to all j>=0, is at most

$$
\left(20000\frac54+200\cdot10^5+40\frac54\right)\tau^2
=20025050\tau^2<3\cdot10^7\tau^2.
$$

This proves (3.4) for all r at once. In particular it remains valid far
beyond the range where an undiscouted perturbation estimate is useful.

## 5. Two Fourier coefficients survive every iterate

Write e_1=(1,0), e_2=(0,1). For j>=1 the two frequencies
S^(-Tj)e_1 and S^(-Tj)e_2 lie outside the support strip |l|<=1 of X.
To verify this for all j, write

$$
S^j=\begin{pmatrix}t_j&2u_j\\u_j&t_j\end{pmatrix},
\quad t_1=3,\ u_1=2,
\quad t_{j+1}=3t_j+4u_j,\quad u_{j+1}=2t_j+3u_j.
$$

The entries are positive and increasing. Consequently

$$
S^{-Tj}e_1=(t_j,-2u_j),\qquad
S^{-Tj}e_2=(-u_j,t_j),
$$

whose second coordinates have absolute value at least 3. Therefore only
j=0 contributes to the two indicated Fourier coefficients of (3.3),
and for every r>=1,

$$
\widehat w_r(e_i)=\tau\ell\widehat X(e_i),\quad i=1,2.
\tag{5.1}
$$

Using (2.3), their squared leading magnitudes are exactly

$$
|\ell\widehat X(e_1)|^2=\frac{101}{60000},\qquad
|\ell\widehat X(e_2)|^2=\frac1{120000}.
\tag{5.2}
$$

In particular both magnitudes exceed 1/400. A Fourier coefficient is
bounded by the uniform norm of its function, so (3.4) gives

$$
|\widehat v_r(e_i)|
\ge\frac\tau{400}-3\cdot10^7\tau^2
\ge\frac\tau{800}>0,
\qquad i=1,2,\quad r\ge1.
\tag{5.3}
$$

The last inequality is checked at the actual rational tau: it is enough
that 3*10^7*tau<1/800. There is no r-dependent smallness requirement.

The first executable check r=2 is particularly transparent:
S^(-T)e_1=(3,-4) and S^(-T)e_2=(-2,3), so the additional linearized
summand contributes zero to both coefficients. The all-j argument above
is the structural extension of that exact check. The covector identity,
these two preimages, the squared magnitudes in (5.2), and the rational
constant 20025050 were independently checked with exact Fraction and
Q(sqrt(2)) arithmetic; no floating-point value of tau was used.

## 6. Excluding every literal translation intertwiner

Suppose for an integer r>=1 and torus translations t_h,t_k that

$$
\Psi^r t_h\Psi^{-r}=t_k.
\tag{6.1}
$$

Choose real representatives of h,k and the equivariant lift F=Psi^r.
Equality on the torus gives
F(x+h)=F(x)+k+n for a constant integer vector n. Iterating the
translation a positive integer L times gives

$$
F(x+Lh)-F(x)=L(k+n).
$$

Since F(x)=S^r x+u_r(x) for a bounded periodic u_r, dividing by L and
letting L grow yields k+n=S^r h. This argument also covers irrational h.

It follows from (3.1) that v_r(x+h)=v_r(x). For a periodic function,
invariance under h implies
(exp(2pi i e_i dot h)-1)*v_r_hat(e_i)=0. The two nonzero coefficients
in (5.3) force both coordinates of h to be integers. Thus h=0 on the
torus and then k=0, proving (1.6).

An important distinction is that (6.1) need not be a commutation
relation. The argument excludes the full literal intertwining relation,
including k!=h. No centralizer theorem or genericity assertion is used.

## 7. Covariance of every pair of arithmetic sectors

The T_g in (1.1) give an exact representation of G. Their Weyl cocycle
is trivial because (dm)^2=N*m. The trace of T_g is zero unless g=0,
when it is N. Finite character orthogonality now proves all projector
claims following (1.1), including rank(P_chi)=N/d^2.

For r>=1, expand

$$
\frac1N\operatorname{Tr}(P_\chi U_N^{-r}P_\eta U_N^r)
=\frac1{d^4}\sum_{g,h\in G}
\overline{\chi(g)\eta(h)}
\frac1N\operatorname{Tr}(T_gU_N^{-r}T_hU_N^r).
\tag{7.1}
$$

With t_g translation by (alpha/d,-beta/d), exact Weyl conjugation and
(2.8) show that F_N=T_g U_N^(-r) T_h U_N^r satisfies fixed-symbol
Egorov for the map

$$
\kappa_{g,h,r}=\Psi^r\circ t_h\circ\Psi^{-r}\circ t_g,
\tag{7.2}
$$

in the convention F_N Op(b) F_N*=Op(b composed with kappa)+o(1).
By (1.6), this map is nonidentity unless g=h=0. It is real analytic,
because the finite trigonometric vector field has a real analytic flow.
A nonidentity analytic map isotopic to the identity has a fixed set of
zero area: after lifting, the fixed set is a finite union of zero sets
of nonzero real analytic functions. Such a scalar zero set has measure
zero by restriction to suitable lines and Fubini.

For clarity, the normalized trace lemma used here is the elementary one
proved in the frozen oldspace report. If unitary F_N quantizes kappa in
the above fixed-symbol operator-norm sense, then any subsequential
functional limit of
b -> Tr(Op_N(b)F_N)/N has an L2 density with norm at most 1, by
Hilbert-Schmidt Cauchy-Schwarz and asymptotic Fourier orthogonality.
Cyclicity of the trace, the product rule Op(b)Op(c)=Op(bc)+O(N^-1),
and Egorov force this density times (b composed with kappa-b) to vanish
for every b. The two coordinate characters force its support into
Fix(kappa). A zero-area fixed set therefore makes the density zero,
and Tr(F_N)/N tends to zero.

Applying this lemma to (7.2), every term in (7.1) except g=h=0 vanishes
in the limit. There are only d^4 terms because d is fixed. The remaining
term is 1/d^4. This proves (1.2) for positive r. The negative-r result
follows by cyclicity, exchanging chi and eta, and applying the positive
case.

## 8. Projection onto the full spectral commutant

Let c=d^(-2) and B_chi=P_chi-cI. Then Tr(B_chi)=0 and

$$
\frac1N\|B_\chi\|_{\rm HS}^2=c-c^2.
$$

For each fixed nonzero integer n, Theorem A gives

$$
\frac1N\operatorname{Tr}(B_\chi U_N^{-n}B_\chi U_N^n)
\longrightarrow0.
\tag{8.1}
$$

Define the finite time average

$$
\mathcal A_{T,N}(B)=\frac1T\sum_{j=0}^{T-1}U_N^{-j}BU_N^j,
\qquad T\ge1.
$$

In a spectral decomposition of a unitary, the Hilbert-Schmidt matrix
blocks Pi_lambda B Pi_mu are mutually orthogonal. Commutation with U
means that only blocks with lambda=mu remain. This proves directly that
(1.3) is the Hilbert-Schmidt orthogonal projection onto the commutant.
It is a contraction and obeys

$$
\mathcal E_{U_N}(\mathcal A_{T,N}(B))=\mathcal E_{U_N}(B).
$$

Thus, for every finite N and T,

$$
\frac1N\|\mathcal E_{U_N}(B_\chi)\|_{\rm HS}^2
\le\frac1N\|\mathcal A_{T,N}(B_\chi)\|_{\rm HS}^2.
\tag{8.2}
$$

Expanding the right side as a fixed T^2-term sum and taking N to infinity,
(8.1) eliminates all off-diagonal time pairs. The T equal-time pairs
each contribute c-c^2. Consequently

$$
\limsup_{N\to\infty}\frac1N
 \|\mathcal E_{U_N}(B_\chi)\|_{\rm HS}^2
\le\frac{c-c^2}{T}.
$$

Now let T tend to infinity, after N has been sent to infinity with T
fixed. This proves Theorem B with no exchange of unproved long-time
limits. No simplicity or minimum-gap estimate is used.

Every eigenvector lies in a single spectral block, so its diagonal
expectation of B_chi equals that of E_(U_N)(B_chi). The sum of squared
diagonal entries in any orthonormal eigenbasis is at most the full
Hilbert-Schmidt norm squared. Formula (1.5) follows, uniformly over the
choice of basis within degenerate eigenspaces. Chebyshev's inequality
then proves the stated zero-density conclusion for almost-old vectors.

By finite Fourier inversion over G, another equivalent consequence is

$$
\frac1N\|\mathcal E_{U_N}(T_g)\|_{\rm HS}^2\to0
\qquad(g\ne0).
$$

This controls the fixed finite group of macroscopic arithmetic Weyl
translations as observables; it is stronger than controlling only the
diagonal in one arbitrarily selected eigenbasis.

## 9. What has and has not been resolved

This pass proves the previously missing all-iterate classical
nonintertwining statement, then actual quantum covariance for every
fixed iterate, then basis-independent arithmetic quantum variance.
The proof of the classical statement is uniform over r; the
semiclassical trace limit is asserted separately for each fixed r.

The conclusion rules out a positive-density eigenbasis supported or
almost supported in a fixed canonical arithmetic sector. It also
handles possible eigenvalue multiplicities through the full commutant
projection. These are genuine results for the specified family, not
properties transferred from a random surrogate.

They do not establish H_diag. In particular, none of (2.8), the
analytic fixed-set trace argument, or their combination has a proved
error bound suitable for r proportional to N. No estimate on the
weighted higher products of Tr(U_N^n) required by H_diag is supplied.
The point-process limit therefore remains unproved, as does a
counterexample to H_diag.

## 10. Frozen input and audit trail

The preceding self-contained Weyl/Egorov and normalized-trace lemmas are
in

`/workspace/scratch/e111873eea6c/research_round2_2026_10_20/arithmetic_oldspace_escape.md`

with SHA-256
`596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a`.
That frozen file was not modified. The family itself is exactly the
one specified by the user, including the modular half and rational
tau. The new proof of Sections 3-6 is independent of any statistical
or genericity assumption.

The discounted error estimate and the two nonzero Fourier coefficients
were independently checked by the parent researcher before the full
report was written. The executable r=2 and numerical-constant check
used exact integer, Fraction, and Q(sqrt(2)) arithmetic. All final
inequalities concerning tau are rational inequalities; no proxy for
tau or large-N numerical experiment is used.
