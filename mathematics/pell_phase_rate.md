# Summable Pell phases and a quantitative Gaussian limit

Status: project derivation with proof, not a priority claim or a fully formalized general theorem. This concerns global cosine-observable blocks, not microscopic BGS eigenphase statistics.

Use the notation and arithmetic lifting argument of `pell_cat_map_gaussian_blocks.md`: alpha=1+sqrt(2), lambda=alpha^2, N+F sqrt(2)=alpha^K for odd prime K, h=3+2/F modulo N, q=-F, n=(N-1)/(2K), X_j=sqrt(K/2) A_j and mu_m(j)=Tr(X_j^m)/n.

## Summable crossing phases

Let P_t be the Pell sequence. For d modulo K, take the signed representative delta in [-(K-1)/2,(K-1)/2]. The exact Pell congruence is

```text
q(h^d-h^(-d)) = -2 P_(2delta) modulo N.
z_d = e_N(q(h^d-h^(-d))).
```

For positive delta write delta=(K-1)/2-ell. Since K is odd,

```text
P_(2delta)/N = lambda^(-ell)/(sqrt(2) alpha)
               * (1-lambda^(-2delta))/(1-lambda^(-K)).
```

The elementary bound |exp(it)-1|<=|t|, the two signs of delta, and alpha(1-lambda^(-1))=2 yield

```text
L_K = sum_(d mod K) |z_d-1|
    <= 2 sqrt(2) pi/(1-lambda^(-K)) < 9,  K>=3.
```

This sums the boundary layer rather than discarding O(log K) labels.

## The improved fixed-moment estimate

For a pairing of 2r positions, its central Weyl phase is a product of c factors z_(a-b) or their conjugates, one per crossing. Under independent H labels, with the first pair label fixed, each individual difference remains uniform modulo K. No independence of the phase factors is required: for unit complex numbers,

```text
|product u_i - 1| <= sum |u_i-1|.
```

The pairing-average phase error is therefore at most 9c/K. If P_r=(2r-1)!!, then

```text
sum_(pairings pi) crossings(pi) = P_r r(r-1)/6.
```

One way to see this is to select four interlaced endpoints and match the remaining 2r-4 positions. Thus the total normalized crossing error is at most (3/2)P_r r(r-1)/K. Repeated-label overcount is at most P_r binom(r,2)/K.

For completeness, the remaining arithmetic input is not a random-matrix assumption. Rotate any m-term reciprocal modular zero relation across its largest cyclic gap. Its polynomial has degree at most K-K/m and coefficient l1 norm at most m. A nonzero value at lambda has algebraic norm divisible by N^2, whereas its absolute norm is at most m^2 lambda^(K-K/m). For fixed m these bounds contradict one another for sufficiently large K. Hence the relation lifts to characteristic zero.

The minimal polynomial x^2-6x+1 has value -4 at 1, excluding odd signed relations. A gap larger than 2 log_lambda(m) splits a lifted relation: otherwise the norm of its lower-exponent part would be a nonzero integer of magnitude below 1. Each resulting component has bounded width at fixed m. After cancellation of opposite equal powers, any remaining component has at least three occurrences. A nonpairable 2r-term relation consequently has at most r-1 freely translated components and only O_r(K^(r-2)) configurations after one label is pinned. The paired configurations have order K^(r-1).

Combining this count with the phase bound and the exact noncentral fixed-point trace estimate gives, for each fixed r,

```text
sup_j |mu_(2r)(j)-(2r-1)!!|
    = O_r(1/K) + O_r(K^(r+1)/N).
```

For odd m and all sufficiently large K,

```text
sup_j |mu_m(j)| <= 2^(m/2+1) K^(m/2+1)/(N-1).
```

The estimates are uniform over all sectors and also allow composite N. Gaussian moment determinacy, tightness, and the higher even-moment bounds give weak convergence of the global empirical measures. This does not prove a microscopic universality statement.

## Exact central fourth moment and its first correction

For K>=11 all reciprocal modular four-relations lift, by the explicit sufficient inequality

```text
lambda^(K/4)(1-lambda^(-K))^2 > 64.
```

A four-term characteristic-zero relation must pair, since lambda>3. The two noncrossing pairings have phase one, and the crossing pairing has phase z_d. The six all-equal balanced sign words are counted twice in the pairing sum and must be subtracted. Consequently

```text
mu_4(j) = [N/(N-1)] [2+S_K-3/(2K)] + R_(4,j),
|R_(4,j)| <= 8 K^3/(N-1),
S_K = [1+2 sum_(delta=1)^((K-1)/2) cos(4 pi P_(2delta)/N)]/K.
```

Define the absolutely convergent constant

```text
a = 4 pi/(sqrt(2) alpha),
gamma = 3/2 + 2 sum_(ell>=0) [1-cos(a lambda^(-ell))].
```

Then, uniformly in j,

```text
mu_4(j) = 3-gamma/K + O(K^3/N).
```

Indeed, replacing the finite Pell ratio by lambda^(-ell)/(sqrt(2)alpha) produces a summed argument error O(lambda^(-K/2))=O(1/N), before division by K. The omitted cosine tail is O(lambda^(-K)). The normalization error N/(N-1)-1 is O(1/N), and all these terms are absorbed by the explicit noncentral bound.

For J terms, the nonnegative tail is bounded by

```text
0 <= gamma-gamma_J <= a^2 lambda^(-2J)/(1-lambda^(-2)).
```

The numerical value starts 5.61422069215119807163. The maintained verifier separates the analytic series-tail bound from floating-point rounding; the decimal is not an interval certificate.

## Verification and scope

`computations/verification/pell_gaussian_regression.py` independently assembles odd orbit blocks, checks nontrivial sectors and composite N, compares matrix-power and eigenvalue moments, tests the fourth-moment remainder, and checks phase control at larger K without constructing exponentially large matrices.

All pairings survive along this deterministic fixed-map Pell sequence, producing Gaussian fourth moment 3. The separately averaged prime magnetic construction suppresses crossings and has semicircle fourth moment 2. These are different families and averaging procedures. Neither result supplies Heisenberg-scale propagator trace comparison, local spacings, or a complete BGS theorem.

## Independent exact interval certificate

The corrected decimal is independently enclosed by `computations/verification/pell_gamma_interval.py`. It uses only integer and rational arithmetic: Machin's identity, alternating arctangent bounds, an integer square-root enclosure, outward fixed-point operations, cosine Taylor remainders, and the geometric tail above. Its output in `evidence/certificates/pell_gamma_interval.json` certifies forty decimal places without assuming floating-point rounding. The preceding numerical companion retains its separate diagnostic scope.
