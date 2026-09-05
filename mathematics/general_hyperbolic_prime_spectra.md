---
title: "Short-period quantum spectra from Weyl covariance, without a split-torus assumption"
author: "WoW research programme"
date: "5 September 2026"
---

# Status and relationship to the preceding work

This note proves an extension of the arithmetic input used by the all-orders
conjugacy construction. It does not assume the Gaussian-average theorem,
Egorov estimates beyond one step, primality of the Hilbert-space dimension,
or diagonalizability over the residue ring. The key finite theorem uses only
Weyl covariance, a fixed-point count, parity, and elementary integer character
multiplicities. This is a project proof, not a priority claim or positive BGS
universality. The finite Weil representation and character orthogonality are
established mathematics; the proof below states the complete input rather
than importing an unverified character formula.

The phase-space matrix is S=A^T when A acts on Fourier covectors. A different
quadratic refinement from the earlier Pell convention is explicitly used
when A does not preserve that convention. No claim is made that two different
characteristics define the identical finite matrix.

# 1. An abstract finite spectral theorem

Let N be odd and q>=3 be odd. On C^(Z/NZ), use centered Weyl operators

    W(a,b)u(x)=exp_N(a(x-b/2))u(x-b),
    Ru(x)=u(-x),

where halves are modular and exp_N(z)=exp(2*pi*i*z/N). The N^2 operators W(v)
are an orthonormal basis of M_N(C) for normalized Hilbert--Schmidt inner
product. If A belongs to SL(2,Z/NZ), the assignment W(v) -> W(Av) preserves
products and adjoints. It therefore extends to a unital star automorphism
of M_N(C), implemented by a unitary U. This elementary inner-automorphism
fact can be checked by mapping a complete system of matrix units. The
implementer is unique up to a scalar because the Weyl matrices span M_N.

Assume

    A^q=I,
    det(A^j-I) is a unit for 1<=j<q.                         (H)

Primality of q is not required in this finite theorem. Since q is odd,
det(A^j+I) is also a unit for every j: modulo a prime divisor of N, a vector
with A^j v=-v would give v=(-1)^q v=-v after q applications.

**Theorem 1.** Hypotheses (H) imply N is congruent to either +1 or -1 modulo q.
Write this sign as c. There is a scalar normalization of U such that

    U^q=I,
    Tr(R U^j)=1                   for all integers j,
    Tr(U^j)=c                     if q does not divide j.

On the parity subspace

    H_c = range((I-cR)/2),
    D=(N-c)/2,

every q-th root of unity occurs with multiplicity exactly

    n=(N-c)/(2q).

On the complementary parity subspace the multiplicity is n at each nontrivial
q-th root, and n+c at the root 1. The statement includes repeated prime
factors of N. In particular, an even sector is required when c=-1; replacing
it by the odd sector would be wrong.

**Proof.** Weyl covariance makes Ad(U^j) a permutation in the Weyl basis.
For any finite matrix V, Tr(Ad V)=|Tr V|^2 when V is unitary. Consequently

    |Tr(U^j)|^2 = # ker(A^j-I) = 1,             1<=j<q,
    |Tr(R U^j)|^2 = # ker(A^j+I) = 1,          all j.         (1)

The first equality also shows Tr U is nonzero. The two implementers RUR and
U have the same Weyl covariance, so RUR=zU for a scalar z. Taking traces
forces z=1: U commutes with R. Since A^q=I, U^q is scalar. Choose its phase
so that U^q=I.

Let zeta=exp(2*pi*i/q). The function j -> Tr(RU^j) is a virtual character of
the cyclic group. Its Fourier coefficients are the integers

    b_l = multiplicity_even(l)-multiplicity_odd(l).

By (1) and Parseval, sum_l b_l^2=1. Also sum_l b_l=Tr R=1. Thus exactly one
b_l equals 1 and all others are zero. A further multiplication of U by a
q-th root of unity places that exceptional coefficient at l=0. This preserves
U^q=I and gives Tr(RU^j)=1 for every j.

Let m_l be the full-space eigenvalue multiplicities. Parseval and (1) give

    sum_l m_l=N,
    sum_l m_l^2=(N^2+q-1)/q.                                (2)

For N=qk+r, 0<=r<q, the least squared sum of q integers with sum N is
qk^2+2kr+r. Indeed, replacing a pair differing by at least two by two closer
integers lowers the squared sum. Comparing this minimum with (2) gives
r(q-r)<=q-1. Integrality of (2) also gives r^2=1 modulo q, excluding r=0.
For q>=3 the only remaining possibilities are r=1 and r=q-1. Thus c exists.

For either residue the lower bound is attained in (2). Hence all m_l equal
k0=(N-c)/q except one, which equals k0+c. Because N and q are odd, k0 is
even. Since the parity differences b_l vanish except for b_0=1, the sole
odd full-space multiplicity must occur at l=0. Therefore

    m_l=k0+c*1_(l=0),
    multiplicity_odd(l)=k0/2+(c-1)*1_(l=0)/2,
    multiplicity_even(l)=k0/2+(c+1)*1_(l=0)/2.

This is exactly the claimed spectrum. End of proof.

This proof establishes the whole multiplicity vector, not just trace moduli.
A modulus-only argument would miss both the phase normalization and the
switch of the uniform parity sector.

# 2. A logarithmic-period sequence for every hyperbolic trace

Let A be any integer matrix of determinant 1 with t=Tr A>2. Define

    u_0=0, u_1=1, u_(r+1)=t*u_r-u_(r-1).

For an odd prime K>3 with K not dividing t-2, put m=(K-1)/2 and

    N_K=u_(m+1)+u_m.

Equivalently, with lambda=(t+sqrt(t^2-4))/2,

    N_K=1+sum_(r=1)^m (lambda^r+lambda^(-r))
       =(lambda^(K/2)-lambda^(-K/2))/sqrt(t-2).               (3)

These expressions are equal as integer polynomials in t. In particular
N_K grows exponentially in K and K=O(log N_K).

**Theorem 2.** N_K is odd, and A modulo N_K satisfies (H) with q=K. Its sign
in Theorem 1 is

    c_K = ( (t-2) / K ),                                    (4)

the Legendre symbol. Thus the exactly uniform sector has dimension
(N_K-c_K)/2 and root multiplicity (N_K-c_K)/(2K).

**Proof.** Cayley--Hamilton gives A^r+A^(-r)=Tr(A^r) I. Hence

    sum_(j=0)^(K-1) A^j=N_K A^m,
    A^K-I=N_K A^m(A-I).                                    (5)

In particular A^K=I modulo N_K. Evaluation of the integer polynomial N_K(t)
at t=2 gives K. Therefore

    gcd(N_K,t-2)=gcd(K,t-2)=1.

Since det(A-I)=2-t, A-I is invertible modulo N_K. If A^j v=v modulo a
prime divisor p of N_K, where 0<j<K, Bezout applied to j and K and A^K=I
implies Av=v. Invertibility of A-I forces v=0. Thus every det(A^j-I) is a
unit modulo N_K. The plus-sign condition follows as in Theorem 1.

For even t, the recurrence u_r modulo 2 alternates 0,1, so N_K is odd. For
odd t the recurrence has the pattern 0,1,1 of period three; a consecutive
sum is even only when m=1 modulo 3, equivalently K=3 modulo 6. This is
impossible for a prime K>3. Thus N_K is odd in every case.

For completeness, (4) has an explicit polynomial proof. In an algebraic
extension modulo K put a^2=t+2, b^2=t-2. The two elements (a+b)/2 and
(a-b)/2 are inverse. Expanding their K-th powers gives the identity

    N_K(t)=2^(1-K) sum_(j odd, 1<=j<=K)
                 binom(K,j) (t+2)^((K-j)/2) (t-2)^((j-1)/2).

Modulo K all the internal binomial coefficients vanish. Fermat's theorem
for 2 and Euler's criterion then yield

    N_K(t)=(t-2)^((K-1)/2)=c_K modulo K.

No square root modulo N_K and no split eigenbasis were assumed. End of proof.

Examples from the exact recurrence, not fitted numerical spectra:

    t=6, K=5:  N=41,  c=+1, odd dimension 20,  multiplicity 4;
    t=4, K=5:  N=19,  c=-1, even dimension 10, multiplicity 2;
    t=4, K=7:  N=71,  c=+1, odd dimension 35,  multiplicity 5;
    t=4, K=11: N=989, c=-1, even dimension 495, multiplicity 45.

The last modulus is 23*43. For trace four its discriminant is 12, a square
modulo 23 and a nonsquare modulo 43. It is therefore a mixed split/nonsplit
example; it cannot be justified by diagonalizing the matrix over Z/989Z.

The sector can depend on K. There is always an infinite subsequence with
one fixed sign by the infinite pigeonhole principle. No claim is made that
the odd sector is uniform along every prime sequence for arbitrary t.
For t=d^2+2, c_K=+1 whenever K does not divide d, recovering the preceding
Pell-type odd-sector situation.

# 3. An invariant quantization characteristic for arbitrary A

The earlier physical convention Q_N(v)=(-1)^(v_1 v_2)W_N(v) has exact
integer-symbol covariance only for matrices preserving that quadratic
refinement modulo 2. Rather than silently imposing this restriction on A,
use the invariant refinement

    q_*(a,b)=ab+a+b modulo 2,
    Q_N^*(a,b)=(-1)^(ab+a+b)W_N(a,b).                         (6)

It takes value zero at 0 and value one at all three nonzero vectors in
F_2^2. It is consequently invariant under every SL(2,F_2) matrix. Direct
multiplication gives

    Q_N^*(v)Q_N^*(w)=exp(pi*i*omega(v,w)/N)Q_N^*(v+w),
    (Q_N^*(v))*=Q_N^*(-v),
    U_N Q_N^*(v) U_N*=Q_N^*(Av).                             (7)

In the first equation v,w are unreduced integer indices. The sign in (6)
cancels the modular-half sign because
q_*(v)+q_*(w)-q_*(v+w)=omega(v,w) modulo 2.

Define Op_N^*(a)=sum_v ahat(v)Q_N^*(v). Absolute Fourier summability gives
operator-norm convergence. Equations (7) imply exact Egorov covariance

    U_N Op_N^*(a) U_N*=Op_N^*(a composed with A^T).            (8)

Parity still quantizes x -> -x, since q_*(-v)=q_*(v). The leading commutator
has the same Poisson bracket and hbar=(2*pi*N)^(-1) as in the previous
convention. The extra factor (-1)^(a+b) is the fixed half-torus translation
of symbols relative to the earlier Q convention. This characteristic choice
is part of the construction, not a claim that the old finite matrices are
unchanged. In the usual terminology it is the invariant odd characteristic.
All results below are stated for this explicit quantization.

# 4. Fixed-strength nonlinear maps and all polynomial quantum times

Let S=A^T. Choose a nonzero real even smooth g0 with

    supp(g0) intersect S^(-1)supp(g0) empty.

Such a function exists: choose a point z outside the finite solution sets
of Sz=+/-z and 2z=0 on the torus, take small closed disjoint neighborhoods
of z and -z whose union misses its S-preimage, and put an even bump there.
There is an infinite-dimensional space of such bumps. Let g=g0-integral g0,
d=g composed with S, f=g-d, and put

    V_(kappa,N)=exp(i*kappa*Op_N^*(f)/hbar_N) U_N,
    J_(kappa,N)=exp(i*kappa*Op_N^*(g)/hbar_N).

The classical symbol f and strength kappa are fixed, and the kick is one
exponential without an N-dependent compensation term. For every a,p>0 and
kappa in any fixed compact interval,

    ||J* V J-U_N||_op=O(N^(-a)),
    sup_(integer |l|<=N^p) ||J* V^l J-U_N^l||_op=O(N^(-a)).   (9)

Here is the proof, so the generalization does not depend on the old Gaussian
or Floquet moment corpus. For odd j define
M_j(a)=sum_v |ahat(v)| |v|_2^j. The exact Weyl commutator in (7) is a sine
series. Each finite odd Taylor coefficient is the quantization of a mixed
local bidifferential expression in g and d, and vanishes because their
positive-order derivatives have disjoint supports. The real remainder
|sin z - Taylor_(j-2)(z)|<=|z|^j/j! gives

    ||[Op_N^*(g),Op_N^*(d)]||_op
        <=2*pi^j*M_j(g)*M_j(d)/(j!*N^j).

For Hermitian H,L and every real e, the two-factor Duhamel inequality is
||exp(ieH)exp(ieL)-exp(ie(H+L))||<=e^2||[H,L]||/2. It follows by integrating
unitary conjugation twice and needs no smallness of eH. With e=2*pi*N*kappa,

    ||J* V J-U_N||_op
       <=4*kappa^2*pi^(j+2)*M_j(g)*M_j(d)*N^(2-j)/j!.

Choose j as large as desired and telescope unitary powers to obtain (9).
This is a finite-remainder argument at each order, not convergence of an
infinite Moyal expansion.

With X_a=(partial_2 a,-partial_1 a), the associated classical map is

    F_kappa=S Phi_f^(-kappa)=Phi_g^kappa S Phi_g^(-kappa).    (10)

The supports make {g,d}=0 and the flows commute; symplecticity gives
Phi_d^t=S^(-1)Phi_g^t S, proving (10). This is a fixed nonlinear symplectic
Anosov map. Its invariant bundles are the smooth pushforwards of those of S.
For every kappa not zero it is nonaffine: it equals S on an open set, and
if it equaled S everywhere then a nonconstant compactly supported Hamiltonian
flow would have a nonzero global period. Averaging a Riemannian metric over
that period would make the whole flow a group of isometries fixing an open
set, hence the identity, a contradiction.

# 5. Complete fixed-order microscopic laws on the uniform sector

Use N=N_K and the uniform parity sector of Theorem 2, of dimension D and
root multiplicity n=D/K. Estimate (9) and the resolvent of a normal matrix
place the perturbed spectrum in K disjoint root neighborhoods of width
eta_N=O_a(N^(-a)) for every a. Riesz projection ranks along the straight
matrix homotopy preserve exactly n eigenvalues in each cluster. This is an
operator-norm argument, not a deduction from a normalized trace bound.

For any fixed p>=2 and Schwartz test Phi on R^(p-1), let

    R_N^(p)(Phi)=(1/D) sum_(a1,...,ap distinct) sum_(z in Z^(p-1))
                   Phi(D(x_a2-x_a1+z2),...,D(x_ap-x_a1+zp)).

Then for every a>0,

    R_N^(p)(Phi)=(n-1)...(n-p+1) Phi(0)+O_(p,Phi,a)(N^(-a)).  (11)

Indeed the same-cluster zero-winding terms have exactly that multiplicity
per anchor and displacement at most 2D eta_N in each coordinate. Every
other ideal separation is a nonzero point of n Z^(p-1), with at most
n^(p-1) choices per anchor. Arbitrarily high Schwartz decay and (9) bound
both errors to every inverse-power order.

The normalized cyclic nearest-neighbor gaps converge weakly to delta_0.
For each fixed x>0 the ordered distinct close-pair count divided by D is
exactly n-1 eventually. The mean gap remains exactly one; rare intercluster
gaps prevent convergence of first moments.

For a uniform random origin and a microscopic interval of length L, the
count Z_N(L) has

    P(Z_N(L)=n)=L/n+O(K eta_N),
    P(Z_N(L)=0)=1-L/n+O(K eta_N),
    P(Z_N(L) not in {0,n})=O(K eta_N).

For every fixed integer r>=2,

    E Z_N(L)=L exactly,
    E Z_N(L)^r=L*n^(r-1)+O_a(N^(-a)),
    Var Z_N(L)=L*n-L^2+O_a(N^(-a)).                          (12)

Moving the ideal lattice clusters changes the count only when an interval
endpoint is within eta_N of a root; that event has probability at most
4K eta_N. It proves these formulas and their separate moment error bounds.
The random-origin point process tends vaguely in probability to the empty
measure, despite intensity one at each N. There is no uniform integrability.

Finally, for the usual map form factor,

    F_N(l)=(1/D)|Tr_sector V^l|^2,
    sup_(|l|<=N^p)|F_N(l)-D*1_(K divides l)|=O_a(N^(-a)).      (13)

The factor D is retained explicitly. Equation (9) permits arbitrary error
orders and therefore absorbs this factor even on Heisenberg times l~D.
Averaging over every integer in [aD,bD], 0<a<b, yields n(1+o(1)), not a
random-matrix ramp. All these limits retain the common arithmetic structure.

# 6. Scientific boundary and verification contract

The extension removes the split-residue-ring and fixed Pell-trace assumptions.
It also shows exactly when the uniform sector changes parity. The quantum
conjugacy is at fixed classical strength and works on every polynomial time
window, but the classical systems are deliberately smoothly conjugate to
arithmetic cat maps. This cannot be described as positive BGS universality,
or as an arithmetic-free counterexample to its generic formulation.

The separate analytic rigidity theorem says that a nonconstant C1 function
with critical set of measure zero cannot Poisson-commute with its next
hyperbolic image. Thus a nonconstant analytic generator cannot use this
particular all-orders cancellation mechanism. That does not imply positivity
of the Green--Kubo variance of its nonzero bracket. Positivity for an arbitrary
finite union of Fourier orbits is not proved here.

A companion verifier is designed to check the integer matrix identity (5),
unit determinants over composite N, Euler sign (4), finite Weyl covariance,
and the predicted full and parity spectra for small examples. Finite checks
are not a proof of the asymptotic law or of external novelty. An execution
claim requires a successful run report tied to the exact source hash; none
is implied by this source file's existence.
