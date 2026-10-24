# Arithmetic word coherence despite uniform auxiliary quantum expansion

**Claim ID: BGS-TRACE-013. Status: PROJECT PROOF + EXTERNAL-THEOREM + AUTHOR SELF-REVIEW.**
4 October 2026. The fixed map and its odd parity sectors below are counterexamples
 to auxiliary mixing criteria, not the prescribed frozen map. The uniform gap
uses Bourgain--Gamburd; frame potentials and Clifford designs are prior mathematics.
No world-first priority, independent referee acceptance or BGS solution is asserted.
All standard and projective phases, and full-space versus sector channels, are
kept explicit. See [the audit](../archive/record/expansion_wavepacket_review_20261004.md)
and [source mappings](../literature/expansion_wavepacket_sources_20261004.md).

## 1. Three fixed maps

Let

$$
R=\begin{pmatrix}4&9\\19&43\end{pmatrix},\qquad
S=\begin{pmatrix}3&2\\1&1\end{pmatrix},\qquad
V=RS^{-1}=\begin{pmatrix}-5&19\\-24&91\end{pmatrix}.
$$

All determinants are one; their traces are 47, 4 and 86. Thus each induces
an Anosov torus automorphism, and VS=R. Write

$$
\beta=\frac{3+\sqrt5}{2},\qquad
\lambda=\frac{47+21\sqrt5}{2}=\beta^4.
$$

The eigenvalues of R are lambda and its reciprocal. The rational matrix

$$
B=\frac{R+8I}{21}
=\begin{pmatrix}4/7&3/7\\19/21&17/7\end{pmatrix}
$$

has trace 3, determinant one and satisfies B^4=R. This rational root is
not an automorphism of the integer lattice.

### R has no topological root

Suppose H in GL(2,Z) satisfies H^k=R, k>=2. H commutes with R, so its
eigenlines are those of R. If det H=1, its expanding eigenvalue has absolute
value at least beta, since its integer trace has absolute value at least 3.
Consequently k<=4.

For k=2, Cayley--Hamilton gives (Tr H)^2=49 and

$$
H=\pm(R+I)/7,
$$

which is not integral. For k=3, t^3-3t=47 has no integer solution:
the adjacent possible positive traces 3 and 4 give 18 and 52.
For k=4, (t^2-9)(t^2+5)=0 and H=+/- (R+8I)/21, again not integral.

If det H=-1, k is even. For k>=4, H^2 would be an excluded nontrivial
determinant-one root. For k=2, Tr(H^2)=(Tr H)^2+2=47 gives t^2=45,
impossible. A root among torus homeomorphisms would induce such an H on
first homology, so no topological root exists.

### R has no topological reversor: an elementary congruence proof

Any C in GL(2,Z) with CR=R^{-1}C has the form

$$
C=\begin{pmatrix}x&y\\z&-x\end{pmatrix},\qquad
-39x+19y+9z=0.
$$

Thus y=3x+9t and z=-2x-19t for integers x,t, and

$$
\det C=5x^2+75xt+171t^2.                       \tag{1}
$$

Determinant +1 is impossible modulo 3, since the right side is 2x^2.

For determinant -1, set X=10x+75t, Y=21t, Z=2x+15t. Equation (1) implies

$$
X^2-5Y^2=-20,\qquad Y^2-5Z^2=4.
$$

Y and Z have the same parity. Hence u=(Y+Z sqrt(5))/2 is a norm-one
unit in the ring of integers of Q(sqrt(5)). Its norm-one units are
+/- beta^k, k in Z. An elementary proof of this fact suffices: beta is
the smallest positive norm-one unit above one, since u-u^{-1}=b sqrt(5)
with integer b; multiplication by a power of beta reduces any positive
unit to [1,beta), where b must be zero.

It follows that Y=+/- v_k, where v_k=beta^k+beta^{-k},
v_0=2, v_1=3 and v_{k+2}=3v_{k+1}-v_k. The exact residue periods are

$$
(v_k\bmod3)=(2,0,1,0,\ldots),\qquad
(v_k\bmod7)=(2,3,0,4,5,4,0,3,\ldots).
$$

Divisibility by 3 requires k odd; divisibility by 7 requires k=2 mod 4.
They cannot hold together. But Y=21t is divisible by both. This excludes
determinant -1 as well. Negative indices satisfy v_{-k}=v_k.

A torus homeomorphism reversing R would induce an excluded C on first
homology. Thus R has no topological, and hence no smooth, reversor.
The earlier finite enumeration was only corroboration; this proof is uniform.

## 2. The arithmetic quantum period

Let p be prime, p=1 mod 20. Then 5 is a square modulo p, and p is different
from 3 and 7. The reduction of B has two distinct eigenvalues beta_p and
beta_p^{-1} in F_p^*. Since R=B^4 modulo p,

$$
d_p=\operatorname{ord}_p(R)\mid(p-1)/4.          \tag{2}
$$

There is no assertion that the order is maximal, and no Artin-type
conjecture is needed. The prime progression is infinite by Dirichlet's theorem.

Let rho_p be a standard finite Weil quantization. The parity subspaces have
dimensions (p+1)/2 and (p-1)/2. Use the even subspace H_p^+ and put

$$
N_p=(p+1)/2,\qquad U_p=\rho_p(R)|_{H_p^+}.
$$

These N_p are odd.

The classical-coordinate convention must also be fixed. For raw modular
Weyl translations T_p(a,b), ordinary midpoint matrices are
(-1)^(ab) T_p(a,b). Use the common coordinate chart translated by
c=(1/2,1/2), so that the midpoint dictionary is
(-1)^(ab+a+b) T_p(a,b). The quadratic form ab+a+b modulo two is one
on all three nonzero vectors of F_2^2 and is invariant under SL_2(F_2).
Thus the modular-to-midpoint conversion introduces no extra conjugation
sign in this chart. Choose the standard compatible Egorov orientation,
with classical matrices R,S,V as displayed. In the unshifted chart the
three maps are conjugated by the same fixed half-translation. All classical
root, reversor and Anosov conclusions are invariant under this conjugacy.
This convention is for this counterexample only; the frozen-model dictionary
in FM-001 is unchanged.

Projective scalar conventions are harmless:

$$
U_p^{d_p}=\zeta_p I.
$$

Every eigenphase therefore lies on a rotated d_p-clock. Its unfolded pitch is

$$
N_p/d_p\ge 2(p+1)/(p-1)>2.                      \tag{3}
$$

For every nonnegative nonzero smooth phi supported in (1/4,1/2), the
positive anchored factorial pair statistic is exactly zero. Its Sine_2
target is strictly positive:

$$
\int_{\mathbb R}\phi(u)
\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]\,du>0.
$$

This is a pair-law counterexample with no moment-tail assumption.

It also excludes weak phase-averaged convergence to Sine_2: choose a
nonnegative smooth compact spatial cutoff g, positive on an interval
of length greater than 1/2, and the bounded functional

$$
1-\exp\!\left[-\int g(x)g(y)\phi(y-x)\,d\Xi(x)\,d\Xi(y)\right].
$$

It is continuous on locally finite point measures, phi vanishes near the
diagonal, and it is zero for every example while having positive expectation
under Sine_2. This argument does not infer weak failure merely from an
unbounded correlation statistic.

## 3. A uniform quantum mixing gap

Define, on End(H_p^+),

$$
\mathcal E_p=\frac12\,\mathrm{Id}
+\frac18\left(
\operatorname{Ad}\rho_p(S)+\operatorname{Ad}\rho_p(S)^{-1}
+\operatorname{Ad}\rho_p(V)+\operatorname{Ad}\rho_p(V)^{-1}\right).
                                                            \tag{4}
$$

Here Ad A(X)=AXA^*, and inverse superscripts denote inverse conjugations.
The identity superoperator has weight one half. This is a self-adjoint,
positive, unital, trace-preserving mixed-unitary channel.

The subgroup generated by S,V contains R. S and R are hyperbolic with
disjoint fixed-point sets: the fixed-line equations of S and R have
resultant -6551. Equivalently their quadratic eigenline fields are
Q(sqrt(3)) and Q(sqrt(5)). Thus the subgroup is non-elementary.
Bourgain--Gamburd, Theorem 1, gives a p-independent Cayley gap for all
sufficiently large primes.

The even Weil sector is irreducible. This can be checked without importing
an irreducibility assertion: a nontrivial shear is diagonal with distinct
eigenvalues indexed by x^2, with x and -x identified; its commutant is
diagonal in the even basis. The Fourier operator has nonzero entries in
that basis (cos(2 pi xy/p) never vanishes for odd p). A diagonal operator
commuting with it must be scalar.

The conjugation representation is genuine even if rho is projective.
Its invariant subspace is exactly the scalar matrices. Decomposition into
irreducible finite-group representations transfers the regular Cayley
gap to this representation. Laziness removes any negative-edge issue.
Consequently, for some gamma>0 independent of p,

$$
\|\mathcal E_p X\|_{HS}\le(1-\gamma)\|X\|_{HS},
\qquad \operatorname{Tr}X=0.                    \tag{5}
$$

This is a full Hilbert--Schmidt gap, not an assertion only about smooth
classical observables. Nonetheless U_p fails the pair and weak local laws.

### An extensive invariant sector on two copies

Let Q_g=rho_p(g)|_{H_p^+}, G_p=SL_2(F_p), and average conjugation on
End(H_p^+ tensor H_p^+):

$$
\mathcal P_{2,p}=\frac1{|G_p|}\sum_{g\in G_p}
\operatorname{Ad}(Q_g\otimes Q_g).
$$

This is an orthogonal projection, even with projective scalar conventions.
Write D_{2,p}=rank P_{2,p}. Taking its superoperator trace gives the exact
character identity

$$
D_{2,p}=\frac1{|G_p|}\sum_g|\operatorname{Tr}Q_g|^4
\ge\frac{2N_p^4}{p(p^2-1)}
=\frac{N_p^3}{2(N_p-1)(2N_p-1)}
=\frac{N_p}{4}+O(1).                           \tag{5a}
$$

The two terms g=I,-I suffice: both act as scalars on the even sector.
There is no numerical estimate of a rare-event tail in this proof.

For the present primes p=1 mod4, the exact value is

$$
D_{2,p}=\frac{p+7}{4}=\frac{N_p+3}{2}.           \tag{5b}
$$

Here is a complete elementary character calculation. Choose the genuine
Weil phases for this calculation; projective changes do not affect any
absolute character or conjugation average. If g=[[a,b],[c,d]] and b!=0,
the full Weil kernel is

$$
\rho_p(g)_{xy}=\frac{\chi_p(-2b)}{\sqrt p}
e_p\!\left(\frac{d x^2-2xy+a y^2}{2b}\right).
$$

For b=0 it is the operator
psi(x) -> chi_p(a) e_p(c x^2/(2a)) psi(a^{-1}x).
Taking the trace and using the elementary quadratic Gauss sum gives
Tr rho_p(g)=chi_p(Tr g-2) when Tr g!=2. For nontrivial unipotents
the two square classes give traces +sqrt(p), -sqrt(p).
Moreover rho_p(-I)=parity, so the even character is
(Tr rho_p(g)+Tr rho_p(-g))/2.

The complete partition of G_p contributes as follows to its fourth moment:

| Elements | Number | Even character fourth power |
|---|---:|---:|
| I,-I | 2 | N_p^4 |
| Regular split elements | (p-3)p(p+1)/2 | 1 |
| Regular nonsplit elements | Remaining regular elements | 0 |
| Noncentral trace +/-2, positive Gauss class | p^2-1 | ((sqrt(p)+1)/2)^4 |
| Noncentral trace +/-2, negative Gauss class | p^2-1 | ((1-sqrt(p))/2)^4 |

For a regular element of trace t, the even character is
(chi_p(t-2)+chi_p(t+2))/2: its fourth power is one in the split
case, zero in the nonsplit case. The (p-3)/2 split traces come from
alpha+alpha^{-1} with alpha!=+/-1; their centralizers have order p-1.
Each nonzero unipotent square class has centralizer order 2p and
class size (p^2-1)/2. Including the negative-central multiples gives
the two counts p^2-1 in the table. These cases exhaust the group.
Summing the table gives

$$
\frac{(p+1)^4/8+(p^2-1)(p^2+6p+1)/8
 +(p-3)p(p+1)/2}{p(p^2-1)}=\frac{p+7}{4}.
$$

Haar averaging of Q tensor Q over U(N_p) has invariant space spanned
by the identity and the swap, of dimension two for N_p>=2. The symmetric
and antisymmetric squares are distinct irreducible U(N_p) representations,
which proves this statement. Therefore at least D_{2,p}-2 directions
are invariant for the finite-group average but orthogonal to its Haar
counterpart. The lazy channel built from S,V on two copies fixes each of
these directions. Its gap on the complement of the Haar space is zero,
despite the uniform one-copy gap (5).

The same mechanism extends to every fixed tensor order k>=2. Averaging
Ad(Q_g^{tensor k}) has invariant dimension

$$
D_{k,p}=\frac1{|G_p|}\sum_g|\operatorname{Tr}Q_g|^{2k}
\ge\frac{2N_p^{2k}}{p(p^2-1)}
=\left(\frac14+o(1)\right)N_p^{2k-3}.
$$

The Haar invariant space has dimension k! for N_p>=k, by Schur--Weyl
duality. Thus the extra invariant hierarchy is already present at every
fixed k. This is a hierarchy of actual invariant spaces, not a conjectured
diagrammatic cancellation formula.

The character identity and its interpretation as a frame potential are
standard; see Gross--Audenaert--Eisert, Section III.B, equation (20)
and Theorem 6. The structural information here is the explicit coexistence
of one-copy contraction and an extensive two-copy memory sector.
Neither a one-copy nor a proposed two-copy random-walk criterion can
replace a proof for the prescribed deterministic word.


### Exact invariant hierarchy at every fixed tensor order

The same complete character partition proves, for $p\equiv1\pmod4$,

$$
D_{k,p}=\frac{2((p+1)/2)^{2k}+(p-3)p(p+1)/2
 +(p^2-1)2^{1-2k}\sum_{l=0}^k\binom{2k}{2l}p^l}{p(p^2-1)}. \tag{5d}
$$

The two unipotent fourth powers in the table are replaced by their
$2k$-th powers; their sum is precisely the displayed even-binomial sum.
The regular characters have absolute value zero or one, and the centers
have absolute value $N_p$, so no class is omitted. In particular
$D_{1,p}=1$, $D_{2,p}=(p+7)/4$, and
$D_{3,p}=(p+3)(p^2+4p+19)/32$. For every fixed $k\ge3$,
$D_{k,p}\sim N_p^{2k-3}/4$; for $k=2$ the unipotents contribute
at the same leading order as the center and $D_{2,p}\sim N_p/2$.
These are exact ranks and asymptotics of the auxiliary finite-group twirl,
not estimates on deterministic Heisenberg words of the frozen map.

### An enlarged full-space channel with a uniform two-copy gap

Use the full p-dimensional H_p, not the even sector. Let P average
Ad(rho_p(g) tensor rho_p(g)) over G_p. The orthogonal Weyl-pair basis
T_p(v) tensor T_p(w) is permuted by simultaneous SL_2(F_p) action.
Its 2p+1 orbits are: one zero pair, p+1 nonzero rank-one projective
ratios, and p-1 nonzero rank-two determinants. Orbit sums give a
complete orthonormal basis of invariants; rank P=2p+1.

Fix e=(1,0), B_p=T_p(e). Conjugation by B_p tensor B_p multiplies
each Weyl pair by e_p(omega(e,v+w)). The zero pair and the orbit
(v,-v), v!=0, have phase one. Their span is I,swap, because
swap=p^{-1} sum_v T_p(v) tensor T_p(-v).
On every other orbit v+w is nonzero and uniformly distributed over
F_p^2 minus zero: this is an equivariant orbit map to a transitive
SL_2(F_p) space. Its exact compressed phase average is

$$
\frac1{p^2-1}\sum_{s\ne0}e_p(\omega(e,s))
=-\frac1{p^2-1}.
$$

Here Re Ad B means (Ad B+Ad B^{-1})/2, the self-adjoint part of
the conjugation superoperator. Put D_B=Id-Re Ad(B_p tensor B_p).
Thus 0<=D_B<=2 Id and, on the
extra invariant space, P D_B P=q_p Id with q_p=1+1/(p^2-1)>=1.
For the original full-space lazy channel E_{Sp,2}, representation
transfer gives Id-E_{Sp,2}>=gamma(Id-P), with 0<gamma<=1 independent
of all sufficiently large p. Define the enlarged channel

$$
\mathcal F_{2,p}=\frac12\mathcal E_{Sp,2}+\frac14\mathrm{Id}
+\frac18\left(\operatorname{Ad}(B_p\otimes B_p)
+\operatorname{Ad}(B_p^{-1}\otimes B_p^{-1})\right).
$$

It is positive and self-adjoint, and on the complement of I,swap,

$$
\|\mathcal F_{2,p}X\|_{HS}
\le(1-\gamma/18)\|X\|_{HS}.                    \tag{5c}
$$

**Proof of the constant.** Write X=u+v, u=PX, v=(Id-P)X; u is
orthogonal to I,swap. Its Dirichlet form is at least
(gamma/2)||v||^2+(1/4)||D_B^{1/2}(u+v)||^2.
If ||v||^2>=||u||^2/8, the first term is >=(gamma/18)||X||^2.
Otherwise ||D_B^{1/2}u||>=||u||,
||D_B^{1/2}v||<=sqrt(2)||v||<||u||/2. The second term is then
>=||u||^2/16 >=||X||^2/18. This proves (5c).
The corresponding full-space one-copy channel has the same bound
on traceless matrices: X tensor I is orthogonal to I,swap if Tr X=0.

The word rho_p(V)rho_p(S), up to its retained scalar, is still
rho_p(R). No B_p enters that word; its period and clock spectrum
are unchanged. Both parity sectors separately fail the Sine_2 test,
although this enlarged auxiliary channel mixes the sectors.
Thus (5c) refutes a criterion using full-space auxiliary two-copy mixing.
It does not refute a different hypothesis requiring a sector-preserving
two-copy channel. The Clifford two-design mechanism is prior; the
orbit compression and uniform gap constant are reconstructed here.

B_p translates classical coordinates by scale 1/p. It quantizes the
identity canonical map at principal classical order, with a nontrivial
Weyl phase. Its role is explicit; it is not another hyperbolic generator.
The enlarged auxiliary model remains distinct from the frozen dynamics.

## 4. Flat perturbation: simple spectra and all nonzero traces

Choose an algebraic orthonormal eigenbasis of the full p-dimensional
rho_p(R), respecting parity, with algebraic eigenvalues z_j. Such a basis
exists since the matrix is algebraic and normal. Put

$$
A_p=\sum_{j=1}^{p}(j/p)|\psi_j\rangle\langle\psi_j|,\qquad
\delta_p=1/p!,\qquad
D_p=e^{i\delta_p A_p}.
$$

Use U'_p=D_p rho_p(R), V'_p=D_p rho_p(V). With genuine Weil phases,
U'_p=V'_p rho_p(S). With projective phases write instead
V'_p rho_p(S)=eta_p U'_p, |eta_p|=1; the scalar is retained and
does not change any absolute trace, pair law or conjugation channel.
Restrict all three to the even sector. Its eigenvalues are
z_j exp(i delta_p j/p), over the corresponding subset of labels.

For different labels, equality of eigenvalues, or equality of their positive
integer powers, would make the exponential of a nonzero algebraic number
algebraic. Hermite--Lindemann excludes it. Therefore every spectrum
is simple, and no positive power is scalar. Moreover

$$
\operatorname{Tr}((U'_p)^m)
=\sum_{j\in H_p^+}z_j^m e^{im\delta_p j/p}\ne0,
\qquad m\ge1,                                  \tag{6}
$$

Indeed, x_m=exp(i m delta_p/p) is transcendental by Hermite--Lindemann.
The trace is the value at x_m of the nonzero polynomial
sum_(j in H_p^+) z_j^m X^j with algebraic coefficients and distinct
integer exponents. It cannot vanish at a transcendental argument.
This uses only the one-exponential transcendence theorem; the stronger
linear-independence form of Lindemann--Weierstrass is unnecessary.
No floating computation at delta_p is used.

Since ||D_p-I||<=delta_p, the conjugation-channel perturbation in (4)
has HS operator norm at most delta_p/2. Thus its traceless contraction
remains at most 1-gamma/2 eventually. The common commuting operators of
the two factors are still only scalars.

On two copies, ||D_p tensor D_p-I||<=2 delta_p. The corresponding
lazy-channel perturbation has HS operator norm at most delta_p.
Identity and swap remain invariant for any unitary generators. Min--max
on their orthogonal complement gives at least D_{2,p}-2 eigenvalues
in [1-delta_p,1]. On the original extra invariant space, telescoping
the powers of two contractions gives, for all ell>=0,

$$
\|(\mathcal E'_{2,p})^\ell X-X\|_{HS}
\le\ell\delta_p\|X\|_{HS}.                     \tag{6a}
$$

At ell of order N_p this error tends to zero. A uniform one-copy gap
coexists with nearly stationary higher-moment memory in a number of
directions proportional to N_p. No assertion is made that every exact
two-copy invariant is removed.

At general fixed tensor order k, the channel perturbation is at most
k delta_p/2. Min--max and telescoping therefore give at least
D_{k,p}-k! eigenvalues in [1-k delta_p/2,1] and displacement at
ell steps bounded by ell k delta_p/2 on the original extra invariant
space. The complete fixed-order memory hierarchy survives ell=O(N_p).

The eigenangles move by at most delta_p. Their unfolded differences change
by at most N_p delta_p/pi. Within one original clock cluster the gaps tend
to zero; between clusters they are at least N_p/d_p-o(1)>2-o(1).
Thus the same pair statistic supported in (1/4,1/2) remains exactly zero
for all sufficiently large p. The weak-local counterexample survives.

For the enlarged full-space channel, replacing rho_p(V) by V'_p
changes F_{2,p} by at most delta_p/2. Hence its gap remains at least
gamma/36 eventually, while the same simple-spectrum, nonzero-trace
and no-scalar-power conclusions hold on full H_p. The full-space
unfolded clock pitch is p/d_p>4. On m in [p,2p] divisible by d_p,
the analogue of (7) below has lower bound 4-o(1).
These assertions coexist with the enlarged channel's two-copy gap.

### Whole Heisenberg resonant sector

For m=r d_p in [N_p,2N_p],

$$
\|(U'_p)^m-\zeta_p^r I\|\le m\delta_p,\qquad
|\operatorname{Tr}((U'_p)^m)|\ge N_p(1-2N_p\delta_p).
$$

There are at least floor(N_p/d_p)>=2 such integers m. Therefore

$$
N_p^{-2}\sum_{\substack{N_p\le m\le2N_p\\d_p\mid m}}
\left||\operatorname{Tr}((U'_p)^m)|^2-\min(m,N_p)\right|
\ge 2-o(1).                                   \tag{7}
$$

This is a realized infinite-sequence obstruction to the stated whole-sector
CUE comparison. It is not a pointwise identification with a CUE expectation,
and it is not an obstruction proved for the project's frozen propagator.

### Bounded traces at every fixed time do not repair the criterion

For each fixed nonzero integer j, the integer matrix R^j has no eigenvalue
1 or -1. Thus only finitely many primes divide
det(R^j-I)det(R^j+I); outside them R^j mod p is regular. The character
partition above gives |Tr rho_p(R^j)|=1 on the full space and at most
1 on the even sector. Consequently telescoping the flat perturbation gives

$$
|\operatorname{Tr}((U'_p)^j)|\le1+|j|p\delta_p=1+o(1). \tag{7a}
$$

Both the full-space and sector families therefore have bounded traces at
every fixed nonzero time and macroscopically uniform eigenphases, while
the coherent Heisenberg return lower bounds (7) survive. This additional
condition can be imposed simultaneously with the simple spectrum, every
nonzero power trace, exclusion of scalar powers and the auxiliary channel
gaps. In particular the positive frozen-model FM-013 input, by itself,
cannot supply the still-missing coherent-word suppression. This does not
identify these counterexample spectra with the frozen family.

### Analytic flatness

For any bounded p-by-p matrix, its Weyl coefficients are bounded by its
operator norm, and it has at most p^2 coefficients at frequencies O(p).
Interpolating D_p-I gives a torus symbol b_p satisfying, for every fixed
derivative order k,

$$
\|b_p\|_{C^k}\le C_k p^{k+2}/p!=O(p^{-L})
\quad\hbox{for every fixed }L.
$$

On each fixed complex strip the analogous bound is
C p^2 exp(C_strip p)/p!, also flat to every order. Thus
U'_p=(I+Op_p(b_p)) rho_p(R) is a standard quantization with exactly the
same formal symbol as the arithmetic map, modified by an analytic flat
remainder. The former weak-Egorov spectral-rounding objection does not
apply to this much smaller perturbation.

This does not claim that equal formal symbols allow different local laws:
the flat perturbation preserves the original nonuniversal local law.
It shows that destroying exact algebraic spectral markers cannot by itself
destroy approximate arithmetic coherence.

## 5. A fixed nonlinear version

Take any fixed nonzero kappa and the analytic Hamiltonian shear

$$
F_\kappa(q,p)=(q,p+\kappa\sin2\pi q).
$$

Let W_p be its standard unitary quantization, chosen compatibly with the
Weil convention. In the usual Schrodinger convention it is a diagonal
Hamiltonian phase. It commutes with parity. Conjugate both factors and
their product by W_p. The channel gap, traces, simple spectrum and
inequality (7) are unchanged exactly.

The fixed classical product is

$$
G_\kappa=F_\kappa R F_\kappa^{-1}.
$$

It is analytic Anosov, primitive and has no topological reversor, since
these properties are invariant under conjugation. It is nonaffine:
its first coordinate contains -9 kappa sin(2 pi q).
The analytic flat correction remains flat under this fixed smooth
microlocal conjugation.

This family still carries inherited arithmetic structure through its smooth
conjugacy to R. It is outside the project's stronger nonaffine-conjugacy
exclusion. That distinction is essential.

The earlier project theorem mathematics/locality/fixed_strength_locality.md already
constructs fixed nonlinear smooth conjugates with arithmetic clustering.
This section carries the simultaneous expansion/memory theorem into a
nonlinear family; it does not claim priority for nonlinear counterexamples.

## 6. Boundary and verification

The [maintained checker](../computations/verification/expansion_wavepacket_audit.py)
replays the integer/rational root and reversor identities, prime orders,
finite Weil character partition and all fixed-order rank formulas through
k=5. It separately tests genuine multiplication at p=5, the two-copy
translation compression at p=5 and the even-sector one-copy channels at
p=41,61 in complex128. The p=5,13 controls check character formulas;
they are not in the resonant prime progression p=1 mod20.
No finite floating gap establishes the uniform gap: that input is the
checked published theorem and the Dirichlet argument above.

The shrinking factorial perturbation is never rounded to the identity in
an eigenvalue experiment; its simplicity/nonvanishing proof is transcendental,
and its persistence proof uses norm inequalities. Fixed nonlinear smooth
arithmetic conjugates were already constructed in
[fixed_strength_locality.md](locality/fixed_strength_locality.md). The simultaneous
channel/memory construction is an additional obstruction to proposed
criteria; it cannot replace TRACE-005 for the different frozen family.
