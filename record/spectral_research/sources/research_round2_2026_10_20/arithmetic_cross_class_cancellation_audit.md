> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/arithmetic_cross_class_cancellation_audit.md`. Embedded SHA256: `3435f9bafe3142f6d9c67b8d99bf235a1a33bb212fb805462b07f84ca9f6c4ef`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit of the actual cross-class cancellation theorem

20 October 2026. This audit checks the frozen theorem in
`adversarial_cross_class_cancellation.md`, SHA-256
`0ba7b2f260b2fbc80236b0e82d4960f726850bad0f33563b5582705d48c549a4`.
The complete text was read independently. Verdict: **PASS**, with the
scope below. No correction to its mathematical statements is needed.

## 1. Inputs checked

| File | SHA-256 |
|---|---|
| `fermionic_pseudoorbit_cutoff.md` | `03173e53d1a10e2c1afad517c48943a5330d43fc4059b80fc0e37d5b1598a9eb` |
| `fermionic_signed_three_cell_profile.md` | `edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5` |
| `fermionic_six_connection_cancellation.md` | `4661fed89558f03c58e085ec70df919b14056ff4ec5e3e765e6564ce35fbb865` |
| `fermionic_homoclinic_and_doubled_transfer.md` | `85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168` |

## 2. Weighted occurrence estimate

Write k=2R and epsilon=Lambda^(-k). After the interior zero fixed
orbit is removed, a primitive orbit of length d<=k cannot contain
k cyclic consecutive zero symbols. For d>=k+1 every marked cyclic
occurrence gives one uniquely centered word 0^R u 0^R. Primitivity
and the unique nonboundary itinerary make different cyclic positions
different centered words. Hence no extraneous factor d enters the
estimate.

The open-word sum is

    [J^R T^(d-k) J^R 1](o) <= C Lambda^(-2R).

Here evaluation of the left J^R supplies exactly Lambda^(-R), the
right factor has norm at most C Lambda^(-R), and powers of T are
uniformly bounded. The periodic/open comparison is uniform in the
middle word, including its shortest possible lengths. Allowing
imprimitive middle words only increases this positive upper bound.
The quantum squared-weight correction is uniformly bounded for
d<=BN. Consequently

    sum_(p primitive, d_p=d) r_k(p)|a_(p,N)|^2 <= C_B epsilon.

The only periodic point on a coding boundary is the origin: the
boundary spines and their iterates lie on its stable or unstable
leaves. Its coding fiber has at most four elements, on which the
shift acts as a permutation. For k>4 no nonconstant such periodic
itinerary can contain k zeros. The separate interior zero fixed
orbit has already been removed. Thus the boundary exception does
not invalidate the occurrence estimate.

## 3. Positive Euler mass and deletion

Deleting the zero primitive orbit divides the positive classical
Euler product by 1+Lambda^(-1)z. Its coefficients therefore retain
the positive limiting value

    C_- = C_F/(1+Lambda^(-1)).

The O(d h^2) squared-weight corrections give uniformly bounded
positive coefficients for m<=BN and convergence to C_- throughout
each fixed band bN<=m<=BN. Distinguishing one marked primitive
component and bounding the remaining positive Euler coefficient
gives

    Q_m^- - Q_m^free <= C_B m epsilon.

The remaining set must omit the distinguished primitive orbit;
dropping that restriction only increases the bound. Thus the
distinct-primitive convention is respected. With fixed R_0 large
enough and R=ceil(log N/(2 log Lambda))+R_0, the marker-free mass
is bounded below uniformly by a positive constant.

For the signed product, the deleted factor is (1-a_0 z)^(-1).
Since |a_0|<=0.48 for large N, this factor is uniformly bounded on
|z|=2. The determinant cutoff and the exact exterior estimate give
an exponentially small coefficient uniformly on
6N/5<=m<=3N/2. The full trace tail in that exterior estimate is
controlled by splitting at log_a N; the bound is o(N), rather
than an unjustified truncation of the infinite series.

## 4. Allowed reconnections and the negative cross term

Every allowed cut has at least R zeros on both sides and every cell
contains a nonzero edge. Reconnecting such cells retains a block of
at least 2R zeros at every new junction. Consequently both sides of
every nontrivial allowed move are marked. Retaining all uncut
components does not change this observation. Outputs with repeated
primitive components, imprimitive cycles, or the deleted fixed orbit
are excluded exactly as stated in the theorem; replacing an
imprimitive output by its primitive root would change the degree
and is not an allowed move.

Marker-free pseudo-orbits are therefore singleton classes under
the generated equivalence relation, even when all nonzero edges,
longer buffers, and admissible successor permutations are allowed.
In fact the argument applies to any partition preserving those
singletons.

If B(C) is the signed amplitude of a class, then

    sum_C |B(C)|^2 >= Q_m^free,

whereas the sum of B(C) is the exponentially small Euler
coefficient. The exact ordered cross-class sum is

    sum_(C != C') B(C) conjugate(B(C'))
      = |sum_C B(C)|^2 - sum_C |B(C)|^2.

It is real and is bounded above by a strictly negative constant
uniformly on the stated band. This deduction needs no unproved
sign assertion about individual cross terms.

## 5. Exact scope

The theorem establishes an actual negative cross-class correlation
in the principal Euler coefficients for this map and these
amplitudes. It rigorously excludes an o(1) deletion of all such
cross-class products after the specified encounter regroupings.
It does not identify those Euler coefficients with the target
power-trace correlation functional, and it does not prove or
refute H_diag. The determinant cutoff alone does not bound the
reciprocal determinant near its eigenvalue zeros.
