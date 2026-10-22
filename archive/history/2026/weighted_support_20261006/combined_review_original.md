# Independent interface audit of the selected weighted coefficient

Date: 6 October 2026. Candidate and canonical bytes preserved. This is an independent internal interface audit, not an external referee certificate or formal proof certification.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** For the unchanged odd-N model at tau=10^(-80), every fixed finite J>=0, and every fixed positive band a0<=m/N<=b0<=2, the representation-dependent unit-homoclinic coefficient of V_(N,J) is O(N^(-1/2)). Its once-counted cyclic/negative family contributes O(N^(-1/2)) to the original N^(-2)-normalized time sum. The transfer to U is aggregate only; fixed J>=2 gives an O(N^(-1/2)) pair-aggregate error. No TRACE-005 or BGS closure follows.

The local paired quantum factor approaches one; the individual conditioned Z need not. The physical measure used for the leading term is normalized area, with the genuine sqrt(J_d) half-density retained. The result is not an unweighted label-Haar theorem.

Frozen target:

- `/workspace/shared/bgs_paired_box_cancellation/selected_weighted_coefficient.md`
- SHA-256 `436093814d94cfa05854696777eb762cddb368511a5c2c0b5a84b3705a01674b`
- Frozen input manifest `selected_weighted_sources.json`, SHA-256 `d1f9bc5ad67d4f5864cec58238f36bf7ac33e027a6886f41d26ee2b2aa3b3d61`.

One editorial correction is recommended in Section 4: the displayed real-lift refinement calculation has mixed coefficient -8, not -10. The candidate states it only modulo integers, where both expressions agree; therefore this is not a failed mathematical assertion or a restriction of the verdict. The exact corrected calculation is recorded in Section 5 below. The frozen candidate was not edited.

## Claim card and dependency graph

The coefficient is

A_m,N,J(d)=D_m^(-1) sum_z beta(z+d) conjugate(beta(z)),

where beta(z)=e(NQ_m(z)) alpha_m,N,J(z), G_m=Fix(S^m), and D_m=|G_m|. This is exactly S1 after using the quadratic polarization identity. It is a term of a chosen fixed-J WKB trace representation, not an intrinsic U observable.

The dependency chain audited at the interfaces is:

1. Exact raw branch quotient and polarization -> this autocorrelation normalization.
2. Reviewed transport/Hill identity -> w_0^2=D_m rho_m.
3. Reviewed physical leaf/phase/ratio theorem -> the limiting marked observable f_N=sqrt(J_d)e(NA), with uniform exponentially small finite-period replacement error.
4. Independently accepted norm-uniform EQ -> bounded positive leading mass and periodic-to-area transfer for f_N.
5. Reviewed physical regularity and fibre nonstationarity -> area integral O(N^(-1/2)).
6. Reviewed exact quantum pair factor -> weighted exact-box replacement error O(N^(-1/2)), using the positive mass only.
7. Summed absolute contour tails -> global V coefficient comparison through m<=2N.
8. Cyclic relabeling and negative autocorrelation symmetry -> the once-counted family estimate.
9. Separate near-unitary operator telescoping -> an aggregate U pair comparison, with no orbitwise identification.

The W, Q and EQ proofs are inherited at their independently reviewed scopes. This audit reconstructs the interfaces, norms, phases, counts and transfer rates rather than treating the three positive verdicts as an automatic combined proof.

## 1. Exact leading normalization and the missing-constant trap

From the exact quotient formula, a paired coefficient carries D_m^(-1). The leading alpha at z is e(N Delta_m(z)) w_0(z), with w_0(z)>0 and w_0(z)^2=D_m rho_m(z). Therefore its product contributes

D_m^(-1) w_0(z+d_m) w_0(z)=sqrt(rho_m(z+d_m)rho_m(z)).

This is a sum over the points, without another division by D_m or by the positive mass Z_m^cl. It is exactly S4. There is no remaining 4^m branch factor or 2*pi factor.

The constant e(NQ_m(d_m)) is necessary in the passage to S5. Choose the literal lift d_m=(S^m-I)^(-1)(0,1), so its winding is n=(0,1). The refinement definition gives

Q_m(d_m)=q(d_m)/2,
q(d_m)=(1/sqrt(2)) (1+lambda^(-m))/(1-lambda^(-m)),
p(d_m)=-1/2.

Hence Q_m(d_m)=1/(2sqrt(2))+O(lambda^(-m)). The physical identity from the source-s stationary construction is

A(chi z)=q_label+D_infinity(z)+1/(2sqrt(2)).

Combining these identities with D_m(z)->D_infinity(z) gives

Q_m(d_m)+q_label+D_m(z)=A(chi z)+O(e^(-c m))

uniformly on G_m. Exponentiation multiplies this error by at most 2*pi*N. Thus the complete phase in S4, including its outer constant, converges to the phase used in S5. Omitting that constant would give a different integral identity, even though its absolute-value bound would survive.

## 2. Weighted finite-to-area transfer and the observable norm

The reviewed EQ applies to the same physical forward map F=S composed with the prescribed Hamiltonian flow. Its notation G is not a different dynamical system. It counts each point fixed by F^m once, including points of smaller least period dividing m, with weight |det(I-DF^m)|^(-1). There is no primitive-orbit or orbit-length normalization. The homeomorphism chi identifies this set bijectively with G_m.

EQ applied to 1 gives Z_m^cl=1+O(e^(-c m)), and thus a uniform upper bound for every m>=1. This makes both finite-period replacement steps legitimate: a uniform error epsilon_m costs at most Z_m^cl epsilon_m in the weighted sum. No exponentially large point-count factor appears.

The finite ratio rho_m(z+d_m)/rho_m(z) tends uniformly to J_d(chi z), with an exponential rate. The latter is positive and bounded away from zero. The same is true uniformly for the finite ratio for sufficiently large m; the finite number of remaining m can be absorbed in a constant. Taking square roots therefore preserves the exponential rate. Together with the phase calculation above this gives a pointwise marked replacement O(N e^(-c m)). Any polynomial factor in m in the homoclinic comparison is absorbed by decreasing c.

For f_N(x)=sqrt(J_d(x))e(NA(x)), the torus phase is well defined because A(q+1,p)=A(q,p)+1, A is periodic in p, and N is an integer. The physical theorem gives a fixed C^(1,1/2) bound for its lift modulo q and a fixed C^(0,1/2) norm for sqrt(J_d). On local torus charts,

|e(NA(x))-e(NA(y))|<=min(2,C N dist(x,y)).

In particular ||f_N||_(C^(0,1/2))<=C(1+N), as claimed. A sharper O(1+sqrt(N)) bound is available but unnecessary. The norm includes its supremum term, and its constant is independent of m and N. EQ at the fixed exponent 1/2 therefore costs O(N e^(-c m)). It is genuinely usable for this changing observable; no differentiability of chi, label-Haar approximation, or unquantified weak convergence is substituted.

For each p, q->A(q,p) is a degree-one C^(1,1/2) circle diffeomorphism with derivative >=1/2. Its inverse has a uniform C^(1,1/2) bound. The transformed density

r_p(t)=sqrt(J_d(q(t,p),p))/A_q(q(t,p),p)

has a uniform half-Hölder norm. Averaging over p preserves it. Translation by 1/(2N) changes e(Nt) by -1, so twice the Fourier coefficient is bounded by C(2N)^(-1/2). This proves the first term in S3, with the finite-to-area error supplying the second term.

## 3. Exact quantum and global-contour interfaces

The scale is h=(2*pi*N)^(-1), while the fixed-J amplitude polynomial is sum_(ell=0)^J (2*pi*h)^ell a_ell. The exact box alpha equals e(N Delta) w_0 P Z. Both Gaussian probabilities P are retained in a paired coefficient; the conditional expectation Z is not the full Gaussian-normalized factor by itself.

The independently audited quantum result gives

P_(z+d)P_z Z_(z+d) conjugate(Z_z)=1+O_(J,b)(sqrt(h)),

uniformly for mh<=b, and specifically for m<=2N by taking b=1/pi. It uses imaginary ell_1 and a uniform O(1) unit-winding change. Individual Z has modulus 1+O(sqrt(h)), but its phase need not tend to zero. This is also enough to bound its modulus uniformly without using a denominator.

Therefore

|A_box-A_0|<=C sqrt(h) sum_z sqrt(rho_m(z+d)rho_m(z))
              <=C sqrt(h) Z_m^cl=O_J(N^(-1/2)).

Here only the bounded mass consequence of EQ is used. Full norm-uniform EQ was needed for the preceding leading-term transfer, not for this Cauchy–Schwarz step.

For the global comparison write a=alpha_box and delta=alpha_global-alpha_box, and use ||v||_(2,D)=D_m^(-1/2)||v||_2. The summed absolute contour-tail result, after removing the 4^m exact duplicate branch copies, is

D_m^(-1/2)||delta||_1<=epsilon_N,
epsilon_N=C_J sqrt(N)exp(-4N/5), 1<=m<=2N.

Thus ||delta||_(2,D)<=epsilon_N. Also ||a||_(2,D)^2<=C Z_m^cl. The translation-and-character operator in S1 is unitary for this finite normalized l2 norm. Consequently

|A_global(d)-A_box(d)|<=2||a||_(2,D)epsilon_N+epsilon_N^2
                       <=C_J sqrt(N)exp(-4N/5).

It is essential that the inherited bound is a summed absolute tail; a bound on the signed trace error alone would not imply this coefficient comparison. The source proof supplies the absolute version. This proves S3 uniformly for m<=2N, and its exponentially small terms imply S2 on every fixed positive subband. The statement for local boxes on arbitrary fixed positive m/N bands is justified by the local theorem, but no larger global-contour band is silently imported.

## 4. Cyclic invariance, negative symmetry and short orbits

Write I_z for the global Fresnel integral associated with a physical quotient class. Cyclically permuting all x coordinates, branch coordinates and winding coordinates maps its label to Sz, preserves the action and amplitude product, and maps its cat center to the new cat center. Thus the centered Abel regulator is preserved exactly. The same permutation preserves the retained centered contour box and its product integration convention. Integer re-gluing identifies any resulting representatives with only the already established integral phase. This yields I_(Sz)=I_z.

Since Q_m(Sz)-Q_m(z) is integral, the e(-NQ_m(z)) factor in alpha is also unchanged. Hence alpha(Sz)=alpha(z), for both global and box conventions. No least-period assumption or division by an orbit length occurs.

Alternatively set beta(z)=e(NQ_m(z))alpha(z). Then S1 is simply

A(d)=D_m^(-1) sum_z beta(z+d)conjugate(beta(z)).

The established S invariance of beta gives A(Sd)=A(d) by z=Sy. Complex conjugation followed by y=z+d gives A(-d)=conjugate(A(d)) exactly.

Because S^m d_m=d_m, the positive orbit has some length p dividing m. Its negative orbit is either disjoint or the same orbit. In the latter case A(d_m) is real, consistently with the negative identity. Defining O_m as a set automatically counts either p or 2p displacements, so |O_m|<=2m. No generic full-orbit claim is needed. For example m=1 has d_m=-d_m and the union has one element; the m=2 union has four elements. The proof covers such coincidences, whether or not the finite test range finds further ones.

For odd N, N d_m cannot be zero because its p coordinate is -1/2 modulo one. Invertibility of S on the finite group gives the same nonresonance for every positive or negative cyclic shift. This excludes this selected family from ker N, without deleting or estimating the full N-torsion sector.

## 5. Exact refinement formula and requested editorial correction

For a real lift z with n=(S^m-I)z in Z^2, use the same lift Sz, whose winding is Sn. Symplectic invariance gives

Q_m(Sz)-Q_m(z)
 = (n_q n_p-(3n_q+4n_p)(2n_q+3n_p))/2
 = -3 n_q^2 -8 n_q n_p -6 n_p^2.

The candidate's Section 4 sentence beginning “For n=(S^m-I)z in Z², the direct refinement calculation gives” displays -10 in the mixed term. Recommended edit: replace that -10 by -8. The difference between the two displayed polynomials is 2 n_q n_p, an integer. Since the frozen sentence explicitly asserts the formula only modulo integers, both establish precisely the required invariance modulo one; no conclusion or bound changes. An editorial v2 should preserve an exact hash mapping to this reviewed version.

## 6. Original time normalization and aggregate U transfer

For fixed smooth w compactly supported in (0,2), choose 0<a0<b0<2 containing its support. S2 bounds every coefficient in O_m by C N^(-1/2), including the cyclic and negative images. Hence

|N^(-2) sum_m w(m/N) sum_(d in O_m) A(d)|
 <=2 C N^(-5/2) sum_m m |w(m/N)|
 <=C_w N^(-1/2).

There are O(N) relevant m and m=O(N), so the last weighted sum is O(N^2). This is the unnormalized displacement sum with the original time prefactor N^(-2), not a displacement average. The short-m range eventually lies outside any such support, but the all-m cyclic identity remains valid. Distinct fixed points of shorter least period are still included in each G_m exactly as required by the trace formula.

For fixed J>=1, the separate operator theorem gives epsilon_m=|Tr U^m-Tr V^m|<=C_J N^(3/2-J) uniformly for m<=2N. Since U is unitary, |Tr U^m|<=N, and |Tr V^m|<=N+epsilon_m<=2N for sufficiently large N. Thus

||Tr U^m|^2-|Tr V^m|^2|<=3N epsilon_m<=C_J N^(5/2-J).

Summing O(N) times and multiplying by N^(-2) gives O_(J,w)(N^(3/2-J)). At fixed J>=2 this is O(N^(-1/2)). The estimate transfers the complete pair aggregate, not any individual A(d).

For the central window supported in (0,1/2), writing the benchmark as m is correct. More generally the same transfer works with any identical deterministic benchmark on both sides; on a window crossing m=N the CUE pair benchmark is min(m,N), and the candidate does not assert an m benchmark there. Removing O_m changes the V aggregate by S9 and leaves the central benchmark unchanged. The complement remains the entire once-counted G_m\\O_m, including resonant and complicated displacement classes. The selected family is not assigned any share of the CUE benchmark.

## Obligation matrix

| Interface | Status |
|---|---|
| All 20 input manifest hashes | Passed |
| Same actual physical map and odd-N quantizer | Passed |
| Point counts versus primitive orbit counts | Passed |
| D_m, 4^m and 2*pi normalizations | Passed |
| Constant Q_m(d_m) in the S5 phase | Passed, explicit reconstruction above |
| Finite ratio/phase replacement using positive mass | Passed |
| N-dependent half-Hölder test norm | Passed, O(1+N) suffices |
| Physical-area half-density Fourier bound | Passed at inherited regularity |
| Exact paired P,P,Z factors | Passed; individual Z need not approach one |
| Absolute-tail l1 -> normalized l2 interface | Passed for m<=2N |
| Cyclic/global-Abel/box invariance | Passed |
| Negative orbit and short-orbit overlaps | Passed, once-counted set formulation |
| Odd-N nonresonance of the selected family | Passed |
| S9 original N^(-2) normalization | Passed |
| Fixed J>=2 U aggregate transfer | Passed; no intrinsic U summands |
| Section 4 real-lift mixed coefficient | Editorial correction recommended; modulo-one claim remains correct |
| Full complement, plateau and TRACE-005 | Not addressed |

## Sources, finite checks and audit boundary

The three inherited exact review hashes are:

- Physical W review: `8d64e064a3a4aa66be6391ff15bdbb50b117dc8d6957f9d255691dcda80ba059`.
- Quantum Q review: `fbebcb9aebad1ab23a2fb97c53f11ea63f099bfee4c03c7284128263f77ff7c2`.
- Classical EQ review: `9a6a9faf045de64ceb46a37f11a1bfc3f7d2ca1d519e02da1efc435b80e02e8e`.

The independently accepted EQ includes the bounded-mass consequence, norm-uniform complex observables at exponent 1/2, fixed-point multiplicities, and the exact model/inverse-convention translation. Its entropy source is the verified Mañé 1981 formula together with mandatory 1983 errata. This audit preserves, and does not repair by implication, the earlier unverified original Pesin locator.

New exact control command:

`python3 /workspace/shared/bgs_physical_quantum_homoclinic_review/check_combined_interfaces.py`

Executed result: all 20 manifest entries matched; 18,816 exact rational algebra checks over m=1,...,64 and 49 lifted label samples per m; full cyclic/negative pulse orbit enumeration in each tested m; m=1 negative overlap retained; composite odd-N examples included. The new implementation derives d_m by rational inversion and checks the real-lift refinement formula, quadratic polarization, q-character, cyclic bilinear invariance and negative autocorrelation phase identity. It is independent of the candidate's integer-denominator family checker.

These are finite algebra controls, not a proof of equidistribution, actual oscillatory integrals or asymptotic cancellation. The analytic interface proofs are given above. This report has its own source/artifact manifest and does not replace the earlier quantum audit or its frozen manifest.

## Strongest safe conclusion and remaining frontier

The combined theorem controls the fully weighted unit-homoclinic V coefficient and an O(m)-sized once-counted cyclic/negative family at the original pair-time normalization. The accepted classical EQ now closes the earlier named mass and weighted-transfer dependencies for this family. The exponentially larger complement, its plateau/benchmark mechanism, the complete signed hierarchy and BGS remain open. No further restriction or missing interface implication was found.
