# Odd-depth newest-sector first-order splitting

Status: independently accepted within the stated newest-sector scope. The independent review is `record/odd_newest_sector_review.md`. This maintained copy changes the historical candidate-status paragraph and the final conditional scope paragraph only; the exact submitted source and its original metadata remain in lossless provenance envelopes under `evidence/odd_newest_20261007/`.

Acceptance is relative to the expressly inherited raw-model, oldform, cat-simplicity, seven-factor and algebraic-time rank-transfer inputs. The original source SHA-256 is a75bd91a452d5285ec447d9ca1be623e8eda3218835ce2ed9af71f741e8872c0; the independent review SHA-256 is 43d7e05efefb0905742b28f82b93c29e3de3eccc40e1189b1894e32912889dd9.

## Claim and dependencies

Let n=5^(2l+1)=5h², h=5^l, l≥1, and N=7n. Every complete M_N eigenspace in the orthogonal complement of W1=H7 tensor J1 H_(n/25) has dimension seven and has a simple Hermitian A_N compression. Consequently this newest sector, of dimension24N/25, splits locally to first order. This does not alone assert full or literal-time simplicity.

Inputs are the accepted exact oldform intertwining/compression and complete-eigenspace isolation, simple five-primary cat spectrum, S=[[3,4],[2,3]] order/valuation, actual32-mode coefficients, and seven-factor cubic eigenspaces. The even-depth newest-sector source supplies the elementary norm-circle/root-lifting argument, rederived below for the odd packet model. The new fiber calculation is explicit here; the contemporaneous residual125 proof is a parallel application, not a premise for this theorem.

Raw convention: T_n(a,b)f(x)=q^[b(x+a/2)]f(x+a), with q the induced primitive n-th root; M_n has kernel q^[-(3x²−2xy+3y²)/8]/sqrt(n). All halves are modular at the relevant odd modulus. Put Q(a,b)=2b²−a² and J=[[0,2],[1,0]]. The actual centered generator is4000^(-1)∑d_u T7(u) tensor T_n(u), with the unchanged32 Gaussian-integer coefficients.

## 1. Five-dimensional packets and complete character labels

Use the exact embedding J_l:H5→H_n and packets

    E_y=T_n(y)J_l H5,     y∈(Z/h)².

They are orthogonal and their sum is H_n. Indeed the oldform compression of T(y−x) vanishes unless both coordinates are divisible byh; each packet has dimension5 and there areh² packets. Weyl translation maps E_y to E_(y+u); the cat maps E_y to E_(Sy). Changes of representatives give only scalar five-power roots times five-dimensional Weyl operators.

Primitive packet labels form norm circles O_c={y:Q(y)=c modh}, c a unit. S acts freely and transitively on each, with length L=6*5^(l−1). As in the even case, labels divisible by5 give exactly W1 before tensoring withH7. Thus all primitive circles make up the newest sector.

Write S^L=[[a,2hβ],[hβ,a]], with β≡2 mod5 and a≡1 modh². On E_y its L-step holonomy is exactly

    B_y=q^[-ω(y,S^L y)/2] T5((S^L−I)y/h),            (1)

because M5^L=I. Its Weyl part is T5(2Jy mod5), primitive. It has five distinct characteristic-zero eigenlines. Each holonomy eigenvalue supplies L roots for a cat eigenvalue, so the circle supplies5L eigenvalues in all. Accepted cat simplicity rules out collisions between different circles.

Replacing a residual cat eigenvalue by a cube root times itself leaves its L-th power unchanged. Hence all three residual cat characters paired with the seven-factor sectors in one full product eigenvalue lie in the SAME circle and on the SAME holonomy eigenline. Every full newest-sector block has dimension3+2+2=7. There are no hidden mixed-circle or mixed-fiber labels.

Choose the representative y0=(a,0), a²=−c modh, when c≡1,4 mod5, and y0=(0,b),2b²=c modh, when c≡2,3. The required square roots lift because their residues are nonzero squares. Thus the initial fiber holonomy is respectively modulation or shift. Its five eigenlines are indexed by a fifth-root character. The remaining cycle eigenvalue supplies all L roots; together these account for every wild label, not just its tame residue.

## 2. Exact overlap normalization and the Gauss-sign kernel

Let η=q^(h²), a primitive fifth root, and g=∑_(x mod5)η^(x²), so g²=5 and v5(g)=1/2. Let ε=g/sqrt(5)∈{±1}. In the initial fiber choose a vector f0 of norm squared5: g times a coordinate vector for a modulation eigenline, or a fifth-root plane wave for a shift eigenline. A cat eigenvector on the circle has L packet components, transported from f0, each with unit scalar coefficient and a fiber Weyl operator times M5^k. Its norm squared is5L; its exact dual therefore has denominator5L.

For one Weyl translation u, a matrix element between the paired residual cat characters is a sum only over y,y+u∈O_c. Multiplication by gL leaves the normalized fiber overlap g/5 times the inner product of two transported fiber states. Every scalar or Weyl carry phase is a five-power root and must be retained until this reduction.

Here is the raw five-dimensional calculation controlling that overlap. Set C=M5/ε. Direct Gauss summation gives

    C(x,y)=g^(-1)η^(-x²−xy−y²),
    C²(x,y)=−g^(-1)η^(x²−xy+y²),
    C³=−P,
    C⁴(x,y)=−g^(-1)η^(-x²+xy−y²),
    C⁵(x,y)=g^(-1)η^(x²+xy+y²),                 (2)

where Pf(x)=f(−x). These formulas use the raw prescribed kernel since −3/8≡−1 and1/4≡−1 modulo5. The quadratic Gauss coefficient in the C² convolution is3, a nonsquare modulo5.

An inserted fiber Weyl operator only changes the linear/constant terms of each nondegenerate kernel. For coordinate-vector endpoints, g times the normalized overlap therefore reduces to ε^d s_d, with

    (s_0,s_1,s_2,s_3,s_4,s_5)=(0,1,−1,0,−1,1).                 (3)

The d=0,3 cases are integral before multiplication byg and vanish afterward. For plane-wave endpoints, the exact two-variable Gauss sum has nonsquare determinant; the nonparallel values in(3) acquire a minus sign. Thus the general factor is

    χ(c) ε^d s_d,       d=k_y−k_x modulo6,                    (4)

where χ is the quadratic character onF5×. This is independent of the wild fiber eigenline and all Weyl carry translations. The paired characters have the same initial fiber eigenline, as proved above. Every normalized overlap has valuation at least0; nonparallel terms have the displayed unit residue and parallel terms have positive valuation.

Let z_i∈{1,ω,ω²} label the seven-factor cat eigenbasis, with repetitions3,2,2. If the full product label has tame reduction ξ^t, put γ_i=ξ^t/z_i. The exact circle coefficient reduces to γ_i^(k_x)γ_j^(−k_y). The factor ε^(k_y−k_x) in(4) is absorbed by replacing allγ_i byγ_i/ε. This merely permutes the six tame labels, so both possible raw Gauss signs are covered.

## 3. Actual coefficient filter and norm intersections

At the Gaussian prime i→2, the actual upper modes u=(1,b), b=0,±1,±6,±7,±8, have unit d_u. Every other actual coefficient has positive valuation. Since all gL-normalized overlaps are integral by section2, every non-upper contribution vanishes after multiplication by4000gL. In particular the nonprimitive modes(0,±5), lower Gaussian coefficients and all diagonal aliases are accounted for, not discarded by a genericity assumption.

For a primitive upper mode u, the intersection condition y,y+u∈O_c is equivalent to

    y=−u/2+a Ju,
    a²=(1−4c/Q(u))/8 modh.                                  (5)

If the right side is a nonzero square modulo5, there are exactly two roots and they lift uniquely at every depth. If it is a nonsquare, there is no intersection. If it is zero modulo5, every intersection has y≡−u/2 and y+u≡−y modulo5. Its endpoint holonomy lines are parallel, so each individual normalized fiber overlap vanishes in the residue by(3). This applies already at l=1 and does not use a cancellation of the number of roots. It also handles all singular higher-digit lifts.

For a nonparallel intersection, the two norm-circle indices modulo6 are exactly the indices on O_(c mod5). All unit phases have residue1. Hence every depth and every wild label reduces to one of only24 finite matrices.

## 4. The finite matrices and lift

Work over the pinned F5^6 field containing a primitive seventh root w and a primitive sixth root ξ. For c=1,2,3,4 choose the pure representative described above modulo5 and number its six-point orbit y_k. For t=0,…,5 setγ_i=ξ^t/z_i. With B7(u)=V7^(-1)T7(u)V7, define

    C_(i,j)(c,t)=∑_(actual upper u) d_u B7(u)_(i,j)
       ∑_(kx,ky: y_kx=y_ky+u mod5)
          χ(c) s_(ky−kx) γ_i^kx γ_j^(−ky).                  (6)

There is no denominator6 in(6): we multiplied the characteristic-zero compression by4000gL, so its full exact circle denominatorL has been removed. The factor1/5 from the fiber normalization is already in the exact Gauss overlap in section2. Tangent points are excluded by s_3=0, rather than counted twice or treated as nonsingular lifts.

`odd_newest_discriminator.py` implements(6), preserving all nine actual upper coefficients and raw seven-factor phases. All24 degree-seven characteristic polynomials have derivative gcd1 overF5^6. Eight exact determinant evaluations and interpolation are used; no illegal division by5 occurs. The supplied JSON is the complete norm/tame list. Every primitive seventh root is a Frobenius conjugate, since ord_7(5)=6.

For each actual characteristic-zero full block, choose the seven-factor integral eigenbasis and the explicit circle/fiber eigenvectors above. The entries of4000gL times its compression are integral and reduce exactly to(6). No integral global ramified cat projector is assumed. The squarefree residue proves a nonzero characteristic-zero discriminant of the scaled compression. Removing the nonzero scalar gives simple Hermitian first-order slopes for every full newest-sector block.

## 5. Scope and next implication

The theorem concerns all odd five-primary depths2l+1≥3, and only their newest sector of dimension24N/25. The older layers are not asserted simple by this argument. The independently accepted proof and the inherited algebraic-time rank-transfer theorem turn these local simple branches into at least24N/25 simple eigenvalues at every nonzero real algebraic time. The separately accepted deepest odd-core theorem adds35 for odd depths≥5. The separately reviewed residual-125 combination, including its exact disjointness and odd-depth threshold, is recorded in odd_sector_count_combination.md. Neither statement establishes full U simplicity or a gap/BGS result.

This calculation differs from residual25's unit lattice: the fiber Fourier denominator really is present. It is removed in the projected matrix elements by the exact Gauss factor. The bounded matrices alone are not the uniform argument; sections1–3 supply the full packet/character/normalization dictionary.
