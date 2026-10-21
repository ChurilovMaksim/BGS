> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_four_branch_physical_kernel.md`. Embedded SHA256: `f2ae8cb525af0d957cfd59656bf4dce020404be80604d390c6800ca185b8e381`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exact four-branch physical kernel

Round 5, 21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

## 1. Frozen target and scope

I read the entire source
`dual_physical_four_branch_kernel.md`, whose independently checked SHA-256 is

`0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c`.

The companion `dual_four_branch_exact_checks.py` has SHA-256

`212d167395bb6ec2a4b7b9d996e9e2f9af1b8b9ebb3ebe67076a290c848679b3`.

I read and executed the companion: its 675 exact checks passed. The analytic
claims below are checked directly and do not follow from those finite tests.
No source was changed. The base checkpoint remains
`e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a`.

**Verdict.** The statements (1.3)--(1.6) of the target, including the original
modular-half convention, all odd moduli, fixed kick, and the stated norm
scales, follow from the supplied proof. I found no missing estimate in this
kernel construction. This audit does not infer spectral universality from a
one-step kernel approximation.

## 2. Exact symbol and all odd moduli

For odd (N), the representative ((N+1)/2) of the inverse of two gives,
for every pair of integers (k,l),

$$
e_N(k2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}.
$$

Thus the finite-shift formula in the target is exact with

$$
a_{k,l}=(-1)^{kl}c_{k,l},\qquad
(A_N\psi)(x)=\sum_{k,l}a_{k,l}
 e^{2\pi ik(x/N+l/(2N))}\psi(x+l).
$$

The sequence is periodically extended before applying this identity. It
continues to hold at wrapped shifts and at small odd moduli where different
Fourier modes alias; it is an identity of sums of operators, not a claim of
linear independence of their labels.

Only (l=\pm1) rows change. Consequently their (q)-factor is

$$
R(q)=r(q+1/2)=(1+\cos14\pi q)(1-\cos2\pi q),
$$

whereas the (q)-only factor stays unchanged. The support satisfies

$$
|k|+|l|\le9,\qquad \sum_{k,l}|a_{k,l}|\le1.18<2.
$$

Indeed the pure part is

$$
0.9\cos14\pi q+0.1\cos2\pi q
-0.05\cos16\pi q-0.05\cos12\pi q,
$$

with Fourier mass (1.1); the two remaining products have mass at most

$$
0.04+0.04.
$$

For the complex tube of width (2\cdot10^{-3}), coefficientwise
differentiation gives the target's bounds (200) for each first derivative
and (10000) for the induced infinity norm of the derivative of

$$
F=(-a_p,a_q).
$$

The second bound includes the sum of the two entries in each row: for example

$$
|a_{pq}|+|a_{pp}|
\le(2\pi)^2\sum |a_{k,l}|\,|l|(|k|+|l|)
 e^{2\pi(2\cdot10^{-3})(|k|+|l|)}
<10000.
$$

The other row is bounded in the same way. No unrecorded factor of two is
needed.

## 3. Exact Gauss splitting and gluing

The unique (\nu\in\{1,3,5,7\}) with (\nu N\equiv-1\pmod8) satisfies

$$
8^{-1}=\frac{1+\nu N}{8}
$$

with the canonical integer representative for every odd (N\ge3). The four
values of (\gamma_\nu(x)=e^{-3\pi i\nu x^2/4}) are

$$
(1,z_\nu,-1,z_\nu),\qquad z_\nu=e^{-3\pi i\nu/4}.
$$

Their normalized Fourier transform is exactly

$$
(g_0,g_1,g_2,g_3)=\tfrac12(z_\nu,1,-z_\nu,1).
$$

Expanding the modular quadratic phase gives the factors

$$
e^{-2\pi i(3x^2-2xy+3y^2)/(8N)}
\gamma_\nu(x)\gamma_\nu(y)e^{2\pi i\nu xy/4}.
$$

Reindexing its four-term Fourier expansion by (m=j+\nu y\pmod4) gives
the stated (d_{m,N}(y)) and proves (V_N(0)=M_N) exactly.

The Hamilton--Jacobi deck relations can also be verified at the level of the
initial polynomial. For example,

$$
\Theta_m(q+1,r)
=\Theta_{m-3}(q,r)+m/4-3/8+r/4.
$$

The same identity persists because (a) is periodic in (q). Adding (q)
to a phase shifts its momentum by one, so periodicity in (p) yields

$$
\Phi_{m+4}=\Phi_m+q.
$$

Translations by four in (q,r) similarly give exactly the last two
relations (5.1). Their additive terms coincide with those of (\Theta_m);
hence (S_m=\Phi_m-\Theta_m) is four-periodic. The transport equation and
initial value one imply the corresponding amplitude relations without
additive terms. Alternatively they follow directly by translating the flow
and its graph Jacobian.

The required coefficient relation is

$$
g_{s-3}=e^{2\pi i(Ns/4-3N/8)}g_s.
$$

It follows from the four displayed (g)'s and (N\equiv-\nu\pmod8).
Substituting (s=m-\nu y) leaves the extra exponent

$$
\frac{(N\nu+1)y}{4}\in\mathbb Z,
$$

which proves (5.3). Therefore shifting (x) to (x+N) in the complete
four-branch sum permutes its terms by (m\mapsto m-3), with exactly the
coefficient required for cancellation. Reducing that index modulo four adds
an integer multiple of (q) to the phase; on (q=x/N) its exponential is one.
Thus the complete approximate column is exactly (N)-periodic at every time.

There is no assertion that an individual branch is separately periodic. The
proof only needs the full column's periodicity, since (A_N) acts on its row
variable. No extra condition in the column parameter is necessary for the
residual calculation.

## 4. Analytic characteristic construction and constants

Use the real Hamiltonian (H=-a), so its flow is

$$
\dot Q=-a_p,\qquad \dot P=a_q.
$$

For (0\le s\le10^{-10}), the vector field and variational bounds imply

$$
|Q_s-u|,|P_s-p_0|\le200s,\quad
\|D(Q_s,P_s)-I\|_{\infty\to\infty}
\le e^{10000s}-1\le20000s.
$$

The graph tangent is ((1,-3/4)), of infinity norm one. Thus

$$
|J_s-1|\le20000s\le2\cdot10^{-6}.
$$

The real endpoint map is increasing and onto, because its difference from
the identity is bounded. It has an analytic inverse with uniform complex
neighborhoods. To make the latter assertion explicit, one may take initial

$$
|\operatorname{Im}u|,|\operatorname{Im}r|\le5\cdot10^{-4}.
$$

Then (p_0=(-3u+r+m)/4) has imaginary part at most (5\cdot10^{-4}),
and the flow displacement is at most (2\cdot10^{-8}), well inside the
larger (2\cdot10^{-3}) tube. On a slightly smaller endpoint tube, solving

$$
u=q-(Q_s(u,r,m)-u)
$$

in a complex disk of radius (4\cdot10^{-8}) is a contraction, with
derivative at most (2\cdot10^{-6}). This supplies the uniform local
analyticity and, by Cauchy estimates, each fixed derivative bound required
in the finite-shift remainder. Periodicity makes the estimates uniform
over real translates and all integers (m).

The action

$$
\Phi_m(s,q,r)=\Theta_m(u,r)+\int_0^s(P_v\dot Q_v+a(Q_v,P_v))\,dv
$$

has the signs appropriate to (H=-a). Integrating (P\,\delta\dot Q)
by parts cancels the interior variation; the initial momentum term cancels
the (u)-variation of (\Theta_m). At fixed endpoint this gives

$$
\Phi_q=P_s,\qquad \Phi_s=a(q,\Phi_q),\qquad
\Phi_r=u/4-3r/4.
$$

The last formula has no omitted evolution term. It is the boundary variation
of the initial action in the external parameter (r).

The graph Jacobian obeys

$$
\dot J_s=-[a_{pq}+a_{pp}\Phi_{qq}]J_s,
$$

so (B=J_s^{-1/2}>0) satisfies exactly

$$
B_s=a_p B_q+\tfrac12(a_{pq}+a_{pp}\Phi_{qq})B.
$$

The quantitative bounds then follow directly:

$$
|S_q|\le200s+\tfrac34(200s)=350s,
\qquad |S_r|\le200s/4=50s,
$$

$$
|S|\le2s,\qquad
|S-sa(q,p_0(q,r,m))|
\le\int_0^s200\cdot350v\,dv=35000s^2,
$$

$$
|B^2-1|\le\frac{20000s}{1-20000s}\le40000s.
$$

## 5. Residual, boundary use, and norm normalization

Set (h=(2\pi N)^{-1}). One shift is (q\mapsto q+2\pi hl), and its
Weyl midpoint factor is (e^{2\pi ik(q+\pi hl)}). For one branch,

$$
A_N(Be^{i\Phi/h})=e^{i\Phi/h}
\left[a(q,\Phi_q)B-ih\left(a_pB_q+
\tfrac12(a_{pq}+a_{pp}\Phi_{qq})B\right)+O(h^2)\right].
$$

In particular the midpoint, amplitude-shift, and phase-curvature terms are
respectively

$$
2\pi^2ihklB,\qquad 2\pi hlB_q,\qquad
2\pi^2ihl^2\Phi_{qq}B.
$$

They match (-ih\,a_{pq}B/2), (-ih\,a_pB_q), and

$$
-ih\,a_{pp}\Phi_{qq}B/2
$$

using the stated Fourier convention. The sign of the transport equation is
therefore correct. A Taylor remainder of the phase through degree two gives
an (O(h^2)) exponent error after division by (h); bounded third derivatives
and the real phases make this uniform. Only finitely many shifts occur, and
all derivatives needed are bounded on a fixed real neighborhood of the
sampled square and its shifted copies. A possibly large first derivative of
the quadratic phase only appears inside an exponential of modulus one.

The preceding exact periodic gluing justifies applying this branchwise
calculation to the entire discrete column across its boundary. Multiplication
by (i/h), followed by the Hamilton--Jacobi and transport equations, leaves
an entrywise residual

$$
|[(\partial_s-iA_N/h)V_N]_{xy}|\le Ch/\sqrt N.
$$

Its column norm is (Ch), not (Ch\sqrt N). Duhamel's formula uses the
unitarity of (e^{isA_N/h}) and gives

$$
\|(E_N(s)M_N-V_N(s))e_y\|_2\le Csh.
$$

Summing squared column norms yields (Csh\sqrt N) for the global
Hilbert--Schmidt norm. No estimate of an exponential by

$$
e^{s\|A_N\|/h}
$$

has been used. Constants are independent of (N,s,y); at the fixed original

$$
t=10^{-80}/(2\pi)>0
$$

the per-column and global errors are (O(N^{-1})) and (O(N^{-1/2})),
respectively.

Finally (sum_m|d_m|=2) implies the entry bound for (V_N), and the
per-column error bounds each entry error by (Cth). Therefore both (U_N)
and (V_N(t)) have maximum entry at most (3/\sqrt N) for all sufficiently
large odd (N). The elementary product identities for (P) and (Q) give

$$
\|P(U)-P(V)\|_{\rm HS},\ \|Q(U)-Q(V)\|_{\rm HS}
\le(\max|U|+\max|V|)\|U-V\|_{\rm HS}=O(N^{-1}).
$$

Transposition in the second product does not change the Hilbert--Schmidt
norm. This completes the claimed kernel input for the separately audited
oscillatory-matrix argument.

## 6. Scope boundary

These estimates hold for the original fixed parameter and all odd moduli.
They are uniform approximations for one application of (U_N), and their
physical-product errors are small in operator norm because they are small in
Hilbert--Schmidt norm. They do not license replacing (U_N^n) by independently
sampled transitions, iterating a one-step error to Heisenberg times without an
additional estimate, or identifying a moment limit. Those further steps are
not asserted in the audited target.
