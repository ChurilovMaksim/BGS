# Resonant BGS sector: quantitative stability, arc-count criterion, and a sharp abstract obstruction

**Stable claim:** `BGS-TRACE-084`. **Integration review:** 16 October 2026, author check.

**Exact scope:** Sufficient selected-sector deletion criterion only; the sector need not vanish for a valid full signed local law.

Canonical status is [the claim ledger](../../record/claim_ledger.md); source `S04` is preserved verbatim in [the imported record](../../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s04). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../../archive/evidence/executions/20261016/chat-integration/receipt.json).


Research note, 14 October 2026. This is an independent in-chat derivation, **not** a claimed proof of BGS, and **not** a priority or peer-review claim. No repository mutations were made.

## Setup
Let `p` be an odd prime, `S=[[3,4],[2,3]]`, `d=ord_p(S)`, and

\[
U_p=e^{i\tau p A_p}M_p, \quad \tau=10^{-80}, \quad M_p^d=\zeta_p I,\quad C_{p,d}=\zeta_p^{-1}U_p^d.
\]

The physical torus symbol is

\[
\begin{split}
g(q,s)&=\cos(14\pi q)+r(q)/10 +r(q)\sin(2\pi q)/100\\
&\quad+r(q+1/2)\cos(2\pi s-\alpha)/100-1/10,\\
r(q)&=(1-\cos(14\pi q))(1+\cos(2\pi q)),\\
\cos\alpha&=-3/5, \quad \sin\alpha=4/5.
\end{split}
\]

Let `||X||_{2,p}^2=p^{-1}Tr(X^*X)` and

\[
E_p([a,b])=p^{-2}\sum_{r\ge1:ap\le rd\le bp}|\operatorname{Tr} C_{p,d}^r|^2.
\]

## Result I: strengthened finite-coupling coherent-return bound

For all primes `p>=19`, Weyl orthogonality and a finite rational Fourier calculation give exactly

\[
\frac1p\operatorname{Tr}A_p^2=\frac{66033}{160000}=:\sigma_g^2.
\]

If `m=rd`, set `V=\zeta_p^{-r}U_p^m`. Since `M_p^m=\zeta_p^r I`, unitary invariance and the telescoping identity imply

\[
\begin{split}
2\left(1-\operatorname{Re}\frac{\operatorname{Tr}V}{p}\right)
&=\|V-I\|_{2,p}^2=\|U_p^m-M_p^m\|_{2,p}^2\\
&\le m^2\|e^{i\tau p A_p}-I\|_{2,p}^2
\le m^2\tau^2p^2\sigma_g^2.
\end{split}
\]

Thus

\[
\frac{|\operatorname{Tr}C_{p,d}^r|^2}{p^2}
\ge\left(1-\frac12 m^2\tau^2p^2\sigma_g^2\right)_+^2.
\]

Because `d<=p+1`, `r=ceil(p/d)` gives `p<=m=rd<=2p`. Accordingly

\[
\boxed{E_p([1,2])\ge (1-2\sigma_g^2\tau^2p^4)_+^2.}
\]

For all primes `19<=p<=10^39` this is at least `0.9998349243130581`. This is finite-range information, **not** asymptotic disproof of `E_p -> 0`.

## Result II: mesoscopic arc-count criterion

Let `C` be *any* `p x p` unitary matrix with eigenangles `phi_j in R/Z`, and define the random-origin arc count

\[
N_C(x;\ell)=\#\{j: \phi_j\in[x,x+\ell)\pmod 1\},
\quad
V_C(\ell)=\int_0^1|N_C(x;\ell)-p\ell|^2\,dx.
\]

Parseval gives the exact identity

\[
\boxed{V_C(\ell)=2\sum_{r=1}^{\infty}
\left(\frac{\sin(\pi r\ell)}{\pi r}\right)^2
|\operatorname{Tr}C^r|^2.}
\]

Fix `0<a<b<infty`, put `B=max(1,b)` and `ell=d/(4Bp)`. For every integer `1<=r<=bp/d`, `0<r ell<=1/4`; hence `sin(pi r ell)>=2 r ell`. Thus

\[
V_C(\ell)\ge \frac{8\ell^2}{\pi^2}\sum_{1\le r\le bp/d}|\operatorname{Tr}C^r|^2,
\]

and the **nonasymptotic inequality**

\[
\boxed{E_p([a,b])\le 2\pi^2 B^2\,\frac{V_C(d/(4Bp))}{d^2}.}
\]

In particular, the family of assertions

\[
V_{C_{p,d}}(d/(4Bp))=o(d^2) \quad\text{for each fixed }b>0
\]

would prove the open prime-resonant sector `E_p([a,b])->0` for all fixed bands. A rate `V=O(d^{2-eta})` gives `E=O(d^{-eta})`, and an especially natural (but OPEN) Poisson-scale bound `V=O(d)` would give `E=O(1/d)`.

As a benchmark, for Haar `V in CUE(p)` and `C=V^d`, the exact CUE identity `E|Tr V^{rd}|^2=min(rd,p)` yields

\[
\mathbb E V_{V^d}(\ell)
\le p\ell(1-\ell)\le d/(4B).
\]

**Important qualification:** since eigenphases of `C` are `d phi_j(U)` modulo a common rotation, an arc of `C` of width `ell=d/(4Bp)` pulls back to `d` disjoint microscopic arcs of width `ell/d=1/(4Bp)` for `U`. The criterion is therefore a *comb of microscopic windows*, not an ordinary classical-scale Weyl law.

## Result III: sharp abstract counterexample to single-power nonreturn criteria

Let `(p,d)` be a sequence with `p->infty`, `d->infty`, and `R=p/d->infty`. Put `n=floor(p/sqrt(R))`, `P=p-n`. Define a **simple-spectrum** unitary `C_p` whose eigenphases consist of

\[
\left\{\frac{j}{P}:0\le j<P\right\}
\quad\cup\quad
\left\{\frac{k}{(n+1)p^2}:1\le k\le n\right\}.
\]

All phases are distinct; the empirical phase measures converge weakly to Haar measure on the circle because `n/p->0`. For every `1<=r<=bR`, the `P`-clock trace is exactly zero (eventually `r<P`) and the small packet contributes `n(1+o(1))` uniformly. Hence for every fixed `0<a<b`,

\[
\sup_{ap/d\le r\le bp/d}\frac{|\operatorname{Tr}C_p^r|}{p}
\sim \frac1{\sqrt R}\longrightarrow0,
\]

yet

\[
\boxed{\frac1{p^2}\sum_{ap\le rd\le bp}|\operatorname{Tr}C_p^r|^2\longrightarrow b-a\ne0.}
\]

Furthermore,

\[
\inf_{|\gamma|=1}\|C_p^r-\gamma I\|_{2,p}^2
=2\left(1-\frac{|\operatorname{Tr}C_p^r|}{p}\right)\to2
\]

uniformly in that band. These powers are maximally far (in normalized HS distance) from scalar operators, but **collective resonant energy does not decay**. The abstract example does not concern the prescribed BGS operator, but proves that no criterion based only on simple spectrum, macroscopic Haar equidistribution, absence of almost-scalar powers, and `max_r|Tr C^r|/p ->0` can establish (R).

## Numerical sanity checks (abstract packet example)

The calculations use the exact finite clock cancellation and explicit sums for the packet; arc-count variances are obtained by integrating the piecewise constant counting function.

| `p` | `d` | `R=floor(p/d)` | Packet `n` | `E([1/2,1])` | `max |Tr C^r|/p` | `V_C(d/(8p))/d^2` | Haar CUE expected `E` |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 199 | 9 | 22 | 42 | 0.48998733 | 0.21105525 | 0.1241188 | 0.04249893 |
| 4663 | 21 | 222 | 312 | 0.49693700 | 0.06690971 | 0.1248291 | 0.01790309 |
| 13729 | 48 | 286 | 811 | 0.49899930 | 0.05907204 | 0.1248157 | 0.00782957 |

## What is still open

No estimate `V_{C_{p,d}}(d/(4Bp))=o(d^2)` has been obtained for the actual fixed-coupling propagator. Since the arc criterion is a rational **comb of microscopic windows**, it still demands coherent dynamical control at Heisenberg times. Existing Weyl delocalization, spectral simplicity, one-step Egorov, and the checked selected-family WKB bounds do not imply this criterion. Moreover, controlling only the prime-resonant sector would not prove the all-order signed trace hierarchy or full BGS universality.

Existing BGS source: `mathematics/fixed-map/prime_resonant_sector.md` (Fejer-energy reduction and open sector theorem); `mathematics/open_questions.md` (TRACE-005). This note gives an alternate variance criterion and explicit abstract inverse obstruction, without claiming external priority.
