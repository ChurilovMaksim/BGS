> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_banded_time_reversal.md`. Embedded SHA256: `39d017750473ee6779fc52656613b06dee5cd5591e4dbd288c64c10904cae6dd`.
> [Thematic guide](../../topics/symmetry.md).

# Exact exclusion of arbitrary common time reversal

Research continuation, 20 October 2026. The matrices are precisely those in
the question; the actual parameter remains tau=10^(-80). This note supplies
a structural theorem for every odd N>=75. It does not prove H_diag or an
estimate of signed trace sums at times proportional to N.

## 1. Main results

Write A=A_N, M=M_N and x_N=pi/N. Define the real number

$$
I_N=\operatorname{Tr}(A M A^2M^*)
       -\operatorname{Tr}(A M^* A^2M).
\tag{1.1}
$$

**Theorem 1.** For every odd N>=75,

$$
\boxed{\frac{I_N}{N}
 =\frac{3}{50\,000\,000}
  (2-\cos(7x_N))(4\cos x_N-\cos(2x_N))
 \ge\frac{3}{20\,000\,000}>0.}
\tag{1.2}
$$

Consequently there is no antiunitary D, of any form, satisfying both

$$
DAD^{-1}=A,\qquad DMD^{-1}=M^{-1}.
\tag{1.3}
$$

This includes antiunitaries outside the Weyl-normalizer and monomial
classes. It also applies in dimensions divisible by 7, where A splits
into seven coordinate Jacobi paths.

The obstruction is uniform in operator norm. For every antiunitary D put

$$
\delta_A=\|DAD^{-1}-A\|,\qquad
\delta_M=\|DMD^{-1}-M^{-1}\|.
$$

Then, with R=59/50,

$$
3R^2\delta_A+2R^3\delta_M\ge\frac{3}{20\,000\,000},
\qquad
\boxed{\max(\delta_A,\delta_M)>2\cdot10^{-8}.}
\tag{1.4}
$$

**Theorem 2.** Let z be any nonzero real algebraic number and
U(z)=exp(izNA)M. There is no antiunitary D=JK whose linear part J is
proportional to a matrix with algebraic entries and which satisfies

$$
DU(z)D^{-1}=\eta U(z)^{-1}
\tag{1.5}
$$

for any scalar eta. Here K is coordinate conjugation. No regularity of D
as a function of z is assumed; it may be chosen at this single parameter.
In particular, (1.5) is impossible in this algebraic class at the original
tau=10^(-80).

Every finite unitary has an antiunitary reverser obtained from an
orthonormal eigenbasis. Theorem 2 says that, for this family and these
dimensions, the linear part of such a reverser cannot be proportional to
an algebraic matrix. It does not deny the spectral-basis construction.

A second exact identity is

$$
\boxed{\frac{\operatorname{Tr}(A^3)}N
 =-\frac{273}{20000}
 +\frac{3\cos(8x_N)+81\cos(7x_N)
          +3\cos(6x_N)-9\cos x_N}{400000}
 \le-\frac{1341}{100000}<0.}
\tag{1.6}
$$

It implies that no unitary or antiunitary conjugates A to -A. Together
with the same algebraic parameter argument, it excludes algebraic
projective unitary reversers and algebraic projective antiunitary
commuters of U(z). These additional conclusions are proved in Section 7.

## 2. Exact Weyl signs and the no-alias range

For integer k,l set

$$
(W_N(k,l)u)(j)
 =\exp\left(\frac{2\pi i k(j+l/2)}N\right)u(j+l).
$$

These ordinary half-integer phases are used only in this auxiliary
definition. The original quantization still uses modular inverses. Since
the inverse of 2 modulo odd N is represented by (N+1)/2,

$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
\tag{2.1}
$$

Thus A=Op_N(a), where

$$
a(q,p)=V(q)+\gamma R(q)e^{2\pi ip}
                    +\overline\gamma R(q)e^{-2\pi ip},
\tag{2.2}
$$

$$
\begin{split}
V(q)&=\frac9{10}\cos(14\pi q)
 +\frac1{10}(1-\cos(14\pi q))\cos(2\pi q)
 +\frac1{100}r(q)\sin(2\pi q),\\
R(q)&=r(q+1/2)=(1+\cos(14\pi q))(1-\cos(2\pi q)),\\
\gamma&=\frac{e^{-i\alpha_0}}{200}
       =\frac{-3-4i}{1000}.
\end{split}
\tag{2.3}
$$

The Fourier support of a lies in |k|<=9, |l|<=1 and has 32 members.
The q-only coefficient mass is bounded by .9+.2+.04, and the p-dependent
mass by .04. Therefore

$$
\|A\|\le\sum_{k,l}|a_{kl}|\le59/50.
\tag{2.4}
$$

Multiplication and the cat conjugation are exactly

$$
W_N(k,l)W_N(k',l')
 =e^{\pi i(lk'-kl')/N}W_N(k+k',l+l'),
\tag{2.5}
$$

$$
MW_N(k,l)M^*=W_N(3k+2l,4k+3l).
\tag{2.6}
$$

For completeness, multiply the given kernel of M by the diagonal Weyl
generator and its adjoint. The additive character sum forces the output
coordinate to be shifted by 4k and gives T_N(4k,3k). Doing the same for
the shift generator gives T_N(3l,2l). The Weyl multiplication rule then
gives the conjugation for T_N. Passing to W_N introduces no remaining
sign, because
(3k+2l)(4k+3l)-kl is even. This proves (2.6) directly from the prescribed
matrix, including its modular phases.

Put B=MAM^*. Its Fourier support lies in |k|<=27, |l|<=36. The total
frequency bounds for ABB and AAB are respectively (63,73) and (45,38).
For N>=75, a frequency in either range is divisible by N in both
coordinates only if both coordinates are zero. Moreover
Tr(W_N(k,l))=0 unless N divides k and l, and Tr W_N(0,0)=N.
Hence in all the cubic traces below there is no frequency alias.
This is why the uniform threshold is N>=75; no numerical large-N
approximation is used.

By cyclicity,

$$
I_N=\operatorname{Tr}(AB^2)-\operatorname{Tr}(A^2B).
\tag{2.7}
$$

## 3. Computing the asymmetric cubic invariant

The nonzero coefficients of R are

$$
R_0=1,\quad R_{\pm1}=-1/2,\quad R_{\pm7}=1/2,
\quad R_{\pm6}=R_{\pm8}=-1/4.
\tag{3.1}
$$

For an index (k,l) in the support of a, the second coordinate of
S^T(k,l) is 4k+3l. The only nonzero such indices having
|4k+3l|<=2 are (1,-1) and (-1,1). Thus only frequencies (1,1) and
(-1,-1) of B can contribute to Tr(A^2B). Applying the same argument to
S^{-T} shows that only (1,-1),(-1,1) contribute after rewriting
Tr(AB^2)=Tr((M^{-1}AM)A^2).

Let x=pi/N and

$$
Q(x)=\sum_j V_j R_{1-j}\cos(jx),
\tag{3.2}
$$

where V_j are the Fourier coefficients of V. The only contributions to
the coefficient of A^2 at (1,1) have l-indices 0,1 in either order.
Equation (2.5) gives the opposite phases exp(ijx) and exp(-ijx), so that

$$
(a\mathbin{\#_N}a)_{1,1}=2\gamma Q(x),\qquad
(a\mathbin{\#_N}a)_{1,-1}=2\overline\gamma Q(x).
\tag{3.3}
$$

Here the notation denotes the exact Weyl product of these finite
polynomials, not an asymptotic expansion. Since a_(1,1)=-gamma/2 and
a_(1,-1)=-bar(gamma)/2, the two pairs of contributing frequencies give

$$
\frac{\operatorname{Tr}(A^2B)}N=-2\operatorname{Re}(\gamma^2Q),
\qquad
\frac{\operatorname{Tr}(AB^2)}N=-2\operatorname{Re}(\gamma^2\overline Q).
\tag{3.4}
$$

Now gamma^2=(-7+24i)/10^6, hence

$$
I_N/N=-96\cdot10^{-6}\operatorname{Im}Q(x).
\tag{3.5}
$$

The necessary imaginary q-Fourier coefficients are

| j>0 | Im V_j |
|---|---:|
| 1 | -1/200 |
| 2 | -1/400 |
| 5 | -1/800 |
| 6 | -1/400 |
| 8 | 1/400 |
| 9 | 1/800 |

All other Im V_j for j>0 vanish, and Im V_-j=-Im V_j. Inserting these
and (3.1) into (3.2) gives exactly

$$
\operatorname{Im}Q(x)=\frac1{3200}
 [-16\cos x+4\cos(2x)-\cos(5x)
   +4\cos(6x)+4\cos(8x)-\cos(9x)].
\tag{3.6}
$$

The bracket with opposite sign is

$$
\begin{split}
&\cos(9x)+\cos(5x)-4\cos(8x)-4\cos(6x)
  -4\cos(2x)+16\cos x\\
&\hspace{12mm}=2(2-\cos(7x))(4\cos x-\cos(2x)).
\end{split}
\tag{3.7}
$$

This proves the equality in (1.2). For N>=3, c=cos(pi/N) lies in
[1/2,1]. Thus 4c-cos(2pi/N)=1+4c-2c^2>=5/2, whereas
2-cos(7pi/N)>=1. This proves its stated positive lower bound.

## 4. Why every common antiunitary is excluded

For Hermitian A, both traces in (1.1) are real: for example
MA^2M^* is Hermitian, and the trace of a product of two Hermitian
matrices is real. An antiunitary conjugates the trace of a matrix and
preserves product order. If D satisfies (1.3), it therefore maps the
first real trace in (1.1) to the second. They must coincide, contrary
to (1.2). This proof imposes no algebraicity or geometric condition on D.

For the quantitative assertion, set A'=DAD^{-1}, M'=DMD^{-1}.
The first trace in (1.1) equals
Tr(A'M'(A')^2(M')^*) because that trace is real. Telescope the five
factors in this word against A M^* A^2M, treating the two A's in A^2
as separate factors. There are three errors bounded by R^2 delta_A
and two bounded by R^3 delta_M after dividing the trace by N.
Every intermediate A or A' has norm at most R; every M factor is
unitary. This proves (1.4)'s first inequality. Finally

$$
3R^2+2R^3=\frac{932908}{125000}<7.464,
\quad
\frac{3/(20\,000\,000)}{3R^2+2R^3}
 =\frac3{149265280}>2\cdot10^{-8}.
\tag{4.1}
$$

## 5. The exact odd moment

Let t=2pi q, C=cos(7t), c=cos t, s=sin t, and

$$
w(t)=c/10+(1+c)s/100,\qquad V=.9C+(1-C)w.
$$

The frequencies of w^j for j<=3 have absolute value at most 6.
Consequently averaging a product of w^j with powers of C factors
through the zero Fourier coefficient of the latter. Elementary
trigonometric integration gives

$$
\langle w\rangle=0,\quad
\langle w^2\rangle=81/16000,\quad
\langle w^3\rangle=3/400000,
$$

$$
\langle V^3\rangle
 =-\frac{27}{10}\langle w^2\rangle
   +\frac52\langle w^3\rangle=-273/20000.
\tag{5.1}
$$

The Jacobi diagonal is V(j/N) and its off-diagonal entry is
gamma R((j+1/2)/N). Expanding the diagonal entries of A^3 gives

$$
\frac1N\operatorname{Tr}(A^3)
 =\langle V^3\rangle
 +3|\gamma|^2\int_0^1
  [V(q-1/(2N))+V(q+1/(2N))]R(q)^2\,dq.
\tag{5.2}
$$

The discrete averages equal these integrals because their frequencies
are less than N. The expansion counts each path with one diagonal
step and two opposite nearest-neighbor steps three times; no triangle
of three off-diagonal steps closes for N>=75.

The real coefficients of V that meet R^2 are
Re V_1=1/20, Re V_6=Re V_8=-1/40, Re V_7=9/20, with equal negative
coefficients. Directly from R^2=(1+cos(7t))^2(1-cos t)^2,

$$
(R^2)_{\pm1}=-3/2,\quad
(R^2)_{\pm6}=(R^2)_{\pm8}=-1,\quad
(R^2)_{\pm7}=3/2.
$$

Since |gamma|^2=1/40000, substitution in (5.2) proves (1.6).
The absolute sum of its four nonconstant cosine coefficients is
96/400000, giving the upper bound -1341/100000. If a unitary or
antiunitary sent A to -A, it would send the real trace Tr A^3 to its
negative without changing its value. This is impossible.

## 6. Transferring a fixed algebraic product reverser

All entries of A,M,M^{-1} are algebraic. If J is proportional to an
algebraic matrix and is unitary, its scalar can be removed and the
result normalized by an algebraic positive square root. Thus the same
conjugation has a unitary representative J with algebraic entries.

For D=JK antiunitary, write A_D=J bar(A)J^* and M_D=J bar(M)J^*.
For complex z define the holomorphic continuation

$$
X(z)=e^{-izNA_D}M_D,\qquad
Y(z)=M^{-1}e^{-izNA}.
\tag{6.1}
$$

For real z, X(z)=DU(z)D^{-1} and Y(z)=U(z)^{-1}.
For any two matrix-entry locations u,v, the projective minor

$$
F_{u,v}(z)=X_u(z)Y_v(z)-X_v(z)Y_u(z)
\tag{6.2}
$$

is a finite exponential polynomial with algebraic coefficients and
algebraic frequencies. Indeed, the distinct eigenvalues a_j of the
algebraic Hermitian matrix A are algebraic, and its spectral projectors
are the algebraic matrices
E_j=product_(h!=j)(A-a_h I)/(a_j-a_h). The same assertion holds for
A_D. Expanding the exponentials proves the stated form of (6.2).

The precise external theorem used is the Lindemann-Weierstrass
linear-independence theorem, Theorem 3.2 in S. A. Popescu,
*A Simple and Self-contained Proof for the Lindemann-Weierstrass
Theorem*, published chapter
[DOI 10.1007/978-3-031-51959-8_16](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16).
Its statement was checked in the author's
[manuscript, Theorem 3.2, PDF page 14](https://arxiv.org/pdf/2306.14352).
It applies to distinct complex algebraic exponents with algebraic
coefficients. After equal frequencies in (6.2) are collected, their
products with the nonzero algebraic parameter z are still distinct
and algebraic. Therefore F_(u,v)(z)=0 at that parameter forces every
collected coefficient to vanish. Thus every minor in (6.2) vanishes
identically if (1.5) holds at the given parameter. This checks all
hypotheses of the published theorem.

Near z=0, X(z)=eta(z)Y(z), with eta holomorphic and nonzero: choose a
nonzero entry of the invertible Y(0), take the ratio there, and use
the vanishing minors for every other entry.

The exact quadratic trace of the bare cat is nonzero. In fact

$$
\operatorname{Tr}M=N^{-1/2}\sum_{j\bmod N}e_N(-\overline2 j^2),
\qquad |\operatorname{Tr}M|^2=1.
\tag{6.3}
$$

To prove the second equality, square the absolute value and change
variables to u=j-k, v=j+k; this is a bijection since 2 is invertible.
The resulting double sum of e_N(-bar(2)uv) equals N, since its
v-sum vanishes unless u=0. Division by N gives (6.3).

At zero parameter M_D=eta(0)M^{-1}. Taking traces gives
bar(Tr M)=eta(0)bar(Tr M), hence eta(0)=1. Differentiating X=eta Y
at zero and multiplying on the right by M gives

$$
-iN A_D=\eta'(0)I-iN M^{-1}AM.
\tag{6.4}
$$

Since A is Hermitian, Tr A_D=Tr A is real; taking the trace of
(6.4) shows eta'(0)=0. Therefore

$$
A_D=M^{-1}AM,\qquad M_D=M^{-1}.
\tag{6.5}
$$

The antiunitary C=MD then satisfies CAC^{-1}=A and CMC^{-1}=M^{-1}.
Theorem 1 excludes it. This proves Theorem 2. Notice that it is C=MD,
not necessarily D itself, that preserves A.

## 7. Two additional algebraic symmetry exclusions

The projective-minor argument also applies to unitary J and to a
commuting relation. No restriction on the scalar at the original
parameter is needed. The local scalar is fixed by the nonzero trace
of M in the same way; the trace derivative fixes its first derivative.

For an algebraic unitary projective reverser,

$$
J U(z)J^{-1}=\eta U(z)^{-1},
$$

the zero-parameter relation is JMJ^{-1}=eta_0 M^{-1}, where eta_0
is nonzero. Differentiating after eliminating this constant scalar
gives JAJ^{-1}=-M^{-1}AM, since Tr A=0 for N>=75. Consequently
MJ conjugates A to -A, contrary to (1.6).

For an algebraic antiunitary projective commuter,

$$
D U(z)D^{-1}=\eta U(z),
$$

the same derivative computation gives DAD^{-1}=-A, again because
Tr A=0. This contradicts (1.6). These arguments impose algebraicity
only on the linear part of the intertwiner up to scalar.

No conclusion about arbitrary algebraic unitary commuters is obtained
here. Such a conclusion would require a separate analysis of the common
commutant of A and M.

## 8. Exact certificate and boundaries of the result

The proof above evaluates (1.2) and (1.6) by hand using finite Fourier
coefficients. The independent executable
`arithmetic_banded_time_reversal.py` also constructs all 32 prescribed
coefficients as Gaussian integers at scale 4000, applies the modular
half-to-real-half signs, multiplies the three Weyl factors, and collects
their exact Laurent coefficients. There are 32 zero-frequency triples
for ABB and for AAB, and 414 for AAA. It verifies the trigonometric
factorization by rational Laurent-polynomial multiplication and writes
`arithmetic_banded_time_reversal.json`. Its inequality checks use exact
rational arithmetic. It performs no eigenvalue experiment.

Inputs read without modification:

| File | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/verify_affine_symmetry.py` | `ded7875ca635745da21bbaef9d523cc24c2d57a3985965f84b82caee1a51626e` |
| `../research_continuation_2026_10_20/affine_reversal_and_crt_obstructions.md` | `856f7e0d7373e1b3c260b20477969a12e3e78886836b11fd4eac9ddd9cc7642c` |
| `arithmetic_second_order_proof.md` | `7d6a0a28d67ab43efa4e444c26ccd25d9d981925c9af80604f3bf608e17c7770` |

The structural novelty relative to those inputs is the removal of all
geometric restrictions on a common antiunitary, its uniform operator-norm
obstruction, and the exclusion of every algebraic actual-product
antiunitary reverser. None supplies a bound on the quantum traces at
times of order N. The first missing estimate for H_diag remains the
weighted signed trace-product cancellation stated in the original task.
Finite bandwidth, the seven exact path cuts, and the positivity of the
invariant above do not establish that cancellation.
