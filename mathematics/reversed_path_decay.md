# Reversed-coordinate-path decay at the fixed physical coupling

**Stable claim ID:** BGS-FM-022.

Pinned base: `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`.
Preexisting project result, reconstructed internal proof audit. No external
referee certificate, world-priority claim, or full BGS conclusion.

## 1. Claim and exact family

Use exactly the odd-dimensional unitary U_N and tau=10^-80 of `fixed_map_path_model.md`.
Put P_xy=|U_xy|² and Q_xy=U_xy conjugate(U_yx). The matrix Q is Hermitian.
For a word x=(x_0,...,x_(m−1)), use cyclic indices and
A(x)=product_j U_(x_j,x_(j+1)). Let C(x) be its set of distinct cyclic
rotations, and let x^rev be its reversal. Define the ordered-pair sum

R_m^rev = sum_x sum_(y in C(x^rev) minus C(x)) A(x) conjugate(A(y)).

**Theorem.** As N tends to infinity through all odd dimensions,

||Q_N||op ->0.

For each fixed 0<a<b<infinity,

sup_(aN<=m<=bN) |R_m^rev|/m ->0.

Consequently for every smooth compactly supported w in (0,infinity),
N^-2 sum_m w(m/N)R_m^rev ->0. No rate or effective startup dimension is
asserted. The coupling is held fixed throughout both limits.

## 2. Exact quantization and the sixteen kernels

The complete direct finite-difference construction is
`four_branch_parametrix.md`. Its exact initial Gauss identity, transport
hierarchy, lattice gluing and unitary Duhamel estimate give

U_(jk)=e(3N/8)/(2 sqrt N) sum_(r=0)^3
 e(N S_r(x,y;t)) [a_(r,0)(x,y;t)+N^-1 a_(r,1)(x,y;t)] + O(N^-3/2),

at t=tau, uniformly in j,k, with all fixed amplitude derivatives bounded
independently of N. In particular max P_xy=O(N^-1). The product defining Q
is the sum of sixteen matrices with entries

N^-1 b_(rs,N)(x,y)e(N phi_rs(x,y)),
phi_rs=S_r(x,y;t)−S_s(y,x;t),

plus an O(N^-2) entrywise error, hence an O(N^-1) operator error. The
amplitudes b_(rs,N) form a uniformly smooth bounded family.

Section4 of that construction reconstructs an actual-time, rather than
formal, certificate. The first t-derivative of the phi_rs,xy Fourier
coefficient at (25/4,1/4) has modulus pi/128. The normalized coefficient
remainder at t=tau is at most10^50 tau²=10^-110. This is strictly less
than (pi/128)tau. Hence phi_rs,xy is a nonzero analytic function for each
of the sixteen branch pairs. Section5 also gives sup|phi_rs,xy|<1/4.
These two facts have different roles; both are needed below.

## 3. Alias-safe discrete norm estimate

The shared local lemma and its analytic zero-set corollary are proved in
Section6 of `four_branch_parametrix.md`, including all sampling aliases.

Apply this lemma after multiplying away the separable phase phi_rs(0),
which is only a unitary diagonal multiplier on each side. The mixed
derivative is unchanged. Its analytic zero set has area zero. On a
fundamental square remove a smooth neighborhood of that zero set and
of the boundary with arbitrarily small area. The removed kernel has
limiting ordinary (unnormalized) Hilbert–Schmidt norm at most a fixed
amplitude bound times the square root of that area. This norm, unlike the
normalized HS convention used for diagonal channels, directly dominates
the operator norm. Its squared value is an ordinary two-dimensional
Riemann sum N^-2 sum|a_N|². Smooth cutoffs and a uniform supremum bound
make the estimate uniform in N. Cover the remaining compact set by
finitely many rectangles with mixed derivative of fixed sign, bounded
away from zero, and use a smooth partition of unity. Each good piece
tends to zero in operator norm by the lemma. First take N to infinity,
then let the removed area tend to zero. Thus every branch-pair matrix has
norm tending to zero. The finite sum and its O(N^-1) error prove ||Q||->0.

For completeness the zero-set fact follows from analytic one-variable
slicing and Fubini: identically zero slices are contained in the zero set
of a nonzero transverse Taylor coefficient. Analytic continuation handles
charts on which a selected local coefficient might vanish. No quantitative
small-value-set exponent is needed or asserted.

## 4. Dihedral multiplicities, including all reflection cases

This step applies to any unitary U, with q=max P_xy<=1. Put
B_xy=sqrt(P_xy P_yx) and C_xy=P_xy P_yx. By Cauchy–Schwarz and double
stochasticity, B is symmetric substochastic and ||B||<=1. Each B entry
is at most q, and each C row sum is at most q.

Let d(x)=|C(x)| be the least cyclic period. The sum over distinct reverse
rotations before deleting overlaps is sum_x d(x) A(x)conjugate(A(x^rev)).
The sum without the factor d(x) is exactly Tr Q^m. Replacing d(x) by m
costs only proper-period words. For a proper divisor d|m, d<=m/2, their
absolute paired weight is at most q^(m−d) times the length-d B-word
weight. Its sum is q^(m−d)Tr B^d<=N q^(m/2). There are at most m proper
divisors and the multiplicity discrepancy is at most m, giving a total
error at most m²N q^(m/2).

It remains to remove words equal to a rotation of their reversal. For
each such word all involved amplitudes equal A(x), so the deleted weight
is a nonnegative multiple of |A(x)|². Bound its sum by enumerating the
m possible reflections of the cyclic index set:

- If m is even and the reflection fixes two opposite vertices, its quotient
  is a path of m/2 paired edges. The total weight is at most N q^(m/2).
- If m is even and the axis passes through two opposite edges, there are
  m/2−1 paired edges and two endpoint loop factors, each at most q. The
  bound is N q^(m/2+1).
- If m is odd, there are floor(m/2) paired edges and one endpoint loop,
  giving N q^(floor(m/2)+1).

Each paired edge uses C and each free starting vertex costs N; its row-sum
bound proves the three estimates. Overcounting words with multiple
reflections is harmless. The additional rotation multiplicity is at most
m. Thus the deleted overlap costs at most m²N q^floor(m/2).
For m>=2 we have proved the explicit finite bound

|R_m^rev−m Tr Q^m| <=2m²N q^floor(m/2).

For the actual model Section2 gives q=O(N^-1), in particular q<=1/5
eventually. Section3 gives ||Q||<=1/2 eventually. Therefore on every
fixed positive Heisenberg band,

|R_m^rev|/m <=N(1/2)^m+2mN(1/5)^floor(m/2) ->0

uniformly. The weighted conclusion follows by a Riemann-sum bound.
The case m=1 is outside a positive Heisenberg band for large N; its
reverse-only family is empty exactly.

## 5. Strongest safe consequence and remaining boundary

Together with `position_chain_mixing.md`, this determines the entire cyclic
family and removes the specified reverse-cyclic family for the unchanged
operator. It does not remove other ordered noncyclic pairs. In particular,
if R_m^other=|Tr U_N^m|²−D_m−R_m^rev, the weighted pair CUE target remains
exactly

N^-2 sum_m w(m/N) R_m^other ->
integral_0^infinity [min(xi,1)−xi]w(xi) dxi.

Above xi=1 the required correction is negative. It cannot be dropped or
replaced by absolute cancellation. The higher signed factorial hierarchy,
deterministic microscopic law and BGS are not proved here. No unreviewed
reconnection estimate has been incorporated.

The finite-N magnetic-gap/Lindemann–Weierstrass argument in historical
notes is not a dependency of this theorem. It need not be promoted with
this proof and alone would not suffice for Heisenberg-time decay.
