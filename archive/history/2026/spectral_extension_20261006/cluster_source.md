# First ramified spectral cluster: exact discriminator and a candidate N=175 lift

Status: new candidate argument, not independently audited. Canonical files are untouched. This concerns simplicity of A, not simplicity of the propagator or BGS.

## Exact model and first residue

In the diagonal unitary real-Jacobi gauge, 200A has upper and lower bonds r((x+h)/N), h=2^(-1) modulo N, and diagonal

    200 cos(14 pi x/N)+20 r(x/N)+2 r(x/N) sin(2 pi x/N)-20.

The gauge ratio is (-3+4i)/5, so this is an algebraic similarity despite that ratio not being a unit at the prime i→2 over5. Write q=zeta_N, Q=q^7 and eta=Phi7(q^h)^2. For N=7*5^e, normalize

    T=(200A_real-180I)/eta.

All its entries are integral. With a=v(Q-1)=1/(4*5^(e-1)), eta has valuation2a. The diagonal terms other than 2r sin/eta have positive valuation. For any position x,

    r(q^x)/eta
      = -([x]_Q/[h]_Q)^2 (q^h-1)^2 (q^x+1)^2/(4q^(8x)),
    [x]_Q=(Q^x-1)/(Q-1).

Reduction gives r_x=x² f_x, where

    f_x= -h^(-2)(qbar^h-1)^2(qbar^x+1)^2/(4qbar^(8x)),

qbar has order7, h≡3 modulo5 and h≡4 modulo7. The reduced diagonal is 3r_x(qbar^x-qbar^(-x)). Its coefficients are 35-periodic, and every fifth bond vanishes. Therefore the full residue is 5^(e-1) copies of the same 35-dimensional matrix.

The exact program pure_five_normalized_spectrum.py computes this residue at N35 and175. At35 all seven degree-five chain characteristic polynomials p_j are squarefree and pairwise coprime. At175 each degree25 original-chain polynomial is squarefree, but pairwise gcd degrees are15 or20; the full repeated residue cannot prove simplicity by itself.

## Nonzero offset derivative

Replace the quadratic x² in every r_x of a length-five block by (x+y)², keeping the qbar phases fixed. Let p_j(X,y) be its characteristic polynomial. The program ramified_cluster_derivative.py differentiates the tridiagonal determinant recurrence exactly and verifies

    gcd(p_j(X,0), partial_y p_j(X,0))=1

for all seven blocks over F_(5^6). Together with squarefreeness, every base eigenvalue has a nonzero first offset derivative. This is a bounded algebraic input, not a numerical derivative.

## Candidate consequence: A_175 is simple

Take e=2 and the uniformizer pi=Q-1, so v_pi(5)=20. Separate the actual T into its 35 consecutive length-five diagonal blocks and the bonds between them. Every interblock bond has pi-valuation at least8: at an internal cut u divisible by5, its valuation is twice(v_pi(1-Q^u)-1), and v_pi(1-Q^u)>=5. Actual chain boundaries are exactly zero.

The seven residue block types each occur five times. Index copies of the same type by shifts delta=35k, k=0,...,4. Since

    [35k]_Q ≡ 2k pi^4 mod pi^5,
    q^(35k) ≡1 mod pi^5,

comparison with the unshifted block gives

    p_(j,k)(X) = p_(j,0)(X)
                 +2k pi^4 partial_y p_j(X,0) mod pi^5.

Terms with coefficients20 or200 do not contribute at these orders. The [h]_Q normalization is common to every block. The displayed variation uses the same offset for diagonal positions x and bond positions x+h.

After a finite unramified extension splitting the squarefree residue polynomials, each length-five actual block has five simple integral eigenvalues and a unit eigenvector matrix by elementary simple-root lifting. If lambda is a root of p_j(X,0), the five copies satisfy

    lambda_(j,k)-lambda_(j,0)
      ≡ -2k pi^4 partial_y p_j(lambda,0)/partial_X p_j(lambda,0)
         mod pi^5.

Both derivatives in the ratio are nonzero by the exact gcd checks. Thus distinct copies have eigenvalue gap valuation exactly4, while distinct base eigenvalues have gap valuation0. Every eigenvalue of the block-diagonal part is therefore simple, with all gap valuations at most4.

Unit block diagonalization keeps interblock perturbations divisible by pi^8. Such a perturbation cannot merge these eigenvalues. Explicitly, near any diagonal value d_j in the disc d_j+pi^5 O, the remaining diagonal differences have valuation at most4. Their block plus the pi^8 perturbation is invertible by a convergent geometric series. The scalar Schur equation has constant displacement of valuation at least8 and derivative correction of positive valuation. Successive substitution therefore gives exactly one root in that disc. The175 discs are disjoint and exhaust the polynomial's degree. Hence the full T, and thus A_175, has simple spectrum.

## Uniform continuation still missing

For e>=3 the first residue contains more copies. The first offset derivative separates their first base-five digit, but deeper equal-digit groups need a further controlled Schur/valuation argument. It is not valid to compare only first-order diagonal gaps to the original interblock norm: deeper gaps can be much smaller. No all-e simplicity theorem is asserted here.

The mod2 alternative is genuinely obstructed already at N21 and63: the actual symmetrized4000A residue has three identical reflected pairs of chain polynomials, while its self-reflected odd chain has repeated roots. Exact records are reduced_chain_charpolys_mod2.json. The useful prime5 result depends on the odd diagonal term that separates those reflected chains.
