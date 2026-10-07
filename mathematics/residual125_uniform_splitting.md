# Residual-125 packets and uniform second-order splitting

**Status:** source-bound author candidate, pending fresh independent audit. The raw packet dictionary and Gauss-overlap identities have exact cyclotomic controls. The 24 residue characteristic-polynomial certificates are author evidence, not an independent review. Accepted packets and canonical BGS files were not changed.

## Target and dependency boundary

Let `j >= 2`, `h=5^j`, `n=125 h^2=5^(2j+3)`, and `N=7n`. Use the prescribed raw Weyl operators and normalized quadratic cats, with the induced primitive root `q` of order `n`:

    T_n(a,b)f(x) = q^[b(x+a/2)] f(x+a),
    (M_n)_(x,y) = n^(-1/2) q^[-(3x²-2xy+3y²)/8],
    S = [[3,4],[2,3]],  J = [[0,2],[1,0]],
    omega(v,w)=v_1 w_2-v_2 w_1,   Q(v)=2v_2²-v_1².

Every fractional exponent uses its inverse at the relevant odd modulus. Put `q125=q^(h²)`, `eta=q125^25`, and `zeta25=q125^5`. The oldform intertwining/compression, complete-eigenspace isolation, simple prime-power cat spectrum, exact order and valuations of `S`, and the return-resolvent identity are inherited from the pinned inputs. No external literature implication is added.

The candidate conclusion is: in `H7 tensor J_j H125`, its **120 new residual product-cat eigenspaces of dimension 7** have simple second-order phase matrices, uniformly for all `j>=2`. Their first-order matrices vanish by the accepted oldform compression. The remaining six old residual product blocks are the prior deepest odd core, with dimensions `7,7,7,4,5,5`; they are not new claims here. Thus the residual-125 space has dimension `840+35=875`, and its total product block count is 126.

This is a local eigenjet statement. It asserts neither full `U_N` simplicity at a fixed nonzero coupling nor BGS universality.

## 1. Exact 25-packet decomposition

Let `J1:H5 -> H125` be the accepted embedding. For representatives `y in {0,...,4}²` set

    E_y = T125(y) J1.

Then `E_y* E_z=delta_(y,z) I5` by the exact Weyl compression rule. Dimension counting gives

    H125 = orthogonal direct sum_(y in F5²) E_y H5.                 (1)

This is a block-coherent basis with 25 fibers of dimension five. It is not a scalar coherent basis.

For a Weyl translation `u`, write `r=u+y mod 5` in the chosen representatives and `d=(u+y-r)/5`. Direct Weyl multiplication gives

    T125(u) E_y = E_r q125^[(omega(u,y)-omega(r,u+y))/2] T5(d).     (2)

Similarly, writing `r=Sy mod 5`, `d=(Sy-r)/5`,

    M125 E_y = E_r q125^[-omega(r,Sy)/2] T5(d) M5.                 (3)

All scalar factors in these formulas have five-power order. The origin packet is `J1 H5`, with cat `M5`; the remaining 24 labels form four primitive norm circles, each with six packets.

## 2. Primitive six-cycle holonomy and exact characters

The exact integer identity

    S^6 = [[19601,27720],[13860,19601]]

and `M5^6=I` give, for a primitive packet `y`,

    M125^6 E_y = E_y H_y,
    H_y = q125^[55 Q(y)] T5(2Jy),
    H_y^5 = eta^[Q(y)] I5.                                      (4)

Indeed `(S^6-I)y/5 = 2Jy mod 5`, and `-omega(y,S^6 y)/2 = 55Q(y) mod125`. The vector `2Jy` is primitive. Its Weyl operator has the five simple eigenvalues `eta^k`, so the fiber holonomy is genuinely non-scalar. Its eigenvalues are

    lambda_(y,k) = zeta25^[11 Q(y)+5k],  k=0,...,4.

Choose a primitive sixth root `xi`. The resulting 30 cat eigenvalues on this circle are

    mu_(y,k,t) = zeta25^[6 Q(y)+5k] xi^t,  t=0,...,5.             (5)

The exponent identity `6(6Q+5k)=11Q+5k mod25` verifies the sixth power. On the circle `Q(y)=c mod5`, its wild exponents run exactly through the five classes `r=c mod5`. Thus all new characters are exactly

    zeta25^r xi^t,  r in (Z/25)^×,  t in Z/6.                   (6)

They are 120 distinct characters. The other five are the inherited tame `M5` characters. Multiplication by a cube root stays in the same circle and the same wild label `k`; consequently a new full product-cat block has dimension `3+2+2=7` and uses three cubic-related tame characters in this one packet circle.

A useful exceptional-depth identity follows directly from (4):

    M125^30|_(E_y H5) = eta^[Q(y)] I5.                           (7)

For primitive returns, `L=6*5^(j-1)`. If `j>=3`, `M125^L=I`. If `j=2`, `L=30`, so the nontrivial residual cat is packetwise scalar by (7). For a product block on norm `c`, its character factor is `rho=mu^(-30)=eta^(-c)`. It must be retained in exact expressions, although it reduces to one.

## 3. The first new denominator and the appropriate lattice

For a nonzero Weyl vector `(A,B)` with `A!=0`, an unnormalized eigenbasis of `T5(A,B)` is

    f_k(x)=eta^[-B x²/(2A)+kx/A],  k in F5.

The basis is a unit diagonal chirp times a permuted Fourier matrix. Its inverse is `1/5` times conjugate unit entries, and its determinant has `v5=5/2`. In particular it is **not** a unit change of basis in the standard five-coordinate lattice. The fiber spectral projectors have the exact denominator 5. For `A=0`, a coordinate basis diagonalizes the Weyl operator, but cat transport to other directions has Gauss denominators.

This is the first actual obstruction to copying the residual-25 unit circlewise argument: residual 25 has scalar six-cycle holonomy and only the unit denominator 6; residual 125 first has a wild five-character fiber split. A globally chosen standard fiber basis cannot make all these changes unit matrices.

There is a useful exact transported lattice. On each primitive norm circle choose a base `y0`, and use `M125^r E_y0` to transport a fiber basis to its six packets, `0<=r<6`. The first five edges are identities in this basis, and the last is `H_y0`. If the base has nonzero translation component in `2Jy0`, the last edge is a monomial five-cycle. Diagonalization can therefore be viewed as a 30-cycle Fourier transform, with dual denominator 30 and determinant valuation 15 relative to that transported coordinate lattice. The latter lattice itself has metaplectic denominators relative to the original packet coordinates. This construction does not assert an integral global spectral projector.

For actual matrix compression it is better to retain explicit eigenvectors and their duals. Put

    g = sum_(x in F5) eta^(x²),   g²=5,   epsilon=g/sqrt(5) in {1,-1}.

For a circle with `c=1,4`, choose a base `y0=(a,0)` and take fiber eigenstates `g delta_x`; for `c=2,3`, choose `y0=(0,b)` and take Fourier eigenstates `eta^(kx)`. Both have squared Hermitian norm 5. Let `f_k` be the appropriate holonomy eigenstate and define

    Phi_mu = sum_(r=0)^5 mu^(-r) M125^r E_y0 f_k.                (8)

Then `M125 Phi_mu=mu Phi_mu` and `||Phi_mu||²=30`. Its exact dual thus has denominator 30. Dividing fiber inner products by 5 leaves the **unit** six-cycle denominator `1/6`. The nonunit fiber overlap is retained and is removed by the additional scalar `g` in the operator normalization below.

The span of the `Phi_mu`, tensored with an integral seven-factor eigenbasis, is the cat eigenlattice used here. The claim is that the **normalized second-order compression**, rather than every unnormalized Weyl matrix, preserves this lattice. This distinction prevents a false unit-eigenbasis assertion.

## 4. Exact raw Gauss-overlap kernel

Write `M5=epsilon C`. Direct finite Gauss summation in `Q(eta)` gives

    C_(x,y)     =  g^(-1) eta^(-x²-xy-y²),
    (C²)_(x,y) = -g^(-1) eta^( x²-xy+y²),
    C³         = -parity,
    (C⁴)_(x,y) = -g^(-1) eta^(-x²+xy-y²),
    (C⁵)_(x,y) =  g^(-1) eta^( x²+xy+y²),
    C⁶         = I.                                            (9)

Let `s=(0,1,-1,0,-1,1)`, indexed modulo six. In the transported gauge, for any fiber Weyl translation and any two fiber character labels, nonparallel endpoint directions have an inner product equal to `1/g` times a root of fifth order and a fixed sign. More exactly,

    residue of g * [ <M5^kx f_i, T5(w) M5^ky f_j>/5 ]
       = chi(c) epsilon^(ky-kx) s_(ky-kx),                      (10)

where `chi` is the quadratic character of `F5×`. The parallel cases `ky-kx=0,3` have integral inner product, so the left side is zero. The quadratic Gauss factor is independent of `w` and the fiber character labels; those only change fifth-root phases.

For modulation-base circles, (10) is read off from (9). For Fourier-base circles the two-variable Gauss sum changes its sign: for instance the quadratic determinant at power one is 2, a nonsquare modulo 5. The same calculation at powers two, four and five gives `-s`. These are precisely `chi(c)=+1` and `-1`, respectively.

Changing the base point around a circle changes the transported eigenvector gauge, not the kernel. Any representative used to enumerate the same circle is therefore allowed. If `epsilon=-1`, absorb `epsilon^(ky-kx)` into the tame factors by replacing every `gamma_i` by `gamma_i/epsilon`. This permutes the six tame labels by three, so the same 24 finite matrices suffice for either primitive-root square class.

## 5. Five-packet primitive returns and normalization

Use the accepted exact intermediate return operator, including its initial factor and character:

    X_u = mu^(-L) z_u T125(b_u) M125^L,
    b_u=(S^L-I)u/h mod125,
    z_u=q^[-omega(u,S^L u)/2].

On packet labels modulo 5 its permutation is `y -> y+2Ju`, for every `j>=2`. This includes `j=2` by (7). Hence every base-label cycle has length five. After five steps the fiber cat is identity because `M5^(5L)=I`; character normalization also disappears since `mu^(5L)=1`. Identifying the packet with global translated label `x=u+hy`, its five-step holonomy has the form

    X_u^5|_y = kappa_x T5(w_x),
    kappa_x = q^[-omega(x,S^(5L)x)/2],
    w_x=(S^(5L)-I)x/(5h) mod5.                                (11)

Choices of packet identifications can conjugate this formula by a Weyl operator; this changes only fifth-root factors in `kappa_x` and the fiber matrix elements, which do not affect the estimates or leading coefficient below. Equivalently one can use the global `T_n(x)J_(j+1)` packet identification, in which (11) is exact as displayed.

The exact five-adic matrix valuation gives

    kappa_x has order 5^(j+2),
    delta = 1-q^(5h),     a=v5(delta)=1/(4*5^(j+1)),
    residue of (1-kappa_x)/delta = Q(u),
    v5(1-kappa_x^5)=5a.                                      (12)

The leading coefficient follows from writing `S^(5L)=[[A,2C],[C,A]]`, where `C/(10h)=1 mod5`; then the exponent in (11) is `(C/2)Q(x)` and `Q(x)=Q(u) mod5`.

On the five-cycle, the exact inverse is

    (I-X)^(-1)=(I+X+X²+X³+X⁴)(I-X⁵)^(-1),
    (I-kappa T5(w))^(-1)
       = [sum_(r=0)^4 kappa^r T5(rw)]/(1-kappa^5).             (13)

Do not first replace the fiber by a scalar and then apply a nonintegral projector. Instead take the explicit fiber matrix elements in (13).

For nonparallel endpoints, every matrix element of the five numerator Weyl terms has a common Gauss factor of valuation `-1/2`; its remaining dependence on `r` is a fifth-root phase. Replacing those phases by the phase at `r=0` changes the numerator matrix element by valuation at least `-1/2+1/4`. After multiplying by `delta*g/(1-kappa^5)`, the error has valuation at least

    a+1/2-5a-1/2+1/4 = 1/4-4a > 0.                          (14)

The constant-phase numerator is the ordinary geometric sum, so its denominator cancels to `1/(1-kappa)`. Equations (10) and (12) give its leading residue. For parallel endpoints every numerator matrix element is integral, and the full normalized expression has valuation at least

    a+1/2-5a = 1/2-4a > 0.                                   (15)

Thus only the nonparallel Gauss kernel survives. This proves that the first fiber correction does not dominate the proposed normalization. No unproved finite-difference gain is needed.

Including the initial residual Weyl factor in the accepted return formula only changes fifth-root phases and the base-label incidence condition. For an equal-integer-norm returning pair `(v,u)`, its initial displacement `c_a=(v+S^a u)/h mod5` belongs to `span(Jv)`: expand `Q(v+hc_a)=Q(v)` modulo `h²`. The return direction is also `span(Jv)`. Therefore the incidence condition is exactly

    x-y in span_(F5)(Jv),                                    (16)

with no omitted affine shift.

## 6. All discarded actual coefficients remain negligible

The normalization for the actual second-order phase operator is

    4000² delta g.                                            (17)

At the Gaussian prime `i -> 2`, only upper modes `v=(1,b)`, `b=0,±1,±6,±7,±8`, have unit `d_v`. Lower coefficients have valuation two and diagonal coefficients have positive valuation. The primitive normalized matrix elements are integral by (14)-(15), so every primitive pair except upper/upper vanishes in the residue.

For the two nonprimitive modes `(0,±5)`, use the exact period `L'=6*5^(j-2)`. Their packet permutations again have five-cycles. Their five-step scalar holonomy has conductor `j+1`, so

    v5(1-(kappa')^5)=25a.

Even at `j=2`, where `M125^6` is non-scalar, it is packetwise Weyl by (4), and its fiber cat factor is identity. Every numerator fiber Weyl matrix element has valuation at least `-1/2`. A deliberately coarse bound after (17) and the two actual coefficients is therefore

    2 + a + 1/2 -25a -1/2 = 2-24a > 0.                       (18)

At `j=2` this is `244/125`. Thus the exceptional nonprimitive branch is negligible without assuming that its residual cat is scalar. Mixed contents do not return. The `k=0` subtraction has no remaining resolvent-period denominator; after multiplying by `g` its compressed Weyl entries are integral, and the further `delta` factor kills it.

For all `j>=2`, the five upper integer norms `-1,1,71,97,127` are distinct modulo 25. Consequently precisely the inherited 17 ordered equal-integer-norm upper pairs survive. This includes all aliases individually.

## 7. Exact 17-pair finite dictionary

Take the pinned residue field

    F = F5[t]/(t^6+t^4+3t^3+t²+1),  w=t^9,

with the recorded primitive sixth root `xi`. Let `V7` diagonalize `H7=G7/Tr(G7)` with labels `z_i in {1,omega,omega²}` of multiplicities `3,2,2`. Seven-factor projectors are integral at five. For norm `c in {1,2,3,4}` and tame index `t in {0,...,5}`, number its six-point circle `y_k=S^k y0`, and put `gamma_i=xi^t/z_i`. The possible `epsilon=-1` case is the tame reindexing already described.

For each actual ordered upper pair `(v,u)` of equal integer norm, let `a0 mod6` be the unique solution `S^a0 u=-v mod5` and retain

    B7(v,u)=V7^(-1) T7(v) T7(S^a0 u) V7.

The actual seven-factor cocycle is in this product. Since `S mod7` has order three, this is the same seven factor as at the full lifted return time. Define

    R_v(x,y)=1 if x-y in span(Jv), else 0,
    P_ij(v;c,t)=(chi(c)/6) sum_(kx,ky=0)^5
       gamma_i^kx gamma_j^(-ky)
       R_v(y_kx,y_ky) s_(ky-kx).

Then the reduction of (17) times the actual seven-dimensional phase compression is exactly

    C_(c,t),ij = sum_(17 pairs)
       [2 d_v d_u / Q(u)] B7(v,u)_ij P_ij(v;c,t).              (19)

The `2` is the reduction of the accepted prefactor `i` at `i->2`. The five-term return orbit sum is unnormalized; `1/6` comes from (8), after treating the fiber denominator by `g`. Neither an additional `1/5` nor the residual-25 identity-plus-reflection kernel is allowed. Parallel/tangent terms vanish through `s_0=s_3=0` rather than an informal multiplicity convention.

Equation (19) is independent of the five wild labels, while those labels were retained until the characteristic-zero block was selected. Thus the 120 new dimension-seven blocks reduce to **24** types, not 24 blocks.

## 8. Certificate, lift, and review boundary

The pinned `gauss_kernel_discriminator.py` constructs the 24 matrices in (19) over the exact field and computes their degree-seven characteristic polynomials by eight determinant evaluations and exact interpolation. Its stored output reports all 24 derivative gcds of degree zero. The script and result were originally labeled conjectural because their dictionary had not yet been proved; that historical labeling is preserved in the input copies. Sections 1-7 above supply the candidate bridge, still pending fresh audit.

The normalized characteristic-zero matrix is integral in the explicit cat eigenvector coordinates by (14)-(18) and the unit six-cycle/seven-factor denominators. Its reduction is (19). Squarefree residue implies a nonzero characteristic-zero discriminant. Removing the nonzero scalar (17) proves the candidate second-order simplicity claim for each of the 120 new blocks. First order vanishes by the inherited oldform theorem.

`verify_packet_dictionary.py` separately checks 15,625 raw cat/packet entries in `Z[q125]/Phi125`, the exact packet Gram matrix, raw Weyl actions, all six-cycle holonomies, all 125 characters, the explicit `M5` kernels, and **7,500** exact fiber Gauss-overlap identities in `Q(eta)`. It also checks primitive/nonprimitive holonomy coefficients for `j=2,...,6`. The latter finite tests support formulas, while the all-j proof is the valuation argument above.

The source manifest pins all input files and certificate dependencies; the output manifest pins the candidate and verifier output. No independent audit is claimed in this packet. A fresh audit must check the global packet gauge in (11), the exact character normalizations, the primitive correction estimate, the exceptional nonprimitive branch, and identification of (19) with the certificate, before promotion.

## Frozen certificate identifiers

- `inputs/gauss_kernel_discriminator.py`: SHA256 `c7b80cd196b87d48119f4cc6a62418512532be7e75e83f019354c144a626b99e`.
- `inputs/gauss_kernel_discriminator.json`: SHA256 `a2bf06ca238a74efcb671b070aab8c7a6ff525df09749305b335d1d869cab4c5`.
- The final certificate uses pure modulation/Fourier base representatives and was replayed after that change; all 24 polynomials were unchanged.
