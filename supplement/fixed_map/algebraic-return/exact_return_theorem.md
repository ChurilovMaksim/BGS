# Exact arithmetic returns at algebraic kick strength

Research continuation from git `e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`
and `../report-audit-20260919/checkpoint.json`, 19 September 2026.
This is a project deduction from Lindemann--Weierstrass, not a new
transcendence theorem, a priority claim, or a BGS proof. No commit or push.

## 1. Scope and external input

The original family is retained exactly:

\[
 U_N=\exp(i\tau N A_N)M_N,\qquad \tau=10^{-80},\qquad
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
\]

Here N is odd, M has the negative cat kernel
\(N^{-1/2}e_N[-8^{-1}(3x^2-2xy+3y^2)]\), and
\(e(kq+lp)\mapsto T_N(l,k)\), with modular midpoint. In particular
\(M T(v)M^*=T(Sv)\). All entries of A and M are algebraic. This follows
from the rational Gaussian Fourier coefficients, roots of unity and
the algebraicity of \(\sqrt N\). No assumption that the eigenvalues of A
are rational or distinct is needed.

The external input is the linear-independence form of
Lindemann--Weierstrass: exponentials of distinct algebraic numbers are
linearly independent over the algebraic numbers. Checked source:
J.-H. Evertse, *Transcendence results*, Theorem 4.8, printed p.48
(PDF p.4), [lecture notes](https://pub.math.leidenuniv.nl/~evertsejh/dio15-4.pdf).
The notes provide a proof. This theorem is imported, not formalized here.

This use depends on the exponent being **i times a nonzero algebraic
number times A**. It is not automatically applicable to the auxiliary
f_star convention `exp(-2*pi*i*kappa*N*Op(f_star))` at algebraic kappa.

## 2. Algebraic specialization lemma

Let \(F(z)=\sum_{\gamma\in E}c_\gamma e^{i\gamma z}\), where E is a
finite set of distinct real algebraic numbers and the coefficients are
algebraic. If \(F(\epsilon)=0\) for a nonzero algebraic real epsilon,
then \(F\equiv0\): apply the cited theorem to \(i\epsilon\gamma\).

Products and sums of these functions remain of this form after collecting
equal frequencies. Thus a polynomial relation over the algebraic numbers
between finitely many such functions at epsilon is an identity in z.
There is **no polynomial dependence on z in the coefficients**. For
example `z-epsilon` is not covered by this lemma.

For algebraic Hermitian A, its distinct eigenvalues \(a_j\) are algebraic,
and the projectors
\[
 P_j=\prod_{k\ne j}(A-a_kI)/(a_j-a_k)
\]
have algebraic entries. The expansion
\(e^{izA}=\sum_j e^{iza_j}P_j\) therefore puts every entry of
\(U(z)^m=(e^{izA}M)^m\) in the lemma, for each positive integer m.

## 3. An invariant average rules out every algebraic projective return

For a unitary M put
\[
 E_M(A)=\sum_j Q_j A Q_j,
\]
where the Q_j are its distinct spectral projectors. This is the Cesaro
average of \(M^r A M^{-r}\). If \(M^R\) is scalar, it equals the finite
average over \(0\le r<R\).

**Theorem 1.** Suppose A is Hermitian, M is unitary, their entries are
algebraic, and \(E_M(A)\) is nonscalar. For every nonzero real algebraic
epsilon and every positive integer m, \(U(\epsilon)^m\) is not a scalar
multiple of any matrix with algebraic entries. In particular
\(U(\epsilon)^m\ne cI\) for every complex scalar c.

**Proof.** If \(U(\epsilon)^m=cB\), with B algebraic, every cross-entry
relation \(B_{kl}(U^m)_{ij}-B_{ij}(U^m)_{kl}=0\) is an identity by
Section 2. Selecting a nonzero entry of B shows that \(U(z)^m=h(z)B\)
for all z. At zero, B is proportional to \(M^m\). Consequently
\(U(z)^mM^{-m}=g(z)I\), with \(g(0)=1\). Differentiation at zero gives
\[
 iD_m=g'(0)I,\qquad D_m=\sum_{r=0}^{m-1}M^r A M^{-r}.
\]
But \(E_M(D_m)=m E_M(A)\) is nonscalar. Contradiction. QED.

The theorem also excludes exact returns to any algebraic change of basis
of a metaplectic or Weyl matrix, up to a global phase. It says nothing
quantitative about distance to these sets, which are dense.

**Spectral consequence.** At least one eigenvalue ratio of
\(U(\epsilon)\) is transcendental.

Proof: set \(a=\operatorname{Tr}A/N\) and \(W(z)=e^{-iaz}U(z)\).
Its determinant is the constant algebraic number \(\det M\). If all
eigenvalue ratios of W(epsilon) were algebraic, the determinant would
force all its eigenvalues, and therefore all characteristic coefficients,
to be algebraic. Section 2 applied to each coefficient minus its value
at epsilon makes the characteristic polynomial constant in z, equal to
that of M. For real z, W(z) is unitary. If the distinct eigenvalues of M
are \(\mu_j\), the projectors of W(z) are
\[
 Q_j(z)=\prod_{k\ne j}(W(z)-\mu_k I)/(\mu_j-\mu_k).
\]
Differentiate \(W(z)Q_j(z)=\mu_j Q_j(z)\) at zero and sandwich by
\(Q_j(0)\). The derivatives of Q cancel, so
\(Q_j(0)W'(0)Q_j(0)=0\). Since \(W'(0)=i(A-aI)M\), this gives
\(Q_j(0)(A-aI)Q_j(0)=0\). Summation would give \(E_M(A)=aI\), a
contradiction. This argument allows repeated eigenvalues of M.

It does not assert that every eigenvalue ratio is transcendental or that
U has simple spectrum.

## 4. A uniform witness for the actual frozen symbol

In the raw modular Weyl expansion
\[
 A_N=\tfrac1{10}I+\sum_v a_vT_N(v),
\]
the coefficients at \(v_\pm=(0,\pm7)\) equal \(9/20\). For the remaining
30 coefficients, direct rational Fourier multiplication gives
\[
 \sum_{v\ne v_+,v_-}\max(-\Re a_v,0)=14/125.
\]
These statements also hold after multiplying coefficients by
\((-1)^{v_1v_2}\), which is the ordinary-midpoint quantization expressed
in the modular basis. This conversion is made on the original integer
labels **before** reduction modulo N: parity of a residue representative
is not a well-defined sign convention for odd N. On integer labels the
signs are invariant under S, since S=I mod 2.

Let \(N\ge3\) be odd, \(N\ne7\), and let O be the S-orbit of
\((0,7)\) in \((\mathbb Z/N)^2\). O does not contain zero. Define
\[
 L_O(B)=\sum_{v\in O}\frac1N\operatorname{Tr}(T_N(v)^*B).
\]
Weyl orthogonality and covariance show that this functional kills I and
is invariant under conjugation by M. Reduction of the Fourier indices
modulo N may produce aliases, but
\[
 \Re L_O(A_N)\ge9/20-14/125=169/500>0.                 \tag{1}
\]
Indeed the positive dominant coefficient is in the orbit; the other
dominant coefficient either adds a positive term or is outside it. No
subset of the remaining coefficients has a more negative real sum than
their total negative real mass. This includes small and composite N.
Thus \(L_O(E_M(A_N))\ne0\), proving nonscalarity for every such N.

**Corollary for the frozen model.** For every odd \(N\ge3\), \(N\ne7\),
every nonzero real algebraic tau (in particular \(10^{-80}\)), and every
positive integer m,
\[
 \boxed{\ (e^{i\tau N A_N}M_N)^m\ne cB
 \quad\text{for every algebraic-entry matrix B and scalar c}.\ }
\]
In particular there is no exact scalar return, at any time. At least one
eigenvalue ratio is transcendental. Both midpoint conventions satisfy
this corollary with their respective A_N; it does not identify their
spectra.

The raw N=7 exception is real: its Jacobi form has r(j/7)=0 at every
site, so A_7=I. Moreover S has order three modulo 7, hence M_7^3 is
scalar and U_7^3 is scalar at every coupling. N=1 is also necessarily
excluded. This is not an exception at every multiple of seven.

## 5. Algebraic symmetries and a separate simplicity criterion

For any algebraic matrix B and nonzero algebraic real epsilon,
\[
 [B,U(\epsilon)]=0\quad\Longleftrightarrow\quad
 [B,A]=[B,M]=0.                                         \tag{2}
\]
In fact specialization turns the left side into an identity in z.
Its value and derivative at zero give the two commutators on the right.
The converse follows by exponentiation. Equation (2) is a reduction of
the **algebraic-entry** commutant only. Arbitrary spectral projectors
still commute with U; no claim of a scalar full commutant is made.

Let G be a nonzero algebraic scalar multiple of M, and let
\(E=E_M(A)\). If G+tE has simple spectrum for some real rational t,
then the restriction of E to each eigenspace of M has simple spectrum.
The derivatives of the corresponding eigenphases of U(z) at z=0 are
exactly these restricted eigenvalues (equivalently, expand the
characteristic determinant in each separated cluster at first order).
Explicitly, at an eigenvalue mu of M, put
\(\lambda=\mu(1+izy)\). In the decomposition into its eigenspace and
the other eigenspaces, the other block of \(\lambda I-U(z)\) stays
invertible. The Schur complement on this eigenspace is
\(i\mu z(yI-PAP)+O(z^2)\). Simple eigenvalues of PAP give distinct
roots by the implicit function theorem. Distinct original clusters
stay separated by continuity.
Thus U(z) has simple spectrum for sufficiently small nonzero real z.
Its characteristic discriminant is an exponential polynomial of
Section 2 and is not identically zero. It cannot vanish at any nonzero
algebraic real epsilon.

This gives a **finite, exact certificate** for a specified dimension:
reduce G+tE modulo a prime splitting the cyclotomic coefficients and
not dividing any denominator, and verify that its characteristic
polynomial is squarefree. A nonzero reduced discriminant proves that
the algebraic characteristic discriminant before reduction is nonzero.
This finite test does not establish simplicity at all dimensions.

## 6. The quantitative barrier is still present

Neither exact nonreturn nor simplicity supplies the Fejer-energy
estimate or CUE-subtracted Heisenberg trace bounds needed for BGS.
For example A_N=diag(0,1,...,N-1)/N^3 and M_N=I have rational entries.
At epsilon=1 every distinct eigenvalue ratio of exp(i A_N) is
transcendental, the spectrum is simple, and Theorem 1 excludes every
algebraic projective return. Nevertheless all N eigenvalues lie in an
arc of length less than 1/N^2, so the number of close ordered pairs
divided by N is N-1. This is a control on the proposed inference, not
a counterexample in the frozen quantization class.

The existing huge-dimensional *approximate* return certificates for
the frozen model are fully consistent with the corollary. No uniform
lower bound on an exponential polynomial follows from the qualitative
Lindemann--Weierstrass input used here. The original all-k fixed-map
target remains open.

Two further controls identify essential hypotheses. For
\(A=\operatorname{diag}(1,-1)\) and M the two-coordinate swap, A is
nonscalar but \(E_M(A)=0\); indeed \((e^{izA}M)^2=I\) for all z.
For \(A=\operatorname{diag}(0,1),M=I\), the transcendental coupling
\(z=2\pi\) gives an exact return. Neither control satisfies Theorem 1's
full hypotheses.

## 7. Exact finite simplicity certificates and their verification

The independently reconstructed 33 Fourier coefficients (including the
mean) agree with the earlier frozen-symbol code. Both gauge negative-mass
identities, the raw N=7 scalar exception, and the invariant orbit witness
were replayed with rational arithmetic. The all-N conclusion is proved by
(1), not extrapolated from these finitely many checks.

In each row below the reduction is in a splitting prime
\(p\equiv1\pmod{4N}\). Set \(G=\sqrt N M\), so its entries are roots
of unity without a normalization denominator. The chosen weight t is
recorded in `certificates.json`. The certificate proves that G+tE has
squarefree characteristic polynomial of degree N.

| Quantization | N | p | Order of S modulo N |
|---|---:|---:|---:|
| Raw modular | 3 | 13 | 4 |
| Raw modular | 5 | 41 | 6 |
| Raw modular | 9 | 73 | 12 |
| Raw modular | 15 | 61 | 12 |
| Raw modular | 21 | 337 | 12 |
| Raw modular | 41 | 821 | 5 |
| Raw modular | 239 | 1913 | 7 |
| Raw modular | 1393 | 5573 | 9 |
| Ordinary midpoint | 7 | 29 | 3 |
| Ordinary midpoint | 41 | 821 | 5 |

It follows that U(epsilon) has simple spectrum at **every nonzero real
algebraic epsilon** in these specified dimensions and conventions.
This includes the original frozen epsilon=N/10^80 in the raw rows.
It is not a claim that floating arithmetic resolves those splittings,
nor that all odd dimensions have been covered.

The generator uses a finite-field scalar Krylov sequence to propose a
monic polynomial q of degree N. Its algorithm is not trusted by the
replay. The certificate contains two vectors u,v and q, and the replay
checks exactly:

1. q(B)v=0, for the independently assembled B=G+tE;
2. the numerator p(t) of \(u^T(tI-B)^{-1}v=p(t)/q(t)\), computed from
   the first N scalar moments, is coprime to q;
3. q is coprime to its formal derivative.

Why this certifies the characteristic polynomial: the first identity
proves the rational-resolvent expression by multiplying the formal
series at infinity by q. The adjugate formula also writes that resolvent
with denominator \(\chi_B\). Coprimality in step 2 implies
\(q\mid\chi_B\). Both are monic of degree N, hence equal. Step 3
then proves a nonzero discriminant. Thus neither a probabilistic rank
assumption nor correctness of the candidate-generation algorithm is a
logical dependency of a passing certificate.

`replay.cpp` reconstructs the matrix differently: it adds each iterated
Fourier mode before collecting, checks the two generating Weyl covariance
identities, and implements its own integer matrix products and polynomial
Euclidean algorithm. Every certificate passed both Python and C++.
All matrix-vector accumulation bounds are checked against int64 overflow.
The true raw N=7 exception fails the degree-N certificate; changing one
polynomial coefficient is rejected by both replayers. Some initial prime,
weight, or vector choices failed to produce a certificate; these failures
are retained in `simple_spectrum.json` and imply no spectral conclusion.

Reproduction from the repository root:

```bash
OPENBLAS_NUM_THREADS=1 python build/algebraic-return/simple_spectrum.py
python build/algebraic-return/export_certificates.py
g++ -std=c++20 -O3 -Wall -Wextra -Werror build/algebraic-return/replay.cpp -o build/algebraic-return/replay
build/algebraic-return/replay build/algebraic-return/certificates.txt
```

Review: the general specialization, projective-return, spectral-ratio,
orbit-witness and simplicity implications received a separate internal
derivation. This is not external peer review or Lean verification. The
available environment did not provide a Lean executable; no compilation
claim is made. `checkpoint.json` identifies all inputs and artifacts.
