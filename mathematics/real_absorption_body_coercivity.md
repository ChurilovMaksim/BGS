# Exact real scalar absorption bound

7 October 2026. Separate ordinary bosonic-body addendum. No edit to the frozen scalar report or matrix-block extension. Independent review pending.

## 1. Exact matrix inequality and sharpness

Let A be a complex d by d matrix with spectral radius at most one, and let 0<=alpha<=1 be real. Then

|det(I-alpha A)| >= ((1+alpha)/2)^d |det(I-A)|.                 (A1)

In particular, (A1) applies to every operator-norm contraction; normality is not required. For d>=1 and alpha<1 its uniform constant is sharp, attained by A=-I. If strict contractions are required, A=-r I, r increasing to one, approaches equality. At alpha=1 it is an identity.

Proof. For any complex lambda with |lambda|<=1, direct expansion gives

4|1-alpha lambda|^2-(1+alpha)^2|1-lambda|^2
=(1-alpha)[(1+3alpha)(1-|lambda|^2)
           +2(1-alpha)(1+Re lambda)] >=0.

Thus |1-alpha lambda|>=((1+alpha)/2)|1-lambda|. Multiply this inequality over all d eigenvalues counted with algebraic multiplicity, using det(I-alpha A)=product_j(1-alpha lambda_j). This argument also covers lambda=1 without division. It does not require diagonalizability.

Equivalently, when lambda!=1,

Re[(1-alpha lambda)/(1-lambda)]
=alpha+(1-alpha)Re[1/(1-lambda)] >=(1+alpha)/2.

This is an elementary finite-dimensional proof with no new external theorem dependency.

## 2. Exact implication for the specified bosonic body

For an N-site field with ordinary bosonic block size k, set d=Nk, U_k=U tensor I_k, and let Z=diag(Z_1,...,Z_N) with every Z_j a strict contraction. Define

A=U_k Z U_k* Z*,
S_alpha(Z)=log|det(I-alpha A)|-log det(I-ZZ*).

Then ||A||<1, so every determinant in this definition is nonzero and the real logarithms are well-defined. Applying (A1) gives

S_alpha(Z)>=S_1(Z)+Nk log((1+alpha)/2).                       (A2)

For alpha=exp(-s/N), with s>=0 real and N>=1,

Nk log((1+exp(-s/N))/2)
=-ks/2+Nk logcosh(s/(2N)) >=-ks/2.

Consequently

**S_alpha(Z)>=S_1(Z)-ks/2.**                                 (A3)

The finer bound is (A2) with the displayed logcosh term retained. The scale convention here is exactly alpha=exp(-s/N); a different physical regulator convention must be translated rather than silently replacing s or a factor of two.

Whenever the centered bare-body coercivity theorem applies, with

c=1/[2(1+sqrt(C-1)/(1-rho))^2],
H(Z)=-log det(I-ZZ*),

one obtains

S_alpha(Z)>=c H(Z)-ks/2,
exp(-S_alpha(Z))<=exp(ks/2) exp(-c H(Z)).                     (A4)

The scalar k=1 statement depends on the independently audited scalar report. The k>1 coercivity statement additionally depends on the separately reviewed status of matrix_block_extension.md; (A1)--(A3) themselves do not depend on that extension.

For the scalar field, (A3) may be applied before the common Mobius change of coordinates. If z is an arbitrary strict disk tuple and w is its unique centered tuple from report.md, the exact bare identity S_1(z)=S_1(w) implies

S_alpha(z)>=c H(w)-s/2.                                      (A5)

No invariance of S_alpha under Mobius transformations is asserted. Generally the real absorption term breaks that bare invariance; (A5) follows by bounding first and using invariance only for S_1.

## 3. Actual-family and auxiliary-measure consequences

If the separate actual_constants_addendum.md is accepted, then for all sufficiently large odd N the unchanged actual scalar family may take c=1/50. The threshold remains noneffective, and for alpha=exp(-s/N),

S_(alpha,U_N)(Z)>=H(Z)/50-s/2

on the centered scalar slice. For an uncentered field use its centered H as in (A5).

For the explicitly auxiliary centered Lebesgue integral in radial_translation.md, the tail bound is multiplied by at most exp(s/2):

integral_(Omega_N,H>=L) exp(-S_alpha) product_(j<N)d^2z_j
 <=exp(s/2-cL/2)[pi/(1+c/2)]^(N-1).

This concerns that exact positive scalar measure, without a source or collective-coordinate factor. It supplies neither a normalization lower bound nor a full phase-integral conclusion.

## 4. Boundary of the conclusion

This is real **scalar** absorption multiplying the entire matrix A. It is not a theorem for arbitrary complex source matrices, nonuniform absorption matrices, differentiated generating functions, or the full supermeasure. No identification of alpha with every source in the cited SUSY representation is asserted.

The same constant does not extend to a generic complex alpha by replacing alpha with |alpha|. For the auxiliary scalar contraction A=-3i/4 and alpha=i/2,

|1-alpha A|=5/8 < (1+|alpha|)|1-A|/2=15/16.

This is a counterexample only to that generic-contraction extension; it is not claimed to be an actual quantum-phase-field counterexample.

The lemma controls body magnitudes, not source derivatives or inverse factors produced by Grassmann integration. Super-Berezinian and boundary terms, all-order signed cancellation, actual integrated tails, the full balanced radial/torus comparison, deterministic off-charge cancellation and BGS remain open.
