> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_sampled_oscillatory_matrix.md`. Embedded SHA256: `984a61a6ced92576ac08cded3c86718f646d72376827271e6707dff39b18ab90`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: sampled oscillatory matrices and reverse paths

Round 5, 21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

## 1. Frozen source and verdict

Target: `root_oscillatory_matrix_cancellation.md`.
Its independently verified SHA-256 is

`ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d`.

The entire source was read and its proof reconstructed. The physical-kernel
input is supplied by `dual_physical_four_branch_kernel.md`, SHA-256

`0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c`,

which I also read and checked independently in
`audit_four_branch_physical_kernel.md`. No frozen source was changed.

**Verdict.** The sampled-matrix lemma is proved under its stated hypotheses.
The supplied physical-kernel proof verifies the listed input, so the resulting
bounds on (P_N) and (Q_N) hold for the actual original family along all odd

$$
N\longrightarrow\infty.
$$

There is no rate asserted for the vanishing operator norm, and this argument
does not prove the full pair form factor or (H_{\rm diag}). The separate
combinatorial interpretation of path-class multiplicities is outside the
target and outside this audit.

## 2. Sampled-matrix normalization and fourth Schatten power

For the target's matrix (T_N), removal of a boundary strip of width

$$
\epsilon
$$

changes at most (4\epsilon N^2+O(N)) entries of magnitude at most

$$
\|b\|_\infty/N.
$$

This proves the stated limiting Hilbert--Schmidt, hence operator, error

$$
2\|b\|_\infty\sqrt\epsilon.
$$

For the fixed cutoff, expanding (operatorname{Tr}(TT^*)^2) gives

$$
N^{-4}\sum_{x,x'\equiv a\ (4)\atop y,y'\equiv c\ (4)}
b_\epsilon(q,r)\overline{b_\epsilon(q',r)}
b_\epsilon(q',r')\overline{b_\epsilon(q,r')}
e^{2\pi iN\Omega(q,q',r,r')}.
$$

The ordering of conjugates and the signs of all four phase terms agree with
the target. The amplitude is smooth and supported strictly inside the four
dimensional cube, so extension to complete arithmetic progressions is exact.

For a Schwartz function (f), the one dimensional identity is

$$
\frac1N\sum_{x\equiv a\ (4)}f(x/N)
=\frac14\sum_{k\in\mathbb Z}e^{2\pi ika/4}
\int_{\mathbb R}f(q)e^{-2\pi iNkq/4}\,dq.
$$

It follows by periodizing (f) with spacing (4/N) and taking its Fourier
series at (a/N). Therefore the four dimensional prefactor is exactly

$$
4^{-4},
$$

the residue phase has a positive sign, and the additional phase in the
integral is (-k\cdot z/4). This is valid for every integer (N); divisibility
by four is not needed.

## 3. Alias control and the analytic zero alias

For (k\ne0), choose (j) with (K=|k_j|=|k|_\infty\ge1). The hypothesis
gives

$$
|\partial_j\Omega-k_j/4|\ge K/4-1/8\ge K/8.
$$

Every higher derivative of this phase is independent of (k). Repeated
integration by parts with the reciprocal first derivative therefore gives,
after six iterations,

$$
\left|\int B(z)e^{2\pi iN(\Omega-k\cdot z/4)}\,dz\right|
\le C_\epsilon N^{-6}(1+|k|_\infty)^{-6}.
$$

Differentiating a reciprocal introduces additional denominator factors; in
particular it does not degrade the displayed decay. The shell (K=j) in

$$
\mathbb Z^4
$$

has (O((j+1)^3)) lattice points, so the sum of all nonzero aliases is

$$
O_\epsilon(N^{-6}).
$$

This summation is uniform in the sixteen residue choices. For each fixed

$$
N
$$

the Poisson identity is legitimate for its smooth compactly supported
integrand; the displayed estimates then justify the uniform summation.

The identity

$$
\partial_q\partial_r\Omega=\partial_q\partial_r\phi(q,r)
$$

shows that the analytic cycle phase is nonconstant. Its domain can be
restricted to a connected rectangular neighborhood of the compact cube.
The hypothesis on the mixed derivative remains nontrivial there by analytic
continuation. At least one first derivative of (Omega) is a nonzero real
analytic function, so the critical set is contained in its zero set.

The target supplies the elementary zero-set argument, which is sufficient:
on a small product box expand in one variable, choose a coefficient which is
not identically zero, use induction in the remaining variables, and apply
Fubini to the nonzero one-variable analytic slices. Analytic continuation
rules out identically zero open boxes; a countable cover completes the
argument. Thus this critical set has measure zero.

After cutting off where (|\nabla\Omega|^2\le\delta), one integration by
parts gives (O_\delta(N^{-1})). The discarded integral is bounded by

$$
\int_{\{|\nabla\Omega|^2<2\delta\}}|B|,
$$

which tends to zero by dominated convergence. Take (N\to\infty) first,
then (\delta\downarrow0). This proves that the zero-alias integral tends
to zero without assuming nondegenerate stationary points or a quantitative
finite-type bound. Finally take the boundary width (\epsilon\downarrow0).
Since (|T|_{\rm op}\le|T|_{S_4}), the lemma follows.

## 4. Exact phase coefficients and the fixed tiny parameter

The ordinary-half symbol has

$$
a(q,p)=V(q)+\gamma R(q)e^{2\pi ip}
+\overline\gamma R(q)e^{-2\pi ip},\qquad
\gamma=e^{-i\alpha_0}/200.
$$

Its (R_8) coefficient is exactly (-1/4). Substitution of

$$
p_m^0=(-3q+r+m)/4
$$

therefore produces the unique coefficient

$$
\widehat{a(q,p_m^0)}(29/4,1/4)
=-e^{im\pi/2-i\alpha_0}/800
$$

on the four-torus, with normalized Fourier integral (1/16). The pure

$$
q
$$

term has zero (r)-frequency and the negative momentum exponential has

$$
r\text{-frequency }-1/4,
$$

so neither contributes. In the swapped term (a(r,p_n^0(r,q))), the only
possible nonzero (q)-frequencies are (\pm1/4); its coefficient at the
displayed frequency is zero.

The kernel construction proves that (S_m=\Phi_m-\Phi_m^0) is real
analytic, four-periodic, and

$$
\|S_m-ta(q,p_m^0)\|_\infty\le35000t^2,
\quad \|S_{m,q}\|_\infty\le350t,
\quad \|S_{m,r}\|_\infty\le50t.
$$

For distinct branches in the same orientation the coefficient of the
correction is

$$
-t e^{-i\alpha_0}(i^m-i^n)/800+e_{mn},
\qquad |e_{mn}|\le70000t^2.
$$

Its magnitude is at least (t/1600), since (|i^m-i^n|\ge\sqrt2) and

$$
t=10^{-80}/(2\pi),\qquad 70000t<1/1600.
$$

For every reversed branch pair, including (m=n), it is instead

$$
-t e^{im\pi/2-i\alpha_0}/800+e'_{mn},
\qquad |e'_{mn}|\le70000t^2,
$$

and the same lower bound holds. A nonzero off-axis Fourier coefficient
implies a nonzero mixed derivative: integration by parts multiplies that
coefficient by

$$
-(2\pi)^2(29/4)(1/4)\ne0.
$$

The nonperiodic initial difference is separable, namely

$$
(m-n)q/4\quad\text{or}\quad(mq-nr)/4,
$$

and hence disappears from the rectangular cycle. For the same-orientation
cycle the largest derivative bound is

$$
2(350+350)t=1400t<1/8.
$$

For a reversed cycle it is

$$
2(350+50)t=800t<1/8.
$$

Thus all twelve same-orientation cross terms and all sixteen reversed terms
meet every hypothesis of the sampled-matrix lemma. The argument keeps the
fixed parameter positive throughout; no limit (t\to0) is taken together
with (N\to\infty).

## 5. Transfer to the actual matrices and all-odd uniformity

The independently audited kernel approximation has per-column error

$$
O(N^{-1})
$$

and global Hilbert--Schmidt error (O(N^{-1/2})). Its four coefficients have
absolute value (1/2), and its amplitudes satisfy

$$
|B_m^2-1|\le40000t.
$$

Consequently both the approximate and the exact matrices have maximum entry

$$
O(N^{-1/2}).
$$

Multiplying the error entrywise by either matrix gives Hilbert--Schmidt
errors (O(N^{-1})) for both (P) and (Q). This step uses the stronger
column bound for the entry bound and the global Hilbert--Schmidt bound for
the product estimate; it does not replace a normalized norm by an
unnormalized one.

After splitting rows and columns modulo four, every root-of-unity
coefficient is constant on its block. Its remaining dependence on (N)
is only through

$$
\nu_N\in\{1,3,5,7\}.
$$

Thus there is a finite collection of phases, amplitudes, and residue blocks,
not an uncontrolled (N)-dependent amplitude family. The lemma applies to
their maximum and therefore to every odd (N\to\infty), including arbitrary
composite moduli.

The self-products in (P(V_N)) are

$$
\frac1{4N}\sum_{m=0}^3B_m^2.
$$

Their difference from (J_N) has each entry bounded by (40000t/N), hence
operator norm at most (40000t). All other terms tend to zero in operator
norm. Therefore

$$
\|P_N-J_N\|_{\rm op}\le40000t+o(1).
$$

The exact unitarity of (U_N) makes (P_N) doubly stochastic, giving

$$
P_NJ_N=J_NP_N=J_N,
\qquad P_N^n=J_N+(P_N-J_N)^n.
$$

For all sufficiently large odd (N), the restriction of (P_N-J_N) to
the (N-1) dimensional orthogonal complement of the constant vector has
norm at most (1/2). Even without normality, the trace bound

$$
|\operatorname{Tr}P_N^n-1|\le(N-1)2^{-n}
$$

follows by summing diagonal matrix coefficients of its (n)-th power in an
orthonormal basis.

Every term of (Q(V_N)) is a reversed branch term, so

$$
\|Q_N\|_{\rm op}\longrightarrow0.
$$

The exact matrix (Q_N(x,y)=U_N(x,y)\overline{U_N(y,x)}) is Hermitian.
If (max P_N\le C/N), then exact bistochasticity gives

$$
\|Q_N\|_{\rm HS}^2
=\sum_{x,y}P_N(x,y)P_N(y,x)\le C,
\qquad \operatorname{Tr}Q_N\le C.
$$

For large odd (N), spectral decomposition and (|Q_N|_{\rm op}\le1/2)
give, for (n\ge2),

$$
|\operatorname{Tr}Q_N^n|\le C2^{-(n-2)}.
$$

Since (sum_{n\ge2}n2^{-(n-2)}=6), the claimed all-time estimate is

$$
\sum_{n\ge1}n|\operatorname{Tr}Q_N^n|\le7C.
$$

The audited kernel even permits (C=9) after increasing the threshold in

$$
N.
$$

No first unproved estimate occurs inside the stated sampled-matrix or
physical-kernel conclusions. The unresolved step toward the original problem
is control of the remaining coherent path pairs, and ultimately all higher
factorial moments. A bound on the displayed (Q_N) powers is not such a
control and is not claimed to be one.
