# Independent audit: radial resolvent addendum

## Claim and primary verdict

**Proved as written**, relative to C1/C6 of the companion radial-shell
theorem, independently audited in `review.md`. No additional actual-map
analytic input is required.

Audited addendum SHA256:
`d76af5e9ad8cff4df4b015698c77d3d1ecebffe1103e5e09966d670f9aaedfd6`.
Its stated parent is the radial-shell candidate at SHA256
`43319ca5c799fd6e10479fca71e8c8fa5d7783dcd38b7493e48bba11218de37a`.
Both pins were verified directly. This is independent internal review;
canonical BGS remains read only.

For the centered, untwisted transfer L=zT+delta D, z=1-delta and every
positive delta_N tending to zero, the addendum proves uniformly for
|xi|>=1:

    delta ||D(xi-zT)^(-1)|| ->0,
    delta ||(xi-zT)^(-1)D|| ->0,
    delta ||(xi-L)^(-1)-(xi-zT)^(-1)|| ->0.

The resolvent difference is also o(1) relative to the normal resolvent
norm at each point, uniformly in that region. The worst unit-circle
resolvent norm is delta^(-1)(1+o(1)), equivalently the least singular
distance to the unit circle is delta(1+o(1)).

## 1. Arc split, including the right-sided estimate

Write R_0(xi)=(xi-zT)^(-1) and xi=r exp(i phi), r>=1. Eventually
0<delta<1/2, so z>=1/2. Since T is unitary,

    ||R_0(xi)|| <= 1/(r-z) <=1/delta.

For a spectral value exp(i theta) of T, let alpha be its wrapped angular
distance from exp(i phi), 0<=alpha<=pi. Exactly,

    |xi-z exp(i theta)|^2
      =(r-z)^2+4rz sin^2(alpha/2).

The elementary bound sin(alpha/2)>=alpha/pi and rz>=1/2 give

    |xi-z exp(i theta)| >= (sqrt(2)/pi) alpha.

Let epsilon=sqrt(delta), and let E be T's spectral projection onto
the angular epsilon-arc around xi/|xi|. Then

    ||R_0(xi)(I-E)|| <= pi/(sqrt(2) epsilon)

uniformly in xi, N, and the spectrum. The spectral projection commutes
with R_0(xi). Consequently

    delta ||D R_0(xi)||
      <= ||DE|| + (pi/sqrt(2)) delta/epsilon,
    delta ||R_0(xi) D||
      <= ||ED|| + (pi/sqrt(2)) delta/epsilon.

Here ||D||<=1 was used for the off-arc terms. C1 gives both
sup ||DE|| ->0 and sup ||ED||=sup ||D*E|| ->0. Since
delta/epsilon=sqrt(delta), both claims R1 follow. The second estimate
genuinely uses the adjoint half of C1; there is no assumption that D is
self-adjoint or that D commutes with the spectral projection.

This argument works for every vanishing delta_N sequence, regardless of
its speed relative to N. The arc norm control is qualitative but already
uniform over all arc centers, so no quantitative Egorov rate is hidden.

## 2. Exact factorization and uniform Neumann control

Set

    alpha_N=sup_(|xi|>=1) delta_N ||D_N R_0(xi)||.

The preceding step gives alpha_N ->0. Direct multiplication, preserving
operator order, gives

    xi-L=[I-delta D R_0(xi)](xi-zT).

For all sufficiently large N, alpha_N<1, so the bracket is invertible
for every |xi|>=1. In particular the perturbed resolvent exists throughout
the claimed closed region. Its exact expression is

    R_L(xi)=R_0(xi)[I-delta D R_0(xi)]^(-1).

Therefore

    ||R_L(xi)-R_0(xi)||
      <= [alpha_N/(1-alpha_N)] ||R_0(xi)||.

This is precisely R3, with one uniform o(1) coefficient. Multiplying
by delta and using delta||R_0(xi)||<=1 proves R2. There is no need to
assume L normal, diagonalizable, or close to normal. The argument does
not use its spectral radius to bound a resolvent.

The symmetric factorization, if desired, uses the other half of R1:

    xi-L=(xi-zT)[I-delta R_0(xi)D].

It is consistent with the first factorization but is not necessary for
the stated R2/R3 bounds.

## 3. Sharp unit-circle scale

Let beta_N=alpha_N/(1-alpha_N), so beta_N ->0. On |xi|=1,

    ||R_L(xi)|| <= (1+beta_N)/delta.

The centered space is nonzero for odd N>=3. Choose xi equal to any
eigenvalue of T on that space. For the normal operator zT,

    ||R_0(xi)||=1/delta.

The reverse triangle inequality and R3 give

    ||R_L(xi)|| >= (1-beta_N)/delta.

Taking the supremum on the unit circle proves

    delta sup_(|xi|=1) ||R_L(xi)|| ->1.

For each xi the matrix is invertible and
sigma_min(xi-L)=1/||R_L(xi)||. Hence exactly

    inf_(|xi|=1) sigma_min(xi-L)/delta
      =1/[delta sup_(|xi|=1) ||R_L(xi)||] ->1.

Both assertions R4 follow. The proof handles the finite-dimensional
nonnormal singular scale, not merely the radial location of eigenvalues.

## 4. Dependency and obligation matrix

- C1 left spectral-arc annihilation: inherited from reviewed companion.
- C1 adjoint annihilation and ||ED|| identity: passed.
- Uniform geometry for every |xi|>=1: passed.
- All vanishing delta sequences and all odd N eventually: passed.
- Noncommutative factor order: passed.
- Uniform invertibility by Neumann series: passed.
- Relative norm estimate R3: passed.
- Scaled absolute estimate R2: passed.
- Both sharp worst-case bounds in R4: passed.
- Normality of L: not assumed or needed.
- Spectral-radius-to-resolvent inference: not used.
- Spectral-radius-to-power-norm inference: not used.
- Trace-class, trace subtraction, and signed cancellation: not proved.
- Arbitrary occupation/Hamming twists: outside the theorem.

## 5. Boundary relevance and remaining gap

The addendum is a legitimate strengthening: at every vanishing switch
scale, the actual untwisted transfer has the same leading worst
unit-circle resolvent scale as the radially contracted unitary zT.
Thus possible nonnormal resolvent inflation does not change this leading
external unit-circle scale.

This still does not estimate the signed marked-switch boundary. The
ordinary trace bound costs dimension N^2, and no cancellation inside
the occupation subtraction or the high-Hamming extraction is supplied.
The statement is for q=1, theta=0. Extending it to the generating
transfer's twists requires new hypotheses or a new argument. Nothing
here controls microscopic eigenphase correlations or removes the switch
regulator.

No mathematical correction to R1–R4 is needed. The strongest safe
conclusion is exactly their operator-norm resolvent comparison and sharp
singular scale. All quantitative rates beyond o(1), arbitrary-twist
uniformity, and the signed Heisenberg closure remain unproved.
