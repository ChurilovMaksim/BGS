# Accepted loop deductions: scoped author excerpt

Editorial excerpt of accepted sections 2–5; original content hash is recorded in provenance.json.

## 2. Exact project normalization and rate boundary

Keep U_N=exp(i tau N A_N)M_N, tau=10^-80, odd N. Randomness is only alpha uniform on [0,2pi). Put s_N(w)=N^-1 sum_j cot((theta_j-alpha)/2-w/N). Its atoms are N(theta_j-alpha)/2+pi N l, of unit mass with intensity 1/pi. Division of positions by pi gives intensity one; origin integration gives the deterministic anchored normalization 1/N. All finite-N moments off the real line exist even with multiplicities.

Use exactly the residual E_(p,N) in supplement/fixed_map/resolvent-flow/loop_bridge.md, equation (3), with holomorphic divided differences at coincident arguments. The repo's sufficient hypothesis (H) matches the theorem. It is a sufficient contract, not a claim of minimal necessary hypotheses. No rate for local convergence follows merely from unspecified o(1) residuals. The all-orders conclusion concerns compactly tested factorial measures, not pointwise densities or a fixed deterministic origin.

## 3. A smaller sufficient testing contract (project deduction)

The compact supremum in (H) need not be an independent estimate. Here is a rigorous replacement that still supplies it.

Fix a countable dense set D in C minus R. Require:

(A) For each integer r>=2, at the single conjugate diagonal tuple with first argument i, r-2 further arguments i and r arguments -i (order p=2r-1),

|E_(2r-1,N)| / (1+E_alpha |s_N(i)|^(2r)) -> 0.

(B) For each p and each mixed tuple in D^p,

|E_(p,N)(w)| / (1+E_alpha max_j |s_N(w_j)|^(p+1)) -> 0.

Same-half-plane tuples need not be tested: their residuals vanish identically for every unitary spectrum. Conditions (A) and (B) are still unknown for the prescribed map. They do not reduce the order quantifier to finitely many equations.

Proof. Let Z=s_N(i). In (A), the leading term is E|Z|^(2r). The other terms have magnitude at most C_r E|Z|^(2r-2): the divided-difference derivative is bounded by C|Z| for arguments i,-i, and the remaining product has degree 2r-3. Young's inequality absorbs this term and the relative o(1) to yield a uniform 2r-th moment bound. The Nevanlinna derivative inequality |s'(z)|<=|s(z)|/Im z and integration along fixed paths from i imply sup_K|s|<=C_K|s(i)| for every upper-half-plane compact K, with reflection treating lower K. Thus all compact-supremum moments are bounded. In (B), denominators are now bounded, so the residuals tend to zero on D^p. Each residual is holomorphic on every sign component of (C minus R)^p, including removable same-half-plane diagonals, and uniformly locally bounded by the moment bounds and Cauchy derivative estimates. Montel compactness and continuity on the dense tuples imply compact-uniform convergence to zero. This proves (H), and the existing exact correlation bridge applies.

This is a quantifier reduction, not a solution or a claim of globally weakest possible conditions. It eliminates a separate uniform-in-spectral-arguments obligation, provided the single-anchor all-order bootstrap is proved. It does not eliminate the long-time spectral content.

## 4. Actual-model short-leg excision in the first mixed loop

Fix s in a compact interval of (0,infinity), q=exp(-2s/N),

L=N^-2 sum_(m>=1) q^m |p_m|^2,
C=N^-3 sum_(a,b>=1) q^(a+b) p_(-a)p_(-b)p_(a+b).

The exact first mixed residual is 8i[L+C-1/(4s^2)]. Let K=floor(c log N), with c no greater than the constant in FM-007, and

B=N^-1 sum_(a=1)^K q^(a/2)|p_a|.

For arbitrary unitaries and each a,

sum_(b>=1) q^(a+b)|p_b p_(a+b)| <= q^(a/2) N^2 L,

by Cauchy–Schwarz applied to x_b=q^(b/2)p_b. Therefore, with C_long restricted to a>K and b>K, and L_long restricted to m>K,

|C-C_long| <= 2 B L,
0 <= L-L_long <= N^-2 sum_(m=1)^K |p_m|^2.

The first estimate bounds the union directly, without subtracting an uncontrolled overlap. The actual bound |p_m|<=C N^(39/40) on this logarithmic interval gives

B=O(K N^(-1/40)),   L-L_long=O(K N^(-1/20)).

Crucially this does not assume that L is bounded. For Z=s_N(is/2), E|Z|^2=1+4L. The mixed p=2 denominator is D=1+E|Z|^3, and Lyapunov gives D>=1+(1+4L)^(3/2). Hence

|[L+C]-[L_long+C_long]|/D
 <= O(K N^(-1/20)) + O(K N^(-1/40)) L/[1+(1+4L)^(3/2)]
 = O(N^(-1/40) log N).

The constants are uniform for s in any fixed positive compact interval. Thus the normalized first mixed equation is equivalent to the same equation with **all legs beyond the actual logarithmic window**, up to this explicit vanishing error. This is real supplied information, but says nothing about that remaining equation. The stronger fixed-j trace estimates do not automatically extend to a growing window.

## 5. Exact-quantization target after excision

There is a finite-dimensional expression for the surviving leaf, requiring neither infinite-series truncation nor path unmarking. Let X=U_N tensor conjugate(U_N), partial trace Tr_2 over the second tensor factor, and

F_K(q)=Tr_2[(qX)^(K+1)(I-qX)^(-1)].

Since ||qX||<1, exactly

F_K=sum_(a>K) q^a p_(-a) U_N^a,
L_long=N^-2 Tr F_K,
C_long=N^-3 Tr(F_K^2).

The square is algebraic, NOT F_K*F_K. The unresolved first mixed leaf is therefore

[ N^-2 Tr F_K + N^-3 Tr(F_K^2) - 1/(4s^2) ] / [1+E_alpha|s_N(is/2)|^3] ->0,

including its imaginary part. Even proving this one leaf does not establish all orders or identify the pair law by itself: it couples pair and cubic data.

Here exact quantization supplies

X=exp(i tau N [A_N tensor I - I tensor conjugate(A_N)])
  (M_N tensor conjugate(M_N)).

This ordered identity is a legitimate starting point for a model-specific bound of the displayed partial trace. It does not replace powers of X by an unordered exponential of transported generators. The resolvent is evaluated at distance 1-q of order 1/N; naive operator bounds cost order N. Compression to the diagonal coordinate algebra only gives P, not this nonlinear partial-trace expression. Q and finitely many controlled reconnection families likewise do not estimate its full signed square.

Executed exact algebra: check_exact.py verifies the partial-trace/geometric formula, once-counted short-leg decomposition, and pair normalization using an independent rational three-point spectrum, q=1/4, K=2. All checks passed with exact SymPy arithmetic. This is finite algebra verification, not a test of actual asymptotic cancellation. The analytic excision proof above applies to the actual map through the cited logarithmic theorem.

