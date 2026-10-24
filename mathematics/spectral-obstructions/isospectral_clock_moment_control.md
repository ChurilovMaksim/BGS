# All-order moment-channel control with a rigid clock spectrum

**Stable claim ID:** BGS-TRACE-014.
**Status:** self-contained project derivation, independently audited internally.
This is an obstruction to an insufficient universality criterion, not a
counterexample to the frozen-map BGS conjecture. No global priority is claimed.

## 1. Objects, norms, and theorem

For an integer N>=3, put ζ=exp(2πi/N) and
D_N=diag(1,ζ,...,ζ^(N-1)). Let Q be Haar distributed on U(N), let Θ be
independent and uniform on [0,2π), and set V_N=exp(iΘ)QD_NQ*.
For each integer k>=1 define operators on End((C^N)^⊗k) by

    M_(N,k)(X)=E[V_N^⊗k X (V_N*)^⊗k],
    P_(N,k)(X)=∫_(U(N)) U^⊗k X (U*)^⊗k dU.

Give this matrix space its Hilbert–Schmidt inner product; either ordinary
or dimension-normalized trace gives the same induced operator norm.
Throughout, 2→2 denotes this induced norm, not the Hilbert–Schmidt norm
of the superoperator itself.

**Theorem (clock moment-channel obstruction).**

1. For every N>=3 and every k>=1, including k depending arbitrarily on N,

       ||M_(N,k)-P_(N,k)||_(2→2) <= 1/N.                 (C1)

2. At k=2, the exact error is

       ||M_(N,2)-P_(N,2)||_(2→2) = 1/(N²-1).          (C2)

   The full channel spectrum, with total eigenspace dimensions, is

       1:                                      2,
       -1/(N²-1):                              4(N²-1),
       0:                                      N²(N²-3)/2,
       4/((N²-1)(N²-4)):                       (N²-1)(N²-4)/2.     (C3)

3. Every realization has exactly equally spaced eigenangles. After unfolding
   to mean spacing one, every consecutive circular gap equals one. An interval
   of integer unfolded length 0<L<N contains exactly L points when taken
   half-open. In particular its number variance is zero. This ensemble does
   not have the Sine₂ local spectral limit.

Thus convergence to Haar of all balanced moment channels, uniformly over
order in this 2→2 norm at the rate (C1), does not by itself imply microscopic
spectral universality. A quantitative passage to the actual spectral tests
must retain their dimension- and order-dependent extraction norms.

## 2. Conjugacy averaging and the root-of-unity character bound

Vectorization identifies M_(N,k) with E R_k(V_N), where
R_k(U)=U^⊗k⊗conjugate(U)^⊗k. This is a finite-dimensional unitary
representation. Its central U(1) action is trivial, so the independent phase
Θ cancels exactly. Decompose it orthogonally as

    R_k ≅ ⊕_λ (π_λ ⊗ I_(m_λ)).

Schur's lemma and invariance of Haar measure give

    ∫ π_λ(Q)π_λ(D_N)π_λ(Q)* dQ
        = [χ_λ(D_N)/d_λ] I_(d_λ).                     (C4)

Indeed the integral commutes with every π_λ(U), and its trace is χ_λ(D_N).
It acts as the identity on each multiplicity factor. Haar averaging of R_k
itself is the orthogonal projection onto its trivial summands. Consequently

    ||M_(N,k)-P_(N,k)||_(2→2)
        = max_(λ nontrivial occurring in R_k) |χ_λ(D_N)|/d_λ.    (C5)

Here an empty maximum is zero.

For an integral highest weight λ_1>=...>=λ_N of U(N), the Weyl character
formula is the quotient of the alternants with exponents λ_j+N-j and N-j.
Evaluate both alternants at 1,ζ,...,ζ^(N-1). Their entries depend only on
exponents modulo N. Repeated numerator residues give two equal rows and
hence zero. Otherwise the numerator rows permute the denominator rows.
The denominator is a nonzero Vandermonde determinant. Therefore

    χ_λ(D_N) ∈ {0,+1,-1}.                              (C6)

The argument allows negative highest-weight coordinates. It needs no
primality, oddness, bounded weight, or restriction on k.

Every summand of R_k has sum_j λ_j=0, by its trivial central action. An
irreducible representation trivial on SU(N) is a determinant power; balance
forces that power to be zero. Each nontrivial summand therefore induces a
nonzero Lie algebra homomorphism su(N)→u(d_λ). Simplicity of su(N) makes it
injective. Comparing real dimensions yields N²-1<=d_λ², and the integer d_λ
must satisfy d_λ>=N. Equations (C5) and (C6) prove (C1).

This elementary type-A calculation is the root-of-unity mechanism behind
classical Coxeter-element character rigidity. It does not assert a new
character theorem.

## 3. Exact two-copy decomposition, including N=3

Write W=C^N, S=Sym²W, and A=Λ²W. Since W⊗W=S⊕A, its endomorphisms split
into End(S), End(A), Hom(A,S), and Hom(S,A). Let Ad_0 denote the traceless
adjoint representation, of dimension N²-1. The decompositions are

    End(S)    = 1 ⊕ Ad_0 ⊕ R_s,
    End(A)    = 1 ⊕ Ad_0 ⊕ R_a,        N>=4,
    End(A)    = 1 ⊕ Ad_0,              N=3,
    Hom(A,S)  = Ad_0 ⊕ R_c,
    Hom(S,A)  = Ad_0 ⊕ R_c*.

For clarity, the needed decomposition follows from explicit constituent
embeddings and dimensions, rather than an unstated large-N rule. The two
identity operators provide the trivial summands. The action H⊗I+I⊗H of a
traceless H provides a nonzero adjoint copy on S and on A. The operator
H⊗I-I⊗H switches S and A, providing a nonzero adjoint copy in each cross
block. These equivariant nonzero maps are injective because Ad_0 is
irreducible. Orthogonal complements exist because the representations are
unitary.

Residual highest-weight vectors are respectively

    e_1² ⊗ (e_N*)²,
    (e_1∧e_2) ⊗ (e_(N-1)*∧e_N*),
    e_1² ⊗ (e_(N-1)*∧e_N*),
    (e_1∧e_2) ⊗ (e_N*)².

The second is used only for N>=4. Each displayed vector is killed by the
positive-root raising operators. Their respective highest weights are

    R_s:  (2,0,...,0,-2),
    R_a:  (1,1,0,...,0,-1,-1),
    R_c:  (2,0,...,0,-1,-1),
    R_c*: (1,1,0,...,0,-2).

The last representation is the contragredient of R_c; its displayed vector
is a highest-weight vector, not the literal dual of R_c's highest-weight
vector (which would have lowest weight).

These weights differ from the trivial and adjoint weights. The Weyl dimension
formula d_λ=∏_(i<j)(λ_i-λ_j+j-i)/(j-i) gives

    d_s=N²(N-1)(N+3)/4,
    d_a=N²(N+1)(N-3)/4,
    d_c=(N²-1)(N²-4)/4.                              (C7)

For N=3 set d_a=0 and omit R_a. Adding the displayed constituent dimensions
gives dim End(S), dim End(A), and dim Hom(A,S), respectively, so no missing
summands remain. This also handles the exceptional smallest dimension.

At D_N, both Tr D_N and Tr D_N² vanish for N>=3. Hence
χ_S(D_N)=((Tr D_N)²+Tr D_N²)/2=0 and
χ_A(D_N)=((Tr D_N)²-Tr D_N²)/2=0. Meanwhile
χ_(Ad_0)(D_N)=|Tr D_N|²-1=-1.
Subtracting these constituent characters from the four block characters
now gives χ_(R_s)=χ_(R_a)=0 and χ_(R_c)=χ_(R_c*)=1 at D_N.
Equation (C4) proves (C3): the zero multiplicity is d_s+d_a, and the final
multiplicity is 2d_c. The four multiplicities sum to N^4.

The two invariant vectors are the identity and physical swap, since they
span the scalar operators on S and A. Removing their Haar projection leaves
the absolute eigenvalues 1/(N²-1), 0, and 4/((N²-1)(N²-4)). Since N²-4>=5,
the first is the maximum. This proves (C2).

## 4. Spectral obstruction and precise scope

Conjugation leaves D_N's spectrum unchanged and Θ rotates it. The unfolded
point configuration is Z+η modulo circumference N, where η is uniform
modulo one. This proves all gap and counting assertions directly. Its local
limit is the uniformly translated integer lattice. By contrast, the Sine₂
kernel K(x,y)=sin(π(x-y))/(π(x-y)) has interval count variance
∫_I∫_(R\I)|K(x,y)|² dy dx>0 for every nonempty finite interval I; the
integrand is nonzero on a set of positive measure. Therefore the two local
laws differ.

The Heisenberg-order trace gives another exact separation:

    N^-2 E|Tr V_N^N|² = 1,
    N^-2 E_Haar|Tr U^N|² = 1/N.                       (C8)

For completeness, the Haar identity follows by expanding the power sum
p_N into hook Schur characters: p_N=∑_(j=0)^(N-1)(-1)^j s_(N-j,1^j).
There are exactly N allowed hooks in N variables; character orthogonality
gives squared Haar L² norm N. Equation (C8) concerns a degree-(N,N) scalar
functional of the Nth balanced moment representation. Small 2→2 operator
error does not bound this functional without its dual extraction norm.
The lattice-count obstruction already proves the theorem independently
of this supplementary trace identity.

**Exclusions.** This is not a diamond-norm approximation, a superoperator
Hilbert–Schmidt approximation, or a spectral-distribution metric bound.
It is not an exact unitary design. No Egorov property, specified classical
map, fixed physical Hamiltonian, frozen coupling, or symmetry-reduced
sector is claimed. It does not refute a theorem that includes these extra
hypotheses and proves the required quantitative spectral extraction.
It does not identify powers of a quenched random matrix with independently
resampled channel powers. It leaves TRACE-005 and deterministic BGS open.

**Relation to existing controls.** TRACE-013 has a bad-spectrum arithmetic
word and a separately enlarged good auxiliary channel. Here the moments
belong to the same ensemble whose every matrix has a clock spectrum,
and the estimate covers every k. The isospectral family in
frozen_spectral_flow_controls.md is another earlier clock control; it does
not state this all-order conjugacy-twirl estimate. These are complementary
obstructions, not retractions of those results.

## 5. Evidence and attribution boundary

The accompanying portable verifier checks bounded highest weights using
integer arithmetic in cyclotomic quotient rings and checks Weyl dimensions
and multiplicity identities at explicitly reported finite N. It does not
construct the complete channel, numerically integrate Haar measure, or prove
the universal theorem by enumeration. Its checks remain enabled under -O.
The universal argument is Sections 2–4 above, using standard finite-dimensional
unitary representation theory, the Weyl character/dimension formulas, and
explicit tensor calculations.

See [the source note](../../literature/isospectral_clock_sources_20261006.md) for prior character rigidity and isospectral twirling.
The report that motivated this audit supplied additional computation counts;
those attachments were unavailable and those counts are not this project's
executed evidence. Neither global novelty nor formal proof-assistant
certification is asserted.
