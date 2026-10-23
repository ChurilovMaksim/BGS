# Intermediate-old-layer rotated returns: exact operator and obstruction

Claim family: BGS-FM-026. Source-bound [independent review](../archive/record/intermediate_return_review.md).
The frozen original SHA256 is `3f42c4f41f448c221e4dc92495a11caa3b2cd661168f8cd888abd35971ed1932`;
its exact bytes, original status and execution records remain in the
[provenance map](../evidence/intermediate_old_layers_20261007/input_map.json).
Inherited [oldform](oldform_tower_compression.md),
[newest-sector](even_new_sector_first_jet.md), and
[rank-transfer](algebraic_time_rank_transfer.md) proofs retain their own scopes.
The [literal-time theorem owner](literal_time_multiplicity_bounds.md) is the
only maintained owner of the resulting fixed-time simple-eigenvalue counts.

The portable maintained command is
`python3 computations/verification/intermediate_old_layers_certificates.py`
(or the same command with `python3 -O`). Original bare script names below
identify archived historical implementations; the portable entry replays the
independent reviewers' algorithms in scratch storage and verifies their
outputs against the frozen reviewed results.

Status: independently reviewed structural proof. The finite controls are supplementary; they do not prove a uniform simplicity theorem.

## Claim, conventions, and dependencies

Let n=5^e=h²m, h=5^j, m=5^s, s=e−2j≥0, j≥1. Write J=J_j:H_m→H_n for the accepted oldform embedding. Let M_n be the prescribed normalized quadratic cat, with induced primitive root q of order n, S=[[3,4],[2,3]], and raw Weyl convention

    T(v)T(w)=q^(ω(v,w)/2)T(v+w),
    M T(v) M^(-1)=T(Sv),  ω((a,b),(c,d))=ad−bc.

Every half in an exponent is the inverse of 2 at the relevant odd modulus. Put Q(a,b)=2b²−a². The residual Weyl root is q_m=q^(h²). The full product cat is M_7⊗M_n, and W_j=H_7⊗J H_m is a sum of complete eigenspaces.

Inputs are the accepted oldform intertwining and compression, the simple prime-power cat spectrum, the exact order/valuation of S, and the even coherent basis. Their source hashes are in the manifest. This note derives the return operator and its sums; it does not re-audit those inputs.

For the actual normalized five-primary cats, M_(5^s)^(6·5^(s−1))=I for s≥1. Phase safety follows from scalar return and restriction, through the old embedding, to M_1=1 at even depth or to the accepted M_5^6=I at odd depth. No phase convention for M_7 is imposed.

Success criterion: an exact residual operator formula retaining the cat character, a correct resonant geometric sum, and a proved failure of the scalar-residue shortcut. Bounded squarefreeness is not the criterion for a uniform theorem.

## 1. Primitive return operator

Put L=6·5^(j−1), R=6·5^(e−1), and D=R/L=hm. For primitive u, S^L u≡u mod h. Set

    b_u=(S^L−I)u/h mod m,
    z_u=q^(−ω(u,S^L u)/2),
    B_u=z_u T_m(b_u) M_m^L.

Then the exact identity is

    M_n^L T_n(u)J=T_n(u)J B_u.                    (1)

Proof: apply covariance, write S^L u=u+h b_u, use the inverse Weyl cocycle, and use T_n(hb)J=JT_m(b) and M_nJ=JM_m. The divided integer lift of b_u is primitive because (S^L−I)/h is invertible modulo 5. For m>1 its residual reduction is primitive; for m=1 the residual translation is trivial.

If λ=αμ is a full product-cat eigenvalue in W_j, α is an M_7 eigenvalue and μ an occupied M_m eigenvalue. Since 3 divides L and M_7 has cubic eigenvalue ratios, α^L is independent of the chosen factorization of λ. Therefore the normalized return operator is

    X_u=ρ B_u,     ρ=α^L/λ^L=μ^(−L).             (2)

The same ρ works for all three cubic-related residual eigenvalues contributing to λ. Its order divides

    5^max(s−j,0)=5^max(e−3j,0).                  (3)

Thus when e≤3j the residual cat M_m^L is I and ρ=1. T_m(b_u) still remains and is non-scalar for m>1. When e>3j, the wild character ρ and the nontrivial residual cat must both be retained. The first instance is j=1, m=25, where L=6 and M_25^6 is non-scalar.

## 2. No eigenvalue 1 for primitive returns

Iteration of (1), or direct covariance, gives

    B_u^t=z_(u,t) T_m((S^(Lt)−I)u/h) M_m^(Lt),
    z_(u,t)=q^(−ω(u,S^(Lt)u)/2).                  (4)

For t=m the translation is identity modulo m, M_m^(Lm)=I, and ρ^m=1. Hence

    X_u^m=z_m I,
    z_m=q^(−ω(u,S^(Lm)u)/2).                     (5)

Write S^(Lm)=[[a,2c],[c,a]]. Exact five-adic order gives v_5(c)=j+s. Since ω(u,S^(Lm)u)=−cQ(u) and Q(u) is a unit, z_m has exact order 5^j=h. Consequently X_u^D=I, every eigenvalue of X_u has exact order D=5^(j+s), and 1 is absent. This is a uniform statement, not a finite-prime observation.

## 3. Initial factors and the exact weighted class sum

For primitive v,u, the return condition v+S^k u∈h Z² is equivalent to Q(v)=Q(u) mod h. If it holds, k lies in one class a mod L, 0≤a<L. Define

    c_a=(v+S^a u)/h mod m,
    θ_a=q^(ω(v,S^a u)/2),
    D_a=θ_a T_m(c_a),
    C_(7,a)=T_7(v)T_7(S^a u),
    X_(u,a)=M_m^a X_u M_m^(−a).

Let P_λ denote the spectral projector in the reduced space H_7⊗H_m. After moving the final cat power onto P_λ, the contribution at k=a+Lt is exactly

    P_λ [C_(7,a)⊗D_a X_(u,a)^t] P_λ.            (6)

The seven-factor Weyl cocycle is inside C_(7,a), not discarded. The factor θ_a is retained exactly. Conjugation by M_m^a is necessary; no unstated commutation with D_a is used.

For any X with X^D=I over characteristic zero, put

    Π=(1/D)∑_(t=0)^(D−1)X^t,
    (I−X)^#=(I−X+Π)^(-1)−Π.

A direct finite geometric calculation gives

    ∑_(t=0)^(D−1)(R−2a−2Lt)X^t
      =2R(I−X)^# + D(L−2a)Π,   R=LD.            (7)

On eigenvalue 1 the left side is D(L−2a); on every other eigenvalue it is 2R/(1−x). This proves both terms and fixes their signs. If a=0, subtract R I inside (7), because the resolvent polynomial runs over 1≤k<R. After multiplying by the initial factors, the subtraction is −R C_(7,0)⊗D_0, not an unconditional identity operator.

For primitive returns Π=0 by (5), so the weighted class equals 2R D_a(I−X_(u,a))^(-1), with the stated initial seven factor and k=0 correction. Its contribution to the second-order matrix also carries i d_v d_u/(2R·4000²).

## 4. The two nonprimitive actual modes

The only nonprimitive modes are u=(0,±5).

For j≥2 use L'=6·5^(j−2), rather than L. The same formulas hold with L', D'=R/L', and ρ'=μ^(−L'). Now X'^m=z'_m I with z'_m of exact order 5^(j−1). Thus Π=0 here as well. Each eigenvalue of X' has exact order 5^(j+s−1); D'=5^(j+s+1) is a possibly nonminimal return length, which does not change (7).

For j=1 these modes lie inside W_1: if u=5u', then T_n(u)J=JT_m(u'). All k return. One convenient partition is six classes a=0,...,5 with L_0=6, so the seven-factor operator is fixed along each class. The exact return operator is

    B_u=T_m(u')^(-1) M_m^6 T_m(u'),
    X_u=μ^(−6)B_u.                                (8)

This is resonant: X_u has eigenvalue 1, because μ is an occupied residual eigenvalue. Its 1-projector is the conjugate of the projector onto all residual eigenvalues ν with ν^6=μ^6. Therefore (7), including D(L_0−2a)Π, is required. At m=25 its rank is 1 for the unique tame old character and 6 for each of the four nontrivial wild labels. Omitting Π is false already in this smallest intermediate case.

Mixed primitive/nonprimitive pairs never return for j≥1.

## 5. Even residuals: exact affine-cycle obstruction

Suppose m=H², H=5^ℓ≥5. Use the accepted coherent basis φ_y=T_m(y)ψ_m, y∈(Z/H)². All cat and Weyl matrices in this basis are monomial with phases of five-power order. Consequently X_u reduces modulo the chosen prime over 5 to the permutation

    F(y)=S^L y+b_u mod H.                         (9)

The character ρ also reduces to 1. For every positive integer t,

    F^t(y)−y=((S^(Lt)−I)/h)(hy+u) mod H.          (10)

The matrix (S^(Lt)−I)/h has valuation v_5(t) times an invertible matrix modulo 5, and hy+u is primitive. Therefore the lifted vector in (10) has exact valuation v_5(t); reduction modulo H retains this valuation only truncated at the exponent of H. Every affine cycle has length exactly H.

It follows immediately that the integral numerator

    (1−z_m)(I−X_u)^(-1)=∑_(t=0)^(m−1)X_u^t       (11)

has identically zero residue: its reduction is H times the orbit-sum on each H-cycle. This refutes a nonzero scalar residue for that numerator at every even intermediate residual depth.

There is a sharper entrywise valuation statement. On a coherent cycle O, let η_O be the exact monomial holonomy, so X_u^H=η_O on that cycle. Equation (5) implies η_O^H=z_m. Every η_O therefore has exact order hH=5^(j+ℓ), and

    (I−X_u)^(-1)|_O
       =(1−η_O)^(-1)∑_(t=0)^(H−1)X_u^t|_O.     (12)

The H powers have disjoint permutation supports within a cycle. Every nonzero matrix entry of (12) has valuation

    −a*,   a*=1/(4·5^(j+ℓ−1)).                   (13)

In contrast, the naive scalar-return normalization δ_j=1−q^h has valuation a_j=1/(4·5^(j+2ℓ−1)), and a*=H a_j. Thus every nonzero entry of δ_j(I−X_u)^(-1) has negative valuation (1−H)a_j in this inherited coherent lattice. It has no entrywise scalar residue there. This does not claim that no other lattice or cancellation after summing pairs can work.

The correct entrywise scale is δ*=1−q^(hH), of valuation a*. At that scale the primitive return has an affine orbit-sum residue, not I.

For completeness, the holonomy leading coefficient is independent of the coherent cycle. Under the global coherent realization, the label is x=u+hy mod hH, and its holonomy before character normalization is

    q^(−ω(x,S^(LH)x)/2).

Here the off-diagonal coefficient of S^(LH), divided by hH, reduces to 2. Dividing the exponent by hH gives Q(u) modulo 5. The character factor μ^(−LH) has order at most 5^max(ℓ−j,0), strictly below hH; it does not change that leading coefficient. Hence

    δ*(I−X_u)^(-1) mod 5
       =Q(u)^(-1)∑_(t=0)^(H−1)P_F^t.           (14)

The corresponding expression with the initial factor is the reduction of D_a times the conjugated affine orbit-sum. Formula (14) is an operator statement on the coherent lattice before cat-character compression.

## 6. Finite controls and exact scope

Run:

    python intermediate_return_control.py

The script uses the unchanged actual 32-mode coefficients, raw CRT roots and modular midpoint phases. It never forms an N×N matrix; the largest matrix is 175×175. It computes the entire reduced rotated-return sum and compresses it onto all 27 full product-cat blocks in W_j. All arithmetic is exact over the stated prime field, with int64 product bounds below 2^63 in the executed cases.

- (e,j,m)=(4,1,25), N=4375, prime 420001: 33 upper/upper return pairs; M_25^6 non-scalar; nine first-order reductions are zero (three dimensions 3,2,2 and six dimension 7); all 27 second-order reductions are squarefree.
- (e,j,m)=(6,2,25), N=109375, prime 2625001: 17 upper/upper return pairs; M_25^30=I; all 27 first-order blocks vanish by the exact oldform rule; all 27 second-order reductions are squarefree.

For three primitive sample modes and every one of the 25 residual eigenvalues, the code verifies X^m=z_m I, no eigenvalue 1, the full degree-25 characteristic polynomial t^25−z_m, the exact geometric identity, and failure of the scalar inverse shortcut. It also verifies the full resonant geometric identity for (0,5). These are finite controls; the uniform identities above have separate proofs.

A zero first-order reduction at j=1 is not by itself characteristic-zero vanishing. Squarefree second-order reductions are bounded algebraic evidence at these N only. They are not extrapolation to all e,j, nor a fixed-coupling U-simplicity assertion.

## 7. Remaining reduction and stopping boundary

The next precise object is the actual cat-character compression of the affine orbit-sum in (14), with D_a, the seven-factor cocycle, actual coefficients, and residual orbit-length denominators all retained. For j≥2 only the 17 equal-integer-norm upper pairs survive the Gaussian leading coefficient filter at the entrywise scale; for j=1 there are 33 upper pairs and an additional resonant branch.

At H=5, the affine cycle direction is Jv, J=[[0,2],[1,0]], and the initial coset offset is determined by (Q(v)−Q(u))/h modulo 5. For j≥2 the offset is zero because the 17 surviving upper pairs have equal integer norms. For j=1 the cross-norm pairs have nonzero offsets that must remain in the dictionary.

At larger H, norm-circle support may lead to identity/reflection structure, but this has not been proved here. In particular one may not reduce a sum modulo 5 before accounting for division by the residual cat-cycle length. The wild character parameter ρ and those denominators are the remaining obstruction to promoting the deepest fixed residue certificate to all intermediate layers.
