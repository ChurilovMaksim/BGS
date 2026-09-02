"""Apply remaining referee fixes D2 (exact em-dash text), D3 (star the R82.16
table), D4 (small-spacings bound wording), D5 (generator scripts)."""
import io

NL = chr(10)


def patch(path, subs):
    s = io.open(path, encoding="utf-8").read()
    for old, new in subs:
        if old in s:
            s = s.replace(old, new, 1)
            print(f"  {path}: replaced {old[:48]!r}")
        else:
            print(f"!! ANCHOR NOT FOUND in {path}: {old[:60]!r}")
    io.open(path, "w", encoding="utf-8").write(s)


# ---- D2 in LEDGER (the actual text uses an em dash) ----------------------
patch("LEDGER.md", [
    ("""CERTIFICATION (`artifacts/r82/second_moment_identity.json`, computed from the
exhaustive `q`-curves — all 198 and all 3570 level sets):

    N = 199,  K = 11:  N/K^2 = 1.644628, mean Tr(V^2) = 1.609557,
                       mean E = -0.0351, max|E| = 0.7235, std E = 0.2153
    N = 3571, K = 17:  N/K^2 = 12.356401, mean Tr(V^2) = 12.348424,
                       mean E = -0.0080, max|E| = 0.7032, std E = 0.1508

so the measured `|E|` is a factor 5.5 inside the proven bound, and the MEAN of
`E` over the level sets decays like `N^{-1/2}` (0.0351 vs 0.0080 for
`N^{-1/2}` ratios 0.0709 vs 0.0167 — predicted ratio 4.24, measured 4.39):
the residual phases equidistribute.  This also explains why `Tr(V_q^2)` looked
"n-independent to 1.2%": the spread is `std E / (N/K^2) = 0.15/12.36`.""",
     """CERTIFICATION — CORRECTED (referee, R82.22): the original artifact
`second_moment_identity.json` certified the CENTRED second moment
`m_+ Var(ev)`, not `Tr(V^2)`; the two differ because `Tr V` is not negligible
(mean 0.092, std 0.407, max 1.073 at N = 199).  Raw-pipeline recomputation
over ALL level sets (`src/large_m/second_moment_raw.py`, referee
`review/referee/lemma82_1.py`):

    N = 199,  K = 11:  N/K^2 = 1.644628, mean Tr(V^2) = 1.628934,
                       mean E = -0.0157, max|E| = 0.7326
    N = 3571, K = 17:  N/K^2 = 12.356401, mean Tr(V^2) = 12.349512,
                       mean E = -0.0069, max|E| = 0.7032

The PROVEN statement `Tr(V_q^2) = N/K^2 + E(q), |E| < 4` holds with a wide
margin (max|E| a factor 5.5 inside).  The finer claim that `mean E` decays
like `N^{-1/2}` at the predicted rate does NOT survive the correct convention
(raw ratio 2.28, within 1 sigma of the MC error) and is RETRACTED; the bound
and the arithmetic leading term are unaffected."""),
])

# ---- D3: star the empirically-normalised columns of the R82.16 table ----
patch("LEDGER.md", [
    ("""    N        <|J|^2>/N     <|J|^4>/N^2   <|J|^6>/N^3   <|J|^8>/N^4
      199     1.060623       2.0143        5.1119        14.5205
     3571     1.007939       2.0022        5.0045        14.0046
    19489     0.996038       2.0062        5.0361        14.1649
    ---------------------------------------------------------------
    CATALAN     1              2             5            14
    Gaussian    1              2             6            24""",
     """    N        <|J|^2>/N     <|J|^4>/N^2   <|J|^6>/N^3   <|J|^8>/N^4
      199     1.060623       2.0143*       5.1119*       14.5205*
     3571     1.007939       2.0022*       5.0045*       14.0046*
    19489     0.996038       2.0062*       5.0361*       14.1649*
    ---------------------------------------------------------------
    CATALAN     1              2             5            14
    Gaussian    1              2             6            24

    (* the k >= 2 columns are EMPIRICALLY normalised
       <|J|^{2k}>/<|J|^2>^k . k!, not /N^k -- referee correction R82.22/D3.
       In the honest /N^k convention the small-N rows deviate materially
       beyond k = 2; the honest-convention confirmation is the N = 95419 row
       0.9994 / 1.9973 / 4.9904 / 13.9672 / 41.8897 (k = 1..5,
       `src/large_m/catalan_honest.py`) and R82.21's fourth-design pass.)"""),
])

patch("THEORY.md", [
    ("""    J(chi,psi;q)/sqrt N = tr(theta),   theta in SU(2) equidistributed,""",
     """    J(chi,psi;q)/sqrt N = tr(theta),   theta in SU(2) equidistributed,

    (normalisation note, referee R82.22/D3: the R82.16 table's k >= 2 columns
    were empirically normalised; in the honest /N^k convention the law is
    confirmed by the N = 95419 row 0.9994/1.9973/4.9904/13.9672/41.8897 for
    k = 1..5, while the small-N rows deviate materially beyond k = 2.)"""),
])

# ---- D4: small-spacings bound wording -----------------------------------
patch("LEDGER.md", [
    ("""All `z` are within +-2.1 with alternating signs across designs, and the extreme""",
     """All `z` are in [-2.41, +2.06] with alternating signs across designs (the
one beyond-2 value, z = -2.41 at `#pairs<0.02`, N = 95419, is a DEFICIT of
tiny spacings -- it REINFORCES the no-degeneracy conclusion), and the extreme"""),
])
patch("THEORY.md", [
    ("""agree with the matched GOE reference within `+-2.1` standard errors with
alternating signs across three designs, and the extreme minima behave like""",
     """agree with the matched GOE reference within the range [-2.41, +2.06]
standard errors with alternating signs across three designs (the single
beyond-2 value is a deficit of tiny spacings, reinforcing the conclusion),
and the extreme minima behave like"""),
])

# ---- README: the same two wordings --------------------------------------
patch("README.md", [
    ("all within `+-2.1 sigma` of matched GOE with alternating signs "
     "at 3 designs (N = 3571/95419/144481)",
     "within the range [-2.41, +2.06] sigma of matched GOE with alternating "
     "signs at 3 designs (N = 3571/95419/144481; the one beyond-2 value is a "
     "DEFICIT of tiny spacings, reinforcing the conclusion)"),
])
print("remaining referee fixes applied")
