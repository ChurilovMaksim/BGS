---
title: "A second-order resonance scale for coboundary kicks of a fixed cat map"
author: "WoW research programme"
date: "5 September 2026"
---

# Status, precedent, and statement

This note gives a project proof, with separately scoped finite checks. It is
not a claim of world priority or a complete Lean formalization. Residual
perturbations, removal of a coboundary at first order, and a second-order
commutator as the effective perturbation are established mechanisms in the
quantum-fidelity literature: Prosen and Znidaric, *Phys. Rev. Lett.* **94**
(2005), 044101, especially equations (4)--(7) and (12) of the primary preprint
[quant-ph/0401142](https://arxiv.org/abs/quant-ph/0401142).
The specific assertions proved here are a uniform finite operator estimate,
a two-species arithmetic collision classification, and deterministic spectral
limits along the Pell recurrence sequence. Fidelity decay in a mixing
approximation must not be substituted for these spectral assertions.

Set
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 \alpha=1+\sqrt2,\quad \lambda=3+2\sqrt2,\quad
 N+F\sqrt2=\alpha^K,
$$
where K tends to infinity through odd primes. Then N is odd,
$N^2-2F^2=-1$, and $N\asymp\lambda^{K/2}$. The moduli need not be prime.
Use the phase-normalized cat quantization $U_0$ from the
[finite Floquet construction](pell_floquet_normal_form.md), so that
$U_0W(v)U_0^*=W(Tv)$ and $U_0^K=I$. Let
$$
 W(a,b)f(x)=e_N(a(x-b/2))f(x-b),\qquad B_v=W(v)+W(-v).
$$
All symmetrized observables and $U_0$ preserve odd parity. Write
$d=(N-1)/2$ and $\tau_-(M)=d^{-1}\operatorname{Tr}_{-}M$.

The perturbation is now a different, fixed Fourier observable:
$$
 A=B_{(1,0)},\quad D=U_0AU_0^*=B_{(3,4)},\quad
 H=A-D,\quad V_\varepsilon=e^{i\varepsilon H}U_0.                 \tag{1}
$$
It is a coboundary: $\sum_{j=0}^{K-1}U_0^jHU_0^{-j}=0$ exactly.
The real classical Fourier symbol of H is independent of N. The products
of the two coordinates of (1,0), (3,4), (2,4), and (4,4) are even, so the
centered finite-Weyl convention introduces no N-dependent sign for these
fixed Fourier modes. As throughout
the project, the quantum exponent epsilon corresponds to a classical action
amplitude proportional to epsilon/N, not epsilon itself.

Put
$$
 s_N=\sin(4\pi/N)>0,\quad \zeta=\varepsilon^2s_N,\quad
 t_K=2\zeta\sqrt K.
$$
**Theorem 1 (second-order critical law).** If $t_K\to t\in[0,\infty)$,
then for every fixed integer m,
$$
 \tau_-(V_{\varepsilon_K}^{mK})\longrightarrow e^{-m^2t^2/2}.     \tag{2}
$$
Thus the empirical spectrum of $V_{\varepsilon_K}^K$ tends to the wrapped
normal law of variance $t^2$, or to the point mass at 1 when t=0. The
critical quantum scale is
$$
 |\varepsilon_K|=\left(\frac{t}{2s_N\sqrt K}\right)^{1/2}
 \sim\sqrt{\frac{t}{8\pi}}\,\sqrt N K^{-1/4}\quad(t>0).         \tag{3}
$$
This can grow without bound, even though the classical amplitude tends to
zero. The sign of epsilon does not change the limit in (2).

**Theorem 2 (negative microscopic consequences).** For the original
propagator in (1), on the whole odd space and with global mean-spacing
normalization, the following hold.

If $|\varepsilon_K|K^{1/4}/\sqrt N\to0$, the empirical nearest-neighbour
spacing measures tend weakly to $\delta_0$, and the normalized number of
ordered distinct pairs at distance at most x mean spacings tends to infinity
for every fixed x>0.

For any subsequence on which $|\varepsilon_K|K^{1/4}/\sqrt N$ is bounded,
the pair measures cannot converge to a bounded density R(s) with
$R(s)\to1$ as $|s|\to\infty$. In particular, escape from this obstruction
requires
$$
 |\varepsilon_K|K^{1/4}/\sqrt N\longrightarrow\infty.            \tag{4}
$$
Condition (4) is only necessary. No positive universality theorem beyond it
is proved. These statements concern global unfolding of the specified odd
spectrum, not arbitrary clusterwise unfolding or an assertion that all
arithmetic symmetries are resolved. They do not refute fixed-system BGS.

# 1. A second-order loop estimate valid at large quantum exponents

**Lemma 3.** For finite Hermitian A,D and any real epsilon,
$$
 \left\|e^{-i\varepsilon A}e^{i\varepsilon(A-D)}e^{i\varepsilon D}
       -e^{-\varepsilon^2[A,D]/2}\right\|_{\rm op}
 \leq |\varepsilon|^3\left(
       \frac12\|[A,[A,D]]\|_{\rm op}
       +\frac16\|[D,[A,D]]\|_{\rm op}\right).                  \tag{5}
$$
There is no hypothesis $|\varepsilon|\|A\|\ll1$.

**Proof.** Write $Q=[A,D]$ and
$L(u)=e^{-iuA}e^{iu(A-D)}e^{iuD}$. Direct differentiation gives
$$
 L'(u)L(u)^*=-\int_0^u
       \operatorname{Ad}_{e^{-iuA}e^{iv(A-D)}}Q\,dv.
$$
The logarithmic derivative of $E(u)=e^{-u^2Q/2}$ is -uQ. By differentiating
unitary conjugation and integrating,
$$
 \|\operatorname{Ad}_{e^{-iuA}e^{iv(A-D)}}Q-Q\|
 \leq u\|[A,Q]\|+v\|[A-D,Q]\|\quad(0\leq v\leq u).
$$
Duhamel comparison of the two unitary evolutions, integrated over
$0\leq v\leq u\leq\varepsilon$, is at most
$\varepsilon^3(\|[A,Q]\|/3+\|[A-D,Q]\|/6)$. The triangle inequality
proves (5) for nonnegative epsilon. Replace A,D by -A,-D for the other
sign. This argument is a norm estimate, not a truncation of a formal BCH
series. End of proof.

Let u=(2,4), z=(4,4) and C=B_u-B_z. Since
$W(v)W(w)=e_N(\omega(v,w)/2)W(v+w)$ and
$\omega((1,0),(3,4))=4$, exact multiplication yields
$$
 [A,D]=-2i s_N C.                                             \tag{6}
$$
Each double commutator in (5) has at most eight Weyl terms of coefficient
modulus $4s_N^2$. Therefore both norms are at most $32s_N^2$, and
$$
 \left\|e^{-i\varepsilon A}V_\varepsilon e^{i\varepsilon A}
                  -e^{i\zeta C}U_0\right\|_{\rm op}
 \leq R_N(\varepsilon):=\frac{64}{3}|\varepsilon|^3s_N^2.        \tag{7}
$$
The same bound holds in normalized odd Hilbert--Schmidt norm. At the scale
(3), $KR_N=O_t(K^{1/4}/\sqrt N)$; this tends to zero. The small quantity is
controlled by nested commutators, not by the norm of epsilon A.

# 2. A two-species arithmetic lemma: collisions must not be discarded

Identify an integer vector v=(a,b) with $\psi(v)=b+\sqrt2 a$. Then
$$
 \psi(Tv)=\lambda\psi(v),\quad
 \psi(u)=4+2\sqrt2,\quad \psi(z)=\sqrt2\psi(u),\quad
 \operatorname{Norm}(\psi(u))=8.
$$
Since N is odd, multiplication by $\psi(u)$ is invertible in
$(\mathbb Z/N\mathbb Z)[\sqrt2]$. The two species of time translates are
therefore faithfully represented by $\lambda^j$ and $\sqrt2\lambda^j$.
Also $T^K=I$ modulo N, as follows from $Q_{2K}=2N^2+1$ and
$P_{2K}=2NF$. Rotating all labels modulo K preserves a vector relation.

**Lemma 4 (lifting).** A signed m-atom modular zero relation in these two
species, after cancellation of identical opposite atoms and rotation across
a largest cyclic gap, has the form
$$
 P(\lambda)=\sum_\nu \epsilon_\nu b_\nu\lambda^{j_\nu},
 \quad b_\nu\in\{1,\sqrt2\},\quad
 0\leq j_\nu\leq K-\lceil K/m\rceil.
$$
For sufficiently large K at fixed m this expression is zero in
$\mathbb Z[\sqrt2]$, not just modulo N. For m=4, K>=11 suffices.

**Proof.** There are at most m occupied time labels, hence a cyclic gap
of at least ceil(K/m). Modular vanishing and the invertibility just proved
imply $P(\lambda)\in N\mathbb Z[\sqrt2]$. Its nonzero algebraic norm
would thus have absolute value at least $N^2$, whereas the two real
embeddings give
$$
 |\operatorname{Norm}P(\lambda)|
 \leq2m^2\lambda^{K-\lceil K/m\rceil}.
$$
Since $N^2=\lambda^K(1-\lambda^{-K})^2/4$, the latter is smaller than
$N^2$ for large K at fixed m. For m=4 it suffices that
$\lambda^{\lceil K/4\rceil}(1-\lambda^{-K})^2>128$. At K>=11 this
follows from $\lambda>11/2$, ceil(K/4)>=3, and
$1-\lambda^{-K}>9/10$, since $(11/2)^3(9/10)^2>128$. End of proof.

A four-atom relation in characteristic zero need **not** balance within
individual species. Apart from cancellation, the sole type is
$$
 z_{j+1}-u_{j+1}=z_j+u_j,\qquad v_j:=T^jv,                     \tag{8}
$$
up to translation and multiplication by -1. The identity is already true
over the integers, since $T(z-u)=z+u$.

Here is a direct completeness proof. Look at the maximal exponent E after
cancellation. With one atom at E, its coefficient has modulus at least 1,
whereas the three lower atoms sum to at most $3\sqrt2/\lambda<1$ times
$\lambda^E$. With three atoms at E, their nonzero coefficient has modulus
at least $2-\sqrt2>\sqrt2/\lambda$, which the remaining lower atom cannot
cancel. With four atoms at E, linear independence of 1 and sqrt(2) forces
balance. With two atoms at E, the only possible nonzero coefficient small
enough is $\pm(\sqrt2-1)$. The lower atoms must both be at E-1: otherwise
at that scale their modulus is at most
$\sqrt2(1+\lambda^{-1})<1+\sqrt2$. At E-1 they must be one of each
species with equal signs because $\lambda(\sqrt2-1)=1+\sqrt2$. This is
exactly (8). Relations with fewer occurrences reduce to the same cases;
there is no nontrivial relation with at most three atoms.

**Corollary 5 (multiplicity two).** For K>=11, form all signed unordered
pairs with distinct time labels:
$$
 \epsilon v_t+\delta w_s,
 \quad 0\leq t<s<K,\quad v,w\in\{u,z\},\quad
 \epsilon,\delta\in\{-1,1\}.
$$
There are $8K(K-1)$ such pairs. Their vector keys are nonzero, have
multiplicity at most two, and have precisely
$$
 4K\ \hbox{double keys},\quad 8K(K-2)\ \hbox{single keys},
 \quad 8K^2-12K\ \hbox{distinct keys}.                          \tag{9}
$$
The double classes are the two identities
$$
 z_{j+1}-z_j=u_{j+1}+u_j,\qquad
 z_{j+1}-u_j=u_{j+1}+z_j,
$$
with their negatives, for j modulo K. The third partition of (8) uses
equal-time pairs and is not in the domain. Each displayed signed pair
belongs to only one class: its species, the two adjacent cyclic labels,
and its signs determine the other pair. Thus there are no triple classes
or overlapping equivalence chains. Lemma 4 ensures that no additional
modular relation is missed. K=3 is a useful negative control: it has six
triple keys, and the range restriction must not be removed.

# 3. Weighted phase control and a finite normal form for C

Write $C_j=U_0^jCU_0^{-j}$,
$\bar C=K^{-1}\sum_j C_j$, $G_C=\sum_j c_jC_j$, where
$c_j=(K-1-2j)/(2K)$. Then
$$
 G_C-U_0G_CU_0^*=C-\bar C,\qquad [\bar C,U_0]=0.                \tag{10}
$$
Define a phase majorant, including both species,
$$
 a_j=\max_{v,w\in\{u,z\}}
          |e_N(\omega(v,T^jw))-1|.
$$
One has $a_{K-j}=a_j$. In particular, no independence assumption about the
several phase factors is being made.

For a centered representative delta of j modulo K,
$$
 \omega(v,T^\delta w)
 =(2v_1w_1-v_2w_2)P_{2\delta}+\det(v,w)Q_{2\delta}.
$$
For the four choices of species these are $-8P_{2\delta}$,
$16P_{2\delta}$, and $\pm8Q_{2\delta}$, respectively. Their absolute
values are at most $8\lambda^{|\delta|}$. If
$|\delta|=(K-1)/2-\ell>0$, this gives
$$
 a_j\leq\frac{32\pi}{\alpha(1-\lambda^{-K})}\lambda^{-\ell}.
$$
At zero, $a_0\leq16\pi/N$. Summing both signs, including their weights
$\ell/K$ and $(\ell+1)/K$, proves the explicit estimates
$$
 \begin{split}
 L_K:=\sum_j a_j
   &\leq\frac{32\pi}{1-\lambda^{-K}}+\frac{16\pi}{N}<128,\\
 K\sum_j|c_j|a_j
   &\leq\frac{16\sqrt2\pi}{1-\lambda^{-K}}+
                                      \frac{8\pi K}{N}<128.
 \end{split}                                                    \tag{11}
$$
For K>=3, use $\lambda^{-K}<1/10$, $N\geq2K+1$, $\pi<22/7$, and
$\sqrt2<3/2$ to check the last inequalities. These constants are deliberately
conservative.

The commutator $[C_t,C_s]$ has sixteen Weyl terms, each of modulus at most
$a_{s-t}$. Corollary 5 says that each key in the sum over t<s has at most
two preimages. Weyl matrices are orthonormal in the *full* normalized
Hilbert--Schmidt inner product, also over composite odd N. Cauchy--Schwarz
inside each key class therefore gives
$$
 \begin{split}
 \|[G_C,\bar C]\|_{2,N}^2
 &\leq\frac{32}{K^4}\sum_{j=1}^{K-1}(K-j)j^2a_j^2\\
 &=\frac{16}{K^3}\sum_{j=1}^{K-1}j(K-j)a_j^2
 \leq\frac{1024}{K}.
 \end{split}                                                    \tag{12}
$$
The equality between the two sums uses $a_{K-j}=a_j$; the final bound uses
$a_j^2\leq2a_j$ and (11). Norm restriction to the odd subspace obeys
$\|M\|_{2,-}\leq\sqrt{2N/(N-1)}\|M\|_{2,N}$ by positivity. We have
not assumed orthogonality of restricted Weyl matrices.

The triangle inequality in operator norm also gives
$$
 \|[G_C,C]\|_{\rm op}\leq2048/K,\qquad
 \|[C,\bar C]\|_{\rm op}\leq2048/K.                           \tag{13}
$$
The usual two-exponential Duhamel inequality is
$\|e^{ixA}e^{ixD}-e^{ix(A+D)}\|\leq x^2\|[A,D]\|/2$ in any
unitarily invariant norm. Applying it first to -G_C,C, then to
C-G_C and $U_0G_CU_0^*$, using (10)--(13), proves
$$
 \left\|e^{-i\zeta G_C}(e^{i\zeta C}U_0)e^{i\zeta G_C}
                        -e^{i\zeta\bar C}U_0\right\|_{2,-}
 \leq\frac{1000\zeta^2}{\sqrt K}\quad(K\geq11).               \tag{14}
$$
Indeed the less rounded bound is
$\zeta^2(2048/K+16\sqrt{2N/(N-1)}/\sqrt K)$, which is smaller than
(14) already using $K\geq11$ and $N\geq7$. This is another estimate valid
for every real zeta, not a formal expansion requiring a small generator.

Combining the two gauges and telescoping unitary powers gives
$$
 \left|\tau_-(V_\varepsilon^{mK})-
          \tau_-(e^{im\zeta K\bar C})\right|
 \leq |m|KR_N(\varepsilon)+1000|m|\zeta^2\sqrt K.              \tag{15}
$$

# 4. The two-species Gaussian limit

**Lemma 6.** Put $X_K=(\sqrt K/2)\bar C$. For every fixed r>=1,
$$
 \tau_-(X_K^{2r})=(2r-1)!!+O_r(K^{-1})+O_r(K^r/N).             \tag{16}
$$
For every fixed odd m, eventually
$|\tau_-(X_K^m)|\leq(4K)^{m/2}/(N-1)$. Consequently its empirical
spectral measures converge weakly and in quadratic Wasserstein distance
to standard normal.

**Proof.** There are 4K signed Weyl atoms, with coefficient +1 for species u
and -1 for species z. For a word with central phase e_N(phi) and total
index v, the exact odd trace is
$$
 e_N(\phi)\frac{N\mathbf1_{v=0}-1}{N-1}.                       \tag{17}
$$
This follows from $\operatorname{Tr}W(v)=N\mathbf1_{v=0}$ and
$\operatorname{Tr}(RW(v))=1$. The noncentral contribution after
normalization $(4K)^{-m/2}$ is at most $(4K)^{m/2}/(N-1)$.

Apply Lemma 4 to central words. The following bounded-cluster argument
handles the unavoidable identities (8), rather than incorrectly excluding
them. In a nonzero polynomial relation with at most m signed atoms and
coefficients 1 or sqrt(2), a gap d with $\lambda^d>2m^2$ separates
independently vanishing components. To see this, write
$P=P_{\rm low}+Z^{a+d}P_{\rm high}$ with degree of P_low at most a.
If $P_{\rm high}(\lambda)\ne0$, its nonzero integer norm and the bound
$|P_{\rm high}(\lambda^{-1})^{\rm conjugate}|\leq\sqrt2m$
give $|P_{\rm high}(\lambda)|\geq1/(\sqrt2m)$. This contradicts
cancellation by $|P_{\rm low}(\lambda)|\leq\sqrt2m\lambda^a$.
Iterating produces components with spans bounded solely in m.

Cancel opposite identical atoms first and restore these pairs after splitting.
Every nonzero component then contains at least three occurrences. A two-atom
relation cannot change species, because its two algebraic norms would be
1 and -2, and cannot change exponent, because lambda>1. A nonbalanced
2r-word thus has at most r-1 components. There are only finitely many
partitions of its positions, species, signs and bounded offset patterns at
fixed r. Each component has K possible cyclic translations, so there are
$O_r(K^{r-1})$ such words. Choosing the largest-gap cut introduces no
additional K factor: this count is over the actual translated components.
Their normalized contribution is $O_r(1/K)$.

In a balanced word, pair identical species-time labels with opposite signs.
For each pairing there are K^r time choices, $2^r$ species choices and
$2^r$ sign choices. Their product is precisely the normalization $(4K)^r$.
Repeated pair labels cause at most $O_r(K^{r-1})$ overcount. Signs from
species z occur twice in each pair and hence multiply to +1. The Weyl phase
is a product of crossing factors or their conjugates. For fixed species,
each crossing time difference is uniform on the cyclic group. By (11) and
$|\prod u_j-1|\leq\sum|u_j-1|$, its average error is at most
128 times the number of crossings divided by K. No independence of the
crossing factors is assumed. Summing over the $(2r-1)!!$ pairings gives (16).

For odd m, reduce a lifted relation in $\mathbb Z[\sqrt2]$ modulo 2.
Here $\lambda=3+2\sqrt2$ reduces to 1. The coefficients of both 1 and
sqrt(2) in the relation must be even. Both species counts would therefore
be even, contradicting odd m. Thus no odd central word exists after lifting.

Bounded second moments yield tightness, higher even moments yield uniform
integrability, and the Gaussian moment sequence is determinate, since its
Carleman sum diverges. Therefore all weak subsequential limits are normal.
Convergence of the second moments gives the claimed Wasserstein upgrade.
End of proof.

Since $\zeta K\bar C=t_KX_K$, (15) and Lemma 6 prove Theorem 1. More
explicitly, the finite comparison error is bounded by
$$
 |m|\left(KR_N(\varepsilon)+\frac{250t_K^2}{\sqrt K}\right).    \tag{18}
$$
For bounded t_K, $KR_N=O(K^{1/4}/\sqrt N)$ follows directly from
$\varepsilon^2=t_K/(2s_N\sqrt K)$ and $s_N\leq4\pi/N$.
The remaining Gaussian characteristic-function error is o(1); no universal
$K^{-1/2}$ rate is asserted for that separate step.

# 5. Microscopic consequences without conflating unfolding conventions

For completeness we give the two spectral implications used in Theorem 2.
First, the 4K Weyl atoms in C_j are distinct, so
$\operatorname{Tr}(\bar C^2)/N=4/K$. Distinctness follows within species
from the unit conditions on $1\pm h^j$ in the Pell construction. Between
species, norm 1 versus -2 would require N to divide 3, which is impossible
for K>=3. Consequently
$$
 \tau_-(\bar C^2)\leq\frac{8N}{K(N-1)}.
$$
The squared-overlap matrix between orthonormal eigenbases of two unitaries
is doubly stochastic. Decomposing it into permutations yields an eigenvalue
matching whose mean squared chord cost is bounded by normalized squared
Hilbert--Schmidt distance. Circle distance in $\mathbb R/\mathbb Z$ is at
most one quarter of chord distance. Using this matching, (7),(14), and
$[U_0,\bar C]=0$, the RMS distance a of the spectrum of V_epsilon from the
K-point lattice satisfies
$$
 a\leq\frac{R_N(\varepsilon)}4+
          \frac{250\zeta^2}{\sqrt K}+
          \frac{|\zeta|}{2\pi}\sqrt{\frac{8N}{K(N-1)}}.         \tag{19}
$$
When t_K tends to zero, Ka tends to zero, and K/d tends to zero.

For an arbitrary d-point circle multiset with this RMS lattice distance,
placing arcs of half-width w<1/(2K) around the lattice and using Markov's
inequality gives, for its unfolded cyclic gaps S_l,
$$
 d^{-1}\#\{l:S_l>x\}\leq2a^2/w^2+K/d+2Kw/x.                  \tag{20}
$$
There are at most $da^2/w^2$ bad points; at most twice as many gaps touch
one, at most K other gaps leave an arc, and the within-arc gaps have total
length at most 2Kw. This proves (20). Partitioning the arcs into cells of
length at most x/d and applying Cauchy--Schwarz to their occupancies also
gives the ordered close-pair bound
$$
 R_2(x)\geq\frac{\max(0,1-a^2/w^2)^2}{K/d+2Kw/x}-1.           \tag{21}
$$
Take $w=(Ka)^{2/3}/K$ for (20), and w=2a for (21). These prove subcritical
spacing collapse and divergent close-pair counts. The a=0 case follows
by counting at most K nonzero gaps and using $R_2(x)\geq d/K-1$.
The average spacing remains exactly one: weak convergence to delta_0 does
not imply convergence of first moments, which are carried by rare long gaps.

For bounded nonzero critical parameter a different argument is necessary.
Let
$\phi_L(s)=L^{-1}(1-|s|/L)_+$, a compactly supported nonnegative function
with integral one and Fourier transform $\operatorname{sinc}^2(L\xi)$.
For the eigenangles theta_l in $\mathbb R/\mathbb Z$, define
$$
 C_d(\phi_L)=\frac1d\sum_{l\ne j}\sum_{q\in\mathbb Z}
                       \phi_L(d(\theta_l-\theta_j+q)).
$$
Poisson summation, including the zero Fourier mode and the removed diagonal,
proves, for d>L,
$$
 C_d(\phi_L)\geq1-\frac1L+
       2\sum_{m=1}^{M}\operatorname{sinc}^2(LmK/d)
                                 |\tau_-(V_\varepsilon^{mK})|^2. \tag{22}
$$
All omitted Fourier coefficients are nonnegative. Take K to infinity at
fixed M, use (2), then let M grow. For t>0 this gives
$$
 \liminf C_d(\phi_L)\geq\Theta(t)-1/L,\qquad
 \Theta(t)=\sum_{m\in\mathbb Z}e^{-m^2t^2}>1.                  \tag{23}
$$
For t=0 the lower bound is infinite. If the pair measures converged on
compact tests to a bounded density R(s) tending to 1 at infinity, then
$\int\phi_LR\to1$ as L grows. This contradicts (23). A bounded subsequence
of $|\varepsilon|K^{1/4}/\sqrt N$ has a further subsequence with finite
limiting t_K, so (4) follows. This is a necessary-condition argument, not
an exchange of a growing test support with the semiclassical limit.

An equivalent moving-window consequence is
$$
 \liminf\operatorname{Var}_{\theta}\!\bigl[
      \#\{l:\theta_l\in[\theta,\theta+L/d)\}\bigr]
       \geq L^2(\Theta(t)-1).
$$
Indeed the finite variance is $L^2(C_d(\phi_L)-1)+L$. The underlying
positive Fourier test was already established in the earlier Floquet note;
it is not claimed as a new result of this pass.

# 6. Scientific boundary and verification contract

The scale (3) is parametrically larger than the first-order cosine scale
$\varepsilon\asymp K^{-1/2}$, but the observable is different. This is
not an improvement obtained while silently changing a fixed hypothesis:
the role of the coboundary is explicit in (1). Both classical perturbation
amplitudes vanish. No fixed nonzero classical perturbation, positive BGS
universality, or trace theorem at times of order d is proved.

The new ingredients relative to the maintained project are the uniform loop
bound with growing quantum exponent, the multiplicity-two classification
needed for the generated two-species observable, and their deterministic
spectral combination. The residual-perturbation mechanism and its second-order
commutator have direct prior literature. A full priority assessment remains
unfinished; no prize-level or first-ever claim follows from these notes.

Verification uses `pell_coboundary_regression.py` in the verification
directory and the independent `pell_coboundary_pairs.cpp` in the C++ directory.
The Python pair verifier iterates original T-vectors and checks each double
class, while C++ uses the quotient quadratic ring after dividing out
4+2sqrt(2). Floating-point dense checks test (5)--(7) and the complete
propagator at K=3,5,7, explicitly outside the universal K>=11 collision range.
They are separate from exact combinatorial checks and not an asymptotic proof.
The finite Lean certificate has its own narrower scope; its successful
compilation must be recorded rather than inferred from source code.

## Numerical propagation and its separate error budget

The optional large-N experiment applies the actual coboundary kick rather
than replacing it by the effective observable. Since the norm of H is at
most 4, the Jacobi--Anger expansion gives
$$
 e^{i\varepsilon H}
 =J_0(z)I+2\sum_{j\geq1}i^jJ_j(z)T_j(H/4),\qquad z=4\varepsilon.
$$
Here $T_j$ is a Chebyshev polynomial. The standard Bessel series, as recorded
in [NIST DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2), implies
$$
 |J_j(z)|\leq b_j:=\frac{(|z|/2)^j}{j!}
                      \exp\!\left(\frac{z^2}{4(j+1)}\right).
$$
For $M+2>|z|/2$, the discarded operator tail is consequently bounded by
$$
 2\sum_{j>M}|J_j(z)|
 \leq\frac{2b_{M+1}}{1-|z|/(2(M+2))}.
$$
The code chooses the degree using this bound and checks norm preservation.
This is a truncation estimate, not interval certification of Bessel-function
rounding or of subsequent matrix arithmetic. A separate exponential-action
implementation agreed on the recorded K=11 controls to about 1e-13.

For R independent probes with fourth-root-of-unity coefficients in an
orthonormal odd basis, the normalized trace estimator has complex
mean-square error at most $1/(Rd)$ for exact unitary applications. Indeed,
only off-diagonal entries contribute to its variance and their squared sum
is at most d. The displayed RMS bounds are stochastic, not confidence
intervals. First and second recurrence modes, including finite-size bias,
are both retained. No agreement with a finite simulation is used as a proof
of the limiting theorem.
