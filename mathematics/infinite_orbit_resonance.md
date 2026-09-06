# Resonance independence on one infinite hyperbolic orbit

Status: self-contained project proof. This extends finite-support nondegeneracy to an explicitly specified infinite-support class. It does not cover arbitrary unions of infinitely many dynamical Fourier orbits and does not establish BGS universality.

## 1. The observable and its correlations

Let A in SL(2,Z) be hyperbolic, C f=f composed with A^T, and v!=0 an integer vector. Let

    g=sum_(j in Z)[c_j e_(A^j v)+conjugate(c_j)e_(-A^j v)]

be real, with M1(g)<infinity. Constants may be added without effect. The two signed A-orbits are distinct. In particular (c_j) is absolutely summable. Put

    S_n=sum_j c_j c_(j+n),
    C_n=sum_j c_j conjugate(c_(j+n)),
    D_k=det(v,A^k v), k>=1.

Then S_(-n)=S_n and C_(-n)=conjugate(C_n), and both correlation sequences are absolutely summable. Every D_k is nonzero.

For h_r={g,C^r g}/(4 pi), the oriented orbit sums on the two positive-gap orbit types are exactly

    J(h_r)_[v+A^k v]=-pi D_k[S_(k-r)-S_(k+r)],
    J(h_r)_[v-A^k v]= pi D_k[C_(k-r)-C_(k+r)].              (1)

The negative oriented orbits give the complex conjugates. Formula (1) follows by expanding the Fourier bracket, separating positive and negative pair gaps, and translating the lower index to zero. Absolute M1 bounds justify all rearrangements.

Distinct positive gaps and the two signs belong to distinct oriented orbits. The invariant det(w,Aw) takes values det(v,Av)[2 plus or minus tr(A^k)], and absolute traces strictly increase with positive k. A vector and its negative cannot lie on the same A-orbit for a hyperbolic matrix. Therefore (1) accounts for all contributions without identifying different output orbits.

## 2. Exact quadratic form

For a finite real sequence a_1,...,a_m define

    A_k=sum_r a_r[S_(k-r)-S_(k+r)],
    B_k=sum_r a_r[C_(k-r)-C_(k+r)].

The dynamical variance is exactly

    V_A(sum_r a_r h_r)
       =2 pi^2 sum_(k>=1) D_k^2 (|A_k|^2+|B_k|^2).         (2)

The series converges under the M1 hypothesis. One way to see this without estimating each term separately is to expand the original absolutely convergent Fourier bracket and use the bounded orbit-sum map from Fourier l1 to l2.

## 3. Strict independence for every nonzero observable in this class

**Theorem.** If g is nonzero, every finite nonzero real sequence (a_r) makes (2) strictly positive. Hence all classes [h_r], r>=1, are linearly independent modulo L2 coboundaries, despite the infinite Fourier support.

Proof. Suppose (2) is zero. Then B_k=0 for every positive k. Since a_r is real, B_(-k)=-conjugate(B_k), so only B_0 could remain. Let

    P(exp(i theta))=sum_j c_j exp(i j theta),
    w(theta)=|P(exp(i theta))|^2,
    s_a(theta)=sum_r a_r sin(r theta).

The uniformly convergent correlation Fourier series gives

    sum_(k in Z) B_k exp(-i k theta)=-2i s_a(theta)w(theta).

The left side is constant. At theta=0 the right side is zero, so that constant is zero. The nonzero continuous function P has nonzero modulus on an open interval. On that interval s_a vanishes. A trigonometric polynomial which vanishes on an interval is identically zero, so every a_r is zero, a contradiction.

For complex linear combinations, separate real and imaginary parts: the h_r are real observables and conjugate oriented orbit sums give the corresponding two real relations. A nonzero orbit sum precludes an L2 coboundary by the Fourier coefficient difference equation on that orbit. No converse for arbitrary M1 observables is assumed.

## 4. A simple quantitative consequence

Since |D_k|>=|D_1|, Parseval in (2) gives

    V_A(sum a_r h_r)
        >=4 pi^2 D_1^2 Var_theta[s_a(theta)w(theta)].         (3)

Here the variance is for normalized uniform theta, and includes the generally nonzero mean when the coefficients c_j are complex.

If the even part w_e(theta)=[w(theta)+w(-theta)]/2 is bounded below by beta>0, the odd part s_a w_e has zero mean and is L2-orthogonal to the even part s_a(w-w_e). Thus

    V_A(sum a_r h_r)>=2 pi^2 D_1^2 beta^2 sum_r a_r^2.       (4)

This bound is for the unnormalized lag classes. It must not be mistaken for a lower bound on the exponentially normalized lambda^(-r) classes.

## 5. Boundary

The proof uses the exact single-orbit correlation structure, not a maximum of an infinite Fourier support. It is compatible with smooth separated-support counterexamples involving many Fourier orbits. It also does not assert independence or Gaussianity of the observables themselves. Its conclusion is strict positivity of their finite dynamical covariance matrices.
