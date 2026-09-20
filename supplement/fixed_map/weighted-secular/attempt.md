# Weighted determinant continuation

Checkpoint: `weighted-secular-20260920-covariance-control-and-ratio-target`.
Parent: `secular-route-20260920-direct-fixed-coupling-attempt`.
Base revision: `e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`.

**The principal fixed-coupling estimate is still open.** This continuation
does not claim a breakthrough, a new positive BGS case, or new asymptotic
control of the original map. All new files are uncommitted research material.

## Actual weighted sums, rather than isolated characters

Use the original centered raw A_N and cat M_N. In the A_N eigenbasis put
B=Q*M_N Q, a_I=sum_(j in I) a_j, b_I=det B_(I,I). At k=floor(N/2),
`weighted_probe.py` enumerates every principal minor for N=15,19,23.
The largest run contains 1,352,078 minors, not a sample of subsets.

For a frequency window Delta, the implemented observables are

    S_Delta(epsilon)=sum_(I!=J, |a_I-a_J|<=Delta)
                       b_I conjugate(b_J) exp(i epsilon(a_I-a_J)),
    A_Delta=sum_(I!=J, |a_I-a_J|<=Delta) |b_I b_J|,
    D=sum_I |b_I|^2.

All ordered pairs are counted; the sorted implementation sums one half
and takes twice the real part. Prefix sums avoid explicit quadratic-size
arrays, without dropping pairs. Their sums use extended-precision
accumulation; the matrix and minor computations use double precision.
`center_checks.py` checks the prefix algorithm against explicit pairs,
including coincident frequencies, zero weights and complex phases.

At epsilon=0, Delta=1/N:

| N | S_Delta | A_Delta | D | Independent-phase standard deviation |
|---:|---:|---:|---:|---:|
| 15 | 6.162938 | 242.9457 | 1.525515 | 0.279087 |
| 19 | 9.214132 | 2417.979 | 1.865924 | 0.261445 |
| 23 | 7.038912 | 26228.69 | 1.911883 | 0.233110 |

The last column is not a fitted error bar or a hypothesis test. If the
minor phases are artificially replaced by independent uniform angles,
the mean of S is zero and its variance is exactly
2 sum_(i>j, close) |b_i b_j|^2. This follows by expanding S^2: only
oppositely oriented edges survive phase integration. Four seeded phase
controls are also saved, but no randomness is attributed to actual minors.

`center_checks.py` changes the actual common exponent to epsilon=t N,
t=0,0.1,1,10,100. These are auxiliary parameters. For N=23 and Delta=1/N,
the S values are respectively 7.0389,6.8460,4.4503,-0.8333,-0.6149.
For Delta=1/N^2 they are 0.56771,0.56732,0.56369,0.52275,0.13058.
The parameter changes the weights coherently, and cannot be represented
as fresh independent phases. These finite observations establish no rate
or asymptotic obstruction at fixed tau=10^-80.

There is also cancellation BETWEEN frequency windows. At N=23, t=1,
the complete squared middle coefficient is approximately 1.904708,
the diagonal contribution is 1.911883, and the Delta=1/N off-diagonal
piece is +4.450293. The complementary off-diagonal piece is therefore
approximately -4.457468. Dropping the complement as already dephased
would discard a substantial cancellation in this finite example.

In particular, tiny tau is not a uniform license to replace epsilon=tau N
by zero. The valid elementary bound is

    |S_Delta(epsilon)-S_Delta(0)|
          <= min(2, |epsilon| Delta) A_Delta.

For Delta=1/N its prefactor is tau, but no uniform bound on A_Delta has
been proved; Cauchy--Schwarz alone permits
A_Delta<=binomial(N,k) D. The small-dimensional data must not be extended
to the asymptotic fixed-coupling problem using this inequality.

## Independent representation check

`jacobi_audit.py` does not use the Fourier coefficient builder to assemble
the generator. It uses the trigonometric diagonal and the raw midpoint
off-diagonal r((x+inverse(2))/N) exp(-i alpha)/200. When N is odd and
coprime to 7, this off-diagonal has exactly one zero. Cut there, reorder,
and apply the constant phase gauge to obtain a real Jacobi matrix with
strictly positive internal off-diagonals. A tridiagonal eigensolver gives
an independent eigenbasis and hence independent principal-minor sums.
This structure concerns A_N; it asserts no simple-spectrum theorem for U_N.

Across the executed N and t=0,1,100, the two implementations agree in
all near-pair counts and to less than 3.3e-12 in the signed sums.
Direct characteristic-polynomial reconstruction at all parameter centres
has residual below 1.2e-11. These are floating cross-checks, not interval
certificates or an exact large-N proof.

## An insufficient endpoint and a correct stronger one

`determinant_boundary.md` proves an elementary method control: the
(N+1)-clock with one point deleted has exactly the CUE determinant
covariance after uniform common rotation, at every finite N and all
polynomial arguments. Its local spectrum is nevertheless regular and
its weighted pair comparison fails. This removes the possibility of
closing BGS solely with second moments of secular coefficients. It is
not a counterexample in the prescribed quantization class.

The same note reconstructs the exact determinant-ratio formula and CUE
reference. The required Abel energy is

    L_N(s)=N^(-2) sum_(m>=1) exp(-2 s m/N) |Tr U_N^m|^2,
    L_CUE(s)=(1-exp(-2s))/(4s^2).

Convergence on the countable set s=s0+n/2 would suffice for every compact
weighted pair test, by positivity and the compact moment problem. The
converse uses a Fejer-kernel translate bound to control Laplace tails;
it is not inferred from vague convergence without a tail argument.
This is a reformulation, not a proved estimate of L_N for the frozen map.

## Additional source-to-target attempt

[Bouclet--De Bievre, Theorem 3.1, equation (3.5)](https://arxiv.org/html/math-ph/0409069v1)
gives analytic Egorov control for
t<=(2-nu)|log(hbar)|/(3 Gamma_epsilon), where
Gamma_epsilon>=Gamma_A=log(lambda). Even granting the convention
identification, this does not reach our odd Pell return K, for which
K=2 log(N)/log(lambda)+O(1), and is far short of t proportional to N.
Its observable propagation and scarring conclusions do not themselves
estimate coherent trace pairs. The exact range was read from the theorem;
the word "long" in its title is not used as a Heisenberg-time assertion.

The previous Faure--Tsujii prequantum comparison gap remains as documented
in `../secular-route/attempt.md`. Even a valid long-time orbit formula
would still require cancellation of the actual weighted orbit sums.
The inspected principal-minor cavity paper concerns positive symmetric
matrices and Bethe approximations, not these complex unitary weights;
it supplies no usable positive-weight estimate here.

## Checks and remaining obligation

Run from the repository root, with OPENBLAS_NUM_THREADS=1:

    python build/weighted-secular/weighted_probe.py
    python build/weighted-secular/center_checks.py
    python build/weighted-secular/jacobi_audit.py
    python build/weighted-secular/determinant_control.py

The last program verifies the deleted-clock polynomial, Newton identities
and Abel generating function with integers/rationals; verifies the ratio
derivative using independent resolvent quadrature and geometric summation;
and checks the known finite CUE ratio formula directly against its
eigenangle density in dimensions 1,2,3. Its floating errors are below
2.2e-15. These checks validate formulas, not an asymptotic theorem.

**Still missing:** any uniform proof of L_N(s)->L_CUE(s), or the stronger
local determinant-ratio convergence, for the one prescribed fixed map.
The generic unitarity bound is only L_N(s)<=1/(exp(2s/N)-1)=O(N),
attained by a scalar unitary; analyticity of the ratios does not improve
it. No additional independent agent or Lean certification was obtained.
There is no justified publication to main under the user's current rule.
