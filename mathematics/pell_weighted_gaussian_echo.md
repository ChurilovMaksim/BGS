---
title: "Weighted Gaussian limits and a periodic Brownian echo for the Pell cat map"
author: "BGS research programme"
date: "5 September 2026"
---

# Status

This is an ordinary project proof, not a priority claim or a complete Lean formalization. Its new objects relative to the unweighted observable law are arbitrary bounded real coefficient arrays, ordered mixed moments, and the actual interaction-picture quantum propagator at all bounded recurrence times. The limiting process is a Gaussian process in the sense of tracial finite-dimensional distributions. No claim of a classical measurement trajectory or independent noise in the finite quantum system is made.

The arithmetic construction, four-letter support theorem and finite normal form are proved in [the Floquet note](pell_floquet_normal_form.md). The present note restates each input used and supplies the additional deductions. It does not establish microscopic BGS or fixed nonzero classical perturbation strength.

# 1. A weighted tracial central limit theorem

Use the Pell sequence N+F sqrt(2)=(1+sqrt(2))^K, with K an odd prime, N odd, and d=(N-1)/2. Let U_0, B, B_j=U_0^j B U_0^(-j), and tau_-=Tr_-/d be as in the Floquet note. Thus U_0^K=I and

    B_j=W(v_j)+W(-v_j),  v_j=(q h^j,h^(-j)),  q=-F modulo N.

For any real array f=(f_0,...,f_(K-1)), define the Hermitian matrix

    X_K(f)=(2K)^(-1/2) sum_j f_j B_j,
    Q_K(f,g)=(1/K) sum_j f_j g_j.

**Theorem 1 (bounded weighted arrays).** Fix a positive integer m and a bound M. Arrays f_1,...,f_m may depend on K but must satisfy |f_(a,j)|<=M. If m=2r, then, uniformly over all these arrays,

    tau_-(X_K(f_1)...X_K(f_(2r)))
      = sum_(pairings pi of {1,...,2r})
          product_({a,b} in pi) Q_K(f_a,f_b)
        + O_(r,M)(1/K) + O_(r,M)(K^r/N).                    (1)

For odd m, for all sufficiently large K depending on m,

    |tau_-(X_K(f_1)...X_K(f_m))|
      <= M^m (2K)^(m/2)/(N-1).                            (2)

Consequently, if a fixed finite collection of bounded arrays has limiting Gram matrix Q, its ordered mixed moments converge to the Wick moments of a centered, commuting real Gaussian vector with covariance Q. Independence is a consequence only when Q is diagonal in the limit; it is not assumed for the Weyl orbit.

**Proof.** Expand the product into its signed Weyl words. The exact parity-projected trace is

    tau_-(e_N(phi)W(v))=e_N(phi)[N 1_(v=0)-1]/(N-1).

Hence the contribution of the subtracted parity term is at most M^m(2K)^(m/2)/(N-1). The central terms satisfy both reciprocal congruences for their time labels.

The arithmetic inputs proved in the Floquet note are these. For fixed m, cut the support at its largest cyclic gap. The resulting polynomial has degree at most K-ceil(K/m), coefficient l1 norm at most m, and quadratic norm divisible by N^2. The norm upper bound m^2 lambda^(K-ceil(K/m)), lambda=3+2sqrt(2), forces characteristic-zero vanishing for all sufficiently large K. A gap greater than 2 log_lambda m splits that relation into independently vanishing bounded-span pieces. After restoring cancelled opposite pairs, any nonbalanced 2r-letter word has at most r-1 translated components, and there are O_r(K^(r-1)) such words. The bounded weights cannot enlarge their normalized total contribution beyond O_(r,M)(1/K). For odd m, divisibility of the lifted polynomial by Z^2-6Z+1 makes its value at 1 divisible by 4; an odd number of signs cannot have that parity. Thus no odd central word remains, proving (2).

For a balanced word choose a matching pi of identical time labels carrying opposite signs. Ignoring coincident labels between different pairs introduces only O_r(K^(r-1)) words and hence O_(r,M)(1/K) error. Each matched pair {a,b} has weight f_(a,j) f_(b,j), regardless of its orientation. With the phase replaced by one, summing pair labels and the 2^r orientations gives exactly the product of the empirical covariances in (1).

It remains to justify replacing the phase by one without assuming independent crossing phases. A pairing phase is the product of factors z_(i-j) or their conjugates, one per crossing, with

    sum_(j mod K)|z_j-1|<9.

For unit complex numbers, |product u_l-1|<=sum |u_l-1|. Each individual pair-label difference is uniform under unweighted summation, while the absolute value of the entire weight product is at most M^(2r). Therefore the absolute normalized phase error for a fixed pairing is at most 9 M^(2r) times its number of crossings divided by K. This is uniform over the coefficient arrays. The prefactor N/(N-1) changes only the already allowed error. Summing pairings proves (1). End of proof.

The result applies, for example, to f_(a,j)=f_a(j/K) for bounded Riemann-integrable functions, where Q(f_a,f_b)=integral_0^1 f_a(x)f_b(x) dx. More generally, convergence of the empirical Gram matrix suffices; continuity or fixed array entries are not required.

# 2. Quantitative asymptotic commutativity

Write ||A||_(2,N)^2=Tr(A*A)/N and ||A||_(2,-)^2=tau_-(A*A). Put p=max|f_j|, q=max|g_j| and c_N=sqrt(2N/(N-1)). For K>=11 the signed pair supports belonging to different unordered time pairs are disjoint. The four Weyl coefficients in [B_t,B_s] each have modulus a_(s-t), where sum_j a_j<9 and a_(K-j)=a_j. Thus

    ||[X_K(f),X_K(g)]||_(2,N)^2
      = (1/K^2) sum_(0<=t<s<K)
          |f_t g_s-f_s g_t|^2 a_(s-t)^2
      <= 36 p^2 q^2/K.                                   (3)

Indeed |f_tg_s-f_sg_t|<=2pq and

    sum_(j=1)^(K-1) (K-j)a_j^2
      = (K/2)sum_j a_j^2 <= K sum_j a_j < 9K.

Positivity under restriction to the odd subspace gives

    ||[X_K(f),X_K(g)]||_(2,-) <= 6 c_N p q/sqrt(K).          (4)

This is a normalized Hilbert--Schmidt result. It is not operator-norm almost-commutativity, simultaneous finite-dimensional diagonalization, or the absence of quantum noncommutativity.

It also yields a convenient exponential version of Theorem 1. For a fixed finite number of bounded coefficient arrays and fixed real t_a, the standard two-factor Duhamel estimate, applied repeatedly, compares

    product_a exp(i t_a X_K(f_a))

in normalized Hilbert--Schmidt norm to exp(i X_K(sum_a t_a f_a)), with error O(K^(-1/2)). Theorem 1 and Gaussian moment determinacy then give

    tau_-(product_a exp(i t_a X_K(f_a)))
      -> exp[-(1/2) sum_(a,b) t_a t_b Q_(a,b)].             (5)

If the arrays vary with K, convergence of their Gram matrix and the uniform moment bounds still suffice. The scalar Gaussian moment problem is determinate, including the zero-variance case. Tightness follows from the second moment; higher even moments give uniform integrability for passing moments to subsequential limits. Thus no unjustified passage from polynomial moments to unbounded exponentials is used: the exponential test itself is bounded and continuous.

# 3. A finite normal form for the interaction-picture echo

Let epsilon=tau/sqrt(2K), where tau is fixed, and define

    U_epsilon=exp(i epsilon B)U_0,
    E_K(t)=U_epsilon^t U_0^(-t),  t an integer.

This is the quantum echo operator. It is not the propagator U_epsilon^t alone. Define

    c_j=(K-1-2j)/(2K),  G=sum_j c_j B_j,
    alpha_K=t/K,  t=mK+s,  0<=s<K,
    w_(t,K)(j)=m+1_(0<=j<s).

Here m is the floor of t/K, including for negative t. The exact coefficient identity is

    c_j + t/K - c_((j-t) mod K) = w_(t,K)(j).              (6)

**Theorem 2 (finite echo comparison).** For K>=11, every integer t, and every real tau,

    ||E_K(t)-exp(i tau X_K(w_(t,K)))||_(2,-)
       <= [6|alpha_K|+c_N(3|alpha_K|+3/4)] tau^2/sqrt(K)
       <= (11C+2)tau^2/sqrt(K),  if |t|<=CK.               (7)

**Proof.** The established finite Floquet normal form is

    ||V_epsilon U_epsilon V_epsilon^*
         -exp(i epsilon Bbar)U_0||_(2,-)
         <=12 epsilon^2/sqrt(K),
    V_epsilon=exp(-i epsilon G),  Bbar=(1/K)sum_j B_j.

Telescoping unitary powers, also for negative t by taking adjoints, and then multiplying by U_0^(-t), approximates E_K(t) by

    exp(i tau X_K(c))
      exp(i tau alpha_K X_K(1))
      exp(-i tau X_K(c_shift)),                            (8)

with error at most 6|alpha_K|tau^2/sqrt(K), where c_shift(j)=c_((j-t) mod K).

Both c and c_shift have supremum norm at most 1/2. Apply the two-factor Duhamel inequality to the first two factors of (8), and then to their sum and the third factor. Equation (4) bounds the sum of the two commutator norms, before the factor tau^2/2, by

    [3c_N |alpha_K| + 3c_N(1/2+|alpha_K|)]/sqrt(K).

Their combined exponent is i tau X_K(c+alpha_K-c_shift), exactly the exponent in (7) by (6). This proves the first inequality. Since N>=7 gives c_N<=sqrt(7/3), its coefficient is bounded by 11C+2 when |alpha_K|<=C. End of proof.

The bound is a comparison estimate, not a convergence rate for the additional limiting Gaussian law. Nor does it require epsilon times the operator norm of G to be small.

# 4. A periodic Brownian limit, not fresh noise each cycle

For real alpha write alpha=m+a, with m=floor(alpha) and 0<=a<1. On [0,1) put

    w_alpha(x)=m+1_(0<=x<a).

Let B(a), 0<=a<=1, be a standard real Brownian motion on an auxiliary probability space, and put Z=B(1). Define a centered Gaussian process on the entire real line by

    Y(alpha)=m Z+B(a).                                    (9)

This is equivalently the integral of the same white-noise sample over a periodically repeated unit interval, with orientation for negative times. It is continuous in mean square across the integers, because B(1)=Z. Consecutive periods repeat the same noise rather than introducing independent increments. For alpha=m+a and beta=n+b,

    Cov(Y(alpha),Y(beta))
      = mn+mb+na+min(a,b),                                (10)
    Var(Y(alpha))=m^2+(2m+1)a.                            (11)

These formulas follow directly from integral_0^1 w_alpha w_beta and do not assume a stochastic model for the quantum system.

**Theorem 3 (finite-dimensional tracial echo limit).** Fix finitely many real times alpha_1,...,alpha_L and integer sequences t_(l,K) with t_(l,K)/K -> alpha_l. Fix integers r_1,...,r_L. Then

    tau_-(product_(l=1)^L E_K(t_(l,K))^(r_l))
      -> E exp(i tau sum_l r_l Y(alpha_l))
       = exp[-tau^2/2 sum_(l,j) r_l r_j
                    Cov(Y(alpha_l),Y(alpha_j))].          (12)

The product on the left is kept in the displayed order. Negative integer powers are allowed because all echo operators are unitary.

**Proof.** The finitely many times have bounded |t|/K, so (7) and telescoping products replace each echo power by exp(i tau r_l X_K(w_(t_l,K))), with vanishing normalized Hilbert--Schmidt error. The step arrays are uniformly bounded. Their empirical Gram matrix converges to the integrals of w_alpha_l w_alpha_j, including when a limiting time is an integer; the corresponding functions are continuous in L2 as the time parameter crosses an integer. Formula (5) now gives (12). Normalized Cauchy--Schwarz bounds the trace error by the Hilbert--Schmidt error. End of proof.

For a single time alpha, the empirical eigenvalue measure of the echo E_K(t_K) therefore converges on the circle to a wrapped normal law with angular variance

    tau^2 [m^2+(2m+1)a].                                  (13)

Indeed take L=1 and every integer power r in (12); these are all Fourier coefficients of the circle measure. The normalized fidelity amplitude and its squared modulus have limits

    tau_-(E_K(t_K)) -> exp[-tau^2(m^2+(2m+1)a)/2],
    |tau_-(E_K(t_K))|^2 -> exp[-tau^2(m^2+(2m+1)a)].         (14)

Within the first recurrence interval, 0<=alpha<=1, the variance is alpha: the amplitude decays exponentially in alpha. At integer returns alpha=m it is m^2: recurrence cycles are perfectly correlated, not a random walk with variance m. At those integer times U_0^(-mK)=I, so (14) recovers the earlier actual-propagator return law exactly.

For alpha=1/2, variance is 1/2. For alpha=3/2 it is 5/2, not 3/2 as an independent-cycle Brownian approximation would predict. This is a testable distinction between the proved periodic-memory limit and a phenomenological memoryless-noise assumption.

# 5. What the result does not assert

The word 'Brownian' specifies the explicitly constructed limiting Gaussian covariance, in finite-dimensional tracial distributions. It does not supply a joint spectral probability measure for noncommuting finite matrices or a measurement-independent quantum sample path. It does not imply independent eigenvalues, local spacing universality, an operator-norm approximation by commuting matrices, or a functional invariance principle in a specified path topology.

The time window remains |t|=O(K)=O(log N). The ordinary microscopic Heisenberg scale is O(d_N), and the present error does not control it. The quantum epsilon is of order K^(-1/2); the corresponding classical kick amplitude is of order 1/(N sqrt(K)). Fixed nonzero classical perturbations and positive BGS universality are not established.

Tracial central limit theorems, semiclassically small cat-map perturbations and fidelity-decay results all have an existing literature. The precise weighted arithmetic array theorem and periodic-memory echo limit require a separate historical-priority review. No world-first claim is inferred from the derivation or a targeted source search.

# 6. Verification obligations

The finite coefficient identity (6), the step-array Gram matrix (10), and signed-pair orthogonality can be tested with exact arithmetic. Dense tests should compare the actual interaction-picture echo to the three-exponential normal form and then to the single weighted exponential, keeping these two errors separate. A comparison only at t=mK does not check the new intermediate-time statement. Tests should include alpha near a recurrence boundary, negative t, and alpha=3/2, where independent-cycle noise gives the wrong predicted variance.

General asymptotic theorems here are justified by the proofs, not by fitting simulated echo curves. Actual execution and compilation status must be recorded separately with source hashes. The new analytic statements are not declared fully formalized in Lean.
