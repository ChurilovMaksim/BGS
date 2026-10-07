# A targeted off-charge boundary counterexample to gap-only closure

Candidate theorem, 7 October 2026. This is an explicitly CHANGED unitary family. It is not the frozen kicked map, does not preserve its exact quantization or its reverse-kernel decay, and is not a counterexample to BGS for that map.

The point is narrower and stronger than inferring off-charge failure from a full-CUE counterexample: here the actual occupation-mismatched, high-Hamming, high-switch residual itself is proved to diverge despite an exact flat position chain and charge-block norms tending to zero. All masks and the signed boundary integral are the same algebraic objects as T13–T17 of the accepted switch-transfer note.

## F1. Universal occupation-gradient bound

For every N-dimensional unitary U and integer m>=1, define

    B_m(U)=integral_(T^N) |Tr((Z_theta U)^m)|^2 dtheta,
    Z_theta=diag(e^(i theta_j)),

with normalized torus measure. Then

    0 <= B_m(U) <= m N.                                    (F1)

Proof. The polynomial p_m(x)=Tr((diag(x)U)^m) is homogeneous of degree m with nonnegative integer exponents:

    p_m(x)=sum_(|n|=m) c_n x^n.

Parseval gives B_m=sum_n |c_n|^2 and

    sum_j integral |partial_(theta_j) p_m(e^(i theta))|^2
      =sum_n (sum_j n_j^2)|c_n|^2 >=m B_m.

By the noncommuting product rule and trace cyclicity,

    partial_(theta_j) Tr((Z_theta U)^m)
      = i m ((Z_theta U)^m)_(jj).

Unitarity gives sum_j |((Z_theta U)^m)_(jj)|^2<=N. Hence the preceding derivative energy is at most m^2N, proving F1. All occupation multiplicities are retained. The torus integral identifies the exact deterministic occupation projector; the original U is not replaced by an ensemble in the conclusion about its off-charge part.

## F2. Explicit flat finite-order family

Let p>=5 run through primes congruent to 2 modulo 3. Such primes are infinite by the elementary Euclid argument: if there were finitely many, a prime factor congruent to 2 modulo 3 of three times their product minus one would be new. Cubing is a permutation of F_p. Let F_p(j,k)=p^(-1/2)e_p(jk) be the unitary discrete Fourier matrix, and define

    V_p(j,k)=p^(-1/2)e_p(j^3 k^3).                           (F2)

This is simultaneous permutation conjugation of F_p. Thus V_p is unitary, all entries have squared modulus 1/p, and

    |V_p|^2=J_p,      V_p^4=I,
    |Tr V_p^m|^2 = p^2 if 4 divides m, and 1 otherwise.      (F3)

For the final trace assertion, Fourier squared is the reflection j->-j, of trace one for odd p, while the odd-power traces have modulus one by the elementary quadratic Gauss identity. Only the lower bound p^2 at multiples of four is needed below.

Boundary: V_p is symmetric. Consequently its reverse kernel Q_(jk)=V_(jk)conjugate(V_(kj)) is J_p and ||Q||=1. This construction does NOT satisfy FM-022 reverse-kernel decay. It refutes a closure from P+charge gap+exact switch/occupation bookkeeping alone, not a criterion that also uses all available model-specific inputs.

## F3. Every nonzero charge block has vanishing norm

For c!=0 modulo p, put

    B_c(j,k)=V_p(j,k)conjugate(V_p(j+c,k+c)).

Then, uniformly over c,

    ||B_c||^2 <= p^(-1)+sqrt(2) p^(-1/4),
    ||B_c|| <=sqrt(1+sqrt(2)) p^(-1/8) ->0.                 (F4)

No external Weil bound is needed.

For distinct rows j,l, write a=j^3-l^3 and b=(j+c)^3-(l+c)^3. Both are nonzero because cubing is injective. The unnormalized row correlation is the complete additive sum of

    f(k)=a k^3-b(k+c)^3.

If a!=b this is cubic; if a=b its quadratic coefficient is -3bc!=0. For a nonzero quadratic over F_p, the Gauss sum has modulus sqrt(p): squaring the sum and differencing leaves p on the zero shift and zero on every nonzero shift.

For a cubic with nonzero leading coefficient, apply the same identity once:

    |sum_k e_p(f(k))|^2
      =sum_h sum_k e_p(f(k+h)-f(k)).

The h=0 term is p. Every h!=0 term is a quadratic sum of modulus sqrt(p), since p!=3. Therefore

    |sum_k e_p(f(k))|^2 <=p+(p-1)sqrt(p)<=2p^(3/2).

Thus every off-diagonal entry of B_c B_c* has modulus at most sqrt(2)p^(-5/4), while every diagonal entry is exactly 1/p. Schur's bound gives F4. The zero-charge block is exactly J, so the centered full pinching satisfies

    ||D_p|I^perp||=max_(c!=0)||B_c|| ->0.                    (F5)

The estimate is intentionally elementary and weaker than what a cubic Weil bound would give; its decay is enough for the claimed obstruction.

## F4. The actual off-charge aggregate diverges

Let w be nonnegative, nonzero, smooth and supported in a fixed interval 0<a<b<1/4. Its deterministic occupation-mismatched trace is exactly

    G_(p,m)(1,1)=|Tr V_p^m|^2-B_m(V_p).

By F1 and the multiples-of-four part of F3,

    p^(-2)sum_m w(m/p)G_(p,m)(1,1)
       >= sum_(4 divides m) w(m/p) -p^(-1)sum_m m w(m/p)
       = p integral_0^infinity (1/4-t)w(t)dt+o(p).          (F6)

The coefficient is strictly positive. The complete signed off-charge target therefore fails by linear divergence along these odd prime dimensions. This conclusion estimates the balanced term independently; it does not infer off-charge failure from full-pair failure alone.

## F5. The divergence lies in the exact high-Hamming/high-switch residual

Fix any kappa>0 and put R_p=floor(kappa p/log p). Retain the literal rooted cyclic-word mask

    occupation(x)!=occupation(y),
    h(y-x)>floor(.49m),
    s(y-x)>R_p.                                           (F7)

Because P=J, the accepted universal raw off-charge Hamming bound

    |low-Hamming off-charge trace| <=2(p^2-1)
             [sum_(r<=floor(.49m)) binom(m,r)] ||P-J||^(m-2floor(.49m))

is exactly zero. Its exponent is positive for every m>=1.

By F5, choose any fixed rho in (0,1) as small as needed and then take p sufficiently large that all nonzero charge blocks have norm <=rho. The charge-zero centered block is zero. Arbitrary occupation row phases preserve those block norms. The accepted exact zero-run annihilation and switch counting therefore give the off-charge bound T11/T12 for this family as well. Choose -log rho >8kappa/a. It follows that the portion with <=R_p switches, with any further Hamming restriction, has exponentially small compact-time aggregate. This argument sums each fiber before taking absolute values; it does not invoke arbitrary-subset monotonicity.

Consequently the residual F7 itself satisfies the lower bound F6 up to an exponentially small error. It is precisely the off-charge residual remaining after the two accepted removals.

Choose z_p=1-A log p/p with A>4/a. Eventually F5 allows rho<=1/2, so T8/T9 and the same low-switch subtraction show that the z_p-weighted F7 aggregate tends to zero. Its undamped aggregate diverges by F6. By the exact fundamental theorem of calculus T15, the signed marked-switch boundary integral T16 for this family diverges at least linearly. Thus complete transfer algebra, positivity at real q=1, P=J, and even a charge-block gap tending to one do not imply the missing boundary estimate.

## F6. Scope and evidence

F1–F6 are elementary analytic/algebraic proofs; finite checks only verify their finite identities and implementation. This example has strong arithmetic recurrence, wrong reverse-kernel behavior, and no fixed smooth frozen quantization. It supplies no conclusion about the literal tau=10^-80 map and no counterexample satisfying every accepted actual-model input. Its role is to reject the stated gap-only boundary closure, and to require any further proof to use additional actual signed-phase information.
