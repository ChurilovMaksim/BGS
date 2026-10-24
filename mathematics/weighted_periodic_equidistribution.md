# Stability-weighted periodic equidistribution for the actual frozen map

Date checked: 2026-10-06. Repository inspected at `41a2788ef21e787e983e88a8b58470d104013740`.
Status: **proved corollary of the checked symbolic source, with the geometric boundary transfer proved below**. This is an external-theorem application and a direct transfer proof, not a claim of novelty or of quantum BGS. No canonical repository files were changed.

## 1. Exact conclusion and dependency boundary

Let

\[
G=S\circ\Phi_g^{\kappa},\qquad S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
\quad \kappa=10^{-80}/(2\pi),
\]

where `mathematics/fixed_model_symmetry_theorem.md` supplies the actual ordinary-midpoint symbol. For every fixed \(0<\alpha\le1\), there are constants \(C_\alpha,c_\alpha>0\), depending on the fixed map and exponent but not on \(n\) or the observable, such that

\[
\left|\sum_{G^nx=x}\frac{a(x)}{|\det(I-DG^n(x))|}
             -\int_{\mathbb T^2}a(x)\,dx\right|
 \le C_\alpha e^{-c_\alpha n}\|a\|_{C^\alpha},\qquad n\ge1. \tag{T}
\]

Here \(dx\) is normalized area and \(\|a\|_{C^\alpha}=\|a\|_\infty+[a]_\alpha\), for a fixed torus metric. Complex observables are allowed. In particular, the denominator sum is \(1+O(e^{-cn})\), and the associated normalized probability \(Q_n\) satisfies the same estimate. The constants are existential, not effective numerical bounds at the tiny fixed coupling.

The same statement applies in the inverse Egorov convention \(U_N^*\operatorname{Op}(a)U_N\sim\operatorname{Op}(a\circ F_\tau)\), where `fixed_model_symmetry_theorem.md` uses \(F_\tau=G^{-1}\). The forward convention for \(U_N(\cdot)U_N^*\) uses \(G\) itself. This is an exact inversion invariance of the weights and fixed-point sets, proved in Section 7; it is not a change of model.

Inherited project inputs, read but not independently recertified in full here:

- `BGS-FM-001`: the displayed map is smooth, area preserving, Anosov, and conjugate to the mixing toral automorphism \(S\).
- `BGS-FM-006`, Section 2: for \(\phi=\log\|DG|_{E^u}\|\), the Hölder potential \(\psi=-\phi\) has pressure zero and normalized area is its equilibrium/Gibbs measure. This retains that result's Ruelle entropy-inequality, smooth-volume entropy-formula and equilibrium-uniqueness dependencies.

The conclusion is valid much more generally for a topologically mixing, sufficiently smooth area-preserving Anosov diffeomorphism of a compact surface. No differentiable structural conjugacy, constant unstable Jacobian, or unweighted equidistribution is assumed.

## 2. Authenticated source contract

William Parry and Mark Pollicott, *Zeta functions and the periodic orbit structure of hyperbolic dynamics*, Astérisque 187–188 (1990), SMF published scan:

https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf

Local authenticated PDF SHA-256:

`4aebc8bf3afa919bedbd10bc2de18da2cbbdd0c310eccdb78d480072923c041a`

The scan has 273 physical pages and a digitization cover: physical PDF page = printed page + 5. It was downloaded and its extracted text read; the boundary and counting pages were also visually checked.

Exact source uses:

- Proposition 1.2 and ensuing paragraph, printed 14–16: bounded linear passage from two-sided Hölder potentials to cohomologous future potentials, with a weaker Hölder exponent.
- Theorem 2.2, Proposition 3.2 and Theorem 3.5: mixing finite-state Ruelle theory, Gibbs cylinder bounds and unique equilibrium.
- Proposition 4.10, printed 60: pressure derivative is equilibrium integration.
- Theorem 5.5(ii) **and its proof**, printed 81–84: locally uniform exponential approximation of periodic partition sums by the leading pressure exponential. The bare theorem statement describes series convergence; the exponential bound used here is in the proof.
- Appendix III.3, printed 227–230, especially 229: Hölder coding, unique coding off iterated boundaries, bounded fibres, and stable/unstable boundary invariance.
- Appendix III.9–III.11, printed 239–240: the exact periodic multiplicity correction. It is considered explicitly in Section 6, not silently discarded.

## 3. The marked symbolic estimate, including its norm dependence

Choose a sufficiently small Markov partition \(R_1,\ldots,R_k\), with coding
\(\pi:\Sigma_A\to\mathbb T^2\), \(\pi\sigma=G\pi\). There are \(C_0>0\), \(0<\rho<1\) with

\[
x_j=y_j\ (|j|\le r)\quad\Longrightarrow\quad
 d(\pi x,\pi y)\le C_0\rho^r. \tag{3.1}
\]

The transition matrix is primitive. Indeed, mixing of \(G\) makes
\(G^n(\operatorname{int}R_i)\cap\operatorname{int}R_j\ne\varnothing\) for all sufficiently large \(n\). In this open set choose an orbit segment avoiding the finitely many relevant preimages of partition boundaries, which are nowhere dense. Its itinerary gives an admissible length-\(n\) path from \(i\) to \(j\).

Put \(f=\psi\circ\pi\), and let \(\nu\) be its symbolic Gibbs measure. Its pressure is zero and \(\pi_*\nu=dx\). This is the coding version of the inherited area-equilibrium identification. To make the transfer explicit: the symbolic equilibrium is ergodic and full support; so is its pushforward, and Appendix III.3 makes the coding an almost-everywhere isomorphism for that measure. Its entropy therefore equals that of its pushforward, giving \(P_\Sigma(f)\le P_G(\psi)=0\). An invariant lift of area gives the reverse inequality by factor entropy monotonicity. Uniqueness on the base then identifies the pushforward with area.

For the fixed \(\alpha\), take a symbolic Hölder space \(\mathcal F_\theta\) sufficiently weak to contain both \(f\) and all \(A=a\circ\pi\), with

\[
\|A\|_\theta\le C_{\pi,\alpha}\|a\|_{C^\alpha}. \tag{3.2}
\]

The future-cohomology map from Proposition 1.2 is linear and bounded; therefore it does not introduce any uncontrolled dependence on \(a\). It preserves pressure, equilibrium integrals and periodic Birkhoff sums.

Define

\[
Z_n(h)=\sum_{\sigma^nx=x}e^{S_nh(x)},\qquad
E_n(h)=Z_n(h)-e^{nP(h)}.
\]

The proof of Theorem 5.5(ii) gives an open complex Hölder ball about the fixed real potential \(f\), and constants \(\varepsilon,C>0\), \(0<q<1\), such that

\[
\sup_{\|h-f\|_\theta\le\varepsilon}|E_n(h)|\le Cq^n. \tag{3.3}
\]

Here and below the radius can be decreased to place the closed ball inside the source's open ball. To spell out the exponential step: the proof replaces \(h\) by a potential \(h_v\) depending on \(v+1\) future coordinates, where \(v=\lfloor\eta n\rfloor\), preserving its leading eigenvalue and satisfying \(\|h-h_v\|_\infty\le K\theta^v\) uniformly. The resulting finite matrix has at most \(k^{v+1}\) eigenvalues and every eigenvalue other than the leading one has modulus at most a fixed \(r<1\). Its trace remainder is bounded by \(k^{v+1}r^n\). The approximation remainder is bounded by

\[
Cn\theta^v e^{n\varepsilon+Kn\theta^v} Z_n(f).
\]

Proposition 5.1 gives \(Z_n(f)\le C_\delta e^{\delta n}\) for any fixed \(\delta>0\), since \(P(f)=0\). First choose \(\eta>0\) with \(k^\eta r<1\), then sufficiently small \(\varepsilon,\delta>0\) with \(\theta^\eta e^{\varepsilon+\delta}<1\). Absorb the polynomial factor into a slightly weaker exponential. All constants are uniform in the potential ball. This is the needed strengthening of mere convergence of the series in the theorem statement.

For \(A\ne0\), apply Cauchy's derivative estimate to
\(z\mapsto E_n(f+zA)\) on \(|z|=\varepsilon/(2\|A\|_\theta)\). It gives

\[
|D E_n(f)[A]|\le (2C/\varepsilon)q^n\|A\|_\theta.
\]

The periodic set and its weight are shift invariant, so

\[
D Z_n(f)[A]
 =\sum_{\sigma^nx=x} e^{S_nf(x)}S_nA(x)
 =n\sum_{\sigma^nx=x} e^{S_nf(x)}A(x).
\]

Also \(D e^{nP(f)}[A]=n\nu(A)\), by pressure differentiation and \(P(f)=0\). Dividing by \(n\) gives

\[
\left|\sum_{\sigma^nx=x} e^{S_nf(x)}A(x)-\nu(A)\right|
 \le C_1q^n\|A\|_\theta. \tag{3.4}
\]

This is a one-mark estimate uniform over the whole Hölder unit ball. No differentiation of an uncontrolled pointwise big-O term is used.

## 4. A fixed-word avoidance bound for the invariant Gibbs measure

We need an exponentially small **weighted** boundary contribution, not merely zero Gibbs measure of boundaries.

For a fixed admissible word \(w\), there are \(C_w,\gamma_w>0\) such that

\[
\nu(\text{no occurrence of }w\text{ wholly inside }[0,N-1])
 \le C_we^{-\gamma_wN}. \tag{4.1}
\]

Here is a direct proof. The Gibbs property at pressure zero provides \(D\ge1\) with

\[
D^{-1}e^{S_tf(x)}\le\nu([v])\le D e^{S_tf(x)}
\]

for every length-\(t\) cylinder \([v]\) and \(x\in[v]\). The Bowen distortion constant

\[
V_f=\sup\{|S_tf(x)-S_tf(y)|:x_j=y_j\ (0\le j<t),\ t\ge1\}
\]

is finite: two-sided Hölder variations give a summable bound in the distance from the nearer endpoint.

Primitivity gives an integer \(H\), depending only on \(w,A\), such that every admissible prefix \(v\) has a length-\(H\) extension \(b(v)\) that contains \(w\). For \(x\in[vb(v)]\), \(y\in[v]\),

\[
\frac{\nu([vb(v)])}{\nu([v])}
 \ge D^{-2}\exp(-V_f-H\|f\|_\infty)=:p>0.
\]

Decrease \(p\) to at most one if necessary. After conditioning on any entire prefix, the probability that the next \(H\)-block avoids \(w\) is at most \(1-p\). Successive conditioning gives \((1-p)^{\lfloor N/H\rfloor}\), up to a harmless initial or terminal block. This proves (4.1). It requires no independence of blocks or unspecified mixing rate.

## 5. The geometric boundary correction, including non-period-preserving lifts

Write \(B=\bigcup_i\partial R_i\). This is closed and nowhere dense. Appendix III.3 supplies subsets \(B^s,B^u\) with

\[
B=B^s\cup B^u,\qquad G B^s\subset B^s,\qquad G^{-1}B^u\subset B^u. \tag{5.1}
\]

If a periodic orbit meets \(B\), its entire orbit lies in \(B\). For example, a visit to \(B^s\) keeps all future iterates there, and periodicity recovers every negative iterate as a future one; the argument for \(B^u\) is reversed. Define

\[
\mathcal B_n=\{y:G^ny=y,\ G^jy\in B\text{ for some }j\}.
\]

Thus every iterate of every \(y\in\mathcal B_n\) belongs to \(B\).

Choose a nonempty symbolic cylinder whose projection is contained in \(\mathbb T^2\setminus B\); this exists by continuity and surjectivity of \(\pi\), since the complement is nonempty open. Reindex this cylinder as a word \(w\) on coordinates \(0,\ldots,L-1\). The reindexing may move the time at which its projection avoids \(B\), which causes no difficulty: **every lift of every point in a boundary periodic orbit avoids \(w\) at every location**.

Let \(\epsilon_{\rm exp}>0\) be an expansivity constant for \(G\), and fix \(r\) with \(C_0\rho^r<\epsilon_{\rm exp}\). For each \(y\in\mathcal B_n\), choose any lift \(s_y\), without requiring \(\sigma^ns_y=s_y\), and its cylinder \(C_y\) on coordinates

\[
-r,\ldots,n+r-1.
\]

These cylinders are pairwise disjoint. Indeed, if two chosen lifts agree there, (3.1) gives \(d(G^jy,G^jz)<\epsilon_{\rm exp}\) for \(0\le j<n\). Since both geometric points are \(n\)-periodic, this extends to every integer \(j\), and expansivity implies \(y=z\).

Gibbs bounds, with only \(2r\) extra terms, give

\[
e^{S_n\psi(y)}=e^{S_nf(s_y)}
 \le D e^{2r\|f\|_\infty}\nu(C_y). \tag{5.2}
\]

Every \(C_y\) avoids \(w\) at each position wholly inside its defining coordinate interval. Sum (5.2) over the disjoint cylinders and use shift invariance and (4.1):

\[
\sum_{y\in\mathcal B_n}e^{S_n\psi(y)}\le C_2e^{-\gamma n}. \tag{5.3}
\]

This estimate expressly includes points whose shortest symbolic lifts have periods strictly larger than \(n\).

For symbolic \(n\)-periodic points projecting into \(\mathcal B_n\), use their distinct length-\(n\) cylinders on \([0,n-1]\). The same Gibbs bound and word-avoidance argument give

\[
\sum_{\substack{\sigma^ns=s\\\pi(s)\in\mathcal B_n}}e^{S_nf(s)}
 \le C_3e^{-\gamma n}. \tag{5.4}
\]

Outside \(\mathcal B_n\), the coding is one-to-one. Its unique lift is automatically \(n\)-periodic, because both \(s\) and \(\sigma^ns\) project to the same point. Hence the geometric and primary symbolic sums agree exactly off this exceptional set. By (5.3)–(5.4), for every bounded observable \(a\),

\[
\left|\sum_{G^ny=y}e^{S_n\psi(y)}a(y)
 -\sum_{\sigma^ns=s}e^{S_nf(s)}a(\pi s)\right|
 \le C_4e^{-\gamma n}\|a\|_\infty. \tag{5.5}
\]

Combining (3.2), (3.4), and (5.5) proves

\[
\sum_{G^ny=y} e^{-S_n\phi(y)}a(y)
 =\int a\,dx+O(e^{-c n}\|a\|_{C^\alpha}). \tag{5.6}
\]

Merely citing measure-zero boundaries would not prove (5.5); the fixed-word and padded-cylinder argument is the additional transfer step.

## 6. What happens to Manning's secondary presentations?

Appendix III.10 gives a signed finite combinatorial identity over the secondary symbolic presentations for the number of length-\(n\) codes above **each individual geometric fixed point**. Multiplying that pointwise identity by \(e^{S_n\psi(y)}a(y)\) gives the corresponding weighted marked identity, because every coding map intertwines the dynamics and every orbit sum pulls back to the same geometric orbit sum.

No assumption that a secondary presentation is mixing, or that its transfer operator has a simple isolated leading eigenvalue, is needed here. The **total signed secondary correction** is exactly the difference in (5.5), and the two positive exceptional sums in (5.3)–(5.4) bound its absolute value exponentially. Thus this proof controls the whole correction even if its individual presentation terms were handled inefficiently or had cyclic components. It does not assert an unproved spectral gap for each secondary presentation, and it never identifies all geometric period-\(n\) points with primary period-\(n\) codes.

The finite-to-one coding statement alone would not justify period preservation. That is why the proof of (5.3) deliberately uses arbitrary lifts, fixed-width cylinders and expansivity.

## 7. From unstable-Jacobian weights to stability determinants

At a point \(G^nx=x\), let \(\Lambda_n(x)\) denote the signed unstable eigenvalue of \(DG^n(x)\). In dimension two and with preserved area, the stable eigenvalue equals \(\Lambda_n(x)^{-1}\), and

\[
|\Lambda_n(x)|=J_n^u(x)=e^{S_n\phi(x)}.
\]

This identity is metric independent at a periodic point. Uniform hyperbolicity gives \(|\Lambda_n(x)|^{-1}\le C_he^{-\chi n}\). Exactly,

\[
\frac1{|\det(I-DG^n(x))|}
 =e^{-S_n\phi(x)}\bigl(1-\Lambda_n(x)^{-1}\bigr)^{-2}. \tag{7.1}
\]

The formula covers negative unstable multipliers as well. For sufficiently large \(n\), the parenthesis factor is \(1+O(e^{-\chi n})\), uniformly over all fixed points. Taking \(a=1\) in (5.6) shows the total unstable-Jacobian weight is bounded. Consequently replacing the weight in (5.6) by (7.1) changes its value by at most

\[
C e^{-\chi n}\|a\|_\infty.
\]

The finitely many smaller \(n\) are absorbed in the constant; hyperbolicity excludes zero determinants. This proves (T).

Write \(W_n(a)\) for its left-hand periodic sum and \(Z_n=W_n(1)\). The \(Z_n\) are positive and \(Z_n=1+O(e^{-cn})\). Therefore

\[
Q_n(a)=W_n(a)/Z_n,\qquad
|Q_n(a)-\textstyle\int a\,dx|\le Ce^{-cn}\|a\|_{C^\alpha}.
\]

There is at least one fixed point for every \(n\), since the actual map is conjugate to \(S\); hence normalization is defined even for the finitely many small periods.

Finally, \(\operatorname{Fix}G^{-n}=\operatorname{Fix}G^n\), and at such points

\[
|\det(I-DG^{-n})|
 =|\det(DG^n)^{-1}\det(DG^n-I)|
 =|\det(I-DG^n)|.
\]

Thus the entire periodic measure, not just its asymptotic, is identical for the forward convention \(G\) and the inverse convention \(G^{-1}\).

## 8. Product measures and the exact conditional input (EQ)

For the ordinary stability-weighted periodic-pair measure on the product map, the weight and normalization factor, so it is \(Q_n\otimes Q_n\). For every joint \(C^\alpha\) observable \(A(x,y)\),

\[
|(Q_n\otimes Q_n)(A)-(dx\otimes dx)(A)|
 \le 2Ce^{-cn}\|A\|_{C^\alpha}. \tag{8.1}
\]

Indeed, apply the one-variable estimate first to each section \(x\mapsto A(x,y)\), then to \(y\mapsto\int A(x,y)\,dx\); both relevant norms are bounded by a fixed multiple of the joint norm. This establishes the (EQ) required by `information-theory/shadow_tube_history_bridge.md`, Section 3, **provided its periodic-pair measure is the stated full product measure**.

If only coincident points are excluded, the conclusion is unchanged: the diagonal mass is exponentially small, since \(\max_x W_n(\{x\})\le Ce^{-\chi n}\) and \(W_n(1)=O(1)\). More elaborate exclusions or additional nonproduct orbit weights must be checked against their exact definition; they are not implicitly covered.

## 9. Scope and review recommendation

The source-to-target chain is now: checked uniform symbolic periodic trace estimate; bounded cohomology and Cauchy differentiation; direct exponential control of all boundary-periodic geometric and symbolic weights; exact determinant comparison; normalized/product consequences.

This resolves a classical missing input. It does not establish oscillatory quantum trace formulas at Heisenberg times, quantum history recombination, regulator removal, or deterministic local spectral statistics. No numerical computation is used as an asymptotic proof. Before promotion, an independent reviewer should particularly check the fixed-word boundary argument (Section 5), the uniform potential-ball estimate (Section 3), and the exact periodic-pair definition used by the downstream application.

## Explicit entropy-source correction

The independently checked entropy formula is Mañé (1981), printed p.95,
equation (2), read with the complete 1983 errata, pp.159–160. The original
Pesin 1977 Theorem5.1 locator remains unverified; no promotion of that locator
is implied. See the existing [alternate-source audit](../literature/smooth_area_entropy_supplement_20261006.md).
The PP complex-ball remainder/Cauchy and geometric boundary transfer are
covered by the new scoped independent review, retaining all norm quantifiers.

## Supporting-source promotion boundary

This source retains its own reviewed hypotheses. Its original verdict is distinct from
the separately reviewed combined S1–S9 interface or an intrinsic orbit
decomposition of the exact unitary. See record/weighted_support_promotion_mapping.json
for original bytes, source hashes and the execution-packaging map.
