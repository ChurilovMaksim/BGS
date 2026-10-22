# Root lifting, local Sine2 statistics, and a sufficient-only resonance target

**Stable claim:** `BGS-TRACE-085`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Abstract spectra, including deterministic existence via CUE local-average variance. Does not identify root labels or traces of the maintained propagator.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S05` is preserved verbatim in [the imported record](../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s05). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../evidence/executions/20261016/chat-integration/receipt.json).


Date: 2026-10-15. Status: exact spectral constructions and a probabilistic existence argument. This is not a proof of BGS for the fixed analytic propagator, not a counterexample to that propagator, and not a priority claim. The original note predates the integration recorded below.

## 1. What is being corrected

For a unitary spectrum of dimension N and an integer d, the condition

\[
 E_{N,d}([a,b])=N^{-2}\sum_{aN\le rd\le bN}|\operatorname{Tr}U_N^{rd}|^2\longrightarrow0
\]

can be useful for deleting the d-divisible time sector from a particular proof. It is NOT necessary for the complete signed microscopic CUE comparison, even when the origin-averaged spectrum has Sine2 correlations of every fixed order. The construction below proves this distinction. It does not assert that this sufficient condition is false for the physical BGS model.

## 2. Exact root-cover identity

Let V have dimension q and phases phi_j in [0,1). For an integer d >= 1, put N=dq and define a diagonal unitary L_d(V) with phases

\[
 \theta_{a,j}=(a+\phi_j)/d,\qquad 0\le a<d,\quad 1\le j\le q.
\]

For a spectrum theta of size N, define its periodic unfolded point measure, centered at alpha, by

\[
 \Xi_{N,\alpha}=\sum_{j=1}^N\sum_{k\in\mathbb Z}
                 \delta_{N(\theta_j-\alpha+k)}.
\]

Then, identically as locally finite point measures,

\[
 \Xi^{L_d(V)}_{N,\alpha}=\Xi^V_{q,d\alpha\bmod1}.
\]

Proof: write each position as q(phi_j-d alpha+a+dk), and use the bijection (a,k) -> a+dk from {0,...,d-1} x Z to Z. Thus the laws under uniform alpha agree EXACTLY, before taking any limit. This includes every bounded local functional and, where integrable, every local factorial moment. The unfolded nearest-neighbor gap list is the gap list of V repeated d times.

Consequently, if a deterministic sequence V_q has the origin-averaged Sine2 limit and locally uniformly integrable count moments of every fixed order, L_{d_q}(V_q) has the same limit for ANY positive integer sequence d_q. In particular d_q may tend to infinity. For odd total dimensions choose q and d_q odd.

## 3. Exact traces and concentration of all energy on sparse times

Summing the d-th roots of unity gives

\[
 \operatorname{Tr}L_d(V)^m=
 \begin{cases}
 0,&d\nmid m,\\
 d\operatorname{Tr}V^{m/d},&d\mid m.
 \end{cases}
\]

Also L_d(V)^d has the spectrum of V repeated d times. Hence

\[
 E_{dq,d}([a,b])=q^{-2}\sum_{aq\le r\le bq}|\operatorname{Tr}V^r|^2.
\]

The proportion of active times is 1/d, but the normalized collective mass need not vanish.

## 4. A deterministic choice of base spectra with nonzero limiting energy

Initially sample V_q from Haar U(q). Fix 0<a<b<1/2. The exact trace moment identities give, for integers r,s with r+s <= q,

\[
 \mathbb E|\operatorname{Tr}V_q^r|^2=r,
 \quad
 \operatorname{Cov}(|\operatorname{Tr}V_q^r|^2,
                    |\operatorname{Tr}V_q^s|^2)=\delta_{rs}r^2.
\]

Thus, with H_q=q^{-2} sum_{aq<=r<=bq}|Tr V_q^r|^2,

\[
 \mathbb EH_q=q^{-2}\sum_{aq\le r\le bq}r
          \longrightarrow (b^2-a^2)/2>0,
 \qquad
 \operatorname{Var}H_q=q^{-4}\sum_{aq\le r\le bq}r^2=O(q^{-1}).
\]

For a fixed real smooth weight w supported in (0,1/2), the analogous formulas are

\[
 \mathbb EH_q(w)=q^{-2}\sum_r r w(r/q)\to\int tw(t)dt,
 \quad
 \operatorname{Var}H_q(w)=q^{-4}\sum_r r^2 w(r/q)^2=O_w(q^{-1}).
\]

These are finite CUE identities, not an independence assumption for a deterministic propagator.

### Why randomness can be removed

On the circle of unfolded length q, the CUE correlation kernel is, up to a gauge,

\[
 K_q(x,y)=\frac{\sin\pi(x-y)}{q\sin(\pi(x-y)/q)},\qquad K_q(x,x)=1.
\]

For circular distance D <= q/2, its modulus is at most min(1,1/(2D)). For each fixed compactly supported local factorial test, the variance of its spatial average is O(1/q):

* Terms in the square sharing at least one point have their two anchors within a fixed distance, have integration volume O(q), and are divided by q^2. All other integrations have bounded volume and all correlation determinants are bounded by one.
* For two disjoint configurations whose anchors are far apart, subtract the product of the two correlation determinants from the joint determinant. Every remaining permutation has at least two edges joining the configurations. The absolute value is therefore bounded by C/(1+D)^2. Its integral over the relative anchor is bounded uniformly in q, again yielding O(1/q).

The means converge to the Sine2 factorial integrals, by local convergence of the kernel and the determinant bound. Apply Chebyshev to any finite family of tests together with H_q. A diagonal selection over countably many dense test families chooses deterministic realizations V_q for which all these limits hold simultaneously. The same selection includes local count moments, giving the uniform integrability needed for the point-process and correlation statements. Smooth Schwartz tests follow by partitioning into unit boxes and bounding mixed count moments by Holder; the summable test tails then vanish uniformly.

This proves EXISTENCE of deterministic simple base spectra, not an explicit closed-form formula for their points. The numerical verifier samples finite CUE matrices and is not used to prove this deterministic existence.

For such a deterministic base sequence and d_q -> infinity,

\[
 \Xi^{L_{d_q}(V_q)}_{d_qq}\Rightarrow\mathrm{Sine}_2,
 \qquad E_{d_qq,d_q}([a,b])\longrightarrow(b^2-a^2)/2>0.
\]

## 5. How the full signed pair comparison nevertheless holds

Define the signed pair statistic

\[
 J_N(w)=N^{-2}\sum_{m\ge1}w(m/N)
                  (|\operatorname{Tr}U_N^m|^2-\min(m,N)).
\]

For the root cover, its actual part is H_q(w), and the N-dimensional CUE reference tends to integral w(t)min(t,1)dt. In the stable band (0,1/2), both limits are integral t w(t)dt. Hence J_N(w) -> 0, while the entire positive actual energy lies on d-divisible times.

For d -> infinity, the reference mass restricted to d-divisible times is O(1/d). Therefore the signed discrepancy on that sector tends to +integral tw(t)dt, and the complementary signed discrepancy tends to the negative of the same number. The full comparison is correct. This is cancellation between DISCREPANCIES, not between nonnegative trace energies.

The distinction is relevant to the all-order signed Fourier formulation too: the exact point-process identity in Section 2 preserves every fixed local correlation, independently of a chosen decomposition of time indices.

## 6. Robustness and prime dimensions

### Removing exact spectral root symmetries

Perturb every lifted phase by at most N^{-4}, choosing the perturbations outside the countable collection of hyperplanes corresponding to rational phase differences. All nonzero powers then have simple spectra. The local unfolded shifts are O(N^{-3}), so the local limit and fixed count moments are unchanged. For m <= bN,

\[
 |N^{-1}\operatorname{Tr}\widetilde U_N^m-
   N^{-1}\operatorname{Tr}U_N^m|\le 2\pi bN^{-3}.
\]

Summing the resulting difference of squared normalized traces over O(N) times costs O(N^{-2}). Thus the nonzero sector energy persists after removing every exact rational eigenvalue ratio.

### Matching split prime cat periods

Let p run through any split prime sequence for which d_p=ord_p(S), d_p | p-1, and q_p=(p-1)/d_p -> infinity. Root lifting gives p-1 eigenphases. Add one distinct phase to obtain dimension p. The unfolding changes by the factor p/(p-1) -> 1; the added point meets a bounded microscopic window with probability O(1/p). All local correlation limits persist, using the uniform local count moments from Section 4.

For a compactly supported smooth positive stable-band weight, the trace at a resonant time is d_p Tr V_{q_p}^r plus one unit complex number. Its additional contribution to the square-root energy is at most sqrt(O(q_p))/p -> 0. The rescaling of the weight from r/q_p to rd_p/p tends to one. Hence the weighted resonant energy remains positive. Arbitrarily small generic phase perturbations can again remove exact rational ratios.

This construction is not the prescribed matrix exp(i tau p A_p)M_p. It only demonstrates that even matching the prime dimensional sequence and the arithmetic time set does not turn sector deletion into a necessary consequence of the local law.

## 7. What the block spectrum forgets

For any U and d, let C=U^d. With a fixed Borel branch of Arg in [0,2pi), define

\[
 R_d(C)=\exp(i\operatorname{Arg}(C)/d),\qquad
 Z=U R_d(C)^{-1}.
\]

Then Z commutes with C and Z^d=I. Thus U=Z R_d(C). Knowledge of C alone loses the root labels, equivalently the joint spectral information of (C,Z). Every statistic based solely on |Tr C^r|^2 loses these labels as well. No new estimate for the physical pair (C,Z) is claimed here.

## 8. Remaining physical problem

The prescribed tau=10^-80 and matrices A_N,M_N have not been changed. No estimate proving J_N(w)->0 for that family has been obtained in this note. The every-fixed-order signed factorial comparison remains the actual target. The residue-sector condition can still be chosen as a sufficient route, but should not be called an indispensable last lemma.

The earlier Gaussian echo used e^{it A_N/sqrt(n_N)} rather than e^{i tau N A_N}; its effective classical coupling tends to zero. Substituting t=tau N sqrt(n_N) into an estimate valid for fixed t gives no control of the physical asymptotic limit. That Gaussian statement is not used here.

## Sources and verification

External inputs checked in primary sources:

1. P. Diaconis and S. N. Evans, Linear functionals of eigenvalues of random matrices, Theorem 2.1. Primary author report: https://statistics.berkeley.edu/sites/default/files/tech-reports/577.pdf .
2. A. Soshnikov, Determinantal random point fields, arXiv:math/0002099, the finite CUE kernel and determinantal correlation formalism. The O(1/q) local-average variance argument needed above is supplied in Section 4.

`verify_root_lift.py` checks the exact trace identity, the unfolded point sets for common origins, repeated spacing lists, and finite CUE energy calibration. It records a fixed random seed and numerical tolerances. `verification.json` is the output of the executed verifier. None of its finite runs establishes Sine2 universality for the physical propagator.


## Additional exact root-label statements from the authored record

<a id="sec-041"></a>

## 9. Один и тот же блок $U^d$ не определяет локальный закон $U$

Для $N=dq$:
$$
U_N^+=\operatorname{diag}_{a,j}e^{2\pi i(a+\varphi_j)/d},
\qquad
U_N^-=\operatorname{diag}_{a,j}e^{2\pi i\varphi_j/d}.
$$
Они имеют одинаковую полную $d$-ю степень. У первого локальный закон
равен базовому по (X4), у второго все уровни сосредоточены в дуге длины
$1/d$, и слабый локальный предел пуст при $d\to\infty$.

Малое общее расщепление остаточных фаз делает спектр общей степени простым,
не меняя различия локальных пределов. Поэтому даже полное знание
простого спектра блока не восстанавливает распределение выбранных корней.

Точная факторизация при $C=U^d$:
$$
U=Z\,R_d(C),
\qquad
R_d(C)=e^{i\operatorname{Arg}(C)/d},
\qquad
Z^d=I,\quad[Z,C]=0.
\tag{X5}
$$
Для блока $\zeta^{-1}U^d$ сначала снимается одна фиксированная глобальная
фаза $U$.

Необходима совместная спектральная информация $(C,Z)$, а не только $C$.

<a id="sec-042"></a>

## 10. Точное локальное сведение к помеченным секторам

Разложим фазы:
$$
\theta_j=\frac{a_j+\varphi_j}{d},
\qquad a_j=\lfloor d\theta_j\rfloor,
\qquad q=N/d.
$$
Число $q$ не обязано быть целым. При равномерных $a\in\{0,\ldots,d-1\}$,
$y\in[0,1)$, $\alpha=(a+y)/d$ определим
$$
\Xi^{\rm sec}_{a,y}
=
\sum_{j:a_j=a}\sum_{n\in\mathbb Z}
\delta_{q(\varphi_j-y+n)}.
$$
На окне $[-L,L]$ оно совпадает с истинным процессом, если
$L/q<y<1-L/q$. Следовательно,
$$
\boxed{
d_{\rm TV}\left(
\mathcal L(\Xi^U|_{[-L,L]}),
\mathcal L(\Xi^{\rm sec}|_{[-L,L]})
\right)
\le\min(1,2Ld/N).
}
\tag{X6}
$$

При $d=o(N)$ это эквивалентность слабых локальных пределов.
Для корреляционных моментов нужны дополнительные моментные оценки.
При $d\asymp N$ ошибка не обязана исчезать. Применение к физическим
помеченным секторам не закончено.

