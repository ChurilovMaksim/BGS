# Tail-bound attack: derivation, required input, obstruction status

Date: Aug 2026. Target: prove `N_3(a,b) <= C (k^2/p + k^{1/2+eps})`
for generic labels; any theta<1 in N_3=O(k^theta) suffices for
Corollary Domination.

## 1. Character-sum identity

For signs (+,-,+,-), reduced system on (x,y,z)=(u2,u3,u4) in H^3:
    f1 = a1 - a2 x + a3 y - a4 z
    f2 = b1 - b2/x + b3/y - b4/z.
Additive-char indicator:

    N3 = p^-2 * sum_{r,s in F_p} S(r,s),
    S(r,s) = sum_{H^3} exp_p( r f1(x,y,z) + s f2(x,y,z) ).

Main term (0,0): k^3/p^2  (= exact ensemble mean by Thm meanlaw).

## 2. Reductions

Innermost z-sum at fixed (x,y):
    K_H(A,B) = sum_{z in H} e_p(A z + B / z),   A=-r a4, B=-s b4.
Completion against Weil's full Kloosterman bound
(|K(tA',tB')| <= (|A'|+|B'|) p^{1/2}, t != 0):
    |K_H(A,B)| <= min( k,  c sqrt(k p) log p ).

Axes (s=0 or r=0): S factorises into three subgroup Gauss sums
Hhat(t)=sum_H e_p(t h); |Hhat| <= min(k, sqrt(p) log p);
axis contribution <= p^-2 * sum_r |Hhat|^3
                 =  (log^3 / p) * min(k, sqrt(p) log)^2
                 <= (k^2/p) * polylog          for k <= p^{2/3}.

Generic cell (r,s both nonzero): iterate completion over y then x;
each completed layer multiplies by (sqrt(k p)/p) = sqrt(k/p) and
leaves one power of the trivial-size k. Three nested completions give
heuristically
    |S(r,s)| <= k * (sqrt(k p) log p)^2 / p^2  = (k^2/p) * log^2 p,
and summing over (p-1)^2 pairs loses another factor p^2/p^2 after the
outer p^-2, so total error <= (k^2/p) polylog. Boundary corrections
from partial tails of Hhat supply at most O(k^{1/2} polylog).

## 3. What this would prove

    N3 << (k^2/p) polylog + k^{1/2} polylog,
i.e. the Phase-1a ladder rung with polylog slack -- enough for
Domination (any o(k) works) and consistent with every measured point
(238 configs: max N3/(k^2/p + sqrt k) = 0.724).

## 4. Obstruction (precisely named)

Step 2's nested completion is valid for FULL field sums; for PROPER
subgroups each re-completion requires bounding
    sum_{t in F_p^*} |Hhat(t)|^j * |K_full(tA', tB')|,
and Weil gives |K_full| only pointwise; extracting the product sum
needs either (i) Deligne-grade Riemann Hypothesis over the
k-th-cyclotomic sheaf restricting the Kloosterman sheaf to mu_k, i.e.
exactly the "Katz tier" input, or (ii) an elementary Stepanov loop
adapted to two simultaneous rational phases on H^3, which to our
knowledge is open. This is the SAME wall met by the classical
subgroup-Kloosterman literature (per our lit notes:
OSV arXiv:2110.10941 Cor 2.9 covers only k > p^{3/7+eps};
nothing printed below).

## 5. Refined empirical law discovered during 1c

Merged 238-point scan (run36_audit + run20_constant):
    form                  min      med      max
    floor(k2/p)+2         0.000    0.500    1.000   <- tight, exact
    C*sqrt(k)             0.000    0.378    2.755   <- FAILS (C>2.7)
    k2/p + sqrt(k)        0.000    0.275    0.724   <- holds at C=1
    max(k2/p, sqrt k)     0.000    0.356    1.357
So: pure sqrt-branch FALSE; smooth law N3 <= k2/p + sqrt k true at
unit constant; floor+2 remains the sharpest integer form. The sqrt
branch may be slack absorbing an O(1) granularity term.

## 6. Status

[OPEN GAP] with fully specified missing input (Sec 4). Any future
progress on subgroup Kloosterman below p^{3/7} immediately implies
our Conjecture tight up to logs, hence unconditional Domination.
