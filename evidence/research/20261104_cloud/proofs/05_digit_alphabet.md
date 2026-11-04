# The ε-digit alphabet is {−1, 0, 1}

Status: **[P]**. The census through shell 16 is a check [P-computation].

N14 stated |E_k| ≤ 2 as a sketch. The code range of the twists gives one better, and the bound is sharp because the letter 1 occurs.

## Theorem

Let τ_k be the code twists of the span proof: τ_k = red(ξ_k) for even k and τ_k = −red(−ξ_k) for odd k, with red(x) = x − ⌊x + 1/2⌋. Let

E_k = −(τ_k − 2 τ_{k−1} − τ_{k−2}).

Then E_k ∈ {−1, 0, 1}.

## Proof

The representative red takes values in [−1/2, 1/2). Indeed red(x) = −1/2 when x ∈ ℤ + 1/2, and red(x) never equals +1/2. Consequently even twists lie in [−1/2, 1/2) and odd twists lie in (−1/2, 1/2].

The quantity Δ_k = τ_k − 2 τ_{k−1} − τ_{k−2} equals −E_k, and E_k is an integer because it equals n_k − 2 n_{k−1} − n_{k−2}. It is enough to show |Δ_k| < 2.

**Even k.** Then τ_k ∈ [−1/2, 1/2), τ_{k−1} ∈ (−1/2, 1/2], τ_{k−2} ∈ [−1/2, 1/2).

The upper bound uses τ_k < 1/2, −2 τ_{k−1} < 1 (because τ_{k−1} > −1/2), and −τ_{k−2} ≤ 1/2. The middle inequality is strict, so Δ_k < 2.

The lower bound uses τ_k ≥ −1/2, −2 τ_{k−1} > −1 (because τ_{k−1} < 1/2), and −τ_{k−2} ≥ −1/2. The middle inequality is strict, so Δ_k > −2.

**Odd k.** Then τ_k ∈ (−1/2, 1/2], τ_{k−1} ∈ [−1/2, 1/2), τ_{k−2} ∈ (−1/2, 1/2].

Upper bound: τ_k ≤ 1/2, −2 τ_{k−1} ≤ 1, and −τ_{k−2} < 1/2. The last inequality is strict, so Δ_k < 2.

Lower bound: τ_k > −1/2, −2 τ_{k−1} > −1, and −τ_{k−2} ≥ −1/2. The first two are strict, so Δ_k > −2.

Thus |Δ_k| < 2. An integer in (−2, 2) lies in {−1, 0, 1}.

## Sharpness and the census

The class α = 2 has word (1, 0, −1), so both nonzero letters occur. The exact enumeration of every fundamental-domain class with 1 ≤ |N| < 2^{17} (81 709 classes, shells j ≤ 16) found no letter outside {−1, 0, 1}. The counts were 276 440 letters equal to −1, 481 927 equal to 0, and 340 525 equal to 1.

## What this does not shrink

Lemma J’s 6145 pair states are carries of Fourier letter-differences |u_k| ≤ 60, not carries of these digits. A twist with E_k ∈ {−1, 0, 1} still has a Bessel expansion over |n| ≤ 60. The collision graph stays the 6145-state graph. The gain is for the symbolic language of polymers: the alphabet is ternary, and a zero-run is a run of the letter 0 in that alphabet.
