# Uniform massive covariance and formal connected coefficients

Project proof; Sections 3–5 of the source were independently internally
reviewed as formal/local dependencies. No convergence of the formal series
is asserted. The separate finite-order trace-table theorem is
[factorial WKB reduction](fixed-map/factorial_wkb_reduction.md).

## 3. Actual Hessians: uniform mass and inverse decay

For a fixed lifted branch/winding class let
Phi(x)=sum_j S_(r_j)(tau,x_j,x_(j+1)) plus its linear alias terms.
The cyclic Hessian at any real x is nearest-neighbour. At zero coupling,

v^T H_0 v=-(3/2)sum v_j²+(1/2)sum v_j v_(j+1),
so -2I<=H_0<=-I.

The actual specified-time C² bounds give each one-step Hessian entry an
error at most epsilon=10^10 tau+10^50 tau²<2*10^-70. Summing the local
quadratic forms gives ||H-H_0||<=4epsilon, independently of m. All linear
alias/gluing terms leave this unchanged. Repeated neighbours at m=1,2
are counted by this quadratic-form formula, not by an incorrect simple
cycle convention.

Set K=-H. For m>=2 write K=D-R with D diagonal. Uniformly,
D_jj>=7/5 and sum_k |R_jk|<=3/5. Therefore rho=3/7 bounds
||D^-1 R||_infinity. The Neumann series and finite propagation on the
cycle give

sum_k |(K^-1)_(jk)|<=5/4,
|(K^-1)_(jk)| <=(5/4)(3/7)^(d_m(j,k)),                 (B1)

where d_m is cyclic graph distance. At m=1, K>=1-4epsilon>4/5 and
(B1) is immediate. These statements hold at EVERY real stationary class,
not just at a selected orbit. No assumption of absence of orbit clusters
is involved.

In stationary-phase normalization h=(2pi N)^-1, the formal Gaussian
covariance for exp(-i y^T K y/2) is C=-i K^-1. Its absolute row sums obey
the same bound. This is a Fresnel/Wick functional, not a positive measure.

## 4. Uniform local analyticity and the formal object

At fixed tau the one-step HJ solution and every fixed finite set of
transport amplitudes are real analytic, with a common small complex
neighbourhood and bounds independent of the real chart after gluing.
This follows directly from the finite Fourier symbol, the short fixed-time
holomorphic characteristic flow, and its uniformly invertible projection.
Compactness of the finitely many fundamental charts gives common constants.
The leading transport amplitude is nonzero (indeed close to 1); for each
fixed J and small h the finite amplitude polynomial is nonzero on a smaller
common complex neighbourhood. Its logarithm is therefore analytic there.
No analytic-in-J bound is being inferred from fixed-J transport existence.

Expand about any real stationary point x*. Put x=x*+sqrt(h)y, factor
out the phase, its quadratic Gaussian and the leading saddle amplitude.
The remaining exponent is a SUM of local vertices, one for each edge:

- phase vertices of polynomial degree d>=3 carry h^((d-2)/2);
- log-amplitude vertices of degree d>=0 and symbol order s>=0 carry
  h^(s+d/2), with s+d/2>0 after removing the constant leading term.

Every vertex depends on at most (y_j,y_(j+1)). Local analytic Taylor
coefficients are bounded by M R^-(d+s), with fixed M,R>0 independent of
m, the stationary class, and j (constants may depend on fixed J and tau).
The finite-J amplitude polynomial has a local analytic logarithm in h,
so these bounds include its induced infinite formal log series in h.

Let Z_m(h) be the FORMAL Gaussian expectation of the exponential of these
vertices, and write

log Z_m(h)=sum_(k>=1) ell_(k,m) h^k.                   (B2)

Odd half-powers vanish: the total Gaussian degree and the total half-power
grade have the same parity. Equation (B2) is a definition by Wick
contraction of finite polynomials at each order. No convergence of Z or
its logarithm is asserted.

## 5. The constructive coefficient theorem

There is C<infinity, depending only on the above local bounds and not on
m or the stationary class, such that

|ell_(k,m)| <= m C^k k! for every k>=1.                (B3)

PROOF. The formal exponential/logarithm identity expresses ell_k as the
sum of CONNECTED Wick diagrams. This can be proved without probabilistic
input: partition each Wick pairing into its connected components on the
vertex labels, and apply the exponential formula for labelled sets.
The exponential carries 1/r! for r vertices. Self-contractions are allowed.

At order h^k the total half-power grade is 2k. Each nonconstant vertex
has grade at least one, hence r<=2k. If D is total polynomial degree,
phase vertices add two more legs than their grade, while amplitude
vertices add at most their grade. Consequently

D<=2k+2r<=6k; write D=2E, so E<=k+r.

For a connected diagram with r>=2, choose any spanning tree of its
cross-vertex contraction graph by a fixed deterministic rule. For each
fixed choice of which of the two local coordinates each leg uses, sum
site labels from the leaves of this tree. Every removed leaf costs at
most sum_k |C_(a,k+sigma)|<=5/4. Every non-tree covariance costs at most
5/4 as well. The remaining root label has m choices. Thus the ENTIRE
site-label sum for each connected Wick diagram is bounded by

m (5/4)^E,

rather than m^r. This bound does not enumerate spanning trees, so it
introduces no additional r^(r-2) combinatorial loss. A deterministic
spanning tree is selected only to bound each already-counted pairing.
For r=1 the same bound is direct. Degree-zero vertices cannot belong to
a connected diagram with r>=2; their r=1 contributions are bounded separately
by m C^k.

The number of pairings of D=2E labelled legs is
(2E-1)!! <=2^E E!. After the exponential denominator 1/r!,

(2E-1)!!/r! <=2^(k+r)(3k)^k <=C_1^k k!.

If E<r, use E!/r!<=1; otherwise the ratio has at most k factors, each
at most 3k. The last inequality follows from k^k<=e^k k!.

There are only exponentially many ordered grade/type choices at fixed
2k: compositions of 2k contribute at most 2^(2k); choices of phase versus
amplitude and of symbol order/degree contribute another C_2^k. Expanding
a two-variable degree-d local polynomial gives at most d+1<=2^d monomial
choices. Their product and the analytic coefficient bounds contribute
C_3^k because D<=6k, r<=2k and total symbol order <=k. Collecting the
bounds proves (B3). END PROOF.

This theorem establishes dimension-uniform Gevrey-1 FORMAL log coefficients.
In particular ell_1=O(m), and at m~N its contribution h ell_1 is O(1).
For fixed k>=2, h^k ell_k=O(N^(1-k)). Thus resumming the first extensive
correction is structurally appropriate. The theorem does not justify
truncating the infinite formal series or identify it with an actual integral.

## Exact controls and boundary

`computations/verification/heisenberg_wkb/cluster_checks.py` checks exact
rational covariance and toy connected-cumulant identities in dimensions
1 through 18, and bounded factorial inequalities. These are algebra controls.
The [rotated-box theorem](rotated_local_first_loop.md) proves a local actual
integral first-loop result. A separate [global contour theorem](global_rotated_box_trace.md)
now controls deformation and the summed contour tail in its finite band.
Neither this formal coefficient bound nor the local first-loop estimate
provides entropy-compatible signed evaluation of the box sum.
