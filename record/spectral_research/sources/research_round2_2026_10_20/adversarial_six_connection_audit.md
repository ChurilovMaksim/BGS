> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_six_connection_audit.md`. Embedded SHA256: `7cdcf40afd1a63f94e455396d44af40c14c830eba29bc8413986b4ef7c8070f2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit of six-connection Euler cancellation

20 October 2026.

## Input and verdict

The full input fermionic_six_connection_cancellation.md has SHA-256
4661fed89558f03c58e085ec70df919b14056ff4ec5e3e765e6564ce35fbb865.
Its complete proof was independently checked against the audited
signed-profile and Gram-permutation arguments. **PASS.**

The actual result concerns all thirty ordered off-diagonal terms
within each six-reconnection cluster of primitive Euler orbit sets:
$$
 O^{\rm enc}_{m,N}
 =W_{m,N}\{-18\operatorname{Tr}K_{t_N}^2
                 +12\operatorname{Tr}K_{t_N}^3\}+o(N^{-1}),
$$
$$
 W_{m,N}=\frac{c_*}{288}m^2\varepsilon^3
                      e^{-\kappa_{\rm esc}m\varepsilon},
 \qquad N\le m\le3N/2.
$$
The error is uniform, with the exact fixed parameter of the problem.

## 1. Distinct primitive Euler terms

A cycle of a successor permutation contains $r\in\{1,2,3\}$
cells and exactly $r$ long zero markers. A proper repetition
number must divide $r$. At $r=1$ this is impossible; at $r=2$
or $3$ it would force the successive marked gaps to be equal.
Their three disjoint length bands exclude that possibility.
The component periods exceed four for large $N$, so none can
be a code in the exceptional periodic boundary fiber. All
components are primitive actual orbits.

Different components are distinct. For three singletons the
lengths differ. In the two-component case their numbers of
marked gaps differ, even if the total periods happen to coincide.

Conversely, an actual orbit set in this collection determines its
three marker gaps. Their lengths determine the labels. The
midpoint of each preceding marker determines the cut and recovers
the entire cell. Following the actual orbit recovers its successor
permutation. Thus every term belongs to exactly one cluster and
one connection. This verifies that the selected thirty ordered
pairs are genuine distinct terms of the Euler coefficient square,
without cyclic or cross-cluster duplication.

## 2. Concavity and phases for every component pattern

For three independent cut variables $q$, let $E_\rho q$
list all six endpoint positions with the identifications
prescribed by $\rho$. Every variable appears twice, including
at a self-connection, so
$$
 E_\rho^TE_\rho=2I.
$$
The negative Hessian of the sum of the three boundary actions
is therefore at least $0.49E_\rho^TE_\rho=0.98I$.
In the limit, its Hessian is $-\chi I$: each variable receives
one output diagonal $s_{\rm u}$ and one input diagonal
$-s_{\rm s}$, while all mixed terms tend uniformly to zero.

The same stationary elimination as in the signed-profile proof
works for each permutation, whether connected or disconnected:
$$
 \mathcal S_\rho
 =\sum_jW_j(q_*,q_*)+
   \frac{\chi\varepsilon}{2}\sum_j(S_j+U_{\rho(j)})^2
   +o(\varepsilon).
$$
The exact deck-gauged action is used on each component. Subtracting
one reference connection cancels the common base value and all
pure squares. Multiplication by $2\pi N$ leaves a uniform
$o(1)$ error because $N\varepsilon$ is bounded.

Matching equal cells at equal offsets gives the localized
$\Gamma_h$ product ratio $1+O(\theta^R)$, also for
self-connections. All component periods sum to $m$, so their
remaining prefactors have the common product
$\zeta_N^m\lambda^{-m/2}$. There is no component-dependent
factor to add to the exact holonomies. Consequently the six
products have the relative phases
$$
 \exp\left(it_N\sum_jS_jU_{\rho(j)}\right)(1+o(1))
$$
after factoring out one common reference weight and phase.

## 3. The signs and all constants

The Euler coefficient uses each primitive orbit once with a
minus sign. For a permutation of three objects,
$$
 (-1)^{c(\rho)}=-\operatorname{sgn}\rho.
$$
Thus the sum of the six weights equals a common factor times
$-\det(e^{it_NS_iU_j})$, with absolute error $o(1)$ after
dividing by the reference weight. No relative error is asserted
at a zero of this determinant.

Under the proved independent endpoint laws the determinant
square has 36 ordered permutation pairs:

* six equal pairs, each of integral $1$;
* eighteen pairs with relative transposition, of negative sign
  and integral $\operatorname{Tr}K_t^2$;
* twelve pairs with relative three-cycle, of positive sign
  and integral $\operatorname{Tr}K_t^3$.

Therefore its expectation is
$$
 6-18\operatorname{Tr}K_t^2+12\operatorname{Tr}K_t^3
 =36e_3(K_t).
$$
The diagonal expectation is $6$. Since $K_t$ is positive
with trace one, its eigenvalues lie in $[0,1]$, and
$$
 0<\operatorname{Tr}K_t^3\le\operatorname{Tr}K_t^2.
$$
The off-diagonal bracket is consequently at most
$-6\operatorname{Tr}K_t^2<0$, uniformly away from zero over
the compact frequency interval.

## 4. Scale and error

At each fixed length triple the total reference multiplier
weight is
$$
 c_*\varepsilon^3e^{-\kappa_{\rm esc}m\varepsilon}(1+o(1)).
$$
The endpoint-weighted version is valid for the bounded,
equicontinuous determinant square. There are
$m^2/288+O(m)$ distinct length triples. An Euler coefficient
has unpointed primitive weights, so no additional factor $m^2$
occurs here.

Thus the leading normalization is $W_{m,N}\asymp N^{-1}$.
The uniform relative error produces $o(m^2\varepsilon^3)
=o(N^{-1})$; rounding produces $O(m\varepsilon^3)=O(N^{-2})$.
Summing the time band gives the asserted finite, strictly
negative weighted contribution of order one.

## 5. Exact scope

These are terms of the principal Euler determinant
$\mathcal Z_N$. Its exact relation to the quantum determinant is
$$
 \mathcal Z_N(z)=\det(I-zU_N)e^{G_N(z)}.
$$
The audit checks the input's distinction between those two
coefficient systems. No selected-term transfer through this
convolution is claimed. Cross-cluster pairs, other Euler orbit
sets, and the complete power-trace statistic remain uncontrolled.
The negative contribution is not a proof of $H_{\rm diag}$
or a refutation of it.
