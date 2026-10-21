> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round14_2026_10_21/obstruction/r14_independent_inserted_trace_audit.md`. Embedded SHA256: `2abd38cb5ddcf268788c1e324c23f9518021aa1d9c700e7cf6363ecc16324ad7`.
> [Thematic guide](../../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of the inserted trace and two-copy coboundary calculation

Date: 21 October 2026. Auditor: /root/r14_original_obstruction.

## 1. Input and result

Audited source:
research_round14_2026_10_21/signed_sum/r14_inserted_trace_and_two_copy_coboundary.md,
SHA-256
066f851dabbcfdb88b0ab640b0e0e0b2242943ae20e59922ed03a3285b60ea52,
42,638 bytes. The raw source was read; §§2--6 were independently
reconstructed. No mathematical change was made to the source.

**The theorem formulas in §§2--6 pass.** In particular the insertion
has its own proved remainder, the two-copy projection includes all
degeneracies, the physical normalization in (5.5) is correct, and
the sign and indices in (6.4)--(6.6) are correct.

There is one wording clarification: the paragraph after (5.5) says
that the residual without the multiplier $N$ has order $N^{-1}$.
The proof establishes a lower bound of that order, not an upper bound
or an exact asymptotic order for the residual. It should say
“the obtained lower bound without the multiplier $N$ has order
$N^{-1}$.” This does not affect the boxed results.

Post-audit correction check: the later source version SHA-256
a4f9f49283b06d0d03c7b9980d795c2b082bf0d761a81e1d10037f7278424896
contains precisely this corrected paragraph, including an explicit
statement that no matching upper bound was established. That revised
paragraph was checked directly. The theorem audit above is pinned to
the original source hash.

## 2. The inserted amplitude is actually proved

Applying the finite Weyl sum to the exact one-step kernel gives
exactly
$$
B_h^A=\sum_{k,l}a_{kl}
\exp\!\left(2\pi ik(Q+\pi hl)
+\frac{i}{h}[F(Q+2\pi hl,q)-F(Q,q)]\right)
B_h(Q+2\pi hl,q).
$$
With $F=F_0+G$, its exponent divided by $i$ is
$$
2\pi((k-3l/4)Q+(l/4)q)
+h(2\pi^2kl-\tfrac32\pi^2l^2)
+2\pi l\int_0^1G_Q(Q+2\pi uhl,q)\,du.
$$
Thus its unbounded real linear part is only a phase. All needed
derivatives of the remaining part are bounded uniformly on the real
plane. Real shifts preserve the analytic strip. The actual amplitude
and its derivatives consequently satisfy
$$
B_h^A=a(Q,F_Q)\,2\sqrt{F_{Qq}}+O(h).
$$
This conclusion differentiates neither the old trace formula nor its
unknown remainder.

Multiplication by $A_h$ preserves the lattice covariance and adds
only a finite number of translations to the absolutely summable
metaplectic word expansion at fixed $h$. The coherent and Abel
bounds are uniform in those translations. The same four exact
sectors therefore apply to $A_hV_h$, with the same phase.
At a sector critical point the output equals the input modulo an
integer lattice vector; periodicity gives $a(Q,F_Q)=a(q,p)$.
Those values are $9/10,9/10,-11/10,-11/10$.
The stationary-phase prefactor is unchanged and each sector has
error $O(h)$ after multiplication by $C_h$. This proves the
inserted formula (2.1) with total $O(N^{-1})$ error.

The numerical inequality for its leading modulus is also correct:
$$
\frac{11}{10}(6150)-\frac9{10}\frac32
=\frac{135273}{20}.
$$
Thus the stated $c_*>11/10$ and the lower limit (3.3) follow.

The raw exact-amplitude and sector proofs used in this check were
read directly earlier in this same audit branch; their pinned hashes
are in input_hashes.json and their read scope is documented in
r14_original_spectral_orbit_barrier.md. The raw Round 13 §§1--6,
including the fixed-dimensional Abel stationary-phase proof, were
also read directly.

## 3. Why coincident difference phases do not invalidate (5.3)

Here is a separate index proof of the delicate two-copy projection.
Choose an eigenbasis of $U$, allowing repeated eigenvalues
$\lambda_j$. On the matrix basis $E_{jk}$,
$$
\mathscr U(E_{jk})=\lambda_j\overline{\lambda_k}E_{jk},
$$
and
$$
(\operatorname{ad}_A)_{(j,k),(l,m)}
=A_{jl}\delta_{km}-\delta_{jl}A_{mk}.
\tag{3.1}
$$
Projection onto the full commutant of $\mathscr U$ retains a
matrix entry precisely when
$\lambda_j\overline{\lambda_k}
=\lambda_l\overline{\lambda_m}$.

In the first term of (3.1), $k=m$, so this condition reduces to
$\lambda_j=\lambda_l$. In the second term, $j=l$, so it reduces
to $\lambda_k=\lambda_m$. Entries at other repeated differences
are zero in (3.1) before any projection. Thus the projection is
exactly
$$
\mathfrak E_{\mathscr U}(\operatorname{ad}_A)
=\operatorname{ad}_{\mathcal E_U(A)}.
$$
Every repeated eigenvalue block of $U$ is retained in full.
No nonresonance or simple-spectrum hypothesis appears.

## 4. Superoperator dimension and normalization

For $Q=\mathcal E_U(A)$, $Q=Q^*$, diagonalizing $Q$ yields
$$
\|\operatorname{ad}_Q\|_{\mathrm{HS}(M_N)}^2
=\sum_{j,k}(q_j-q_k)^2
=2N\|Q\|_{\rm HS}^2-2(\operatorname{Tr}Q)^2.
$$
The dimension of the space acted on is $D=N^2$. For the original
matrices at $N>18$, the finite Fourier support and zero constant
coefficient give $\operatorname{Tr}A=0$, hence
$\operatorname{Tr}Q=0$.

The range of $B\mapsto B-UBU^*$ is the orthogonal complement of
the full commutant, by division by $1-\lambda\overline\mu$ on
every off-diagonal spectral block. Applying this statement to
$\mathscr U$ gives the exact infimum
$$
\inf_{\mathscr B}
\|N\operatorname{ad}_A-(\mathscr B-\mathscr U\mathscr B\mathscr U^*)\|
_{\mathrm{HS}(M_N)}
=N\sqrt{2N}\,\|Q\|_{\rm HS}.
$$
Dividing by $\sqrt D=N$ leaves
$\sqrt{2N}\|Q\|_{\rm HS}$.
Finally
$$
\sqrt N\|Q\|_{\rm HS}\ge|\operatorname{Tr}(QU)|
=|\operatorname{Tr}(AU)|.
$$
The limit lower bound is therefore exactly $\sqrt2\,c_*$,
as claimed in (5.5). The physical multiplier $N$ is essential.
Without it this reasoning gives only a lower bound proportional
to $N^{-1}$, which explains the wording clarification in §1.

## 5. The complete derivative and the triple trace indices

Cyclic differentiation gives
$p'_m=iNm\,\operatorname{Tr}(AU^m)$. Hence
$$
S'_N=-\frac2N\sum_m mw_m
\operatorname{Im}\{\overline{p_m}\operatorname{Tr}(AU^m)\}
=-\frac2N\operatorname{Tr}(QG).
$$
The sign is negative because
$\operatorname{Re}(iz)=-\operatorname{Im}z$.
The matrix $G$ is Hermitian, commutes with $U$, and has zero
trace. Projecting $A$ after this differentiation is exact and
does not require differentiating $\mathcal E_U$, even at an
eigenvalue crossing.

Put $Z_m=\overline{p_m}U^m$. The four terms in
$$
\operatorname{Tr}(\operatorname{Im}Z_m\operatorname{Im}Z_n)
=-\tfrac14\operatorname{Tr}
(Z_mZ_n-Z_mZ_n^*-Z_m^*Z_n+Z_m^*Z_n^*)
$$
are paired by complex conjugation. In particular
$$
\operatorname{Tr}(Z_mZ_n^*)
=\overline{p_m}p_np_{m-n},\qquad
\operatorname{Tr}(Z_mZ_n)
=\overline{p_m}\overline{p_n}p_{m+n}.
$$
It follows that their contribution is
$$
\tfrac12\operatorname{Re}
\{\overline{p_m}p_np_{m-n}
-\overline{p_m}\overline{p_n}p_{m+n}\}.
$$
Summation proves (6.6), including the factor $1/2$, the negative
second term, $p_0=N$, and $p_{-j}=\overline{p_j}$.
The largest positive time needed is $4N-2$. Positivity belongs
to the full expression $\|G\|_{\rm HS}^2$, not to its individual
triple-trace terms.

As a finite exact algebra check, r14_inserted_audit_exact_checks.py
uses rational arithmetic and a unitary with phase exponents
$(0,0,1,2)$ modulo 4. All 256 projected superoperator entries agree
with $\operatorname{ad}_Q$, including 38 additional coincident
difference-phase pairs. Independently computed quantities give
$\|Q\|_{\rm HS}^2=8$,
$\|\operatorname{ad}_Q\|_{\rm HS}^2=64$, both sides of the triple
trace identity equal $49/36$, and both forms of the parameter
derivative equal $7/12$. The JSON output records these exact
checks. This is a check of the general identities, not an experiment
on the original small-parameter family.

## 6. Original spectral status

The calculation proves a fixed-time inserted asymptotic and excludes
an exact, unrestricted coboundary elimination, with a positive lower
bound for the physically scaled two-copy generator. It gives no
$o(1)$ estimate for the original weighted pair functional or for
the triple sum in (6.6). No sign relation between
$\operatorname{Tr}(QG)$ and the CUE deficit is established.

Thus the first original $H_2$ estimate remains unproved, and no
original countersequence has been obtained. The source keeps this
boundary explicit; the audit confirms it.

