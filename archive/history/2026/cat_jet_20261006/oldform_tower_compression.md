# The complete oldform tower and its zero first-order blocks

Status: new candidate extension, pending independent audit. This is an exact structural obstruction to a first-order criterion, not a propagator collision theorem.

Let n=5^e and 0<=2j<=e. Put m=5^(e-2j). Define the isometry J_j:H_m→H_n by

    (J_j f)(x)=5^(-j/2) f(x/5^j modulo m) if5^j divides x,
               0 otherwise.

The repeated coordinates contribute the factor5^j to its squared norm. For m=1 use the one-dimensional normalized cat M_1=1.

## Exact intertwining and Weyl compression

For every primitive-root version of the prescribed quadratic kernel,

    M_n J_j=J_j M_m,

where the lower root is q_n^(5^(2j)). To verify it, write y=5^j(t+m l), with0<=l<5^j. The l-sum vanishes unless5^j divides x; on that support the remaining phase is exactly the m-dimensional kernel and the normalization is the displayed isometric one.

Likewise,

    J_j* T_n(a,b) J_j=0 unless5^j divides both a and b;
    J_j* T_n(a,b) J_j=T_m(a/5^j,b/5^j) otherwise.     (1)

The support enforces the a condition; the repeated-coordinate sum enforces b. Modular midpoint phases reduce correctly in the surviving case.

## The tower consists of full product-cat eigenspaces

The accepted uniform cat theorem makes M_n and M_m simple. Their eigenvalue sets satisfy E_m⊂E_n by the intertwining. They have exactly one partial orbit under multiplication by a primitive cube root omega; its occupancy is one for even e and two for odd e.

The normalized quadratic Gauss traces agree after lowering e by two. Indeed, writing x=y+5^(e-1)z in the raw trace sum and summing z modulo5 forces5|y, giving G_e=5G_(e-2). Division by the square-root normalization yields Tr M_e=Tr M_(e-2). The primitive-root coefficient reduces unchanged. Therefore M_n and M_m have the SAME partial cubic orbit with the same occupied subset: for occupancy one its eigenvalue is the trace; for occupancy two the missing eigenvalue is minus the trace.

All other occupied cubic orbits are full. It follows that E_n\E_m is a union of full cubic orbits. After tensoring with the seven-dimensional cat (whose three eigenvalues have multiplicities3,2,2 and cubic ratios), a product eigenvalue cannot receive one contribution from E_m and another from E_n\E_m. Consequently

    W_j=H_7 tensor J_j H_m

is a direct sum of COMPLETE eigenspaces of actual M_(7n), not merely an invariant proper part of a repeated eigenspace.

## Actual first-order compressions

In exact CRT coordinates the actual centered generator is

    A_(7n)=sum_v c_v T7(v) tensor Tn(v).

Combining with(1):

- j=0 retains the entire actual symbol;
- j=1 retains only the two actual modes(0,±5), so

  (I tensor J_1*) A (I tensor J_1)
    = -i/800 T7(0,5) tensor T_m(0,1)
      +i/800 T7(0,-5) tensor T_m(0,-1);

- j>=2 retains no mode at all, because |a|<=1, |b|<=9 and the zero Fourier coefficient is zero.

Therefore for EVERY e>=4, A has zero compression on the full spectral subspace W_2 of dimension7*5^(e-4). Every M eigenspace contained in W_2 has an identically zero first-order slope matrix. Their exact block dimensions are those of the smaller cat M_(7*5^(e-4)):

- e even: 5^(e-4)-1 blocks of size7, and3,2,2;
- e odd: 5^(e-4)-2 blocks of size7, and4,5,5.

For e=4 the first count is zero and only3,2,2 remain. Further zero first-order blocks may arise in the j=1 layer, but are not asserted here. In particular this theorem does not interpret a zero residue compression as characteristic-zero vanishing.

## Perturbation boundary

For unrotated powers, P_(W_j) A^k P_(W_j) is scalar when9k<5^j, since only total frequency zero can survive(1). This growing threshold is not a lower bound for effective eigenjet order: resolvents contain all cat rotations and hence arbitrarily long S-orbits at fixed perturbation order. A higher-order block analysis must retain those exact rotated returns.

This source inherits the reviewed uniform cat multiplicity theorem and the fixed32-mode dictionary. It neither assumes simple U nor converts simple A into simple U.
