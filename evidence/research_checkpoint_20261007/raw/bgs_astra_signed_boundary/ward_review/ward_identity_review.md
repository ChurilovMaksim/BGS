# Exact switch source, diagonal Ward identities, and a nonvanishing control

Date: 7 October 2026. Scope: independent finite-dimensional algebraic review of the endpoint source in `global_switch_transfer.md`, not an asymptotic endpoint estimate. Canonical BGS files are read-only and unchanged. All matrices below are auxiliary controls, not the prescribed BGS quantum map.

## Result and claim card

**Verdict: the twirl and endpoint trace identities are proved as written. Universal Ward vanishing is refuted by an explicit dense rational example at odd dimension 3, even under a strict centered one-step gap.**

Quantifiers: every integer N>=1, U in U(N), integer m>=1, and arbitrary occupation phases theta in R^N. Hilbert space H=End(C^N) has the ordinary Hilbert--Schmidt inner product `<X,Y>=tr(X*Y)`. `tr` denotes the N-dimensional matrix trace; `Tr` denotes the N^2-dimensional superoperator trace. Indices are modulo N. Let

- `E_(c,j)=|j><j+c|`, and `P_c` the orthogonal projector onto their span;
- `T=Ad(U)`, `D=sum_c P_c T P_c`;
- `omega=exp(2 pi i/N)`, `Z_b=diag(omega^(bj))`, `R_b=Ad(Z_b)`;
- `Z_theta=diag(exp(i theta_j))`, `V=Ad(Z_theta)`, `W=Z_theta U`;
- `A=VT=Ad(W)`, `B=VD`, `S=A-B=V(T-D)`.

All conclusions through the counterexamples use only finite matrix algebra. The conditional gap consequence explicitly assumes `||D|I^perp||<=rho<1`; it does not establish that estimate for the actual map.

Dependencies: character orthogonality -> pinching identity; multiplication and trace of adjoint representations -> endpoint trace formula; unitary norm identity -> Dirichlet form; cyclic trace invariance -> Ward identities. No external theorem or asymptotic input is needed. Exact computations check the stated examples and indexing, rather than proving the universal algebraic identities.

## 1. Charge pinching is a finite diagonal twirl

One has `R_b E_(c,j)=omega^(-bc) E_(c,j)`. Therefore, for an arbitrary superoperator C,

`P_c [(1/N)sum_b R_b C R_b*] P_d`
`= [(1/N)sum_b omega^(b(d-c))] P_c C P_d`
`= 1_(c=d) P_c C P_c`.

Consequently

`D=(1/N)sum_b R_b T R_b*`.                                      (1)

The sign in the character is fixed by the stated basis `|j><j+c|`; reversing it does not change the final projector. Since V commutes with every R_b and preserves every charge space,

`B=VD=(1/N)sum_b R_b A R_b* = sum_c P_c A P_c`.                  (2)

Thus the occupation-twisted problem is exactly the same algebra with U replaced by W=Z_theta U. No occupation phase averaging is being inserted into U as an assumption about randomness.

## 2. Endpoint marked traces

For `M(z)=zA+(1-z)B`, the noncommutative product rule and cyclicity give

`d/dz Tr M(z)^m = m Tr[M(z)^(m-1)(A-B)]`.

At z=1 this is `h_m(theta)=m Tr[A^(m-1)S]`. Products of adjoint maps satisfy `Ad(C)Ad(E)=Ad(CE)`, and

`Tr Ad(C)=|tr C|^2`

for every square C (using Ad(C)X=CXC*, with C unitary whenever composition with adjoints is used here). Applying (2) gives

`h_m(theta)=m ( |tr W^m|^2`
`  - (1/N)sum_b |tr(W^(m-1) Z_b W Z_b*)|^2 )`.                 (3)

In particular theta=0 gives exactly

`m Tr[T^(m-1)(T-D)]`
`=m ( |tr U^m|^2 - (1/N)sum_b |tr(U^(m-1)Z_b U Z_b*)|^2 )`.

Every quantity in (3) is real, but the difference has no fixed sign. At m=1 it is zero because pinching preserves superoperator trace, equivalently because `tr(Z_b W Z_b*)=tr W`.

The exact off-charge endpoint source is

`h_m(0)-integral_(T^N) h_m(theta) dtheta`.                     (4)

The torus integral is normalized and removes precisely the nonzero integer occupation Fourier modes, as in the supplied transfer. Formula (3) does not cause (4) to vanish.

## 3. The commutant has positive real dissipation, not source vanishing

Write `A_b=R_b A R_b*=Ad(Z_b W Z_b*)`. All A_b are unitary on H. Define the rotated source

`K=A* S=I-(1/N)sum_b A* A_b`.

For every X in H, direct expansion of squared norms proves

`Re <X,KX> = (1/(2N))sum_b ||AX-A_b X||_HS^2 >=0`.             (5)

This is a genuine real Dirichlet form for the rotated source. The unrotated S need not be accretive on all H.

For `X in Fix(A)=Comm(W)`, AX=X, so (5) specializes to

`Re <X,SX> = (1/(2N))sum_b ||X-A_b X||_HS^2 >=0`.              (6)

Its zero set inside Comm(W) is exactly

`Comm(W) intersect (intersection_b Comm(Z_b W Z_b*))`.         (7)

In particular identity lies in the kernel. Nothing makes the whole commutant lie in the kernel. Equality in (6) forces every summand to vanish; conversely simultaneous fixedness makes S X=0. Do not replace positive real quadratic form by a claim that the uncompressed source is a positive self-adjoint operator or that it preserves the commutant.

If the supplied branch's one-step hypothesis `||D|H0||<=rho<1`, `H0=I^perp`, is available, V is unitary and preserves H0. Hence for every centered X in Comm(W),

`Re <X,SX> = ||X||^2-Re<X,VDX>`
`          >=(1-rho)||X||^2`.                                (8)

Therefore the source is strictly nonzero on every nonzero centered commuter under that hypothesis. A unitary N-by-N matrix has commutant dimension at least N, so for N>=2 this is a substantial subspace. This coercivity statement alone controls neither `Tr[A^(m-1)S]` nor its occupation-subtracted, time-weighted signed aggregate.

## 4. What simultaneous diagonal invariance actually cancels

Let Y be any diagonal unitary and L=Ad(Y). Replacing U by Y U Y* transforms T,D,A,B,S by simultaneous conjugation with L because L commutes with the charge projectors and V. Thus every full trace `Tr M(z)^m` is unchanged. Infinitesimally,

`m Tr[A^(m-1)[J,A]]=0`                                      (9)

for every superoperator generator J. This kills tangent commutators. It does not kill the finite average chord `A-(1/N)sum_b R_b A R_b*`.

An exact finite Ward identity records the distinction. Since `Tr A_b^m=Tr A^m`, telescoping and then subtracting the first-order term gives

`m Tr[A^(m-1)(A-A_b)]`
`=sum_(k=0)^(m-1) Tr[(A_b^k-A^k)(A_b-A) A^(m-1-k)]`.         (10)

Averaging (10) is an exact rewrite of h_m. Each right-hand term is at least quadratic in the finite chord after a second telescoping expansion. The chord is not a small parameter, so this is not a boundary estimate or a vanishing identity.

There is also an exact charge-projector form:

`A-B=(1/2)sum_c [P_c,[P_c,A]]`,

`h_m(theta)=-(m/2)sum_c Tr([P_c,A^(m-1)] [P_c,A])`.           (11)

For m=1 this is zero. For m>1 it is generally nonzero; the factors in (11) are not adjoints of one another in general. This explains why an infinitesimal gauge identity cannot be substituted for source cancellation.

At the path level simultaneous diagonal conjugation changes an edge U_jk by `exp(i(phi_j-phi_k))`, which telescopes to 1 around each closed x path and each closed y path separately. It does not test the occupation difference `n(x)-n(y)`. Left multiplication by Z_theta, which produces the occupation projector, is a different operation. Haar left-diagonal invariance is an ensemble statement and does not furnish fixed-U vanishing.

## 5. Dense rational odd-dimensional counterexample, with a strict gap

Take N=3 and

`U=(1/9) [[7,-4,-4],[-4,1,-8],[-4,-8,1]]`
` = I-2 v v*,  v=(1,2,2)^T/3`.

This is a real symmetric dense unitary, `U^2=I`, `tr U=1`. The charge blocks of D have characteristic polynomials

- c=0: `(lambda-1)(9 lambda+7)(27 lambda-11)/243`;
- c=1,2: `(9 lambda+1)(81 lambda^2-24 lambda-25)/729`.

D is self-adjoint. Its nontrivial eigenvalues are `-7/9`, `11/27`, and, twice each, `-1/9`, `(4-sqrt(241))/27`, `(4+sqrt(241))/27`. Since `sqrt(241)<17`, their largest absolute value is 7/9. The unique eigenvalue 1 is the identity direction. Thus

`||D|H0||=7/9<1`.                                           (12)

Set `X=U-I/3`. It is centered, commutes with U, and has `||X||^2=8/3`. Direct rational multiplication gives

`(T-D)X=(1/243)[[64,8,8],[8,-32,-128],[8,-128,-32]]`,

`<X,(T-D)X>=256/243>0`.                                    (13)

The commutant source does not vanish even in the same abstract strict-gap class used by the regularized transfer.

For m=2, (3) gives

`h_2(0)=2816/243`.

For a hand check, b=0 contributes `|tr U^2|^2=9`; for b=1,2, `|<v,Z_b v>|^2=1/9`, hence `tr(U Z_b U Z_b*)=-5/9`. Therefore the average subtracted in (3) is `779/243`, giving the stated source.

The once-counted m=2 switch polynomials, obtained also by enumerating the 81 ordered pairs `(x,y) in {0,1,2}^2 x {0,1,2}^2`, are

`Tr[zT+(1-z)D]^2 = 779/243 + (1408/243) z^2`,

`G_(3,2)(z,1) = 1046/729 + (3200/729) z^2`.

The occupation condition in the second line is literal equality/inequality of coordinate counts. In particular

`G'_(3,2)(1,1)=6400/729 !=0`.                                (14)

Thus subtracting the occupation-balanced contribution does not create universal cancellation.

Finally use the same U and the occupation twist `Z_theta=diag(1,-1,1)`. Then B=VD has exactly the same centered singular norm 7/9, but

`h_2(theta)=-9728/6561<0`.                                   (15)

The full endpoint marked trace is therefore sign-indefinite even with this strict one-step gap. Positive real dissipation on the commutant must not be promoted to positive marked traces.

## 6. Verification scope and exact remaining gap

`check_ward.py` uses exact SymPy arithmetic over Q(i,sqrt(3)), with no floating tolerance or randomness. It checks N=3 at the untwisted fixture and two occupation twists, m=1,...,6, including the twirl, twisted identity, endpoint trace formula, both Ward rewrites, and Dirichlet identities. It verifies the charge-block characteristic polynomials, the strict centered norm, all 81 m=2 ordered path pairs with the literal occupation mask, and selected direct polynomial/gauge-conjugation identities. `exact_results.json` records its actual output. `computation_manifest.json` records provenance and hashes.

Obligations: finite twirl **passed by proof**; endpoint formula **passed by proof**; twisted extension **passed by proof**; positive real commutant form **passed by proof**; universal source/Ward vanishing **failed by exact counterexample**; actual BGS centered-gap input **not re-audited here**; signed undamped Heisenberg aggregate **not addressed**.

The remaining target is exactly the signed, occupation-masked, high-Hamming/high-switch boundary integral in T16 of the supplied transfer. None of (5)--(15) bounds that quantity at Heisenberg scale. The counterexamples reject a universal algebraic cancellation mechanism; they do not refute that actual-map asymptotic target.

Bounded prior search: canonical `mathematics/` and `record/` were searched for Ward, pinching, dephasing, Dirichlet, switch, and commutant terminology. Existing low-switch and frozen-operator/Dirichlet programs are prior context; this note claims no novelty. Its algebra is rederived from the exact supplied definitions.
