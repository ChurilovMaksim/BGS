> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_return_audit_full_weight_cancellation.md`. Embedded SHA256: `f1d755d9f7a91988b03562ee471db1d5ebb12389eda03a1763335698ba29830d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: full-weight relative-path cancellation

Date: 21 October 2026. Auditor: Round 8 signed-resolvent branch.

## Source, conclusion, and scope

The full audited source is
`r8_weyl_full_weight_relative_path_cancellation.md`, SHA-256
`038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109`.
The source was not modified. The auditor independently derived the closed
relative-path factorization, the exact terminal phase, the local
Weyl-adjoint coefficient formula, and cancellation of the residual phase
before reading the completed source.

**Conclusion:** no mathematical defect was found. The source proves its
exact identities at all stated odd moduli and times. In particular,
each specified nonzero closed relative path has zero full signed
background sum. If $S^m-I$ is invertible modulo $N$, the complete
equal-endpoint sector of $|\operatorname{Tr}U_N^m|^2$ is exactly 1,
and every other endpoint sector is exactly one diagonal entry of the
full quantum Weyl-adjoint propagator raised to the power $m$.

This is a refinement of unitarity into precisely identified path
cancellations. It uses the actual full kick, without any truncation, but
also holds for any unitary replacing that kick. It does not prove the
CUE ramp or the required pair estimate. The source correctly states
this limitation and identifies the remaining coherent trace.

## 1. Exact coefficient identities and both half-phase signs

The convention is the original modular one,

$$
W(u)W(v)=e_N(\overline2\omega(u,v))W(u+v),
\quad \omega((k,l),(k',l'))=lk'-kl'.
$$

All calculations are in $(\mathbb Z/N\mathbb Z)^2$, with an
actual modular inverse of 2. The normalized Weyl expansion of a unitary
$E=\sum d(\eta)W(\eta)$ satisfies
$\sum|d(\eta)|^2=1$.

The coefficient of $W(\delta)$ in $E^*E$ is

$$
\sum_\eta\overline{d(\eta)}d(\eta+\delta)
e_N(-\overline2\omega(\eta,\delta)).
$$

Taking its complex conjugate proves
$F_d(\delta,\overline2\delta)=\mathbf1_{\delta=0}$.
The corresponding coefficient in $EE^*$, followed by conjugation,
proves $F_d(\delta,-\overline2\delta)=\mathbf1_{\delta=0}$.
Both signs in source Lemma 1 are therefore correct. No passage to
ordinary real halves is involved.

## 2. The relative-area expansion and the first differing site

Write $x_j=S^j\eta_j$, $a_j=S^j\delta_j$,
$A_{<j}=\sum_{i<j}a_i$, and $\Gamma=\sum_j a_j$.
Expansion of the quadratic area gives its constant term
$\mathcal A(\delta)$ and the linear term at site $j$

$$
\omega(A_{<j},x_j)+\omega(x_j,\Gamma-A_{<j}-a_j)
=\omega(2A_{<j}+a_j-\Gamma,x_j).
$$

Thus source equation (3.3) is exact. Multiplying by
$-\overline2$, reversing the alternating pairing, and transporting
by $S^{-j}$ gives exactly the argument

$$
S^{-j}A_{<j}+\overline2\delta_j-\overline2S^{-j}\Gamma
$$

of $F_d$ in (3.6). There is no interaction between the remaining
background labels after this expansion; the sum genuinely factorizes.

When $\Gamma=0$, the first nonzero $\delta_j$ has
$A_{<j}=0$, so its factor vanishes by the positive-half identity
from $E^*E$. If the relative path is identically zero, every local
factor is 1. This proves (3.5) for each relative path separately, with
no restriction on $m$, residue-label sizes, or factorization of $N$.

The transported three-site change $(h,-6h,h)$ is closed because
$S^2-6S+I=0$. If $h\ne0$, it is nonzero even over a composite
ring, since its first coordinate in the list of labels is $h$.
The theorem thus applies without an additional divisibility condition.

## 3. Terminal trace magnitude, including singular cases

For any matrix $V$, the trace of $B\mapsto VBV^*$ on full
matrix space is $|\operatorname{Tr}V|^2$. Computing this trace in
the normalized Weyl basis for $V=W(\lambda)M_N^m$ gives

$$
\operatorname{Ad}V(W(v))
=e_N(\omega(\lambda,S^mv))W(S^mv).
$$

Only fixed labels contribute to the trace. At a fixed label,
$S^mv=v$, and therefore

$$
|g_m(\lambda)|^2
=\sum_{v\in\ker(S^m-I)}e_N(\omega(\lambda,v)).
$$

There is no missing normalization factor: the trace is on an
$N^2$-dimensional matrix space, whereas the normalized Weyl inner
product makes each $W(v)$ have norm 1. If the kernel is trivial,
this trace magnitude is exactly 1 for every terminal label.

For a nontrivial kernel, the displayed character sum must remain inside
the background sum. The source explicitly preserves this case and does
not apply its constant-terminal-factor conclusion there. It consequently
does not overextend (3.5) into a weighted cancellation that has not been
proved.

## 4. The exact Cayley phase

Assume $R-I$ is invertible, with $R=S^m$, and set
$H=(R-I)^{-1}$, $C=(R+I)(R-I)^{-1}=I+2H$.
The identity $R^TJ R=J$, for the matrix of the alternating form,
implies $C^TJ+JC=0$. The source's multiplication by
$(R-I)^T$ and $R-I$ verifies this directly over the finite
ring. Thus $\omega(u,Cv)$ is symmetric, as needed for the
quadratic polarization.

Conjugation by $W(v)$, with $v=(I-R)^{-1}\lambda=-H\lambda$,
gives

$$
g_m(0)=e_N(-\overline2\omega(v,Rv))g_m(\lambda).
$$

Here $Rv=v-\lambda$, so
$\overline2\omega(v,Rv)=-\overline2\omega(\lambda,H\lambda)$.
Consequently

$$
g_m(\lambda)=g_m(0)e_N(Q_R(\lambda)),
\quad Q_R(\lambda)=-\overline4\omega(\lambda,C\lambda),
\quad |g_m(0)|=1.
$$

Polarization then yields

$$
g_m(\lambda)\overline{g_m(\lambda+\Gamma)}
=e_N\bigl(\overline2\omega(\lambda,C\Gamma)-Q_R(\Gamma)\bigr).
$$

The signs in (5.1)--(5.4), including the complex conjugation of the
second trace, agree with this independent calculation.

## 5. The local adjoint coefficient and cancellation of the global phase

Inserting the terminal phase into the relative-path background sum gives
the local argument $w_j+\overline2\delta_j$, with

$$
w_j=S^{-j}(H\Gamma+A_{<j}).
$$

To check the local factor independently, expand $E W(v)E^*$.
Its coefficient at $W(v-\delta)$ has $\eta' =\eta+\delta$
and the Weyl phase

$$
\omega(\eta,v)-\overline2\omega(\eta,\delta)
-\overline2\omega(v,\delta).
$$

This proves exactly

$$
C^E_{v-\delta,v}
=e_N(-\overline2\omega(v,\delta))
F_d(\delta,v-\overline2\delta).
$$

Setting $v=w_j+\delta_j$ gives

$$
F_d(\delta_j,w_j+\overline2\delta_j)
=e_N(\overline2\omega(w_j,\delta_j))
C^E_{w_j,w_j+\delta_j}.
$$

The definition of $w_j$ yields
$w_j+\delta_j=S w_{j+1}$ and
$w_m=w_0=H\Gamma$. The accumulated scalar phase is

$$
\sum_j\omega(w_j,\delta_j)
=\mathcal A(\delta)+\omega(H\Gamma,\Gamma)
=\mathcal A(\delta)+2Q_R(\Gamma).
$$

It cancels precisely the prefactor
$-\overline2\mathcal A(\delta)-Q_R(\Gamma)$. No residual phase
has been omitted and no absolute value has been taken prematurely.
The resulting product is therefore exactly

$$
\mathcal T_m(\delta)=\prod_j C^E_{w_j,S w_{j+1}},
$$

as asserted in (5.12).

## 6. The endpoint-sector sum is a coherent diagonal propagator entry

For fixed $\Gamma$, the inverse transformation is
$\delta_j=S w_{j+1}-w_j$, with $w_m=w_0=H\Gamma$.
Its accumulated transported displacement telescopes to
$(S^m-I)w_0=\Gamma$. It is therefore a bijection, not merely
an injection into a larger set of paths.

Since $C^U_{u,v}=C^E_{u,Sv}$, summing these products with the
endpoint fixed gives

$$
\sum_{\delta:\,\sum S^j\delta_j=\Gamma}\mathcal T_m(\delta)
=((C^U)^m)_{H\Gamma,H\Gamma}.
$$

The matrix $C^U$ is unitary on matrix Hilbert space, so each such
fully summed sector has modulus at most 1. This is a bound after all
the signed sums in that sector, but contains no small factor in $N$.

For $\Gamma=0$, the corresponding path starts at the identity
label. Unitality and trace preservation give zero coefficients for
transitions between that label and a nonzero Weyl label. Only the
identity path contributes, with weight 1. This is the operator meaning
of the first-differing-site cancellation; it does not produce the
Heisenberg-time ramp.

Summing all other sectors gives exactly the trace of $(C^U)^m$
on the traceless Weyl subspace. No Markov matrix, positivity assumption,
or independence of phases is introduced. The source correctly observes
that Cauchy--Schwarz gives only 1 for a remaining diagonal entry, while
the known entrywise tail combined with a column one-norm loses a factor
up to $N$.

## 7. Prime-power times and the separate $3^a$ check

The source's finite-field proof is valid for every odd prime. Writing
$S=3I+2J_0$, with $J_0^2=2I$, the commuting binomial expansion
in characteristic $p$ gives

$$
S^p=3I+2\varepsilon J_0,
\qquad \varepsilon=2^{(p-1)/2}\in\{1,-1\}.
$$

The stated elementary permutation proof gives
$2^{p-1}=1$, and the field has odd characteristic, so the last
assertion follows. The two outcomes are $S$ and $S^{-1}$.
Iteration makes $S^{p^a}$ one of these two matrices modulo $p$.
Both have determinant 1 and trace 6, so

$$
\det(S^{p^a}-I)\equiv-4\pmod p.
$$

It is a unit modulo $p^a$, and the inverse matrix is then supplied
by the adjugate formula. This proves the stated conclusion at
$m=N=p^a$. It is explicitly a family of times where the exact
terminal-factor calculation applies, not an asymptotic result claimed
for all odd dimensions.

For the other example, modulo 3 one has $S^2=-I$ and order 4.
At residues $m=1,3$, $\det(S^m-I)=2\pmod3$; at residue
$m=2$, the matrix $S^m-I=-2I$ is also invertible. At residue
0 it is not. Thus the stated three residue classes are exactly correct
for $N=3^a$.

## 8. Independent finite sign check

The accompanying standard-library script
`r8_return_full_kick_sign_check.py` performs a finite consistency check
with $N=3$, $m=3$, and a dense rational Householder unitary in
place of the kick. This choice gives several nonzero Weyl coefficients
and tests interference rather than a single-mode identity.

It directly builds the specified $M_N$, all Weyl matrices, all 729
background paths and 729 relative paths, their terminal trace factors,
and the Weyl-adjoint matrix. Independently formed expressions gave:

- largest closed-relative-path error: less than $7\times10^{-16}$;
- largest full-sector versus adjoint-path error: less than
  $2.3\times10^{-15}$;
- largest Cayley trace-phase error: less than $2\times10^{-15}$;
- total trace-square reconstruction error: less than
  $1.4\times10^{-14}$.

This check is supplementary verification of signs and indexing in a
general algebraic identity. It is not an asymptotic experiment on the
original family and is not a substitute for the proofs above.

## 9. The exact unresolved estimate remains unresolved

For $k=2$, the original criterion still requires, for every admissible
fixed $b$,

$$
N^{-2}\sum_{m\ge1}|\widehat b(m/N)|^2
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0.
$$

The normalization here is correct: the two nonzero Fourier signs cancel
the factor $1/2$ in the unordered pair moment. The preceding exact
identities do not control this weighted sum, even on the prime-power
sequence. The equal-endpoint value 1 is only one component of the trace
square; it cannot be compared to the complete CUE value to infer a
defect for the original family.

The audit approves all stated exact identities and their explicit scope.
It does not certify an additional signed-sum estimate or a solution of
$H_{\rm diag}$.
