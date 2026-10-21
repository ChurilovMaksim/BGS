> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/adversarial_endpoint_symbols_and_renewal.md`. Embedded SHA256: `561efce86a8aa2cab0c49fa05236e64f420ce26919ae0342dee2566e552ec32a`.
> [Thematic guide](../../topics/dephasing.md).

# Uniform endpoint symbols and exact marker renewal for the actual family

Research continuation, 20 October 2026. These are direct lemmas for the
signed three-cell calculation. They address the possibility that long
windings or cell lengths might destroy the symbol bounds needed for
the transfer argument.

## 1. Inputs

| Input | SHA-256 |
|---|---|
| ../research_continuation_2026_10_20/exact_amplitude.md | 69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e |
| fermionic_coherent_pair_mass.md | dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816 |
| fermionic_quantitative_pressure.md | d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2 |

The exact phase is
$$
F(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8}+G(Q,q).
$$
The exact-amplitude proof gives $G$ holomorphic on a strip over
the entire real plane. On the strip of width $0.002$, its
second partial derivatives at the actual parameter have modulus
less than $10^{-70}$, by the reserved-strip Cauchy bounds.
In particular they are less than $1/100$.

The coherent-pair proof supplies the exact cell boundary function
$W_e$, the odd-dimensional deck normalization, and
$$
|DW_e(q_*,q_*)-p_*(1,-1)|\leq C\Lambda^{-R}
\tag{1.1}
$$
for cells with $R$ zero edges at each end. Coordinates here are
ordered as output, input. The actual $\Lambda>5$ is fixed.

The positive future transfer operator has
$$
\mathcal T^n=\Pi+O((9/10)^n),\qquad
\Pi=\mathfrak h\nu,\quad
\nu(\mathfrak h)=\nu(1)=1.
\tag{1.2}
$$
For the zero-loop prefix $J$,
$$
J^k=\Lambda^{-k}(g\delta_o+O(\theta^k)),\quad
\theta=2/3,\quad g(o)=1,
\tag{1.3}
$$
in the fixed Holder operator norm. These facts were independently
checked in the companion coherent-pair audit.

## 2. Endpoint derivatives do not grow with length or winding

**Lemma 2.1.** For every fixed derivative order $r\geq2$,
there is a constant $C_r$ such that every real boundary function
$W_e$ of every cell, with arbitrary length and deck winding,
satisfies
$$
\|D^rW_e\|\leq C_r.
\tag{2.1}
$$
It has holomorphic dependence on the two endpoint positions on
a common neighborhood of every real endpoint pair. After its
constant and linear jets are removed, its holomorphic bound
on that neighborhood is independent of length and winding.

**Proof.** For a fixed pair of real endpoints take the unique
real critical internal path $q^*$. Let its endpoint variations
be $\delta=(\delta_0,\delta_d)$, and write the variations of
the $d-1$ internal positions as $y$.

The internal Hessian of the unperturbed action is
$$
H_0=-\frac32 I+\frac14(R+R^T).
$$
Here $R$ is the one-sided path shift, with missing boundary
entries simply absent. Its inverse has both induced
$\ell^1$ and $\ell^\infty$ norms at most $1$. Indeed,
factor out $-3/2$ and sum the Neumann series; the norm
of $(R+R^T)/6$ is at most $1/3$.

The variation equation is
$$
H_0y+B_0\delta+\mathcal R(y,\delta)=0.
\tag{2.2}
$$
The boundary forcing $B_0\delta$ occurs only at the first
and last internal sites, with coefficient $1/4$.
Thus
$$
\|B_0\delta\|_\infty\leq\frac12\|\delta\|_\infty,\qquad
\|B_0\delta\|_1\leq\frac14(|\delta_0|+|\delta_d|).
$$
The first inequality includes a one-site internal path, where
both endpoints force the same site.

The remainder is the change in the internal gradient of
$\sum G(q_{j+1},q_j)$. At each site it has only three
neighboring arguments. Its derivative has row and column
sums at most $4\epsilon$, where
$\epsilon=10^{-70}$. Its part forced by the endpoints has
$\ell^1$ norm at most
$\epsilon(|\delta_0|+|\delta_d|)$.

Choose a fixed small endpoint polydisc, for example
$\|\delta\|_\infty<10^{-4}$. The fixed-point map obtained
from (2.2) preserves $\|y\|_\infty\leq\|\delta\|_\infty$
and has contraction constant at most $4\epsilon<1$.
All complex paths stay in the reserved strip, irrespective
of the real size of $q^*$. The holomorphic iterates converge
uniformly on smaller endpoint polydiscs. This proves uniform
holomorphic dependence.

The same equation in $\ell^1$ gives
$$
\|y\|_1
\leq \frac{1/4+\epsilon}{1-4\epsilon}
       (|\delta_0|+|\delta_d|).
\tag{2.3}
$$
This bound is independent of the number of internal positions.
Cauchy's formula therefore bounds every fixed endpoint
derivative of $y$, including its $\ell^1$ norm, independently
of that number.

The envelope identities are
$$
\partial_{\rm out}W_e
=F_Q(q_d,q_{d-1})-(n_e)_p,\qquad
\partial_{\rm in}W_e=F_q(q_1,q_0).
$$
Their changes from the real base endpoint pair are bounded
by $C\|\delta\|_\infty$, using (2.3) or its
$\ell^\infty$ counterpart and the bounded second
derivatives of $F$. The constant deck momentum disappears
on taking a difference. Integrating along the endpoint segment
proves
$$
|W_e(q+\delta)-W_e(q)-DW_e(q)\delta|
\leq C\|\delta\|_\infty^2
\tag{2.4}
$$
throughout the common complex polydisc. Cauchy's formula
applied to (2.4) proves (2.1). A one-edge cell is the same
statement directly for $F$ plus a linear deck term. $\square$

The very large value of $W_e(q_*,q_*)$ for a large winding
can never be bounded uniformly by this argument. That value,
however, is the identical sum of cell constants for two
permutations and cancels exactly before estimating the
phase difference. Removing it first is essential.

## 3. Uniform quadratic reduction at the encounter scale

Define the rescaled centered branch
$$
\mathcal W_{e,R}(x_{\rm out},x_{\rm in})
=\Lambda^{2R}\left[
 W_e(q_*+\Lambda^{-R}x_{\rm out},
     q_*+\Lambda^{-R}x_{\rm in})
 -W_e(q_*,q_*)
 -p_*\Lambda^{-R}(x_{\rm out}-x_{\rm in})
 \right].
\tag{3.1}
$$
On every fixed bounded complex polydisc in $x$, this has
a uniform bound, independently of the cell length and winding,
for all large $R$. This follows from (1.1) and (2.4).
Moreover
$$
\|D^r\mathcal W_{e,R}\|\leq C_r\Lambda^{(2-r)R}
\quad(r\geq2).
$$
Its first derivative is uniformly bounded by (1.1).
In particular its third derivative is $O(\Lambda^{-R})$.

For a fixed number of cyclic cells, the rescaled cut action
is strongly concave with a fixed Hessian bound. Its gradient
at zero is uniformly bounded, so its maximizer belongs to
a fixed real ball. Taylor's theorem on that ball shows that
the exact maximum differs from the maximum of its quadratic
Taylor polynomial by $O(\Lambda^{-R})$, uniformly over
all interior words.

Returning to unscaled actions, this is an error
$O(\Lambda^{-3R})$. For
$$
R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+O(1)
$$
the quantum phase error is
$$
O(N\Lambda^{-3R})=O(N^{-1/2}).
\tag{3.2}
$$
Thus the full phase comparison reduces uniformly to finitely
many bounded endpoint gradients and Hessians. Winding does
not cause exponentially large endpoint-symbol norms.

This lemma by itself does not identify the limiting
distribution of those endpoint jets. That identification
requires the actual homoclinic endpoint coordinates and
their prefix/suffix laws. The next sections verify the
renewal and measure-normalization components of that step.

## 4. An exact noncommuting renewal identity

Put $B=\mathcal T-J$, and let $\mathcal G_{k,\ell}$
be the sum of prefix operators for all words of length
$\ell$ containing no run $0^k$. Define
$$
A_k(z)=\sum_{j=0}^{k-1}(zJ)^j.
$$
The decomposition into short zero runs separated by
nonzero edges gives the formal operator series
$$
\mathcal G_k(z):=\sum_{\ell\geq0}z^\ell\mathcal G_{k,\ell}
=A_k(z)(I-zBA_k(z))^{-1}.
\tag{4.1}
$$
The order matters: with the prefix convention, the
rightmost operator supplies the earliest chronological edge.
The displayed language decomposition uses exactly that order.

Since $A_k$ commutes with $J$,
$$
(I-zBA_k)(I-zJ)
=I-z\mathcal T+z^{k+1}BJ^k.
$$
Consequently the exact identity is
$$
\boxed{\mathcal G_k(z)
=(I-z^kJ^k)
 (I-z\mathcal T+z^{k+1}BJ^k)^{-1}.}
\tag{4.2}
$$
No commutation between $B$ and $J$ is presumed.
For example, at $k=2$ its second-order coefficient is
$B^2+BJ+JB$, as required.

## 5. The rare-marker pole with a uniform error

Write $\epsilon_k=\Lambda^{-k}$ and $P_0=g\delta_o$.
By (1.3), $J^k=\epsilon_k(P_0+O(\theta^k))$.
The fixed subspace of $\mathcal T$ is
$\Pi=\mathfrak h\nu$; let $Q=I-\Pi$.
On $|z|\leq1.05$, the inverse of
$I-zQ\mathcal TQ$ is uniformly bounded, since the
complementary powers are $O((9/10)^n)$.

The perturbation $z^{k+1}BJ^k$ is bounded throughout
this disc by $C(1.05/\Lambda)^k$. Thus the complementary
block remains invertible for all large $k$. Its exact
rank-one Schur complement is a scalar analytic function.
Near $z=1$ it is
$$
f_k(z)=1-z+\kappa\epsilon_k z^{k+1}
 +O(\epsilon_k\theta^k+\epsilon_k^2),
\tag{5.1}
$$
uniformly on $|z-1|\leq C\epsilon_k$, where
$$
\kappa=\nu(Bg)\,\mathfrak h(o).
$$
The cross-block Schur term is $O(\epsilon_k^2)$.
On the full fixed disc the analogous error estimates
include the harmless powers $|z|^{k+1}$.

Rouche's theorem on a sufficiently large fixed multiple
of the $\epsilon_k$-circle about $1$ gives its
unique nearby zero. The same theorem on $|z|=1.05$,
where $|1-z|\geq0.05$, shows that there are no
additional zeros inside that disc. Expanding (5.1) gives
$$
z_k=1+\kappa\epsilon_k
 +O(k\epsilon_k^2+\epsilon_k\theta^k).
\tag{5.2}
$$
The pole is simple because $f'_k(z_k)=-1+O(k\epsilon_k)$.
It is real by conjugation and uniqueness.

The normalized power limit also gives $Jg=\Lambda^{-1}g$.
Using $\nu\mathcal T=\nu$,
$$
\nu(Bg)=(1-\Lambda^{-1})\nu(g)>0.
$$
Therefore $\kappa>0$ and $z_k>1$ eventually.

The singular part of (4.2), written as
$R_k/(1-z/z_k)$, has
$$
R_k=\Pi+O(k\epsilon_k).
$$
After this pole is removed, the operator function is
analytic and uniformly bounded on the circle $|z|=1.05$.
Cauchy's formula therefore proves
$$
\mathcal G_{k,\ell}=z_k^{-\ell}R_k+O(1.05^{-\ell}).
\tag{5.3}
$$
If $\ell\asymp N$ and $N\epsilon_k$ is bounded, (5.2)
implies the useful uniform form
$$
\boxed{\mathcal G_{k,\ell}
=e^{-\kappa\ell\epsilon_k}\Pi
 +O(k\epsilon_k+\theta^k)+O(1.05^{-\ell}).}
\tag{5.4}
$$
This is the needed renewal estimate for $k=2R$, with
no averaging in $N$.

## 6. Consistent endpoint laws and factorization

Let $A=J_a$, and write $J_w$ for the chronological
word operator, with reversed prefix-operator order.
The proposed distributions of finite endpoint words are
$$
P_K(w)=\frac{\nu(J_wAg)}{\nu(Ag)},\qquad
Q_K(v)=\frac{(AJ_v\mathfrak h)(o)}
                {(A\mathfrak h)(o)}.
\tag{6.1}
$$
All entries are nonnegative and both denominators are positive.
Summing length-$K$ words uses
$\nu\mathcal T^K=\nu$ and
$\mathcal T^K\mathfrak h=\mathfrak h$, so each family
has total mass one.

For a prefix word $w$, appending an edge $e$ gives
$J_{we}=J_eJ_w$. Summing over $e$ in the numerator
of $P_{K+1}$ gives $\nu\mathcal T J_wAg=\nu J_wAg$.
For a suffix $v$, prepending $e$ gives
$J_{ev}=J_vJ_e$. Summing in $Q_{K+1}$ uses
$\mathcal T\mathfrak h=\mathfrak h$.
Thus the prefix and suffix cylinder distributions are
consistent and define probability measures on the
respective compact one-sided spaces.

For fixed endpoint words $w,v$ of length $K$ and
a long middle, the relevant cell expression is
$$
(AJ_v\mathcal G_{k,\ell-2K}J_wAg)(o).
$$
Equation (5.4) factors it into
$$
e^{-\kappa\ell\epsilon_k}
 \nu(J_wAg)(AJ_v\mathfrak h)(o)+o_K(1),
\tag{6.2}
$$
uniformly for $\ell\asymp N$. Replacing
$\ell-2K$ by $\ell$ changes the exponential by
$1+O_K(\epsilon_k)$.

There is a small combinatorial qualification: avoiding
$0^k$ only inside the middle does not automatically
exclude a run crossing a cut. For fixed $K$ and
eventually $k>K$, there are at most $2K$ possible
crossing runs, counted by a start in the prefix or an
end in the suffix. Positive insertion of $J^k$
bounds their scalar weight by $O_K(\epsilon_k)$.
Thus (6.2) also holds for genuine avoidance in the
entire interior.

For the physical inverse map, the coded prefix gives
the stable output endpoint and the coded suffix the
unstable input endpoint. Equation (6.2) proves
independence of their limiting laws, with cell
normalization $\nu(Ag)(A\mathfrak h)(o)$.
For three cells its cube is exactly the constant $c_*$
in the coherent-pair count.

For a bounded equicontinuous family of kernels of
these endpoint variables, first approximate the endpoint
functions uniformly by fixed finite-cylinder functions.
Then apply (6.2) for that fixed $K$, and finally let
$K$ grow. This order is sufficient for a uniform
bounded-frequency limit. It avoids introducing an
exponentially large Holder norm by composing an
endpoint observable with an entire length-$\ell$ shift.

These lemmas remove the proposed endpoint-norm and
marker-renewal gaps. The actual quadratic endpoint
coordinates must still be inserted into the signed
phase before a complete signed-family theorem is stated.
