# Scale-normalized positive-quantization bound for the unchanged BGS kick

**Stable claim:** `BGS-FM-033`. **Integration review:** 16 October 2026, author check.

**Exact scope:** Conditional on the exact quantitative G1-G3 analytic inputs pinned in the source. Finite algebra checks do not recertify those analytic inputs. No cyclic Heisenberg trace bound.

Canonical status is [the claim ledger](../../record/claim_ledger.md); source `S09` is preserved verbatim in [the imported record](../../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s09). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../../archive/evidence/executions/20261016/chat-integration/receipt.json).


Date: 2026-10-15.

Status: a mathematical deduction from the quantified one-step Egorov and
finite-type estimates in BGS-FM-023, with a full derivation of the added
positive-quantization and scale-normalization steps. No external referee,
formal proof, priority claim, or BGS solution is asserted. Numerical controls
below do not prove the analytic bounds. No GitHub changes were made.

## 1. Model, notation, and statement

Keep the physical symbol and matrices exactly as in BGS-FM-001/FM-023:

    Q_N = exp(i tau N A_N),  U_N=Q_N M_N,  tau=10^-80,
    S = [[3,4],[2,3]],  N odd,
    T_N(a,b)psi(x)=e_N(b(x+inv2*a))psi(x+a).

The physical midpoint Weyl operator is W_N(a,b)=(-1)^(ab) T_N(a,b)
for integer labels, before reduction of labels. Symbols use
Op_N(exp(2pi i(kq+lp)))=W_N(l,k). These conventions are not interchanged.
Let rho_N(v) be the maximum norm of the centered integer representative
of v in (Z/NZ)^2. Thus rho_N(v)>=1 for v!=0. Put beta=1/65.

**Theorem A (all label scales, one kick).** There is C_tau, independent
of N,v,w, such that for all sufficiently large odd N and all v!=0,

    |(1/N) Tr[T_N(w)* Q_N T_N(v) Q_N*]|
                 <= min(1, C_tau rho_N(v)^(-1/65)).       (A)

The inverse-kick version has the same type of estimate. This controls an
individual matrix element of conjugation, not powers of this superoperator.
It is valid up to the largest centered labels O(N); it is not an Egorov
propagation theorem for time O(N).

**Theorem B (every prime cat orbit).** For p odd prime, set

    d_p=ord_p(S),
    F_p(v)=(1/p)Tr[Q_p* T_p(v) Q_p T_p(v)*].

For all sufficiently large primes,

    sup_(v!=0) (1/d_p) sum_(n=0)^(d_p-1) |F_p(S^n v)|
                 <= C_tau d_p^(-1/65)
                 <= C'_tau (log p)^(-1/65).              (B)

There is no split-prime condition and no premise d_p >> sqrt(p).
The same conclusion, with a changed constant, holds for the average over
0<=n<p. These are probes transported by the UNPERTURBED cat, acting on
one physical kick Q_p. They are not traces of powers of U_p.

## 2. Analytic inputs actually used

Let Psi=Phi_g^(-tau/(2pi)); replacing Psi with its inverse does not change
the argument. For a torus translation t_xi put

    H_xi = Psi t_xi Psi^(-1).

The four embedding coordinates are a_j=cos(2pi q), sin(2pi q),
cos(2pi p), sin(2pi p). Given input/output translations xi,eta, write

    u_j=a_j o H_xi, v_j=a_j o t_eta,
    B_j=u_j-v_j, B=(B_1,...,B_4), r=||xi||_(T,infinity)>0.

FM-023 supplies, using the actual primitive Fourier coefficients and the
explicit small-time remainder of this exact g:

(i) a fixed-step O(N^-2) Egorov estimate for smooth symbols, uniform in
all translation labels;
(ii) a finite-type estimate of order 16 for a selected component of
xi-eta+u(x+xi)-u(x), after division by r, where Psi(x)=x+u(x);
(iii) uniform smooth bounds on Psi and its inverse.

In particular, after the area-preserving change x -> Psi(x),

    area{|B|<=r epsilon} <= C_tau epsilon^(1/16),
                           0<epsilon<=1.                 (G1)

Embedding the torus in R^4 turns small chord distance into coordinate
distance modulo integers. Only a bounded number of integer lifts can occur.
The source's finite-type constants are proportional to |tau|r; |tau| is
fixed here and absorbed in C_tau. No uniformity as tau->0 is claimed.

Let K=Q_N T_N(v)Q_N*, L=T_N(w), D=K*L, and

    t_N(c)=(1/N)Tr[D Op_N(c)].

Exact translation Egorov and two uses of (i) give

    Op_N(u_j)D-D Op_N(v_j)=O_op(N^-2).                    (G2)

The product formula, cyclic trace and Fourier Cauchy-Schwarz yield

    |t_N(c B_j)| <= C_tau[N^-1 ||c||_(H3)
                              +N^-2 ||c||_(H2)].         (G3)

These are the quantified inputs reconstructed in FM-023 Sections 2--5.
The original source bounds t_N(chi) by a square root of bad-set area.
Sections 3--4 below replace that step with a positive quantizer, retaining
its error, and normalize the shrinking geometric scale BEFORE differentiating.

## 3. An explicit positive quantizer with a controlled Weyl error

This section does not assume positivity of Weyl quantization.
For odd N define the normalized, real, parity-even vector

    psi_N(x)=Z_N^(-1/2) exp(-pi center_N(x)^2/N),
    Z_N=sum_x exp(-2pi center_N(x)^2/N),
    R_N=|psi_N><psi_N|.

Gaussian sums/integrals give universal constants c,C>0 with

    c sqrt(N)<=Z_N<=C sqrt(N),
    sum_x center_N(x)^2 |psi_N(x)|^2 <= C N,
    ||(X-I)psi_N||^2 <= C/N.                             (P1)

For the last bound, on each non-wrapping edge use
|f(x+1)-f(x)|^2 <= integral_x^(x+1) |f'(s)|^2 ds for
f(s)=exp(-pi s^2/N); the wrapping edge connects equal endpoint values.
The integral over R of |f'|^2 is O(N^-1/2), and divide by Z_N.
The first two bounds follow by comparison with Gaussian integrals; a
fixed multiple of sqrt(N) interior lattice points gives the lower bound.

Let Z be coordinate modulation. The second bound in (P1) gives
||(Z^b-I)psi_N||<=C |b|/sqrt(N), while telescoping translations gives
||(X^a-I)psi_N||<=C |a|/sqrt(N). Since
W_N(a,b)=exp(pi i ab/N) Z^b X^a, this implies for |(a,b)|<=sqrt(N)

    ||(W_N(a,b)-I)psi_N||<=C |(a,b)|/sqrt(N).

Parity sends W_N(a,b) to W_N(-a,-b)=W_N(a,b)* and fixes psi_N.
Therefore t_(a,b)=<psi_N,W_N(a,b)*psi_N> is real and

    |1-t_(a,b)| = (1/2)||(W_N(a,b)-I)psi_N||^2
                   <= C |(a,b)|^2/N.                     (P2)

For larger integer labels, the same bound follows from |1-t|<=2.
All integer alias signs are retained; t_v W_N(v) is alias invariant.

For a scalar symbol a(q,p), define

    AW_N(a)=(1/N) sum_(q,p in Z/NZ)
       a(q/N,p/N) T_N(-q,p) R_N T_N(-q,p)*.               (P3)

It is positive for a>=0. Weyl orthogonality gives AW_N(1)=I and exactly

    (1/N)Tr AW_N(a)=(1/N^2)sum_(q,p) a(q/N,p/N),
    AW_N(e_(k,l))=t_(l,k) W_N(l,k).                       (P4)

Hence, using (P2),

    ||Op_N(a)-AW_N(a)||op
       <= (C/N) sum_n |n|^2 |a_hat(n)|
       <= (C/N)||a||_(H4).                               (P5)

In dimension two the Fourier Cauchy-Schwarz sum is finite at H4.
Also

    |(1/N^2)sum_grid a-integral a|
       <= C N^-4 ||a||_(H4),                             (P6)

by bounding the Fourier coefficients a_hat(Nk), k!=0.
For any unitary D and nonnegative smooth chi, positivity and (P5)--(P6)
therefore give the useful replacement for the square-root estimate:

    |(1/N)Tr[D Op_N(chi)]|
         <= integral chi + C N^-1 ||chi||_(H4).           (P7)

Indeed |Tr(D AW_N(chi))|<=Tr AW_N(chi). This is why the area, rather
than its square root, is legitimate here. The O(N^-1 H4) correction is
part of the proof and is NOT omitted.

## 4. Scale normalization and proof of Theorem A

Put s=dist_T,infinity(eta,xi). Smoothness and H_0=id imply

    ||a_j o H_xi-a_j o t_xi||_(C^k)<=C_(tau,k) r.         (G4)

This is the mean-value theorem in the translation parameter on compact
sets; higher x-derivatives obey the same bound. It is crucial to retain r.
Fix a sufficiently large constant A0 depending on the smooth map Psi.

### Near translations: s<=A0 r

The translation difference a_j o t_xi-a_j o t_eta is O_(C^k)(s).
Consequently beta_j=B_j/r has uniform C^k bounds for every required fixed k.
Equation (G1) states area{|beta|<=epsilon}<=C_tau epsilon^(1/16).
Choose a fixed smooth cutoff chi, equal to one below 1 and zero above 4,
and put

    chi_e=chi(|beta|^2/epsilon^2),
    c_(j,e)=(1-chi_e) beta_j/|beta|^2.

Then sum_j c_(j,e) beta_j=1-chi_e, and chain rule gives

    ||chi_e||_(H4)<=C_tau epsilon^-4,
    ||c_(j,e)||_(H3)<=C_tau epsilon^-4,
    ||c_(j,e)||_(H2)<=C_tau epsilon^-3.                   (G5)

Divide (G3) by r and use (G5). This yields

    |t_N(1-chi_e)|
       <= C_tau[(Nr)^-1 epsilon^-4
                      +(N^2 r)^-1 epsilon^-3].           (G6)

Equation (P7) handles the bad set:

    |t_N(chi_e)|
       <= C_tau[epsilon^(1/16)+N^-1 epsilon^-4].          (G7)

As r<=1 and epsilon<=1, all quantum errors are bounded by
C_tau (Nr)^-1 epsilon^-4. Since input v!=0 is a grid label, Nr>=1.
Set epsilon=(Nr)^(-16/65). The balanced terms equal (Nr)^(-1/65), so

    |t_N(1)|<=C_tau (Nr)^(-1/65).                         (G8)

For centered grid translations, Nr=rho_N(v).

### Separated translations: s>A0 r

For A0 sufficiently large, H_xi-t_xi has lift size at most (A0/2)r,
so H_xi and t_eta are separated on the torus by at least s/2.
Embedding coordinates give |B|>=c s. Also ||B||_(C^k)<=C_(tau,k) s.
Normalize beta=B/s and use c_j=beta_j/|beta|^2, whose needed derivatives
are uniformly bounded. Equation (G3), divided by s, gives

    |t_N(1)|<=C_tau/(Ns)<=C'_tau/(Nr)
                         <=C'_tau (Nr)^(-1/65).          (G9)

The modulus of t_N(1) is the modulus of the matrix element in (A).
Unitarity gives the additional bound one. This proves Theorem A, with
no restriction on the relative size of v and N beyond v!=0.

## 5. Consequence for divisor-grid operator compressions

For an odd D>=3 dividing N, let Pi be projection onto the D^2-1
nonzero Weyl labels (N/D)v. Each has centered size at least N/D.
The cat permutes this grid. Thus every matrix entry of Pi Ad(U_N) Pi
is bounded by C_tau(D/N)^(1/65). Retaining the full dimension loss,

    ||Pi Ad(U_N)Pi|| <= min(1,C_tau (D^131/N)^(1/65)).     (C)

For example D<=N^(1/262) gives O_tau(N^-1/130). This improves the
D^262/N power in FM-023 to D^131/N by the combined positive-quantization
and normalization argument. It is still a restricted compression, not
a gap for the full unitary superoperator Ad(U_N).

## 6. Elementary conic counting and proof of Theorem B

At odd primes, nonzero S-orbits have exactly d_p points. This follows
from its two distinct eigenvalues lambda,lambda^-1 of order d_p over
F_p or F_(p^2): S^j-I is invertible for 0<j<d_p.

S preserves Q(a,b)=a^2-2b^2. For any fixed centered first coordinate a,
the equation Q(a,b)=c modulo p has at most two b solutions. Therefore
for any nonzero orbit O and integer R>=1,

    #{v in O: rho_p(v)<=R} <= 2(2R+1) <= 6R.             (C1)

This includes c=0 on split primes; b^2=a^2/2 still has at most two
solutions for a fixed a. No nonsingular-shell assumption is needed.
If rho_1<=...<=rho_d are the sorted centered radii on O, (C1) implies
rho_j>=j/6. For 0<beta<1,

    (1/d)sum_(v in O) rho_p(v)^(-beta)
         <=6^beta/(1-beta) d^(-beta).                     (C2)

The diagonal matrix element in (A) is conjugate to F_p(v). Apply (A),
then (C2) with beta=1/65. This proves the first bound in (B).
Finally p^2 divides the nonzero integer det(S^d-I), while
|det(S^d-I)| < lambda^d, lambda=3+2sqrt(2). Hence
d>2 log p/log lambda, proving the logarithmic consequence.

Periodicity gives, for the p-step average, at most ceil(p/d) complete
cycles. Since d<=p+1, its ratio to the full-cycle average is at most
ceil(p/d)d/p <=1+d/p<=3. This proves the asserted O(p)-lag version.
The modulus is INSIDE the orbit sum throughout.

## 7. Where the attempt to close the spectral problem still stops

For a nonnegative bandlimited spectral test b, the outstanding pair defect
is still

    Delta_(2,N)(b)=N^-2 sum_(m>=1) |b_hat(m/N)|^2
                           (|Tr U_N^m|^2-min(m,N)).       (S)

Writing the kick superoperator in the Weyl basis as K and the cat
permutation as R, Ad(U_N)=K R and

    |Tr U_N^m|^2 = Tr_HS[(K R)^m].                        (S1)

Theorem A controls entries of K; Theorem B controls diagonal probes of
one kick along R-orbits. Neither theorem estimates the coherent closed
products of K R in (S1). No independence of successive factors is proved.
A normalized Fourier matrix has small entries and fourth power I, so an
entry estimate cannot silently become a power estimate. The present
physical assumptions do not identify our Q_N with that example; it only
invalidates that proposed inference.

Thus this continuation removes an actual arithmetic-size restriction and
extends a one-step matrix-element estimate to all input label scales. It
DOES NOT establish (S), Sine2, an all-order hierarchy, or deterministic
noise removal. The full signed sum (S), including all resonant and
nonresonant times together, remains the target.

## 8. Reproducibility and source boundaries

Run:

    OPENBLAS_NUM_THREADS=1 python -O verify_scaled_overlap.py --output verification.json

The program independently constructs the physical Jacobi generator and
metaplectic matrix. At proxy tau=0.03 and p=31,61,127,199,239,509 it checks
Weyl normalization, covariance, and the OTOC Fourier identity, evaluates
ALL nonzero S-orbits, and checks their exact integer small-box bounds.
It also checks (P3)--(P4), aliases, parity reality and finite multiplier
bounds at N=3,5,7,11,31. The global analytic constants in (P1)--(P7) are
proved above, NOT established by those finite runs.

The literal coupling 10^-80 is NOT simulated. Proxy diagnostics are not
proofs of applicability of the analytic finite-type estimate at tau=0.03,
nor tests of the literal asymptotic limit. No fitted decay exponent is used.

Read sources:
- ChurilovMaksim/BGS, mathematics/spectral-obstructions/arithmetic_translation_exclusion.md,
  Sections 2--6; fetched source blob be8f73cc57b78088cd6e4c3f6162addaa75aedde.
- mathematics/phase_ward_identity.md (the different open spectral-overlap
  obligation; not supplied by the present Weyl-entry theorem).
- The supplied no-extra-UI THEOREM.md (the precise outstanding pair source).

Established background, not a claim of novelty: Rivas and Ozorio de Almeida,
The Weyl representation on the torus, arXiv:quant-ph/9904041; Saraceno and
Ozorio de Almeida, Translations and reflections on the torus,
arXiv:1808.00990. The positive-quantizer estimate required here is derived
explicitly instead of treating a general reference as proof of (A).
