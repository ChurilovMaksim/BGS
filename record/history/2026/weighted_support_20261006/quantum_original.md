# The exact box factor under one homoclinic insertion

6 October 2026. Author candidate; independent audit required. This separates
three obligations: imaginary first loop, uniform localized first-loop change,
and the independently sourced bound on total leading periodic mass. Only the
third is still an external/classical transfer dependency here. No replacement
of the whole signed displacement sum is made.

## 1. Exact conventions and the retained object

Use h=(2*pi*N)^-1. The one-step finite-J amplitude is
sum_(ell=0)^J N^-ell a_ell =sum_(ell=0)^J (2*pi*h)^ell a_ell.
For each actual real stationary class let K=-Phi'', G=K^-1, and let Z_z be
the EXACT conditioned rotated-box expectation in the accepted local theorem,
as extended to the retained radius-one contour box in the accepted global
proof Section6. Its full-Gaussian normalization additionally contains
P_z=P_(G)(B_h), with P_z=1+O(m exp(-c/h)).

The exact box coefficient is

 alpha_box(z)=e(NDelta_m(z)) w_0(z) P_z Z_z,                         (Q1)

where w_0 is the actual leading transport/Hill weight in W3. For every fixed
J and mh<=b, the accepted theorem gives

 Z_z=exp(h ell_1(z))[1+epsilon_z],  |epsilon_z|<=C_(J,b)sqrt(h),      (Q2)

uniformly in the stationary class. No trace sum has yet been taken.

## 2. First loop is purely imaginary in the actual Weyl convention

For a real test amplitude, the coefficient P_n in the one-step expansion of
the Hermitian Weyl operator is i^-n times a real differential operator.
This follows term by term: replace each symbol moment in k,l by the matching
real derivative of g divided by the corresponding power of 2*pi*i. A phase
Taylor factor contributes i, but also one additional symbol-moment order;
the net power for total h-grade n is i^-n. The midpoint kl term obeys the
same count. Thus D_n=iP_n is i^(1-n) times a real operator.

The transport recursion and real initial a_0=1, a_ell=0 for ell>=1 imply
that a_0 is real positive and a_1 is purely imaginary. Only these two symbol
orders enter ell_1; if J=0, the missing a_1 term is simply zero.

Write c=exp(-i*pi/4). In rotated variables the exact exponent begins

 R_h=c sqrt(h) W+h Q+O(h^(3/2) local polynomials),                   (Q3)

where W is real odd, with local linear and cubic terms. Every term of Q is
purely imaginary: the quadratic leading-log-amplitude factor has c²=-i,
the quartic phase factor is i*c^4=-i, and the subleading constant amplitude
is 2*pi*a_1/a_0, also imaginary. Consequently

 ell_1=E_G Q +(c²/2)E_G W² is purely imaginary.                    (Q4)

The expectations defining this formal first coefficient are full real
Gaussian Wick expectations. The accepted conditioned-box theorem already
accounts for its exponentially small boundary discrepancy. Q4 preserves the
2*pi conversion from N^-1 to h and does not alter the frozen quantizer.

## 3. Uniform change under a literal unit winding

Keep a lifted branch r fixed and interpolate its winding by nu+s e_i,
0<=s<=1. The actual stationary point obeys

 x'(s)=G(s)e_i,
 sum_j |x'_j(s)|<=C,
 |x'_j(s)|<=C 2^(-dist_m(i,j)).                                    (Q5)

The accepted massive inverse estimates hold for all these real stationary
points, including m=1,2 with combined edge entries. Phase derivatives of
order at least two and all amplitude derivatives are unchanged by integer
branch gluing. The endpoint ell_1 is thus exactly the coefficient for the
physical translated label z+d_m (or its cyclically shifted pulse).

Every coefficient of a local W_j or Q_j is a smooth function of the two edge
coordinates, with a fixed uniform derivative bound from actual analyticity.
Q5 gives

 sum_j |(local coefficient at j)'|<=C,
 sum_(a,b)|K'_(a,b)|<=C.                                            (Q6)

Since G'=-G K' G and G has uniformly bounded row AND column absolute sums,

 sum_(a,b)|G'_(a,b)|<=C.                                            (Q7)

Differentiate the FINITE Wick formula in Q4. One-vertex Q terms have degrees
0,2,4; coefficient derivatives sum by Q6 and covariance derivatives by Q7.
For W_j W_k, both vertex degrees are odd (one or three), so every pairing
contains at least one cross covariance joining j and k. When a coefficient
is differentiated, this cross covariance sums the other site by the row-sum
bound. When a cross covariance is differentiated, use the entrywise l1
bound Q7. When a self covariance is differentiated, the remaining cross
covariance sums the other site and Q7 sums the differentiated local entry.
There are at most 15 pairings for the largest degree-six term. All undifferentiated
covariances and local coefficients are uniformly bounded. Hence

 |d ell_1/ds|<=C,  |ell_1(z+d_m)-ell_1(z)|<=C,                        (Q8)

with no m factor. A chain of r literal unit-winding insertions costs at most
Cr, without claiming that all physical displacements have a short such chain.

This is an actual local-contraction argument. It does not differentiate the
Holder label map or invoke ordinary long-time stationary phase.

## 4. Exact box insertion becomes harmless in a weighted average

By Q4, conjugate(ell_1(z))=-ell_1(z). Thus Q2 and Q8 give

 P_(z+d)P_z Z_(z+d)conjugate(Z_z)=1+O_(J,b)(sqrt(h)),                 (Q9)

uniformly for the unit pulse d=d_m. The O(h) first-loop phase difference is
absorbed by O(sqrt(h)); the Gaussian probabilities add only an exponential
error. Also |Z_z|>=1/2 for sufficiently small h uniformly, so no unverified
zero-free denominator is needed. For r successive pulses the same argument
gives O(sqrt(h)+rh) whenever rh is bounded, with an appropriate fixed constant.

Let rho_m(z)=w_0(z)^2/D_m and Z_m^cl=sum_z rho_m(z), as in W9. The difference
between the exact-box unit-pulse paired coefficient and its leading-weight
counterpart is bounded by

 C sqrt(h) sum_z sqrt(rho_m(z+d)rho_m(z))
                         <= C sqrt(h) Z_m^cl.                       (Q10)

The inequality is Cauchy–Schwarz and translation is a permutation of G_m.
This is precisely why no exponentially many-box loss occurs in this ONE
normalized autocorrelation. The third obligation is now isolated:

 sup_m Z_m^cl<infinity.                                              (Q11)

It is a positive classical periodic-mass bound, currently being independently
checked through the exact weighted-periodic transfer theorem. Once Q11 is
proved, Q10 is O(N^-1/2), uniformly at m~N in a fixed band.

Together with the physical-area integral W13 and a norm-uniform periodic
transfer EQ, this would give O(N^-1/2) for the actual full-box unit-pulse
coefficient, not merely its unweighted phase. The complete global Fresnel
coefficient can also be compared in the conservative m<=2N band using the
SUMMED ABSOLUTE contour tails: after the paired-identity normalization their
l1 norm divided by sqrt(D_m) is exponentially small, hence their normalized
l2 norm is exponentially small. Q10/Q11 bound the main normalized l2 norm.
This is again a one-coefficient comparison, not a sum over all displacements.

## 5. Unclosed global obligations

The original trace hierarchy has an unnormalized outer displacement SUM.
Neither Q9 nor an O(N^-1/2) bound for one selected coefficient permits summing
it over exponentially many d. Resonant N-torsion sectors and complicated
multi-pulse classes retain their own exact weights and phases. The WKB-to-U
fixed-J trace-table reduction remains the separate accepted comparison; no
intrinsic decomposition of U's spectrum into these orbit labels is asserted.
