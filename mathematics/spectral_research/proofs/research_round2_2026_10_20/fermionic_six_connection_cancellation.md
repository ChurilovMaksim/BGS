> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_six_connection_cancellation.md`. Embedded SHA256: `4661fed89558f03c58e085ec70df919b14056ff4ec5e3e765e6564ce35fbb865`.
> [Thematic guide](../../topics/histories.md).

# Six actual reconnections and a negative fermionic contribution

Research continuation, 20 October 2026. This note evaluates all six
connections of the three actual buffered cells used in the signed
three-cell theorem. Connections with one, two, and three periodic
components are included. Their alternating Euler weights produce an
actual negative off-diagonal contribution. Its scale and its scope
are kept separate from those of the original trace pair statistic.

## 1. Inputs and the precise statement

| Input | SHA-256 |
|---|---|
| fermionic_signed_three_cell_profile.md | edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5 |
| fermionic_pseudoorbit_cutoff.md | 03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb |
| root_gram_permutation_identity.md | ca635dab171d81b673aec7136b2123ab9f2b82deac8a8a9b82a436d961520375 |

The first input supplies the actual scattering coordinates, their
probability laws $\sigma,\upsilon$, the positive operator $K_t$,
the exact marker renewal estimate, and their full proof. Its
notation is retained:

$$
 R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0,\quad
 \varepsilon=\Lambda^{-2R},\quad x_N=N\varepsilon,\quad
 t_N=2\pi\chi x_N,\qquad R_0\ge0\text{ fixed}.
 \tag{1.1}
$$

Let $c_*,\kappa_{\rm esc}>0$ be its constants, and write
$p_r(t)=\operatorname{Tr}(K_t^r)$; in particular $p_1=1$.
The three interior lengths have the same disjoint bands

$$
 m/8\le\ell_1\le m/6,\quad m/4\le\ell_2\le m/3,\quad
 \ell_3=m-6R-6-\ell_1-\ell_2.
 \tag{1.2}
$$

Each word $u_j:i\to i$ avoids $2R$ consecutive zero edges.
It defines a cell $e_j=0^R a u_j a0^R$, of length
$d_j=2R+2+\ell_j$. A cluster means one such ordered triple of
labelled cells, with all six physical successor permutations
$\rho\in S_3$. Each cycle of $\rho$ gives an actual periodic
orbit. Their union is denoted $\mathfrak p_\rho$.

Let $a_{p,N}$ be the exact primitive principal-orbit weight.
The signed weight of this finite set of orbits is

$$
 C_\rho=(-1)^{c(\rho)}
                \prod_{p\in\mathfrak p_\rho}a_{p,N},
 \tag{1.3}
$$

where $c(\rho)$ is the number of cycles. For fixed $m,N$,
sum over all clusters, with the unique labels and anchors
specified in Section 2, and define

$$
 \begin{split}
 F_{m,N}&=\sum_{\rm clusters}
                         \left|\sum_{\rho\in S_3}C_\rho\right|^2,\\
 D_{m,N}^{\rm enc}&=\sum_{\rm clusters}
                              \sum_{\rho\in S_3}|C_\rho|^2,\\
 O_{m,N}^{\rm enc}&=
             F_{m,N}-D_{m,N}^{\rm enc}
        =\sum_{\rm clusters}\sum_{\rho\ne\eta}C_\rho\overline{C_\eta}.
 \end{split}
 \tag{1.4}
$$

All these are finite sums of exact weights. In particular the last
quantity is real, and it is an actual selected off-diagonal sum
in the square of the corresponding degree-$m$ principal Euler
coefficient.

Put

$$
 W_{m,N}=\frac{c_*}{288}m^2\varepsilon^3
                              e^{-\kappa_{\rm esc}m\varepsilon}.
 \tag{1.5}
$$

We prove, uniformly for $N\le m\le3N/2$, along all odd $N$,

$$
 \boxed{\begin{aligned}
 F_{m,N}
   &=W_{m,N}\,[6-18p_2(t_N)+12p_3(t_N)]+o(N^{-1})\\
   &=36W_{m,N}\,e_3(K_{t_N})+o(N^{-1}),\\
 D_{m,N}^{\rm enc}&=6W_{m,N}+o(N^{-1}),\\
 O_{m,N}^{\rm enc}
   &=W_{m,N}\,[-18p_2(t_N)+12p_3(t_N)]+o(N^{-1}).
 \end{aligned}}
 \tag{1.6}
$$

Since $0<p_3(t)\le p_2(t)$, the last bracket is at most
$-6p_2(t)<0$. Continuity on the compact frequency interval
gives constants $c,C>0$ such that

$$
 -C/N\le O_{m,N}^{\rm enc}\le-c/N
 \tag{1.7}
$$

for every sufficiently large odd $N$ and every $m$ in the
interval.

There is no $m^2$ pointed-orbit factor in an Euler coefficient.
Thus (1.6) has scale $N^{-1}$ per coefficient, rather than
the scale $N$ of the trace-pair result. After summing a band
of $m$'s, the negative contribution is of order one. More
precisely, for every continuous $w$ on $[1,3/2]$,

$$
 \boxed{\begin{aligned}
 \sum_{N\le m\le3N/2}w(m/N)O_{m,N}^{\rm enc}
  ={}&\frac{c_*}{288}x_N^3
          [-18p_2(t_N)+12p_3(t_N)]\\
   &{}\times\int_1^{3/2}w(v)v^2
                      e^{-\kappa_{\rm esc}x_Nv}\,dv+o(1).
 \end{aligned}}
 \tag{1.8}
$$

For a nonnegative weight positive on a subinterval, its right
side is bounded above by a strictly negative constant, for all
large odd $N$.

## 2. All six connections give distinct legitimate Euler terms

We verify the primitive-orbit, distinct-component, and counting
claims before using the Euler signs.

The physical map $\Psi$ reads a coded cell backwards. Given
a successor permutation $\rho$, connect the physical output
of $e_j$ to the physical input of $e_{\rho(j)}$. A cycle of
length $r$ in $\rho$ is the periodic word of those $r$
cells in the reversed coded cycle order.

Each such component contains exactly $r$ zero markers of
length $2R$, with no other run of that length: its interiors
avoid the run, and every marker is flanked by the fixed nonzero
edge $a$. A proper repetition number would divide $r$.
For $r=1$ none is possible. For $r=2$ a repetition would
have number two and equal marker-gap lengths. For $r=3$ it
would have number three and all three equal gaps. Distinct
length bands in (1.2) exclude both possibilities. Thus each
component is a primitive symbolic orbit.

Its length is at least $m/9$. For large $N$ it is greater
than four. The checked coding theorem says that the only
periodic boundary point is the origin, with an itinerary fiber
of at most four points. A primitive symbolic code of larger
period cannot belong to that fiber. Away from it, periodic
coding is injective. Hence every component is a primitive
actual geometric orbit of its asserted length.

Different components of the same permutation are distinct.
For the identity permutation their lengths $d_1,d_2,d_3$
are distinct. A permutation with a two-cycle has one component
with two marked gaps and one with one marked gap. These cannot
be the same geometric orbit, even if their total lengths
happen to agree. The three-cycle has only one component.
Consequently every $\mathfrak p_\rho$ is a finite set of
distinct primitive orbits, as required for an Euler coefficient.

There is no collision between different connections or different
clusters. From a union $\mathfrak p_\rho$, recover its exactly
three marked gaps. Their lengths assign labels $1,2,3$
uniquely. The middle of the zero marker preceding each gap
fixes that cell's cut, and recovers its word $u_j$.
Following the physical orbit from a cell output to the next
cell input recovers $\rho$. This reconstructs the entire
cluster, its lengths, and its connection. In particular the
six Euler terms of each cluster are distinct, and no such
term is used in two different clusters.

This reconstruction is a statement about geometric periodic
orbits, so it already accounts for cyclic shifts. There is no
factor $m$ or $d_j$ in the cluster count.

## 3. Exact phases and amplitudes for several components

### 3.1. The cut action works for every permutation

Let $W_j(q_{\rm out},q_{\rm in})$ be the exact boundary function
of cell $e_j$ in the common fixed-point chart. The first input
proves, with $\delta=\Lambda^{-R}$, uniformly over all allowed
words and lengths,

$$
 \begin{split}
 D^2W_j&=\operatorname{diag}(s_{\rm u},-s_{\rm s})+o(1),\\
 \partial_{\rm out}W_j(q_*,q_*)&=
                         p_*+\chi\delta S_j+o(\delta),\\
 \partial_{\rm in}W_j(q_*,q_*)&=
                        -p_*+\chi\delta U_j+o(\delta).
 \end{split}
 \tag{3.1}
$$

It also proves the global negative Hessian lower bound
$0.49I\le-D^2W_j$. For a permutation $\rho$, identify each
output endpoint $j$ with input endpoint $\rho(j)$, and sum
the three boundary functions. There are exactly three cut
variables, irrespective of the number of components.

The sum is strongly concave with negative Hessian at least
$0.98I$: every cut occurs twice among the six endpoints.
This remains true for a self-connection, where the two endpoints
of one $W_j$ are the same variable. At a two-cycle the two
off-diagonal contributions may add, but both tend to zero.
At a one-cycle the mixed derivative occurs twice in that
diagonal, and also tends to zero. Thus in every case the cut
Hessian tends uniformly to $-\chi I$.

The exact periodic components of the coded permutation are
critical for this sum, with the same cell deck branches.
The branch-label and stationary uniqueness argument in the
first input is unchanged when the cut graph has more than one
component: apply it to each component. Strong concavity makes
the combined critical cut vector unique. The argument giving
the stationary quadratic action therefore applies verbatim
to these three variables and gives

$$
 \mathcal S_\rho
   =\mathcal S_{\rm base}
      +\frac{\chi\delta^2}{2}\sum_{j=1}^3
                                   (S_j+U_{\rho(j)})^2
      +o(\delta^2).
 \tag{3.2}
$$

Here $\mathcal S_{\rm base}=\sum_jW_j(q_*,q_*)$ is independent
of $\rho$, and the error is uniform over the six permutations
and all interiors. The exact odd-dimensional local phase
law identifies the product of the component holonomies with
$\exp(i\mathcal S_\rho/h)$; no constant phase has been omitted.

For the reference physical three-cycle $\rho_0=(132)$, which
corresponds to the coded order $123$, (3.2) implies

$$
 \mathcal S_\rho-\mathcal S_{\rho_0}
  =\chi\delta^2\left[
       \sum_jS_jU_{\rho(j)}-\sum_jS_jU_{\rho_0(j)}\right]
         +o(\delta^2).
 \tag{3.3}
$$

The terms $\sum S_j^2+\sum U_j^2$ cancel.

### 3.2. The exact scalar cocycle is still localized

Match equal cells at equal offsets between two connections.
The codes agree on a central block of radius at least
$R+\min(b,d_j-1-b)$, up to a fixed indexing constant, because
the neighboring cells always supply a buffer of $R$ zeros.
This remains true if the neighboring cell is the same cell
through a self-connection. The uniform Hölder bound for
$\log\gamma_h$ therefore gives

$$
 \left|\log
   \frac{\prod_{p\in\mathfrak p_\rho}\Gamma_h(p)}
        {\Gamma_h(p_{\rho_0})}\right|
   \le C\theta^R .
 \tag{3.4}
$$

The sum has no factor equal to a cell length; the offsets give
a summable geometric series at each boundary. Scalar products
can be matched regardless of the order of the separate cycles.

All component lengths sum to $m$. Hence their factors
$\zeta_N^{d_p}\lambda^{-d_p/2}$ have the common product
$\zeta_N^m\lambda^{-m/2}$. The exact modulus comparison over
the reference orbit is

$$
 |a_{p_{\rho_0},N}|^2
          =\Lambda_{\rho_0}^{-1}(1+O(N^{-1})).
 \tag{3.5}
$$

Put $B_\rho=\prod_{p\in\mathfrak p_\rho}a_{p,N}$.
Equations (3.3)--(3.5), $h=(2\pi N)^{-1}$, and
$N\delta^2=x_N=O(1)$ give the uniform complex relation

$$
 \boxed{\displaystyle
 B_\rho=B_{\rho_0}\,
   \exp\left(it_N\left[
     \sum_jS_jU_{\rho(j)}-\sum_jS_jU_{\rho_0(j)}
                          \right]\right)(1+o(1)).}
 \tag{3.6}
$$

This is the needed extension of the actual action and amplitude
calculation to all component patterns. It is not an assumption
that disconnected orbits have independent phases.

## 4. Fermionic signs and the full six-term square

The exact Euler expansion proved in the second input is

$$
 \mathcal Z_N(z)=\prod_{p\ {\rm primitive}}
                           (1-a_{p,N}z^{d_p}),\qquad
 [z^m]\mathcal Z_N
   =\sum_{\mathfrak p:\,\sum d_p=m}
                    (-1)^{|\mathfrak p|}\prod_{p\in\mathfrak p}a_{p,N}.
 \tag{4.1}
$$

At every fixed degree these sums are finite. Section 2 verifies
that every term (1.3) is one of the distinct terms in (4.1).
For a permutation of three objects,

$$
 (-1)^{c(\rho)}=-\operatorname{sgn}(\rho).
 \tag{4.2}
$$

Let $E_t$ be the $3$-by-$3$ matrix
$(e^{itS_iU_j})_{i,j}$. Equation (3.6) gives, pointwise
in every cluster,

$$
 \sum_{\rho\in S_3}C_\rho
  =-B_{\rho_0}e^{-it_N\sum_jS_jU_{\rho_0(j)}}
                                      [\det E_{t_N}+o(1)] .
 \tag{4.3}
$$

This is an absolute error $o(|B_{\rho_0}|)$, not a relative
error measured against a possibly vanishing determinant.
Since $|\det E_t|\le6$, squaring and using (3.5) proves

$$
 \left|\sum_\rho C_\rho\right|^2
     =\Lambda_{\rho_0}^{-1}
                              [|\det E_{t_N}|^2+o(1)],
 \quad
 \sum_\rho|C_\rho|^2
     =\Lambda_{\rho_0}^{-1}[6+o(1)] .
 \tag{4.4}
$$

All errors are uniform in the clusters.

The endpoint factorization proved in the first input applies
to any bounded equicontinuous function of the six scattering
coordinates. In particular it applies to
$|\det E_t|^2$ for $t$ in the compact interval containing
all $t_N$. It uses fixed endpoint cylinders first and their
limit afterwards, so no new frequency-dependent mixing estimate
is needed.

Under the resulting product probability
$\sigma^{\otimes3}\otimes\upsilon^{\otimes3}$, the exact
six-term determinant integral is

$$
 \int|\det E_t|^2
  =6-18p_2(t)+12p_3(t)=36e_3(K_t).
 \tag{4.5}
$$

One can check the constants without any determinant theorem.
Expand its two determinants, giving $36$ ordered permutation
pairs. A pair with relative permutation equal to the identity
has integral $1$, and there are six of them. Each of the
three relative transpositions has six ordered pairs, negative
sign, and integral $p_2(t)$. Each of the two relative
three-cycles has six ordered pairs, positive sign, and integral
$p_3(t)$. The cycle integrals follow by integrating one group
of endpoint variables first, which gives the kernel of $K_t$,
and then composing along the cycle. This proves the first
identity in (4.5). The coefficient identity
$6e_3=p_1^3-3p_1p_2+2p_3$, with $p_1=1$, gives the second;
the third input supplies a direct proof from the eigenvalue
product or from permutation cycle counting.

Because $K_t$ is positive with trace one, its nonnegative
eigenvalues are at most one. Thus $0<p_3(t)\le p_2(t)$.
The full integral (4.5) is nonnegative, while its part after
removing the six diagonal terms is strictly negative:

$$
 -18p_2(t)+12p_3(t)\le-6p_2(t)<0 .
 \tag{4.6}
$$

The negative terms are the actual signs of Euler orbit sets.
No signs were attached to geometric orbit pairs by hand.

## 5. Summing the actual clusters with their correct scale

At fixed $(\ell_1,\ell_2,\ell_3)$, the reference multiplier
sum over all good interiors is

$$
 c_*\varepsilon^3e^{-\kappa_{\rm esc}m\varepsilon}(1+o(1)).
 \tag{5.1}
$$

The full endpoint-weighted version of that statement is proved
in the first input. Applying it to (4.4)--(4.5) gives, for
the fixed triple, the same leading factor times respectively
$36e_3(K_{t_N})$, $6$, and
$-18p_2(t_N)+12p_3(t_N)$, with error $o(\varepsilon^3)$.
It is uniform in all admissible lengths.

There are exactly $m^2/288+O(m)$ length triples. Section 2
has proved that this is also the count of distinct cluster
labels without cyclic overcounting. Multiplying gives (1.6).
The uniform error is $o(m^2\varepsilon^3)=o(N^{-1})$, and the
integer rounding error is $O(m\varepsilon^3)=O(N^{-2})$.
This calculation explains why no $m^2$ factor can be inserted:
the primitive Euler factors in (4.1) already have their
unpointed weights.

The power traces are continuous in $t$, as follows directly
from their bounded-kernel cycle integrals. Their positive
minimum on the fixed compact interval containing $t_N$
and the bounds $x_N\asymp1$ prove (1.7). Summing the
uniform $o(N^{-1})$ remainder and taking a Riemann sum with
the bounded parameter $x_N$ gives (1.8).

## 6. Exact scope relative to the quantum spectral problem

The selected negative sum $O_{m,N}^{\rm enc}$ comprises all
thirty off-diagonal ordered pairs within each six-connection
cluster. Each such term is an actual term in the square of
the degree-$m$ coefficient of $\mathcal Z_N$.
The same expansion also contains pairs from different clusters,
and pairs involving other orbit sets. No estimate for those
terms follows from (1.6).

Moreover the exact relation to the finite quantum determinant is

$$
 \mathcal Z_N(z)=\det(I-zU_N)e^{G_N(z)},\qquad
 G_N(z)=\sum_{m\ge1}\frac{E_{m,N}}m z^m,\quad
 |E_{m,N}|\le2(0.421)^m .
 \tag{6.1}
$$

This relation, including its analytic domain, is established in
the second input. Thus the present calculation concerns the
principal Euler determinant with the exact quantum orbit
amplitudes. It is not, term by term, a calculation of the
polynomial coefficients of $\det(I-zU_N)$. Transferring a
selected subsum through the convolution in (6.1) would require
additional control; it is not asserted here.

Within its stated expression, the result exhibits both signs
with a fully controlled error: the two three-cycle reconnections
give the positive trace-cube profile, while all component
patterns with their prescribed fermionic signs give the
strictly negative complete off-diagonal profile (4.6).
The complement required for $H_{\rm diag}$, and the mixed
numerator/denominator estimates needed to recover long trace
statistics from determinant coefficients, remain unproved.
