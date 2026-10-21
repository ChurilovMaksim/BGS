> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_signed_three_cell_audit.md`. Embedded SHA256: `13d89186d90925a8d69ff38192772f087e7e94daeef6f913c9c316d8998923a0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit of the signed three-cell profile

20 October 2026. This audit concerns the exact family, with fixed
$\tau=10^{-80}$, and all sufficiently large odd $N$. It does
not assert the full pair limit or $H_{\rm diag}$.

## 1. Frozen inputs and verdict

| File | SHA-256 |
|---|---|
| fermionic_signed_three_cell_profile.md | edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5 |
| adversarial_endpoint_symbols_and_renewal.md | 561efce86a8aa2cab0c49fa05236e64f420ce26919ae0342dee2566e552ec32a |
| root_gram_permutation_identity.md | ca635dab171d81b673aec7136b2123ab9f2b82deac8a8a9b82a436d961520375 |

The first file was read in full. Its load-bearing steps were
independently rederived, rather than accepted from a previous
verdict. **PASS.** No mathematical correction is needed.

The conclusion checked is
$$
 E^{\rm full}_{m,N}
 =\frac{c_*}{144}\,m^4\varepsilon^3
 e^{-\kappa m\varepsilon}
 \operatorname{Tr}(K_{2\pi\chi N\varepsilon}^{\,3})+o(N),
 \qquad N\le m\le3N/2,
$$
uniformly, where
$$
 R=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0,
 \quad \varepsilon=\Lambda^{-2R},\quad R_0\ge0
$$
is any fixed integer offset. The constants and measures are those
explicitly defined in the input. In particular the rounding
parameter $N\varepsilon$ is retained, not presumed convergent.

## 2. The edge normalization has no missing multiplier

For the rare marker word $a0^{2R}a$, place its zero edges at
indices $-R,\ldots,R-1$. The left $a$ is at $-R-1$, the
right $a$ at $R$, and the cut is the vertex between edges
$-1$ and $0$. Relative to the first $a$, that cut is at
shift $R+1$. Nevertheless each zero tail has exactly $R$
edges:

* the stable output base is the state just before the right
  $a$, whose code has edge zero $a$ and zero negative past;
* the unstable input base is just after the left $a$, whose
  code has edge $-1$ equal to $a$ and zero nonnegative future.

Physical motion is inverse to forward coding. Thus the cut is
obtained by $R$ iterates of physical $\Psi$ from the stable
base, and $R$ inverse iterates from the unstable base. These
are exactly the $S,U$ definitions in the input's Section 2.1.
The normalization is $\Lambda^R(q-q_*)$, with no additional
$\Lambda$ or $\Lambda^{-1}$.

The scalar recurrence
$$
 f(t)=\Lambda^{-1}t+O(t^2),\qquad
 |f^j(t)|\le C\Lambda^{-j}|t|
$$
gives
$$
 |\Lambda^{j+1}f^{j+1}(t)-\Lambda^jf^j(t)|
 \le C\Lambda^{-j}|t|^2.
$$
Summing its tail proves
$$
 f^R(t)=\Lambda^{-R}L_*(t)+O(\Lambda^{-2R})
$$
uniformly on the fixed entry interval. The derivative product
$$
 \Lambda^R(f^R)'(t)=
 \prod_{j<R}\bigl(1+O(\Lambda^{-j}|t|)\bigr)
$$
is uniformly bounded. Hence $L_*$ is Lipschitz. A common finite
entry time exists from the frozen homoclinic construction, so
all constants remain uniform over arbitrarily long excursions.
The coding estimate then gives the fixed-cylinder approximation
of $S,U$ used later; its constant is independent of the
interior length.

## 3. Uniform Hessian convergence from continued fractions

Write
$$
 \alpha_*=F_{QQ},\qquad \beta_*=F_{Qq}>0,\qquad
 \gamma_*=F_{qq}
$$
on the fixed lifted edge. The internal negative Hessian has
diagonal entries $a_j\in[1.49,1.51]$ and adjacent entries
$-b_j$, $b_j\in[.24,.26]$. Its inverse has a uniform row-sum
bound by the Neumann series after dividing by the diagonal:
$$
 \frac{.52}{1.49}<1.
$$
Differentiating the internal critical equations with respect
to the two endpoint positions produces forcing only at the
two end coordinates. Therefore changing the endpoints by
$O(\delta)$, $\delta=\Lambda^{-R}$, changes every internal
critical coordinate by $O(\delta)$, independently of the
number of internal coordinates. Momentum changes obey the
same bound by the bounded Hessian of $F$.

At the first and last $j\le R/2$ physical edges the unmodified
homoclinic path is within $C\Lambda^{-(R-j)}$ of the fixed
orbit. The preceding response estimate preserves convergence
on those edges throughout the complete $O(\delta)$ endpoint
neighborhood. Exact deck covariance allows comparison in the
same fixed local charts.

The elimination recursion is
$$
 d_j=a_j-\frac{b_j^2}{d_{j+1}},\qquad d_j\ge1.4.
$$
Indeed $1.49-.26^2/1.4>1.4$, and the recursion contracts its
last denominator by at most
$$
 .26^2/1.4^2<.04.
$$
Thus a distant tail of the Hessian changes an endpoint Schur
diagonal by $O(.04^j)$. Combining this with convergence of
the first $R/2$ coefficients proves convergence of both
endpoint diagonals. The endpoint mixed term is bounded by
$C(.26/1.4)^{d-1}$, so it tends uniformly to zero.

The limiting recursion solves
$$
 d_*=-\alpha_*-\gamma_*-\beta_*^2/d_*.
$$
Its larger positive solution yields
$$
 W_{{\rm out},{\rm out}}\longrightarrow
 \alpha_*+\beta_*^2/d_*,
 \qquad
 W_{{\rm in},{\rm in}}\longrightarrow
 \gamma_*+\beta_*^2/d_*.
$$
The exact input-output slope formula is
$$
 s'=\alpha_*-\frac{\beta_*^2}{\gamma_*+s},
 \qquad b=-\frac{\gamma_*+s}{\beta_*}.
$$
Substitution shows
$$
 s_{\rm u}=\alpha_*+\beta_*^2/d_*,
 \qquad
 s_{\rm s}=-\gamma_*-\beta_*^2/d_*,
 \qquad
 \Lambda=d_*/\beta_*.
$$
The two horizontal factors are respectively $\Lambda$ and
$\Lambda^{-1}$. In particular
$$
 \chi=s_{\rm s}-s_{\rm u}
 =d_*-\beta_*^2/d_*
 =\beta_*(\Lambda-\Lambda^{-1})>0.
$$
Consequently
$$
 D^2W_e\longrightarrow\operatorname{diag}(s_{\rm u},-s_{\rm s})
$$
uniformly on the required neighborhoods and over all interiors.
This proof does not assume differentiability of the global
conjugacy or of the invariant bundles.

## 4. Stationary phase and its uniform error

At the homoclinic endpoints,
$$
 \begin{aligned}
 (q_{\rm out},p_{\rm out})
   &=(q_*+\delta S,\ p_*+s_{\rm s}\delta S)+O(\delta^2),\\
 (q_{\rm in},p_{\rm in})
   &=(q_*+\delta U,\ p_*+s_{\rm u}\delta U)+O(\delta^2).
 \end{aligned}
$$
Use the exact endpoint derivatives
$\partial_{\rm out}W=p_{\rm out}$ and
$\partial_{\rm in}W=-p_{\rm in}$. Translating the endpoints to
$(q_*,q_*)$ and using Section 3 gives
$$
 \partial_{\rm out}W(q_*,q_*)=p_*+\chi\delta S+o(\delta),
 \qquad
 \partial_{\rm in}W(q_*,q_*)=-p_*+\chi\delta U+o(\delta).
$$
At a cut joining output $i$ to input $j$, the $p_*$ terms
cancel. The three-cut gradient is
$\chi\delta(S_i+U_j)+o(\delta)$, and its Hessian is
$-\chi I+o(1)$.

Global strong concavity first places the critical cut vector
within $C\delta$ of the fixed cut vector. Taylor's theorem on
that whole segment then yields the critical-value increment
$$
 \frac{\chi\delta^2}{2}
       \sum_{\text{consecutive }i,j}(S_i+U_j)^2+o(\delta^2).
$$
The base value $\sum_eW_e(q_*,q_*)$ is identical for both
orders. The sums of the pure squares cancel. With the input's
orientation convention the two coded orders therefore have
action difference
$$
 -\chi\delta^2 Q+o(\delta^2),
$$
where
$$
 Q=S_1U_2+S_2U_3+S_3U_1
     -S_1U_3-S_3U_2-S_2U_1.
$$
Each $W_e$ contains its exact deck term. Thus their sum
computes the original phase; no winding-dependent constant is
dropped here.

Because $N\delta^2=N\varepsilon$ stays in a compact interval,
$N\,o(\delta^2)=o(1)$ uniformly. Combined with the frozen
localized $\Gamma_h$ comparison and its cycle modulus,
$$
 a_{123,N}\overline{a_{132,N}}
 =\Lambda_{123}^{-1}e^{-2\pi i\chi N\varepsilon Q}(1+o(1)).
$$
The modulus error is $O(mh^2)=O(N^{-1})$, and the additional
scalar-cocycle error is $O(\theta^R)$. The resulting observable
has bounded frequency in bounded scattering coordinates.

## 5. Renewal and endpoint normalization

The exact avoidance generating function is
$$
 G_k(z)=(I-z^kJ^k)
       (I-zT+z^{k+1}(T-J)J^k)^{-1}.
$$
The order follows from the exact product
$$
 (I-zBA_k)(I-zJ)=I-zT+z^{k+1}BJ^k,
 \quad B=T-J,\quad A_k=\sum_{j<k}(zJ)^j.
$$
No factors are commuted.

With $J^k=\varepsilon(g\delta_o+O(\theta^k))$ and
$T=\Pi+T_Q$, $\Pi=\mathfrak h\nu$, the complementary
resolvent is uniformly bounded for $|z|\le1.05$.
The scalar Schur denominator near $1$ is
$$
 1-z+\kappa\varepsilon z^{k+1}
   +O(\varepsilon\theta^k+\varepsilon^2),
 \qquad
 \kappa=\nu((T-J)g)\mathfrak h(o).
$$
Since $Jg=\Lambda^{-1}g$ and $\nu T=\nu$,
$\kappa=(1-\Lambda^{-1})\nu(g)\mathfrak h(o)>0$.
Rouché's theorem first on a fixed disk about $1$, then on
a disk of radius $C\varepsilon$, yields its unique simple pole
$$
 z_k=1+\kappa\varepsilon
      +O(k\varepsilon^2+\varepsilon\theta^k).
$$
The normalized pole numerator is $\Pi+O(k\varepsilon)$.
The remainder is uniformly bounded on $|z|=1.05$, yielding
$$
 G_{k,\ell}
 =e^{-\kappa\ell\varepsilon}\Pi
   +O(k\varepsilon+\theta^k+1.05^{-\ell})
$$
for $\ell\asymp N$, uniformly. These are the same independently
proved estimates in the second frozen input.

The open three-cell expression is
$$
 [J^R A G_{k,\ell_3}A J^k
       A G_{k,\ell_2}A J^k
       A G_{k,\ell_1}A J^R1](o).
$$
Reading from the right, the normalized factors alternate
$g$, $Ag$, $\mathfrak h\nu(Ag)$, and
$g(A\mathfrak h)(o)\nu(Ag)$. Evaluation of the last left
$J^R$ is exact. Thus the zero-branch factor is
$\Lambda^{-2R-2k}=\varepsilon^3$, and the leading scalar is
$$
 c_*=[\nu(Ag)(A\mathfrak h)(o)]^3.
$$

The prefix and suffix cylinder laws are
$$
 P_K(w)=\frac{\nu(J_wAg)}{\nu(Ag)},\qquad
 Q_K(v)=\frac{(AJ_v\mathfrak h)(o)}{(A\mathfrak h)(o)}.
$$
Their consistency follows with precisely the reverse operator
order $J_{we}=J_eJ_w$, $J_{ev}=J_vJ_e$. The fixed-cylinder
factorization is obtained by inserting
$A J_vG_{k,\ell-2K}J_wA$. A missed run across an interface
forces $k-K$ successive zero edges, costing $O_K(\varepsilon)$.
With all three markers restored this is $O_K(\varepsilon^4)$,
which is negligible compared with the total
$O(\varepsilon^3)$.

Only after fixing $K$ is the transfer estimate applied. The
bounded, equicontinuous phase on the scattering supports can
then be approximated by these cylinders, uniformly in the
compact parameter $t=2\pi\chi N\varepsilon$. Taking $N$
large at fixed $K$, followed by $K$ large, proves a uniform
$o(\varepsilon^3)$. There is no unbounded symbolic norm hidden
in that order of limits.

## 6. Positivity and the coefficient $1/144$

Under the independent endpoint laws,
$$
 \int e^{-itQ}\,d\sigma^{\otimes3}d\upsilon^{\otimes3}
 =\operatorname{Tr}(K_t^3),
$$
because integrating the $U$'s produces the cyclic product of
the three kernels of $K_t$. If
$$
 (V_tf)(s)=\int e^{itsu}f(u)\,d\upsilon(u),
$$
then $K_t=V_tV_t^*$, $\|V_t\|_{\rm HS}^2=1$. Hence $K_t$
is positive trace class with trace $1$. Its trace cube is
strictly positive: $\operatorname{Tr}(K_t^3)=0$ would give
$V_t^*K_t=0$, hence $K_t^2=0$, hence $K_t=0$.
Continuity gives a positive minimum over any fixed compact
$t$-interval.

The admissible length choices have cardinality
$$
 \bigl(\lfloor m/6\rfloor-\lceil m/8\rceil+1\bigr)
 \bigl(\lfloor m/3\rfloor-\lceil m/4\rceil+1\bigr)
 =m^2/288+O(m).
$$
Goodness gives exactly three long zero markers. A proper
repetition would have repetition number $3$ and force all
marker gaps equal, contradicting their three disjoint length
bands. The primitive codes cannot map to the sole periodic
boundary point, whose itinerary fiber has at most four points.
Thus the geometric orbits are primitive.

The marker immediately preceding the unique shortest gap has
a unique midpoint cut. It reconstructs the first word and all
three interiors. The opposite cyclic gap orientation identifies
the partner. This prevents both cyclic overcount and unordered
pair overcount. Each primitive orbit has $m$ pointed trace
terms, and an unordered pair contributes both directions.
Therefore the coefficient is exactly
$$
 2m^2\cdot(m^2/288)=m^4/144.
$$

The $O(m)$ length-count error contributes
$O(m^3\varepsilon^3)=O(1)=o(N)$. The uniformly normalized
transfer and phase errors contribute
$o(m^4\varepsilon^3)=o(N)$. This proves the audited uniform
error statement and the subsequent weighted Riemann sum with
the exact bounded parameter $N\varepsilon$.

## 7. Scope

The signed profile is a substantive actual-family calculation:
the complete specified encounter family is evaluated without
termwise phase selection and without losing its Heisenberg
scale. The equality does not determine the complementary
different-orbit sum. In particular the explicit remaining
weighted cancellation displayed in the input's equation (8.2)
is not proved by this audit or by positivity of the trace cube.
The full pair criterion and higher $H_{\rm diag}$ moments
remain open in this work.
