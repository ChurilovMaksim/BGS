# Source-bound accepted review: first_old_layer_classification.md

This is the historical independent internal review, with its original scope
and verdict. Its frozen SHA256 is `f6942b135d0429f9212fb7c2a54a90e0093dd4bc038e31272da5c332a4d9746d`.
The [maintained proof](../mathematics/first_old_layer_classification.md) makes only the status, navigation,
and disclosed nonblocking exposition changes recorded in the promotion map.
Original outside paths and commands in the report identify historical
artifacts; their exact bytes are recoverable through the
[archive map](../evidence/intermediate_old_layers_20261007/input_map.json).
The [portable replay](../computations/verification/intermediate_old_layers_certificates.py)
replaces historical execution paths and retains all arithmetic checks under
Python optimization. This is independent internal review, not external peer
review or formal certification.

# Independent audit: even first-old-layer classification

## Verdict and frozen target

**ACCEPT: proved as written within the explicitly inherited, accepted cat/oldform inputs.** The new conclusions concern actual first-order Hermitian compression on complete cat eigenspaces in the even first-old quotient, and no larger operator or statistical statement.

Frozen proof:

- `/workspace/shared/bgs_intermediate_old_layer_classification/first_old_layer_classification.md`
- SHA256 `3711869ecb05efda76066216ce29b84263ec12edca9c379e2ede9d16c5f21b41`
- `provenance_manifest.json` SHA256 `8089ece36cd2151f992ef1629e5ff04f3e0d1279d4e1f36911f3f890e52f1000`

All thirteen source/output hashes declared by that manifest were checked and match. The canonical repository was read only. This review neither imports the candidate's Python modules nor treats its previous diagnostics or verdict as proof. The two new exact checks below use different matrix and polynomial representations; comparison with supplied JSON occurs only after independent construction.

### Claim card

For every integer l>=1, N=7*5^(2l+2), h=5^l, m=h^2 and L=6h/5, identify W1 orthogonal to W2 with H7 tensor the primitive coherent sector of H_m. Every product-cat eigenspace there is complete and has dimension seven. For each unit c modulo h, its L block labels belong to the oriented norm circle Q(a,b)=2b^2-a^2=c.

- c=1 modulo 5: all L blocks are exactly zero.
- c=2 or 4 modulo 5: all L blocks are simple, rank six. These give exactly 12*5^(2l-2) blocks, half the quotient dimension.
- c=3 modulo 5: each block is exactly zero or simple of rank six; the given exact root-of-unity coefficient test decides the alternative at every depth and label.
- At l=1 the singular six blocks are simple; at l=2 the only intersecting singular circle is c=13, with exactly six zero blocks and 24 simple blocks.

This is an all-depth algebraic classification by a finite integer algorithm, not an all-depth elementary digit formula for the singular zero set.

## Dependency graph and scope

1. Canonical `oldform_tower_compression.md` (SHA256 `506064db5360f204360f54cb8598e61d5db50d9fa3d0589dc8fc289271a6eeb1`): exact CRT operator, J_j intertwining and Weyl compression, full-eigenspace isolation.
2. Canonical `even_new_sector_first_jet.md` (SHA256 `ba95e0bfd9a4a3a8445339b9c8a47de11c1eb8f41b4905f062ebd81aa1ccb72a`): primitive coherent basis, norm-circle transitivity, simple prime-power cat, exact L denominator.
3. These inputs yield complete size-seven blocks for the *actual* two-mode operator. The root equation gives the intersection classification. The fixed characteristic-five matrices prove simplicity on regular residue classes. The singular exact phase factorization gives a scalar sine matrix, and cyclotomic divisibility decides its scalar.

These are explicitly inherited accepted project inputs. Their relevant raw statements were inspected, including the raw kernel, seven normalization, uniform cat multiplicity and parity arguments. This is not a fresh end-to-end external audit of every transitive theorem in the repository. No new external theorem or unverifiable literature input is needed for the extension.

## Reconstruction and proof obligations

### 1. Actual operator and full eigenspaces: passed

For n=5^(2l+2), J1* T_n(a,b) J1 vanishes unless both a,b are divisible by five; when they are, it is T_m(a/5,b/5). The actual symbol therefore retains precisely the coefficients -i/800 and +i/800 of (0,5) and (0,-5). The seven factor retains frequencies (0,5) and (0,-5), without dividing those frequencies or discarding a midpoint phase. Thus the actual compressed operator is

    (1/800)[-i T7(0,5) tensor T_m(0,1)
             +i T7(0,-5) tensor T_m(0,-1)].

The primitive coherent sector has dimension m-m/25=24*5^(2l-2). Its eigenvalues are closed under multiplication by cube roots on each L-cycle. Prime-power simplicity and the inherited old/new isolation ensure these are complete product-cat eigenspaces of dimension 3+2+2, not pieces of a larger eigenspace. All L oriented labels are retained; there is no quotient by parity or signed orbits.

### 2. Intersections and their counts: passed

Q(a,b+1)-Q(a,b)=4b+2, so b=-1/2 and a^2=1/2-c modulo h. This directly gives the empty c=1 class and the two unique Hensel lifts for c=2,4. For singular D, nonzero solvable D has even valuation 2s and square unit part; its root count is 2*5^s. D=0 has 5^floor(l/2) roots. Counting the possible D of each valuation gives exactly

    1 + 2 sum_(s=1)^floor((l-1)/2) 5^(l-2s-1)

nonempty singular circles. At l>=2 their root counts are divisible by five and all roots reduce to the same point modulo five. This proves the two residue depth regimes without extrapolating a finite run.

### 3. Exact coordinate phases and L denominator: passed

Using the raw kernel q^[-(3x^2-2xy+3y^2)/8]/sqrt(m), one can reconstruct phases without the candidate's carry routine. For v=(a,b), w=(A,B)=Sv modulo h in canonical representatives, evaluate M phi_v at x=-A. Summing the h support points imposes x=-A modulo h, and the phase relative to phi_w is

    e(v) = -(3A^2-2Aa+3a^2)/8 - ab/2 + AB/2 modulo m.

It is divisible by h and equals the stated Weyl-carry expression. Likewise the direct coordinate phase of T(0,1) from (a,b) to (a,B), B=b+1 modulo h, is

    -a + a(B-b)/2 modulo m,

which equals the stated -a/2 plus carry. These are the phases used in the new cancellation implementation.

An L-cycle eigenvector has coefficients lambda^(-k) q^(E_k)/sqrt(L); its dual has the conjugate phase and the same sqrt(L). Every compression entry therefore has exact denominator L. Multiplication by 800L, including its five-adic valuation, is valid. Replacing this by a projector denominator would not be justified, but the candidate does not do so.

### 4. Regular-class residue certificate: passed independently

The new `replay_position_residues.py` constructs the seven cat directly in the position basis, with raw kernel

    G_xy = w^[-8^(-1)(3x^2-2xy+3y^2)] modulo seven,
    H=G/Tr(G).

It does not compute or import an eigenbasis. For each directed intersection, its contribution in that position basis is

    (-2*sign) xi^[t(kx-ky)] H^(-kx) T7(0,5*sign) H^(ky).

This is conjugate to the claimed eigenbasis entry formula because H's eigenvalues are the z_i. Spectral projectors directly verify the multiplicities 3,2,2. Field multiplication uses cyclic convolution modulo X^7-1 followed by elimination of X^6 with Phi_7; characteristic polynomials use eight determinant samples and a Vandermonde solve, unlike the candidate's subset determinant.

All six primitive seventh roots were enumerated, not only inferred by conjugation. The result is 288 exact matrices: 180 squarefree/rank-six and 108 zero. For w at the candidate's root, all 48 records, coefficients, ranks and gcd degrees match exactly. The three c=2,4 polynomials are precisely the three printed degree-seven polynomials. The shallow c=3 polynomial is X^7+3X^5+4X^3+3X. The integral seven eigenbasis can be chosen with local unit determinant because the three cubic eigenvalues are distinct modulo five. Hence squarefree residue proves nonzero characteristic-zero discriminant after scaling.

Simultaneous parity preserves each complete cat block and anticommutes with the actual two-mode generator. Its Hermitian spectrum is symmetric. A simple seven-dimensional block thus has exactly one zero eigenvalue, proving rank six.

### 5. Singular scalar-conjugacy: passed

Every singular intersection has y reducing to the same point modulo five, with x=-y there. Since the six-point orbit has S^3=-I, ky and kx have the same fixed residue r modulo three. For lambda_i=lambda/z_i, their exact coefficients factor as

    lambda_i^kx lambda_j^(-ky)
      = z_i^(-r) z_j^r lambda^(kx-ky),

including every higher-order phase. This is exact over characteristic zero, not only after residue reduction.

The order of S modulo m is R=6*5^(2l-1), with S^(R/2)=-I. This last assertion also follows by raising S^3=-I modulo five through the odd five-power lift. Exact covariance and Weyl irreducibility give M^(R/2)=kappa P. Since R/2 is divisible by three, replacing lambda by lambda/z_i leaves the parity eigenvalue unchanged. Therefore the T(0,1) and T(0,-1) matrix elements between the paired states agree. On the diagonal their being adjoints makes the common scalar G real.

The full block is thus exactly G/(800L) times a diagonal conjugate of -i T7(0,5)+i T7(0,-5). Its seven sine eigenvalues are distinct for every primitive seventh root, and exactly one is zero. This proves the zero-or-simple/rank-six dichotomy uniformly, without any Gauss-sum nonvanishing assumption.

### 6. All-depth cyclotomic test and label coverage: passed

The cycle condition is lambda^L=q^E_L, with E_L divisible by h. For zeta of order 6m, q=zeta^6, the proposed alpha_j=5E_L/h+5hj obeys alpha_j L=6E_L modulo 6m and has exactly L distinct values as j ranges from 0 to L-1. Thus no tame or wild character is omitted.

All intersection differences d_a have the same residue modulo six. Subtracting one complete exponent from all exponents therefore leaves a multiple of six. After removing this nonzero root-of-unity factor, G is an integer-coefficient polynomial in the primitive m-th root q. A polynomial of degree less than m vanishes at q precisely when it is divisible by Phi_m. Since Phi_m=1+X^(m/5)+...+X^(4m/5), divisibility is exactly equality of the five coefficient multiplicities in each residue class modulo m/5. Empty root sets are already declared zero before this choice of a term.

Changing j adds 5h(d_a-d_0)/6 to the relative q exponents. The printed lcm formula is consequently a valid zero-test period, and that period divides L. This is a reduction of all labels, not a sampling argument. The independent replay did not use this period and checked every label explicitly through l=5.

## Independent exact cancellation replay

`replay_coordinate_cancellation.py` uses the coordinate phases above and an intersection point as orbit base. Instead of factoring a sixth-root prefactor and applying the candidate's five-bin balance test, it reduces the full zeta-polynomial directly by

    Phi_(6m)(X)=Phi_30(X^(m/5)),
    Phi_30(X)=X^8+X^7-X^5-X^4-X^3+X+1.

This gives an independent sparse exact-integer calculation. It visits every singular c and every one of its L labels at l=1,...,5, without a period shortcut. All source zero label sets and counts match. Nonempty-circle zero/simple counts are respectively

    l=1: 0 / 6
    l=2: 6 / 24
    l=3: 120 / 330
    l=4: 300 / 7950
    l=5: 3150 / 195600.

At l=2 it independently reproduces E_L=450, the five (f,d) pairs printed in the note, all five signed beta expressions, and exactly j=3 modulo five as the six zero labels. The equivalent t=93 modulo 125 condition follows from t=18+25j when lambda=(zeta^5)^t. Thus the whole first-old quotient has 276 zero and 324 simple size-seven blocks at that depth; W2 separately has dimension 175 and zero compression.

## Reproduction and residual scope

Run from any working directory:

    python3 /workspace/shared/bgs_intermediate_first_layer_review/replay_position_residues.py
    python3 /workspace/shared/bgs_intermediate_first_layer_review/replay_coordinate_cancellation.py

The review manifest records actual commands, software, input hashes before and after execution, outputs and logs. No numerical arithmetic or tolerance is used in either certificate.

No mathematical correction was found. The finite computations do not prove the all-depth theorem by themselves: the all-depth reduction, scalar factorization, root-count argument and cyclotomic divisibility above do that work. The observed restriction of cancellation zeros to D=0 through depth five remains only a bounded observation, as the candidate correctly states. Full U simplicity, fixed-coupling noncollision, effective higher eigenjets, global commutants and BGS universality are outside this review and receive no new conclusion.
