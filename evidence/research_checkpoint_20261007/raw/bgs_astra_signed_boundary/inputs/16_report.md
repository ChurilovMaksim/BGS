# Exact signed charge transfer and a model-specific scalar-gauge obstruction

Research outcome, 6 October 2026. Read-only source: `/workspace/shared/BGS`, HEAD `d4132ccee82849b644520d88c953cb9b33382a59`, with pre-existing dirty files. All new outputs are confined to this separate directory. No canonical edits or publication.

## Result first

1. There is an exact all-multiplicity secular recurrence for the complete coordinate charge amplitudes, coupled to sparse exterior-power evolution of the **prescribed** Jacobi generator. It resums repeated ports of every multiplicity and arbitrary powers, including the plateau, without an Ehrenfest truncation. This is an executable reduction, **not an estimate** of the large-N signed sum. Newton identities and exterior powers are standard; the specialization and the discriminants below are the outcome of this pass.
2. A concrete proposed closure, eliminating the exact ordered transfer phases by a diagonal phase gauge, is false for this map for every odd N >= 19 and every nonzero real algebraic kick time. This uses the actual symmetry-breaking Fourier coefficient, not merely the generic Weyl cocycle. A one-entry diagonal witness is stronger than the initial triangle test. Lindemann–Weierstrass makes the conclusion genuinely fixed-time and nonperturbative; it provides no quantitative cancellation bound.
3. Executed all-occupation Newton reconstructions agree with independent matrix powers, and exhibit substantial *signed* nonzero-charge corrections beyond the Heisenberg threshold at auxiliary coupling. These finite runs cannot probe the asymptotics at fixed tau=10^-80.

## Dependency closure and rejected duplicates

Read AGENTS, source-of-truth/conventions, current RESEARCH and authority files, `four_branch_parametrix.md`, `fixed_map_path_model.md`, `signed_heisenberg_comparison.md`, `frozen_operator_transfer_coercivity.md`, `frozen_algebraic_spectral_simplicity.md`, `heisenberg_time_insertion.md`, the weighted-secular attempt and determinant boundary, and the nearby resolvent frontier. The determinant-covariance and bare self-inversive closures are already ruled out by the deleted-clock example; they are not claimed as new here. The ordinary Weyl-adjoint generator formula is already O5–O6 of the coercivity note. The all-occupation coordinate definitions are shared with the parallel exact-method report, whose independent-phase projection analysis is complementary.

The external input used below is precisely the existing project's Lindemann–Weierstrass leaf: exponentials of distinct algebraic numbers are linearly independent over algebraic numbers. Its verified project locator is in `frozen_algebraic_spectral_simplicity.md` §4. No new external theorem or priority claim is made.

## 1. Exact prescribed structure

Write W(a,b), M, A, U(t)=exp(it N A)M exactly as in `fixed_map_path_model.md`; frequency coordinates here are (a,b)=(p-frequency,q-frequency). Put Q=iN ad A and C=Ad M. Then

P(t)=Ad U(t)=exp(tQ) C,

Q W(nu)=-2N sum_v c_v sin(pi omega(v,nu)/N) W(nu+v),
C W(nu)=W(S nu), S=((3,4),(2,3)).

The finite Fourier coefficients from the stated symbol include

c_(0,1)=1/20-i/200, c_(0,2)=-i/400, c_(0,-2)=i/400.

All formulas use integer Weyl labels with their actual wrap signs; no periodicization dropping the half-shift is made. Specifically

W(a+Nr,b+Ns)=(-1)^(br+as+Nrs) W(a,b).

These identities are algebraic at every finite odd N. They are independent of a semiclassical parametrix error.

## 2. Complete-transfer diagonal obstruction, all algebraic nonzero times

**Proposition.** For every odd N>=19 and nonzero real algebraic t, the matrix P(t) in the ordinary Weyl basis cannot be made real by conjugating with a diagonal unitary matrix. Consequently it cannot be converted by such a gauge into a scalar real/positive transfer whose ordered-path phases are only endpoint phases.

**Proof.** Use nu=(-1,(N+1)/2). Then

S nu=(2N-1,(3N-1)/2),
S nu+(0,1)=nu+(2N,N).

The corresponding wrap sign is (-1)^(3N)=-1. Also omega((0,1),S nu)=1-2N. The symbol support is injective modulo N for N>=19. Therefore the only symbol frequency contributing to the indicated diagonal derivative is v=(0,1), and exactly

(d/dt) P(t)_(nu,nu)|_(t=0)=2N(1/20-i/200) sin(pi/N).

Its imaginary part is -N sin(pi/N)/100 !=0. In particular this witness is the actual nonreal symbol coefficient; it is not the generic commutation phase. A diagonal phase conjugation leaves diagonal entries unchanged.

It remains important not to infer the specified time from a Taylor coefficient and an uncontrolled remainder. A is Hermitian algebraic, M and every W are algebraic. By its algebraic spectral projectors, each entry of P(t) is a finite exponential polynomial with algebraic coefficients and frequencies iN(a_j-a_k). The real-time imaginary part is itself a finite exponential polynomial (extend the conjugated expression analytically), with algebraic coefficients/frequencies. It is nonzero as an entire function by the displayed derivative. At any fixed nonzero algebraic t, collect identical frequencies and apply Lindemann–Weierstrass: a nonzero such polynomial cannot vanish. Thus Im P(t)_(nu,nu) !=0 at the literal tau=10^-80, for every N>=19. This concludes the claim without a small-tau remainder. □

The witness is a high Weyl frequency. Its use is valid precisely because the goal concerns the full transfer, not a low-frequency Egorov surrogate. The proposition is a failure of one resummation mechanism. It does not obstruct a complex signed resummation, quantify the imaginary entry, prove a positive lower bound on the pair defect, or refute BGS.

For comparison, even the kick alone has a nontrivial model-specific cycle holonomy. Use Weyl vertices (1,0),(1,1),(1,2). Its three frequency increments are collinear (0,1),(0,1),(0,-2), with all mutual symplectic products zero. Nevertheless

c_(0,1)^2 c_(0,-2)=1/800000 + 99 i/16000000.

Multiplication by the nonzero real sine factors gives a nonreal generator cycle product. The same exponential-polynomial argument applied to the three kick entries proves the nonreal cycle invariant at every nonzero real algebraic time. Thus this is not a restatement of noncommutativity of two Weyl generators.

## 3. Exact all-multiplicity recurrence, with sparse actual dynamics

For formal commuting x_1,...,x_N, let D_x=diag(x_j), and define

p_m(x;t)=Tr((D_x U(t))^m)=sum_(|n|=m) c_m(n;t) x^n,
b_I(t)=det U(t)_(I,I),
e_k(x;t)=sum_(|I|=k) b_I(t) x_I.

Every repeated-port occupation is included. The finite secular polynomial is

det(I-z D_x U(t))=sum_(k=0)^N (-z)^k e_k(x;t).

Coefficient comparison in its logarithmic derivative gives the exact recurrence

c_m(n;t)=sum_(I:1<=|I|<m, |I|<=N) (-1)^(|I|-1) b_I(t) c_(m-|I|)(n-1_I;t)
          + (-1)^(m-1) m b_I(t) if n=1_I and |I|=m<=N.

The last term is zero otherwise; coefficients with negative components are zero. This holds for every m, without an upper time cutoff. At m>N it is a homogeneous recurrence driven by the same finite collection of minors. Self-inversiveness gives b_I=det(U) conjugate(b_(I-complement)), but does not remove the denominators/logarithm or create charge orthogonality.

Here the minors have additional *actual-model* structure. Let X_r(t)=wedge^r U(t), indexed by r-subsets. Then exactly

(d/dt) X_r(t)=iN H_r X_r(t), H_r=dGamma_r(A), X_r(0)=wedge^r M.

H_r connects only configurations obtained by one nearest-neighbor occupied-site hop, with the appropriate fermionic ordering sign, together with the sum of on-site diagonal values. Its coefficients are those of the fixed trigonometric Jacobi A; there is no new ensemble. Initial X_r entries are the explicitly known Fourier–chirp minors of M. Principal b_I are X_r(I,I). Their evolution involves off-diagonal X_r(K,I); replacing this by a closed positive evolution of the principal energies discards quantum currents. This is the named missing closure, and the proposition above shows why a scalar endpoint-phase gauge does not supply it.

The recurrence yields the complete signed pair exactly:

|Tr U(t)^m|^2 = |sum_n c_m(n;t)|^2
              = sum_n |c_m(n;t)|^2 + sum_(n!=n') c_m(n;t) conjugate(c_m(n';t)).

The second sum is the full nonzero-charge contribution; it has no restriction on repeated ports or on the number of reconnections. Known coordinate families can be subtracted **after** this complete resummation, leaving the genuine OTHER rather than a family overlap convention. This does not yet bound OTHER.

## 4. Plateau retained exactly

Equivalently, |Tr U^m|^2=Tr_HS P^m. For 7 not dividing N, the existing simplicity theorem gives an exactly N-dimensional fixed eigenspace of P. For 0<z<1,

N^-2 sum_(m>=1) z^m |Tr U^m|^2
= z/[N(1-z)] + N^-2 Tr_(fixed-space-perp)[z P (I-zP)^-1].

With z=exp(-2s/N), the first term tends to 1/(2s). The CUE target is (1-exp(-2s))/(4s^2), so the second term must tend to

(1-exp(-2s)-2s)/(4s^2),

which is negative. Therefore a positive bound or a dephasing argument that throws away the complementary signed term cannot generate the plateau crossover. For dimensions with multiplicities, replace N in the fixed-space rank by sum of squared eigenvalue multiplicities; no simplicity is assumed there. This full resolvent identity is standard and is included to identify what the recurrence must actually estimate.

## 5. Executed discriminants and limits

`probe.py` constructs the symbol over Q(i), performs exact QQ(zeta_(4N)) arithmetic for a principal-energy current derivative, and reconstructs all charge coefficients from all principal minors. It checks their evaluations against direct powers of D_phi U and U. `independent_check.py` assembles A directly from the trigonometric midpoint formula, independently of Fourier extraction, and checks the complete-transfer diagonal derivative above for N=19,21,23,25,31. These latter matrix cross-checks are floating diagnostics of the exact proof, not interval certificates.

The exact derivative of sum_j |U_jj(t)|^2 at t=0 is nonzero at N=3,5,11 and zero at N=7,9,19. The zeros are retained, not filtered. Thus a naive claim that every charge-zero observable immediately has a nonzero linear current is false. The complete-transfer diagonal witness avoids that false inference. N=7 is a symbol-aliasing exceptional control: r(j/7)=0 and the sampled generator is scalar; its charge data must not be read as representative nonlinear dynamics.

At auxiliary tau=0.137, N=5,m=12, all 1820 occupations are retained. The full pair is approximately 2.4276450675, the charge-zero term 5.0430943137, and the signed nonzero-charge correction -2.6154492462. The Newton polynomial/direct matrix residual is below 9e-15. N=7,m=14 retains all 38760 occupations; it is the exceptional scalar-kick control just described. A separate N=9,m<=10 run supplies a non-scalar additional check. See JSON outputs for complete tested ranges, rather than inferring an unexecuted range from the algorithm.

These checks are structural discriminants. They do not access N anywhere near the fixed-tau quantum crossover. The actual fixed tau is never replaced by 0.137 in a theorem. The all-N nonvanishing proposition above uses exact algebraicity and is separate from the numerical probes.

## 6. Executable continuation and stopping condition

The next meaningful task is to estimate the complete cross-charge quadratic form generated by the exterior Jacobi evolution, not to enlarge a repeated-port cutoff. The executable recurrence permits exact comparisons of candidate signed identities at all multiplicities before attempting bounds. A candidate identity must survive both phase-evaluated direct powers and the model-specific nonreal diagonal witness. A successful analytic continuation would bound the signed microscopic resolvent remainder in §4 (or its compact-weight analogue), including the negative plateau correction. A larger finite run alone is not success, and no global research-attempt quota is implied.

No such quantitative bound was proved in this pass. The present route outcome is a rigorous specific failed mechanism plus an explicit all-multiplicity continuation. TRACE-005 and deterministic BGS remain open.

## 7. Collective charge-excursion resummation (added continuation)

There is a more useful exact reduction than the scalar gauge test. On the 2m-replica space define

K_m(t)=U(t)^(tensor m) tensor conjugate(U(t))^(tensor m),
H_m=sum_(r=1)^m A^(r) - sum_(r=1)^m conjugate(A)^(m+r),
K_m(0)=M^(tensor m) tensor conjugate(M)^(tensor m).

Thus K_m(t)=exp(itN H_m)K_m(0). Let R_m be the tensor product of the ket and bra cyclic permutation operators, with matching trace convention, so that Tr(R_m K_m)=|Tr U^m|^2. Let Π be the diagonal coordinate projector onto pairs of ordered m-tuples having identical occupation vectors, and Q=I-Π. Both R_m and H_m commute with the simultaneous replica-cycle action; R_m also commutes with Π.

The independent-coordinate-phase charge-zero pair is exactly

B_m(t)=Tr(R_m Π K_m(t)),

whereas the actual full pair is Tr(R_m(Π+Q)K_m(t)). This is a finite, unaveraged identity for the maintained matrices; averaging is used only to identify the projector, not imposed on U.

**Exact compression identity:** Π H_m Π=0. Diagonal on-site energies cancel because the occupation vectors agree. Every off-diagonal nearest-neighbor Jacobi hop, on either ket or bra, changes the charge by a nonzero dipole, hence leaves the balanced subspace. This holds with all repetitions; no distinct-port hypothesis enters.

Write X(t)=ΠK_m(t), Y(t)=QK_m(t). Eliminating Y gives the exact all-excursion Volterra equation

X'(t)=iN ΠH_m Q exp(itN QH_mQ) QK_m(0)
       -N^2 integral_0^t ΠH_mQ exp(i(t-s)N QH_mQ) QH_mΠ X(s) ds,

Y(t)=exp(itN QH_mQ) QK_m(0)
       +iN integral_0^t exp(i(t-s)N QH_mQ) QH_mΠ X(s) ds.

Exponentials here are on the Q-subspace. There is no finite interaction cutoff, Markov approximation, discarded multiplicity, or truncation at Ehrenfest time. Both the inhomogeneous initial metaplectic source and the memory kernel must be retained. The full pair is obtained by tracing R_m(X+Y); in particular the Q contribution is not assumed negligible.

The actual Jacobi coefficients give a new exact scale for this memory kernel. Set d_m=rank Π=sum_(|n|=m)(m!/prod n_j!)^2. Direct counting of orthogonal single-replica moves gives

Tr(Π H_m Q H_m Π)/d_m = (2m/N) ||A_off||_HS^2.

Here HS is the **ordinary unnormalized** matrix norm. For the prescribed symbol and odd N>=19, its off-diagonal entries are r(q+half-shift)(-3∓4i)/1000. Fourier degree of r^2 is at most 16, so exact lattice averaging equals its constant Fourier coefficient, namely 9/4. Therefore

||A_off||_HS^2=9N/80000,
Tr(Π H_m Q H_m Π)/d_m=9m/40000.                 (★)

This exact relation is uniform in arbitrary m, including m comparable to and larger than N, and includes all occupation multiplicities. It is not a Taylor approximation at tau. It calibrates the initial memory-kernel strength, rather than proving its long-time decay. The source cannot be discarded on norm grounds: K_m(0) is unitary, so the squared HS norm of ΠH_m QK_m(0) is exactly the left-hand trace in (★).

`projector_check.py` independently checks the zero-compression and occupation-balance counting at (N,m)=(3,1),(3,2),(3,3),(5,2),(7,2), using exact integer combinatorics, and checks the constant coefficient 9/4 over exact rational polynomials. It does not assume the large-N no-alias energy formula in dimensions below 19. The all-N proof of (★) is the preceding Fourier identity and symmetry count.

This supplies a concrete next analytic target: estimate the traced, *signed* driven Volterra system using the sparse dipole coupling and the exact off-charge Hamiltonian, rather than posit phase independence. The obstruction is now precise: there is no proved control on its oscillatory memory kernel or its correlated metaplectic source at m~N and t=tau. Kernel size at zero, even the exact formula (★), does not justify a Markovian decay model. The full-pair plateau is still present because X and Y reconstruct the entire original replica transfer.

Finally, the no-real-gauge proposition in §2 is strictly about a diagonal phase change of the ordinary Weyl basis. A general change to a Hermitian operator basis does make Ad U real orthogonal. Nothing here excludes that general basis change, and it does not produce positive weights or a decay estimate.

An additional independent full-replica test (`replica_check.py`) at N=3,m=2 reconstructs the 81-dimensional Hamiltonian directly, verifies the replica/occupation-polynomial full and charge-zero pair dictionaries, and numerically integrates the Volterra memory term with 32-point Gauss quadrature. The largest reported residual is below 9e-16. This is an auxiliary-coupling floating cross-check, not a certified analytic quadrature bound. The energy comparison there uses the actual finite aliased A, not formula (★), whose stated N>=19 hypothesis is preserved.

At N=9,m=10 and auxiliary tau=.137, the additional non-scalar run retains all 43,758 occupations and gives full pair 3.9460222197, charge-zero pair 8.5837658724, and full nonzero-charge sum -4.6377436527. Maximum phase-evaluation residual over m<=10 is below 1.9e-14.
