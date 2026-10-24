# Second-order splitting of the deepest odd-depth core

Status: independently accepted project proof within the stated component scope. Scope is N=7*5^(2r+1), r>=2, and only the complete M-eigenspaces in the deepest oldform subspace H7 tensor J_r H5. Its six block dimensions are7,7,7,4,5,5. First-order compression vanishes. The claim is simplicity of their second-order phase matrices, not full or fixed-coupling U-simplicity.

Full-eigenspace isolation and the zero first-order compression are the separate oldform_tower_compression.md input, at j=r. The even-depth3,2,2 result is the separately reviewed even_oldform_second_jet.md. This extension uses its fixed17-pair residue matrix, with an additional pairwise-coprimality check between its three compressed characteristic polynomials.

## 1. A cat-stable small-translation lattice in dimension five

Let eta be the induced primitive fifth root, pi5=eta-1, and choose rho with rho²=pi5, so v5(rho)=1/8. On functions on x=0,...,4 take the lattice L0 spanned by rho^k x^k, 0<=k<=4. Polynomial evaluation on these five points has Vandermonde determinant prime to5 before the displayed scaling.

The cyclic shift X satisfies (X-I)L0⊂rho L0. The ordinary polynomial difference lowers degree and gains at least one rho. The wrap correction at x=4 involves5^k for k>=1; its expansion in the integral Lagrange basis has valuation at least k+(k-4)/8>=5/8, so it satisfies the same bound.

For Zf(x)=eta^x f(x), expand eta^x=(1+pi5)^x through degree four. Multiplication by its jth term gains pi5^j; reducing polynomial degree modulo product_(a=0)^4(x-a) is integral and raises the output degree by at most j. After the rho scaling its valuation is at least j/8. Thus (Z-I)L0⊂rho L0 as well. It follows for every raw Weyl T5(v) that

    (T5(v)-I)L0⊂rho L0.                              (1)

The normalized M5 has M5^6=I. A phase-safe derivation uses its accepted simple spectrum and scalar sixth power: it occupies five of the six possible roots; its missing root is -Tr M5, and the elementary fifth-root Gauss identity gives (Tr M5)²=1. Hence the sixth-power scalar is one.

Define L=sum_(j=0)^5 M5^j L0. This is a full lattice stable under M5. Exact Weyl covariance transports(1) to every summand, so

    (T5(v)-I)L⊂rho L  for every v.                  (2)

The six possible cat eigenvalues are distinct modulo5. Its five nonzero spectral projectors are integral on L, with rank-one direct-summand images. Therefore(2) is valid in an integral M5 eigenbasis. This avoids treating the nonintegral standard Fourier matrix as a unit matrix at5.

## 2. Exact operator-valued return sum

Put h=5^r, n=5h², R=6*5^(2r), and let q be the CRT primitive root of order n. The old embedding J=J_r obeys M_n J=J M5 and the exact Weyl compression rule. The second-order resolvent is the same finite sum as in the even-depth proof.

For a primitive mode u, set Lh=6*5^(r-1). Since S^Lh=I modulo h, the translated oldspace T_n(u)J H5 is preserved by M_n^Lh. Direct covariance gives the exact identity

    M_n^Lh T_n(u)J = T_n(u)J B_u,
    B_u=z_u T5(b_u),
    b_u=(S^Lh-I)u/h modulo5,
    z_u=q^(-omega(u,S^Lh u)/2).                     (3)

Here M5^Lh=I. Write S^Lh=[[a,2h beta],[h beta,a]]. Then beta is a unit with beta≡2 modulo5, and

    z_u=(q^h)^(beta Q0(u)/2),  Q0(a,b)=2b²-a².       (4)

Thus z_u has order5^(r+1). In particular I-B_u is invertible, because T5(b_u) has order dividing5.

For a returning pair v,u, the return times are a modulo Lh, as in the norm-torus classification. Moving the initial a powers through(3), and cancelling the cat eigenvalue on the right, gives a fixed factor

    D0=theta T5(c0)

times powers of a conjugate B_a of B_u. Both theta and all scalar conjugating phases are roots of5-power order. The seven-dimensional Weyl factor is fixed along this class since3 divides Lh.

There are R/Lh=5^(r+1) terms. The exact matrix geometric identity yields

    sum_j(R-2a-2Lh j) D0 B_a^j
       =2R D0(I-B_a)^(-1).                          (5)

The k=0 term, if present, must be subtracted exactly as in the even proof. It disappears after the final normalization. Formula(5) follows from B_a^(R/Lh)=I and invertibility of I-B_a; it is not a scalar approximation to a matrix sum.

For the only nonprimitive modes(0,±5), use Lh'=6*5^(r-2). The same argument gives a scalar z_u of order5^r instead. Mixed contents cannot return. All statements include r=2, where Lh'=6.

## 3. Uniform leading residue

Let zeta=q^h have order5^(r+1), delta=1-zeta, and use the Gaussian prime i→2 above5. Then

    v5(delta)=1/(4*5^r)<1/8=v5(rho).

For primitive returns, write B_a=z T5(b). In the lattice L,

    (I-B_a)/delta = ((1-z)/delta)I
                   - z(T5(b)-I)/delta.

The second term has strictly positive valuation by(2), while the first reduces to Q0(u) times the identity because beta/2≡1. Consequently

    delta D0(I-B_a)^(-1) reduces to Q0(u)^(-1) I5.   (6)

The constant D0 reduces to I5. For nonprimitive pairs the scalar denominator has valuation5v5(delta), still strictly less than1/8 for r>=2. Their two Gaussian coefficients have total valuation2, so their normalized contribution has positive valuation at least2-4v5(delta).

Now multiply the common second-order operator by4000² delta. Exactly as in the accepted even-depth proof, only the17 upper/upper pairs survive. The distinct upper norm values -1,1,71,97,127 are already distinct modulo25. The scalar return time modulo3 and the seven-factor cocycle are unchanged. Hence, in the tensor product of the standard seven-dimensional lattice and L, the leading residue is

    K7 tensor I5,                                   (7)

where K7 is EXACTLY the fixed matrix from oldform_second_jet_residue.json. This is a statement about the actual second-order operator, with both the projector denominator and the five-dimensional lattice controlled.

## 4. Compression and bounded certificate

M7 and M5 have prime-to-five scalar orders3 and6, so their spectral projectors are integral in the chosen lattices. Each M5 eigenspace is rank one. At a fixed product eigenvalue, at most one M5 eigenvalue occurs for each of the three M7 eigenvalues. Therefore the compression of(7) is a direct sum of a subset of the three K7-compression blocks of dimensions3,2,2.

The prior certificate proves each of their characteristic polynomials squarefree. The supplementary exact check oldform_second_jet_pairwise.py proves these three polynomials are pairwise coprime over the pinned F5^6 field. Every such direct sum is therefore simple. The actual old-core dimensions are7,7,7,4,5,5, consistent with these subsets.

Residue discriminant nonvanishing lifts through the integral projector lattices, and the nonzero scalar normalization can be removed. Thus all six actual second-order phase matrices are simple for every r>=2. Since first order vanishes, these groups split at exactly order two near t=0.

This treats only the deepest odd core of dimension35. The larger oldform tower and new size-seven blocks remain separate. It gives no global discriminant or literal-U simplicity theorem by itself.

## Finite discriminator, separate from the uniform proof

odd_core_second_order_control.py directly sums all rotated actual-mode returns for N21875 over F525001, constructs the35-dimensional operator, and checks all six compressed polynomials squarefree. It supports the operator dictionary at r=2 but is not the reason for the all-r conclusion. The norm-torus, lattice and Gauss-residue arguments above supply that implication.

## Publication and dependency scope

This exact source has its separately pinned independent review in the
cat/jet promotion map. The final accepted combined FM-026 statement is in
[the theorem owner](literal_time_multiplicity_bounds.md). Conditional sector
premises retain their historical proof structure and are used only where
the separately accepted premise is explicitly bound. No unpublished CRT or
first-old-layer diagnostic is a new theorem input or extra U dimension.
