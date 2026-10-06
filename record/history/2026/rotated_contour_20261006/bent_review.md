# Fresh independent audit of the global bent contour and conditional tail

Date: 6 October 2026. No canonical or author-candidate edits. This is a separate audit, not an extension of the earlier reciprocity verdict by implication.

## Normalized claims and verdict

**Primary verdict: proved as written**, for the global contour representation/tail bounds (C1)–(C3) and the per-integral conditional large-field bound (D1), at the actual fixed coupling and each fixed finite WKB order, with sufficiently large `N` and the stated bandwidth restrictions. The finite initial `N` range in C2 can be absorbed in its constant. The explicit radius-`sqrt(2)` application of the corrected local theorem is also justified by the additional quantitative estimates reconstructed below.

The verdict does not establish a uniform optimal first-loop remainder, absolute summability of algebraic local errors, a signed CUE comparison, or BGS universality.

### Frozen sources

- `global_bent_contour.md`: SHA-256 `d4abd7785da50537bc4cfd218bb753dd10426d07175a7d954ebddb67b8f38aec`.
- `conditional_bent_tail.md`: SHA-256 `762aeac6e6840cf8798ab810ff77f2be3b2a327f42e47c5d53625b1d8a2d2ce1`.

Copies retained in `bent_frozen/`. The author was contacted before any potential repair; this review makes no edits to the candidates.

Relevant accepted local dependency: `rotated_local_first_loop_v2.md`, SHA-256 `fe41ac7dc34660f2adedb82f741903be482e2b8eaef35d84feba6341bfcc32f1`. Its exact object and hypotheses were reread, together with `local_review/review.md`, `local_review/v2_hash_confirmation.md` and the retained convex-box Poincare source check. Its original small-radius acceptance alone is NOT used as permission to enlarge the box. The enlargement is verified independently below.

Actual-model inputs remain the canonical raw/midpoint four-branch construction inspected at `300d99270d11c87d0aa84e9d8f624491788629ba`; hashes and conventions are recorded in `review.md` in this directory. The global reciprocity source is the separately audited frozen `6cbbc685...` revision.

## Exact usable bandwidths

Use two different symbols for bandwidth to avoid mixing `m/N` with `mh`.

1. **Frozen C2 statement:** for `m<=beta N`, its stated exponentially decaying total trace error holds for

   `0<beta<8*pi/(5*log(7)) = 2.5831348113...`.

   At `beta=2`, the published safe estimate is `C_J sqrt(N) exp(-4N/5)`.

2. **Direct sharper reading of the same C10 calculation:** retaining `3sqrt(5)` instead of rounding to 7 gives

   `0<beta<8*pi/(5*log(3sqrt(5))) = 2.6409214157...`.

   This is a consequence of the reviewed proof, not the literal C2 rate.

3. **Frozen D1 statement:** the dimension-normalized per-class bound holds for every fixed finite `b_h` with `mh<=b_h`, where `h=(2*pi*N)^-1`. It has no finite upper bandwidth threshold at the per-class level. Thus for `m<=beta N`, set `b_h=beta/(2*pi)`.

4. **Additional independently derived summed consequence of D1:** put `eta=10^-4`, `gamma=10^-7`, and

   `kappa = log(1+sqrt(2)) + gamma - (1/2)log(1-4eta)`.

   Then the total trace tail is bounded by

   `C_(J,beta) sqrt(N) exp[-(4*pi/5-beta*kappa)N]`

   for each fixed `0<beta<(4*pi/5)/kappa = 2.8508949913...`.

   This keeps the exact cyclic Gaussian determinant rather than replacing it by a diagonal product. It is an extra consequence derived in this review, not a claim already written in the frozen conditional note. At `beta=2` its rate is about `0.7501266688`, so it is weaker there than C2's published `0.8` rate, despite the larger admissible bandwidth. All endpoints are strict; no vanishing error at the critical endpoint is certified.

## Dependency graph and obligation matrix

Literal symbol bounds → complex characteristic inverse on an enlarged endpoint strip → bounded holomorphic phase correction and finite-order amplitudes → saturated-contour damping → finite-Abel Cauchy deformation → explicit absolute tail bound with every branch/winding count.

For D1: the same strip inputs → partition by actual large coordinates → absorb cross terms using the still-present core box → retain principal Gaussian and exact local real tilt → uniform conditioned coordinate moments and Poincare → `exp(Cmh)` core bound → Schur determinant ratio costing only the large-set size → binomial sum.

| Obligation | Status |
|---|---|
| Literal `tau=10^-80` complex-flow and graph certificate | Passed |
| Closed width-2 endpoint strip with room for higher transports | Passed, explicit margin reconstructed below |
| `m=1,2` cyclic multiplicities | Passed |
| Full saturated contour and Abel limit | Passed for each finite `m,N`; no simultaneous-limit assumption |
| C1 prefactor, Jacobian and all branch/winding counts | Passed |
| C2/C3 for `m<=2N` | Passed |
| Principal-core Gaussian retained on its box | Passed |
| D6 exact tilted-box hypotheses at radius `sqrt(2)` | Passed by explicit reconstruction below |
| Elimination of artificial `C^m` in D1 | Passed; only incident edges and Schur ratios pay `C^|S|` |
| Unrestricted-core Gaussian-completion shortcut | Failed; not used by the reviewed proof |
| Signed ensemble evaluation / optimal local remainder | Not addressed and remains open |

## 1. Literal complex-strip certificate

On the symbol strip `|Im q|,|Im p|<=9/4`, each Fourier mode has modulus at most `exp(45*pi)`, because `|k|+|l|<=10`. Coordinate derivatives cost at most 63 each. The given coefficient mass is at most 52. The bounds `|g|<10^66`, `|partial²g|<10^70`, and `|partial³g|<10^72` follow from the stated rational exponential majorants. A first derivative is bounded, for example, by `63*10^66`.

For the characteristic field `(-g_p,g_q)/(2*pi)`, conversion of coordinate derivative bounds to induced max-norm bounds costs at most 2 for first derivatives and 4 for second derivatives. These costs remain below `B=10^73`. Therefore `B*tau=10^-7`; the complex flow displacement, first-derivative defect and second-derivative bounds claimed in C4 follow from the integral and variational equations with ample slack.

The initial endpoint map `(a,y) -> (a,(y+r-3a)/4)` has induced max norm 1. If endpoint imaginary parts are at most 2 and `a` lies within `4*10^-7` of `x`, the initial position/momentum remain within `2+4*10^-7` of the real planes, and the flow displacement adds at most `2*10^-7`. This stays far inside width `9/4`. The fixed-point map `a=x-(X_t(a,p_0)-a)` maps that closed neighborhood into itself and has contraction constant at most `2*10^-7`. Its holomorphic inverse and derivative bounds are uniform in all real translates and branch labels.

The resulting endpoint derivatives of `p` through order two are bounded by 100. Composing `g(x,p)` and differentiating twice costs at most a handful of terms of size `10^70*(1+100)^2`, plus a first-derivative term times 100; this is below `10^76`. Integrating to literal `tau` gives C5, an edge Hessian bound of `eta=10^-4`.

The same calculation gives `|delta S|<10^-14` and a first-derivative bound much smaller than `10^-4`, validating the extra d=0,1 bounds used in D2. These are bounds for the phase correction, not for the unbounded initial quadratic phase.

There is genuine room for the amplitude assertions on the *closed* width-2 strip: repeat the inverse construction for endpoint width `2+1/100`, still strictly inside the width-`9/4` symbol strip. Its constants have the same stated slack. A finite number of derivative losses in any fixed order of transport can then use nested strips between these widths while retaining a neighborhood of the closed width-2 strip. This supplies the margin only abbreviated in the candidate.

The leading transport coefficient has modulus below `10^73`; hence its integrated logarithm has modulus at most `gamma=10^-7`. Thus

`exp(-gamma)<=|a_0(z)|<=exp(gamma)`

on the needed strip, and `a_0` is positive at real endpoints. The finitely many higher amplitudes have finite uniform strip bounds by induction along the same analytic characteristics. For each fixed `J`, the finite amplitude converges uniformly to `a_0` as `N` grows, giving both C6 and the lower bound `1/2` used in D2. A holomorphic logarithm is available from the explicit leading exponential and the convergent logarithm of `1+(a_J-a_0)/a_0`; a modulus bound alone would not have established that logarithm.

## 2. Geometry and the global damping inequality

`K_0=B_m/4=I+(1/4)L_cycle`. The cycle has repeated edges at `m=2`, and zero Laplacian at `m=1`; therefore `K_0=[1]` at `m=1` and has off-diagonal `-1/2` at `m=2`. These are the correct matrices throughout this audit.

For `f_j=clip(u_j,-1,1)`, monotonicity gives

`u^T K_0 f = sum u_j f_j +(1/4)sum_edges (u_j-u_k)(f_j-f_k) >= sum min(u_j²,|u_j|)`.

The correction `q`, after subtracting the stationary constant and affine terms, has zero gradient at zero and a symmetric nonnegative matrix of entrywise Hessian suprema with row sums at most `4eta<epsilon=1/10`. For `a_j=|u_j|`, `b_j=min(a_j,1)`, symmetry and

`(a_i-a_j)(b_i-b_j)>=0`

give `sum E_ij b_i a_j <=epsilon sum a_j b_j`; similarly `sum E_ij b_i b_j<=epsilon sum a_j b_j`. Integrating the gradient first radially and then vertically proves the claimed `2epsilon` bound on the imaginary correction. The same proof applies on the homotopy `u-i s f(u)` with an extra factor `s`.

This proves C8 globally, not merely within a Taylor neighborhood. At `m=1` the edge Hessian becomes `delta S_xx+2delta S_xy+delta S_yy`, whose bound is `4eta`; at `m=2` the repeated neighbor terms combine with the same row bound. No small-dimensional exception changes the constants.

## 3. Cauchy deformation with the actual Abel regulator

The original Abel regulator is centered at the cat center. Translating to the actual stationary point makes it exactly

`exp[-pi*eta_reg*sum(z_j+d_j)^2]`,

where `d` is the real center displacement. Distinguish this damping parameter from the fixed Hessian constant `eta=10^-4`.

At positive `eta_reg`, every product contour used in the deformation has bounded imaginary parts. The unbounded quadratic phase has imaginary part at most linear in the real coordinates there; the nonlinear correction and amplitudes are bounded on the strip. The regulator's negative real quadratic term dominates this linear growth. Thus finite-box Cauchy deformation followed by the box-size limit is legitimate, including the side faces. The coordinatewise saturated contour is piecewise smooth; its corners have measure zero. There is no global rotation leaving the analytic strip.

On the final graph, C8 gives an integrable bound independent of `eta_reg` for `0<eta_reg<=1`, because the regulator modulus is at most `exp(pi*eta_reg*m)`. Dominated convergence removes the regulator. This establishes equality separately for each finite `m,N`; a dimension-uniform interchange of Abel limits is unnecessary. Uniform tail bounds are then obtained directly on the already identified final contour.

The Jacobian has modulus `sqrt(2)` on each core coordinate and 1 on each saturated coordinate, at most `2^(m/2)` overall. Inside the core it is precisely the oriented contour `x*+(1-i)u` in C1.

## 4. Global normalization and crude summed tail

Combining G6 and G7 gives exactly

`e(3mN/8) N^(m/2)/8^m`.

The two Maslov factors cancel. There are precisely `4^m D_m` listed terms, without a claim that these are distinct physical orbits. The determinant satisfies `D_m<=6^m`.

With `c=8*pi/5`, the scalar core-plus-tail integral is bounded by

`I_N<=sqrt(5/(8N))+(5/(4*pi*N))*exp(-cN)`,

and its saturated part is exactly `J_N=(5/(4*pi*N))*exp(-cN)`. The union bound over at least one large coordinate costs `m J_N I_N^(m-1)`. Amplitudes cost `2^m`, the crude Jacobian `2^(m/2)`, and the trace counts/prefactor give precisely C10, not a hidden extra determinant or branch factor.

Simplifying gives

`C (m/sqrt(N)) (3sqrt(5))^m exp(-cN)(1+O(N^-1/2 exp(-cN)))^m`.

For `m<=beta N` the final factor is bounded. Rounding `3sqrt(5)` upward to 7 proves C2 in its stated range. At `beta=2`, `pi>3` and `log7<2` give `c-2log7>4/5`. The fixed-`J` startup threshold is harmless: the remaining bounded set of pairs `(m,N)` can be absorbed in the constant.

The separate one-step norm error `O_J(N^-J-1/2)` produces a trace-power error `O_J(N*m*N^-J-1/2)=O_J(N^3/2-J)` for `m<=2N`; the near-unitary power-growth factor stays bounded. This proves the stated C3 reduction, without identifying `U` with its WKB surrogate exactly.

## 5. Semiclassical parameter and local radius

The finite WKB polynomial is in `N^-1`. The contour Gaussian parameter is instead

`h=(2*pi*N)^-1`, so `N^-ell=(2*pi*h)^ell`.

All finite amplitude coefficients in h notation must include this factor. The candidate's asymptotic constants are unaffected at fixed `J`, but this identification should be written explicitly wherever `a_(r,J)(h,...)` first appears.

The exact change of variables is `y=sqrt(2/h)u`, so

`z=(1-i)u=exp(-i*pi/4)sqrt(h)y`.

The radius is therefore `rho=sqrt(2)`, not 1. The quadratic weight is `exp(-u^T K u/h)` and its contour Jacobian changes `(pi h)^(m/2)` into `(2*pi*h)^(m/2)`. Since `2*pi*h=1/N`, this agrees with the original reciprocity normalization.

The accepted small-radius theorem cannot simply be quoted at this larger radius. Here is the additional verification. On the actual radius-one u box, the exact phase-remainder Hessian in y coordinates has entrywise row bound at most `8eta`: the edge Hessian difference between a complex point and the saddle is at most `2eta`, with four entries per row. Scalar tilt strengths up to 4 cost at most `32eta`. The exact log-amplitude Hessian costs only `C_J h` after scaling.

For the additional polynomial tilt family in the corrected local theorem, apply Cauchy to the edge Hessian on the bidisk of radius `R=7/4` about the real saddle, contained in the certified strip. On `|z_j|<=sqrt(2)`, its linear and quadratic Taylor pieces together are bounded per entry by

`eta*(2sqrt(2)/R + 6/R²) < 4eta`.

Thus the cubic and quartic phase truncations, pure cubic tilts and their interpolants still have row perturbations well below 0.1, even after the tilt factor 4. The leading log-amplitude quadratic truncation costs `O(h)`; its linear truncation has no Hessian. This verifies the entire finite tilt family, not just the exact exponent.

For sufficiently small h, one consequently has `1.3<=V_jj<=2` and `sum_(k!=j) sup|V_jk|<=.7` for `m>=2`, and curvature in `[.8,2]` for `m=1`. These are sums of entrywise suprema. Local Taylor remainders through the required degree follow by Cauchy on an interior strip around the rotated points, which have imaginary parts at most 1. There is no need to enlarge an unknown Taylor convergence radius. The normalization of the actual box remains `P_G(B_h) Z_(m,h)` after dividing by the full Gaussian factor, as the candidate states.

## 6. Large-set partition, cross terms, and why unrestricted completion fails

Partition by the actual set `S={j:|u_j|>1}`. For `T=S^c`, retain `|u_T|<=1` until after all cross terms have been bounded. With `s_j=sign(u_j)`, the imaginary quadratic phase is

`u_T^T K_TT u_T + u_T^T K_TS s_S + u_S^T K_ST u_T + u_S^T K_SS s_S`.

The diagonal entries minus all absolute off-diagonal entries are at least `1-4eta`; the off-diagonal row sums are at most `.5+2eta`. Bound the two cross terms using `|u_T|<=1`, and bound the internal S off-diagonal terms by the relevant row sums. The coefficient of each `|u_j|` is then its full row mass, while the sole additional constant is its S-to-T row sum. This is exactly D3. No completion of the square is performed.

For the nonlinear difference after setting `z_S=0`, only incident edges change. On each edge, the bounded analytic correction contributes at most `2eta`; its subtracted linear and quadratic terms contribute at most a fixed multiple of `eta*(|u_j|+1)` per large endpoint. At most two edge factors meet each large vertex, counting repeated/self endpoints. The proposed constant 20 in D4 has ample slack, including `m=1,2`.

The affine bound `(1-24eta)|u|-(.5+22eta)` is at least `.9|u|-.5` for `|u|>=1`: check its slope and its value at 1. This proves D5 and the threshold exponent `2/(5h)`.

An explicit independent diagnostic illustrates the forbidden shortcut. For the unperturbed three-cycle, take one large coordinate `u_S=100`, and call the two unrestricted core coordinates y,z. Its exact imaginary quadratic phase is

`150+(3/2)(y²+z²)-(1/2)yz-(101/4)(y+z)`.

Its unconstrained optimizer is `y=z=101/10`, outside the core box, with value `-4201/40`. Thus completing this Gaussian on all of R² before using the cutoff destroys the positive tail lower bound. The reviewed argument avoids precisely this operation.

## 7. D6: the actual tilted-box estimate, without a dimension-volume loss

For each principal set T, set `z_S=0` and `z_T=exp(-i*pi/4)sqrt(h)y_T`. Define the exact real exponent

`H_T(y)=Re[log(A(h,z_T,0)/a*) + i R_phi(z_T,0)/h]`.

Its base measure is the centered Gaussian with precision `K_TT`, conditioned on the symmetric box `|y_j|<=sqrt(2/h)`. This is not the full covariance restricted to T; the relevant covariance is exactly `K_TT^-1`.

Principal deletion preserves the diagonal entries, can only reduce the off-diagonal supremum sums, and does not increase the local degree. All phase terms still vanish to cubic order. The constant finite-amplitude logarithms contribute `O(mh)`, including edges whose two endpoints were deleted.

The estimates in Section 5 give uniform strict diagonal dominance for the real tilted potentials `V_t=(1/2)y^T K_TT y-tH_T`, for the bounded tilt range needed in L7. At zero, their gradients are `O(sqrt(h))`. Conditional clipped-mode contraction, with ratio at most `.7/1.3`, supplies raw coordinate moments of every fixed order, uniformly in T and m. This is the step that cannot be replaced merely by saying “strong convexity.” The checked hard-box Poincare inequality then gives

`f''(t)=Var_t(H_T)<=2 E_t|grad H_T|²<=C m h`,

where `f(t)=log E_B exp(tH_T)` and the last estimate uses local support and `|partial_j H_T|<=C sqrt(h)(1+sum_near |y_k|²)`.

At t=0, the degree-one log-leading-amplitude and degree-three phase terms are globally odd and have zero expectation under the centered Gaussian on a symmetric box. The remaining terms have expectation `O(mh)` by the same local moments and bounded fourth derivatives. Thus `f'(0)=O(mh)` and `f(1)<=Cmh`.

The unnormalized core integral is its full Gaussian mass times `P(B) E_B exp(H_T)`, with `P(B)<=1`. This is exactly D6. The empty core has determinant 1 and only the `O(mh)` amplitude constants. Nothing here produces `C^|T|`, and no normalization probability is silently set equal to 1.

## 8. Incident amplitudes, Schur determinants and D1

Each changed local amplitude factor has ratio at most 4 by the upper/lower strip bounds. At most `2|S|` factors change, so the cost is at most `16^|S|`, including small-dimensional repeated-edge cases.

The large-coordinate integral is exactly

`integral_(|u|>1) exp[-(.9|u|-.5)/h]du=(20h/9)exp[-2/(5h)]`.

The retained core's Jacobian is `2^(|T|/2)`, and its Gaussian mass is `(pi h)^(|T|/2)/sqrt(det K_TT)`. Dividing by the full mass `(2*pi*h)^(m/2)/sqrt(det K)` leaves `(2*pi*h)^(-|S|/2)` times the determinant ratio.

Since `K` is positive definite and `||K||<=2+4eta<2.1`, its positive Schur complement is bounded above by `K_SS<=2.1 I`. Therefore

`sqrt(det K/det K_TT)<=2.1^(|S|/2)`.

Only the number of actually large coordinates pays a constant. Combining the factors gives `exp(Cmh)[C sqrt(h) exp(-2/(5h))]^|S|`; `C=100` safely covers the displayed numerical factors. Summing over all nonempty subsets is exactly the binomial expression D1. For `mh<=b_h`, its bracket is at most `C_b m sqrt(h) exp(-2/(5h))` at sufficiently small h.

This proves the requested removal of the artificial constant-to-the-dimension loss from actual locality and verified tilted-box hypotheses.

## 9. Derivation of the additional summed range

The Gaussian-normalized D1 error for a single integral must still be multiplied by its full leading Gaussian weight. The absolute trace prefactor gives per-class weight

`a*/(8^m sqrt(det K))`.

The actual Hessian perturbation has operator norm at most `4eta`; since `K_0>=I`,

`K >= (1-4eta)K_0`, and `det K >= (1-4eta)^m D_m/4^m`.

Also `a*<=exp(gamma*m)`. Summing all `4^m D_m` classes therefore costs at most

`exp(gamma*m) (1-4eta)^(-m/2) sqrt(D_m) <= exp(kappa*m)`,

because `D_m<(3+2sqrt(2))^m`. This exact-determinant argument is why the per-class D1 improvement can be retained after the structural counts. Converting `exp(-2/(5h))` to N gives `exp(-4*pi*N/5)` and proves the extra range recorded at the beginning. Genuine exponential winding mass remains; nothing in this calculation provides cancellation.

## 10. Executed checks, clarifications, and safest use

New independent `check_bent_audit.py` uses exact rational arithmetic and explicit fail-closed guards. Results in `bent_audit_checks.json`:

- 5,334 finite corner certificates for the quadratic conditional bound through dimension 6;
- 494 exact principal determinant-ratio checks for two extremal signed nearest-neighbour perturbations through dimension 7, correctly collapsing repeated endpoints;
- 28 exact h/Jacobian normalization checks;
- the unrestricted three-cycle completion counterexample above.

These finite controls do not prove the analytic deformation or uniform local estimates; those are reconstructed in this report. The source's numerical constant checks were read as supporting evidence only.

Recommended clarifications before promotion, without changing the mathematical claims:

1. Explicitly define `h=(2*pi*N)^-1` in the global contour note and `a_J(h)=sum (2*pi*h)^ell a_ell` in the conditional note.
2. Add the short enlarged-endpoint-strip argument for fixed-J amplitude derivative bounds on the closed width-2 strip.
3. Insert the exact principal-box tilt argument and the quantitative radius-enlargement estimates, instead of leaving D6 and the larger local radius as a reference to the small-radius theorem.
4. Keep both Gaussian conditioning factors and the prohibition on unrestricted core completion visible.
5. If the additional summed D1 range is used, state its determinant comparison and fixed `gamma,eta` explicitly; do not merely claim that removing `C^m` automatically improves every numerical rate.

The strongest safe result is a uniform finite-band representation of the actual trace by exact rotated-box integrals, with the stated operator replacement error and exponentially small *contour-tail* error, plus an improved per-integral large-field estimate. The exact local boxes have not been evaluated collectively. Signed CUE comparison and optimal local remainders remain open.
