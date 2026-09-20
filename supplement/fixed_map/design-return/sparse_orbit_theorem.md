# Sparse Weyl words on arbitrary odd Pell periods

Project derivation, 18 September 2026, based on local revision
`e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`. Self-reviewed below;
no external review, Lean certificate or priority claim. This strengthens
the finite-symbol normal form but does not solve fixed-map BGS.

Write beta=1+sqrt(2), lambda=beta^2,

    N_k+F_k sqrt(2)=beta^k,    S=[[3,4],[2,3]],

and let K>=3 be odd, N=N_K. All labels are in (Z/NZ)^2.

## 1. Exact fixed submodules

For every odd d,

    B_d=[[N_d,2F_d],[F_d,N_d]],
    det(B_d)=-1,    S^d-I=2N_d B_d.                    (1)

If d divides K, then N_d divides N_K. Indeed, factor S^K-I by S^d-I
and use (1); right multiplication by the integer inverse of B_K shows
that N_K/N_d is an integer. As 2 and B_d are invertible modulo odd N,

    S^d r=r mod N   iff   r is in (N/N_d) Z^2 mod N.   (2)

In particular, S^K=I mod N. Every nonzero label has a least period d
dividing K. This avoids assumptions about primality or squarefreeness of N.

## 2. A sparse-orbit lower bound

Suppose a nonzero label has the representation

    r=sum_(a=1)^q S^(j_a) v_a mod N,
    j_a in Z/KZ,   v_a in Z^2,   L=sum_a ||v_a||_1.

Repeated j_a and cancellations are allowed. Then its least period d obeys

    d >= K/q - 2 log_lambda(6 beta L).                 (3)

Proof: among the q cyclic gaps there is one of length at least K/q.
Rotate the labels so that their integer exponents lie in an interval of
length D<=K(1-1/q), and rotate again to its nearest integer centre.
The resulting integer representative r' satisfies

    ||r'||_1 <= 2 beta L lambda^[K(1-1/q)/2],           (4)

using ||S^j||_(1->1)<=2 lambda^|j| for signed j. Since (2) is unchanged
by multiplication by S or S^-1, r' is coordinatewise divisible by N/N_d.
It is a nonzero integer vector: if it were zero, the original label
would be zero. Therefore

    ||r'||_1 >= N/N_d > (1/3) lambda^[(K-d)/2],        (5)

where lambda^(k/2)/3<N_k<lambda^(k/2) for positive odd k.
Combining (4)-(5) proves (3). QED.

Let p be the smallest prime divisor of K. A proper period is at most K/p.
Consequently, if q<p and

    6 beta L < lambda^[K(1/q-1/p)/2],                 (6)

then every nonzero such label has the full period K.
For q=1 the conclusion holds directly when K is prime as well.

The q<p threshold cannot be dropped uniformly. For composite K let
ell=K/p and take the p-term label

    r=sum_(j=0)^(p-1) S^(j ell) e_1.                 (7)

It is nonzero modulo N and has exactly period ell. To see this, factor

    sum_j S^(j ell)=(N_K/N_ell) B_K B_ell^-1.

The last matrix C=B_K B_ell^-1 is integral, unimodular and commutes with S.
Thus the period of (7) modulo N equals the period of e_1 modulo N_ell.
If a proper divisor d of ell fixed e_1, (2) would force N_ell/N_d to
divide 1, which is impossible. Since ell>=3, N_ell>1 and the label is
nonzero. This proves the asserted exact period.

The threshold concerns short label orbits, not a zero trace resonance
classification and not an obstruction to every possible higher-order
normal form.

## 3. Application to the full symbol: composite K are admissible

Assume every nonconstant frequency of the fixed finite symbol satisfies
||v||_1<=R. Every label in [G,Abar] has the form v+S^d w, with L<=2R.
Because K is odd, p>=3, so it is sufficient that

    12 beta R < lambda^(K/12).                       (8)

This also ensures that each original nonzero label has period K.
Whenever a commutator label is zero, its commutator coefficient is zero.
For all other labels, full-period Weyl orthogonality holds. Thus every
step of `finite_symbol_normal_form.md` remains valid for these composite
K, with the same constants and with no primality condition.

For the frozen symbol R=9, (8) holds for every odd K>=39. An entirely
rational sufficient certificate is

    N_39=423859315570607 > 270^6=387420489000000,
    beta<5/2,   lambda^K>N_K^2.

It gives lambda^(39/12)>270>12 beta R. Monotonicity handles larger K.
The constants are conservative; (8) is sufficient, not necessary.

## 4. A sharper finite certificate without trigonometric rounding

For a particular admissible K, let c_d=(K-1-2d)/(2K), and let u_v be
rational upper bounds on |a_v|. Define the centred integer residue
distance dist_N(t)=min(t mod N, -t mod N) and

    g_(v,w,d)=min(2, (44/7) dist_N(det(v,S^d w))/N),
    C0=sum_(v,w,d) u_v u_w g_(v,w,d),
    C1=sum_(v,w,d) u_v u_w |c_d| g_(v,w,d).

Since pi<22/7, g bounds the exact commutator modulus. The same proof as
in the normal-form note now gives

    ||[G,A0]||op <= C1,
    ||[A0,Abar]||op <= C0/K,
    ||[G,Abar]||_2 <= C0 ||c||_(ell2)/K,
    ||c||_(ell2)^2=(K^2-1)/(12K).

Two unitary Duhamel comparisons and K-step telescoping therefore prove

    ||exp(-i epsilon K f0) U^K-I||_2
      <= |epsilon| K ||Abar-f0 I||_2
         + (epsilon^2/2) [K C1+C0(1+||c||_(ell2))].    (9)

Here ||Abar-f0 I||_2^2 is computable exactly from the collected modular
Weyl coefficients. No claim of simple spectrum is needed. Rational upper
square roots turn (9) into a finite certificate at arbitrarily large N
without constructing an N-by-N quantum matrix.

If the resulting upper bound is b and 0<b<t<2, at least
(1-b^2/t^2)N eigenvalues lie in K arcs of angular radius
2 arcsin(t/2)/K. Binning at angular length 2 pi/N yields

    B_N >= (1-b^2/t^2)^2 /
             [K/N + 2 arcsin(t/2)/pi] - 1.           (10)

The arcs may overlap; assign each selected eigenvalue to one bin. The
number of bins does not increase. Subtracting all N equal-label pairs
only weakens the lower bound. For rational certification use
arcsin(x)<=x/sqrt(1-x^2), pi>157/50, and a rational lower square root.

## 5. Adversarial checks and exact scope

`sparse_orbit_checks.py` tests 348 divisor identities, 1,009,120 nonzero
two-frequency labels with all relative shifts in its stated finite set,
40,000 further radius-nine label pairs, and the exact p-term short-orbit
examples. These are independent integer checks, not substitutes for the
all-K proof. The p-term examples specifically falsify a tempting extension
that would declare every bounded-length word to have full period.

The extension controls quadratic commutators and makes the arithmetic
coverage broader. In (9), epsilon=tau N still diverges for fixed tau>0.
Neither (3) nor removal of the prime restriction makes this error small
as N tends to infinity. A nonperturbative estimate for the coherent
fixed-map evolution remains missing.
