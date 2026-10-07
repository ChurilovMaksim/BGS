# Fixed-word freeness of the literal kick and cat factors

Author proof candidate, 7 October 2026. Exact model inputs frozen in
`inputs/`; source hashes and the read-only base are in `manifest.json`.
No canonical BGS edit or publication. The requested signed microscopic
target TRACE-005 remains open.

## F1. Statement and precise sense of freeness

Keep the actual odd-dimensional matrices

    Q_N=exp(i tau N A_N),     U_N=Q_N M_N,     tau=10^(-80),

with the centered raw Weyl generator A_N, its corrected physical midpoint
symbol g, and S=[[3,4],[2,3]]. Let F_2=<q,m> be the abstract free group on
two generators. For a finite group word w, write

    W_N(w)=w(Q_N,M_N),     tr_N(X)=N^(-1)Tr(X).

Here inverse letters mean unitary adjoints. Every word and all exponents
in the theorem are fixed independently of N.

**Theorem F.** Through all odd N tending to infinity,

    tr_N(W_N(w)) -> 1 if w is the identity in F_2,
                   0 otherwise.                             (F1)

Equivalently, the deterministic pair (Q_N,M_N) converges in normalized
noncommutative *-moments to two free Haar unitaries, or to the canonical
generators in the free-group algebra with its canonical trace. This is a
description of its limiting moments, not replacement of the actual matrices
by a random ensemble. No strong/operator-norm freeness is asserted.

Every fixed nontrivial word W_N(w) therefore has an asymptotically uniform
macroscopic eigenphase measure, since w^ell is nontrivial for every integer
ell!=0 and its ell-th moment is covered by F1.

**Relative-word corollary.** For any two distinct fixed words v,w in F_2,
the empirical singular-value law of W_N(v)-zW_N(w) tends, uniformly over
|z|=1, to

    F(s)=(2/pi)arcsin(s/2),      0<=s<=2.                     (F2)

For r_N/N->rho in [0,1), the best rank-r_N correction has limiting squared
normalized HS residual

    2(1-rho)-(2/pi)sin(pi rho),                               (F3)

and limiting operator-norm residual

    2cos(pi rho/2),                                          (F4)

uniformly in z. In particular every rank-o(N) correction leaves limits
sqrt(2) and 2. Taking v=(qm)^k, w=m^k gives this conclusion for
U_N^k versus zM_N^k, for every fixed integer k!=0.

## F2. A faithful derivative representation at one exact equilibrium

Let Phi=Phi_g^(kappa), where kappa=tau/(2pi). The exact physical symbol is

    g(q,p)=cos(14pi q)+r(q)/10+r(q)sin(2pi q)/100-1/10
           +r(q+1/2)cos(2pi p-alpha)/100,
    r(q)=(1-cos(14pi q))(1+cos(2pi q)),
    cos(alpha)=-3/5, sin(alpha)=4/5.

Both S and Phi fix P=(0,0). Direct differentiation, retaining the forced
ordinary half-shift, gives

    dg(P)=0,
    Hess g(P)=diag(-(19606/125)pi^2,0).

Thus, with E=E21=[[0,0],[1,0]],

    D Phi(P)=T(x):=I+xE,
    x=(9803/125)tau*pi !=0.                                  (F5)

The nilpotent linearization makes F5 exact, not an approximation in tau.
Since tau is the prescribed nonzero rational, x is transcendental. Only
transcendence of pi is used: it follows from the registered Hermite-Lindemann
corollary, since algebraicity of nonzero i*pi would force exp(i*pi)=-1
to be transcendental. This invokes no quantitative transcendence estimate.

We prove that S and T(x) freely generate a free group in SL(2,R). A
nontrivial word is conjugate either to a nonzero pure power S^a or T(x)^b,
or to a cyclically reduced alternating word

    C(x)=S^(a_1)T(x)^(b_1)...S^(a_k)T(x)^(b_k),              (F6)

where k>=1 and all a_j,b_j are nonzero integers. This is elementary free
reduction and cyclic reduction in Z*Z. For the alternating case,
T(x)^b=I+b x E even for negative integers b. Therefore Tr C(x) is an
integer-coefficient polynomial of degree at most k. Its coefficient of
x^k is

    (product_j b_j) Tr(S^(a_1)E...S^(a_k)E)
      =(product_j b_j)(product_j (S^(a_j))_12).               (F7)

The identity E A E=A_12 E proves the last equality, including k=1.
Every displayed off-diagonal entry is nonzero: S has eigenvalues
lambda=3+2sqrt(2) and lambda^(-1), and

    (S^a)_12=(lambda^a-lambda^(-a))/sqrt(2) !=0  for a!=0.

In particular (F7) is a nonzero integer. Hence Tr C(x) has exact degree k
and takes a transcendental value at the transcendental x. (A nonconstant
algebraic-coefficient polynomial cannot take an algebraic value at a
transcendental argument.) It is therefore not the trace 2 of the identity.
The pure powers are also nonidentity: S is hyperbolic and T(x)^b=I+b x E.
Conjugation does not turn a nonidentity matrix into the identity.
Thus every abstract nontrivial word has nonidentity derivative matrix.

Derivative at the common fixed point is a group homomorphism. It follows
that S and Phi freely generate a group of real-analytic torus maps.
Every nontrivial word in them is a nonidentity analytic torus map. This
argument also applies after inverting either generator or reversing a
word, which will account for the Egorov conventions below.

## F3. Analytic coincidence sets have area zero

For a nonidentity real-analytic torus map F, take the four embedding
coordinates a_j=cos(2pi q),sin(2pi q),cos(2pi p),sin(2pi p) and set

    f_F(y)=sum_j [a_j(F(y))-a_j(y)]^2.

This is a nonzero real-analytic function. Its zero set, exactly Fix(F),
has area zero by the analytic zero-set theorem. In this elementary
dimension-two setting, the fact follows locally by the one-variable
identity theorem, analytic expansion in one coordinate, and Fubini;
a countable analytic atlas covers the torus. We need only qualitative
zero area for one fixed map at a time, not a uniform finite-type bound.

Consequently every nontrivial word in S and Phi has area-zero fixed set.
The common equilibrium P is allowed: one fixed point is a zero-area set.
No assumption of free action at every point is made.

## F4. Exact quantization and fixed-word Egorov

The unchanged Weyl quantization obeys, for every fixed smooth a,

    Q_N* Op_N(a) Q_N = Op_N(a composed with Phi^(-1))+o_op(1),
    M_N* Op_N(a) M_N = Op_N(a composed with S^(-1)).            (F8)

The first follows by the actual finite-Fourier sine-commutator estimate
and Duhamel over the fixed Hamiltonian time kappa. The second is the exact
metaplectic Egorov identity, including ordinary midpoint alias signs.
Both are maintained inputs of FM-016/FM-018, restated and derived at the
needed precision in `literal_kick_phase_law.md`, Sections 3-4.

If K_N*Op(a)K_N=Op(a composed with F_K)+o(1) and likewise for L_N,
then

    (K_N L_N)* Op(a) (K_N L_N)
        = Op(a composed with F_K composed with F_L)+o(1).     (F9)

All composed symbols are fixed smooth symbols. Induction therefore gives
fixed-word Egorov for W_N(w), with F_w equal to the same ordered word
evaluated at Phi^(-1),S^(-1). For inverse letters use the inverse maps.
By Section F2, F_w is not the identity whenever w is nontrivial.

The normalized trace overlap lemma of FM-016 now applies to W_N(w) and
the identity quantizer: its maps F_w and Id coincide only on the area-zero
fixed set from F3. It gives tr_N(W_N(w))->0. Its proof uses only the
standard torus Weyl product/HS laws, a smooth cutoff away from that fixed
set, cyclicity, and HS Cauchy-Schwarz. The cutoff shrinks only after the
N limit. It is restated explicitly in the companion note so no long-time
trace formula or spectral conclusion is hidden here.

If w is the abstract identity, ordinary cancellation of each inverse pair
makes W_N(w)=I exactly, not merely semiclassically. This proves F1.

## F5. Relative words, empirical phases, and rank residuals

Every fixed nontrivial free-group element has infinite order. Applying F1
to w^ell for all fixed ell!=0 shows that W_N(w)'s eigenphase measures have
all nonzero Fourier moments tending to zero. Fourier approximation gives
weak convergence to uniform probability on the circle.

For distinct v,w, the relative word v w^(-1) is nontrivial. Right multiply
W_N(v)-zW_N(w) by W_N(w)* to obtain W_N(vw^(-1))-zI. The normal matrix
W_N(vw^(-1)) has uniformly distributed eigenphases. Uniform circular-arc
discrepancy follows from its continuous limiting measure. Its chord
singular values therefore satisfy F2 uniformly over scalar phases z.

The finite-dimensional singular-value variational principle identifies
the best rank-r residual with the surviving N-r smallest singular values.
Their limiting quantile is 2sin(pi u/2). Integrating its square up to
1-rho gives F3; taking its endpoint gives F4. The detailed uniform-arc
and endpoint arguments are in companion Sections 5 and K11-K12.

## F6. What is excluded, and the exact remaining limitation

The theorem excludes every fixed nontrivial word relation or approximate
scalar return in the actual quantum factors, even along an infinite odd-N
subsequence and even after rank-o(N) corrections. In particular it removes
direct scalar-cat rephasing as an explanation of a putative literal BGS
failure. No operator, coupling, quantization, or arithmetic dimension has
been changed, and no average in N or tau is taken.

It is only fixed-word *-moment information. The constants and N thresholds
may depend arbitrarily badly on the word. It does not cover logarithmically
growing Pell periods, Heisenberg words/powers, microscopic clusters, full
complex spectral commutants, strong convergence, or free-probability
predictions for microscopic spectra. In particular it does not substitute
Haar randomness for U_N, nor estimate the signed factorial TRACE-005 sum.

The group-theoretic leading-coefficient argument and its explicit physical
application are newly written here. The actual symbol/Hessian is inherited
from FM-001; fixed-time quantization and trace overlap are inherited from
FM-016/FM-018; Hermite-Lindemann is the registered EXT-POPESCU-2023 input.
No external priority claim or assertion of an external referee is made.
