> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_coherent_pair_mass_audit.md`. Embedded SHA256: `278d5022b06cd1b28e2a2ec4ce2dde0666ca80b1bbefe443417ef30f836ed30b`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: a positive off-diagonal subsum at the pair-statistic scale

Research continuation, 20 October 2026. This audit concerns the exact
original map and the exact quantum weights at the fixed parameter
$\tau=10^{-80}$.

## 1. Frozen inputs and verdict

| Input | SHA-256 |
|---|---|
| fermionic_coherent_pair_mass.md | dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816 |
| fermionic_homoclinic_and_doubled_transfer.md | 85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168 |
| fermionic_quantitative_pressure.md | d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2 |

**Verdict: PASS.** For every sufficiently large odd $N$ and every
integer $m\in[N,3N/2]$, the construction selects distinct primitive
geometric orbit pairs whose two ordered cross directions have total
weight $E_{m,N}$ satisfying
$$
cN\leq E_{m,N}\leq CN.
\tag{1.1}
$$
The constants and the dimension threshold are fixed for the original
map. The exact scalar amplitude and odd-dimensional deck phase are
retained.

The three critical issues were checked independently: quadratic
stationary action error with no cell-length factor; uniform weighted
marker counts for the nonlinear unstable Jacobian; and the exact
conversion from canonical words to geometric orbits, without a
missing factor of $m$.

This is a theorem about a selected positive subsum. The omitted
off-diagonal terms can be negative. No lower bound for their sum
with $E_{m,N}$, and no proof or refutation of $H_{\rm diag}$,
follows from (1.1).

## 2. Exact multiplier rate on both homoclinic tails

Let $0$ be the fixed loop coding the interior nonzero fixed
point, and let $\Lambda>5$ be its actual unstable multiplier
for the physical inverse map. For every finite excursion
$a u a$, the coding bound first places its two homoclinic
tails within $C\lambda^{-j/2}$ of that fixed point.
The constant and entry time are independent of the word $u$
and its length.

Near the fixed point, in real eigen coordinates, write
$$
F_*(x)=Dx+R(x),\qquad
D=\operatorname{diag}(\Lambda,\Lambda^{-1}),\quad
R(0)=DR(0)=0.
$$
For a backward orbit $F_*(x_n)=x_{n-1}$, the formulas
$$
u_n=\Lambda^{-n}u_0-
 \sum_{j=1}^n\Lambda^{-(n-j+1)}R_u(x_j),\qquad
v_n=\sum_{j\geq1}\Lambda^{-(j-1)}R_v(x_{n+j})
$$
are obtained directly by iteration and convergence at infinity.
On sequences with norm $\sup_n2^n|x_n|$, their convolution
norms are bounded by $1/(\Lambda-2)$ and
$1/(2-\Lambda^{-1})$. On a fixed sufficiently small ball
they give a contraction. Differentiating this contraction twice
is legitimate: multiplication of two tangent sequences has
an additional decaying factor $2^{-n}$, so the second
differentiated Nemytskii term remains in the same Banach space.

The resulting unstable curve is $v=b(u)=O(u^2)$. The
previous homoclinic tails belong to this graph by uniqueness,
since $2<\sqrt\lambda$. Its backward scalar map satisfies
$$
u_{n+1}=\Lambda^{-1}u_n+O(u_n^2),\qquad
|u_{n+1}|\leq|u_n|/2
$$
after shrinking the fixed neighborhood. Multiplying the
relative factors and summing the geometric bound on
$|u_n|$ proves
$$
|u_n|\leq C\Lambda^{-n}|u_0|.
$$
The inverse construction gives the stable tail. Absorbing
the common entry time proves endpoint bounds $C\Lambda^{-R}$
for every cell $0^R a u a0^R$. Using the exact $\Lambda$
instead of a weakened fixed rate is necessary for the eventual
power of $N$, and the proof does supply this exact rate.

## 3. Global boundary actions and their deck normalization

The physical map traverses each forward-coded cell backwards.
Its input and output charts are therefore the right and left
coded endpoint charts, respectively. The total physical
deck label $n_e$ is fixed by the finite list of inverse
edge labels and their lengths. It is identical for the
homoclinic realization and any periodic concatenation.
Reversing the physical cyclic order still permutes the same
three branch functions.

For a cell of length $d$, define
$$
W_e(q_{\rm out},q_{\rm in})
=\operatorname*{crit}_{q_1,\ldots,q_{d-1}}
\sum_{j=0}^{d-1}F(q_{j+1},q_j)
 -(n_e)_p q_{\rm out},
$$
with $q_0=q_{\rm in}$ and
$q_d=q_{\rm out}+(n_e)_q$.

For the full open-chain quadratic form, the endpoint diagonal
of its negative Hessian is $3/4$, the internal diagonal is
$3/2$, and off-diagonal neighbors have magnitude $1/4$.
The uniformly tiny perturbation has bounded row sums,
independently of $d$. Thus the full negative Hessian lies
between $0.49I$ and $2.01I$. Bounded $G$ gives coercivity
toward minus infinity in the internal positions, so their
critical point is unique for every pair of real endpoints.

The negative Hessian of the reduced boundary function is a
Schur complement. Its inverse is the corresponding principal
block of the inverse full Hessian. Therefore it obeys the
same bounds:
$$
0.49I\leq-D^2W_e\leq2.01I.
\tag{3.1}
$$
This comparison is uniform in both the cell length and its
possibly large winding. The linear deck correction does
not affect a Hessian.

The endpoint derivative identities are
$$
\partial_{q_{\rm out}}W_e=p_{\rm out},\qquad
-\partial_{q_{\rm in}}W_e=p_{\rm in},
$$
where the output momentum is reduced by $(n_e)_p$.
These signs follow by differentiating the original critical
action; the internal derivatives vanish by stationarity.

The exact odd-dimensional Landau gauge identifies the branch
phase with $\exp(iW_e/h)$. Resetting lifts at intermediate
cuts produces precisely the local output factor
$\exp(-i(n_e)_p q_{\rm out}/h)$. Equivariance of the
prequantum lift proves that successive resets are the same
as one final reset. In particular a large winding cannot
produce an extra order-dependent constant: the possible
integer deck constants have exponential $1$ because
$L\equiv I\pmod2$ and $N$ is an integer. The original
half-winding phase is already exactly canceled for odd $N$.

## 4. Why stationary permutation error is quadratic

On the homoclinic realization, both endpoint states of each
cell are $O(\Lambda^{-R})$ from $(q_*,p_*)$.
By (3.1), evaluating derivatives instead at
$(q_*,q_*)$ changes them by only $O(\Lambda^{-R})$.
Hence the two endpoint derivatives are
$p_*+O(\Lambda^{-R})$ and
$-p_*+O(\Lambda^{-R})$.

For $n$ cyclic cells, let $\mathcal S$ be the sum of
their boundary functions. Each cut belongs to two endpoint
pairs, so
$$
-D^2\mathcal S\geq0.98I.
$$
At the constant cut vector, the $p_*$ terms cancel in
each component of the gradient, giving
$$
|D\mathcal S(q_*,\ldots,q_*)|^2
 \leq Cn\Lambda^{-2R}.
$$
For any globally $c$-strongly concave function,
$$
0\leq\max\mathcal S-\mathcal S(x_0)
\leq |D\mathcal S(x_0)|^2/(2c).
\tag{4.1}
$$
This follows by maximizing its global quadratic tangent
upper bound.

The known periodic orbit of the concatenated code is first
taken as an existing object. Its zero buffers put its cuts
in the common endpoint chart, and the fixed inverse labels
give the same branches $n_e$. Its internal path and its
cut momenta solve the displayed critical equations.
Uniqueness then identifies it with the maximizer in (4.1).
This ordering avoids assuming that an arbitrary variational
critical point has a prescribed itinerary.

At the constant cut vector the value is
$\sum_e W_e(q_*,q_*)$, unchanged by permutation.
Consequently the two exact orbit actions differ by
$$
|\mathcal S_w-\mathcal S_{w'}|
 \leq Cn\Lambda^{-2R}.
\tag{4.2}
$$
There is no factor proportional to an interior word length.
The improvement from a first-order distance error to
(4.2) is the essential quantitative step.

## 5. Localized scalar amplitude and phase alignment

If the position inside a matched cell of length $d$ has
offset $j$, the two full codes agree at least to radius
$$
R+\min(j,d-1-j)
$$
up to a fixed indexing adjustment. The additional $R$
comes from the zero buffer of the adjacent cell. The
uniform coded variation of $\log\gamma_h$ therefore sums
over this cell to at most
$$
C\theta^R
\sum_{j=0}^{d-1}\theta^{\min(j,d-1-j)}
\leq \frac{2C}{1-\theta}\theta^R,\quad \theta=2/3.
$$
For three cells the scalar logarithm ratio is $O(\theta^R)$,
independently of all their lengths.

Take
$$
R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0.
$$
By (4.2), multiplying the action discrepancy by $h^{-1}=2\pi N$
gives a bounded phase error that can be made smaller than
$1/20$ by choosing the single fixed integer $R_0$.
The scalar discrepancy tends to zero. The complete
one-point weights thus have ratio within $1/4$ of $1$
eventually, uniformly over the counted words.

The actual all-time modulus comparison, for $m\leq2N$,
is
$$
|a_{p,N}|^2=(1+O(N^{-1}))\Lambda_p^{-1}.
$$
It follows that the two ordered cross directions are
positive and bounded above and below by fixed multiples
of $m^2\Lambda_p^{-1}$, as claimed.

## 6. The positive transfer normalization

The one-sided transfer operator for the actual potential
has
$$
\mathcal T^n=\mathfrak h\nu+O((9/10)^n),\qquad
\nu(\mathfrak h)=\nu(1)=1,
$$
with $\mathfrak h>0$ and positive $\nu$.
For a periodic word its branch weight equals
the actual unstable multiplier inverse.
At the zero fixed word $o$,
$$
\lambda^{-1}e^{v(o)}=\Lambda^{-1}.
$$

For the zero prefix $J$,
$$
\Lambda^kJ^k f(x)
=\exp\!\left(\sum_{j=1}^k[v(0^jx)-v(o)]\right)
 f(0^kx)
$$
on its vertex cylinder. Prefixing $j$ equal edges
contracts the Holder norm of the potential difference
by $\theta^j$. The exponential consequently converges
in that norm to $g$, with $g(o)=1$, and
$$
\|\Lambda^kJ^k-g\delta_o\|\leq C\theta^k.
\tag{6.1}
$$
All normalized zero-prefix powers are uniformly bounded.
Outside the vertex cylinder the functions vanish, which
is harmless because vertex cylinders are clopen.

Let $A$ prefix the nonzero loop $a$. For fixed
interior lengths $\ell_1,\ell_2,\ell_3$, the sum of
open weights is exactly the prefix product in the input.
The rightmost factor supplies the earliest edge; checking
two prefix operations gives this order directly.
Its total zero length is $6R$.

The periodic continuation and the open zero continuation
of a word agree through $m+R$ edges. Their potential
sums therefore differ by at most $C\theta^R$, so open
and periodic weights differ by a factor
$\exp(O(\theta^R))$, uniformly in the interiors.

Replacing the three long unrestricted factors by
$\mathfrak h\nu$, and the normalized zero factors
by (6.1), gives the leading constant
$$
c_*=[\nu(Ag)\,(A\mathfrak h)(o)]^3>0.
$$
Every replacement has a uniformly bounded neighboring
product. For $\min\ell_j\geq\varepsilon m$, the
periodic weight sum is therefore
$$
\Lambda^{-6R}
\{c_*+O(\theta^R+(9/10)^{\varepsilon m})\}.
\tag{6.2}
$$
All factors are those of the actual nonlinear potential.
No replacement of its Jacobian by $\lambda^m$ is made.

## 7. Extra markers and exact orbit counting

A bad additional run of $2R$ zeros must lie wholly
inside an interior word, since the displayed runs are
flanked by $a$. At a specified starting position,
inserting the additional zero-prefix factor gives a
uniform weight bound $C\Lambda^{-8R}$, even when
the remaining unrestricted lengths are short.
There are at most $m$ starts, so positivity and the
union bound give
$$
Z_{\rm bad}\leq Cm\Lambda^{-8R}.
$$
Increasing the same fixed $R_0$ makes this a fixed
small fraction of (6.2), uniformly for $m\leq3N/2$.
Thus every admissible long length triple retains
weight comparable to $\Lambda^{-6R}$.

The length bands in the input give order $m^2$
triples. The three lengths are distinct and all at
least $m/9$ eventually. Each good cyclic word has
exactly three maximal marked zero runs. A proper
repetition number must divide three; a repetition
number three would force their consecutive gap lengths
equal. The distinct bands exclude this. The coding
fiber argument then proves primitive geometric period.

For each first orbit, the unique marker immediately
preceding the short interior determines one cut: the
vertex after exactly $R$ edges of this length-$2R$
run. This reconstructs the counted word uniquely.
The cyclic order short--medium--long differs from
short--long--medium, so the partner is a different
orbit and never another first orbit of the construction.
This proves injectivity into unordered geometric
orbit pairs, including across different length triples.

In particular the code weight sum is the geometric
orbit weight sum with no extra factor $m$ or $1/m$:
$$
\sum_{\rm selected}\Lambda_p^{-1}
\asymp m^2\Lambda^{-6R}.
\tag{7.1}
$$
The only $m^2$ from point multiplicity enters later,
because each of two different primitive orbits has
exactly $m$ points and a constant cyclic one-point
weight in the trace formula.

## 8. Final scale and exact limitation

Combining the positive cross-weight comparison with (7.1)
gives
$$
E_{m,N}\asymp m^4\Lambda^{-6R}.
$$
The chosen rounding gives
$$
\Lambda^{-2R_0-2}/N
\leq\Lambda^{-2R}\leq\Lambda^{-2R_0}/N.
$$
For $m\in[N,3N/2]$ this is exactly (1.1).
For the fixed test with $|\widehat b_*|^2$ strictly
positive on $[1,3/2]$, summing order $N$ such
terms and dividing by $N^2$ gives the strictly
positive limit inferior.

The proof establishes actual positive off-diagonal
mass at the desired pair-statistic scale. The remaining
signed orbit pairs have not been bounded. Their
contribution can cancel both this selected class and
the positive excess from the same-geometric-orbit
diagonal above time $N$. The input correctly leaves
that cancellation as the first unproved estimate.
