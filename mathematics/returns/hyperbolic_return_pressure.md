# A convergent pressure formula for arithmetic quantum returns

**Research status.** The argument below is a project proof, checked by direct
algebra and finite computations. It has not received independent review or
a priority determination. It is an asymptotic theorem at one arithmetic
return, not a theorem about microscopic BGS statistics. This working note
has not been incorporated into the unified manuscript.

## 1. A family beyond the original Pell matrix

Let $A\in SL_2(\mathbb Z)$ have even trace $T\ge4$. Write
$d=T-2$, $\lambda=(T+\sqrt{T^2-4})/2$. Define integers
$u_{-1}=0,u_0=1,u_{j+1}=Tu_j-u_{j-1}$. For odd $K=2n+1\ge3$ put
$$
 N=u_n+u_{n-1}
   =\frac{\lambda^{K/2}-\lambda^{-K/2}}{\sqrt{T-2}}.
                                                               \tag{P1}
$$
Assume $\gcd(K,d)=1$. Fix $v\in\mathbb Z^2$ with
$\gamma=\omega(v,Av)$ invertible modulo $N$, where
$\omega((x,y),(x',y'))=xy'-yx'$. Let $a$ be any unit modulo $N$.
There is no primality assumption and no harmonic average.

Use centered Weyl operators with
$W(x)W(y)=e_N(\omega(x,y)/2)W(x+y)$, where division by $2$
is in $\mathbb Z/N$. For example,
$$
 (W(q,p)f)(x)=e_N(q(x-p/2))f(x-p).
$$
Let $U_0$ implement $U_0W(x)U_0^{-1}=W(Ax)$ and normalize its scalar
phase so that $U_0^K=I$. Set
$$
 U=e^{i\epsilon(W(av)+W(-av))}U_0,\qquad D=(N-1)/2.
                                                               \tag{P2}
$$
The odd trace $\operatorname{tr}_-$ is normalized by $D$.
The odd space is preserved. For $v=(1,0)$ the kick is the physical
position multiplier $2\cos(2\pi ax/N)$.

The normalization in (P2) exists: Cayley--Hamilton gives the exact identity
$$
 A^{n+1}-A^{-n}=N(A-I),\quad
 A^K-I=NA^n(A-I),\quad \sum_{j=0}^{K-1}A^j=NA^n.              \tag{P3}
$$
Consequently $A^K=I$ modulo $N$, so $U_0^K$ commutes with all Weyl
operators and is scalar. Also $N$ is odd, and $N\equiv K\pmod d$.
For a concrete member take $A=\left(\begin{smallmatrix}T&-1\\1&0
\end{smallmatrix}\right)$ and $v=(1,0)$; then $\gamma=1$.
A chirp times the inverse finite Fourier transform supplies its quantization.

**Theorem (one-return pressure).** There is a function
$\Lambda_T(\epsilon,\theta)$, analytic in complex $\epsilon$ for
$|\epsilon|<1/10$, continuous and periodic in real $\theta$, such that,
uniformly over the above choices and real $|\epsilon|\le1/10$,
$$
 \operatorname{tr}_-U^K
  =\Lambda_T(\epsilon,\gamma a^2/N)^K+E_K,\qquad
 |E_K|\le20(4/5)^K.                                         \tag{P4}
$$
For these real parameters,
$$
 e^{-3\epsilon^2/2}\le|\Lambda_T(\epsilon,\theta)|
                       \le e^{-\epsilon^2/2}.               \tag{P5}
$$
In particular (P4) is also a uniform relative asymptotic.
The function is defined by a convergent scalar equation in Section 4,
not by an unbounded transfer operator assumed to have a spectral gap.

For fixed $T$, its first resonance correction is
$$
 \log\Lambda_T(\epsilon,\theta)
 =\log J_0(2\epsilon)
   +\frac{2(-1)^{T/2-1}}{T!}\,
      e^{-\pi iT\theta}\epsilon^{T+2}
   +O_T(\epsilon^{T+4}),                                    \tag{P6}
$$
uniformly for real $\theta$. The branch of the logarithm is zero at
$\epsilon=0$.

For the original matrix with $T=6$ and $\gamma=4$, put
$\vartheta=a^2/N$. Formula (P6) reads
$$
 \log\Lambda_6(\epsilon,4\vartheta)
 =-\epsilon^2-\frac{\epsilon^4}{4}-\frac{\epsilon^6}{9}
   +\left(-\frac{11}{192}+\frac{e^{-24\pi i\vartheta}}{360}\right)
      \epsilon^8+O(\epsilon^{10}).                           \tag{P7}
$$
This keeps the Weyl phase of the first resonance. Discarding that phase
would lose the harmonic dependence.

## 2. The full central lattice, including its finite quotient

Let $L=S+S^{-1}-TI$ on $\mathbb Z^K$, with cyclic indices, and set
$$
 \mathcal C=\{c\in\mathbb Z^K:\sum_jc_jA^jv=0\bmod N\}.
$$
The orbit sum in (P3) makes $\mathbf1$ central. One has
$$
 L\mathbb Z^K=\{c\in\mathcal C:\sum_jc_j=0\bmod d\},
 \qquad
 \mathcal C=\coprod_{r=0}^{d-1}(L\mathbb Z^K+r\mathbf1).
                                                               \tag{P8}
$$
Indeed $|\det L|=\lambda^K+\lambda^{-K}-2=dN^2$.
The map
$$
 c\longmapsto\left(\sum_jc_jA^jv,\ \sum_jc_j\bmod d\right)
$$
onto $(\mathbb Z/N)^2\times\mathbb Z/d$ is surjective:
$v,Av$ are a basis modulo $N$, and a multiple of $Ne_0$ independently
adjusts the last coordinate because $\gcd(N,d)=\gcd(K,d)=1$.
Its kernel contains $L\mathbb Z^K$ and has the same index.
Finally $K=\sum_j1$ is a unit modulo $d$, proving the coset statement.
This proves (P8) at every order, without truncating the Fourier series.

For every real vector $p$,
$$
 \|Lp\|_1\ge d\|p\|_1.                                      \tag{P9}
$$
In the coset $r$, write $c=L(q-r\mathbf1/d)$.
For $0<z<1$ its generating function is bounded by $A_r(z)^K$, where
$$
 A_0(z)=\frac{1+z^d}{1-z^d},\qquad
 A_r(z)=\frac{z^r+z^{d-r}}{1-z^d}\quad(1\le r<d).             \tag{P10}
$$
In particular
$$
 \sum_{r=1}^{d-1}A_r(z)^K
 \le\frac{1}{1-z^K}\left(\frac{2z}{1-z^2}\right)^K.           \tag{P11}
$$
To check (P11), use $(x+y)^K\le2^{K-1}(x^K+y^K)$, sum the
two finite geometric series, and use $d\ge2$.

## 3. Exact localization of the ordered Weyl action

In the product
$$
 U^K=\prod_{j=0}^{K-1}
       e^{i\epsilon(W(aA^jv)+W(-aA^jv))}
$$
choose Fourier indices $c_j$. The scalar coefficient is
$\prod_j i^{c_j}J_{c_j}(2\epsilon)$, and the ordered Weyl phase is
$$
 \phi(c)=\frac12\sum_{i<j}c_ic_j\,
                       \omega(aA^iv,aA^jv)\pmod N.
$$
If $c=Lp$ for an integer $p$, then
$$
 \phi(c)=\frac{\gamma a^2}{2}\sum_jp_jc_j
 =\gamma a^2\sum_j(p_jp_{j+1}-T p_j^2/2)\pmod N.             \tag{P12}
$$

Here is a proof that also checks the order of multiplication.
Write $w_j=aA^jv$, $P_j=\sum_{i<j}c_iw_i$ and
$b_j=\omega(P_j,w_j)$. Centrality makes $b$ cyclic modulo $N$.
The recurrence $w_{j+1}=Tw_j-w_{j-1}$ gives
$$
 b_{j+1}-Tb_j+b_{j-1}=\gamma a^2c_j.
$$
Thus $b-\gamma a^2p$ solves the homogeneous recurrence. Every such
solution is a linear functional of $w_j$, since $w_0,w_1$ form a basis.
Its pairing with $c$ vanishes by centrality. Substitution into
$\phi=\frac12\sum_jc_jb_j$ proves (P12).
Even $T$ permits the ordinary integer expression on its right.

Also $i^{\sum c_j}=(-1)^{(T/2-1)\sum p_j}$. Hence the integer-image
part of the normalized full trace is exactly $J_0(2\epsilon)^K Z_K$,
where
$$
 Z_K=\sum_{p\in\mathbb Z^K}
 (-1)^{(T/2-1)\sum_jp_j}
 e^{2\pi i\theta\sum_j(p_jp_{j+1}-Tp_j^2/2)}
 \prod_j\frac{J_{p_{j-1}-Tp_j+p_{j+1}}(2\epsilon)}
               {J_0(2\epsilon)},\quad \theta=\gamma a^2/N.
                                                               \tag{P13}
$$
The expression defines an absolutely convergent sum for the complex
$\epsilon$ considered below and real $\theta$. Analyticity in a complex
$\theta$ is not asserted: the quadratic phase becomes a growing weight.

## 4. A convergent gas of intervals

Put $\delta=|\epsilon|\le1/10$, $z_0=2\delta$ and
$v_0=2z_0^d/(1-z_0^d)\le1/12$. The Bessel series gives
$$
 |J_0(2\epsilon)|\ge1-\delta^2e^{\delta^2}>0,\quad
 |J_0(2\epsilon)|\le e^{\delta^2},\quad
 \left|\frac{J_j(2\epsilon)}{J_0(2\epsilon)}\right|
 \le z_0^{|j|}.                                             \tag{P14}
$$
For $j\ne0$ use $|J_j|\le e^{\delta^2}\delta^{|j|}/|j|!$
and $e^{\delta^2}/|J_0|<2$; for $j=0$ the ratio is one.

For a finite nonzero string $p_1,\ldots,p_l$, extended by zero,
with nonzero endpoints,
$$
 \|Lp\|_1\ge d\|p\|_1+2(|p_1|+|p_l|)\ge d\|p\|_1+4.         \tag{P15}
$$
Sum $|(Lp)_j|\ge T|p_j|-|p_{j-1}|-|p_{j+1}|$
over the hull, and then add the two exterior contributions
$|p_1|,|p_l|$. This proves (P15), including $l=1$.

Define $w_{l+2}$ as the sum of the weight in (P13) over all these
strings with **no two consecutive zeros inside the hull**. Include the
Bessel factors at the two exterior zero sites. These are the weights
of intervals of length $l+2$. Different support components whose nearest
nonzero sites are at distance at least three have disjoint influence
intervals, so their weights multiply.

Each permitted string has at least $\lfloor l/2\rfloor+1$ nonzero
entries. Summing their possible values by (P15) yields
$$
 |w_{l+2}|\le z_0^4\,2^l
                    v_0^{\lfloor l/2\rfloor+1}.             \tag{P16}
$$
Thus $W(z)=\sum_{j\ge3}w_jz^j$ is analytic on $|z|<3/2$ and
continuous on the closed disk, uniformly in the stated parameters.
At $r=3/2$,
$$
 \sum_{j\ge3}|w_j|r^j
 \le z_0^4r^2\,\frac{2v_0r+4v_0^2r^2}{1-4v_0r^2}
 \le\frac9{2000}=:M.                                       \tag{P17}
$$
The last bound is attained by the majorant at $T=4,\delta=1/10$.
As a function of $\delta$, this majorant has nonnegative coefficients
and starts at order at least six. Its value is therefore at most
$M(10\delta)^6\le(9/20)\delta^2$.

Let $\mathcal Z_K$ be the partition sum of cyclic tilings by one-site
empty tiles of weight one and intervals of length $j\ge3$ of weight
$w_j$. A cyclic integer string with at least two consecutive zeros has
a unique such tiling: group nonzero entries joined by gaps of at most
two, then attach one exterior zero at either end of each group.
The all-zero configuration is the all-empty tiling.

Strings with no consecutive zeros constitute the remainder. By (P9)
their absolute weight is bounded by the binary cyclic partition function
with nonzero-site weight $v_0$ and forbidden adjacent zeros. Its transfer
matrix is $\left(\begin{smallmatrix}v_0&1\\v_0&0\end{smallmatrix}\right)$.
Both eigenvalues have absolute value at most $2\sqrt{v_0}$, so
$$
 |Z_K-\mathcal Z_K|\le2(2\sqrt{v_0})^K.                       \tag{P18}
$$

Counting cyclic sequences of tiles gives the formal, and then analytic,
identity
$$
 \sum_{K\ge1}\mathcal Z_K z^K
   =-z\frac{d}{dz}\log(1-z-W(z)).                            \tag{P19}
$$
Indeed $-\log(1-z-W)=\sum_{q\ge1}(z+W)^q/q$ counts sequences of
$q$ tiles; multiplication of its degree-$K$ coefficient by $K$
marks the label origin on the circle. This gives each labeled tiling
once, including tilings with a rotational stabilizer: count pairs of a
tiling and a tile boundary before dividing by $q$.

On $|z|=3/2$, (P17) is smaller than $|1-z|\ge1/2$.
Rouche's theorem shows that $G(z)=1-z-W(z)$ has exactly one zero
$\zeta$ in the disk, counted with multiplicity. It is simple, satisfies
$|\zeta-1|\le M$, and depends analytically on $\epsilon$.
Define
$$
 \Lambda_T(\epsilon,\theta)=J_0(2\epsilon)/\zeta,\qquad
                   1-\zeta-W(\zeta)=0.                     \tag{P20}
$$
Subtract the pole $z/(\zeta-z)$ from the right side of (P19).
The remainder is analytic inside $3/2$. On $|z|=4/3$, Cauchy's
bound $|W'|\le6M$ gives its absolute value at most
$$
 \frac{(4/3)(2+6M)}{1/3-M}<9.
$$
Coefficient extraction and (P18) yield
$$
 |Z_K-\zeta^{-K}|\le9(3/4)^K+2(1/\sqrt3)^K.                 \tag{P21}
$$
This establishes the claimed dominant term without discarding winding
configurations or exchanging an uncontrolled infinite-volume limit.

## 5. The other central cosets and the odd projection

Equations (P11) and (P14) bound all noninteger cosets by
$$
 \frac{|J_0(2\epsilon)|^K}{1-(1/5)^K}(5/12)^K.               \tag{P22}
$$
For a centered Weyl operator, the normalized odd projected trace is
$(N\mathbf1_{\{x=0\}}-1)/(N-1)$. The Fourier--Bessel series has total
absolute mass at most $e^{2K\delta}$, so replacement by the central
indicator costs at most $e^{2K\delta}/(N-1)$.

From (P1), $N\ge\lambda^{(K-1)/2}$ and $N\ge5$. Using
$\lambda\ge2+\sqrt3$ bounds this last error by
$$
 \frac54\sqrt{2+\sqrt3}
       \left(\frac{e^{1/5}}{\sqrt{2+\sqrt3}}\right)^K.
                                                               \tag{P23}
$$
Each base in (P21)--(P23), after the factor $e^{K/100}$ where
needed, is less than $4/5$. The sum of the displayed constants is
less than $20$. This proves (P4), including a uniform error constant.

For real $\epsilon$, alternating Bessel series imply
$1-\delta^2\le J_0(2\epsilon)\le e^{-\delta^2}$ in this interval.
Also $|\zeta-1|\le(9/20)\delta^2$ and $|\zeta-1|\le M$.
Consequently
$$
 -\frac{\delta^2}{1-\delta^2}-\frac9{20}\delta^2
 \le\log|\Lambda_T|
 \le-\delta^2+\frac{(9/20)\delta^2}{1-M}.
$$
These inequalities imply (P5).

## 6. The first local resonance and a further scale

The one-site interval is exactly
$$
 w_3=\frac{2}{J_0(2\epsilon)^3}
 \sum_{b\ge1}(-1)^{(T/2-1)b}J_b(2\epsilon)^2J_{Tb}(2\epsilon)
                   e^{-\pi iT\theta b^2}.                  \tag{P24}
$$
Its leading term has degree $T+2$ and is the term in (P6).
Every interval with at least two nonzero entries has degree at least
$2d+4=2T$, by (P15). For $T\ge4$, $2T\ge T+4$.
The root equation gives $\log(1/\zeta)=w_3+O_T(\epsilon^{T+4})$.
All infinite series involved converge normally by (P16); hence these
degree arguments apply to their analytic sums. This proves (P6).

For $T=6$, the next coefficient in the one-site contribution is
$13\epsilon^{10}e^{-24\pi i\vartheta}/2520$, in agreement with
direct rational Bessel-series multiplication.

There is a resonance scale after division by the independent-site factor.
For fixed $T$, if $\epsilon_K\to0$, $K\epsilon_K^{T+2}\to\eta$ and
$\gamma a_K^2/N\to\theta$ modulo one, then
$$
 \frac{\operatorname{tr}_-U^K}{J_0(2\epsilon_K)^K}
 \longrightarrow
 \exp\!\left(\frac{2(-1)^{T/2-1}}{T!}
                   e^{-\pi iT\theta}\eta\right).             \tag{P25}
$$
Indeed $K\epsilon_K^{T+4}\to0$, and the exponentially small error
in (P4) remains negligible after the division. This is a statement about
a rescaled trace; it is not a new microscopic spectral limit.

## 7. What happens at the next return

For $m\ge2$, expansion over $mK$ sites still has the two central
congruences modulo $N$, but its recurrence determinant is now
$\lambda^{mK}+\lambda^{-mK}-2$. Its central quotient therefore has
order
$$
 \frac{\lambda^{mK}+\lambda^{-mK}-2}{N^2}.                    \tag{P26}
$$
This grows exponentially in $K$ for fixed $m\ge2$. More decisively,
$c=e_j-e_{j+K}$ is central and has norm two. It cannot lie in the
integer image of the length-$mK$ recurrence matrix. For $d>2$
this follows immediately from (P9); for $d=2$, an integer preimage
would have norm at most one, and the image of a signed coordinate
vector has norm $T+2=6$, not two.

Thus noninteger cosets at repeated returns contain contributions of
order $\epsilon^2$. The exponentially small coset estimate used at one
period has no analogue obtained merely by replacing $K$ with $mK$.
These are the inter-period pairings that the growing-return work handles
in a vanishing-kick regime. Neither (P4) nor classical mixing controls
their summed Weyl phases at Heisenberg times.

No theorem here covers a fixed nonzero classical perturbation: in the
usual semiclassical scaling a fixed quantum $\epsilon$ corresponds to
a classical kick of order $1/N$ (for a fixed harmonic). No claim is made
that the original BGS problem is closed.

## 8. Relation to earlier literature

The Fourier--Bessel expansion, cyclic recurrence determinant, interval-gas
counting and analytic root argument are established mathematical methods;
their use here is proved explicitly rather than claimed as new technology.
The bounded literature search has not established priority for (P4).

Keppeler, Marklof and Mezzadri, *Quantum cat maps with spin 1/2*,
[arXiv:nlin/0012012](https://arxiv.org/pdf/nlin/0012012), derive a
semiclassical trace formula and compare a diagonal form-factor approximation
with CSE. Their spin coupling and observable are different from (P2).
That paper does not supply a microscopic universality theorem for this
scalar family.

Axenides, Floratos and Nicolis, *Arnol'd cat map lattices*,
[arXiv:2208.03267](https://arxiv.org/abs/2208.03267), concern coupled
classical cat maps. Only its abstract was inspected in this search;
no priority conclusion about the present trace pressure follows from it.
