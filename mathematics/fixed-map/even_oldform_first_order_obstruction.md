# Exact failure of first-order cat splitting at every even depth e>=4

Status: independently reviewed obstruction to the first-order criterion. This refutes a sufficient first-order criterion, not simplicity of the actual propagator.

Let e=2r with r>=2, n=5^(2r), N=7n. Use the exact CRT factorization of the raw kernel, with the induced primitive-root powers on its two factors. In the n-dimensional factor define

    psi(x)=5^(-r/2) if 5^r divides x, and zero otherwise.

It is a unit vector. Direct summation in the normalized quadratic kernel gives M_n psi=psi: the sum over y=5^r k vanishes unless5^r divides x, and otherwise the chirp phase is one and the geometric sum is5^r. This works for every primitive-root power in the CRT factor.

The same geometric sum gives, for the raw Weyl operators,

    <psi,T_n(a,b)psi> = 1 if5^r divides both a and b,
                         0 otherwise.

The actual centered symbol has32 nonzero modes, all with |a|<=1 and |b|<=9, and no (0,0) coefficient. Since5^r>=25, none meets the divisibility condition. Therefore, with W=H_7 tensor span(psi),

    P_W A_N P_W=0                                      (1)

as an exact characteristic-zero matrix identity. The CRT changes the primitive roots, not this divisibility condition.

It remains to check that W contains full eigenspaces of M_N, not merely pieces of larger ones. The separately audited uniform cat-multiplicity theorem says that M_n is simple and, for e even, its eigenvalue set has exactly one partially occupied orbit under multiplication by a primitive cube root omega. That orbit has occupancy one. All other occupied cubic orbits are full.

The exact normalized Gauss trace for n=5^(2r) is Tr(M_n)=1 for every primitive-root power. This follows directly by writing the quadratic trace sum as x=u+5^r v: the inner sum over v kills every u except0, giving5^r before division by sqrt(n)=5^r. Full cubic orbits have zero trace, so the unique partially occupied orbit consists of the eigenvalue1. Consequently omega and omega² are absent from M_n's spectrum.

The three eigenvalues of the seven-dimensional factor are alpha, alpha omega, alpha omega² with multiplicities3,2,2. For a product eigenvalue alpha omega^j in the full tensor product, the n-factor eigenvalue would have to be1,omega,oromega². Only1 exists, and its eigenvector is psi because M_n is simple. Thus W is exactly the direct sum of three COMPLETE M_N eigenspaces of dimensions3,2,2.

Equation(1) makes each of their Hermitian compressions P_lambda A_N P_lambda identically zero. The first-order eigenphase slopes therefore have multiplicities3,2,2 at every even e>=4. The uniform condition “every first-order compression is simple” is false in this actual family.

This does not imply any eigenvalue collision at nonzero coupling. These blocks require a higher discriminant jet. For a block with P A P=0, the second-order effective Hermitian phase matrix is

    H_2=(i/2) P A Q (lambda+M_Q)(lambda-M_Q)^(-1) Q A P,
    Q=I-P, M_Q=QMQ on QH.

It follows by a second-order Schur expansion of exp(itA)M around the eigenvalue lambda. Simplicity of this matrix would resolve that block at order t². No assertion about H_2 is made here.

Exact finite CRT diagnostics at N4375 additionally found six zero size-seven compressions, at both p420001 and p525001. They motivated this obstruction but are not needed for its proof, and their characteristic-zero vanishing is not asserted by this document.
