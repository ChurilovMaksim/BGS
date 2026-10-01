# Why deterministic Heisenberg comparison must retain cancellation

**Claim ID:** `BGS-TRACE-010`. Date: 30 September 2026.
**Status:** project proof and author self-review; exact CUE calibration uses
the prior Diaconis--Evans moment theorem. Finite checks support the algebra.
The frozen-map BGS target is open. No external validation or priority is claimed.
The obstruction compares deterministic unitary spectra with the finite CUE
reference; no theorem for other random-matrix symmetry classes is asserted.

The absolute sufficient condition in [TRACE-003](trace_to_local_statistics_bridge.md)
is logically valid. Its simultaneous unaveraged application at every order
is impossible: pair absolute comparison forces higher absolute errors to
diverge. This note proves that obstruction, calibrates a signed cubic test,
and tests an explicit phase mechanism without treating an unrealized trace
table as a quantum system. Earlier signed cubic work is credited in the
[research review](../record/signed_heisenberg_review_20260930.md).

## 1. Quantitative cubic obstruction

Let $U_N$ be any unitary $N\times N$ matrix, $T_j=\operatorname{Tr}U_N^j$,
$A_j=|T_j|^2$, $T_{-j}=\overline{T_j}$. Fix $0<a<b$, $2b<1$, and put
$$
I_N=[aN,bN]\cap\mathbb Z,\quad L_N=|I_N|,\quad
J_N=[aN,2bN]\cap\mathbb Z,\quad \delta_j=A_j-j.
$$
Define two **absolute**, unaveraged discrepancies:
$$
\mathcal A_{2,N}=N^{-2}\sum_{j\in J_N}|\delta_j|,\qquad
\mathcal A_{3,N}=N^{-3}\sum_{m,n\in I_N}
|D_N(m,n,-m-n)-2(N-m-n)|.                         \tag{1}
$$
The factorial sum $D_N$ has the [partition--Möbius definition](trace_to_local_statistics_bridge.md).
The finite CUE cycle formula in [the supporting note](heisenberg_trace_support.md)
gives $\mathbb E_{\rm CUE}D_N(m,n,-m-n)=2(N-m-n)$ in this box.

**Theorem 1.** For every $0<\eta<a$, writing $\ell_N=L_N/N$,
$$
\mathcal A_{3,N}\ge
\sqrt N\,(a-\eta)\sqrt{2a-\eta}\,
\ell_N\bigl(\ell_N-3\mathcal A_{2,N}/\eta\bigr)_+
-3\ell_N\mathcal A_{2,N}.                         \tag{2}
$$
Consequently, if $\mathcal A_{2,N}\to0$, then
$$
\liminf_{N\to\infty}\frac{\mathcal A_{3,N}}{\sqrt N}
\ge (b-a)^2a\sqrt{2a}>0.                           \tag{3}
$$
For $a=1/8,b=1/4$, the constant in (3) is exactly $1/1024$.

**Proof.** The exact cubic identity is
$$
D_N=T_mT_n\overline{T_{m+n}}-A_m-A_n-A_{m+n}+2N,
$$
so its CUE-subtracted value is
$$
\Delta D_N=T_mT_n\overline{T_{m+n}}
             -\delta_m-\delta_n-\delta_{m+n}.       \tag{4}
$$
There are at most $N\mathcal A_{2,N}/\eta$ bad indices with
$|\delta_j|>\eta N$. Each bad index occurs as $m$, $n$, or $m+n$
in at most $L_N$ pairs of each type. Thus at least
$(L_N^2-3L_NN\mathcal A_{2,N}/\eta)_+$ pairs are good.
Their cubic product has modulus at least
$(a-\eta)\sqrt{2a-\eta}\,N^{3/2}$.
Across all pairs, the sum of the three $|\delta|$ terms is at most
$3L_NN^2\mathcal A_{2,N}$. Sum the reverse triangle inequality to
obtain (2). Then $\ell_N\to b-a$; let $\eta\downarrow0$ after taking
the liminf. No hypothesis on chaos, primes, or the kick is used. $\square$

Smooth nonnegative compact Fourier weights can be chosen at least one on
these boxes. Their inverse transforms are Schwartz tests. Absolute pair
comparison for every compact test implies the pair premise in (3), while
the corresponding absolute cubic comparison dominates (1). Therefore
**no deterministic sequence can satisfy that all-order absolute CUE criterion**.
Even imposing real or permutation-symmetric tests does not evade the result:
one can add the reflected and permuted bumps without decreasing either bound.

The theorem does not rule out the signed pair law, pair absolute comparison
alone, or an absolute comparison of quantities already averaged before
taking their modulus. It does not refute BGS or retract TRACE-003.

## 2. The obstruction persists at every fixed higher order

**Theorem 2.** Fix $k\ge3$, $q=k-1$, and $0<a<b$ with $qb<1$.
Let $I_N=[aN,bN]\cap\mathbb Z$, $J_N=[aN,qbN]\cap\mathbb Z$, and
assume $N^{-2}\sum_{j\in J_N}|A_j-j|\to0$. For
$m_1,\ldots,m_q\in I_N$, set $S=\sum_i m_i$, $m_k=-S$. Then
$$
\liminf_{N\to\infty}N^{1-k/2}N^{-k}
\sum_{m_1,\ldots,m_q\in I_N}
|D_N(m)-(-1)^q q!(N-S)|
\ge (b-a)^q a^{q/2}\sqrt{qa}>0.                    \tag{5}
$$
Every $k$-cycle has partial-sum span $S$: start just after its unique
negative mode and read the positive modes. No proper subset has zero sum.
The finite cycle formula therefore gives the displayed CUE reference.

To prove (5), call a tuple good if all its $2^q-1$ nonempty positive
subset sums have $|\delta_j|\le\eta N$, with $0<\eta<a$.
For a fixed subset and bad value, fixing all but one of its variables
leaves at most one choice. The number of bad tuples is at most
$(2^q-1)|\mathrm{Bad}|L_N^{q-1}=o(N^q)$.
On good tuples the singleton partition has modulus at least
$(a-\eta)^{q/2}\sqrt{qa-\eta}\,N^{k/2}$.
Every block in a proper partition has nonzero mode equal, up to sign,
to a positive subset sum. Its trace modulus is at most
$\sqrt{(qb+\eta)N}$. All partitions with two to $k-1$ blocks contribute
$O_{k,b,\eta}(N^{(k-1)/2})$ in total. The one-block term and CUE
reference are $O_k(N)$, within that same bound. Reverse triangle on
good tuples, divide by $N^{k/2-1}$, and let $\eta\downarrow0$.
This is a theorem at each fixed $k$, with no uniform claim as $k\to\infty$.

## 3. The viable deterministic target

For a fixed compactly supported smooth Fourier weight $W$ and the matching
finite ensemble reference, the exact bridge instead requires
$$
N^{-k}\sum_{m\in\mathbb Z^{k-1}} W(m/N)
\left[D_{U_N}(m_1,\ldots,m_k)
       -\mathbb E_{\rm RMT}D_V(m_1,\ldots,m_k)\right]\longrightarrow0,
\quad m_k=-\sum_{i<k}m_i.                           \tag{6}
$$
The modulus, when used, is outside the entire sum. For every such $W$,
(6) is exactly the corresponding band-limited correlation comparison;
TRACE-004 gives the every-bandwidth extension under its stated positivity
hypotheses. Correct unfolding and symmetry reduction remain required.

On the positive cubic cone $m,n>0,m+n<N$, (4) identifies the first mixed
obligation. For $m,n<N<m+n$, the CUE raw cubic counterterm is $m+n-N$;
it cannot be replaced by zero. The prior
[high-band cubic calculation](../supplement/fixed_map/report-audit-20260919/cubic_variance.md)
already treats that different region. Equation (6) is not an estimate
for the maintained map.

## 4. Exact signed cubic variance in a stable CUE band

This is a calibration under actual Haar CUE, not an independent-Gaussian
assumption for the deterministic traces. Let
$I\subset\{1,\ldots,\lfloor N/4\rfloor\}$ and take arbitrary complex
weights $W_{mn}$ on $I^2$. Define
$$
X_W=N^{-3}\sum_{m,n\in I}W_{mn}\Delta D_N(m,n,-m-n),
$$
where $\Delta D_N$ is CUE-subtracted as in (4), and
$$
c_j=\sum_{n:(j,n)\in I^2}W_{jn}
   +\sum_{m:(m,j)\in I^2}W_{mj}
   +\sum_{(m,n)\in I^2:m+n=j}W_{mn}.                  \tag{7}
$$
Then $\mathbb E X_W=0$ and the exact complex variance is
$$
\mathbb E|X_W|^2=N^{-6}\left[
\sum_{m,n\in I}mn(m+n)
  \left(|W_{mn}|^2+W_{mn}\overline{W_{nm}}\right)
+\sum_j j^2|c_j|^2\right].                         \tag{8}
$$
The first sum is real and nonnegative after exchanging $(m,n)$.
It equals $\tfrac12\sum mn(m+n)|W_{mn}+W_{nm}|^2$.

**Proof.** Diaconis--Evans Theorem 2.1(a), checked at the exact
[source locator](../literature/signed_heisenberg_sources.md), gives
$$
\mathbb E\prod_jT_j^{u_j}\overline{T_j}^{v_j}
=1_{\{u=v\}}\prod_j j^{u_j}u_j!,\qquad
\max\left(\sum j u_j,\sum j v_j\right)\le N.       \tag{9}
$$
All moments below have weighted degree at most $4\max I\le N$.
For $B_{mn}=T_mT_n\overline{T_{m+n}}$, the positive and negative
multisets in $B_{mn}\overline{B_{rs}}$ are
$\{m,n,r+s\}$ and $\{m+n,r,s\}$. Their maxima force
$m+n=r+s$, and then $\{m,n\}=\{r,s\}$. Thus
$$
\mathbb E B_{mn}\overline{B_{rs}}
=mn(m+n)(1_{m=r,n=s}+1_{m=s,n=r}).                  \tag{10}
$$
This includes the extra factor two at $m=n$.
Also $\mathbb E\delta_j\delta_l=j^2 1_{j=l}$ and
$\mathbb E B_{mn}\delta_j=0$: the latter moment has unequal
positive and negative multiplicity lists. Substitute (7) into (4) to
obtain (8). $\square$

For bounded weights and $|I|=O(N)$, (8) is $O(N^{-1})$.
More precisely, if $I\subset[1,bN]$, $\ell=|I|/N$, then
$$
\mathbb E|X_W|^2\le
N^{-3}(4b^3+36b^2\ell)\sum_{m,n\in I}|W_{mn}|^2.   \tag{11}
$$
Each $c_j$ contains at most $3|I|$ summands, each weight occurs three
times, and $j\le2bN$; Cauchy--Schwarz proves this bound from (8).
If a bounded weight is restricted to at least one of $m,n,m+n$ being
a multiple of $d$, its support has $O(N^2/d+N)$ pairs. The CUE variance
is therefore $O(1/(Nd)+1/N^2)$. This calibrates a **joint resonant**
test; it is not a result about the actual resonant block.

## 5. Deterministic quadratic phase cancellation: algebra and failed realization

For an explicitly **formal trace table**, put
$$
t_0=N,\quad t_j=\sqrt j\,e^{2\pi i j^2/N},\quad
t_{-j}=\overline{t_j}\quad(1\le j\le N).
$$
Use the partition polynomial to define $D^{\rm tab}_N$, without claiming
that these are the traces of an $N$-point spectrum. Fix $k\ge3$, $q=k-1$,
$0<a<b$ with $qb<1$ and $2(q-1)b<1$. For
$W\in C_c^\infty((a,b)^q)$ and every fixed $H>0$,
$$
N^{-k}\sum_{m\in\mathbb Z^q}W(m/N)
\left[D^{\rm tab}_N(m,-S)-(-1)^q q!(N-S)\right]
=O_{W,k,H}(N^{-H}).                                \tag{12}
$$
This shows how signed cancellation can coexist algebraically with the
absolute divergence in (5). It does not construct a BGS example.

**Proof.** A partition with $\ell\ge3$ blocks has $\ell-1$ positive
block sums $s_1,\ldots,s_{\ell-1}$ and one negative block sum
$-\sum s_j$. Its phase, in scaled coordinates, is
$$
\Psi=\sum_j s_j^2-(\sum_j s_j)^2
      =-2\sum_{i<j}s_i s_j.
$$
For a variable in positive block $j$, its derivative is
$-2\sum_{i\ne j}s_i\in[-2(q-1)b,-2a]$, separated from every integer.
The amplitude is $N^{\ell/2}$ times a smooth function on the compact
support. Poisson summation expresses the lattice sum as
$N^q\sum_{h\in\mathbb Z^q}\int G(x)e^{2\pi iN(\Psi(x)-h\cdot x)}dx$.
The gradient never vanishes for any integer $h$; for large $|h|$ it grows
linearly. Repeated integration by parts gives, for every $M$, a bound
$C_M N^{-M}(1+|h|)^{-M}$ for the integrals. Take $M>q$ and arbitrarily
larger to absorb the prefactor. This proves rapid decay for every
partition with at least three blocks, including the singleton partition.

The two-block products are exactly $t_s t_{-s}=s$.
For a positive variable, the sum of its two-block coefficients, apart
from the common sign, is
$\sum_{h=1}^q\binom{q-1}{h-1}(h-1)!(q-h)!=q!$.
The two-block and one-block terms therefore sum exactly to
$(-1)^{q-1}q!S+(-1)^q q!N$, the CUE benchmark. $\square$

**Realization check.** For $N=3$, set $z=e^{2\pi i/3}$ and
$(t_0,t_1,t_2,t_3)=(3,z,\sqrt2 z,\sqrt3)$.
The Hermitian Toeplitz moment matrix $H_{jl}=t_{j-l}$, $0\le j,l\le3$,
has determinant
$$
\det H=-5-6\sqrt2-6\sqrt6<0.                       \tag{13}
$$
Every actual spectral moment matrix is positive semidefinite, since it
is a sum of outer products of eigenphase Vandermonde vectors, and this
$4\times4$ matrix would also have rank at most three. Thus this table
already fails at dimension three. No general or asymptotic unitary
realization is established. The table is a phase-cancellation control;
(12) cannot be transferred to the frozen map by declaration.

## 6. What the resonant pair result does and does not supply at order three

Let $I\subset[aN,bN]$, $J\subset[aN,2bN]$ contain every $m,n,m+n$ in
the test. Put $R=\{j\in J:d\mid j\}$,
$E_R=N^{-2}\sum_{j\in R}|T_j|^2$ and
$Q=N^{-2}\sum_{j\in J}|T_j|^2$. For bounded weights supported on
the union of the three resonant strips, Cauchy--Schwarz gives
$$
N^{-3}\sum_{m,n\in I:\{m,n,m+n\}\cap R\ne\varnothing}
|W_{mn}T_mT_n\overline{T_{m+n}}|
\le3\|W\|_\infty Q\sqrt{|R|E_R}.                  \tag{14}
$$
For a fixed resonant $m$, the inner sum of $|T_nT_{m+n}|$ is at most
$N^2Q$; then $\sum_{m\in R}|T_m|\le N\sqrt{|R|E_R}$.
The same argument fixes $n$ or $m+n$ and bounds the union.
Hence $E_R=o(1)$ alone, as required by the prime pair criterion,
does not make this particular absolute upper bound small when
$|R|\asymp N/d$ grows. It is not a counterexample to signed comparison.
The variance calibration (11) identifies the cancellation discarded
by this loss; it must be proved afresh for the actual ordered blocks.

## 7. Next model-specific proof obligation

The first direct target is (6) at $k=3$, with the exact factorial
counterterm, and with arbitrary compact weights rather than one mode.
In the low positive cone the raw term is $T_mT_n\overline{T_{m+n}}$;
in higher bands use the nonzero CUE cumulant. Separate all three
resonant strips using the correctly ordered TRACE-009 block, then
control their **signed** contribution and the nonresonant remainder.
Pair-sector mass, logarithmic-time traces, scalar finite type and
external-noise relaxation currently supply no such estimate.
The next success must be an actual-map bound for this sum or a proved
positive-time obstruction on an infinite dimension subsequence.

The [verifier](../computations/verification/signed_heisenberg_audit.py)
checks independent finite identities and adversarial controls. It does
not prove the asymptotics or this model-specific obligation.

## Subsequent density-controlled sector estimate

[TRACE-011](resonant_cubic_density_control.md) replaces the cardinality loss
under explicit local spectral density control and proves a realizable critical
cluster obstruction, including a CUE-pair-compatible background. It supplies
no actual-map mass/density estimate and leaves the signed BGS target open.
