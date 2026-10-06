# Independent audit: stability-weighted periodic equidistribution

Date: 2026-10-06. Review workspace only; no canonical files edited.

## Claim and primary verdict

**Verdict: proved as written.** This verdict concerns the mathematical statement
and application in Sections 1–8 of the frozen candidate identified below. It is
an independent internal proof/source audit, not an external referee certificate.
The original Pesin 1977 theorem-number locator is **not** newly verified; the
entropy input is independently verified through the alternate primary proof by
Mañé 1981, together with its mandatory 1983 errata. That provenance distinction
must be retained when this result is integrated.

The reviewed source is
`bgs_weighted_periodic_source_check/weighted_periodic_equidistribution.md`,
SHA256 `c3cfabab0ab190ea164871a536f044a1db262867f798b37e66720c143b4d9fbb`.

For the literal smooth area-form-preserving map
\(G=S\circ\Phi_g^{10^{-80}/(2\pi)}\), with the ordinary-midpoint symbol of
FM-001, and each fixed \(0<\alpha\le1\), there are constants
\(C_\alpha,c_\alpha>0\) such that, simultaneously for every complex
\(a\in C^\alpha(\mathbb T^2)\) and every integer \(n\ge1\),

\[
\left|\sum_{G^nx=x}\frac{a(x)}{|\det(I-DG^n(x))|}-\int a\,dx\right|
\le C_\alpha e^{-c_\alpha n}\|a\|_{C^\alpha}.
\]

Here fixed points, including points whose least period divides \(n\), are counted
once each; there is no division by orbit length. Area is normalized to one.
Constants depend on the fixed map, exponent, metric and chosen coding, but not
on the observable or period. They are existential, not numerical startup bounds.

There is no remaining mathematical gap in this claim. In particular, the proof
does not require a geometric period-\(n\) point to have a primary symbolic
period-\(n\) lift, and its use for \(N\)-dependent tests is genuinely norm-uniform.
The pair result remains limited to the specified full product measure, or its
off-diagonal conditioning; it does not identify a differently weighted or
restricted pair ensemble.

## Dependency graph

1. Literal symbol and FM-001 Section 3.1: smoothness, invariant area, Anosov
   splitting, and topological conjugacy to the hyperbolic toral automorphism.
2. Mixing of that automorphism, hence of \(G\); a sufficiently small Markov
   partition then has a primitive primary adjacency matrix.
3. Ruelle's entropy upper bound plus the smooth-volume entropy formula;
   PP's symbolic Gibbs/uniqueness theorem and almost-everywhere injective coding:
   \(f=-\log J^uG\circ\pi\) has symbolic pressure zero and Gibbs measure projecting
   to area.
4. PP Proposition 1.2 and bounded future-cohomology map; Lemma 5.3,
   Corollary 5.3.1, and the proof of Theorem 5.5(ii): a uniform complex-potential
   ball has exponentially small periodic-partition remainder.
5. Complex Cauchy differentiation and Proposition 4.10: a one-mark estimate in
   the full Hölder norm, uniformly in the direction being differentiated.
6. Markov boundary invariance, a fixed forbidden word, Gibbs cylinder ratios,
   and padded-cylinder injectivity from expansivity: exponentially small total
   geometric and symbolic boundary weights.
7. The exact surface determinant identity and uniform hyperbolicity: replace
   unstable-Jacobian weight by the desired stability determinant.
8. Positive normalization, factorization, and a diagonal atom estimate: inverse
   map, normalized measure and precisely stated product-measure consequences.

No edge uses a quantum trace estimate, a differentiable structural conjugacy,
constant unstable expansion, unweighted periodic equidistribution, or the theorem
being proved. The full symmetry classification and pressure-growth conclusions
of FM-001/FM-006 are outside this dependency closure and were not recertified.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Frozen bytes and inherited source identities | Passed | All three project-source hashes match the author's manifest |
| Actual fixed-coupling dynamical hypotheses | Passed, scoped | FM-001 Section 3.1 reassembled; exact finite Fourier derivative budget checked independently |
| Hölder potential and observable pullback | Passed | Fixed hyperbolic splitting regularity; coding gives a bounded linear pullback |
| Primitive primary coding | Passed | Mixing open interiors plus finite avoidance of nowhere-dense boundaries |
| Pressure zero and area Gibbs measure | Passed | Ruelle plus checked Mañé+errata; explicit entropy/lift argument below |
| Original Pesin 1977 Thm5.1 locator | Conditional as a citation | Original PDF still unretrieved; not needed after explicit alternate-source verification |
| Uniform complex-ball exponential remainder | Passed | PP Lemma 5.3/Corollary 5.3.1 and pp.82–84, with both Hölder losses tracked |
| Cauchy differentiation uniform in the test | Passed | Radius inversely proportional to the test norm; no observable-dependent hidden constant |
| Boundary word-avoidance estimate | Passed | Uniform conditional cylinder ratio; no independence assumption |
| Geometric points without period-preserving lifts | Passed | Arbitrary lifts and fixed-width padded cylinders; geometric expansivity supplies injectivity |
| Symbolic multiplicities and secondary presentations | Passed | Two positive boundary sums bound the complete signed correction |
| Stability denominator and inverse-map convention | Passed | Exact determinant-one two-dimensional identities |
| Small periods and normalized measure | Passed | Hyperbolicity, finiteness, and conjugacy to \(S\) |
| Full product and diagonal removal | Passed, exact scope | Tensorization and exponentially small maximal atom |
| Quantum weights, arbitrary exclusions, full TRACE-005 | Out of scope | No implication asserted by this classical audit |

## 1. Inherited actual-map inputs

The checked project files retain their original hashes:

- `fixed_model_symmetry_theorem.md`:
  `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`.
- `nonlinear_bracket_pressure.md`:
  `311ec9ba6d0fc8dc942103971d191db4364d7b21b9d616911312320fdc8ba3c1`.
- `shadow_tube_history_bridge.md`:
  `12e72992e2c81fc542e390b3f42aabde805c0c27b35c3b8b57d73a5251d67059`.

For FM-001, the Hamiltonian flow of its finite trigonometric symbol is smooth,
complete and area-form preserving; \(\det S=1\). The independently executed
`finite_checks.py` reconstructs the **ordinary-midpoint** symbol, including the
\(r(q+1/2)\) term, using exact rational complex coefficients. It obtains 32
nonzero modes, no constant mode, and
\(\sum (|\Re c_v|+|\Im c_v|)|v|^2=51451/1000\), with \(|v|<10\).
Using the rational upper bound \(\pi<22/7\) verifies the displayed derivative
budgets \(400,3000,200000\). This finite check supports those coefficients only.

The variational-equation bound, invariant cones, and split Green inverse in
Section 3.1 then apply throughout the stated small-\(\kappa\) range and hence at
the actual frozen parameter. The conjugacy's injectivity proof correctly uses
small integer lift discrepancies and bounded two-sided orbits of a hyperbolic
linear map. It does not assume differentiability of the conjugacy. A hyperbolic
toral automorphism is topologically mixing: Fourier correlations of any two
trigonometric polynomials eventually decouple, and positive-measure open sets
then give topological mixing. Conjugacy transfers it to \(G\).

The unstable line of a smooth Anosov map is Hölder. In this particular cone
construction this can also be seen by the slope graph transform: its uniform
fiber contraction \(q<1\) remains contracting in a sufficiently small Hölder
exponent \(\beta>0\) once \(q\operatorname{Lip}(G^{-1})^\beta<1\). Thus
\(\phi=\log\|DG|_{E^u}\|\) is a fixed real Hölder potential. No regularity
exponent depending on the test is necessary.

### Entropy, pressure and area

Ruelle's1978 Theorem 2, printed pp.84–85, was read directly at the author's
primary PDF. It applies to all invariant probabilities, not only ergodic ones.
The compact smooth map has one positive Lyapunov exponent, whose integral is
\(\int\phi\,d\mu\). Hence \(h_\mu(G)\le\int\phi\,d\mu\).

The original Pesin 1977 Math-Net PDF remains unavailable in this pass; the
historical audit recorded 403 and the present direct retrieval timed out. No
claim is made to have checked its Theorem 5.1/p.81 locator. Instead I read the
cached published primary sources:

- Mañé, *A proof of Pesin's formula*, ETDS 1 (1981), 95–102,
  DOI `10.1017/S0143385700001188`, printed p.95 equation(2) and its surrounding
  hypotheses. The assumption is an invariant absolutely continuous probability
  for a diffeomorphism of a compact boundaryless manifold with Hölder derivative.
- Mañé, *Errata to “A proof of Pesin's formula”*, ETDS 3 (1983), 159–160,
  DOI `10.1017/S0143385700001863`, both pages. The corrections replace an
  intermediate bound by \(\beta^n\) and make two graph-transform smallness
  conditions explicit. They do not change the entropy formula or its hypotheses.

The actual map and normalized area meet these hypotheses. Birkhoff averaging
of the one-dimensional unstable logarithmic expansion identifies the integral
of the positive exponent with \(\int\phi\,dx\), without assuming ergodicity.
Thus \(h_{dx}(G)=\int\phi\,dx\).

There is a direct noncircular verification of the symbolic measure used in the
candidate. Let \(\nu\) be the unique equilibrium/Gibbs state of
\(f=-\phi\circ\pi\) on the primitive coding. It is ergodic and full support, so
its pushforward is also ergodic and full support. PP Appendix III.3 makes the
factor map injective almost everywhere for this pushforward. Consequently
\(h_\nu(\sigma)=h_{\pi_*\nu}(G)\), and Ruelle's bound gives
\(P_\Sigma(f)\le0\). Conversely lift area to an invariant symbolic probability
\(\widetilde{dx}\): a probability lift exists for a compact continuous
surjection, and Cesàro averaging produces an invariant one. Factor entropy
monotonicity and the entropy formula give
\[
h_{\widetilde{dx}}(\sigma)+\int f\,d\widetilde{dx}
\ge h_{dx}(G)-\int\phi\,dx=0.
\]
The symbolic variational principle therefore gives \(P_\Sigma(f)=0\), and
uniqueness gives \(\widetilde{dx}=\nu\) and \(\pi_*\nu=dx\). This argument
does not need to assume area ergodicity in advance or use an unproved
pressure-preservation assertion at boundary measures.

## 2. Exact symbolic source and uniform marked estimate

The retained PP 1990 PDF is the published SMF scan, 273 physical pages, SHA256
`4aebc8bf3afa919bedbd10bc2de18da2cbbdd0c310eccdb78d480072923c041a`.
The official SMF PDF was also opened for authentication. In this precise file,
**one-based physical PDF page = printed page +5**. Critical source pages were
read as extracted text and pp.79,82,229,240 were inspected visually.

Exact locators are:

- Proposition 1.2, pp.14–15; the bounded linear future map is explicit on p.16.
- Theorem 2.2, p.21; Proposition 3.2 and Corollary 3.2.1, pp.37–39; Theorem 3.5,
  pp.42–43.
- Proposition 4.7, p.57; Proposition 4.8, p.59; Proposition 4.10, p.60.
- Proposition 5.1, pp.74–75; Lemma 5.3, pp.78–79; Corollary 5.3.1, pp.79–80;
  Theorem 5.5(ii) and proof, pp.81–84.
- Appendix III.3 proposition/theorem/proof, pp.227–230; boundary facts p.229.
- Appendix III.9–III.11, pp.239–240; longer-period lifts are explicitly discussed
  on pp.238–239, and Manning's pointwise identity is on p.240.

Some inherited external-registry PDF-page references use the older +4 offset;
they should not be copied for this scan. The reviewed candidate itself gives
the correct +5 offset. Its p.60 pressure-derivative locator is correct.

### Track both Hölder losses

Choose a two-sided space \(\mathcal F_{\theta_0}\) containing the fixed \(f\)
and all pullbacks \(A=a\circ\pi\), with
\(\|A\|_{\theta_0}\le C_{\pi,\alpha}\|a\|_{C^\alpha}\).
PP's bounded linear map
\(W:\mathcal F_{\theta_0}\to\mathcal F^+_{\theta_1}\),
\(\theta_1=\sqrt{\theta_0}\), produces future potentials modulo coboundaries.
The proof of Theorem 5.5(ii) uses spectral perturbation on the still weaker
space \(\mathcal F^+_{\theta_2}\), \(\theta_2=\sqrt{\theta_1}\).
Thus the successive losses can be \(\theta_0,\theta_0^{1/2},\theta_0^{1/4}\),
all fixed below one. The candidate's reuse of the letter \(\theta\) suppresses
this notation only; no claimed same-norm bounded cohomology map is needed.

At the fixed real future potential \(g_0=Wf\), pressure is zero and the leading
eigenvalue is1. Shrink a strong-norm ball about \(g_0\). The source constructs
locally constant \(g_v\), with a finite-coordinate eigenfunction of eigenvalue
\(e^{P(g)}\), such that, uniformly over that ball,
\[
\|g-g_v\|_\infty\le K\theta_1^v,
\qquad
\|g-g_v\|_{\theta_2}\le K'\theta_1^{v/2}.
\]
The second estimate places \(g_v\) in one fixed spectral neighborhood for all
sufficiently large \(v\). On that neighborhood the nonleading spectrum has
modulus at most one fixed \(r<1\). The finite-coordinate restriction inherits
that bound; its leading eigenvalue has multiplicity one. Its dimension is at
most \(k^{v+1}\). The periodic trace identity gives a remainder bounded by
\(k^{v+1}r^n\).

For the approximation error use positivity of the fixed real reference:
\[
|Z_n(g)-Z_n(g_v)|
\le Kn\theta_1^v\exp(n\varepsilon+Kn\theta_1^v)Z_n(g_0).
\]
Proposition 5.1 gives \(Z_n(g_0)\le C_\delta e^{\delta n}\) for every fixed
\(\delta>0\). Choose \(v=\lfloor\eta n\rfloor\) with \(k^\eta r<1\), then
choose the potential-ball radius and \(\delta\) small enough that
\(\theta_1^\eta e^{\varepsilon+\delta}<1\). Polynomial factors and the finite
initial range are absorbed into fixed constants. This proves a common
\(Cq^n\) bound, \(q<1\), for the **whole complex ball**, rather than merely
pointwise convergence of the series in the theorem statement.

Boundedness of \(W\) pulls that neighborhood back to an actual complex ball
about \(f\) in the original two-sided space. Periodic sums and pressure are
unchanged by its coboundaries. For
\(E_n(h)=Z_n(h)-e^{nP(h)}\), Cauchy's inequality on the circle
\(|z|=\varepsilon/(2\|A\|_{\theta_0})\) gives
\[
|DE_n(f)[A]|\le (2C/\varepsilon)q^n\|A\|_{\theta_0}.
\]
Shift invariance of the finite periodic sum gives
\(DZ_n(f)[A]=n\sum_{\sigma^ns=s}e^{S_nf(s)}A(s)\).
Pressure differentiation gives \(D(e^{nP})(f)[A]=n\nu(A)\).
The real directional source formula extends complex-linearly. Division by
\(n\) therefore proves the required uniform marked estimate. All choices
precede the selection of \(A\); an \(N\)-dependent test introduces only its
displayed Hölder norm.

## 3. Boundary multiplicities and non-period-preserving lifts

For the actual Markov partition, its stable boundary union maps into itself
under \(G\), and its unstable boundary union maps into itself under \(G^{-1}\).
Thus if a geometric periodic orbit ever meets the partition boundary \(B\),
all its points lie in \(B\). This uses periodicity essentially.

There is a finite symbolic cylinder whose projection lies in the nonempty open
complement of \(B\). After shifting its finite coordinate interval to a word
\(w\), every lift of every boundary periodic orbit avoids \(w\) everywhere.
The shift might change which physical time avoids \(B\); an entirely boundary
orbit is still excluded. No positivity of the distance from every nonboundary
periodic orbit to \(B\) is assumed.

For the fixed real Gibbs measure, primitivity supplies a common extension
length \(H\) which allows \(w\) after any admissible prefix. The two-sided
Bowen variation bound and Gibbs bounds give a lower conditional probability
\(p\ge D^{-2}e^{-V_f-H\|f\|_\infty}>0\). Conditioning successively on finite
prefixes bounds avoidance over length \(N\) by
\(C(1-p)^{\lfloor N/H\rfloor}\). Overlaps between words do not matter because
it suffices to count the prescribed nonoverlapping extension opportunities.
There is no independence or unspecified mixing-rate step.

Now choose a fixed padding \(r\) so that coding agreement on a symmetric
\(2r+1\) window forces physical distance below an expansivity constant. For
each geometric boundary point fixed by \(G^n\), choose **any** lift, and its
cylinder on \([-r,n+r-1]\). Two distinct geometric points cannot give the same
cylinder: they would remain close for times 0 through \(n-1\), and their
geometric \(n\)-periodicity would extend this to all integer times, contradicting
expansivity. The cylinders are consequently disjoint, whether or not the
chosen lifts are periodic at all. Gibbs gives
\[
e^{S_n\psi(y)}\le D e^{2r\|f\|_\infty}\nu(C_y).
\]
Their union is contained in the corresponding fixed-word-avoidance event.
The total geometric boundary weight is therefore exponentially small.

For primary symbolic \(n\)-periodic lifts into the boundary, distinct sequences
have distinct length-\(n\) cylinders, since their entire sequences repeat those
\(n\) entries. The same Gibbs/avoidance comparison bounds their total weight
exponentially. Off the geometric boundary-orbit set the lift is unique and
automatically fixed by \(\sigma^n\). The difference of the two complete marked
sums is bounded by the two **positive** exceptional weight sums times
\(\|a\|_\infty\).

This addresses both directions of the multiplicity problem: extra primary
period-\(n\) lifts, and geometric fixed points with no primary period-\(n\)
lift. Finite-to-one coding alone would not address the latter.

Manning's Appendix III.10 identity is pointwise over each geometric fixed point.
It can be multiplied by its common geometric weight and mark. Its total signed
secondary correction equals precisely the difference just bounded. Individual
secondary presentations need not be mixing, need not have a simple leading
eigenvalue, and need not receive separate pressure-gap assertions. The proof
does not depend on such assertions or discard a possibly cancelling correction.

## 4. Stability weights, normalization and downstream norm budget

At a geometric fixed point of \(G^n\), write \(\Lambda\) for its signed real
unstable multiplier. The actual map has determinant 1, so its stable multiplier
is \(\Lambda^{-1}\), and
\[
|\det(I-DG^n)|=|\Lambda|(1-\Lambda^{-1})^2,
\qquad |\Lambda|=e^{S_n\phi}.
\]
This identity includes negative multipliers; the square and absolute value are
correct. At a periodic point a choice of metric cannot alter the multiplier.
Uniform hyperbolicity gives \(|\Lambda|^{-1}\le C_he^{-\chi n}\). The correction
factor is therefore \(1+O(e^{-\chi n})\) uniformly at all sufficiently large
periods. The already established marked formula at \(a=1\) bounds total
unstable-Jacobian mass. Hence replacing all weights incurs
\(O(e^{-\chi n}\|a\|_\infty)\), with no exponential point-count loss.
Hyperbolicity makes the remaining finite-period fixed-point sets finite and
their denominators nonzero, so one common constant handles them.

The resulting positive mass is \(1+O(e^{-cn})\), and the actual conjugacy to
\(S\) ensures a nonempty fixed-point set for every \(n\). Normalization is
legitimate. The determinant relation for \(DG^{-n}=(DG^n)^{-1}\) at the same
fixed point proves exact equality of forward and inverse weighted measures.

For a joint Hölder test, both its sections and the area average of its sections
have norm bounded by the joint norm (up to the fixed choice of product metric).
Successive one-variable applications give the stated product estimate. The
maximal normalized atom is \(O(e^{-\chi n})\), so the product diagonal mass is
at most that maximum. Removing and renormalizing the diagonal preserves the
estimate. The actual \(S\)-conjugate model has at least four points fixed by
each iterate, so this conditioning is never empty.

In particular, for \(n\ge\tau_0N\), any family with
\(\|a_N\|_{C^\alpha}=e^{o(N)}\), including polynomially growing oscillatory
test norms, has exponentially small equidistribution error after allowing a
slightly weaker exponent. If only an \(e^{KN}\) bound is known, the error is
not automatically small: one needs \(K<c_\alpha\tau_0\). The theorem does not
bound its own application to arbitrary exponentially growing tests. This
preserves the precise sublinear-history budget in the older shadow-tube note.

## Source checks, reproducibility and final boundary

Primary URLs:

- PP 1990: https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf
- Ruelle 1978: https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B51%5D.pdf
- Mañé 1981: https://doi.org/10.1017/S0143385700001188
- Mañé 1983 errata: https://doi.org/10.1017/S0143385700001863

The exact local Mañé paths, both content hashes, project hashes, source URL
records, and review artifacts are pinned in `source_manifest.json` and
`SHA256SUMS`. The primary-source scope is source authentication, theorem and
errata extraction, and exact hypothesis/normalization translation; it is not a
new line-by-line proof of every historical entropy theorem.

Commands actually used include `sha256sum`, `pdftotext -layout`, visual review
of the retained primary-page images, and `python finite_checks.py`. The finite
check certifies only rational Fourier assembly and the printed derivative
budgets. No finite orbit sample is offered as proof of asymptotic decay.

No correction to the mathematical target or its boundary argument is required.
Recommended integration additions are the explicit Mañé+errata provenance,
the exact scan's page offset, and, for readability, distinct symbols for the
two Hölder-space weakenings. These are not restrictions on the theorem.

The strongest safe use is the full norm-uniform classical estimate above,
including its scalar total-mass consequence and specified product measure.
It does not by itself estimate quantum transport factors, a sum over
exponentially many displacements, N-torsion sectors, or the signed Heisenberg
trace hierarchy. TRACE-005 and BGS remain outside this audit and open.

## Curated source roles

Original review bytes and command/source roles are retained in the promotion
mapping. Portable replay: computations/verification/weighted_periodic_support.py.
This packaging preserves the original separate verdict; it is not combined
S1–S9 acceptance. No primary PDF is redistributed in this compact package.
