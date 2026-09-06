# M1 cycle 003 — exact q≠0 centering, k=2 residual, and corrected N=3571 stress case

Status: **CENTERING IDENTITY CLOSED; SINGULAR-SINGULAR TERM REMOVED EXACTLY; ASSEMBLED REGULAR-REGULAR VARIANCE STILL OPEN**.

This cycle resolves the ambiguity left by cycle 001: the spectral calibration is over nonzero additive frequencies `q in F_N^*`, so the raw energy `sum_t B(t)^2` is not itself the fluctuation variance. The correct centering can be written exactly and checked against the historical `N=53,199` numbers.

Executable paths:

- small/medium exact assembly: `code/research/m1/cross_twist_energy.py` and `.cpp`;
- memory-aware large stress: `code/research/m1/large_stress.py` and `.cpp`;
- dual large runner: `code/research/m1/run_large_stress.py`;
- corrected result: `results/research/m1/large_stress_N3571.json`.

## 1. Exact centering over q != 0

Let

`Sigma(q) = sum_{t in F_N} B(t) e_N(qt)`, `q in F_N^*`.

Write

`S = sum_t B(t)`, `E = sum_t B(t)^2`, `B0=B(0)`, `M=N-1`.

Using

`sum_{q != 0} e_N(qr) = N-1` if `r=0`, and `-1` otherwise,

the exact mean is

`mu = (N B0 - S)/(N-1)`.

The exact second moment is

`(N E - S^2)/(N-1)`.

After subtraction of the mean, the variance simplifies to

`Var_{q!=0}(Sigma) = N/(N-1) [ sum_{t!=0} B(t)^2 - (sum_{t!=0} B(t))^2/(N-1) ]`.

Equivalently, if `C` subtracts the mean over the `N-1` nonzero `t` values,

`Var_{q!=0}(Sigma) = N/(N-1) || C(B|_{t!=0}) ||_2^2`.

For exact integer regression it is useful to keep the rational numerator

`N[(N-1)(E-B0^2) - (S-B0)^2]`

over denominator `(N-1)^2`.

At `N=53`, `S=423879`, `B0=12063`, `E=3410502105`, this gives

`mu=4143.461538...`, `std=1913.789539...`,

exactly reproducing the historical `4143.46` / `1914` calibration. At `N=199` it gives `mu=73483.525252...`, `std=8317.335744...`, again reproducing the historical calibration.

Thus the old numerical standard deviations were centered quantities even though some manuscript prose described the raw Parseval energy `E` as if it were itself the fluctuation object.

## 2. What centering removes — and what it does not

Cycle 001 gave the exact weighted decomposition

`B = c^2 delta_0 + 2 c R_00 + D`, `c=N-2`,

where `R_00` is the regular `(H,H)` difference histogram and

`D = sum_gamma R_gamma * R_{-gamma}`

is the regular-regular contribution.

Taking the additive Fourier transform gives

`Sigma(q) = c^2 + 2 c S_off(q) + Y(q)`,

where

`S_off(q) = sum_{d!=0} R_00(d)e_N(qd)`

is precisely the exact `k=2` off-diagonal fluctuation already isolated elsewhere in the programme, and `Y(q)=Dhat(q)`.

Therefore centering over `q!=0` removes the huge `c^2` term **exactly**. It does not remove the scaled `k=2` fluctuation. The centered observable is

`Sigma(q)-mu = 2c [S_off(q)-mean(S_off)] + [Y(q)-mean(Y)]`.

The old raw lower bound `E >= (N-2)^4` is therefore not an obstruction to the centered spectral variance. It was an obstruction only to treating the raw `E` itself as the fluctuation energy.

## 3. The residual singular piece is analytically controllable

Let

`P = sum_d R_00(d) = (K-1)(K-2)`.

For fixed regular `d` and fixed `u in H`, the Möbius fiber determines at most one `v`. Hence

`R_00(d) <= K`.

Therefore

`sum_d R_00(d)^2 <= K P < K^3`.

The exact nonzero-q variance formula then gives

`Var(S_off) <= N/(N-1) K^3`.

Consequently the scaled residual

`X(q)=2(N-2)S_off(q)`

satisfies the elementary bound

`Var(X) <= 4(N-2)^2 N/(N-1) K^3`.

So the singular part no longer needs a new deep theorem. If `Var(Y)` is controlled, the remaining covariance obeys Cauchy--Schwarz:

`|2 Cov(X,Y)| <= 2 sqrt(Var(X) Var(Y))`.

This reduces the load-bearing analytic problem to controlling the regular-regular fluctuation `Y` strongly enough in the true arithmetic regime.

## 4. Exact symmetry of the regular coset histograms

Let `gamma=(c_u,c_v)` be a quotient-coset pair. Inverting both multiplicative coordinates sends

`(u,v) -> (u^{-1},v^{-1})`,

which sends `gamma -> -gamma` and, from the exact difference formula,

`d(u^{-1},v^{-1}) = -d(u,v)`.

Hence

`R_{-gamma}(d)=R_gamma(-d)`.

For the additive Fourier transform this gives

`Rhat_{-gamma}(q)=conj(Rhat_gamma(q))`.

Therefore the regular-regular spectral term has the positive exact representation

`Y(q)=Dhat(q)=sum_gamma |Rhat_gamma(q)|^2`.

This identity is both conceptually cleaner than the historical twist-diagonal shortcut and computationally useful: it lets the large stress test avoid the `H^2 x N^2` partner-grid gather and avoids constructing the dense twist tensor.

The primary analytic target after this cycle is therefore

`Var_{q!=0}( sum_gamma |Rhat_gamma(q)|^2 )`.

## 5. Component sizes at exact anchors

After centering in the dual `t!=0` representation, write

`C(B)=C(X)+C(D)`.

The centered energy splits into `||C(X)||^2`, `||C(D)||^2`, and `2<C(X),C(D)>`.

At `N=53,K=13`, their fractions of the centered `t`-energy are approximately

- scaled `k=2`: `36.17%`;
- regular-regular: `20.84%`;
- covariance: `42.99%`.

At `N=199,K=11` they are approximately `29.11%`, `27.05%`, `43.83%`.

At `N=461,K=23` they are approximately `36.23%`, `23.93%`, `39.84%`.

At corrected `N=3571,K=17` they are approximately `34.92%`, `23.87%`, `41.21%`.

The covariance is therefore not a small finite-N nuisance. The correct strategy is to control `Y` and then use the exact `X` structure plus covariance inequalities, rather than to assert orthogonality.

## 6. Historical N=3571 driver is invalid

The restored `code/large_m/third_calibration.py` is not an authoritative large-N implementation.

It contains two independent assembly bugs:

1. `Dgrid[U2-1, V2-1]` uses two one-dimensional NumPy advanced indices. NumPy therefore selects **paired** entries. The required partner of a grid cell `(u_i,v_j)` is the outer grid `(U2_i,V2_j)`. The historical code consequently does not implement its own stated permutation map.
2. The diagonal/regular class is added only once. For ordered key pairs the exact decomposition contains `2(N-2)R_00`, i.e. both diagonal--regular and regular--diagonal orientations.

Applying the same historical algorithm to the already exact `N=53` and `N=199` anchors fails to reproduce their known integer `V4`, `B(0)`, and energy. The old `N=3571` calibration produced by that driver is therefore quarantined.

The original historical source remains preserved in `archive/legacy-workspace/`; the active research path uses the corrected implementation below.

## 7. Corrected memory-aware N=3571 result

The new algorithm builds only the regular quotient-coset histograms `R_gamma(d)` and then uses

`Dhat(q)=sum_gamma |Rhat_gamma(q)|^2`.

The inverse FFT is checked against the integer lattice before rounding. On `N=53,199,461` the resulting `B(t)` agrees **exactly** with the dense cycle-001 integer construction. Python and an independent C++17/FFTW implementation then agree on the full `N=3571,K=17,m=210` vector checksum and every integer summary.

Corrected `N=3571` values:

- trace-3 eigenvalue used for labeling: `a=1105` (the inverse root is equivalent for the subgroup);
- regular key mass: `12,734,192`;
- `R_00` mass: `240=(17-1)(17-2)`;
- `R_00` L2 count: `464`;
- maximum regular histogram cell: `4`;
- `V4 = 3,691,721,361`;
- `B(0) = 26,385,585`;
- `sum_t B(t)^2 = 4,459,481,908,480,417`;
- exact variance numerator: `833,080,273,095,375,744` over denominator `12,744,900`;
- `mean Sigma_4(q!=0) = 25,358,880.300840337`;
- `std Sigma_4(q!=0) = 255,667.31424374814`;
- relative standard deviation: `0.01008196384109577`;
- full `B` FNV-1a-64 regression checksum: `c95d6971a1ee53a5`.

Python inverse-FFT integer-rounding error is below `1.9e-9`; C++/FFTW is below `1.3e-9`. Both implementations agree exactly on `V4`, `B(0)`, integer L2 energy, the exact mean/variance rational numerators and denominators, and the full-vector checksum.

These numbers supersede the historical `N=3571` M1 calibration produced by the buggy driver.

## 8. New primary target

After cycles 001--003 and the cycle-002 Weil lemma, M1 no longer needs to solve an undifferentiated “coupled energy” problem.

The remaining analytic core is:

1. prove a strong enough bound for
   `Var_{q!=0}(Y(q))`, `Y(q)=sum_gamma |Rhat_gamma(q)|^2`;
2. combine it with the explicit `O(N^2 K^3)` bound for the scaled `k=2` piece and Cauchy--Schwarz for covariance;
3. compare the resulting standard deviation with the exact mean in the true trace-3 arithmetic regime `K=K(N)`;
4. only then reconnect the controlled fourth-moment fluctuation to the spectral-law argument through a valid noncommutative reduction.

Promotion rule: the centering question is closed by this cycle, but M1 remains `OPEN GAP` until the regular-regular variance and downstream spectral implication are proved.
