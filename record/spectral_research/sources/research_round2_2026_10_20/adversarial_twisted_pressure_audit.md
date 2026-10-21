> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_twisted_pressure_audit.md`. Embedded SHA256: `d0779d626fe958e466e476830bc3911048f8fe2b8f4e712d2069958ccbd13cea`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of all Weyl-twisted trace bounds

Date: 20 October 2026. The original family and the exact fixed
`tau=10^-80` are used throughout.

## 1. Frozen input and verdict

The audited file is `fermionic_twisted_pressure.md`, SHA-256
`9bfc9b4a27e8cd7d23bc1693d439f7cb0be31321fbe1947875d9bb8271649bd5`.
Its pressure input is `fermionic_pressure_transfer.md`, SHA-256
`90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756`,
independently audited in `adversarial_pressure_audit.md`.

For the genuinely new exact-sector passage I also read the original
proofs in `../research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md`,
SHA-256 `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b`,
Sections 3, 5–8, and in `gaussian_cocycle_and_modulus.md`, SHA-256
`c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1`,
Sections 1–9. This audit does not infer the twisted identity merely from
the already established untwisted conclusion.

**Verdict: PASS.** The bound

$$
\sup_{a,b\bmod N}|\operatorname{Tr}(T_N(a,b)U_N^m)|
\le C_\eta e^{(P_*+\eta)m}+2(0.421)^m
$$

holds with the claimed single threshold for each fixed `eta>0`, uniformly
over positive `m` and all Weyl indices. Its new consequences at the first
Pell return are justified. The proof does not bound the corresponding
spectral-difference projections under `Ad U_N`, and does not claim to.

## 2. Pointwise Gaussian identity, including the endpoint gauge

Use the physical forward map `Psi=phi_a^(-tau/(2pi)) composed with L`.
At an edge let `alpha=F_QQ`, `beta=F_Qq>0`, and `gamma=F_qq`. An input
tangent vector of slope `s=delta p/delta q` satisfies

$$
\delta p=-\gamma\delta q-\beta\delta Q,
\qquad \delta P=\beta\delta q+\alpha\delta Q.
$$

Therefore its coordinate expansion and new slope are

$$
b=-(\gamma+s)/\beta,
\qquad s'=\alpha-\beta^2/(\gamma+s).
$$

Near the cat slope `s_0=-1/sqrt2`, the derivative of the slope map is
`beta^2/(gamma+s)^2<0.04`. The parameter derivatives have absolute sum
less than two on the stated neighborhood. The map on continuous sections
is consequently a contraction on `||s-s_0||<=4 eta_F`; this construction
does not presume ambient differentiability of the unstable bundle. The
coordinate expansion is positive and greater than five, identifying
the resulting line as the unstable one.

The proposed section `C(x) exp(s(x)y^2)` has scalar product one with
the fixed reference Gaussian. Its normalization

$$
C(x)=\frac{\sqrt{-s(x)-s_0}}{d_0\sqrt\pi}
$$

is correct. The elementary Gaussian moment bounds in the input give its
distance from the reference vector at most `24 eta_F`, so it lies in the
same uniquely normalized graph ball as the existing operator cocycle.

Applying the exact Gaussian kernel

$$
\lambda_0^{-1}2\sqrt\beta
\exp(\alpha y'^2+2\beta y'y+\gamma y^2)
$$

and completing the square gives its scalar multiplier

$$
\gamma_0(x)=\sqrt\lambda\,b(x)^{-1/2}
\frac{C(x)}{C(\Psi x)}.
$$

Both factors `2 sqrt(beta)` and
`lambda_0=2 sqrt(pi)/sqrt(lambda)` are used here. This is a pointwise
identity for the actual graph, established by uniqueness; it is stronger
than a statement about its products around closed cycles.

For `w(x)=(1,s(x))` and `n(x)=||w(x)||` in the metric used for pressure,

$$
J^u(x)=b(x)n(\Psi x)/n(x).
$$

The correct scalar gauge is `D=C/sqrt(n)`, as in the input. Direct
substitution verifies

$$
\gamma_0(x)=\sqrt\lambda[J^u(x)]^{-1/2}
D(x)/D(\Psi x).
$$

Its open products therefore differ from `J_m^u(x)^(-1/2)` by the bounded
endpoint ratio `D(x)/D(Psi^m x)`. The original Gaussian proof, equation
(8.7), already establishes the uniform **pointwise** estimate
`log|gamma_h|^2=2 log gamma_0+O(h^2)`. Summing that pointwise estimate
proves the claimed open-product estimate for every base point and every
length, with one edge threshold. No periodic repetition is used to infer
it and no `mh^2` smallness is assumed.

## 3. Exact rational twist and its signs

For integer representatives `a,b` put `xi=(a/N,-b/N)`. Direct action on
the comb quotient gives

$$
T_N(a,b)=(-1)^{ab}(\mathcal T_{-\xi})_N.
$$

The scalar is the difference between an ordinary real half and the
modular inverse `(N+1)/2`. It has not been discarded in the finite trace.
For every integer deck vector `w`, the commutator of
`mathcal T_(-xi)` and `R_w` is one because
`N(-xi_p w_q+xi_q w_p)` is an integer. Thus
`W=mathcal T_(-xi)V^m` has exactly the same integer-deck covariance as
`V^m`. The existing coherent frame and coset unfolding consequently
apply to `W`, with the same number of cosets and without an extra
determinant factor.

Independently multiplying the two physical Weyl operators gives

$$
R_{-n}\mathcal T_{-\xi}
=(-1)^{n_qn_p}
\exp\!\left[\frac{i(n_p\xi_q-n_q\xi_p)}{2h}\right]
\mathcal T_{-(n+\xi)}.
$$

For the rational `xi` in use, the exponential is the sign
`(-1)^(n_p a+n_q b)`. Thus the total finite-Weyl and sector sign, before
the already known metaplectic scalar, is
`(-1)^(ab+n_q n_p+n_p a+n_q b)`. This agrees with all signs in the input.
The boundary action must use `t=n+xi`:

$$
q_m=q_0+t_q,
\qquad S_{m,t}=\sum_{j<m}F(q_{j+1},q_j)
-t_p(q_0+t_q/2).
$$

Its critical equations are exactly `Psi^m x=x+n+xi`, with the physical
translation sign shown. In particular there is no unintended replacement
of `xi` by `-xi` in the return set.

## 4. Convergence, critical points, and the nonperiodic endpoint

The original proof expands each exact plane operator into translated
metaplectic words with finite total absolute coefficient mass at fixed
`m,N`. Left multiplication by the rational Weyl translation only shifts
their real displacements and changes unit-modulus factors. The original
whole-plane coherent integral bound and lattice Gaussian bound are
independent of those displacements. Hence they justify the same absolute
convergence and coset rearrangement for the twisted operator.

The same fact verifies its Abel/Fresnel interpretation. The path-word
Hessian is still `-(6I-R-R^-1)/4`; the twist changes only real linear and
constant terms. The common bound for each damped Gaussian integral is
independent of its real linear term. The finite absolute word mass thus
permits the same composition and common Abel limit. This proves the new
exact sector input before any contour reduction.

The perturbed real action is uniformly strictly concave for every real
`t`. Its quadratic part is coercive toward minus infinity; its remaining
bounded phase perturbation and fixed linear term do not change existence
or uniqueness of its critical point. Changing an initial integer lift
changes `n` by `(L^m-I)w`. This proves the claimed bijection and count

$$
\#\{x:\Psi^m x=x+\xi\}=|\det(L^m-I)|<\lambda^m
$$

for every real torus translation. The multiplicities of coincident
edges for `m=1,2` are retained in the stated cyclic Hessian.

At a critical orbit, position variations satisfy `z_m=z_0` even though
the base orbit is open. The edge linear terms telescope to
`(p_m-p_0)z_0=t_p z_0`, canceled exactly by the boundary action. All
centered edge kernels are therefore the same globally defined operators
as in the untwisted construction. Their contour coercivity, trace-class
norms, and one-edge threshold were uniform over all real base points,
so no new time- or translation-dependent threshold is introduced.

The rank-one product has trace

$$
\Gamma_h(x,m)\ell_h(x)v_h(\Psi^m x).
$$

The endpoint bracket is correctly retained. Its norm is at most
`(1+r_0)/(1-r_0)`, and all mixed rank-one/residual words still vanish
because that cancellation uses consecutive edges, not equality of the
two endpoints. The residual trace bound is consequently still
`0.209(0.174)^(m-1)`. Summing over fewer than `lambda^m` critical points
with the outside factor `lambda^(-m/2)` proves the unchanged
`2(0.421)^m` total residual.

## 5. The finite cyclic difference argument

Ordinary periodic expansivity would be insufficient for an open translated
return. The proof in the input avoids that error. For two points of the
same return set choose their short lift differences `d_j`, `0<=j<m`,
and use the common endpoint translation to set `d_m=d_0`. The integer
jump in their difference recurrence has norm less than the shortest
lattice vector, by the specified separation radius, and hence vanishes.

Extend only these finite difference and forcing lists periodically.
They solve the bounded two-sided equation

$$
d_{j+1}-Ld_j=e_j,
\qquad \|e_j\|\le\kappa\|d_j\|.
$$

The checked Green inverse then gives `||d||<=K kappa ||d||` and thus
`d=0`. The actual nonlinear orbit has not been periodically continued.
This proves a single separation radius for all lengths and all real
translations.

The positive sum of `J_m^u(x)^(-1/2)` over any such set is bounded by
the same fixed-scale separated-set partition supremum. Its logarithmic
limsup is at most `P_*`. Absorbing the finite initial range gives the
uniform pressure upper bound in `xi`. There is no extra transfer-operator
or periodic-orbit asymptotic assumption.

## 6. Uniformity and the actual consequences

Combining the pressure bound with the two bounded endpoint factors and
the open modulus gives an exponential error rate `C_jet h^2/2` per
edge. A single dimension threshold absorbs it into `eta/2` for every
length and translation. This proves the all-Weyl assertion (A).

At `N_r=(lambda^r-lambda^-r)/(4sqrt2)` and odd `r` tending to infinity,
the same exponent conversion as in the scalar pressure audit gives

$$
\max_{a,b}N_r^{-1}|\operatorname{Tr}(T_{N_r}(a,b)U_{N_r}^{2r})|
=O(N_r^{-\delta})
$$

for every fixed `0<delta<2 Delta/log lambda`. The constants may depend
on that chosen exponent, as stated. Taking adjoints permutes the Weyl
family, so the exact Hilbert–Schmidt expansion proves separation from
every scalar multiple of every Weyl operator.

The coefficient-spreading claims use only the complete exact orthogonal
Weyl basis. For a unitary matrix its normalized Weyl coefficients satisfy
`sum_v |c_v|^2=1`. Therefore
`sum_v |c_v|^4<=max_v |c_v|^2`; the claimed inverse-participation lower
bound follows. If a comparison unitary has at most `K` supported Weyl
coefficients, Cauchy–Schwarz gives its normalized overlap at most
`sqrt(K) max_v |c_v|`, proving the sparse-comparison assertion.

These last steps are valid in every odd composite dimension as well as
at primes. They do not infer unweighted eigenphase-pair counts from
matrix-element weights. The unsolved order-one exponential pair bound
and all higher comparisons in `H_diag` remain explicitly outside this
result.
