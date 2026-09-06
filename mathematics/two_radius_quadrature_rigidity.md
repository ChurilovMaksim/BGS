# Two-radius rigidity and exact quadrature orthogonality

Status: project theorems with complete elementary proofs. External priority and full Lean formalization are not established. The word spectrum below refers to a covariance symbol, not quantum eigenphases.

## 1. An elementary polynomial rigidity theorem

Let P(z)=sum_(j=0)^n c_j z^j be a nonzero complex polynomial. Write P=A+iB where A and B have real coefficients. For rho>0 define

    N_rho(theta)=|A(rho exp(i theta))|^2+|B(rho exp(i theta))|^2.

**Theorem.** If N_rho is constant in theta at two distinct positive radii, P has at most two nonzero coefficients. If there are two, their complex phases are orthogonal:

    Re(c_j conjugate(c_k))=0.

Conversely, these conditions make N_rho constant at every positive radius. The result holds for Laurent polynomials after removing a monomial factor.

Proof. Remove initial zero coefficients, so c_0,c_n are nonzero. Put v_j=(Re c_j,Im c_j) in R^2. Constancy at rho means

    sum_(j=0)^(n-l) rho^(2j) (v_j dot v_(j+l))=0,
        1<=l<=n.                                           (1)

The top equation gives v_0 perpendicular to v_n. For k=1,...,floor(n/2), use l=n-k. Inductively the intermediate terms vanish: v_j is parallel to v_0 and v_(n-k+j) parallel to v_n for 0<j<k. Hence

    v_0 dot v_(n-k)+rho^(2k) v_k dot v_n=0.

The two distinct radii force both terms to vanish separately. Thus v_k is parallel to v_0 and v_(n-k) parallel to v_n. If n is even the middle coefficient is zero. All coefficients in the left half are now parallel to v_0, and all in the right half to v_n.

Let p be the last nonzero index in the left half and q the first nonzero index in the right half. If p>n-q, the lag-p equation in (1) has the single nonzero term v_0 dot v_p, a contradiction. If p<n-q the symmetric argument applies to the right half. Therefore p=n-q=k. If k>0, the lag-k equation reduces to

    v_0 dot v_k+rho^(2q) v_q dot v_n=0.

Again two radii force both nonzero terms to vanish, a contradiction. Thus k=0 and only the two endpoint coefficients survive. The converse follows directly from (1).

One radius is insufficient: A(z)=1+2z-z^2 and B(z)=1+z^2 have N_1=8, but N_2 is not constant.

## 2. Application to a single signed hyperbolic orbit

Let A0 in SL(2,Z) be hyperbolic, C f=f composed with A0^T, lambda>1 its expanding eigenvalue in modulus, and v a nonzero integer vector. Consider a real Fourier polynomial

    g=sum_j (c_j e_(A0^j v)+conjugate(c_j)e_(-A0^j v)).

Use eigen-covectors xi,eta normalized by det(u,w)=xi(u)eta(w)-eta(u)xi(w). The high-lag covariance symbol for the normalized brackets lambda^(-r){g,C^r g}/(4 pi) is

    F_g(theta)=4 pi^2 xi(v)^2 eta(v)^2
               N_lambda(theta)N_(lambda^(-1))(theta).       (2)

Both factors are finite real nonnegative Laurent polynomials. Their product is a positive constant if and only if each factor is constant: a product which is a unit in the Laurent polynomial ring has unit factors, and an everywhere real nonnegative Laurent monomial is constant. The two-radius theorem therefore proves:

**Corollary.** The tail symbol F_g is constant if and only if g contains one signed Fourier mode, or exactly two time-separated signed modes whose complex coefficients have phase difference pi/2 modulo pi.

Including both oriented A0-orbits is essential in (2). A criterion using only |P|^2 for complex coefficients would miss the cancellation between opposite orientations.

## 3. Exact diagonal covariance, not only a constant limiting symbol

Write the two coefficients as c_0=a exp(i phi), c_d=i b exp(i phi), with a,b real, d>=1. Put

    D_r=det(v,A0^r v), h_r={g,C^r g}/(4 pi),
    Gamma_(r,s)=<J(h_r),J(h_s)>,

where J collects oriented Fourier-orbit sums. Then, for all r,s>d,

    Gamma_(r,s)=0  if r!=s,

and

    Gamma_(r,r)=4 pi^2 [(a^4+b^4)D_r^2
                    +a^2 b^2(D_(r+d)^2+D_(r-d)^2)].         (3)

Proof. The same-sign pair channel has coefficient sequence

    A_0=exp(2i phi)(a^2-b^2), A_d=A_(-d)=i ab exp(2i phi),

whereas the opposite-sign channel has

    B_0=a^2+b^2, B_d=-i ab, B_(-d)=i ab.

Opposite oriented channels are complex conjugates. Distinct positive pair gaps and signs belong to distinct oriented A0-orbits, as seen from det(w,A0w) at w=v plus or minus A0^k v. Therefore a covariance can overlap only at lag difference d or 2d. At difference d each contribution is purely imaginary and cancels with the conjugate channel. At difference 2d the same-sign and opposite-sign real contributions cancel. On the diagonal the squared amplitudes give (3).

The identity

    D_(r+d)^2+D_(r-d)^2=(tr(A0^d)^2-2)D_r^2+2D_d^2

also yields

    Gamma_(r,r)=4 pi^2 [((a^2-b^2)^2+a^2b^2 tr(A0^d)^2)D_r^2
                         +2a^2b^2 D_d^2].                 (4)

For a=b=1,d=1 this is 4 pi^2[tr(A0)^2 D_r^2+2D_1^2]. Both trace signs are included. The finite coefficients and their exponential normalization are exact; no Gaussian or independence claim follows from diagonal covariance.

## 4. Verification boundary

computations/verification/two_radius_rigidity.py exhaustively checks a stated finite coefficient alphabet at two radii, retains the three-coefficient one-radius counterexample, and computes the Gram matrices by independent exact Gaussian-rational Fourier multiplication and full orbit canonicalization. These finite controls do not replace the arbitrary-degree rigidity proof above. Neither a flat covariance symbol nor pairwise orthogonality proves random-matrix local statistics.
