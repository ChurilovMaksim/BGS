# Quantitative one-mode transversality for the second resonance

This note addresses arbitrary backgrounds containing many Fourier orbits,
without asserting that the second resonance is positive at every nonzero
background. It strengthens the earlier open-dense statement to an explicit
sublevel estimate and a deterministic three-point certificate. The proof is
an elementary quadratic projection argument. It is not a claim of priority,
positive BGS, or a classification of all degenerate symbols.

## Definitions

Let A belong to SL(2,Z) with |Tr A|>2. Write C_A g(x)=g(A^T x), and let g
be real, even, smooth and of mean zero. Put

    h_g={g,C_A g}/(4*pi).

Expand a real even h in cosine modes b_v(x)=2 cos(2*pi*v dot x), using one
representative of each sign pair. The signed A-orbits are the equivalence
classes w=+/-A^j v. Let a_O(h) be the sum of cosine coefficients on orbit O.
Define the real Hilbert-space vector

    Q(g)=sqrt(2)*(a_O(h_g))_O,
    Gamma_A(g)=||Q(g)||_l2^2.

All sums converge absolutely for smooth functions: the Fourier l1 norm of a
Poisson bracket is bounded by weighted Fourier l1 norms of its factors.
The orbit sums are bounded in l1, hence in l2. Q is a continuous homogeneous
quadratic map on this smooth real space.

For a fixed nonzero integer v, let b=b_v and gamma_b=Gamma_A(b). Direct
Fourier calculation gives

    gamma_b=4*pi^2*omega(v,Av)^2>0.                         (1)

Indeed {b_v,b_Av}/(4*pi)=pi*omega(v,Av)*(b_(v-Av)-b_(v+Av)). The two
frequencies are in different signed A-orbits: the invariant quadratic form
q_A(w)=omega(w,Aw) has respective values
q_A(v)*(2-Tr A) and q_A(v)*(2+Tr A), of opposite signs. Also q_A(v) is
nonzero, since otherwise A would have a rational eigenline and a rational
algebraic-unit eigenvalue, necessarily +1 or -1. This proves (1), for either
trace sign.

## A uniform sublevel theorem

**Theorem 1.** For every such background g, every epsilon>0 and every
nonzero mode b,

    Leb{t in R : Gamma_A(g+t*b)<=epsilon*gamma_b}
         <=2*sqrt(2)*epsilon^(1/4).                        (2)

The bound is independent of the number of background modes, their
coefficients, and their frequency radius. It measures length in the
coefficient t of the explicitly normalized mode b. It is not a lower bound
on Gamma_A(g) at a prescribed t.

**Proof.** Quadraticity gives

    Q(g+t*b)=Q(g)+t B(g,b)+t^2 Q(b),
    B(g,b)=Q(g+b)-Q(g)-Q(b).

Project onto the nonzero vector Q(b). The real polynomial

    p(t)=<Q(g+t*b),Q(b)>/||Q(b)||^2=t^2+beta*t+eta

is monic. Cauchy--Schwarz gives Gamma_A(g+t*b)>=gamma_b*p(t)^2.
Consequently the set in (2) is contained in {|p(t)|<=sqrt(epsilon)}.

For any monic real quadratic, completing the square reduces the sublevel
set {|p|<=delta} to {|x^2-a|<=delta}. If a<=delta it is one interval of
length at most 2*sqrt(2*delta), or empty. If a>delta it has total length

    2*(sqrt(a+delta)-sqrt(a-delta))<=2*sqrt(2*delta).

Take delta=sqrt(epsilon). This proves (2). End of proof.

An equivalent unnormalized statement is

    Leb{t : Gamma_A(g+t*b)<=u}
         <=2*sqrt(2)*(u/gamma_b)^(1/4), u>0.

No theorem about arbitrary quartic sublevel sets is imported; the Hilbert
projection retains the useful monic quadratic structure.

## Probabilistic and conditional versions

If T is a real random variable with density bounded by M, then

    P(Gamma_A(g+T*b)<=epsilon*gamma_b)
        <=min(1,2*sqrt(2)*M*epsilon^(1/4)).                 (3)

For a centered Gaussian of standard deviation s>0, this becomes

    min(1, 2*epsilon^(1/4)/(s*sqrt(pi))).                   (4)

For T uniform on [-r,r], r>0, it becomes

    min(1, sqrt(2)*epsilon^(1/4)/r).                       (5)

The same estimates hold conditionally on arbitrarily chosen other Fourier
coefficients, provided the conditional density of the selected coefficient
is bounded by M. Independence of the other modes from one another is not
needed. For a random smooth background independent of T, condition on that
background and integrate (3). In particular Gamma is positive almost surely
under this one continuously distributed nondegenerate mode.

These statements concern a classical variance functional. They do not imply
random-matrix eigenvalue statistics for the perturbed quantum propagator.

## A deterministic three-point nondegeneracy certificate

**Theorem 2.** For every background g and every r>0,

    max{Gamma_A(g-r*b), Gamma_A(g), Gamma_A(g+r*b)}
        >=(r^4/4)*gamma_b.                                 (6)

If Gamma_A(g)=0, the stronger conclusion holds:

    max{Gamma_A(g-r*b), Gamma_A(g+r*b)}>=r^4*gamma_b.          (7)

**Proof.** For the monic quadratic p above,

    p(r)+p(-r)-2p(0)=2*r^2.

At least one of the three absolute values is at least r^2/2. The projection
bound proves (6). If Gamma_A(g)=0 then Q(g)=0 and

    Q(g+r*b)+Q(g-r*b)=2*r^2 Q(b).

The triangle inequality shows that at least one of their norms is at least
r^2 ||Q(b)||. Squaring proves (7). End of proof.

Thus the nondegenerate set is not merely dense: any prescribed amplitude
radius in one fixed Fourier direction contains one of three explicit choices
with the displayed variance bound. No root search over an unknown quartic
is needed. The bound is on the variance, not on microscopic spectral statistics.

## Compatibility with the flat smooth branch

The support-separated smooth construction has an infinite-dimensional set
with Gamma=0, and its Fourier approximants can have positive Gamma smaller
than every inverse power of their bandwidth. Neither fact contradicts (2)
or (6). Those inequalities allow a thin set of near-degenerate values and
permit changing one coefficient; they do not give a positive lower bound
uniform over all coefficients in a Fourier box.

The finite-polynomial several-orbit question is already closed by
`extremal_resonance_nondegeneracy.md`: every nonconstant real trigonometric
polynomial has positive Gamma. The 22 September project proof in
`finite_orbit_resonance_rigidity.md` further covers every nonconstant real
smooth observable supported on finitely many signed A-orbits, and all finite
lag combinations. Arbitrary real-analytic support on infinitely many orbit
families remains open. Pointwise nonvanishing, genericity, and the bounds
above are not substitutes for that remaining all-members theorem.
