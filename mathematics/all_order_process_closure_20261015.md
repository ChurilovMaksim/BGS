# Closing the hierarchy-to-process step without an independent UI assumption

**Stable claim:** `BGS-TRACE-086`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** The implication is proved; H_diag and TRACE-005 for the frozen matrix remain open. Every fixed order and every compact bandwidth are required.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S08` is preserved verbatim in [the imported record](../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s08). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../archive/evidence/executions/20261016/chat-integration/receipt.json).


Date: 2026-10-15.

Status: self-contained finite comparison inequality and a conditional implication. The signed trace hypothesis is NOT proved for the frozen BGS propagator. No priority, independent external refereeing, formal verification, or solution of BGS is claimed. Original research note; subsequently integrated with the review below.

## 1. Precise remaining hypothesis

Let U_N be any deterministic unitary N by N matrix, with phases theta_j in R/Z, allowing multiplicities. Let alpha be uniform on R/Z and define the periodic, unfolded counting measure

    Xi_(N,alpha) = sum_(j=1)^N sum_(l in Z) delta_(N(theta_j-alpha+l)).

Expectation below is over alpha only. In particular, for every bounded Borel set I,

    E Xi_(N,alpha)(I) = |I|.                                      (1)

For an integer tuple m_1+...+m_k=0, define

    D_U(m) = sum_(j_1,...,j_k distinct) exp(2 pi i sum_a m_a theta_(j_a)).

For a real nonnegative Schwartz function b with smooth compactly supported Fourier transform and sup b < 1, define

    b_N(t) = sum_(l in Z) b(N(t+l)),
    M_(k,N)^U(b) = (1/k!) integral_0^1
        sum_(j_1,...,j_k distinct) product_a b_N(theta_(j_a)-alpha) d alpha.

Set M_(0,N)=1. Exactly, M_(1,N)=H:=integral_R b(x) dx.

Let M_(k,N)^CUE(b) be the expectation of the same statistic for Haar U(N). Put

    Delta_(k,N)(b) = M_(k,N)^U(b) - M_(k,N)^CUE(b).

The reduced hypothesis is

    Delta_(k,N)(b) -> 0                                        (H_diag)

for every fixed k>=2 and every b in the class above. The full signed Heisenberg hypothesis of the project implies (H_diag). No rates uniform in k or in the Fourier bandwidth are assumed. The limits are always taken at fixed k and fixed b.

### Exact Fourier expression

Poisson summation and integration over alpha give

    M_(k,N)^U(b)
      = 1/(k! N^k) sum_(m_1+...+m_k=0)
              product_a b_hat(m_a/N) D_U(m_1,...,m_k).          (2)

This is a finite sum because b_hat has compact support. Its test weight is

    W_(k,b)(xi_1,...,xi_(k-1))
      = (1/k!) product_(a<k) b_hat(xi_a)
                    b_hat(-sum_(a<k)xi_a).

The absolute value in Delta is taken AFTER the complete signed sum. Individual trace products are not replaced by absolute values. If supp b_hat is contained in [-B,B], contributing trace indices still have size O_k(BN).

## 2. Exact CUE reference and its factorial bound

Define the Hermitian Toeplitz matrix, indexed by 0<=i,j<N,

    T_(N,b)(i,j) = (1/N) b_hat((i-j)/N).

It is positive semidefinite: for c in C^N,

    c* T_(N,b) c = integral_0^1 b_N(t)
                       |sum_j c_j exp(2 pi i j t)|^2 dt >= 0.

Also Tr T_(N,b)=H. For sufficiently large N (depending on fixed b), b_N<=1, so T_(N,b)<=I. Indeed, after choosing the nearest lift, all other terms of the periodization are bounded uniformly by a Schwartz tail O_A(N^-A), while sup b<1.

The CUE eigenphase density is the squared Fourier Vandermonde divided by N!. Expanding its two determinants and integrating each variable proves the finite identity

    E_CUE product_(j=1)^N (1-z b_N(theta_j))
                  = det(I-z T_(N,b)).                         (3)

Thus M_(k,N)^CUE(b) is the kth elementary symmetric polynomial in the nonnegative eigenvalues of T_(N,b). In particular

    0 <= M_(k,N)^CUE(b) <= H^k/k!.                            (4)

The upper bound follows by expanding (sum lambda_j)^k: each product with distinct indices occurs k! times, and all remaining terms are nonnegative. Equation (3) is the standard finite CUE/Toeplitz determinant identity; its elementary argument is given here, not a new priority claim.

## 3. Finite Bonferroni comparison

For h_1,...,h_N in [0,1], write e_k(h) for the elementary symmetric polynomials. For odd J,

    sum_(k=0)^J (-1)^k e_k(h)
       <= product_j(1-h_j)
       <= sum_(k=0)^(J-1) (-1)^k e_k(h).                     (5)

One proof is to realize h_j as the success probabilities of independent Bernoulli variables and apply the finite inclusion-exclusion inequalities. This auxiliary proof device changes no distribution in the BGS model. The statement is a pointwise polynomial inequality.

Apply (5), then average over alpha, to the deterministic spectrum and to CUE. Comparing their upper and lower bounds gives

    |Z_N^U(b)-Z_N^CUE(b)|
      <= sum_(k=2)^J |Delta_(k,N)(b)| + H^J/J!,               (6)

where Z_N^U(b)=integral product_j(1-b_N(theta_j-alpha)) d alpha.
The k=1 difference is exactly zero. This inequality needs no bounds on moments of the deterministic spectrum beyond the finitely many displayed Delta values. In particular, no uniform-in-N exponential count moment is assumed.

## 4. Compact local tests and positive Fourier smoothing

Fix f in C_c^infinity(R), f>=0, and put h=1-exp(-f). Then 0<=h<=c<1 and H=integral h.

Choose a nonzero eta in C_c^infinity(R), let a be its inverse Fourier transform, and normalize

    K(x)=|a(x)|^2/integral |a|^2,
    K_B(x)=B K(Bx),
    b_B=h*K_B.

Then b_B is nonnegative Schwartz, sup b_B<=c<1, b_B_hat is smooth and compactly supported, integral b_B=H, and ||b_B-h||_1 ->0 as B->infinity.

For large N both h_N and b_(B,N) lie in [0,1]. The elementary product Lipschitz inequality gives

    |Z_N^U(h)-Z_N^U(b_B)|
       <= sum_j integral_0^1
                    |h_N(theta_j-alpha)-b_(B,N)(theta_j-alpha)| d alpha
       <= ||h-b_B||_1.                                       (7)

The same bound holds after CUE averaging. If N exceeds the diameter of supp f, each eigenvalue label contributes at most one periodic point to that support, and

    Z_N^U(h) = E_alpha exp(-<f,Xi_(N,alpha)>).

Combining (6) and (7) proves the NONASYMPTOTIC certificate

    |L_N^U(f)-L_N^CUE(f)|
       <= 2||h-b_B||_1
          + sum_(k=2)^J |Delta_(k,N)(b_B)|
          + H^J/J!,                                         (8)

for every fixed B and odd J, once N is large enough for the displayed periodizations.

There is no exchange of the N limit with an infinite factorial expansion. For a prescribed accuracy, first choose B to control the smoothing error, then a finite odd J to control H^J/J!, and only then let N increase at these fixed choices. Numerical examples for H<=1,2,4 give tail below 10^-6 at odd J=11,15,21 respectively; these are reference-tail bounds, NOT bounds on the physical Delta terms.

## 5. Conditional local Sine2 theorem

**Theorem.** If (H_diag) holds, then Xi_(N,alpha) converges in distribution to the Sine2 point process. Every fixed local count moment is uniformly integrable and converges to the corresponding Sine2 moment. Every fixed compactly supported factorial correlation test also converges. An independent tightness or UI assumption is unnecessary under this all-order hypothesis.

**Proof of weak convergence.** At fixed B,J the middle term of (8) vanishes by (H_diag). Let B and J increase afterward. The finite CUE unfolded kernel, up to a gauge that cancels from determinants, is

    K_N(x,y)=sin(pi(x-y))/(N sin(pi(x-y)/N)).

Its correlation determinants converge locally to those of K(x,y)=sin(pi(x-y))/(pi(x-y)), and they are bounded by one (Gram/Hadamard). For compact h the coefficient convergence follows by dominated convergence; bound (4) and (5) give convergence of its Laplace functional by the same finite truncation. Hence L_N^CUE(f) tends to the Sine2 Laplace functional. Equation (8) gives the identical limit for U_N. Laplace functionals on nonnegative compact smooth tests determine the law of locally finite counting measures. Alternatively use (1) and Markov on increasing compact intervals for tightness, then the Laplace identity to identify every subsequential limit.

**Proof of local UI.** Fix a compact interval I. Choose a nonnegative bandlimited Schwartz b with sup b<1 and b>=c_I>0 on I. Such a b is obtained by squaring the inverse Fourier transform of a smooth bump, dilating its nonzero neighborhood to cover I, and multiplying by a sufficiently small positive constant. For N>diam I, different points in I have different original labels, even if some labels have coincident positions. Therefore pointwise

    (Xi_N(I))_r <= r! c_I^(-r) e_r(
                   b_N(theta_1-alpha),...,b_N(theta_N-alpha)).

Averaging and using (H_diag) and (4) shows that every fixed falling-factorial count moment is bounded uniformly in N. Stirling's identity expresses every ordinary count moment as a finite positive combination of these. In particular, the (r+1)st moment is uniformly bounded, proving UI of the rth power. Sine2 has no point at any deterministic endpoint, so count moments on intervals converge under weak convergence and UI. Compact continuous factorial tests are bounded by a fixed power of a local count, and converge in the same way. Extension to anchored Schwartz tests can also use the existing TRACE-004 occupation argument: Holder bounds masses in every translated unit cube by the same local moment, making Schwartz tails uniformly summable.

This is a sufficient theorem based on (H_diag), which is implied by the project's full H. It does not infer (H_diag) from a pair law, from one Fourier bandwidth, or from sublinear-time traces.

## 6. The first genuinely unproved physical coefficient

For real b, the pair coefficient is exactly

    Delta_(2,N)(b)
      = (1/N^2) sum_(m>=1) |b_hat(m/N)|^2
                     (|Tr U_N^m|^2-min(m,N)).                (9)

The m=0 term cancels. Positive and negative m have equal contributions, cancelling the 1/2! factor. This includes resonant and nonresonant times together. Equation (9) remains UNPROVED to tend to zero for the prescribed frozen U_N in this note. The stronger all-order coefficients are likewise unestimated. Equations (6)-(8) close the logical transition after these coefficients are controlled; they do not supply that control.

The earlier condition E_p(K)->0 for a separately selected resonance lattice is merely one sufficient deletion route, and is not inserted into this proof.

## 7. Assumption audit: what is, and is not, removed

- Fixed analytic symbol, odd N, and fixed tau=10^-80 define the studied family. They narrow generality; they are not unproved random-matrix hypotheses.
- Exact Weyl identities and correctly applied existing theorems are mathematical dependencies, not speculative assumptions.
- Prime-only results, shrinking kick amplitudes, logarithmic-time statements, and auxiliary random noise have their stated narrower domains. They cannot be substituted for the fixed all-odd-N problem.
- The main Heisenberg-scale signed coefficient estimates are substantive unresolved mathematical obligations. Calling them one hypothesis does not make them a small remaining step.
- Under full H, independent local UI, factorial-series tail, and local tightness premises can be removed as shown above. The existing TRACE-004 already addresses the every-bandwidth-to-Schwartz part; this note does not claim that extension as new.
- At weaker inputs (pair-only, bounded order, one fixed band, or weak convergence alone), UI cannot in general be dropped.
- No full audit of every p-adic or WKB source was performed in this continuation.

## 8. Sources, verification, and scope

Read project sources: mathematics/trace_to_local_statistics_bridge.md (exact Fourier/Mobius identity); mathematics/bandlimited_correlation_extension.md (occupation and Schwartz extension); record/claim_registry.md (separate conditional scopes); the supplied AUDIT_RU.md and CLAIM_LEDGER_RU.md (15 October 2026).

Primary background: A. Soshnikov, Determinantal random point fields, arXiv:math/0002099 (determinantal processes and convergence). The proof above spells out the finite CUE determinant and truncation operations needed here. Standard results are not attributed to this research as discoveries.

verify_closure.py checks exact rational Bonferroni brackets, a finite comparison bound, Stirling moment identities, the Fourier/Mobius coefficient identity, the finite CUE Toeplitz pair benchmark, and the integrated comparison bound on 15 spectra. Six tests use the exact BGS matrix formula at proxy tau=0.03, solely as finite algebra checks. These are NOT simulations of the frozen asymptotic coupling and NOT proofs of H. The verifier is run with python -O and uses explicit exceptions, not assert.
