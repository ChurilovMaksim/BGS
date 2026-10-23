# Quantum cyclic cohomology and a parity-resolved spectral susceptibility for the frozen BGS kick

**Stable claim:** `BGS-FM-032`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Additive normalized-HS cohomology and initial eigenphase response only; fixed physical strength grows as tau*p. No multiplicative holonomy or microscopic limit.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S02` is preserved verbatim in [the imported record](../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s02). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../archive/evidence/executions/20261016/chat-integration/receipt.json).


**Research note (14 October 2026). Status:** elementary finite-dimensional theorem, proof and independent exact Fourier/matrix checks. No microscopic random-matrix universality is established. External priority and full mathematical refereeing remain open. The original note predates the integration recorded below.

## Model and conventions

For each odd prime p > 99, consider the BGS Hermitian kick generator

A_p = Op_p(g),   U_p(t) = exp(i t A_p) M_p,

with the exact 32-mode physical midpoint symbol

g(q,r) = cos(14 pi q) + R(q)/10 + R(q) sin(2 pi q)/100 - 1/10
         + R(q+1/2) cos(2 pi r - alpha)/100,
R(q) = (1-cos(14 pi q))(1+cos(2 pi q)),
cos(alpha) = -3/5, sin(alpha) = 4/5.

Use the raw modular Weyl basis T_p(a,b) and covariance M_p T_p(v) M_p^{-1} = T_p(Sv), S=[[3,4],[2,3]]. In particular, if ghat(k,l) denotes ordinary Fourier coefficients, then the **raw** coefficient of T_p(l,k) is (-1)^(k*l) ghat(k,l), not just ghat(k,l). All norms below are normalized Hilbert-Schmidt: ||X||_p^2=Tr(X*X)/p.

Let d = ord_p(S), T = Ad(M_p), and P=(1/d)sum_{j=0}^{d-1} T^j. Then T^d=Id, P is the orthogonal conditional expectation onto the commutant of M_p, and Ran(I-T)=Ker P.

## Main theorem

Define eps_p = inf_{B=B*} ||A_p-(B-M_p B M_p^{-1})||_p. Then

eps_p = ||P A_p||_p,

and, with Sigma_p = d eps_p^2, **for all odd primes p>99**,

- if d is odd: 81/200 <= Sigma_p <= 81/200 + 20449/250000;
- if d is even: 81/100 <= Sigma_p <= 81/100 + 20449/250000.

In particular eps_p = Theta(d^(-1/2)) with explicit constants independent of p, and the two parity-dependent permitted intervals are disjoint.

Let B_min be the unique solution of (I-T)B=A_p-P A_p orthogonal to Ker(I-T). Every solution has norm at least ||B_min||_p, and

- if d is odd: ||B_min||_p^2 >= 81(d^2-1)/(2400 d);
- if d is even: ||B_min||_p^2 >= 81(d^2-4)/(4800 d).

There is also a uniform upper bound ||B_min||_p <= 2(593/500) sqrt(d). Thus the minimal transfer norm is Theta(sqrt(d)).

At the *physical generator strength* t_p = tau p with tau = 10^(-80),

inf_{B=B*} ||t_p A_p - (B-M_p B M_p^{-1})||_p
 =t_p eps_p >= (9 tau/(10 sqrt(2))) p/sqrt(d)
 >= (9 tau/(10 sqrt(2))) p/sqrt(p+1) -> infinity.

This is only an **additive, linearized** cohomological statement, not a nonperturbative obstruction to a multiplicative unitary coboundary.

## Proof of the cyclic cohomology formula

The raw Weyl operators for nonzero v form cycles of length exactly d under T because S has eigenvalues lambda,lambda^(-1) of order d over F_(p^2), and S^j-I is invertible for 0<j<d. Hence, for each orbit O, list its coefficients a_(O,j), j modulo d, and let s_O=sum_j a_(O,j). Then

P A_p = sum_O (s_O/d) sum_{j=0}^{d-1} T_p(S^j v_O),

||P A_p||_p^2 = (1/d) sum_O |s_O|^2.

The optimal additive coboundary error equals ||P A_p|| because P is the orthogonal projection onto Ker(I-T), and Ran(I-T)=Ker P.

## Exact principal-orbit isolation and parity

The physical symbol has two coefficients a_(0,+7)=a_(0,-7)=9/20, and Q(a,b)=a^2-2b^2 equals -98 for both. The other 30 Fourier labels have Q-values in {-162,-128,-127,-97,-72,-71,-50,-8,-2,-1,1}, all differing from -98 by nonzero integers of absolute value <= 99. Since Q(Sv)=Q(v), for p>99 neither main mode can collide with any other support mode under the mod-p cat action.

If d is odd, +w and -w lie in different cycles and contribute 2(9/20)^2=81/200 to d||P A_p||^2. If d is even, S^(d/2)=-I mod p, they lie in the same cycle and contribute (9/10)^2=81/100. The tail contributes an independent sum of squares E_p>=0. Direct exact rational assembly of the other Fourier coefficients gives sum_(v neq +-w) (|Re a_v|+|Im a_v|)=143/500. Therefore E_p<=(143/500)^2=20449/250000.

## Minimal primitive norm and its growth

For one isolated raw Weyl mode of amplitude a on a cycle of length d, the mean-zero solution to

b_j-b_(j-1)= a (1_(j=0)-1/d)

is b_j = a(d-1-2j)/(2d), j=0,...,d-1. Its squared norm is |a|^2(d^2-1)/(12d).

For the principal pair of amplitude a=9/20:

- d odd: two independent cycles give 2 a^2(d^2-1)/(12d) = 81(d^2-1)/(2400d).
- d even: both modes occupy antipodal positions on one cycle. The discrete Fourier transform has amplitude 2a at even nonzero Fourier integers and zero at odd integers. The identity sum_(k=1)^(m-1) csc^2(pi*k/m)=(m^2-1)/3, with m=d/2, gives a^2(d^2-4)/(12d) = 81(d^2-4)/(4800d).

Other support orbits are orthogonal and can only increase the minimum primitive norm. For the upper bound, solve the cyclic difference equation orbit by orbit via partial sums and use |b_j|<=2 sum_(v in O)|a_v|. The total raw Fourier coefficient l1 norm is at most 593/500 (exact rational bound), giving the displayed O(sqrt(d)) estimate.

## Spectral perturbation interpretation and curvature

Choose local analytic eigenphase branches theta_j(t) of U_p(t)=exp(it A_p)M_p near t=0, with repeated eigenvalues of M_p resolved by degenerate perturbation theory. The initial phase velocities are the eigenvalues of the Hermitian compressions P_lambda A_p P_lambda, where P_lambda denotes a spectral projector of M_p. Since P A_p=sum_lambda P_lambda A_p P_lambda,

(1/p)sum_(j=1)^p (theta_j'(0))^2=||P A_p||_p^2=Sigma_p/d.

As M_p^d=zeta_p I, define f_p(t)=Tr(U_p(t)^d)/(p*zeta_p). The ordered product rule and trace cyclicity show

f_p(0)=1, f_p'(0)=0, f_p''(0)=-d^2 ||P A_p||_p^2=-d Sigma_p.

Hence the (negative) quadratic response of the arithmetic return is trapped between two explicit parity-dependent intervals proportional to d. The Taylor calculation is a LOCAL response statement at t=0. It cannot be extrapolated to the physical t_p=tau*p because t_p grows without bound as p->infinity.

## Exact checks and caution

Exact rational Fourier/orbit calculations yield:

| p | d | d eps_p^2 exactly | numerical |
|---:|---:|---:|---:|
| 101 | 102 | 412563/500000 | 0.825126000 |
| 127 | 63 | 165209/400000 | 0.413022500 |
| 509 | 510 | 412563/500000 | 0.825126000 |
| 1009 | 72 | 1650207/2000000 | 0.825103500 |
| 10007 | 5003 | 330151/800000 | 0.412688750 |

Independent actual matrix calculations at p=19,29,31 agree with the Weyl-orbit projection and eigenphase-slope squared sum to ~1e-16. An initial check missing the (-1)^(ab) raw/midpoint conversion produced discrepancies of order 1e-4 at p=19,31; correcting it eliminated the discrepancies. The error is in the preliminary check, not in the model or its canonical Fourier conventions.

This theorem does **not** imply the missing E_p(K)->0 for the resonant trace sector, does not bound actual U_p(tau*p) traces, and does not establish BGS or any GOE/GUE microscopic law. It shows why finite cyclic additive Hilbert-Schmidt approximate-coboundary conditions alone are too weak for a quantum Livsic-to-RMT theorem: the defect is O(d^-1/2) while its primitive has norm Omega(sqrt(d)), and physical semiclassical scaling amplifies the defect. A genuine result must control the multiplicative holonomy and its complete signed Heisenberg-time spectrum.

## Context

BGS original model and arithmetic return inputs: `mathematics/frozen_arithmetic_trace_rigidity.md`, `mathematics/prime_resonant_sector.md`, `mathematics/fixed_model_symmetry_theorem.md` in the user's BGS repository. Analogues of matrix-valued Livsic theory exist for Holder cocycles over hyperbolic dynamics (e.g., Kalinin, *Livsic theorem for matrix cocycles*, arXiv:0808.0350), but they do not provide the uniform-in-dimension quantum trace estimates required here.

## Exact Haar-conjugation benchmark and a parity-doubling phenomenon

For p>99, normalized tracial variance of the actual BGS Hermitian generator is exactly

||A_p||_p^2 = 66033/160000 = 0.41270625.

Let V be Haar distributed in U(p) and let P_V denote normalized-HS projection onto the commutant of V M_p V*. Under unitary adjoint conjugation, traceless End(C^p) is an irreducible complex representation. As the fixed space of Ad M_p has dimension 1+(p^2-1)/d (one scalar plus one vector per nonzero Weyl orbit), Schur orthogonality gives the exact identity

E_V ||P_V A_p||_p^2 = ||A_p||_p^2 / d = (66033/160000)/d.

In particular, the ratio of the *actual* first-order spectral-velocity variance to this Haar-conjugate expectation equals

Sigma_p / (66033/160000).

The exact rational orbit checks above yield, e.g., ratios 1.9993058 at p=101 or p=509 (even d), 1.0007663 at p=127 (odd d), and 0.9999576 at p=10007 (odd d). The arithmetic factor approximately two is not a statement about a GOE or CUE eigenphase law. It reflects coherent pairing of Weyl vectors under the exact half-return S^(d/2)=-I for even d.

For *any* single real Weyl-cosine generator A=a[T_p(w)+T_p(-w)] on a nonzero orbit of length d, with p odd and w not self-opposite, the ratio is **exactly 1 for odd d and exactly 2 for even d**, because ||A||_p^2=2|a|^2 while d||P A||_p^2 equals 2|a|^2 or 4|a|^2 respectively.

For the full BGS symbol, another refinement uses all twelve exact Q-invariant classes of its finite Fourier support. If p>163, all Q-values of distinct classes remain distinct modulo p (their maximal integer difference is 163). Summing the exact rational per-Q bounds yields

sum_(Q neq -98) [sum_(v:Q(v)=Q)(|Re a_v|+|Im a_v|)]^2 = 37747/2000000.

Consequently, for **all primes p>163**, the upper limits in the main theorem can be improved to

- odd d: Sigma_p <= 81/200 + 37747/2000000 = 0.4238735;
- even d: Sigma_p <= 81/100 + 37747/2000000 = 0.8288735.

The lower limits remain 0.405 and 0.81, respectively. These are uniform all-prime arithmetic bounds, not fitted numerical limits.

## Exact maximal-inert-order evaluation

Suppose p>163, (2/p)=-1 and d=ord_p(S)=p+1. Identify (a,b) with z=a+b sqrt(2) in F_(p^2). The action S sends z to lambda*z for lambda=3+2sqrt(2), and Q(a,b)=a^2-2b^2 is the finite-field norm. The norm-one group has order p+1, so <lambda> is the entire norm-one group under the maximal-order assumption and acts freely and transitively on each shell Q(v)=q neq 0. All the integer Q-values of our Fourier support remain distinct modulo p except when they were already equal as integers. Thus

Sigma_p = sum_(q in Z) |sum_(v in supp(g), Q(v)=q) a_v|^2 = 412563/500000

exactly. This is an exact rational arithmetic response for the physical symbol, on every prime satisfying the displayed condition; examples include p=509,2003,5003. Infinitude of primes with maximal inert order is **not asserted**.

This norm-shell decomposition is structurally related to the previously studied arithmetic variance of quantum cat-map matrix elements in Kurlberg--Rudnick and Kurlberg--Rosenzweig--Rudnick. No priority claim is made for the arithmetic variance framework.

## Next genuinely nonlinear trace obligation: a density-one threshold

For the exact resonant block C_(p,d)=zeta_p^(-1) U_p(tau*p)^d, the prime-sector obligation for a fixed compact K=[a,b] subset (0,infinity) is

E_p(K)=p^(-2) sum_(r>=1: a*p<=r*d<=b*p) |Tr C_(p,d)^r|^2 -> 0.

An elementary arithmetic bound shows that for every epsilon>0, all but O_epsilon(X^(1-2epsilon)) primes p<=X satisfy d_p>p^(1/2-epsilon). Indeed p divides det(S^(d_p)-I), while log |det(S^m-I)|=O(m), so the product over all m<=X^(1/2-epsilon) has O(X^(1-2epsilon)) distinct prime factors.

Consequently, if one can establish, for some eta>0, the **model-specific** uniform noncommutative trace estimate

|Tr C_(p,d_p)^r| <= C p^(3/4-eta)

for every resonant r with r*d_p/p in K along a density-one set of primes whose orders exceed p^(1/2-epsilon), with 0<epsilon<2eta, then

E_p(K) <= C_K p^(epsilon-2eta) -> 0

on that set of primes. This would settle only the specified *resonant pair sector on a density-one prime subsequence*, not all primes, nonresonant times, composite dimensions, or higher signed factorial statistics. No such trace estimate is proved by the current cohomology/susceptibility work. Proving it is a possible next target, substantially weaker than a uniform O(sqrt(p)) trace bound but still a highly nontrivial Heisenberg-scale cancellation statement.
