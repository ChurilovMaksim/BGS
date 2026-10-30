# Line I, step (3) v2 (Session 4, referee fixes B6, B7, B8-scope, B9-labels applied; theory_E2.md kept for provenance)

Notation: z_nu = (nu+i)/2h (nu mod 2h) on SL2(Z)\H; Z_nu = sum_n Phihat(n) e(-nu P(n)/2h);
C(k) = sum_{n,n'} Phihat(n) conj(Phihat(n')) 1[P(n)-P(n') ≡ k mod 2h]  (depends on k mod 2h), so (Parseval)
C(k) = (1/2h) sum_{nu mod 2h} |Z_nu|^2 e(nu k/2h)  and  sum_{k mod 2h} |C(k)|^2 = (1/2h) sum_nu |Z_nu|^4.
c_q(j) = sum_{nu mod q, gcd(nu,q)=1} e(nu j/q)  (Ramanujan sum).  Sigma |Phihat|^2 = 1 (referee).

## Lemma I5' (corrected statement of I5) [P]   — fixes B6 (sign; unit restriction) and one further point
For f on SL2(Z)\H, f(x+iy) = sum_{k in Z} c_k(y) e(kx) (absolutely convergent, e.g. f smooth):
 (a) ALL residues:  sum_{nu mod 2h} |Z_nu|^2 f(z_nu) = 2h sum_{k in Z} c_k(1/2h) C(k)            (C(k), not C(-k)).
 (b) UNITS only:    sum_{nu unit} |Z_nu|^2 f(z_nu) = sum_{k in Z} c_k(1/2h) sum_{n,n'} Phihat(n) conj Phihat(n') c_{2h}(k - P(n) + P(n')).
Proof: expand |Z|^2 and f, sum over nu (orthogonality mod 2h, resp. definition of c_{2h}). QED.
Diagonal class. Pairs with P(n) ≡ P(n') (mod 2h) (in particular n = n') contribute
 (a) C(0) * sum_{nu mod 2h} f(z_nu) = C(0) * 2h sum_{j in Z} c_{2hj}(1/2h);   (b) C(0) * sum_{nu unit} f(z_nu).
Correction to the old text: even in (a) the diagonal meets every c_{2hj}, j ∈ Z (not only c_0), so it is NOT invisible for cusp
forms; it is C(0) times the UNWEIGHTED sum of f over the 2h horocycle points (a), resp. over the phi(2h) primitive ones (b).
These unweighted sums are o(2h), resp. o(phi(2h)), for fixed cusp forms f by equidistribution of (primitive) rational points on
the closed horocycle of height 1/2h (classical; cite with explicit rate before use — not checked in this line).  Hence the diagonal
contributes C(0)·o(1) to the normalised sum (1/phi) sum_unit (...); this is o(m) PROVIDED C(0) = O(m) (C(0) is the mean of |Z|^2 over
all nu mod 2h; numerically O(m), not proved).  Correct message: the real content of (E″) is off-diagonal, MODULO an unweighted
equidistribution input and the bound C(0) = O(m).  The word "purely off-diagonal / invisible" is withdrawn.

## Route A: Deshouillers–Iwaniec large sieve -> obstruction [assessment]  (was labelled [P]; B9)
DI: sum_{|t_j|<=T} |sum_{|k|<=N} a_k rho_j(k)|^2 / cosh(pi t_j) << (T^2 + N^{1+eps}) sum |a_k|^2.  With a_k = C(k) K(...) and
N ≍ 2h this gives for S_j := sum_nu |Z_nu|^2 f_j(z_nu): sum_{|t_j|<=T} |S_j|^2 << h^{1+eps} * sum_nu |Z_nu|^4.
(E″) needs S_j = o(m h).  Even an RMT-sized bulk fourth moment (≍ m^2 h) gives h^{2+eps} m^2 vs the needed o(m^2 h^2), and
the resonant residues make the unrestricted fourth moment exponentially larger.  What this shows: THIS inequality chain cannot
give (E″); it is not a proof that no method works.

## Route B: Kuznetsov / Kloosterman -> l^1 obstruction [assessment]  (was [P]; B9)
Opening rho_j(k) via Kuznetsov gives Kloosterman sums weighted by C(k)C(k'); Weil saves sqrt(c) but the weights enter in l^1:
sum_k |C(k)| <= (sum_n |Phihat(n)|)^2 = (sum_j |J_j(1.8)|)^{2m} ≈ 2.37^{2m} ≈ 5.6^m vs target m h ≍ 2.414^m.  Exponential loss
for this chain (no cancellation among Phihat exploited).

## Route C: Bowen–Margulis / Pell geodesic -> wrong measure [assessment]
(unchanged) z_nu lie on one closed horocycle; their UNWEIGHTED equidistribution is classical (Zagier/Sarnak; cite rate).  The
weighted measure |Z_nu|^2 delta_{z_nu} is invariant under no unipotent/diagonal flow, so Ratner/mixing theorems do not apply.

## What CAN be said rigorously
(i) Prop I8 (one-sided reduction) [P] (B7: hypotheses made explicit). Facts used:
   (1) the sets {nu_rho} (rho ∈ P*) and M_d(rho) are pairwise disjoint: by the frozen rule a common member of levels d, d' lies at
       level gcd(d,d') | d and is excluded from M_d; distinct rho differ mod h/d >= sqrt h;  (2) RMT_m = 4m - m^2/h <= 4m;
   (3) N_res := #resonant residues <= phi.
   Then, since |Z|^2 >= 0 on the non-resonant units,  W'_m >= -RMT_m (1 - N_res/phi) + (1/phi) sum_{rho, d incl.} Dev_d(rho),
   Dev_d(rho) := sum_{nu ∈ M_d(rho)} (|Z_nu|^2 - |Z_rho|^2/d^2);  so W'/m >= -4 + (1/(m phi)) sum Dev unconditionally.
   The lower half of R' (W' >= -o(m)) REDUCES TO (is implied by) "bulk not much below RMT" plus dilation-deviation control
   (was: "is exactly the statement").
(ii) Scope (B8): Prop I2' + Theorem I6 bound the SQUARE part of the d = 7 deviation only: rho = (±2,8), m ≡ 3 (mod 6)
   (Session 4 symmetry extension; Session 3 had m ≡ 9 (mod 24), rho=(2,8)), and the bound is < 0.01 (F units) only for m >= 321.
   Relevance to Dev: members' square parts satisfy sum_{t∈M}|Delta_t|^2 <= sum_{t≠0}|Delta_t|^2 = d sum_u|delta_u|^2
   (Parseval, Delta_0 = 0).  The cross part is NOT controlled.
(iii) Positive-density / average-over-m versions: no unconditional statement obtained (see also theory_session4.md).

## Halo near theta = ±1/2 (8|b) — quantified [N] (unchanged numbers; wording: the halo SUM stayed O(1) in F units for m = 11..17,
which if it persisted would contribute O(1/m) to W'/m — an observation, not a bound).
Contribution of |theta - 1/2| <= 0.1 to W'/m: +.073, +.068, +.062, +.048 (m = 11..17); in F units (×m): 0.80, 0.88, 0.93, 0.82.
