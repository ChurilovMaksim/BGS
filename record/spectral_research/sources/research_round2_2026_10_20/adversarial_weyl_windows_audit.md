> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_weyl_windows_audit.md`. Embedded SHA256: `ec844db9c890ee7b1cbb94392be4cd45a433bf729a13c320179ec184ab16a26a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent check of the moving maximal Weyl return bounds

Input: `fermionic_weyl_return_windows.md`, SHA-256
`de901fca5b512781737f7543a4f094172184d3fe3991d5cb61eacf17373a457d`.
The all-Weyl twisted pressure input was independently audited in
`adversarial_twisted_pressure_audit.md`.

**Verdict: all statements (3)--(14) pass.** The proof is finite-dimensional
and the complete tails are handled by convergent geometric sums.

Let Q_N(m)=max_v |Tr(T_v^* U^m)|^2/N^2. At each time m+j select an
independent maximizing Weyl index v_j. With the normalized
Hilbert--Schmidt inner product set A_j=T_(v_j) U^-j and f=U^m.
Cyclicity gives <A_j,f>=Tr(T_(v_j)^* U^(m+j))/N. Another cyclic
permutation gives

|<A_j,A_k>|=|Tr(T_(v_j)^* T_(v_k) U^(j-k))|/N.

The Weyl product is a phase times T_(v_k-v_j), so the uniform twisted
trace estimate bounds this by C a^|j-k|/N for j different from k.
The Gram matrix has largest eigenvalue at most
1+(2C/N) sum_(d=1)^(L-1) a^d. Bessel's inequality for this finite
family proves the bound for the sum of the Q_N(m+j). No vector
independence and no restriction on the window location m is needed.

Choosing L=floor((log N-2 log log N)/log a) makes the Gram error
O(log^-2 N). Partitioning any integer interval into such blocks gives
the stated uniform finite-interval estimate. For an exponentially
weighted infinite sum, take the largest weight on each block and
sum the geometric progression with ratio exp(-2sL/N). Positivity
justifies the bound without exchanging a conditionally convergent
sum. After multiplication by log N/N its limsup is at most log a/(2s).
Taking the fixed pressure slack to zero only after the N limsup gives
P_*/(2s). This is stronger than the scalar bound because the maximizing
Weyl index is allowed to change at every time.

On the Pell sequence put V=U^(2r), epsilon=max_v |Tr(T_v^*V)|/N,
and q_k=max_v |Tr(T_v^*V^k)|^2/N^2. The same two-vector Gram calculation
gives q_k+q_(k+1)<=1+epsilon, with different maximizing indices allowed,
and q_1=epsilon^2. For t=exp(-4sr/N), an even-odd pair satisfies

q_(2j)+t q_(2j+1)
=(1-t)q_(2j)+t(q_(2j)+q_(2j+1))
<=1+epsilon t.

Separating the first term and summing all subsequent pairs therefore
gives exactly

sum_(k>=1) t^k q_k <= t epsilon^2+t^2(1+epsilon t)/(1-t^2).

Since epsilon tends to zero and 1-t^2 is asymptotic to 8sr/N,
multiplication by r/N gives limsup at most 1/(8s). There is no
pointwise conclusion that q_2 is small. The estimate still permits
total normalized return energy of order N/log N; it does not prove
the order-one pair bound or H_diag.
