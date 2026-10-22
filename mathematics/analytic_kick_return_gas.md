# Analytic and smooth position kicks: resonances and return asymptotics

**Status.** Project proof, checked by the author, with finite exact controls;
independent review and priority verification remain open.
Base revision: 9ed93cd1bc5e3362c1dbf520f0f391478dfb6969.
The arithmetic setup and complex-gas lemma are those of
[the fixed-harmonic note](fixed_harmonic_return_gas.md).
This is a further result about arithmetic returns, not microscopic BGS
or a fixed nonzero classical perturbation.

## 1. Statement for a class of fixed smooth symbols

Let $K=2m$, $m\ge3$ odd, $N=b_m$, and $A,U_0,D$ be as in (G1)
of the preceding note. Fix $a\ne0$, with $\gcd(a,N)=1$ along the
sequence being considered. In particular $a=1$ needs no restriction.

Let $f$ be a nonzero real even $2\pi$-periodic function with
$$
 \widehat f_0=0,\qquad
 F_\rho:=\sum_{n\in\mathbb Z}|\widehat f_n|e^{\rho|n|}<\infty
                  \quad\hbox{for some }\rho>0.
$$
Every real analytic periodic function has this property after reducing
the strip width if necessary. Define
$$
 U_{\epsilon,f,a}
   =e^{i\epsilon f(2\pi ax/N)}U_0,\qquad
 \sigma_f^2=\frac1{2\pi}\int_0^{2\pi}f(\theta)^2\,d\theta>0,
 \quad F_0=\sum_n|\widehat f_n|.
$$
The kick is a fixed smooth position symbol and preserves parity.
Its classical strength is nevertheless proportional to $\epsilon/N$.

**Theorem 1.** There are constants $s_0>0$ and $C<\infty$, depending
only on $f,a$, such that for every admissible $K$, every integer $r\ge1$,
and every real $\epsilon$ with $s=r|\epsilon|\le s_0$,
$$
 |\operatorname{tr}_-U_{\epsilon,f,a}^{rK}|
 \le e^{-\sigma_f^2Ks^2/4}+(3/4)^K
                                   +\frac{e^{KsF_0}}{N-1}, \tag{A1}
$$
and
$$
 \left|\operatorname{tr}_-U_{\epsilon,f,a}^{rK}
                     -e^{-\sigma_f^2Ks^2/2}\right|
 \le \frac{C}{\sqrt K}+(3/4)^K
                                   +\frac{e^{KsF_0}}{N-1}. \tag{A2}
$$
We may, and do, choose $s_0F_0<\log\lambda/4$, so the last error
decays exponentially in $K$ uniformly in the stated range.
These are uniform estimates over the replica count, not estimates with
an unspecified constant depending on $r$.

For every $\epsilon_K\to0$ and each fixed $r$,
$$
 \operatorname{tr}_-U_{\epsilon_K,f,a}^{rK}
            -e^{-\sigma_f^2r^2K\epsilon_K^2/2}\to0.          \tag{A3}
$$
In particular $K\epsilon_K^2\to\infty$ gives uniform circle measure
as the global eigenphase law of $U_{\epsilon_K,f,a}^K$.
For $K\epsilon_K^2\to t<\infty$ the law is the wrapped Gaussian
of variance $\sigma_f^2t$.

For this class, $\sigma_f^2$ is also the classical Green--Kubo variance:
all nonzero-time autocorrelations vanish by Fourier orthogonality.
Indeed $A^j(1,0)$ is not parallel to $(1,0)$ for $j\ne0$.
No assertion of this simpler variance formula is made for arbitrary
two-dimensional symbols or for coboundaries.

## 2. A weighted bound for the entire resonance lattice

Let $L=S+S^{-1}-6I$ on the cyclic index set and
$$
 \mathcal C=\{c\in\mathbb Z^K:\sum_jc_jA^j(1,0)=0\bmod N\},
 \qquad q(c)=|\{j:c_j\ne0\}|.
$$
The 32-class calculation gives $p=L^{-1}c\in(1/16)\mathbb Z^K$.
Its fractional parts are constant on each parity.
A noninteger class therefore has no two consecutive zero coordinates.

**Weighted lattice lemma.** For every $\alpha>0$ there are finite
$B_\alpha>0$ and $\eta_\alpha>0$, independent of $K$, such that
$$
 \sum_{c\in\mathcal C}\eta^{q(c)}e^{-\alpha\|c\|_1}
 \le e^{B_\alpha K\eta^3}+(3/4)^K
                       \quad(0\le\eta\le\eta_\alpha).       \tag{A4}
$$
The third power counts occupied Fourier sites. It replaces a bound in
which a mode of index six would incorrectly cost six powers of the kick.

Here are explicit admissible constants. Put
$$
 b_\alpha=\frac{2}{e^{\alpha/2}-1},\qquad
 h_\alpha(g)=\exp\left[-\frac{\alpha}{200}
                              \lambda^{(g-1)/2}\right],
 \quad H_\alpha(R)=\sum_{g\ge1}h_\alpha(g)R^g.
$$
The last series converges for every finite $R$. One can take
$$
 \eta_\alpha=\frac1{2b_\alpha H_\alpha(2)},\qquad
 B_\alpha=2b_\alpha^3H_\alpha(1)^2.                         \tag{A5}
$$

### 2.1 Long homogeneous gaps require large rational amplitudes

Suppose the forcing $c=Lp$ vanishes strictly between two successive
nonzero forcing sites $i<j$, with gap $g=j-i$.
If the preimage has no consecutive zeros in this interval,
the homogeneous state $(p_i,p_{i+1})$ is nonzero.
Along the interval
$$
 p_{n+1}=6p_n-p_{n-1},\qquad
 p_{n+1}^2-6p_np_{n+1}+p_n^2=Q\ne0.
$$
Since the entries have denominator dividing 16, $|Q|\ge1/256$.
The invariant cannot vanish on a nonzero rational state because its
two real slopes $\lambda,\lambda^{-1}$ are irrational.
Writing $p_n=u\lambda^n+v\lambda^{-n}$ gives $Q=-32uv$.
Both coefficients at a specified state are bounded by twice the
$\ell^1$ norm of that state. The two endpoint states, separated by
$g-1$ iterations, consequently satisfy
$$
 |p_i|+|p_{i+1}|+|p_{j-1}|+|p_j|
                   \ge\frac1{100}\lambda^{(g-1)/2}.        \tag{A6}
$$
For example their norm product is at least
$\lambda^{g-1}/32768$, and the arithmetic-geometric mean inequality
gives (A6).

The endpoint norms summed over disjoint forcing gaps count each
coordinate of $p$ at most four times.
Also $\|Lp\|_1\ge4\|p\|_1$: on the cycle, $L^{-1}$ is
convolution with the periodization of the Green kernel
$g_n=-\lambda^{-|n|}/(4\sqrt2)$ of $z+z^{-1}-6$, all of whose
terms have one sign, and
$\sum_{n\in\mathbf Z}|g_n|
 =\frac1{4\sqrt2}\bigl(1+\frac{2}{\lambda-1}\bigr)=\frac14$,
so $\|p\|_1\le\frac14\|Lp\|_1$.
For a nonwinding component, or for all cyclic gaps in a winding
configuration, this proves
$$
 \|c\|_1\ge\frac1{100}
                  \sum_{\text{forcing gaps }g}\lambda^{(g-1)/2}. \tag{A7}
$$

### 2.2 Nonwinding components start at three occupied forcing sites

If an integer preimage has consecutive zeros, divide it into its unique
components, joining nonzero coordinates whose gap is at most two.
Add one exterior zero at either end of each component.
The forcing supports of different components are disjoint.

A finite nonzero component has at least three nonzero forcing entries.
Indeed its forcing Laurent polynomial is divisible by $z+z^{-1}-6$.
One nonzero monomial cannot vanish at $\lambda$; two would require
$\lambda^d$ to be rational for some $d\ge1$, which is impossible.

For a component with $q\ge3$ forcing sites and successive gaps
$g_1,\ldots,g_{q-1}$, split the exponential weight in (A4) into two
equal parts. Sum the first part over all nonzero integer forcing
values, and apply (A7) to the second part. Its total weight is bounded by
$$
 (\eta b_\alpha)^q\prod_{\nu=1}^{q-1}h_\alpha(g_\nu).
$$
This remains an upper bound after dropping the integrality and component
constraints on the candidate forcing values.
For a fixed starting site, the sum over every component is at most
$$
 \sum_{q\ge3}(\eta b_\alpha)^qH_\alpha(1)^{q-1}
 \le B_\alpha\eta^3.
$$
Allowing arbitrary subsets of components, rather than only disjoint
influence intervals, bounds the nonwinding partition by
$e^{B_\alpha K\eta^3}$.

### 2.3 Winding configurations include all noninteger classes

For a cyclic preimage with no consecutive zeros, let $q\ge1$
be the number of nonzero forcing sites.
Its cyclic gaps sum to $K$ and obey (A7).
Mark a forcing site as origin. There are $K$ choices for its position
and each unmarked configuration is counted $q$ times. Thus the
winding contribution is at most
$$
 \sum_{q=1}^K\frac Kq(\eta b_\alpha)^q
                   [z^K]H_\alpha(z)^q
 \le K2^{-K}\sum_{q\ge1}\frac{(\eta b_\alpha H_\alpha(2))^q}{q}
 \le K2^{-K}\log2\le(3/4)^K.
$$
The counting is over forcing vectors, whose real preimage is unique;
no additional multiplicity of 32 is introduced.
Together with the preceding part this proves (A4), including every
noninteger class and arbitrary Fourier indices.

## 3. Analytic Fourier coefficients and the zero-aggregate gas

Let
$$
 e^{i\epsilon f(\theta)}=\sum_{n\in\mathbb Z}k_n(\epsilon)e^{in\theta}.
$$
These are the exact coefficients of the physical diagonal kick,
including all lattice aliases. For complex $\epsilon$,
$$
 \sum_n|k_n(\epsilon)|e^{\rho|n|}
            \le e^{|\epsilon|F_\rho},\qquad
 k_0(\epsilon)=1-\tfrac12\sigma_f^2\epsilon^2+O_f(|\epsilon|^3).
                                                               \tag{A8}
$$
The vacuum is nonzero in a fixed disk.
For any $0<\beta<\rho$, both
$$
 \sum_{n\ne0}|k_n(\epsilon)|e^{\beta|n|},
 \qquad
 \sum_{n\ne0}|n|\,|k_n(\epsilon)|e^{\beta|n|}
$$
are $O_{f,\beta}(|\epsilon|)$.
The second estimate follows by leaving a positive gap between
$\beta$ and $\rho$.

At a clean site take vectors $\boldsymbol n\ne0$ with
$\sum_\nu n_\nu=0$, vacuum $v=k_0(\epsilon)^r$, and activities
$$
 w_j(\boldsymbol n)=v^{-1}\prod_\nu k_{n_\nu}(\epsilon)
                                    e^{i\boldsymbol h_j\cdot\boldsymbol n}.
$$
At least two coordinates must be nonzero.
For $s=r|\epsilon|$ sufficiently small, (A8) therefore yields
$$
 M_\beta:=\sup_j\sum_{\boldsymbol n\ne0}
        |w_j(\boldsymbol n)|\,l(\boldsymbol n)e^{\beta l(\boldsymbol n)}
                                        \le C_f s^2.       \tag{A9}
$$
For an explicit intermediate bound, if $A_\beta$ and $B_\beta$
denote the two nonzero-mode sums above, the left side is at most
$$
 \frac{rB_\beta}{|k_0|}
       \left[\left(1+\frac{A_\beta}{|k_0|}\right)^{r-1}-1\right].
$$
This proves the uniformity in $r$.

The ordered phase kernel is exactly (G6)--(G8), with the same
matrix $H$ and the same summable row bound.
Apply the tree argument of Section 3 of the preceding note with
root majorant $e^{\beta l}$.
Its criterion is $C_aM_\beta<\beta$, and its connected remainder
is still bounded by $\tfrac12 KC_aM_\beta^2=O_{f,a}(Ks^4)$.
All charges and repeated-particle hard-core terms are included.

The full one-site sum at external fields is
$$
 B_j=\frac1{2\pi}\int_0^{2\pi}
       \exp\left(i\epsilon\sum_{\nu=1}^r f(\theta+h_{\nu j})\right)d\theta.
$$
Its first moment vanishes. Taylor's formula and the gas estimate give
for the partition sum on any specified clean sites
$$
 \log|\mathcal Q|
 \le-\frac{\epsilon^2}{2}\sum_{j\ {\rm clean}}
       \left\|\sum_\nu f(\,\cdot+h_{\nu j})\right\|_2^2
                                            +C_{f,a}Ks^3. \tag{A10}
$$
The circle $L^2$ norm is normalized by $1/(2\pi)$.
The cubic remainder is uniform because the summed function has
supremum norm at most $r\|f\|_\infty$.
The corresponding complex estimate at zero external field is
$$
 \left|\log Q_{r,K}(\epsilon)
                   +\tfrac12\sigma_f^2K(r\epsilon)^2\right|
                                   \le C_{f,a}K|r\epsilon|^3. \tag{A11}
$$

## 4. Conditioning on all nonzero aggregates

For a fixed $c\in\mathcal C$, condition on every replica vector
at the dirty sites $B=\{j:c_j\ne0\}$.
As before $S_B=\sum_{j\in B}l(\boldsymbol n_j)$ and
$\sum_{j\notin B,\nu}|h_{\nu j}|\le r(C_a-1)S_B$.
Translation in $L^2$ gives
$$
 \left\|\sum_\nu f(\,\cdot+h_\nu)\right\|_2^2
 \ge r^2\sigma_f^2
            -2r\|f\|_2\|f'\|_2\sum_\nu|h_\nu|.
$$
Therefore the conditional clean sum is at most
$$
 \exp\left[-\tfrac12\sigma_f^2Ks^2
                    +C_{f,a}Ks^3+C_{f,a}s^2(|B|+S_B)\right]. \tag{A12}
$$

Choose $\alpha=\rho/4$ and make $s_0$ small enough that the weight
$e^{C_{f,a}s^2l}$ leaves at least this analytic strip width.
The convolution at a dirty site of aggregate $c_j\ne0$, including
its factor $e^{C_{f,a}s^2}$, is bounded by
$$
                         C'_{f,a}s\,e^{-\alpha|c_j|}.       \tag{A13}
$$
Indeed the total weighted mass of all nonzero aggregate coefficients
is bounded by
$(|k_0|+A_{\alpha+C_{f,a}s^2})^r-|k_0|^r=O_{f,a}(s)$.
The absence of a nonzero aggregate in the all-vacuum term is essential.

Put $\eta=C'_{f,a}s$ and use (A4).
The normalized full trace is at most
$$
 e^{-\sigma_f^2Ks^2/2+C_{f,a}Ks^3}
          \left[e^{B_\alpha K\eta^3}+(3/4)^K\right].
$$
Shrinking $s_0$ makes both cubic exponents smaller than
$\sigma_f^2Ks^2/4$ and ensures $\eta\le\eta_\alpha$.
This proves (A1) after the odd-projector correction is added.

For completeness the rate in (A2) follows without an uncontrolled
change of limits. Equations (A11)--(A13) and (A4) imply, after
possibly decreasing $s_0$ again,
$$
 |Q_{r,K}-e^{-\sigma_f^2Ks^2/2}|
       \le C_{f,a}Ks^3e^{-c_fKs^2},
$$
and the entire nonzero-aggregate contribution is at most
$$
 C_{f,a}Ks^3e^{-c_fKs^2}+(3/4)^K
$$
for a fixed $c_f>0$.
Use $|e^z-1|\le|z|e^{|z|}$, with the cubic exponent absorbed
by the negative quadratic exponent.
Finally
$$
 \sup_{s\ge0}Ks^3e^{-c_fKs^2}
    =K^{-1/2}\sup_{y\ge0}y^3e^{-c_fy^2}<\infty\cdot K^{-1/2}.
$$
This proves (A2).

## 5. A cubic term and a finite alias that the first prediction missed

Take
$$
 f(\theta)=2\cos\theta+2b\cos(6\theta),\qquad b\ne0.
$$
Its one-site third moment vanishes and $\sigma_f^2=2(1+b^2)$.
The ordinary finite-component resonance $(1,-6,1)=Le_j$
has ordered Weyl phase $e_N(-6a^2)$.
Its two signs contribute the cubic activity
$-2ib\,e_N(-6a^2)\epsilon^3$ per site.

At $K=10$, however, this is not the whole finite cubic coefficient.
The exact additional relation
$$
 6v_0+6v_4+v_7
       =v_9+v_1+v_3+v_5+v_7=0\bmod N,\qquad v_j=A^j(1,0),
$$
comes from the parity-orbit sum.
Its aggregate has fractional preimage $15/16$ on even sites and
$13/16$ on odd sites, modulo integers; it is a winding class.
Its phase at $a=1,N=1189$ is $e_N(210)$.
For $b=1/5$, exact enumeration gives the cubic coefficient of
$K^{-1}\log(\operatorname{Tr}U_{\epsilon,f,a}^{K}/N)$
$$
             -\frac{2i}{5}e_N(-6)-\frac{2i}{25}e_N(210)
                        \quad(K=10).                      \tag{A14}
$$
The second term was absent from the preliminary prediction.
It was found by the independent atom-word enumeration, and is explicitly
retained here. At $K=14,18$ the same complete cubic enumeration has only
the ordinary term.

More generally, grouping adjacent terms of the length-$m$ parity sum
using $v_{j-1}+v_{j+1}=6v_j$ produces a winding relation with
$(m+1)/2=(K+2)/4$ occupied Fourier sites using only modes 1 and 6.
Thus these finite aliases cannot simply be declared absent.
They are covered collectively by the winding part of (A4).

The rate $K^{-1/2}$ in (A2) is in fact attained by this example.
For each fixed real $t$ and fixed admissible $a$,
$$
 \sqrt K\left[
 \operatorname{tr}_-U_{t/\sqrt K,f,a}^{K}
                         -e^{-(1+b^2)t^2}\right]
          \longrightarrow-2ib\,t^3e^{-(1+b^2)t^2}.          \tag{A15}
$$
Here is a remainder argument for this last assertion.
For one period and an integer preimage, the ordered action is
$a^2\sum_jp_j(Lp)_j$ modulo $N$.
Separated nonwinding components therefore multiply exactly, including
their phases. Normalize each local Fourier coefficient by $k_0$.
The component sum is analytic, uniformly bounded by $C|\epsilon|^3$
on a fixed complex disk by the proof of (A4).
Cauchy's estimate leaves $O(|\epsilon|^4)$ after its cubic coefficient.

The only finite three-monomial relations with coefficients in
$\{\pm1,\pm6\}$ are translates of $\pm(1,-6,1)$.
To see this, evaluate $a_0+a_1z^d+a_2z^e$ at $\lambda$, $0<d<e$.
The largest term forces $e=d+1$; the coefficient bounds then force
$a_2=\pm1$, $a_1=\mp6$, and
$a_0=\pm\lambda^{d-1}$. Rationality gives $d=1$ and $a_0=\pm1$.
Thus the cubic component coefficient is the one stated above.
Terms with two or more components have absolute mass
$O(K^2|\epsilon|^6e^{CK|\epsilon|^3})$.
Truncating component lengths to the circle changes the estimates only
exponentially in $K$, by $H_\alpha(2)<\infty$.
Consequently the full central trace is
$$
 k_0(\epsilon)^K
 \left[1-2ib\,e_N(-6a^2)K\epsilon^3
          +O(K|\epsilon|^4+K^2|\epsilon|^6e^{CK|\epsilon|^3})\right]
                                      +O(e^{-cK}).
$$
At $\epsilon=t/\sqrt K$, $k_0(\epsilon)^K
=e^{-(1+b^2)t^2}(1+O(K^{-1}))$.
The odd correction and $e_N(-6a^2)-1$ are exponentially small.
This proves (A15), which is nonzero for $bt\ne0$.

## 6. The first Edgeworth correction for every analytic position symbol

The cubic mechanism above is not restricted to two Fourier modes.
Write $f_j(z)=f(2\pi\langle A^j(1,0),z\rangle)$ on the classical
two-torus, with normalized area, and put
$$
 \mu_3=\int f_0^3,\qquad
 C_{d,e}=\int f_0 f_d f_e,\qquad
 \kappa_3(f)=\mu_3+6\sum_{1\le d<e}C_{d,e}.                 \tag{A16}
$$
The series is absolutely convergent, as proved below.

**Theorem 2.** For every fixed $T<\infty$, uniformly over all integers
$r\ge1$ and all real $|t|\le T$,
$$
 \operatorname{tr}_-
 U_{t/(r\sqrt K),f,a}^{\,rK}
 =e^{-\sigma_f^2t^2/2}
       \left[1-\frac{i\kappa_3(f)t^3}{6\sqrt K}\right]
       +O_{f,a,T}(K^{-1}).                                 \tag{A17}
$$
This is an expansion of the normalized trace, not a local spectral
correlation theorem. When $r$ grows, the kick in (A17) decreases with $r$.
It does not provide control of the same kick at all times.

### 6.1 A relative estimate for the conditioned background

Set $x=r\epsilon$ and let $Q_{r,K}$ be the zero-aggregate partition
from (A11). The gas proof gives a nonvanishing analytic $Q_{r,K}$
on a fixed disk $|x|<s_*$, uniformly in $r,K$.
Remove a set $B$ of sites and impose the real fields generated by
specified dirty replica charges of total absolute mass $S_B$.
Let $Q_{B,\boldsymbol h}$ include the vacuum factors at the remaining
sites. Then, after reducing $s_*$,
$$
 \left|\log\frac{Q_{B,\boldsymbol h}}{Q_{r,K}}\right|
          \le C_{f,a}|x|^2(|B|+S_B).                       \tag{A18}
$$
The logarithm is continued from $x=0$.
This is a local perturbation estimate; there is no factor $K$ on
the right.

Here are details needed for this strengthening of (A12).
Differentiate the absolutely convergent connected series with respect
to an activity. The derivative is a rooted connected series, bounded
by $e^{\beta l}$ by the same tree majorant as in Section 3.
Removing a site by varying its fugacity from one to zero therefore
changes the logarithm by at most $C|x|^2$.
For fields use the interpolation
$w_j(\boldsymbol n;u)=w_j(\boldsymbol n;0)
 e^{iu\boldsymbol h_j\cdot\boldsymbol n}$, $0\le u\le1$.
Its logarithmic derivative has absolute sum bounded by
$$
 M_\beta\sum_j\max_\nu|h_{\nu j}|
       \le C|x|^2(C_a-1)S_B.
$$
The last inequality follows entry by entry from $|H_{\nu\mu}|=1$
and the row bound (G8). Finally the missing vacua contribute
$|B|\,|r\log k_0(x/r)|\le C|B||x|^2$.
All interpolations obey the same strict tree criterion.
This proves (A18) also for complex $x$; the imposed fields remain real.

At zero external field the exact one-site resummation is $k_0(x)$.
Since the nonvacuum site activity is $O(|x|^2)$, (G11) also gives
$$
 \log Q_{r,K}
   =K\log k_0(x)+O_{f,a}(K|x|^4)
   =-\tfrac12\sigma_f^2Kx^2
       -\tfrac{i}{6}\mu_3Kx^3+O_{f,a}(K|x|^4).             \tag{A19}
$$
This estimate is uniform on a fixed complex disk.

### 6.2 Isolating one finite component with a uniform remainder

Divide the full central trace by $Q_{r,K}$, and use its unique
preimage decomposition. For each prescribed dirty vector, (A18)
absorbs the background ratio into the Fourier weight
$\exp(C|x|^2(|B|+S_B))$.
Leaving analytic strip width as in (A13) gives the majorant
$$
                 (C|x|)^{q(c)}e^{-\alpha\|c\|_1}.          \tag{A20}
$$
In particular the entire winding contribution to this relative trace
is $O((3/4)^K)$ by Section 2.3.

For each possible start, sum the exact contributions of configurations
with exactly one nonwinding component, including their conditional
background ratios. This is an analytic function of $x$, uniformly
$O(|x|^3)$ on a fixed disk by (A20) and Section 2.2.
The connected-background ratio equals one at $x=0$.
Cauchy's estimate therefore leaves $O(|x|^4)$ after the cubic term,
uniformly in $r,K$ and in the start. More explicitly, divide this
analytic function by $x^3$, use its uniform bound on $|x|=s_*$,
and apply the geometric-series estimate on $|x|\le s_*/2$.

For configurations with two or more components, the phases need
not factor when $r>1$. Their absolute values are one, and (A20)
does factor over the disjoint forcing supports. Their total mass
is at most
$$
       C K^2|x|^6 e^{CK|x|^3}.
$$
No factorization of replica phases is being assumed here.
We have proved
$$
 \frac{\operatorname{Tr}U_{\epsilon,f,a}^{rK}}{NQ_{r,K}}
 =1+Kx^3d_{r,K}
    +O_{f,a}\!\left(K|x|^4+
                K^2|x|^6e^{CK|x|^3}+(3/4)^K\right).        \tag{A21}
$$

### 6.3 Exact cubic orientation count

A finite three-site forcing is a triple of nonzero integers satisfying
$$
 n_0v_0+n_dv_d+n_ev_e=0 \quad\hbox{over }\mathbb Z^2,
                      \qquad 0<d<e.                       \tag{A22}
$$
It is a single finite component: every component needs at least three
forcing sites. Its one-period phase is $e^{i\vartheta}$, where
$$
       \vartheta=\frac{2\pi a^2 n_0n_d b_d}{N}.
$$
For a central triple, an even permutation of its three Weyl factors
has this phase and an odd permutation has its inverse.
Assign its three distinct physical sites independently to $r$ replicas,
then order by replica first and physical site second.
The two orientation counts are exactly
$$
             \frac{r^3+r^2}{2},\qquad\frac{r^3-r^2}{2}.     \tag{A23}
$$
With three distinct replica labels the orientations balance.
With two equal labels their signed excess, summed over the possible
equal pairs, is two for each pair of replica labels.
With all labels equal the excess is one.
Thus the excess is $2\binom r2+r=r^2$, proving (A23).

The resulting phase average is
$$
             \Psi_r(\vartheta)=\cos\vartheta+
                                      \frac{i}{r}\sin\vartheta.
$$
Every finite component has $K$ translates. The sum over all replica
assignments is invariant under cyclically moving the physical origin:
the corresponding time order is cyclically permuted, and conjugation
by $A$ preserves its central Weyl phase.
Consequently
$$
 d_{r,K}=-i\!\!\sum_{\substack{1\le d<e\le K-1\\
                              n_0v_0+n_dv_d+n_ev_e=0\\
                              n_0n_dn_e\ne0}}
       \widehat f_{n_0}\widehat f_{n_d}\widehat f_{n_e}
                             \Psi_r(\vartheta).             \tag{A24}
$$
The cutoff is the length of a finite influence interval.
Winding triples, including (A14), belong to the separate remainder
in (A21); they have not been included in (A24) or discarded.

### 6.4 Convergence to the classical third cumulant

For a triple in (A22), (A7) bounds $\lambda^{(d-1)/2}$
by $100\|c\|_1$. Hence
$$
 |n_0n_db_d|\le C\|c\|_1^4.
$$
The analytic Fourier decay and the component estimate imply absolute
summability even with this polynomial factor inserted.
Since $|\Psi_r(\vartheta)-1|\le2|\vartheta|$ for every $r\ge1$,
the phase error in the entire sum (A24) is $O_{f,a}(N^{-1})$,
uniformly in $r$.
For the length tail, insert the factor $2^{d+(e-d)}$ in the
gap majorant. The finiteness of $H_\alpha(2)$ gives
an $O_f(2^{-K})$ tail. Therefore
$$
 d_{r,K}=-i\sum_{1\le d<e} C_{d,e}
                  +O_{f,a}(N^{-1}+2^{-K}),                \tag{A25}
$$
uniformly over all replica counts. This also proves the absolute
convergence asserted in (A16).

For explicit computation, the integral $C_{d,e}$ is precisely the
Fourier sum in (A24) without $\Psi_r$.
All its integer triples are multiples of
$$
 \frac1g(b_{e-d},-b_e,b_d),\qquad
             g=\gcd(b_{e-d},b_e,b_d).                       \tag{A26}
$$
The two determinant equations prove this formula directly.
Terms with exactly two equal time indices have zero integral, because
the Fourier support of $f_i^2$ remains parallel to $v_i$, whereas
$v_j$ is not parallel to $v_i$ for $j\ne i$.
Expanding the cube of a classical time sum and using absolute
convergence now proves
$$
 \lim_{L\to\infty}\frac1L\int
                \left(\sum_{j=0}^{L-1}f_j\right)^3
                       =\kappa_3(f).
$$
Thus (A16) is a classical cumulant rate, with all combinatorial
factors specified; this identification does not appeal to a
separate classical central limit theorem.

Finally put $x=t/\sqrt K$ in (A19)--(A25).
The two remainders $K|x|^4$ and $K^2|x|^6e^{CK|x|^3}$
are $O_T(K^{-1})$. The cross terms in multiplying the two expansions
have the same bound.
The odd-projector correction is
$O(e^{F_0T\sqrt K}/N)=O_{f,T}(K^{-1})$.
This proves (A17).

For $f=2\cos\theta+2b\cos6\theta$, the only temporal term is
$C_{1,2}=2b$ and $\mu_3=0$, so $\kappa_3=12b$.
Theorem 2 therefore contains (A15) and makes it uniform in the
replica count with the stated rescaling.
For the independent four-mode check with positive Fourier
coefficients $(1,1/3,1/5,1/7)$ at modes $(1,2,6,35)$, the
nonzero temporal terms are
$$
 C_{1,2}=2/5,\quad C_{1,3}=C_{2,3}=2/35,\quad
                   \mu_3=2,\quad\kappa_3=178/35.
$$
These examples separate one-site skewness from temporal skewness.

## 7. Removing analyticity in the central-limit window

Analyticity can be removed from the first-correction result, with
explicit control of the constants needed in Fourier truncation.
In this section suppose that $f$ is real, even, nonzero and mean zero,
and that
$$
 {\cal F}_{32}(f):=\sum_n(1+|n|)^{32}|\widehat f_n|<\infty.
$$
In particular every $C^\infty$ position symbol qualifies.

**Theorem 3.** For every fixed $T$, uniformly in $r\ge1$ and
$|t|\le T$,
$$
 \operatorname{tr}_-U_{t/(r\sqrt K),f,a}^{rK}
 =e^{-\sigma_f^2t^2/2}
       \left[1-\frac{i\kappa_3(f)t^3}{6\sqrt K}\right]
                   +O_{f,a,T}(K^{-7/12}).                  \tag{A27}
$$
Here $\kappa_3$ is still the absolutely convergent series (A16).
The exponent and the Fourier regularity requirement are convenient
sufficient choices, not claimed optimal.

Put $f_M=\sum_{|n|\le M}\widehat f_n e^{in\theta}$ and give it
strip width $\rho_M=1/M$. Its weighted Fourier norms of orders zero
and one are bounded by $e{\cal F}_{32}(f)$, uniformly in $M$.
Thus the constants in the one-site estimates, (A9), and (A18)
are uniform; the tree criterion only requires $C|x|^2<c/M$.
For $\alpha=1/(4M)$, the explicit lattice constants obey
$$
 b_\alpha\le CM,\quad H_\alpha(1)\le CM,\quad
 H_\alpha(2)\le CM,\quad
 B_\alpha\le CM^5,\quad \eta_\alpha\ge cM^{-2}.              \tag{A28}
$$
Indeed $e^{-y}\le (ey)^{-1}$ and $2/\sqrt\lambda<1$ bound
both series $H_\alpha(R)$ by convergent geometric series times
$C/\alpha$, for $R=1,2$.

Choose the uniform complex disk $|x|\le cM^{-2}$.
It satisfies both the tree criterion and the required analytic
strip margin in (A20). The one-component sum per start is
$O(M^5|x|^3)$ there; Cauchy's estimate after the cubic term is
$O(M^7|x|^4)$ on the disk of half that radius.
The multi-component bound becomes
$CK^2M^{10}|x|^6e^{CKM^5|x|^3}$.
The polynomial factor in the phase estimate (A25) costs at most
another $M^4$, by absorbing $\|c\|_1^4$ into half of the strip.
Consequently at $x=t/\sqrt K$ the error in (A17) for $f_M$ is at most
$$
 C_{f,a,T}\left[
 \frac{1+M^7}{K}
 +\frac{M^{10}}K e^{CM^5/\sqrt K}
 +\frac{M^9}{N\sqrt K}+\frac{M^5\,2^{-K}}{\sqrt K}
 +(3/4)^K+\frac{e^{F_0T\sqrt K}}{N-1}\right].               \tag{A29}
$$
This estimate, rather than an unspecified constant depending on $f_M$,
justifies the moving truncation.

For completeness, absolute convergence of (A16) for the present
nonanalytic $f$ follows directly from the gap bound.
For any fixed nonzero charge triple of total absolute size $R$,
(A7) allows at most $C\log^2(2+R)$ pairs $(d,e)$.
Summing this bound against the three Fourier coefficients proves
absolute convergence. It also gives
$$
 |\kappa_3(f)-\kappa_3(f_M)|\le C_f M^{-16},\qquad
 |\sigma_f^2-\sigma_{f_M}^2|\le C_f M^{-32}.                 \tag{A30}
$$
For example on the tail $\max|n_j|>M$, absorb the logarithmic
factor into $(1+\max|n_j|)^{16}$, extract $M^{-16}$, and use
the remaining order-32 Fourier moment. The onsite cubic tail
has the stronger order-32 bound.

Finally the unitary telescoping inequality, applied to the actual
diagonal kicks, gives
$$
 \left|\operatorname{tr}_-U_{\epsilon,f,a}^{rK}
           -\operatorname{tr}_-U_{\epsilon,f_M,a}^{rK}\right|
 \le rK|\epsilon|\|f-f_M\|_\infty
 \le T\sqrt K\,{\cal F}_{32}(f)M^{-32}.                    \tag{A31}
$$
Choose $M=\lfloor K^{1/24}\rfloor$.
For all sufficiently large $K$ the complex-disk condition holds.
The largest term in (A29) is $M^{10}/K=O(K^{-7/12})$;
$M^5/\sqrt K\to0$. The error in (A31) is $O(K^{-5/6})$.
The variance and third-cumulant replacements from (A30) are smaller.
This proves (A27).

This argument proves a bounded-$t$ result for smooth symbols.
It does not extend (A1) to arbitrary smooth $f$ and every sequence
$\epsilon_K\to0$ with $K\epsilon_K^2\to\infty$.
The moving cutoff would have to satisfy incompatible estimates in
some of those larger ranges, so no density argument is asserted there.

## 8. Checks and unresolved scope

[analytic_kick_return_gas.py](../computations/verification/analytic_kick_return_gas.py)
checks 1,152 exact rational homogeneous gaps, all 1,034 finite components
in the indicated bounded alphabet and hull range, and 1,579 seeded
cyclic rational-preimage configurations.
It also exhausts 612,864 ordered cubic atom words across $K=10,14,18$,
including repeated physical kick sites.
An independently organized expansion into unordered atom multisets
with exact factorial weights checks another 2,532,760 configurations.
It verifies (A23) for two Fourier alphabets and several replica counts,
including the winding alias at $K=10$.
For the four-mode classical coefficient, (A7) proves that both
temporal gaps are at most 11; exhaustive enumeration in that proved
range gives the three correlations displayed above.
A further 5,152,304 unordered cubic configurations are classified
by their exact rational preimages at $K=10,14,18,22,34$.
They confirm separately the zero aggregate, the finite-component
coefficient (A24), and winding contributions.
For these four modes, additional winding terms occur at $K=14,18$
as well as $K=10$. They are absent at $K=22,34$ in the enumeration.
At $K\ge34$ their absence is proved without enumeration:
a cubic forcing has total absolute size at most $3\cdot35$,
so (A7) bounds each winding gap by 11 and $K\le3\cdot11$
would be necessary.
These checks verify finite algebra and expose the extra term in (A14).
They do not replace the analytic convergence arguments.

    OPENBLAS_NUM_THREADS=1 python computations/verification/analytic_kick_return_gas.py \
      --output build/analytic-kick-return-gas-precheck.json

The analytic strip assumption is essential to the uniform bound (A1).
Section 7 extends the central-limit window and its first correction to
smooth position symbols, with a controlled moving Fourier truncation.
Arbitrary functions of both position and momentum are not covered here.
The analytic time bound remains $r|\epsilon|\le s_0$.
When $K\epsilon^2\to\infty$, this gives $rK=o(K^{3/2})$,
far below the Heisenberg scale $D\asymp N$.
No implication from (A1)--(A3) to microscopic BGS is asserted.
