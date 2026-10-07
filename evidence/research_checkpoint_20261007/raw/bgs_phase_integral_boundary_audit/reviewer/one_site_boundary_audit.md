# Independent one-site audit: standard versus boundary-corrected type-A CFT

## Claim and verdict

For arbitrary complex `a,b,c,d` with `|a|,|b|<1`, let `ζ` be Haar-uniform on `U(1)`, and set

\[
R(a,b,c,d)=\mathbb E\frac{(1-c\zeta)(1-d\zeta^{-1})}{(1-a\zeta)(1-b\zeta^{-1})}.
\]

The claim that the standard `N=1`, one-boson/one-fermion type-A color-flavor bulk integral equals this scalar ratio is **refuted**, already for `a=b=c=d=0`: the bulk is zero and the phase average is one. This is not merely a failure for an unrelated reproducing kernel. The specified determinant ratio itself fails the bulk-only identity.

The boundary-corrected functional of Zirnbauer (2021), equations (4.28)–(4.31), gives the correct ratio. For general sources, the separate bulk and surface parts diverge logarithmically when `cd≠0`; a common cutoff, or combining their integrands before taking the limit, is essential.

## Exact source and conventions

Primary source: Martin R. Zirnbauer, *Color-Flavor Transformation Revisited*, arXiv:2109.10272v1, September 21, 2021; [versioned source](https://arxiv.org/abs/2109.10272v1).

Local source PDF: `../sources/z21v1.pdf`.
SHA-256: `a275027f5b760a31a8c26b645fb0e73e97d9d7e15b2b23772691c7bdd771ba59`.

Exact checks: source equations (2.55), (4.3), (4.7)–(4.9), (4.15)–(4.21), (4.28)–(4.35); PDF page 30 was rendered and visually checked to disambiguate the normal derivative in (4.29). Section 4.4 verifies the corrected reproducing functional by Fock-basis orthogonality.

Use the source conventions

\[
Z=\begin{pmatrix}z&\alpha\\\beta&w\end{pmatrix},\qquad
\widetilde Z=\begin{pmatrix}\bar z&\gamma\\\delta&-\bar w\end{pmatrix},
\quad |z|<1,\quad w\in\mathbb C,
\]

\[
\partial_{Z,\widetilde Z}=\partial_\alpha\partial_\delta\partial_\gamma\partial_\beta,
\qquad G=\gamma\beta\alpha\delta,\qquad \partial_{Z,\widetilde Z}G=1.
\]

The flat even area measures satisfy the normalization in source (4.9). The overall constant is `π⁻²`.

Set `A=diag(a,c)`, `B=diag(b,d)`, with the bosonic entry first. Row/advanced sources act on the left of `Z`, and column/retarded sources act on the right: `Z↦AZB`. Thus the insertion in the requested convention is

\[
F=\operatorname{SDet}^{-1}(1-\widetilde Z A ZB).
\]

Take the source paper's `g^{-1}=ζ` if `A` is assigned to the `ζ` sector. The advanced/retarded naming can be exchanged together with `A↔B`, but source order must not be silently changed within a sector. The scalar formula is invariant under exchanging the two sectors. No restriction to real or paired-conjugate sources is used here.

## Direct phase integral

Expanding the denominators, absolute convergence follows from `|a|,|b|<1`. The four required Haar expectations are

\[
\mathbb E[(1-a\zeta)^{-1}(1-b\zeta^{-1})^{-1}]=(1-ab)^{-1},
\]
\[
\mathbb E[\zeta/((1-a\zeta)(1-b\zeta^{-1}))]=b/(1-ab),\quad
\mathbb E[\zeta^{-1}/((1-a\zeta)(1-b\zeta^{-1}))]=a/(1-ab).
\]

Consequently,

\[
R=\frac{1-bc-ad+cd}{1-ab}
 =1+\frac{(a-c)(b-d)}{1-ab}.
\]

## Grassmann calculation

Write

\[
t=|z|^2,\quad s=|w|^2,\quad q=ab,\quad r=cd,\quad u=bc,\quad v=ad,
\quad H=1+s,\quad J=1-qt.
\]

Let

\[
P=\gamma\beta,\quad Q=\alpha\delta,\quad
X=\gamma w\delta z,\quad Y=-\alpha\bar w\beta\bar z,
\quad L=P+Q+X+Y.
\]

Then `L²=2(1+ts)G`. From source (4.16),

\[
S=\operatorname{SDet}(1-\widetilde Z Z)
 =\frac{1-t}{H}-\frac{L}{H^2}+G\frac{1-s}{H^3}.
\]

Direct expansion of the inverse Berezinian gives

\[
F=\frac{1+rs}{J}
 +\frac{uP+vQ+qr(X+Y)}{J^2}
 +G\frac{qr(1+qt)}{J^3}.
\]

This polynomial expression in `c,d` avoids any spurious singularities from a temporary factor `1+cd|w|²` in a Schur-complement representation. The only bosonic-source denominator is `1-ab|z|²`, nonzero on the closed disk under the stated hypotheses.

Hence the bulk radial integrand is exactly

\[
C_4(t,s)=\partial_{Z,\widetilde Z}(SF)
 =\frac{(1-s)(1+rs)}{H^3J}
 -\frac{u+v+2qrts}{H^2J^2}
 +\frac{qr(1-t)(1+qt)}{HJ^3}.
\]

After the angular integrations, the bulk measure is `dt ds`.

## Boundary operator and surface integrand

The source (4.29) reads, in these conventions,

\[
\Omega=-\frac{L}{2H}
 +G\left(\frac1{2H^2}+\frac1{4H}\partial_\rho\right),
\qquad \rho=|z|.
\]

Crucially, `∂ρ` acts on `SF` before setting `ρ=1`. The degree-zero term `(SF)₀=(1-t)(1+rs)/(HJ)` vanishes on the boundary but its normal derivative does not.

At `t=1`, the degree-two multiplication part contributes `(1+rs)/(H²(1-q))`; the normal derivative contributes `−(1+rs)/(2H²(1-q))`. The nondifferential quartic term vanishes. Therefore

\[
\left.\partial_{Z,\widetilde Z}(\Omega SF)\right|_{t=1}
 =\frac{1+rs}{2H^2(1-q)}.
\]

The surface angular factor from `π⁻² d²w dθ` is `2 ds`, giving the surface radial integrand

\[
C_{\rm surf}(s)=\frac{1+rs}{(1+s)^2(1-q)}.
\]

## Exact common-cutoff formulas

Use the identical cutoff `|w|²≤T` for both pieces, and define

\[
\ell(q)=-\frac{\log(1-q)}{q},\qquad \ell(0)=1.
\]

Here `|q|<1`, so the analytic logarithm near `q=0` is unambiguous. Direct elementary integration yields

\[
I_{\rm bulk}(T)=
 (1-r)\ell(q)\frac{T}{(1+T)^2}
 +\frac{(2r-u-v)T/(1+T)-r\log(1+T)}{1-q},
\]

\[
I_{\rm surf}(T)=
 \frac{(1-r)T/(1+T)+r\log(1+T)}{1-q}.
\]

Adding first gives

\[
I_{\rm bulk}(T)+I_{\rm surf}(T)
 = (1-r)\ell(q)\frac{T}{(1+T)^2}
  +\frac{1+r-u-v}{1-q}\frac{T}{1+T}.
\]

Thus

\[
\lim_{T\to\infty}(I_{\rm bulk}(T)+I_{\rm surf}(T))
 =\frac{1+cd-bc-ad}{1-ab}=R.
\]

For `cd≠0`, the bulk behaves as `−cd log(1+T)/(1-ab)` and the surface as `+cd log(1+T)/(1-ab)`. Neither has an ordinary separate improper-integral value. Writing their sum requires the common regularization, exactly as source (4.35) does in its first divergent example.

## Decisive finite examples

1. `a=b=c=d=0`: `Ibulk=0`, `Isurf=1`, `R=1`.
2. `c=d=0`, arbitrary complex `|a|,|b|<1`: `Ibulk=0`, `Isurf=1/(1-ab)`, `R=1/(1-ab)`. In this whole family the boundary supplies the entire answer.
3. More generally `cd=0`: `Ibulk=−(bc+ad)/(1-ab)` and `Isurf=1/(1-ab)`. The scalar discrepancy is always nonzero.
4. `a=c`, `b=d` makes the original ratio identically one, but if `ab≠0` the bare bulk still diverges. Supersymmetric source cancellation does not repair the integration measure.

## Dependency and obligation summary

- Haar expectation and holomorphic domain: **passed**, direct geometric series.
- Berezinian and Grassmann ordering: **passed**, source conventions and independent exterior-algebra check script.
- Source insertion `AZB`: **passed**, advanced/retarded row/column assignment with `g^{-1}=ζ`.
- Boundary derivative interpretation: **passed**, visually checked source page and explicit action before restriction.
- Finite cutoff integration: **passed**, exact formulas above and symbolic derivative checks.
- Bulk-only equality: **failed**, explicit zero-source and `c=d=0` counterexamples.
- Boundary-corrected equality: **passed** for the scalar determinant ratio for all stated sources with common cutoff.
- Generalization to multiple sites/nontrivial propagation: **out of scope**.

Computation: run `python verify_one_site.py` in this directory. It constructs the inverse Berezinian from a direct 2×2 Schur complement in a four-generator exterior algebra, checks the displayed bulk and boundary coefficients, and verifies the finite-cutoff antiderivatives. This report and script are reviewer artifacts only; no canonical project files were changed.
