# A quantitative route from parameter averages to the fixed-coupling BGS problem

**Stable claim:** `BGS-TRACE-087`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Only the reduction is proved. The required physical parameter q-moment o(N^-2), or sixth moment O(N^-3), is unproved; Haar sixth moments cannot supply it.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S11` is preserved verbatim in [the imported record](../record/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s11). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

**Status.** The finite parameter-bandwidth theorem, the de-averaging inequality, and the CUE reference moment bounds below are mathematical deductions. The required parameter-moment estimate for the prescribed BGS matrices is **NOT proved**. No BGS solution, external refereeing, formal verification, or priority claim is made. Original research note; subsequently integrated with the review below.

## 1. Original operator and target are retained

Let A_N be Hermitian, M_N unitary, and assume a uniform bound

\[
\|A_N\|_{\mathrm{op}}\le C.
\]

Set

\[
U_N(t)=e^{itNA_N}M_N.
\]

For the physical BGS family N runs over odd integers, C may be taken as 79/50, the physical parameter is t_*=10^{-80}, and A_N,M_N are exactly the matrices used by the previous research packets. In particular, with

\[
r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\quad e^{i\alpha}=(-3+4i)/5,
\]

A_N has diagonal

\[
\cos(14\pi x/N)+r(x/N)/10+r(x/N)\sin(2\pi x/N)/100-1/10
\]

and upper cyclic edge

\[
(A_N)_{x,x+1}=e^{-i\alpha}r(((x+2^{-1})\bmod N)/N)/200.
\]

The lower edge is its conjugate. Modular inverses are taken modulo odd N. Also

\[
(M_N)_{xy}=N^{-1/2}\exp\{-2\pi i8^{-1}(3x^2-2xy+3y^2)/N\}.
\]

The bound C follows from a diagonal absolute bound 1.54 and a total off-diagonal row bound 0.04. Small-size aliasing does not affect this bound.

Fix real w in C_c^infinity((0,B)), B finite. The signed pair target is

\[
J_{N,w}(t)=N^{-2}\sum_{m\ge1}w(m/N)
   (|\operatorname{Tr}U_N(t)^m|^2-\min(m,N)).                 \tag{1}
\]

All active times, resonant and nonresonant, are retained. No assertion that a selected sector separately vanishes is imposed.

## 2. Exact Fourier bandwidth in the coupling parameter

**Theorem 1.** As a function of real t, J_{N,w} is a finite exponential polynomial with angular Fourier frequencies contained in

\[
[-\Omega_N,\Omega_N],\qquad \Omega_N=1+2CBN^2.              \tag{2}
\]

Moreover

\[
\sup_{t\in\mathbb R}|J_{N,w}(t)|\le C_w N.                 \tag{3}
\]

No independence, spectral gap, Diophantine bound, or absence of eigenvalue collisions is used.

**Proof.** Write A_N=sum_j a_j P_j using its distinct spectral values; repeated eigenvalues are permitted. Then

\[
e^{itNA_N}=\sum_j e^{itNa_j}P_j.
\]

Every term in Tr U_N(t)^m has frequency N(a_{j_1}+...+a_{j_m}), whose absolute value is at most CmN. For real t the conjugate trace has the negative frequencies. Hence the squared trace has bandwidth at most 2CmN. The active m satisfy m<BN. The constant CUE subtraction only adds frequency zero. Finally |Tr U^m|<=N and there are O_w(N) terms in (1). This proves (2)-(3).

This is an exact bound on frequencies **in the scalar parameter t**. It is not an Egorov time window or a bound on frequencies of the classical symbol.

### All fixed factorial orders

For a nonnegative bandlimited Schwartz test b, with supp b_hat subset [-B,B], use the previous packet's scalar coefficient

\[
\Delta_{k,N}(t;b)=\frac1{k!N^k}
 \sum_{m_1+...+m_k=0}\prod_a\widehat b(m_a/N)
 \{D_{U_N(t)}(m_1,...,m_k)-\mathbb E_{\mathrm{CUE}(N)}D_V(m_1,...,m_k)\}.
                                                               \tag{4}
\]

The partition-Mobius formula expresses D as products of traces of positive and negative powers. For every partition, the sum of absolute block powers is at most sum_a |m_a|<=kBN. Expand inverse powers using U_N(t)^{-1}=M_N^{-1}e^{-itNA_N}. It follows that (4) is a finite exponential polynomial of bandwidth at most CkBN^2, and

\[
\sup_{t\in\mathbb R}|\Delta_{k,N}(t;b)|\le C_{k,b}N^{k-1}. \tag{5}
\]

The bound in (5) also follows directly from |D|<=N^k and the O_{k,b}(N^{k-1}) active lattice tuples. Thus the parameter bandwidth remains order N^2 at every **fixed** correlation order.

## 3. Local de-averaging theorem

Let F be a finite exponential polynomial with frequencies in [-Omega,Omega], Omega>=1, and sup_R |F|<=M. Let I be a fixed bounded interval and K a compact subset of its interior; write delta=dist(K,R\I)>0. Let q>1.

Choose chi in C_c^infinity(R), chi=1 on [-1,1], and let

\[
k(x)=\frac1{2\pi}\int e^{ix\xi}\chi(\xi)\,d\xi,\qquad
 k_\Omega(x)=\Omega k(\Omega x).
\]

Termwise integration of the finite exponential polynomial gives the exact identity F=k_Omega*F. Holder's inequality on I, and rapid decay of k on the complement, give for every A>0

\[
\boxed{
\sup_{t\in K}|F(t)|
\le \|k\|_{q'}\Omega^{1/q}
          \left(\int_I|F(s)|^qds\right)^{1/q}
   +C_A M(\Omega\delta)^{-A},\qquad q'=q/(q-1).
}                                                               \tag{6}
\]

The constants depend on the fixed kernel, q,A and the interval separation, not on the number or spacing of exponential frequencies. No lower bound on a difference of frequencies is required.

### Explicit reproducing kernel

The first kernel may alternatively be chosen with arbitrarily high finite regularity and an explicit formula. For an integer r>=1 set

\[
k_r(x)=\frac{\sin(2x)}{\pi x}
       \left(\frac{\sin(x/(2r))}{x/(2r)}\right)^{2r}.        \tag{7}
\]

Its Fourier transform is the convolution of 1_{[-2,2]} with the probability density of a sum of 2r uniform variables on [-1/(2r),1/(2r)]. Thus it is one on [-1,1] and zero outside [-3,3]. Consequently it reproduces the same bandwidth. Its explicit tail estimate is

\[
\int_{|x|\ge T}|k_r(x)|dx
 \le\frac{(2r)^{2r}}{\pi r}T^{-2r}.                         \tag{8}
\]

The inequality remains valid when the right-hand side is large. Replacing the last term of (6) by M(2r)^{2r}/(pi r)(Omega delta)^(-2r) gives a fully explicit finite-tail form. Increasing a fixed r controls any prescribed polynomial M_N.

### Application to the exact BGS family

Theorem 1 and (6) imply, for every fixed q>1 and every A>0,

\[
\boxed{
\sup_{t\in K}|J_{N,w}(t)|
\le C_{I,K,w,q}N^{2/q}
       \left(\int_I|J_{N,w}(t)|^qdt\right)^{1/q}
       +O_{I,K,w,A}(N^{1-2A}).
}                                                               \tag{9}
\]

Therefore

\[
\int_I|J_{N,w}(t)|^qdt=o(N^{-2})
\quad\Longrightarrow\quad
\sup_{t\in K}|J_{N,w}(t)|\longrightarrow0.                 \tag{10}
\]

In particular, a **physical parameter** sixth-moment bound

\[
\int_I|J_{N,w}(t)|^6dt=O_{I,w}(N^{-3})                     \tag{11}
\]

would give

\[
\sup_{t\in K}|J_{N,w}(t)|=O_{I,K,w}(N^{-1/6}).             \tag{12}
\]

More generally any O(N^{-2-epsilon}) qth-moment input gives O(N^{-epsilon/q}). Normalizing the integral by |I| only changes constants for a fixed interval.

For the literal parameter one may choose I=(t_*/2,3t_*/2), K=[3t_*/4,5t_*/4]. Both are fixed independently of N. The constants are allowed to depend on t_*, and the reconstruction kernel only becomes narrowly localized inside I after N^2 t_* grows large. No practical startup threshold or extrapolation from t=0.03 is asserted.

### All-order conditional closure

The same proof applied to (4)-(5) shows: if, for every fixed k and admissible b,

\[
\int_I|\Delta_{k,N}(t;b)|^6dt=O_{I,k,b}(N^{-3}),            \tag{13}
\]

then all these factorial coefficients converge uniformly on compact subsets of I to their CUE reference values. The previous packet's finite Bonferroni/Toeplitz comparison then gives the origin-averaged Sine2 process at each fixed t in int(I), including t_*. Its all-fixed-order moment control supplies local UI. No uniformity in growing k or growing Fourier support is required.

Equation (13) is a **sufficient, currently unproved physical input**, not an established assertion about U_N(t). This theorem does not turn an annealed mean, an almost-everywhere limit, or a CUE theorem into the desired input.

## 4. Why the rate matters: a sharp bandwidth obstruction

For any fixed t_* put

\[
F_N(t)=\left[\frac{\sin(N^2(t-t_*)/2)}{N^2(t-t_*)/2}\right]^2.
                                                               \tag{14}
\]

It is bounded by one, equals one at t_*, and has Fourier support in [-N^2,N^2]. For every fixed interval with t_* in its interior,

\[
\int_I |F_N(t)|^6dt\asymp N^{-2},\qquad F_N(t_*)=1.       \tag{15}
\]

In fact

\[
\int_{\mathbb R}\left(\frac{\sin x}{x}\right)^{12}dx
=\frac{655177}{1663200}\pi,
\quad
N^2\int_{\mathbb R}|F_N(t)|^6dt
=\frac{655177}{831600}\pi.
\]

The obstruction also occurs within the narrower class of **finite exponential polynomials**. With M=N^2, set

\[
G_N(t)=\left|\frac1M\sum_{j=0}^{M-1}e^{ij(t-t_*)}\right|^2.
\]

It is nonnegative, bounded by one, equals one at t_*, and has bandwidth M-1. For |t-t_*|<=pi it is bounded by min(1,pi^2/(M^2|t-t_*|^2)). For |t-t_*|<=1/M its value is at least cos(1/2)^2, by centering the phases in the geometric sum. Therefore the integral of G_N^6 on any fixed neighborhood of t_* of width less than one period is bounded above and below by positive constants times 1/M=N^{-2}. The verifier checks five such examples by exact integer coefficient convolution and independent alias-free Fourier quadrature.

Thus O(N^{-2}), without little-o improvement, does not force pointwise decay in the general bandwidth class. This is not claimed to be a BGS-matrix counterexample. It shows why an uncontrolled exceptional value cannot be dismissed solely from averaged convergence.

The natural CUE orders are second moment N^{-1}, fourth moment N^{-2}, sixth moment N^{-3}. The sixth is the first such even moment whose rate is strictly stronger than the N^{-2} bandwidth threshold. Nothing intrinsic about quantum dynamics singles out six; other quantitative qth-moment bounds can be used in (10).

## 5. CUE sixth-moment benchmark at arbitrary fixed bands

This section is ONLY a reference-ensemble result. It is not the physical assertion (11) or (13).

On the circle of length N, CUE is determinantal with projection kernel

\[
K_N(x,y)=\frac1N\sum_{j=0}^{N-1}e^{2\pi ij(x-y)/N}.
\]

For circular distance d_N, uniformly in N>=2,

\[
|K_N(x,y)|\le\min(1,(2d_N(x,y))^{-1}),\quad
\int_0^N|K_N(x,y)|^2dy=1,\quad
\int_0^N|K_N(x,y)|dy=O(\log(2N)).                           \tag{16}
\]

Consider an ordered fixed-k local U-statistic

\[
S_N=\sum_{j_1,...,j_k\text{ distinct}}
 H_N(x_{j_1},...,x_{j_k}),
\]

where H_N is the periodization of a translation-invariant Schwartz function of k-1 relative coordinates. For fixed k and fixed kernel,

\[
\operatorname{Var}(S_N)=O(N),\qquad
|\operatorname{cum}_r(S_N)|\le C_r N\log(2N)^{r-1},\quad r\ge2.
                                                               \tag{17}
\]

Here is the complete mechanism of the bounds. It is standard determinantal cumulant calculus, supplied to delimit the reference statement rather than claim novelty.

1. Expand a product of r copies of S_N by partitions of their kr point labels. Two labels in the same copy cannot be identified, since each copy is factorial. Each admissible global identification gives an integral against a determinantal correlation function in v<=kr distinct positions.
2. Expand each determinant into permutations. A diagram has (a) one fixed local hyperedge for each copy of H_N, (b) identifications from the label partition, and (c) directed K_N edges of the permutation. In the cumulant, the coefficient of such a diagram is the sum of partition-Mobius coefficients over partitions of the r copies coarser than its connectivity partition. This sum is zero unless the diagram connects all r copies. The determinant-permutation sign is unchanged by this cancellation.
3. Since the relative-coordinate kernel is Schwartz, for any sufficiently large fixed L it is bounded by a constant times a product of k-1 periodized envelopes h_N(x_i-x_k), with h(x)=(1+|x|)^(-L). These envelopes have uniformly bounded L1 and Linfinity norms. The hyperedge graph has c<=r connected components. Retain a spanning forest of its envelope edges and c-1 kernel edges connecting those components. Discard the remaining bounded factors. Integrating this spanning tree gives N times uniformly bounded L1 envelope factors and at most r-1 L1 norms of K_N. This proves the cumulant bound in (17). All sums of diagrams are finite for fixed k,r.
4. For r=2 the logarithm can be removed. If the two source copies share a point, their hyperedge graph is connected, and its integrable envelopes give O(N). If their positions are disjoint, a connected determinant permutation has at least two cross-edges between them. Integrate the relative anchor displacement s using
   \[
   \int_0^N |K_N(s+a)K_N(s+b)|ds\le1
   \]
   by Cauchy-Schwarz and (16). The internal relative coordinates are controlled by the L1 Schwartz envelopes. This also gives O(N), proving the variance assertion.

For the centered normalized real statistic Y_N=(S_N-E S_N)/N, (17) gives

\[
\kappa_2(Y_N)=O(N^{-1}),\qquad
\kappa_r(Y_N)=O(N^{1-r}\log(2N)^{r-1}).
\]

The exact sixth central-moment formula is

\[
E Y_N^6=\kappa_6+15\kappa_4\kappa_2+10\kappa_3^2+15\kappa_2^3.
\]

The first three terms are O(N^{-5}log^5 N), O(N^{-4}log^3 N), and O(N^{-4}log^4 N). The last is O(N^{-3}). Hence

\[
\boxed{E|Y_N|^6=O(N^{-3}).}                                 \tag{18}
\]

For (1), take the even extension W(x)=w(|x|), put phi=Fourier^{-1}(W), and periodize phi on the unfolded circle. The Fourier identity gives exactly

\[
J_{N,w}(V)=\frac1{2N}\left(
 \sum_{i\ne j}\phi_N(x_i-x_j)
 -E_{\mathrm{CUE}}\sum_{i\ne j}\phi_N(x_i-x_j)\right).
\]

Thus (18) proves the CUE bound E|J|^6=O_w(N^{-3}) for **every fixed compact band**, including bands above the plateau threshold m/N=1.

The same argument applies to each fixed scalar factorial coefficient M_{k,N}(b). Indeed its translation-invariant kernel is

\[
H_b(x_1,...,x_k)=\int_{\mathbb R}\prod_{a=1}^k b(x_a-t)dt,
\]

Schwartz in the relative coordinates, and M_{k,N} is its normalized ordered U-statistic with the factor 1/k!. Consequently the CUE sixth centered moment has the rate appearing in the unproved physical input (13).

### Independent stable-band calibration

When 6m_max<=N, the exact Diaconis--Evans trace moment theorem permits a shorter check. The moments through order six of J equal those of

\[
N^{-2}\sum_m m w(m/N)(E_m-1),
\]

where E_m are independent mean-one exponential variables. Its cumulants are

\[
\kappa_r=(r-1)!N^{-2r}\sum_m m^r w(m/N)^r.
\]

The same sixth-moment formula agrees with exact rational moment convolution. This shortcut is used by the verifier only in its proper stable range. The proof outside that range is the connected-determinant argument above, not an extension of Gaussian trace independence.

## 6. The physical parameter integral still needs a new estimate

The bandwidth reduction also gives an exact description of the missing moment. Write the actual real exponential polynomial as

\[
J_{N,w}(t)=\sum_\gamma a_\gamma e^{i\gamma t},\qquad
a_{-\gamma}=\overline{a_\gamma}.
\]

Collect the frequencies of its cube:

\[
J_{N,w}(t)^3=\sum_\lambda b_\lambda e^{i\lambda t}.
\]

For I=(c-L/2,c+L/2), exactly

\[
\boxed{
\int_I |J_{N,w}(t)|^6dt
=L\sum_{\lambda,\mu} b_\lambda\overline{b_\mu}
 e^{ic(\lambda-\mu)}
 \operatorname{sinc}\!\left(\frac{L(\lambda-\mu)}2\right),
}\tag{19}
\]

with sinc x=sin x/x. This is a positive Gram form in the complete complex coefficients b, not a sum of independent positive diagonal contributions.

In the A_N eigenbasis, coefficients of Tr U_N(t)^m are cyclic products of entries of the transformed M_N, grouped by occupation vectors. Formula (19) therefore retains the exact model and all signs. No approximation of e^{itN Op(g)} by Op(e^{itNg}) is used.

I checked the occupation expansion and (19) by independent finite matrix evaluations. I did **not** derive O(N^{-3}) or o(N^{-2}) for (19) in the physical family. Small frequency gaps can occur among the many occupation sums. Merely excluding exact algebraic relations does not bound the Gram form; replacing its off-diagonal terms by absolute values destroys the cancellations one is trying to establish.

The result is therefore a quantitative **conditional route** to the desired fixed parameter, not an actual deterministic universality theorem. It is also not a legitimate reason to import CUE's sixth moment into a one-parameter quantum family.

## 7. Relation to the attempted determinant route

The repository already contains a spectrum with exactly the CUE second covariance of its characteristic polynomial and a non-CUE local law. I therefore did not use a determinant-covariance criterion. Its determinant-ratio formula correctly preserves the missing information, but the required microscopic ratio estimate remains unproved.

The contribution of this packet is different: bounded generators give an exact N^2 parameter bandwidth, allowing a sufficiently rapid moment estimate on an interval to be turned into a fixed-parameter theorem without leaving an exceptional algebraic value unaddressed. This is elementary Fourier interpolation applied to the exact quantum family, not a newly established physical moment estimate.

## 8. Verification, sources, and limits

`verify_deaveraging.py` is self-contained and does not import previous research code. It checks:

- parameter-frequency expansions of the exact BGS matrix prescription at N=3,5,7, with 18 evaluations against direct matrix exponentials and powers;
- the sinc Gram formula for the sixth moment at N=3 against positive one-dimensional quadrature;
- nine Fourier reproduction tests for the explicit flat-top kernel, with a separate analytic tail bound;
- eighteen exact rational stable-CUE sixth-moment calculations by two independent formulas;
- nine exact rational connected-permutation/partition-Mobius determinant identities;
- the explicit sinc-spike integral and five exact finite Fejer-spike moment controls at the N^-2 scale.

All checks remain active under `python -O`. Floating-point controls are not interval-arithmetic certification, and none proves a limiting parameter moment for the physical coupling. N=7 is deliberately retained as an exceptional scalar-generator algebra check, not evidence for BGS.

Primary/background sources checked:

1. Diaconis--Evans, *Linear Functionals of Eigenvalues of Random Matrices*, Theorem 2.1, https://statistics.berkeley.edu/sites/default/files/tech-reports/577.pdf . Printed pages 3-4 were visually inspected. The theorem's weighted-degree condition is retained.
2. Soshnikov, *Determinantal random point fields*, https://arxiv.org/abs/math/0002099 . Determinantal and convergence background, not a theorem about the actual U_N.
3. Conrey--Farmer--Zirnbauer, *Howe pairs, supersymmetry, and ratios of random characteristic polynomials*, https://arxiv.org/abs/math-ph/0511024 . The result concerns Haar averages; none are imposed on the deterministic operator.
4. ChurilovMaksim/BGS, `supplement/fixed_map/weighted-secular/determinant_boundary.md` and `mathematics/heisenberg_pair_heat_formula.md`. These identify exact determinant reductions and explicitly unestimated physical terms.
5. Prior supplied `RESEARCH_STATUS.md` and `bgs_no_extra_ui_2026-10-15/THEOREM.md`. Their physical gap is retained; the latter supplies the already stated all-order Laplace closure.

**Final boundary:** equations (11), (13), and the corresponding o(N^-2) physical moment bounds remain unproved. The original all-odd-dimension Sine2 problem and general BGS are not closed by this packet.
