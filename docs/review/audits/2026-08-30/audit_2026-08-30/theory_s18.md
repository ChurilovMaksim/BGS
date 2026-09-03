
## 18. RUN 82 — TORUS RIGIDITY: THE OBSERVABLE FAMILY IS A ONE-PARAMETER
### ARITHMETIC CURVE

Standing assumptions for this section: `N` an odd prime with
`gcd(N, t^2 - 4) = 1` and `N` split for `A` (all three certified designs are
split); `A in SL_2(Z)`, `tr A = t = 3`; `K = ord_N(A)`; `U = U_A` the Weil
(metaplectic) propagator quantising `A^T` with exact Egorov covariance
`U T(n) U^* = T(A^T n)` (T1/A1, certified 3e-14); `P` the orthogonal projector
onto one `U`-eigenspace, of dimension `m = (N -+ 1)/K`; `R` the parity
operator, `P_+-` the parity blocks (Theorems C/D, §10); and

    V_n := P_+ (T(n) + T(-n)) P_+,        n in (Z/N)^2 \ {0}.

### 18.1 The Hecke torus and the invariant form

Let `T <= SL_2(Z/N)` be the centraliser of `A`.  Its Weil operators `U_g`,
`g in T`, commute with `U` up to a scalar and are exactly the HECKE OPERATORS
of Kurlberg-Rudnick (chao-dyn/9901031).  Write

    R_A = (Z/N)[x]/(x^2 - t x + 1),

so that `(Z/N)^2` is a free `R_A`-module of rank one (send `e_1` to `1` and
`A e_1` to `x`).  Under this identification `T` is the group of norm-one units
of `R_A` and

    Q(n) = n_1^2 - n_1 n_2 - n_2^2      (disc 5 = t^2 - 4)

is a scalar multiple of the norm form, hence `T`-invariant.  In the split case
`R_A = (Z/N) x (Z/N)`, the norm is `(u, v) -> uv`, `|T| = N - 1`, every level
set `{Q = q}`, `q != 0`, is a single simply transitive `T`-orbit of size
`N - 1`, and the cone `{Q = 0} \ {0}` has `2N - 2` elements.  Consequently
each nonzero level set contains exactly `|T|/K = m` distinct `<A>`-orbits and

    (N - 1) . m  +  (2N - 2)/K  =  (N^2 - 1)/K.

### 18.2 THEOREM I (torus rigidity) [PROVEN]

(a)  If `Q(n) = Q(n')` then `V_{n'} = U_g V_n U_g^*` for an explicit
     `g = a I + b A in T`; in particular `spec(V_n) = spec(V_{n'})`.
(b)  The family `{V_n}` has at most `N` distinct spectra — one per value of
     `Q` — rather than the `(N^2 - 1)/K` suggested by counting `<A>`-orbits.
(c)  The counting identity of §18.1 holds exactly.

PROOF.  By §18.1, `T` acts transitively on `{Q = q}`, so `n' = g n` for some
`g in T`.  Since `g` commutes with `A`, `U_g` commutes with `U` up to a
scalar and therefore preserves each `U`-eigenspace, i.e. `U_g P = P U_g`.
Since `-I` is central in `SL_2`, `U_g` commutes with `R` and so preserves
each parity block: `U_g P_+ = P_+ U_g`.  The Weil intertwining property gives
`U_g T(n) U_g^* = T(gn)` and `U_g T(-n) U_g^* = T(-gn)`.  Hence

    U_g V_n U_g^* = U_g P_+ (T(n) + T(-n)) P_+ U_g^*
                  = P_+ (T(gn) + T(-gn)) P_+ = V_{n'}.     []

Certification: `src/r82f_torus_rigidity.py`, five certificates C1-C5 at
`(N, K) = (199, 11), (3571, 17), (9349, 19)`, 15/15 PASS; full sorted spectra
agree across 8 distinct `<A>`-orbits in each of 6 level sets to
`2.4e-14 / 2.0e-13 / 3.3e-13`, while different level sets differ by 11-13
decades more.  Two-key value check through the exact `N x N` projector (no
randomised eigenbasis): `mu_4 = 1.85357709` both ways, `|diff| = 1.3e-14`
(`src/r82d_orbit_invariant.py`).

### 18.3 What Theorem I does to the ensemble route [PROVEN corollaries]

1.  The `n`-ensemble is a deterministic one-parameter curve `q -> V_q` with
    each member repeated `m` times.  Any ensemble average over
    `n in (Z/N)^2` equals the corresponding average over `q in F_N^*` (plus
    the cone).  The effective ensemble size is `N - 1`, not `(N^2-1)/K`.
2.  The R81.4 "coherent arithmetic fluctuation mode" is this curve.  One
    dominant fluctuation direction, positively correlated window counts, and
    an excess over GOE growing with `m` are all automatic for a
    one-parameter family whose spread is `O(1)` in `m`.  The reading
    "modulated universality, driver unknown" (R81.4/R81.5, ~75%) is
    superseded: the modulation is one-dimensional and its parameter is
    `q = Q(n)`.
3.  No i.i.d.-GOE statement can hold for `{V_n}`, for an exact and
    elementary reason.
4.  CEILING ON THE FREQUENCY ENSEMBLE.  Averaging moments over `n` buys
    concentration in one arithmetic scalar only.  It cannot separate
    per-system behaviour and therefore cannot substitute for a per-system
    local law.  With Theorem G (the moment route is provably closed) this
    closes the last "average it away" escape route of the programme
    explicitly.  The correct form of `op:local` is: for a FIXED `q`, prove
    GOE local statistics for the single matrix `V_q`.

### 18.4 The equivariant normal form, and the entry point for op:local

Let `{f_j}_{j in Z/m}` be the Hecke basis of the eigenspace: the joint
eigenbasis of all `U_g`, i.e. the `T`-character basis (the characters
occurring are those with a fixed value on `<A>`, a coset of the dual of
`T/<A> ~ Z/m`).  For `g in T`, equivariance
`<f_j|T(gn)|f_k> = (chi_j chi_k^{-1})(g) <f_j|T(n)|f_k>` forces

    <f_j|T(n)|f_k> = c_{jk}(q) . zeta^{(j-k) s(n)},    zeta = e^{2 pi i/m},

where `s(n) in Z/m` is the discrete logarithm of the torus element carrying a
fixed base point `n_q` to `n`.  Hence

    V_n = D_{s(n)} ( C_q + C_q^* ) D_{s(n)}^*,   D_s = diag(zeta^{js}),
    C_q = ( c_{jk}(q) )_{j,k},

so the entire arithmetic content of the family is ONE matrix `C_q` per level
set, its entries being explicit exponential sums, and the `n`-dependence
inside a level set is a diagonal unitary conjugation (consistent with
Theorem I).  `op:local` therefore becomes a LOCAL LAW FOR A MATRIX WITH
ARITHMETIC ENTRIES.  The decorrelation input required by any local-law
framework is precisely the kind supplied by Katz's equidistribution theorems
for Kloosterman sheaves, which Kurlberg-Rudnick already use for the value
distribution of Hecke eigenfunctions (math-ph/0101008); verifying the
entrywise moment conditions against those bounds is the named next step
(`op:local_entries`).

### 18.5 The modulation in closed form: a Fibonacci frequency comb
### [NUMERICALLY-SUPPORTED]

With `q` as the parameter the curve is computable exhaustively — all 3570
level sets at `N = 3571` (`src/r82g_q_curve.py`).  Write
`A^j = u_j I + v_j A`, so `u_j = -v_{j-1}` and

    v_j = 1, 3, 8, 21, 55, 144, 377, 987, 2584, ...   (t = 3: the
                                     even-index Fibonacci numbers)

Then the additive Fourier transform in `q` of the raw central traces is
sparse and supported on those coefficients: 16 frequencies `a = +- v_j`,
`j = 1..8`, carry 90% of the variance of `Tr(V_q^4)` and `Tr(V_q^6)` (0.4% of
the available modes), with nearly equal masses.  A least-squares fit on
exactly those `(K-1)/2 = 8` frequency pairs (17 parameters, 3570 points):

    Tr(V_q^4)  R^2 = 0.9426       mu_4(q)  R^2 = 0.98655
    Tr(V_q^6)  R^2 = 0.9276

    mu_4(q) = c_0 + sum_{j=1}^{(K-1)/2} 2 Re( alpha_j e_N(v_j q) ) + eps,
    var(eps)/var(mu_4) = 1.3%.

Enlarging the frequency set to 71 frequencies (adding `u_j`, doubles,
pairwise sums and differences) moves `R^2` only to 0.9472/0.9872: the comb is
saturated.  Mechanism, consistent with Lemma F (§11.4): each word of the
trace expansion carries a Weil phase `w^{Q_J(v)}` with
`v = sum_i eps_i A^{J_i} n`; a `T`-invariant quadratic form in `n` is a
multiple of `Q(n) = q`, and the multipliers reachable from products of powers
of `A` are exactly the `v_j`.  Deriving the `alpha_j` from the `Q_J` would
upgrade this to [PROVEN] and is the second open item of the R82 handoff.

Measured scale facts at the certified designs (exhaustive over level sets):

    Tr(V_q^2)/m_+   mean 0.117600, spread 1.22%,  N/(K^2 m_+) = 0.117658
    mu_4(q)         mean 1.9694, std 0.2350, range [1.2246, 2.8573]
    mu_6(q)         mean 5.084 (semicircle 5), std 0.55

so the macroscopic law is semicircular IN THE MEAN (the arcsine alternative is
refuted: it would give `mu_4 = 1.5`, `mu_6 = 2.5`), with an `O(1)` shape
modulation that does not decay in `m` (`std(mu_4)` = 0.38, 0.23, 0.21 at
`m_+` = 9, 105, 246, against GOE's 0.26, 0.027, 0.011).

### 18.6 Corrections to §17 issued by this run

* `op:dpbug` is CLOSED and the R81.6 retraction of the DENSE `S(R)` rows is
  itself withdrawn: the dense series was correct; the apparent
  supermultiplicativity failure came from comparing counts computed under two
  different WIDTH CAPS in the full (not dense) series.  What survives of
  R81.6 is the Int128 overflow for `R >= 110` and hence the voiding of the
  R81.2 extrapolation.  New rigorous sandwich, from an exact BigInt run that
  passes the glue check at every pair `R1 + R2 <= 150`:

      2.265415 <= C_dense <= 3,   S(150) = 1.87137...e53.

* §17.5's "modulated local law" is superseded by §18.3: the modulation is
  exactly one-dimensional and identified.  The falsifiable prediction of
  §17.5 ("the coherent-mode fraction should -> 1") is now a triviality for a
  one-parameter family and carries no information.
