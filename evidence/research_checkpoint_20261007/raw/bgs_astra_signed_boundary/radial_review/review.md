# Independent audit: actual charge compactness and radial shell

## Normalized claim and verdict

**Proved as written**, for the stated untwisted, centered transfer and relative
to the expressly inherited actual-map analytic inputs. There is no missing
compactness, embedding, uniformity, adjoint, or all-odd-dimension implication
in the new theorem. Two notational corrections and one scope clarification
are listed below; none changes the hypotheses or conclusions C1–C3.

The audited candidate is `actual_radial_shell.md`, SHA256
`43319ca5c799fd6e10479fca71e8c8fa5d7783dcd38b7493e48bba11218de37a`.
This is fresh independent internal mathematical review, not external referee
acceptance or formalization. Canonical BGS was read only. All audit output is
confined to `radial_review/`; no claim status, manuscript, publication, commit,
or remote state was changed.

For the literal odd-dimensional U_N at fixed tau=10^-80, let T_N=Ad(U_N),
D_N=sum_a P_a T_N P_a, and L_N(delta)=(1-delta)T_N+delta D_N. In a common
ordinary-Weyl isometric embedding, the extensions of D_N converge in operator
norm to compact K. Every centered unit T_N-quasimode whose unit-circle
residual tends to zero is annihilated in norm by both D_N and D_N*. For
every positive delta_N tending to zero, uniformly over every centered
eigenvalue lambda of L_N(delta_N),

    ||lambda|-(1-delta_N)| = o(delta_N),
    dist(lambda,(1-delta_N) spec(T_N|H_N^0)) = o(delta_N).

The second assertion is one-sided spectral proximity. No power-norm bound,
eigenvalue bijection, effective rate, arbitrary-twist estimate, or signed
Heisenberg boundary estimate follows.

## 1. Dependency graph and source checks

The new chain is:

1. The exact ordinary-Weyl midpoint formula identifies the charge-a fiber
   with its shifted discrete q-Fourier basis.
2. A12/A13 of the pinned all-translation source give a compact operator-norm
   limit for every fixed positive charge in the step embedding; G2/G3 of
   the pinned one-step source supply charge zero.
3. The exact negative-charge antiunitary relation gives the same statement
   for fixed negative charges. The step and Fourier embeddings are strongly
   compatible on both sides, sufficient to transport a compact norm limit.
4. A8/A11 supply the simultaneous growing-charge tail bound. Finite-fiber
   norm convergence plus these tail bounds give full operator-norm
   convergence to a compact direct sum.
5. FM-018 O8 at one step and the exact alias convention give strong
   convergence of the full quantum adjoint to C_G. Unitarity of C_G gives
   the corresponding adjoint strong convergence.
6. FM-018 O11, extended to L2, excludes centered unit-circle eigenfunctions
   of the actual normalized-area Koopman operator.
7. Weak compactness forces every centered quantum quasimode to escape all
   fixed classical modes. Compactness of K and K* converts this into both
   norm-annihilation assertions.
8. Every damped eigenvector is a 4 delta-quasimode. Its eigenvalue equation
   gives the radial shell; normality of T_N gives one-sided spectral
   proximity.

All 18 input-file checksums in the parent source manifest were recomputed
and agree. The candidate checksum also agrees with the assigned pin. The
raw pinned proofs, rather than only summaries, were inspected. The existing
all-translation review covers the exact A8/A11/A12/A13/A15/A16 input used
here. The one-step review covers the zero-charge norm limit G3. Their
candidate checksums agree with this packet.

For the classical leaf, the durable FM-018 source check identifies
Parry–Pollicott, Proposition 2.4, printed pp. 29–31 / PDF pp. 33–35,
with Theorem 2.2(ii) and Appendix III.3. Its transfer to the same nonlinear
normalized-area measure explicitly retains FM-001 and the FM-006
area/Gibbs identification, including their Ruelle/Pesin inputs. This audit
uses that checked source boundary. It does not independently re-prove the
underlying mixing theorem, all of the actual parametrix, or the literal-time
nonlinear phase certificate. No new external theorem is imported.

The strict one-step bound ||D_N|H_N^0||<1 is not actually needed for the
new radial-shell proof. Only its zero-charge compact norm limit is used.
The older strict gap is relevant to comparing the new conclusion with the
previous damped interior estimate.

## 2. Ordinary Weyl, midpoint phases, and all aliases

For odd N, inv2=(N+1)/2 and the raw Weyl action is

    (T_N(a,b)psi)(j)=e_N(b(j+inv2*a)) psi(j+a).

Consequently the ordinary Weyl matrix W_N(a,b)=(-1)^(ab)T_N(a,b) has
the exact entry

    W_N(a,b)_(j,k)=e(b(j+a/2)/N) 1_(k=j+a mod N).

Indeed its extra exponent is ab/2+ab(N+1)/(2N), which differs from
ab/(2N) by the integer ab. This works for negative labels, odd a, and
wrapped j+a. There is no additional half-grid sign to discard.

For centered representatives a,b, these matrices are orthonormal for
the normalized Hilbert–Schmidt inner product. Different a have disjoint
matrix support; for equal a, orthogonality in b is the exact finite
geometric sum. Therefore

    I_N W_N(a,b)=e(bq+ap)

is an isometry onto the square Fourier band V_N. All odd N have a unique
centered residue representative; no prime, coprime, parity-subsequence,
or spectral-simplicity assumption enters.

For arbitrary integer aliases k,l, the exact relation is

    W_N(a+kN,b+lN)=(-1)^(bk+al+Nkl) W_N(a,b).

The factor has modulus one, but it is not always +1. The proof never
identifies aliases without it. If r_N(nu) is the centered reduction and
sigma_N(nu) this sign, then for every smooth f with absolutely summable
Fourier coefficients,

    I_N Op_N(f)=sum_nu fhat(nu) sigma_N(nu) e_(r_N(nu)).

In particular,

    ||I_N Op_N(f)-f||_2
      <= 2 sum_(nu outside the centered square) |fhat(nu)| -> 0.

This estimate is a direct alias-safe way to fill in C3's fixed-symbol
quantization convergence. It requires neither uniform high-frequency
Egorov nor operator-norm closeness of the two embeddings.

Direct matrix multiplication gives the charge block

    B_(N,a)(j,k)=U_N(j,k) conjugate(U_N(j+a,k+a)),

with no N or sqrt(N) factor. A coefficient vector f_j corresponds to the
matrix having f_j at (j,j+a), and its normalized HS norm equals
(N^-1 sum_j |f_j|^2)^(1/2).

## 3. Transporting the step limit to the common Fourier embedding

Use normalized l2_N and let J_N send a vector to its step function on
[j/N,(j+1)/N). Let F_(N,a) send the orthonormal discrete basis

    f_b(j)=e(b(j+a/2)/N), b centered,

to e(bq). Then I_N restricted to charge a is precisely F_(N,a), with
the p-factor e(ap) appended. Put S_(N,a)=F_(N,a)J_N*.

For a fixed integer b and all sufficiently large odd N, an exact cell
average calculation gives

    S_(N,a)e(bq)
      = sinc(pi b/N) e(b(1-a)/(2N)) e(bq),

where sinc(0)=1. Also S_(N,a)*e(bq) is the step function whose value in
cell j is e(b(j+a/2)/N). Thus both S_(N,a) and its adjoint converge
strongly to identity for each fixed a. Their operator norms are at most
one, so trigonometric-polynomial density extends these conclusions to L2.

If K_a is compact, finite-rank approximation gives

    ||S_(N,a) K_a S_(N,a)*-K_a|| -> 0.

The exact algebra is

    F_(N,a) B_(N,a) F_(N,a)*
      =S_(N,a) [J_N B_(N,a) J_N*] S_(N,a)*,

because J_N*J_N is identity. Hence the accepted step-embedding norm
limit transports to the ordinary-Weyl Fourier embedding. This closes
the potentially important escaping-alias issue: strong convergence alone
would not transport an arbitrary noncompact operator in norm, but the
limit here is compact and the original convergence is already in norm.

For completeness, negative charge requires an antiunitary, not a purely
unitary, comparison. With (R_c f)(j)=f(j+c), exact entries give

    B_(N,-c)=R_(-c) conjugate(B_(N,c)) R_c.

On L2, J_N R_(+/-c) J_N* and their adjoints converge strongly to identity
for fixed c. Complex conjugation commutes with J_N. Applying the same
compact-conjugation argument shows

    J_N B_(N,-c) J_N* -> conjugate(K_c),

where conjugate(K_c) means f -> conjugate(K_c(conjugate(f))). This
operator has kernel conjugate(k_c(x,y)) and is exactly K_(-c).
Thus the positive-charge source suffices without assuming a reflection
symmetry of U_N or an unproved uniform approximation for negative shifts.

## 4. Why all charge fibers give a compact norm limit

A11 and the negative-charge norm identity imply: for every eta>0 there
are C_eta,N_eta such that every odd N>=N_eta and every centered
|a|>=C_eta satisfy ||B_(N,a)||<=eta. For any fixed such integer a,
letting odd N tend to infinity in the fixed-a norm limit gives
||K_a||<=eta. This is valid even though a may be arbitrarily large:
one fixes it before passing to N, while the same C_eta works for all a.

On the orthogonal decomposition

    L2(T2)=direct_sum_(a in Z) {f(q)e(ap)},

define K=direct_sum_a K_a. Its finite-a truncations are compact. The
tail operator norm is sup_(|a|>=C) ||K_a|| and tends to zero, so K is
compact. If Dbar_N=I_N D_N I_N*, then after a fixed charge cutoff,
the finitely many retained blocks converge in norm. The remaining
blocks have difference norm at most 2 eta, including a outside the
finite quantum band where the quantum block is zero. Therefore

    ||Dbar_N-K|| -> 0.

The same holds for adjoints by taking adjoints in this norm limit.
The constant vector is exactly I_N I; both Dbar_N and Dbar_N* fix it.
K and K* therefore fix it and preserve its orthogonal complement.

Norm convergence to compact K, together with finite rank of each Dbar_N,
also proves collective compactness in the usual sense. Nothing here
asserts trace-class convergence or a rate for the tail cutoff.

Fixed-mode pairings and Egorov identify K_a=i_a* C_G i_a. The full
operator is the corresponding orthogonal direct sum under the displayed
decomposition. This identification uses the actual forward-adjoint
convention G=S composed with Phi_g^(tau/(2pi)); replacing it by its
inverse would be a convention error.

## 5. Strong convergence, adjoints, and weak quasimode escape

Let P_N be the orthogonal projection onto V_N and
Tbar_N=I_N T_N I_N*. These are contractions satisfying

    Tbar_N*Tbar_N=Tbar_N Tbar_N*=P_N,  P_N -> I strongly.

For a fixed trigonometric polynomial f, I_N* f=Op_N(f) for N large.
FM-018 O8 at one step bounds the difference from Op_N(f composed with G)
in operator norm by O_f(N^-2). Operator norm bounds normalized HS norm.
The alias estimate above then gives Tbar_N f -> C_G f. Contractivity
and density extend this to every L2 f.

Strong convergence of bounded operators does not ordinarily imply strong
convergence of adjoints. Here the unitary limit and the projection identity
provide it. Set g=C_G* f. Then exactly

    Tbar_N* f-g
      =Tbar_N*(f-Tbar_N g)+(P_N-I)g,

whose norm tends to zero. Thus the adjoint convergence needed in C4 is
fully justified, without a separate inverse-time Egorov theorem.

The smooth O11 mixing estimate extends to centered L2 by approximation,
with errors uniformly bounded in time using unitarity. It follows that
C_G has no nonzero centered eigenfunction with unit-modulus eigenvalue.
Only this consequence, weaker than the full mixing rate, is needed.

Suppose x_N=I_N X_N are unit centered quasimodes with phases zeta_N
and residual tending to zero. From any subsequence choose a further one
with zeta_N -> zeta and x_N weakly convergent to x. For every fixed f,
strong adjoint convergence and the boundedness of x_N give

    <f,C_G x> = lim <Tbar_N* f,x_N>
              = zeta <f,x>.

Also <1,x>=0. The preceding absence of eigenfunctions forces x=0.
Every subsequence therefore has only the zero weak limit, so x_N is
weakly null. Compactness implies ||Kx_N||+||K*x_N|| ->0; the two norm
limits transfer this to ||D_NX_N||+||D_N*X_N|| ->0.

The sequence argument supplies the required uniformity. If an operator
norm on any shrinking spectral arc failed to tend to zero, choose
successive unit vectors witnessing that failure and their arc centers.
An angular arc of radius epsilon has residual at most epsilon. This
would contradict the quasimode conclusion. Degeneracies, linear
combinations within an arc, and the entire traceless commutant are all
covered. The zero-dimensional centered space at N=1 is irrelevant to
the asymptotic all-odd-N statement; one may explicitly write odd N>=3.

## 6. Uniform shell and spectral proximity

Let L_N(delta)X=lambda X with X unit and centered. For 0<delta<1,
L_N(delta) is a contraction and ||L_N(delta)-T_N||<=2 delta. Applying
these inequalities to this eigenvector gives

    1-2 delta <= |lambda| <=1.

When delta<1/4, zeta=lambda/|lambda| is defined and

    ||(T_N-zeta)X|| <=4 delta.

Therefore along any positive delta_N ->0, all such eigenvectors satisfy
||D_NX||=o(1), uniformly. If uniformity failed, a sequence of failing
eigenvectors would be an already excluded sequence of quasimodes.

The exact eigenvector equation reads

    lambda X=(1-delta)T_N X+delta D_N X.

Triangle and reverse-triangle inequalities give

    ||lambda|-(1-delta)| <=delta ||D_NX||=o(delta).

Normality of (1-delta)T_N on the centered space gives

    dist(lambda,(1-delta)spec(T_N|H_N^0))
      <=||((1-delta)T_N-lambda)X||
      =delta ||D_NX||=o(delta).

Every eigenvalue has at least one eigenvector, even when L_N is defective.
Hence this covers all eigenvalues, including those counted with algebraic
multiplicity for trace purposes. No left-eigenvector conditioning,
diagonalizability, reverse spectral inclusion, or pseudospectral theorem
is hidden in the proof. The adjoint-annihilation part of C1 is stronger
than what C2 and C3 actually need.

## 7. Exact boundary relevance and non-claims

For the centered, entirely untwisted transfer, let r_N be its spectral
radius. The result gives r_N=1-delta_N+o(delta_N), so
1-r_N=delta_N(1+o(1)). An enhanced spectral gap asymptotically larger
than delta_N is impossible for this operator in this regime.

For every integer m>=1 the finite-dimensional eigenvalue trace identity,
not a power-norm bound, yields

    |Tr L_N(delta_N)^m-1|
      <=(N^2-1) exp[-(1-o(1))m delta_N].

Thus at delta_N=A log N/N the leading radial coefficient improves from
the older unspecified kappa to 1. This still leaves the dimension
prefactor. It does not bound ||L_N(delta_N)^m|| by r_N^m, nor does it
bound a noncommuting marked trace by the radius alone.

The actual signed boundary T16 retains occupation twists theta and a
Hamming coefficient extraction through q. This theorem is for q=1 and
theta=0. Neither twist-uniform quasimode annihilation nor the requisite
signed subtraction is proved here. In particular the fixed smooth-symbol
limit of T_N cannot simply be reused for arbitrary N-dependent diagonal
occupation phases. General Hamming twists also need a separate argument.

At the known interior endpoint, o(delta_N)=o(log N/N) does not imply
o(1/N): its unknown coefficient might decrease too slowly. Even the
proved one-sided spectral proximity has no microscopic matching or
signed cancellation content. The nonnormal marked derivative, occupation
projection, high-Hamming mask, and complete time-weighted subtraction
remain outside the new result. No BGS, CUE pair, balanced-complement,
full off-charge, or higher-factorial conclusion is obtained.

## 8. Minimal corrections and obligation matrix

Recommended editorial corrections:

1. In C1's first line, write the normalized HS **squared** norm as
   ||X||_N^2=N^-1 Tr(X*X), or put a square root around the displayed
   expression. The later proof clearly uses the Hilbert-space norm.
2. In C2's negative-charge sentence, replace “unitary-conjugate relation”
   by “permutation-unitary conjugation combined with complex conjugation,”
   or “antiunitary equivalence.” The complete argument is in Section 3.
3. For the excluded twists, the proof establishes “These conclusions are
   not asserted uniformly over arbitrary occupation phases.” The stronger
   wording “do not hold uniformly” is a separate impossibility assertion
   and should not be inferred merely from failure of this proof's smooth
   limit. This audit does not address that excluded-family assertion.
   In C6, “untwisted” should explicitly mean q=1 and theta=0.

Obligations:

- Literal quantizer and fixed nonzero tau: passed, with inherited input scope.
- Exact ordinary midpoint and negative/wrapped labels: passed.
- Integer alias signs: passed; explicitly retained above.
- Normalized-HS versus normalized-l2 identification: passed.
- Step/Fourier compatibility on both sides: passed.
- Negative-charge compact norm limit: passed after the stated wording fix.
- Simultaneous tail cutoff and compact direct sum: passed.
- Full centered D_N and D_N* norm limits: passed.
- Strong quantum and adjoint convergence: passed.
- Actual normalized-area mixing dependency: passed within recorded scope.
- Weak quasimode escape and spectral-arc uniformity: passed.
- Every shrinking delta sequence, every eigenvalue: passed.
- Algebraic multiplicity and possible nonnormality: passed.
- Radius-to-power-norm inference: not used.
- Arbitrary occupation/Hamming twists: outside the theorem.
- Boundary trace subtraction and microscopic statistics: not proved.

## 9. Evidence, remaining gap, and cheapest next check

The new theorem is established analytically from the pinned inputs.
No numerical experiment at a visible surrogate tau was used. Source
hash verification and exact formula reconstruction support provenance
and conventions; they do not certify the inherited asymptotic analytic
theorems independently. A bounded search of canonical mathematics and
records for collective compactness, quasimode annihilation, radial
shell, and charge compactness found no already stated identical theorem.
This is not an external originality claim.

No substantive new implication remains missing for C1–C3. The exact
remaining research gap is still the original signed marked-switch
boundary estimate with its occupation and Hamming masks. The cheapest
useful next step for this candidate is to make the three local wording
clarifications above and preserve the fully untwisted scope when citing
the improved radial coefficient. Re-proving the interior gap or treating
the new radius as a power-norm estimate would not advance that boundary.
