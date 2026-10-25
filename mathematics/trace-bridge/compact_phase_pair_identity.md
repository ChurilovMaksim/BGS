# A compact color-one pair projector and finite-size source identity

7 October 2026. Author derivation, independent review pending. Canonical read-only base: d37c92e563d10d25bb1d6ab85bedffc1f160f773. No canonical edits or publication. This is a finite-dimensional identity, not an annealed CUE theorem or deterministic BGS theorem.

## 1. Exact target and first uncertain implication

For a fixed N by N unitary U and independent uniform phases D, let

G_U(a,b;c,d) = E_D det(I-cDU) det(I-dU*D*) / [det(I-aDU) det(I-bU*D*)],

where |a|,|b|<1 and c,d are arbitrary complex numbers. The immediate objective is an exact full-source integral that can be tensorized without separately integrating divergent bulk/surface pieces. The subsequent unresolved objective is the microscopic asymptotic at a=b=exp(-s/N), after mixed numerator-source differentiation and N^-2 normalization.

The first uncertain implication was whether an alternative compact functional reproducing the four color-neutral coherent-section families remains valid for the coupled N-site superdeterminant. The proof below resolves the finite-size step by its local coherent-state projector. It does not justify a positive-measure saddle approximation.

## 2. Variables and the compact local functional

Use

Z = [[z,alpha],[beta,w]],   Ztilde = [[zbar,gamma],[delta,-wbar]],

with independent odd variables ordered gamma,beta,alpha,delta, so the top monomial is gamma beta alpha delta. Coefficient extraction always refers to this order. The commuting pairs (z,zbar) and (w,wbar) are first independent algebraic coordinates, later restricted to complex conjugates where indicated.

For a superfunction F define its body F_0, and denote its coefficients of gamma beta and alpha delta by F_gb and F_ad. Define

C[F] = integral_{|z|=1} [ F_0(z,zbar,0,0) + partial_w partial_wbar F_0(z,zbar,0,0) ] dtheta/(2pi)
       - integral_{|z|<1} [ F_gb(z,zbar,0,0) + F_ad(z,zbar,0,0) ] d^2z/pi.

Other sites, if present, are treated as external parameters. All derivatives/extractions are performed before setting the variables to zero. This is a sum of four bounded-domain coefficient functionals, not an invariant positive measure on the supermatrix chart. Its domain for the theorem is the coherent-section span and its holomorphic trace-class completion described below; no equality on arbitrary smooth superfunctions is asserted.

## 3. Local reproducing proof

The color-neutral oscillator space has four families of sections and duals. In the present conventions they can be taken as

A_k = z^k,                   Atilde_k = zbar^k,                       k>=0;
B_k = sqrt(k) z^(k-1) alpha,  Btilde_k = -sqrt(k) delta zbar^(k-1),    k>=1;
C_k = sqrt(k) z^(k-1) beta,   Ctilde_k = sqrt(k) gamma zbar^(k-1),     k>=1;
D_l = z^l w - l z^(l-1) alpha beta,
Dtilde_l = zbar^l wbar + l zbar^(l-1) gamma delta,                      l>=0.

At l=0 the derivative terms are omitted. Their diagonal products are precisely the four families checked independently against the corrected Zirnbauer functional. The literal index typo in source (4.43)-(4.45) is not used; Table 1's actual dual pairing is used.

The A and D diagonal pairings are unit-circle monomial inner products. For D, only the w wbar body coefficient survives C, and its value is |z|^(2l). The B and C diagonal products have coefficient -k |z|^(2k-2) in alpha delta or gamma beta, respectively; their C integral is k integral_0^1 x^(k-1) dx =1. Cross-family pairings vanish by odd or w extraction. Within a family, different indices vanish by angular integration. Therefore C[f_v e_w]=delta_vw for all four families and all indices.

These are the neutral coherent-state sections from Zirnbauer, Color-Flavor Transformation Revisited, arXiv:2109.10272v1, Table 1 and (4.36)-(4.40), printed pp.31-32. Thus C represents the same neutral Fock-space projector as the source's corrected bulk-plus-surface functional, on the stated coherent-section domain. The result is an elementary alternate realization of that projector; no priority claim is made.

The proof also gives an elementary way to see the compact measures: pure boson and paired-fermion sectors have Hardy-circle norms, while the two mixed sectors have Bergman-disk norms. The fourth family's Grassmann derivative is needed in the coherent kernel even though C does not itself extract its fourth-degree coefficient.

## 4. Tensorized full-source theorem

Let Z and Ztilde now be block diagonal in the site labels, with the local 1|1 blocks above. On site times flavor space, set A=diag(a,c), B=diag(b,d). The ordinary unitary U acts only on the site label. Then

G_U(a,b;c,d) = (product_{i=1}^N C_i) SDet^-1[ I - Ztilde (U tensor A) Z (U* tensor B) ].     (T)

Equivalently, expand the right side into 4^N terms indexed by a local choice of the two circle coefficient functionals and two disk coefficient functionals. Each term is an ordinary compact integral of a finite coefficient of the displayed inverse Berezinian. This prescription includes the complete local boundary correction in a reorganized form; there is no plane cutoff to remove and no separately divergent summand.

Proof by the neutral projector. Represent each retarded ratio by bosonic and fermionic Fock second quantization, and the advanced ratio by its independent counterpart. The independent coordinate-phase integration projects onto equal retarded/advanced total occupation at each site. At one site, the equal-occupation subspace has exactly the four coherent-section families in Section 3. Inserting C_i resolves that projector exactly. Multiplying the local resolutions and taking the remaining Gaussian/oscillator contraction gives the superdeterminant in (T), by the usual finite boson/fermion Gaussian contraction. The sources are placed consistently with (U tensor A) Z (U* tensor B); N=1 reduces to SDet^-1(I-Ztilde A Z B).

Convergence and source derivatives. The bosonic body is det[I-ab Zbar U Z U*]^-1, where every |z_i|<=1. The matrix Zbar U Z U* has norm at most one, so this body denominator does not vanish for |ab|<1. Expansion of the finite odd algebra introduces only finitely many further powers of that inverse body matrix. All numerator-source dependence is polynomial. Hence every one of the finitely many compact coefficient integrals exists absolutely, and all source derivatives are allowed locally uniformly on |ab|<1. The oscillator/Fourier construction initially applies with |a|,|b|<1, and polynomial c,d; the resulting compact expression continues in the product ab where appropriate. Uniformity is for fixed N on compact source subsets, not a dimension-uniform microscopic estimate.

For a direct rigorous exchange argument one can first restrict the oscillator occupation to a finite cutoff, use the finite-span projector identity, and then use trace-norm convergence of second quantization when |a|,|b|<1. Polynomial fermion factors cannot destroy this convergence. The finite compact coefficient integral has the same power series near zero; analyticity on the source domain extends the equality. This avoids separately bounding the original noncompact chart expressions.

## 5. Exact checks

For N=1, write q=ab, r=cd, u=bc, v=ad and x=|z|^2. The relevant coefficients of the source insertion are

F_0 = (1+r|w|^2)/(1-qx),
F_gb = u/(1-qx)^2,
F_ad = v/(1-qx)^2.

Thus

C[F] = (1+r)/(1-q) - (u+v) integral_0^1 (1-qx)^-2 dx
     = (1+r-u-v)/(1-q)
     = 1+(a-c)(b-d)/(1-ab).

This agrees with the independently verified common-cutoff bulk-plus-surface result for every allowed source.

The executable check_compact_n2.py computes the inverse superdeterminant formal expansion for U=[[3/5,4/5],[-4/5,3/5]] using an independent sparse exterior/polynomial algebra with exact rational arithmetic. With a=b=t, numerator sources c*t,d*t, it applies product C_i to all coefficients through t^6 and compares them with a separate ordinary determinant ratio expansion followed by exact U(1)^2 Fourier projection. Every coefficient passes, including its full polynomial dependence on c,d. This is a finite implementation check of the coupled orientation and signs, not the proof for arbitrary N.

## 6. Boundary and relevance to global coercivity

(T) supplies a correct finite-N differentiated source identity with compact, absolutely convergent summands. It does not make their absolute sum small. Even for N=1, the circle and disk summands have opposite signs and source-dependent poles. With a=c,b=d, their sum is exactly one only after cancellation.

The functional C is not the locally flat invariant supermeasure times SDet(I-Ztilde Z). Its support includes |z|=1, and some terms evaluate only selected odd coefficients. Therefore the existing centered scalar/body coercivity inequality cannot simply be inserted into each summand of (T): the vanishing local factor that drives the interior action is not present as a positive density in this realization. A controlled cancellation or an admissible change of this entire compact functional is still required to exploit that estimate.

The four-state local projector also cannot be collapsed to the pure-boson torus functional: with fermions, fixed coordinate-occupation spaces have multiplicity greater than one. A commutator-torus trace gives a Hilbert-Schmidt norm of each weight block, while the original phase-average ratio involves products of its traces. The separate Schur-radial worker supplies that exact multiplicity obstruction. It does not invalidate the four-state identity (T).
