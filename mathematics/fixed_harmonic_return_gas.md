# Fixed-harmonic returns from a convergent complex gas

**Status.** Project proof, checked by the author, with separately scoped exact finite
checks and floating matrix experiments. Independent review and priority
verification are outstanding. The starting repository revision is
9ed93cd1bc5e3362c1dbf520f0f391478dfb6969; this note also uses the uncommitted
32-class lattice proof in [the even-period note](resonance-cohomology/even_period_spin_resonance.md).
The target remains microscopic BGS for fixed smooth chaotic systems.
The results below concern arithmetic return times and do not achieve that target.

## 1. Statements and the physical regime

Let
$$
 A=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
 \lambda=3+2\sqrt2,\quad b_0=0,\ b_1=1,\ b_{j+1}=6b_j-b_{j-1}.
$$
For odd $m\ge3$ set $K=2m$, $N=b_m$, $D=(N-1)/2$.
Use centered Weyl operators with
$W(v)W(w)=e_N(\omega(v,w)/2)W(v+w)$ and
$U_0W(v)U_0^{-1}=W(Av)$, normalized so that $U_0^K=I$.
For a nonzero integer $a$ with $\gcd(a,N)=1$, define
$$
 U_{\epsilon,a}=e^{2i\epsilon\cos(2\pi ax/N)}U_0,\qquad
 C_a=1+\frac{4\pi a^2}{\lambda-1},\qquad
 s_a=\frac1{32\sqrt{C_a}}.                                  \tag{G1}
$$
Here $\operatorname{tr}_-$ denotes the normalized odd trace.
In particular $a=1$ is admissible for every $K$.

**Theorem 1 (uniform return bound).** For every positive integer $r$
and real $\epsilon$ with $s=r|\epsilon|\le s_a$,
$$
 |\operatorname{tr}_-U_{\epsilon,a}^{rK}|
 \le34e^{-Ks^2/2}+\frac{e^{2Ks}}{N-1}.                      \tag{G2}
$$
The number of replicas $r$ is not held fixed in this finite inequality.
Every central aggregate and every Bessel charge is included.

**Corollary 1 (all fixed returns and the global return law).**
Fix $a\ne0$, restricting to the indicated unit subsequence if necessary.
For every real sequence $\epsilon_K\to0$ and every fixed integer $r\ge1$,
$$
 \operatorname{tr}_-U_{\epsilon_K,a}^{rK}
                    -e^{-r^2K\epsilon_K^2}\longrightarrow0. \tag{G3}
$$
If $K\epsilon_K^2\to\infty$, the empirical eigenphase measure of
$U_{\epsilon_K,a}^K$ converges weakly to uniform measure on the circle.
If $K\epsilon_K^2\to t<\infty$, its Fourier moments are $e^{-r^2t}$,
the wrapped centered Gaussian with variance $2t$.
These are global laws for the return operator.

There is also a relative correction, not just decay to zero.
Put
$$
 S_{a,K}=\sum_{\ell=1}^{m-1}
       \left[1-\cos\left(4\pi a^2\frac{b_{m-\ell}}{b_m}\right)\right],
 \quad
 S_a=\sum_{\ell\ge1}[1-\cos(4\pi a^2\lambda^{-\ell})].        \tag{G4}
$$
For example $S_1=1.6221274986792295244903668068\ldots$.
Both series and their comparison will be bounded below.

**Theorem 2 (relative fourth-order transition).**
Fix $a\ne0$. Let $r_K\ge1$ be any sequence of positive integers,
let $\epsilon_K$ be real,
$x_K=r_K\epsilon_K$, and suppose $Kx_K^4\to u<\infty$.
Then, along admissible moduli,
$$
 \frac{\operatorname{tr}_-U_{\epsilon_K,a}^{r_KK}}
                   {J_0(2x_K)^K}
 -
 \exp\left[-\frac{1-r_K^{-2}}3 S_a Kx_K^4\right]
                         \longrightarrow0.                 \tag{G5}
$$
The denominator is positive eventually. Formula (G5) is uniform in the
replica count; it does not require $r_K$ to converge.
If $r$ is fixed and $K\epsilon_K^4\to v<\infty$, its correction is
$\exp[-r^2(r^2-1)S_av/3]$.

The symbol $2\cos(2\pi aq)$ is fixed and smooth when $a$ is fixed.
Nevertheless the associated classical kick strength is proportional to
$\epsilon/N$. These statements do not concern a fixed nonzero classical
perturbation, whose quantum exponent would be of order $N$.
The distinction remains essential even in (G5), where $r_KK$ may be large.

## 2. All ordered phases have a summable spatial kernel

Let $\boldsymbol n_j=(n_{1j},\ldots,n_{rj})\in\mathbb Z^r$ be the
indices at site $j$ in the $r$ consecutive periods, and let
$c_j=\sum_\nu n_{\nu j}$.
Define the replica matrix
$$
 H_{\nu\mu}=\begin{cases}1,&\nu\le\mu,\\-1,&\nu>\mu.\end{cases}
$$
Multiplying Weyl operators in their original period order gives the phase
$$
 e_N\left(a^2\sum_{i<j} b_{j-i}
                         \boldsymbol n_i^{\mathsf T}H\boldsymbol n_j\right).
                                                               \tag{G6}
$$
Indeed equal-period pairs give the diagonal of $H$; for different periods
the earlier occurrence of site $i$ gives a plus sign and the earlier
occurrence of site $j$ gives a minus sign. This derivation does not assume
that the aggregate is zero or central.

Since $b_{K-d}\equiv-b_d\pmod N$ and $b_m=N$, the phase in (G6)
has the exact real representative
$$
 \prod_{i<j}
 e^{i\theta_{j-i}\boldsymbol n_i^{\mathsf T}H\boldsymbol n_j},
 \qquad
 \theta_d=\begin{cases}
 2\pi a^2 b_d/N,&d<m,\\
 0,&d=m,\\
 -2\pi a^2 b_{K-d}/N,&d>m.
 \end{cases}                                                \tag{G7}
$$
At the antipodal separation the omitted angle is an integer multiple of
$2\pi$, including for all replica vectors. Because
$b_{m-\ell}/b_m\le\lambda^{-\ell}$,
$$
 \sup_i\sum_{j\ne i}|\theta_{|j-i|}|
          \le\frac{4\pi a^2}{\lambda-1}=C_a-1.              \tag{G8}
$$
For the norm $l(\boldsymbol n)=\sum_\nu|n_\nu|$,
$|\boldsymbol n^{\mathsf T}H\boldsymbol p|\le l(\boldsymbol n)l(\boldsymbol p)$.
Thus all these estimates are independent of $r$.

The normalized full trace selects precisely
$$
 \mathcal C=\{c:\sum_jc_jA^j(1,0)=0\bmod N\}.
$$
The unit assumption on $a$ is used here. The 32-class proof gives
$$
 \sum_{c\in\mathcal C\setminus\{0\}}z^{\|c\|_1}
 \le G_K(z):=e^{5Kz^8}-1+2(13/50)^K+31(3/5)^K
 \quad(0\le z\le3/10).                                    \tag{G9}
$$
Here is the 32-class argument.  On parity-constant vectors the
operator $L$ (symbol $z+z^{-1}-6$) is given by
$B=\bigl(\begin{smallmatrix}-6&2\\2&-6\end{smallmatrix}\bigr)$,
and $\mathbf Z^2/B\mathbf Z^2$ has order $\det B=32$ and maps
injectively to $\mathcal C/L\mathbf Z^K$.  A Hermite basis of
$B$ is $\bigl(\begin{smallmatrix}16&10\\0&2\end{smallmatrix}\bigr)$,
so the classes are represented by $(r,s)$, $0\le r<16$,
$0\le s<2$, with fractional preimages
$p_{\rm even}=-(3r+s)/16$, $p_{\rm odd}=-(r+3s)/16$.
The noninteger classes have numerator pairs among
$(0,8),(1,3),(1,5),(2,2),(2,6),(3,7),(4,4),(5,7),(6,6),(8,8)$.
With $x=z^{1/4}$ and $H_j(x)=(x^j+x^{16-j})/(1-x^{16})$, the
Green-kernel bound $\|Lp\|_1\ge4\|p\|_1$ (the inverse of $L$
has kernel $-\lambda^{-|n|}/(4\sqrt2)$, of $\ell^1$ norm
$1/4$) bounds the $(i,j)$ class by $[H_i(x)H_j(x)]^{K/2}$;
at $x=3/4$ the maximum is
$H_1H_3=\frac{10040323357589760}{28926125721773329}<\frac9{25}$,
so the 31 noninteger classes contribute at most $31(3/5)^K$.
For the integer class, intervals starting at a fixed site have
total activity, with $v=2z^4/(1-z^4)$,
$$
B(z)=z^4\,\frac{2v+4v^2}{1-4v}
    =\frac{4z^8(1+3z^4)}{(1-z^4)(1-9z^4)}\le5z^8
\qquad(z\le3/10);
$$
disjoint intervals therefore contribute at most $e^{KB(z)}$, and
configurations with no adjacent zeros at most
$2(2\sqrt v)^K\le2(13/50)^K$, since $2\sqrt v<13/50$.
Subtracting the zero configuration gives (G9).

The difference between the full and odd normalized traces is at most
$e^{2rK|\epsilon|}/(N-1)$. Individual Weyl words need not preserve parity;
the correction uses the linear trace with the odd projector.

## 3. A complex-gas lemma with a proof of convergence

At a site with aggregate zero, the vacuum weight is
$v=J_0(2\epsilon)^r$. Nonzero particles are vectors
$\boldsymbol n\ne0$ with $\sum_\nu n_\nu=0$, of activity
$$
 w_j(\boldsymbol n)
 =v^{-1}\prod_\nu J_{n_\nu}(2\epsilon)
                         e^{i\boldsymbol h_j\cdot\boldsymbol n},
                                                               \tag{G10}
$$
where $\boldsymbol h_j$ is any real external field.
The factors $i^{\sum n_\nu}$ are one. The activities may have either sign
and may be complex. Two particles at the same site have factor $1+f=0$;
at different sites $1+f$ is the phase in (G7), always evaluated in
increasing physical site order. Thus $f$ is symmetric as a function
of the two labeled particles.
In particular $|1+f|\le1$.

Here is the precise estimate that will be used. Suppose
$$
 |f((i,\boldsymbol n),(j,\boldsymbol p))|
       \le c_{ij}l(\boldsymbol n)l(\boldsymbol p),\quad
 \sup_i\sum_j c_{ij}\le C,
$$
and
$$
 M=\sup_j\sum_{\boldsymbol n\ne0}
              |w_j(\boldsymbol n)|\,l(\boldsymbol n)e^{l(\boldsymbol n)},
 \qquad CM<1.
$$
For $k$ allowed sites the gas partition function is nonzero, has the
logarithm continued from zero activities, and satisfies
$$
 \left|\log Z-\sum_{j,\boldsymbol n}w_j(\boldsymbol n)\right|
                              \le\frac12 kCM^2.             \tag{G11}
$$

For clarity, this is an application of the classical Penrose
tree-graph identity, not a newly claimed graph identity. Its complex
version appears as Proposition 1 of Procacci and Yuhjtman,
[arXiv:1508.07379v1](https://arxiv.org/pdf/1508.07379v1).
The needed specialization and convergence argument follow.

Root a connected labeled graph at its first vertex, assign distance levels,
and give each other vertex its smallest neighbor in the preceding level
as parent. The resulting tree $T$ determines an interval of graphs:
one may add all edges within a level, and all edges from a vertex to
preceding-level vertices with label no smaller than its parent.
Conversely exactly these additions preserve the levels and smallest parents.
These intervals partition the connected graphs. It follows algebraically
that their sum of products of $f$ is a sum over trees of
$$
 \prod_{e\in T}f_e\prod_{e\in R(T)\setminus T}(1+f_e).
$$
Taking absolute values bounds the connected sum by
$\sum_T\prod_{e\in T}|f_e|$.

The rooted positive tree series, with its root particle fixed and
its root activity omitted, obeys the iterative majorant
$$
 T_\gamma=\exp\left(\sum_{\gamma'}
                  |w_{\gamma'}|\,|f_{\gamma\gamma'}|T_{\gamma'}\right).
$$
Start the iteration at one. If $T_{\gamma'}\le e^{l(\gamma')}$,
the next iterate is at most $e^{CMl(\gamma)}\le e^{l(\gamma)}$.
Monotone convergence bounds the entire rooted series and gives
$$
 T_\gamma-1\le CMl(\gamma)e^{l(\gamma)}.
$$
In the connected logarithm, a graph with $n\ge2$ vertices has weight
$1/n!$, whereas the rooted series has $1/(n-1)!$. The ratio is
$1/n\le1/2$. Summing its root activity therefore proves (G11).

For a fully justified logarithm, first truncate the charge set and multiply
all activities by one complex parameter. The usual finite exponential
formula partitions graphs into connected components and identifies the
Taylor series of the partition function with the exponential of the
connected series near zero. The strict tree bound gives absolute convergence
on a disk containing the closed unit disk. Analytic continuation establishes
the identity and nonvanishing there. Finally pass to the countable charge
set by absolute convergence; the same bounds are uniform in the cutoff.
This also establishes the analytic version for complex $\epsilon$ used below.

In the present gas choose $c_{ii}=1$ and
$c_{ij}=|\theta_{|j-i|}|$ for different sites, so $C=C_a$.
Every nonzero zero-sum vector has norm at least two, which handles
the same-site hard core.

## 4. Uniform activity and one-site estimates

Write $\delta=|\epsilon|$, $s=r\delta\le s_a$.
The Bessel series and modified-Bessel convolution give
$$
 M\le
 \frac{2e^2s^2e^{e^2s^2}}
            {(1-\delta^2e^{\delta^2})^r}
 \le16s^2.                                                 \tag{G12}
$$
To obtain the numerator, multiply each charge by $e^{|n_\nu|}$,
majorize by $I_{|n_\nu|}(2e\delta)$, and differentiate their
zero-coefficient convolution $I_0(2re\delta)$.
Each series monomial has degree at least the sum of the absolute indices.
Use $I_1(2s e)\le se\,e^{s^2e^2}$ and
$|J_0(2\epsilon)|\ge1-\delta^2e^{\delta^2}$.
The last inequality follows for $s\le1/32$ by the positive exponential
series, using $r\delta^2\le s^2$.
In particular $C_aM\le16/1024<1$.

The exact one-site sum is
$$
 v\left(1+\sum_{\boldsymbol n\ne0}w_j(\boldsymbol n)\right)
 =B_j:=J_0\left(2\epsilon
                 \left|\sum_{\nu=1}^r e^{ih_{\nu j}}\right|\right).
                                                               \tag{G13}
$$
This follows by taking the zero Fourier coefficient of the product of
$r$ shifted factors $e^{2i\epsilon\cos\alpha}$.
For real fields $|\sum_\nu e^{ih_{\nu j}}|\le r$.
Taylor's formula, uniformly in these fields, gives
$$
 \left|r\log J_0(2\epsilon)
         +(B_j/v-1)
         +\epsilon^2\left|\sum_\nu e^{ih_{\nu j}}\right|^2
 \right|\le16s^4.                                         \tag{G14}
$$
One direct estimate is to put
$A=r\epsilon^2$ and $B=\epsilon^2|\sum e^{ih_\nu}|^2$.
The bounds $|A|,|B|\le s^2$,
$|r\log J_0(2\epsilon)+A|\le s^4$,
$|v^{-1}-1-A|\le4s^4$, and
$|B_j-1+B|\le s^4/3$ suffice.
They follow from the absolutely convergent Bessel and logarithm series
for $s\le1/32$. The same estimate holds for complex $\epsilon$,
with absolute values on the remainders.

Combining (G11)--(G14), for $k$ clean sites with specified fields,
the corresponding conditional partition sum $\mathcal Q$ satisfies
$$
 \log|\mathcal Q|
 \le-\delta^2\sum_{j\ {\rm clean}}
               \left|\sum_\nu e^{ih_{\nu j}}\right|^2
                              +160C_aKs^4.                 \tag{G15}
$$
The harmless replacement of $k$ by $K$ is convenient.
The constants account for $16ks^4$ and at most
$128C_aks^4$ of connected-graph remainder.

## 5. Nonzero aggregates do not destroy the cancellation

Fix $c\in\mathcal C$, and let $B=\{j:c_j\ne0\}$.
Condition on the complete replica vector at every site in $B$.
Write $S_B=\sum_{j\in B}l(\boldsymbol n_j)$.
All their interactions with clean sites are real external fields.
The entrywise bound $|H_{\nu\mu}|=1$ and (G8) give
$$
 \sum_{j\notin B}\sum_\nu|h_{\nu j}|
                           \le r(C_a-1)S_B.
$$
Also
$$
 \left|\sum_\nu e^{ih_\nu}\right|^2
                 \ge r^2-2r\sum_\nu|h_\nu|.
$$
Thus (G15) bounds the clean sum by
$$
 \exp\left[-Ks^2+160C_aKs^4+s^2|B|
                                  +2(C_a-1)s^2S_B\right]. \tag{G16}
$$
The phases internal to $B$, including $i^{\sum_jc_j}$, have unit modulus.

Let $\tau=2(C_a-1)s^2$. For a dirty site of aggregate $c_j$,
the weighted absolute mass is bounded by
$$
 \sum_{\sum n_\nu=c_j}\prod_\nu|J_{n_\nu}(2\epsilon)|
                                e^{\tau\sum|n_\nu|}
 \le I_{|c_j|}(2re^\tau\delta)
 \le e^{s^2e^{2\tau}}\frac{(se^\tau)^{|c_j|}}{|c_j|!}.
$$
The first inequality follows termwise from
$|J_n(2\epsilon)|e^{\tau|n|}\le I_{|n|}(2e^\tau\delta)$.
Since $|c_j|\ge1$, the factor $e^{s^2}$ in (G16) is absorbed by setting
$$
 z=s\exp\big[\tau+s^2(1+e^{2\tau})\big]\le2s.
$$
Therefore the contribution of each aggregate is at most
$$
 e^{-Ks^2+160C_aKs^4}z^{\|c\|_1}.                          \tag{G17}
$$
All charges at dirty sites were integrated, not truncated.
All Fourier series converge absolutely at finite $K$.

Sum (G17) using (G9). The entire normalized full trace is bounded by
$$
 e^{-Ks^2+160C_aKs^4}[1+G_K(z)]
 \le34\exp[-Ks^2+160C_aKs^4+1280Ks^8].
$$
For $s^2\le1/(1024C_a)$ the positive terms are less than $Ks^2/2$.
Adding the odd-projector error proves (G2).
The same argument, omitting $c=0$, gives the sharper comparison
$$
 |\operatorname{tr}_-U_{\epsilon,a}^{rK}-Q_{r,K}(\epsilon)|
 \le e^{-Ks^2+160C_aKs^4}G_K(2s)
                                  +\frac{e^{2Ks}}{N-1},    \tag{G18}
$$
where $Q_{r,K}$ denotes the exact zero-aggregate contribution.

## 6. Quartic pressure, including a growing number of replicas

At zero external field the gas argument also proves that $Q_{r,K}$
is nonzero on $|r\epsilon|\le s_a$. Its analytic logarithm, normalized
to zero at $\epsilon=0$, obeys
$$
 \left|K^{-1}\log Q_{r,K}(\epsilon)+(r\epsilon)^2\right|
                           \le160C_a|r\epsilon|^4.          \tag{G19}
$$
It is an even function: every zero-aggregate configuration has total
charge zero, so changing $\epsilon$ to $-\epsilon$ leaves its weight invariant.

The order-four coefficient has a finite description.
An order-two particle is $e_\nu-e_\mu$, $\nu\ne\mu$, with leading
activity $-\epsilon^2$. For $r$ replicas let
$$
 q_r=\#\{(\alpha,\beta):\alpha,\beta=e_\nu-e_\mu,\
                                  \alpha^{\mathsf T}H\beta\ne0\}
                         =\frac{r^2(r^2-1)}3.              \tag{G20}
$$
To verify the count, for $\nu<\mu$ the row
$(e_\nu-e_\mu)^{\mathsf T}H$ equals two on the interval
$[\nu,\mu)$ and zero elsewhere.
If that interval has length $d$, precisely $2d(r-d)$ oriented
charges cross its boundary. Summing both orientations of its
$r-d$ placements gives
$4\sum_{d=1}^{r-1}d(r-d)^2=r^2(r^2-1)/3$.
All nonzero pairings equal $2$ or $-2$, in equal numbers.

The one-site part of the logarithm, with all charges at that site resummed,
is $\log J_0(2r\epsilon)$.
At order four, a connected contribution involving different sites has
exactly two order-two particles. Their sum is
$q_r[\cos(2\theta_{j-i})-1]\epsilon^4$.
Graphs on three occupied sites start at order six.
The two complementary separations $m-\ell,m+\ell$ have total
multiplicity $K$; the antipodal phase is zero.
Consequently
$$
 K^{-1}\log Q_{r,K}(\epsilon)
 =-(r\epsilon)^2
   -\left[\frac14+\frac{1-r^{-2}}3 S_{a,K}\right](r\epsilon)^4
                              +O_a(|r\epsilon|^6).         \tag{G21}
$$
The remainder is uniform in both $r$ and $K$.
Indeed apply Cauchy's coefficient bound to the even analytic function
in (G19), in the variable $x=r\epsilon$, on the circle $|x|=s_a$.
For $|x|\le s_a/2$, the tail from degree six is bounded by
$220000C_a^2|x|^6$. The strict activity criterion supplies analyticity
on a neighborhood of that circle.

For the series in (G4),
$$
 \sum_{\ell>M}[1-\cos(4\pi a^2\lambda^{-\ell})]
 \le\frac{8\pi^2a^4\lambda^{-2(M+1)}}{1-\lambda^{-2}}.
$$
The Binet formula and $|\cos x-\cos y|\le|x^2-y^2|/2$ for $x,y\ge0$
also give
$$
 |S_{a,K}-S_a|
 \le\frac{16\pi^2a^4(m-1)\lambda^{-K}}{1-\lambda^{-K}}
             +\frac{8\pi^2a^4\lambda^{-K}}{1-\lambda^{-2}}. \tag{G22}
$$
For $a\ne0$, $S_a>0$, since already the first angle is not an integer
multiple of $2\pi$.

If $Kx_K^4$ is bounded, then $K|x_K|^6\to0$.
Subtract $\log J_0(2x_K)$ in (G21), use (G22), and exponentiate.
This proves (G5) first for $Q_{r,K}$.
To replace it by the physical odd trace, divide (G18) by
$J_0(2x_K)^K$.
The first error is bounded by a constant times $G_K(2|x_K|)$,
which tends to zero since $K|x_K|^8\to0$.
The odd error tends to zero because its logarithm is
$-\tfrac12K\log\lambda+2K|x_K|+O(Kx_K^2)+O(1)$.
This completes Theorem 2 without a fixed-$r$ assumption.

For bounded $K\epsilon_K^2$ and fixed $r$, (G18)--(G19) give (G3).
For $K\epsilon_K^2\to\infty$, use (G2).
A subsequence argument covers arbitrary sequences.
Fourier approximation by trigonometric polynomials then proves
Corollary 1, including the uniform circle limit.

## 7. Independent checks and a failed test that was corrected

The companion
[fixed_harmonic_return_gas.py](../computations/verification/fixed_harmonic_return_gas.py)
performs the following finite checks:

- all 33,866 labeled simple graphs with two through six vertices,
  including exact interval cardinalities for every connected graph;
- 4,320 seeded ordered Weyl words, with one through six replicas,
  four moduli, and three harmonics, including constructed nonzero central
  aggregates and completely unrestricted words;
- all 49,192 oriented charge-species pairings through twelve replicas;
- eighteen high-precision checks of the conservative Bessel constants;
- physical matrices at $N=1189$ in both parity sectors, two harmonics,
  and the first five return traces at three kick strengths.

The first attempt to extract the quartic coefficient from the odd trace
alone failed. The reason was substantive: its finite-$N$ noncentral
projection correction has lower-order Taylor terms. Dividing it by
$\epsilon^4$ makes it grow as $\epsilon$ decreases.
The corrected experiment combines the two physical parity blocks to obtain
the exact normalized full trace and reports the odd trace separately.
At $K=10$, (G9) excludes all nonzero aggregate terms through order four.
Thus the full trace genuinely tests (G21) at that order.

All ten matrix cases show fourth-coefficient error decreasing by roughly
a factor four when the kick is halved at the smaller strengths.
This supports the derived coefficient; it is not an interval certificate
or an independent proof of the uniform remainder.
The test of the full-space coefficient does not erase the odd-projection
term from (G2), (G5), or (G18).

    OPENBLAS_NUM_THREADS=1 python computations/verification/fixed_harmonic_return_gas.py \
      --output build/fixed-harmonic-return-gas-precheck.json

## 8. Why this still does not reach microscopic BGS

The estimate covers $r\le s_a/|\epsilon|$.
At the same time, removal of the first return requires
$K\epsilon^2\to\infty$.
Therefore its largest directly controlled time obeys
$$
 rK\le s_a K/|\epsilon|=o_a(K^{3/2})
                                  =o_a((\log N)^{3/2}).    \tag{G23}
$$
Here $K\asymp\log N$. The exact microscopic Fourier bridge requires
joint trace information at times comparable to $D\asymp N$.
To put $rK\asymp N$ inside the present radius would instead require
$|\epsilon|=O_a(K/N)$, which forces $K\epsilon^2\to0$ and leaves
the first arithmetic return intact. This is an incompatibility of the
proved ranges, not a counterexample to BGS.

The fixed-classical-strength route is outside a different hypothesis:
it requires $\epsilon$ of order $N$, rather than a small quantum kick.
The gas expansion cannot be continued there by the bounds above.
The local coefficient $J_0(2r\epsilon)$ itself acquires zeros when
$r|\epsilon|$ is of order one, so zero-free pressure continuation across
that range also needs a new argument.

The next missing input is a nonperturbative comparison of the required
joint traces, including symmetry sectors, at Heisenberg times.
Neither global equidistribution of $U^K$ nor the relative law (G5)
supplies that comparison. These implications remain open; the user's
original target has not been relabeled as the results of this note.
