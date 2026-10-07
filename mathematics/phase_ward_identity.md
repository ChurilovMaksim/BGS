# Stationary phase diffusion and the exact absorbed overlap defect

Author derivation, 7 October 2026. Read-only BGS base d37c92e563d10d25bb1d6ab85bedffc1f160f773. This is a full balanced-pair reduction through eigenvector overlaps, not a proof that the overlap defect vanishes. It keeps absorption strictly positive and does not invoke boundary-delay second moments.

Prior search: canonical mathematics, supplements and record searched for phase Brownian motion, phase Ward identities, eigenphase diffusion and overlap kernels. The nearest maintained facts are the normalized unitary heat generator and pair heat formula in mathematics/heisenberg_pair_heat_formula.md and circular_dyson_actual_start.md. Those concern full unitary Brownian motion and do not assert stationarity of the coordinate-phase ensemble under it.

## 1. Exact stationary process

Fix U in U(N). Let D(0) have independent uniform diagonal phases, and let B_a(t) be independent standard real Brownian motions. Put

V(t)=diag(exp(i B_a(t))) D(0) U.

The law of V(t) is the original law of DU for every t. This is only phase diffusion, not Haar/unitary Brownian motion. On a simple spectral chart write

V psi_j=exp(i theta_j) psi_j,
w_ja=|psi_j(a)|²,
G_jk=sum_a w_ja w_ka.                                    (1)

G is real symmetric, positive semidefinite, entrywise nonnegative, and each row sums to one. G_jj is the inverse participation ratio. In particular, G is not the initial coordinate transition matrix P=|U|².

For a fixed Hermitian H, ordinary second-order eigenvalue perturbation along exp(itH)V gives

theta'_j=H_jj,
theta''_j=sum_(k != j)|H_jk|² cot((theta_j−theta_k)/2),     (2)

where H is expressed in the eigenbasis of V. To check the sign, use

(lambda_j+lambda_k)/(lambda_j−lambda_k)
   =−i cot((theta_j−theta_k)/2).

Apply (2) to H=E_aa and Itô's formula. Exactly,

d theta_j=sum_a w_ja dB_a
       +(1/2)sum_(k != j)G_jk cot((theta_j−theta_k)/2)dt,
d theta_j d theta_k=G_jk dt.                             (3)

For a smooth symmetric class function F of the angles, stationarity therefore gives

0=E[(1/2)sum_jk G_jk partial_j partial_k F
     +(1/4)sum_(j != k) G_jk cot((theta_j−theta_k)/2)
                              (partial_j−partial_k)F].   (4)

The cotangent term is written in its symmetrized form. At a collision the gradient difference cancels the apparent pole for smooth symmetric F; the original matrix derivative formulation is nonsingular. No inverse eigenvalue gap is estimated separately.

For completeness, the simple spectral locus has full phase measure. A diagonal Hermitian perturbation can be chosen to have simple compressions on each eigenspace of any starting unitary: the compressed coordinate rank-one forms span a positive frame, and successively choosing distinct, separated coefficients breaks all finite-dimensional multiplicities. Small perturbation then gives a simple member of the phase family. Its discriminant is a nonzero real-analytic function of the phases, whose zero set has measure zero. Formula (4) can alternatively be obtained first with a smooth matrix class function, before passing to local eigenangle charts.

## 2. Exact CUE reference and signed error

For a Haar-distributed complex eigenbasis, the overlap mean is

G^H_jk=(1+delta_jk)/(N+1).                                (5)

This follows from the elementary fourth moments of one Haar unit vector: E|v_a|⁴=2/[N(N+1)] and E|v_a|²|v_b|²=1/[N(N+1)] for a!=b. It is a reference value, not a fact established for DU.

Put E_jk=G_jk−G^H_jk and define

R_E F=(1/2)sum_jk E_jk partial_j partial_k F
      +(1/4)sum_(j != k)E_jk cot((theta_j−theta_k)/2)
                                   (partial_j−partial_k)F. (6)

For translation-invariant F, substituting G^H in (4) gives N/(N+1) times the normalized CUE radial generator

A_N F=(1/(2N))sum_j partial_j² F
      +(1/(2N))sum_(j != k)cot((theta_j−theta_k)/2)partial_jF. (7)

The additional all-ones covariance term is a second derivative in the common angle and vanishes. Consequently

E A_N F=−(N+1)/N E R_E F.                               (8)

This is a signed averaged identity. Neither |E_jk| nor individual cotangent factors are put outside the complete contraction.

## 3. One universal Poisson test gives the entire absorbed pair defect

For fixed s>0 set q=exp(−2s/N) and define the smooth translation-invariant class function

F_(N,s)(V)=N^(-2)sum_(m>=1)q^m |Tr V^m|².                (9)

The fixed-N series and all derivatives converge. Its exact CUE mean is

c_(N,s)=q(1−q^N)/[N²(1−q)²],
which tends to (1−exp(−2s))/(4s²).

Let P_t be normalized full unitary Brownian heat, with E B_t=exp(−t/2)I, and let

Psi_(N,s)=−integral_0^infinity P_t(F_(N,s)−c_(N,s))dt.     (10)

At fixed N this is the unique zero-Haar-mean smooth solution of

A_N Psi_(N,s)=F_(N,s)−c_(N,s).                            (11)

Here A_N is restricted to class functions. Existence and smoothness follow either from the positive spectral gap of the compact unitary heat generator on mean-zero smooth functions or by its Peter-Weyl spectral expansion, positive fixed-N gap, and smoothing. Equation (10) is a definition of a universal test depending on N,s, not on the specific U. It does not insert extra Brownian noise into the phase-ensemble target.

Combining (8) and (11) gives the exact finite-N identity

E_D F_(N,s)(DU)−c_(N,s)
   =−(N+1)/N E_D R_(G−G^H) Psi_(N,s).                   (12)

Thus the desired full balanced Abel limit for every s>0 is equivalent to

E_D R_(G−G^H) Psi_(N,s) →0, for every fixed s>0.          (13)

This is the minimal single-test overlap obligation produced by this route. It does not demand pointwise QUE, a uniform absolute bound on all overlaps, or unregularized delay moments. A theorem controlling the complete signed contraction (13), including its Hessian and cotangent-gradient terms together, would close the full balanced pair transform. It would leave deterministic nonzero-charge terms and higher factorial orders separate.

At Heisenberg Fourier degree the Poisson test is not a fixed low-degree observable. Replacing (13) with fixed-degree overlap moment convergence is not justified.

## 4. How the actual classical gap enters, and where it stops

Let P_ab=|U_ab|², unchanged by left multiplication by D. The eigenvector equation gives, for each j,

w_ja=sum_b P_ab w_jb + c_ja,
c_ja=sum_(b != c)U_ab conjugate(U_ac) psi_j(b) conjugate(psi_j(c)). (14)

Each c_j is real and centered. If ||P−J||op<1, write R=(I−P+J)^(-1). Then exactly

w_j−(1/N)1=R c_j,
G_jk−1/N=<R c_j,R c_k>.                                 (15)

The initial P gap makes R bounded. It supplies no evaluation of the spectrally weighted covariance of the c_j in (13). In particular, it does not prove G_jj≈2/N or G_jk≈1/N near microscopic spectral pairs. The initial reverse kernel Q also is not the kernel G and does not replace this missing joint coherence estimate.

The necessary CUE fluctuation has size 1/N: merely proving w_j→uniform in a weak norm, or G_jk→0, would erase the scale that distinguishes the covariance and drift. The exact Haar reference (5) has diagonal/offdiagonal ratio two; imposing only the common mean 1/N produces the wrong diffusion strength after removing the common angle.

## 5. Cheap controls and current status

- N=1: G=G^H=1, every translation-invariant F is constant, and both sides of (12) vanish.
- Diagonal U: eigenvectors are coordinate vectors, G=I. The phase ensemble is Poisson at microscopic scale, and the overlap error does not vanish. This catches any attempted use of phase stationarity alone.
- Complex Haar eigenvectors independent of their eigenvalues: conditional mean E[G | theta]=G^H, so the overlap contraction on the right-hand side of (12) is exactly zero for every smooth class test. Equating it to the spectral defect on the left-hand side additionally requires the phase stationarity of Section 1. Haar eigenvectors alone impose no restriction on the eigenvalue law. This is a normalization check, not an actual-model premise.
- Symmetric-unitary representatives have real eigenvectors in an appropriate phase gauge. Their Haar-real reference is (1+2delta_jk)/(N+2), yielding the orthogonal rather than unitary radial generator. This catches the missing factor in the diffusion term.
- The explicit dark-resonance control in boundary_delay_obstruction.md has infinite boundary-delay second moment, but (9)–(12) remain well-defined at every fixed N and positive s.

The actual overlap obligation (13) is OPEN. A direct signed estimate derived from the literal U_N is the next step; equations (14)–(15) identify its first unproved correlation input. No generic-gap universality theorem or QUE assertion is being imported.
