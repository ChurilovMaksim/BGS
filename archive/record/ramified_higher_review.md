# Curated higher-ramified v2 review

Exact original review and candidate correction lineage are retained in
record/history/2026/ramified_higher_20261006. Historical execution filenames below refer
to that review; new portable executions have separate receipts.

# Independent audit: actual common commutant for odd multiples of 245

## Primary verdict

**Proved as written for the corrected frozen v2 candidate:** for every odd
integer N divisible by 245, the actual prescribed pair (A_N,M_N) has scalar
complex common commutant. The verdict is bound to
`ramified_higher_seven_lift_v2.md`, SHA-256
`da6e802bb121912948c6e34c96aede4f4046c7a1ffe9feb841907a45199dc61c`.

This is an independent internal mathematical audit with exact finite inputs,
not an external-referee certificate or formalization. The finite computations
check the stated bases and dictionaries. The universal conclusion additionally
uses the uniform arguments reconstructed below and the explicitly inherited,
previously reviewed polynomial certificates. Neither all-N spectral simplicity,
the full complex commutant of a single U_N, quantitative spectral gaps,
TRACE-005, nor microscopic BGS is proved here. Combining other theorem families
is outside this audit's claim.

The original candidate, hash
`f48b530afd255b5bd4ae2c86799723107736ed02a31cb4dc69342a30e7411052`,
had one finite-witness gauge/provenance discrepancy. The supplied base program
uses the actual unit-upper gauge, whereas the original prose literally called
that witness the effective-gauge kernel. The v2 paragraph explicitly separates
these and proves their geometric-gauge transfer. No other source paragraph
changed. Independently, both sets of six literal witnesses pass, so the
discrepancy is not a counterexample to the theorem. The original is retained.

## Claim card and dependencies

Write N=5^e n, e>=1, 5 not dividing n, n=7m, and 7 dividing m. Then
L=N/7=5^e m. The actual matrices use the modular half-shift h=2^(-1) modulo N,
positions a+t+jL with a=1-h, and

- 1000A(x,x+1)=(-3-4i)r((x+h)/N);
- 1000A(x+1,x)=(-3+4i)r((x+h)/N);
- r=-(z^7-1)^2(z+1)^2/(4z^8);
- G(x,y)=q^(-8^(-1)(3x^2-2xy+3y^2)), with M=G/sqrt(N).

The scalar changes from (A,M) to (1000A,G) do not change the common
commutant. Work over a finite extension E of Q_5 containing these algebraic
coefficients and sigma of valuation -3/4. The residue characteristic is five,
with i reducing to two, q reducing to exact order n, Q=q^7 reducing to order m,
and omega=qbar^m of order seven. All spaces and lattices below are finite.

Dependency graph:

1. Actual Jacobi and raw-kernel definitions, chain ordering and valuations.
2. Exact row recurrence for every integral actual commuter; graded error bound.
3. q-Lucas and ordinary Lucas identities; simultaneous unit gauge into the
   mixed-digit Toeplitz algebra.
4. Highest-to-lowest high-digit Fourier block equals a shifted, invertible
   prime-to-five base kernel.
5. Scalar shifted base commutants: inherited exact polynomial certificates
   plus a newly checked shifted-pole dictionary and tail argument for m>=21;
   six exact dimension49 bases for m=7.
6. High-digit coefficient induction; saturated integral lattice; extension
   of algebraic matrix rank from the number field to E and C.

Every implication passed. The inherited polynomial input is precisely the
source-bound accepted `actual_family_review.md`, including completed norm,
factor-product and irreducibility checks. Its old theorem excluded 5|N. This
audit does not extend that theorem by assertion: it separately verifies the
shifted base argument using the stronger independent-pole polynomial identity
already established inside its certificate.

The accepted source proof at hash
`47b2692f034a23888d4223e73120a685609a6ca58c2a983293310bc735e42d4f`
was compared with the candidate's dependency at hash
`cc90a3e0fc2354692e93aac2f8f5948d5d62fec58b563ae96292f418a182b725`.
The differences are review-status wording and corrected completed-certificate
locators. No mathematical claim was enlarged. Copies of both are retained.

## Obligation matrix

| Obligation | Disposition | Basis |
|---|---|---|
| Actual matrix and prime normalization | Passed | Laurent identity and exact coefficients |
| Internal valuations and every chain boundary | Passed | Internal u<L; boundary bonds vanish exactly |
| Recurrence grade, including s<r | Passed | Induction on row and uniform valuation inequality |
| Gaussian ratio and simultaneous gauge | Passed | Product calculation; independent finite controls |
| Mixed-digit carry zeros | Passed | q-binomial product identity and characteristic-five Lucas |
| Exact endpoint block and invertibility | Passed | Direct gauge/position calculation |
| Independent primitive pole parameter | Passed | Fourier interpolation removes the grid; inherited norm |
| Shifted higher tails | Passed | H is a common invertible left factor at every depth |
| Six short bases | Passed | Independent effective and unit-upper constructions |
| Every high-digit coefficient | Passed | Multi-index induction using one invertible block |
| Saturation and characteristic-zero conclusion | Passed | Reduction kernel is exactly pi times the lattice |
| Spectral simplicity/BGS/full single-U commutant | Out of scope | No implication asserted |

## 1. Actual recurrence and valuation bound

At this Gaussian prime, the constants -3-4i and -3+4i have valuations zero
and two. Each nonzero internal bond r_u has valuation in [0,1/2]. Indeed,
z+1 is a unit because its residue has odd order. A positive valuation of
1-Q^u can occur only when its nontrivial root-of-unity order is a power 5^b,
and then v(1-Q^u)=1/(4*5^(b-1))<=1/4. Internal u<L excludes Q^u=1 in
characteristic zero. The seven boundary bonds u=L are zero exactly and are
never divided by. The actual diagonal of 1000A has valuation at least one.

The displayed D=lambda U is exactly the inverse-upper-bond recursion, since
b_(u,j)=(3+4i)q^(-8u)w^(-j)(Q^u-1)^2(1+q^u w^j)^2/4.
Consequently sigma D^(-1)(1000A)D has upper blocks I, diagonal blocks of
valuation >=1/4, and lower blocks of valuation
1/2+2v(r_u)>=1/2. U and its inverse are integral units.

The row recurrence is the actual commutator equation, not a surrogate:

S_(r+1,s)=S_(r,s-1)+S_(r,s)V_s-V_rS_(r,s)
          +S_(r,s+1)W_s-W_(r-1)S_(r-1,s).

For a contribution from first-row coefficient C_d to S_(r,s), let a be the
number of diagonal insertions and b the number of lower insertions. Induction
on r gives d-s+r=a+2b. Its coefficient has valuation >=a/4+b/2.
The term with a=b=0 is C_(s-r), with coefficient one, and occurs exactly when
s>=r. Terms outside the column range, and terms in negative rows, are zero.
Truncation removes paths; it creates no lower-grade contribution. The last row
commutator equations are additional constraints; the forward recurrence does
not need to solve them to obtain this necessary form.

Since C_d=lambda_d Ctilde_d and Ctilde_d=X_(0,d)U_d is integral, a correction
with h=d-s+r>0, after scalar-depth conjugation, has valuation at least

h-F(d)+F(s)-F(r), where F(t)=2 sum_(u=1)^t v(1-Q^u).

The exact product identity
lambda_r lambda_d/lambda_(r+d)=q^(-8rd)[r+d choose r]_Q^2
proves F(r+d)>=F(r)+F(d) whenever r+d<L. Every increment of F is <=1/2.
For s>=r, put k=s-r; then d=k+h, so F(d)<=F(k)+h/2 and
F(s)>=F(r)+F(k). For s<r, put k=r-s; then h=d+k,
F(d)<=d/2 and F(r)-F(s)<=k/2. Both give the uniform bound h/2>0.
All F-indices used are <L, even if r+d>=L. Thus every discarded actual
diagonal/lower contribution vanishes on reduction, including below the diagonal.

## 2. The simultaneous tensor gauge

The q-binomial product identity, grouped into complete odd m-blocks, gives
q-Lucas at Qbar of order m. The whole-block product is 1+z^m. Comparing the
usual Gaussian coefficient phases yields no residual phase because m is odd.
The characteristic-five identity (1+z)^5=1+z^5 then gives ordinary digitwise
Lucas. Therefore the squared coefficient is zero exactly in a carried digit,
and otherwise equals f_s/(f_r f_(s-r)). Each f_t is a unit: low products stop
strictly below m, and the high-digit factorials stop at four.

The conjugation is explicitly

Y=diag(f_t qbar^(-4t^2)) Shat_bar diag(qbar^(4t^2)/f_t).

For d=s-r, its phase is
qbar^(-8rd+4s^2-4r^2)=qbar^(4d^2), and the factorial ratio becomes 1/f_d.
Thus the carry-free entries are precisely the monomials in
J_m tensor J_5 tensor ... tensor J_5, with chain-matrix coefficients Chat_d.
Since Shat=U^(-1)XU, the same total conjugation of G is exactly
D_eff^(-1)G(qbar)D_eff. No nonunit Fourier normalization or independent change
of the two generators has been introduced.

## 3. Exact highest/lowest block

Write p=5^e-1=7k+r. Powers of five modulo seven give r in {0,1,2,3,4,5},
never six. Let T=mp. Relabel chains by j'=5^e j modulo seven. Both positions
and U then use the common grid omega. The reduction of the original modular
half-start a_N is the base half-start a_n, since 5^e is odd.

There is a particularly direct proof of the endpoint identity. For s<m,
the highest high-digit factorial contribution is (4!)^(2e)=1. Because 7|m,
the square-depth phase has qbar^(4T^2)=1 and cross term omega^(ps), while
omega^(jT)=1. Hence its numerator is exactly the numerator of the base gauge
at (s,j+r). Splitting the denominator product at T gives

prod_(u=1)^(T+s)(1+qbar^u omega^j)^2
 =4^k h_r(j) prod_(u=1)^s(1+qbar^u omega^(j+r))^2.

Every complete n-block contributes four. Thus
D_eff,N(T+s,j)=D_eff,n(s,j+r)/(4^k h_r(j)). The raw row position also shifts
from j to j+r. These two exact equalities give
E=4^k(I_m tensor H_r)K_n with no missing row, column, or scalar phase.

The base raw Fourier-type matrix is invertible because n is prime to five
and qbar has order n. All diagonal gauge factors, h_r(j), and the scalar four
are units. Therefore E is invertible even though the full reduced N-kernel
is singular.

## 4. Shifted base lemma and exact certificate reuse

In the effective base gauge the actual reduced upper generator is cJ,
c=4qbar^(-4). D_unit=D_eff c^(-t) turns it into J. This geometric factor
commutes with every H_r because H_r acts only on chain labels. This validates
the repaired v2 finite-witness dictionary.

For long chains, write the accepted last-row blocks as u_s v_s^T. Left
multiplication by H_r changes the independent columns to H_r u_s and leaves
every right row v_s unchanged. The penultimate block transforms as

H_r Q u_0 v_0^T R=(H_r Q H_r^(-1))(H_r u_0)v_0^T R.

Since H_r=diag(h_r) times the shift j -> j+r, conjugation replaces the pole
coefficient omega by eta=omega^(r+1). Its diagonal entries are
(1+eta qbar^(-1)omega^j)^(-2). Eta is primitive for all six allowed r.
The left diagonal h_r does not produce an extra pole factor.

To check that the previously accepted polynomial theorem really covers an
independent eta, put z_j=omega^j and
H(z)=prod_(u=1)^6(1+qbar^u z)^2. The accepted normalized row matrix has the
factorization V=C(qbar)F_omega diag(z_j^3/H(z_j)). On conjugating the pole
matrix, the column diagonals cancel. Fourier interpolation of
H(z_j)/(1+eta qbar^(-1)z_j)^2 produces the coefficient row of
H(z)/(1+eta qbar^(-1)z)^2 modulo z^7-1. The grid omega has disappeared.
Thus the numerator is precisely the accepted K(qbar,eta), with denominator
an associate of P(qbar)(qbar^7+1)^2. It is not a new unverified two-parameter
polynomial. The accepted norm over Phi7 excludes its zeros for every primitive
eta whenever qbar has order divisible by49. The accepted y_j conditions are
unchanged. The same two-row argument, keeping C_1's column-zero contribution,
therefore forces scalar C_0.

The tail argument also survives. Subtract the scalar and take the least
d>0 with C_d nonzero. If d<=m-7, last-row columns d through d+6 isolate
v_s^T C_d=0 by independence of the seven H_r u_s. If d>=7, the bottom d rows
at column d give H_r K_(t,0)C_d=0; invertibility of H_r removes it, and seven
consecutive right Fourier rows force C_d=0. For m>=21 every positive d belongs
to at least one case. The only shorter allowable m is seven.

For m=7, the independent exact construction checks all six shifts, in both
effective and unit-upper gauges. In each case the vector at depth-major index
24 is cyclic for the stated J+H_r K, with rank49, and the commutator-column
matrix has rank48. If X commutes with J and H_r K, then X is a polynomial in
the cyclic T of degree <=48. The rank48 test kills every nonconstant
coefficient. Since ord_49(5)=42=degree(Phi49), this field calculation covers
every primitive49 root by Frobenius conjugation. The failed endpoint-vector
attempt is provenance only and is not used.

## 5. High-digit induction and saturation

Index high blocks by multi-indices in {0,...,4}^e. Let H=(4,...,4), and let
Y_D be the low/chain-matrix coefficient of the high monomial D. The highest
row of Y has only Y_0; the lowest column has only Y_0. Therefore the (H,0)
block equation gives [Y_0,E]=0. As Y_0 also commutes with J_m tensor I_7,
the shifted base lemma proves Y_0 scalar.

In the (H,D) equation, scalar Y_0 terms cancel and the remaining terms are
-sum_(0<=A<=D,A!=D) K_(H,A)Y_(D-A). Induct on the sum of D's coordinates.
For A!=0, the positive degree of D-A is strictly smaller, so those terms
vanish. The remaining term is -E Y_D. Invertibility of E gives Y_D=0.
This checks the exact multi-index orientation and includes any number of
ramification digits; no invertibility of other high blocks is assumed.

Let C be the E-common commutant and L=C intersect M_N(O_E). It is a full,
finite free lattice. Every X in L has scalar reduction after the invertible
unit transformations already proved, so X itself has scalar reduction.
If all entries of X are divisible by a uniformizer pi, X/pi is still both
integral and an actual commuter. Hence the reduction kernel is exactly pi L.
It follows that rank(L)=dim_k(L/pi L)<=1. The identity supplies the reverse
inequality. Thus dim_E C=1. The coefficient matrices are algebraic over a
common number field, and rank is invariant under embedding/field extension
to E or C. This proves the complex statement.

## 6. Independent finite evidence and reproduction

`independent_checks.py` imports no author verification program. It implements
field multiplication by a monomial long-reduction table for Phi49 and field
inversion by the polynomial Euclidean algorithm. All arithmetic is exact;
there is no floating tolerance or random sampling. The raw metaplectic kernel,
effective gauge, unit-upper gauge, H_r, pole blocks and Gaussian recursion are
rebuilt from their definitions. The q-Pascal recurrence is the alternative
one to that used in the supplied dictionary script.

Completed scopes:

- Six shifted dimension49 bases in the literal effective gauge, and six in
  the unit-upper gauge: all cyclic ranks49 and commutator-column ranks48.
- Full squared q-Lucas coefficient triangles at N=245,1225,6125,735:
  404845 entries, including their carried zero entries. N6125 independently
  exercises three high digits, beyond the supplied e<=2 controls.
- All endpoint-block entries in those four cases: 28812 identities, plus
  420 explicit simultaneous phase/factorial gauge identities at N245.
- All49 entries of each of six shifted n147 penultimate identities.
- All36 independently varied seventh-root evaluation-grid/pole pairs at
  q of order49, checked against the frozen accepted polynomial dictionary.
- Row-recursion support grades at L=1,2,3,7,35, including truncated boundaries;
  exact rational valuation inequalities in five declared (m,e) regimes.
  The three fully enumerated correction ranges contain 5445020 triples.

From this audit directory run:

    OPENBLAS_NUM_THREADS=1 python independent_checks.py bases
    OPENBLAS_NUM_THREADS=1 python independent_checks.py unit_bases
    OPENBLAS_NUM_THREADS=1 python independent_checks.py dictionary
    OPENBLAS_NUM_THREADS=1 python independent_checks.py poles
    OPENBLAS_NUM_THREADS=1 python independent_checks.py grades

Each successful command writes its matching `*_results.json`; a disabled
assertion interpreter is rejected. The manifest binds frozen inputs, code,
outputs, runtime and environment. Integer convolution/reduction sums and raw
Fourier matrix-vector sums are far below int64 overflow. The earlier
degree828 norm factorization is inherited with its original independent
completed review, not rerun or relabeled as a new computation here.

No canonical repository file was written by this reviewer. The canonical tree
was already being edited by the parent for other reviewed work; its current
dirty state is recorded without attributing those edits to this audit.

## Remaining issues and strongest safe statement

The original finite-witness gauge discrepancy is resolved by the source-bound
v2 paragraph. No remaining mathematical gap was found in this exact claim.
The strongest accepted statement of this audit is scalar actual pair
commutant for every odd 245|N, with the preceding explicit dependencies.
Promotion should cite v2, this review, the independent finite outputs and the
accepted unramified polynomial review. Other families and BGS conclusions must
retain their separate proofs and review boundaries.
