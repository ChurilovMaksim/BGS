# BGS-TRACE-027: weighted phase coherence and slow-window Ward covariance

The exact exported author proof and fresh independent review are accepted at the scopes below. The original ZIP was inaccessible with HTTP 403; its original verifier, source-pins and receipts were not downloaded or replayed. The exact proof UTF-8 bytes/hash were independently reproduced from the authorized Work export. The fresh independent controls here are separately executed evidence, not authentication of the unavailable archive's runs. Historical pending-review labels in the proof remain unchanged.

For finite unitary U, independent uniform diagonal D, V=DU, P=|U|², J=11ᵀ/N, Q_ab=U_ab conjugate(U_ba), max P<=C/N, C>=1 and r=||Q||, put

    e_m=m![C^(m-1)r+C^(m-1/2)/sqrt(N)+m(m-1)C^m/N],
    L_m=sum_(u=0)^(m-1) P^u circ (P^(m-u))^T,
    S_m=E[d_m d_m*], d_m(a)=(V^m)_aa.

For every m>=2, ||S_m-L_m||<=e_m/N for arbitrary deterministic complex spatial weights, retaining repeated occupations and all m>N. For m=1 the diagonal covariance is exact. Under ||P-J||<=rho<1, Pi=I-J, R=(I-P+J)^(-1), H=R+R^T-I and k_m=m(C-1)rho^(m-2)+2rho^m/(1-rho),

    ||N Pi S_m Pi-Pi H Pi||<=e_m+k_m,
    ||N E[c_m c_m*]-(I-PP^T)||<=(1+rho)^2(e_m+k_m),
    c_m=(I-P)d_m.

The classical Green–Kubo term H is nontrivial and must not be replaced by I. For m>=3 the complete averaged signed Hessian-plus-cotangent Ward action on |p_m|² obeys

    |E R_(G-G_H)|p_m|²|<=m²(C-1)rho^(m-2)+m(1+m/N)e_m.

For the unchanged literal odd-N actual family eventually C=5, rho=1/2, r_N->0. The explicit T_N in proof equation (16) tends to infinity, but convergence of these errors holds only uniformly for ceil(T_N/2)<=m<=T_N. It is neither all-fixed-m convergence nor uniform full-prefix convergence, and is not a Heisenberg window. Startup and r_N rate are noneffective.

The separate unconjugated transpose-product B_ab=U_ab U_ba has ||B_N||=O_tau(sqrt(log(2N)/N)) for the actual fixed tau=10^-80 operator. With the exact diagonal repeated-occupation subtraction retained, the precise mixed moment E[p_1² conjugate(p_2)] has the same bound. This resolves the degree-two exception for that mixed-moment family only; it is not all-fixed-degree CUE moment identification. The generic m=2 mixed-trace inequality is excluded, as required by the preserved short-cycle falsifier.

[Byte-exact proof](../../evidence/wave2_checked_20261007/raw/ward_covariance/input/weighted_coherence.md), equations (1)-(19); [fresh focused review](../../evidence/wave2_checked_20261007/raw/ward_covariance/review.md); [sealed closure](../../evidence/wave2_checked_20261007/raw/ward_covariance/SHA256SUMS). The exact independent Gaussian-rational controls cover N=3,4 and degrees 1..6, six raw signed Ward identities, 46,197 covariance permutations and 34,404 two-cycle cases. Floating norm inequalities have their original disclosed finite tolerances. No finite run certifies the analytic parametrix or asymptotic limit.

Inherited actual flatness/P mixing, reverse decay, accepted Ward v2 and raw branch parametrix remain their own proof/review inputs; no new external-source leaf is added. The complete absorbed infinite Poisson/Ward overlap obligation (13), Heisenberg and larger degrees, balanced microscopic law, literal signed masked T16, higher factorial TRACE-005 and deterministic BGS remain OPEN.
