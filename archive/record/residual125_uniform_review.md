# Independent audit of residual-125 uniform second-order splitting

## Claim and verdict

**Primary verdict: proved as written, relative to the expressly inherited accepted cat, oldform and exact return-resolvent inputs. ACCEPT. No mathematical correction is needed.**

For every integer `j >= 2`, let `h=5^j`, `n=125h^2=5^(2j+3)` and `N=7n`. In the complete oldform spectral subspace `H7 tensor J_j H125`, all **120 new product-cat eigenspaces of dimension seven** have zero first-order compression and simple second-order phase matrices. The six old blocks, with dimensions `7,7,7,4,5,5`, are an inherited separate result. The dimensions sum to `120*7+35=875`; the total block count is 126.

The exact audited source is `frozen/residual125_uniform_candidate.md`, SHA256 `9efdd0257feae0d20c583e8ee94c0d8e1cee36c45d275cd4a5347a269c6b095a`. The source manifest and all thirteen dependencies were hash-verified before review and copied unchanged. All work resides in this independent review directory. No canonical BGS file or frozen source was edited.

This is a local eigenjet theorem. It proves neither full fixed-coupling propagator simplicity, gap bounds, arbitrary larger residual depth, nor BGS statistics. The computations below establish finite algebraic assertions. The separate uniform argument in sections 3–6 supplies the all-`j` implication.

## 1. Dependency graph and obligation matrix

The dependency graph is:

1. Accepted raw CRT/Weyl conventions, simple cat spectrum, oldform intertwining and complete-eigenspace isolation imply the exact target blocks and zero first order.
2. The separately audited general intermediate-return identity gives the actual second-order contribution, including character, initial factor, conjugation and seven-factor cocycle.
3. The raw 25-packet decomposition and six-step fiber holonomy select each actual residual cat character before any reduction.
4. The explicit Gauss overlap and five-step resolvent numerator give an integral normalized compression and its leading residue uniformly in depth.
5. Actual coefficient valuations and the shorter nonprimitive return remove exactly the discarded terms.
6. The resulting dictionary is formula (19). Its finite characteristic polynomials are independently squarefree.
7. The integral normalized matrix therefore has nonzero characteristic-zero discriminant; the common scalar normalization can be removed.

There is no additional external-literature leaf. Earlier cat and oldform theorems are inherited inputs, rather than claims re-proved by this computation. The general return source is pinned at SHA256 `3f42c4f41f448c221e4dc92495a11caa3b2cd661168f8cd888abd35971ed1932`; its accepted status is recorded by the pinned residual-25 independent review.

| Obligation | Disposition | Evidence |
|---|---|---|
| Exact 25 packets and raw Weyl/cat conventions | Passed | Direct integral cyclotomic packet checks and algebra below |
| Non-scalar primitive six-step holonomy | Passed | Exact `S^6`, fiber Weyl spectrum and all 24 primitive labels |
| All 120 wild/tame characters; product block counts | Passed | Character construction before reduction |
| Fourier denominator and transported lattice | Passed | Determinant valuations and explicit norm-30 duals |
| Raw Gauss normalization/sign in both base types | Passed | 180,000 exact identities, all fifth-root choices |
| Primitive five-step global packet gauge | Passed uniformly | Global translated oldform identity |
| Exceptional `j=2` residual cat and character | Passed | Retained explicitly until five-step cancellation |
| Primitive error and parallel bounds | Passed uniformly | `1/4-4a>0`, `1/2-4a>0` |
| Nonprimitive exceptional branch | Passed uniformly | Retained Weyl fiber action; bound `2-24a>0` |
| All discarded actual coefficients and initial shift | Passed uniformly | Gaussian valuations, norm polarization, subtraction bound |
| Exact 17-pair Gauss-sign dictionary | Passed | Independent reconstruction with raw seven-factor products |
| Root coverage and finite squarefreeness | Independently verified | 288 matrices, alternative arithmetic, basis and charpoly algorithm |
| Characteristic-zero lift | Passed uniformly | Integral compression plus squarefree reduction |

## 2. Packets, holonomy, characters and denominators

Write `E_y=T125(y)J1`, with labels `y in F5^2`. Oldform Weyl compression gives `E_y*E_z=delta_yz I5`. Hence the 25 five-dimensional packets exhaust `H125`. Weyl multiplication and covariance give the candidate's formulas (2)–(3), including both midpoint cocycles. These are identities for the prescribed raw operators.

The integer matrix is

    S^6 = [[19601,27720],[13860,19601]].

Consequently `(S^6-I)y/5=2Jy mod5` and `-omega(y,S^6y)/2=55Q(y) mod125`. Since `M5^6=I`, the six-step packet holonomy is

    H_y=q125^(55Q(y)) T5(2Jy),    H_y^5=eta^Q(y) I.

For primitive `y`, `2Jy` is nonzero and its Weyl matrix has each fifth root once. The six roots above each of its five eigenvalues give

    mu=zeta25^(6Q(y)+5k) xi^t,    k=0,...,4, t=0,...,5.

The sixth-power check is `6(6Q+5k)=11Q+5k mod25`. For each circle `Q(y)=c`, the five wild exponents are exactly the residue classes `r=c mod5`; all four circles give all twenty units modulo 25. Thus the 120 characters are distinct. Multiplication by a cube root preserves both the circle and the wild character, so each resulting new product eigenspace has dimension `3+2+2=7`. No sum over the five wild labels is taken in the compression.

For a nonzero translation component, the five-dimensional character basis is a chirp times a Fourier matrix. Its inverse has denominator 5 and its determinant has valuation `10*(1/4)=5/2`. Therefore a unit standard-coordinate change of basis would be false. The candidate does not make that assertion. A transported 30-cycle Fourier matrix has determinant valuation 15; this does not repair the nonintegrality of its transport to standard packet coordinates.

Use `g=sum eta^(x^2)`, with `g^2=5`. At modulation-base circles choose `g delta_k`; at shift-base circles choose the Fourier waves. Each has squared Hermitian norm 5. Transporting through six orthogonal packets gives `Phi_mu` with squared norm 30. Its dual is exactly the adjoint divided by 30. After factoring the fiber inner product divided by 5, only the unit factor `1/6` remains. Multiplication by `g` is essential to make the surviving Gauss overlaps integral.

The independent raw calculation transports the actual quadratic kernel successively, rather than assuming the displayed closed forms for its powers. It verifies for every pair of absolute powers, Weyl shift and fiber labels that a nonparallel overlap satisfies

    g * (<C^kx f_i,T5(w) C^ky f_j>/5)
      = chi(c) s_(ky-kx) * a fifth root,
    s=(0,1,-1,0,-1,1).

Parallel overlaps are zero or a signed fifth root before multiplication by `g`. All four primitive fifth roots are checked. Restoring `M5=epsilon C` multiplies the overlap by `epsilon^(ky-kx)`, absorbed by `gamma_i -> gamma_i/epsilon`. This is exactly a tame shift by three, already covered by all six tame labels.

## 3. Uniform primitive return and global packet gauge

Let `L=6*5^(j-1)`. The exact return operator, before any approximation, is

    X_u=mu^(-L) q^(-omega(u,S^L u)/2) T125((S^L-I)u/h) M125^L.

For `j>=3`, `150` divides `L`, so both residual cat and character are trivial. At `j=2`, `L=30` and

    M125^30|E_y=eta^Q(y) I,     mu^(-30)=eta^(-c).

These are generally nontrivial. They remain in the exact operator. Each step still permutes the base packets by `y -> y+2Ju`; it acts on the fiber by a Weyl operator and a scalar. The five-step product has `M5^(5L)=I` and `mu^(-5L)=1`, including `j=2`.

For clarity about the gauge, compose the original embeddings. Up to a scalar independent of the fiber coordinate,

    T_n(u) J_j E_y = T_n(x) J_(j+1),    x=u+hy.

On this global packet chart, covariance at time `5L` gives exactly

    X_u^5|y = kappa_x T5(w_x),
    kappa_x=q^(-omega(x,S^(5L)x)/2),
    w_x=(S^(5L)-I)x/(5h) mod5.

The scalar relating the two packet charts cancels on a return to the same packet. Changing a fiber chart by a Weyl operator only contributes a fifth-root cocycle. This establishes formula (11) without silently replacing the fiber holonomy by a scalar.

Here is the all-depth matrix valuation argument. `S^6=I+5A` with `A mod5=2J`. Binomial expansion inductively gives

    S^(6*5^r)=I+5^(r+1) A_r,    A_r mod5=2J.

Writing this matrix as `[[A,2C],[C,A]]`, one obtains `C/(2*5^(r+1))=1 mod5`. Its diagonal correction has twice the off-diagonal valuation, since `(A-1)(A+1)=2C^2` and `A+1` is a unit. At time `5L`, this gives `C/(10h)=1 mod5`.

Since `omega(x,S^(5L)x)=-C Q(x)`, the scalar exponent divided by `5h` reduces to `Q(u)`, which is nonzero. For

    delta=1-q^(5h),    a=v5(delta)=1/(4*5^(j+1)),

the scalar has exact order `5^(j+2)` and

    (1-kappa_x)/delta -> Q(u),    v5(1-kappa_x^5)=5a.

This is a uniform derivation, independent of the bounded `j=2,...,8` controls.

Use the exact two-stage inverse

    (I-X)^(-1)=(I+X+X^2+X^3+X^4)(I-X^5)^(-1),
    (I-kappa T5(w))^(-1)=sum_(r=0)^4 kappa^r T5(rw)/(1-kappa^5).

For fixed endpoint packets there is at most one contributing outer power. It only adds Weyl displacement and unit phases. For nonparallel fiber directions, each inner numerator overlap is a common signed `1/g` Gauss factor times a fifth root. Replacing those five fifth-root phases by the first changes each term by valuation at least `-1/2+1/4`. Consequently, after multiplying by `delta g`, the error has valuation at least

    a+1/2-5a-1/2+1/4 = 1/4-4a > 0.

The constant-phase geometric numerator cancels exactly to `1/(1-kappa)`. Its normalized leading coefficient is the Gauss sign times `Q(u)^(-1)`. In a parallel direction every numerator overlap is integral, and its normalized valuation is at least `1/2-4a>0`. At the smallest depth these bounds are respectively `121/500` and `123/250`.

Roots of higher five-power order in the outer packet transports are units. They are reduced only after integrality has been established. The argument needs a fifth-root error bound solely for the inner fiber numerator; it never falsely assigns that bound to every packet phase.

## 4. Initial factors, discarded coefficients and exceptional nonprimitive branch

The inherited weighted return identity contributes

    i d_v d_u / 4000^2 * P [B7(v,u) tensor D_a(I-X_(u,a))^(-1)] P,

with the exact initial Weyl factor `D_a`, the conjugated return, and the raw seven-factor product. The factor `i` is the result of `i/(2R)` times `2R`. No residual period or projector denominator is dropped.

For surviving upper pairs the integer norms are equal. Write `S^a u=-v+h c_a`. Polarizing the norm gives

    B_Q(v,c_a)=h Q(c_a),    B_Q(v,c)=-2v_1c_1+4v_2c_2.

Its mod-5 kernel is `span(Jv)`. Both the initial displacement and the conjugated return direction lie in that same line. The incidence condition is therefore exactly `x-y in span(Jv)`, with no affine shift. Higher lifts of `a` do not change the seven factor because `S mod7` has order three, and the return modulo five fixes `a mod6`.

At `i -> 2`, an upper coefficient is a unit. Lower coefficients have valuation two: their common factor `-3+4i` has norm 25 and unit conjugate. All diagonal coefficients have positive valuation. The primitive normalized compression is already integral by section 3; all primitive pairs other than upper/upper therefore disappear.

For the only nonprimitive modes `u=5u0=(0,+/-5)`, set `L'=6*5^(j-2)`. Their base packets again form five-cycles. At `j=2`, `M125^6` is genuinely non-scalar on a packet, but its fiber part is Weyl, not a residual cat matrix. Thus all relevant numerator overlaps still have valuation at least `-1/2`.

In the global chart `x=5u0+hy`, the off-diagonal coefficient at time `5L'` has valuation `j`, and `Q(x)` has valuation two. The scalar exponent therefore has valuation `j+2`, so its order is `5^(j+1)`. At `j=2` the character factor `mu^(-5L')=mu^(-30)=eta^(-c)` must also be included in this scalar. It has order five, strictly smaller than the scalar's order 125, and changes neither its conductor nor the denominator estimate. For `j>=3` that character factor is trivial. This makes explicit an exceptional-depth factor already allowed by the candidate's scalar holonomy notation.

Hence `v5(1-(kappa')^5)=25a`. With the two actual coefficients of total valuation two, the deliberately coarse normalized bound is

    2+a+1/2-25a-1/2 = 2-24a > 0.

At `j=2` it is `244/125`. This argument does not set `M125^6` or the exceptional character to one. Mixed contents do not return. The finite `k=0` subtraction has no remaining resolvent-period denominator; `g` makes its compressed Weyl entries integral and `delta` kills its reduction.

The upper norm values `-1,1,71,97,127` are distinct modulo 25. Thus for every `h>=25`, upper pairs return exactly when their integer norms agree. This leaves the stated 17 ordered pairs, including all aliases separately.

## 5. Dictionary, all wild labels, finite certificate and root coverage

Each actual block is selected in characteristic zero first. Its seven coordinates have residual characters with the same norm circle and same wild label, with tame reductions `gamma_i=xi^t/z_i`. Combining the norm-30 dual, the Gauss factor and section 3 yields precisely

    C_(c,t),ij = sum_(17 pairs) [2 d_v d_u/Q(u)] B7(v,u)_ij
      * (chi(c)/6) sum_(kx,ky)
          gamma_i^kx gamma_j^(-ky) R_v(y_kx,y_ky) s_(ky-kx).

The `2` is the image of `i`; `1/6` is the remaining unit dual denominator. The line orbit sum is unnormalized. There is no further `1/5`, and the residual-25 scalar reflection kernel does not apply. Parallel positions vanish through `s_0=s_3=0`. The five fiber labels can affect only fifth-root phases in the leading calculation, so all five wild labels give the same residue after their actual blocks have been selected. The 120 blocks therefore reduce to 24 matrix types.

`rebuild_residue.py` imports no author module. It uses:

- schoolbook polynomial multiplication over `F5[t]/(t^6+t^4+3t^3+t^2+1)`, with an independent Rabin irreducibility check, rather than exponent/log tables;
- raw seven-position cat and Weyl matrices;
- spectral-projector columns selected from right to left, rather than the author's kernel/free-column basis;
- a division-free recursive Berkowitz characteristic polynomial, rather than eight determinant evaluations and interpolation;
- exact polynomial derivative gcds.

All **288 matrices** are rebuilt: six primitive seventh roots, both primitive sixth roots, four circles and six tame labels. Every derivative gcd has degree zero. At the pinned roots all 24 characteristic polynomials match the author's frozen polynomials exactly, although matrix coordinates use a different basis. All root changes also match the exact Frobenius permutation of the polynomials. Because `ord_7(5)=6`, this explicitly covers every seventh-root choice; the four fifth-root choices and both raw-cat Gauss signs are covered by the raw identities and tame relabeling.

`rebuild_raw.py` uses integer cyclic convolution modulo `1+eta+...+eta^4` and raw cat transport. It checks **180,000 exact fiber identities**, including all four primitive fifth roots, both base types, all 36 absolute cat-power pairs, all 25 fiber Weyl shifts and all 25 character-label pairs. It independently checks **15,625 raw cat/packet entries**, **15,625 packet Gram entries**, **390,625 raw Weyl entries**, all 24 primitive holonomies, and all 120 new characters. Modular conductor controls cover `j=2,...,8`; their role is implementation control, not uniform proof.

## 6. Lift and stopping boundary

The seven-factor cat projectors have unit denominators at five, so a characteristic-zero integral eigenbasis can lift the finite projector-column bases. In each already-selected residual character block, the explicit dual and sections 3–4 show that

    4000^2 delta g * H2

is integral in the stated cat-eigenvector coordinates and reduces to its certified `C_(c,t)`. The discriminant reduces to a nonzero field element. It is therefore nonzero in characteristic zero. Removing the nonzero scalar normalization preserves multiplicities. Together with inherited exact first-order vanishing, this proves the claimed second-order splitting for every `j>=2`.

There is no missing uniform implication in this continuation. The accepted inherited inputs remain explicit. The proof uses a normalized compression lattice; it does not assert an integral full residual spectral projector or a unit standard-position eigenbasis.

## Reproduction and provenance

From this directory, with assertions enabled and Python 3:

    python rebuild_residue.py
    python rebuild_raw.py
    python run_checks.py
    python validate_manifest.py computation_manifest.json --root .

The first two commands reproduce the mathematical controls. `run_checks.py` reruns both in captured subprocesses, records actual argv, start time, software, resource caps and input hashes before/after, and writes the version-2 computation manifest. The source and final review manifests pin the portable frozen inputs and all review artifacts. Randomness, floating-point eigenvalues and numerical tolerances are absent.
