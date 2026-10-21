> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_homoclinic_and_doubled_transfer.md`. Embedded SHA256: `85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168`.
> [Thematic guide](../../topics/histories.md).

# Actual coherent orbit pairs and the doubled quantum transfer

Research continuation, 20 October 2026. The family is exactly the
one in the question, with `tau=10^-80`, and dimensions are all
sufficiently large odd integers. This note gives two further
direct results at the point where a long-time cancellation
argument is needed. It does **not** prove `H_diag` or a
counterexample to it.

First, two distinct primitive orbits of the actual nonlinear map,
of a common length within four of N, have complete principal
weights agreeing to relative error `O(N^2 exp(-c N))`. The
construction retains the odd-dimensional lattice phase and the
exact Gaussian scalar. Second, the exact doubled quantum transfer
is an explicitly given unitary matrix with a finite-hop generator.
It identifies the first missing pair bound as a Hilbert--Schmidt
resolvent estimate and proves why a strict operator-norm
contraction on this quantum space cannot supply it.

The coherent pairs have exponentially small total weight. Thus
they do not contradict CUE statistics. Their use is to test an
attempted assertion of uniform separation of distinct orbit-pair
phases. Close phase values at discrete periodic points do not, by
themselves, contradict a derivative nonstationarity condition.

## 1. Frozen inputs and conventions

All input statements used below have proofs in the indicated files.
The quantitative coding and analytic-potential files were also
independently audited before this note was written.

| Input | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `../research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `fermionic_quantitative_pressure.md` | `d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2` |
| `arithmetic_pressure_analytic_potential.md` | `44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f` |
| `fermionic_weyl_return_windows.md` | `de901fca5b512781737f7543a4f094172184d3fe3991d5cb61eacf17373a457d` |

Write

$$
 S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
 L=S^{-1},\quad \lambda=3+2\sqrt2,\quad
 h=(2\pi N)^{-1},\quad q_*=0.421.
$$

The actual map is `Psi=Xi_tau^(-1)`, with
`Xi_tau=S composed with Phi_tau`. The analytic-potential input
constructs a lift `H=id+w`, periodic modulo the integer lattice,
such that

$$
 \Xi_\tau H=HS,\qquad \Psi H=HL.
 \tag{1.1}
$$

It is a homeomorphism and is spatially Holder with exponent 1/2.
The smooth map Psi and its inverse have Lipschitz constants at most 8, in
the ordinary coordinate max norm, after passing to the torus.
This follows also directly from the uniform derivative bound
for the very short Hamiltonian flow and `||S||_infty=||L||_infty=7`.

The phase generating Psi is

$$
 F(Q,q)=-\frac{3Q^2-2Qq+3q^2}{8}+G(Q,q),\qquad
 p=-F_q,\quad P=F_Q.
 \tag{1.2}
$$

The exact-amplitude input proves uniform analytic spatial bounds
on G and on the exact amplitude B_h on fixed strips; real h is
allowed to tend to zero. The centered operator cocycle K_h on
the single Hilbert space `L^2(R)` has its normalized right graph
and scalar

$$
 K_h(x)v_h(x)=\gamma_h(x)v_h(\Psi x),\qquad
 v_h=e_0+w_h,\quad e_0^*v_h=1,
 \tag{1.3}
$$

with `||w_h||<=2.5*10^-4` and

$$
 |\gamma_h-1|<0.0002.
 \tag{1.4}
$$

For every m at one sufficiently large odd-dimensional threshold,

$$
 p_{m,N}=\mathcal P_{m,N}+E_{m,N},\qquad
 |E_{m,N}|\le2q_*^m,
 \tag{1.5}
$$

$$
 \mathcal P_{m,N}
 =\zeta_N^m\lambda^{-m/2}
   \sum_{x\in\operatorname{Fix}\Psi^m}
       \omega_{m,N}(x)\Gamma_h(x,m),\qquad
 \Gamma_h(x,m)=\prod_{j=0}^{m-1}\gamma_h(\Psi^j x),
 \tag{1.6}
$$

where `|zeta_N|=1`. For a primitive geometric orbit p of length m,
denote its single-orbit weight by

$$
 a_{p,N}=\zeta_N^m\lambda^{-m/2}\omega_{p,N}\Gamma_h(p,m).
 \tag{1.7}
$$

Its contribution to (1.6) is `m a_(p,N)`.

## 2. Exact removal of the half-winding phase for odd N

Let a lifted closed orbit have winding n, so that
`Psi^m z_0=z_0+n`. The original, audited phase is

$$
 \omega_{m,N}
 =(-1)^{n_qn_p}
  \exp\!\left[\frac{i}{h}
       \left(\sum_{j=0}^{m-1}F(q_{j+1},q_j)
                  -n_p(q_0+n_q/2)\right)\right].
 \tag{2.1}
$$

Since N is odd,

$$
 (-1)^{n_qn_p}\exp(-i n_pn_q/(2h))
 =\exp(i\pi(1-N)n_qn_p)=1.
$$

Consequently the exact, simpler formula is

$$
 \boxed{\displaystyle
 \omega_{m,N}
 =\exp\!\left[\frac{i}{h}
       \left(\sum_{j=0}^{m-1}F(q_{j+1},q_j)-n_pq_0\right)\right].}
 \tag{2.2}
$$

This is an exact cancellation of two factors, not a discarded
lattice character.

Here is a local scalar version suitable for symbolic comparison.
On `R^2 times C`, use the deck identifications

$$
 (z,u)\longmapsto
       (z+n,\exp(i n_p q/h)u).
 \tag{2.3}
$$

They form an action of the integer lattice: the extra factor in
composing two deck maps is `exp(2 pi i N n_p k_q)=1`.
The phase deck law from the exact-amplitude input is

$$
 F(Q+a,q+b)-F(Q,q)
 =cQ-dq+(ca-db)/2,\qquad (a,c)=L(b,d).
 \tag{2.4}
$$

Since `L=I mod 2`, the integer `ca-db` is even. Applying (2.4)
shows directly that

$$
 (z,u)\longmapsto
    (\Psi z,\exp(iF(Q,q)/h)u)
 \tag{2.5}
$$

respects (2.3). Indeed the factor `exp(i d q/h)` from the input
deck change cancels `exp(-i d q/h)` in (2.4); the output deck
factor is `exp(i c Q/h)` and the remaining constant factor is one.

Choose a bounded lifted representative of each Markov rectangle.
If a coded edge has lifted input z, chosen lifted output z', and

$$
 \Psi z=z'+d_e,\qquad d_e\in\mathbb Z^2,
$$

then reducing the output of (2.5) using (2.3) gives its local
unit-modulus factor

$$
 \eta_{N,e}(x)=
 \exp\!\left[\frac{i}{h}
   \big(F(q'+d_{e,q},q)-d_{e,p}q'\big)\right].
 \tag{2.6}
$$

The integer `d_e` is constant on a fixed edge. Multiplying (2.6)
around a closed orbit gives exactly (2.2): one may either telescope
the intermediate deck reductions or use the equivariance just
proved and reduce only at the final point. No global real branch
of a torus action is required.

## 3. Uniform Holder regularity of the actual scalar gamma_h

The fixed-point construction of a contracting graph does not imply
spatial analyticity, or even spatial C^1 regularity, of that graph.
The weaker regularity required here follows from a strict numerical
inequality, as we now prove.

### 3.1. A uniform base derivative for the centered operator

Put `s=sqrt(h)`. The Gaussian input, Sections 1--4, gives the exact
kernel

$$
 k_s(x;y',y)=\lambda_0^{-1}
 B_{s^2}(Q+z_s(y'),q+z_s(y))J_s(y)
 \exp\!\left(\frac{i\widetilde F_x(z_s(y'),z_s(y))}{s^2}\right),
 \tag{3.1}
$$

where `z_s(y)=sy-i psi(sy)`, psi is a fixed smooth monotone
saturated contour, `|z_s(y)|<=sqrt(2)s|y|`, and

$$
 \widetilde F_x(Z)=F(X+Z)-F(X)-DF(X)Z,
 \qquad X=(Q(x),q(x)).
 \tag{3.2}
$$

The contour and all its derivatives are independent of x. A base
derivative of (3.2) equals

$$
 D_xX\cdot
 \big(DF(X+Z)-DF(X)-D^2F(X)Z\big).
 \tag{3.3}
$$

The bracket is quadratic in Z, with a uniform bound by the integral
form of Taylor's theorem and the fixed-strip bound on `D^3F`.
The segment from X to X+Z remains in that strip, including when
the real part of Z is unbounded. Therefore

$$
 s^{-2}|D_x\widetilde F_x(z_s(y'),z_s(y))|
 \le C(|y|+|y'|)^2.
 \tag{3.4}
$$

The same argument after up to two derivatives in each of y,y'
gives a fixed polynomial bound. For a first y derivative the
remaining zero of the first Taylor jet supplies one factor of Z;
for two or more derivatives the factors from `D_y z_s` cancel
the displayed `s^-2`. Derivatives of the contour beyond its first
one carry further nonnegative powers of s. Derivatives of B_h
are uniformly bounded on a smaller fixed strip by Cauchy's
formula. Thus all kernel derivatives appearing below, including
one base derivative, are bounded by a fixed polynomial in
`|y|+|y'|` times the original exponential decay, uniformly for
`0<s<=s_0`.

More explicitly the monotone-contour coercivity in the Gaussian
input is bounded above in modulus by

$$
 \exp[-c s^{-2}\{sy\,\psi(sy)+sy'\,\psi(sy')\}].
 \tag{3.5}
$$

For some fixed u_0,c_0>0, monotonicity and the straight contour near
zero give `u psi(u)>=c_0 min(u^2,u_0|u|)`. Hence (3.5) is at most

$$
 \exp[-c'\{\min(y^2,u_0|y|/s_0)
                    +\min((y')^2,u_0|y'|/s_0)\}],
 \tag{3.6}
$$

an h-independent integrable majorant after multiplication by any
fixed polynomial. This also supplies dominated differentiation.

For `A_osc=1-partial_y^2+y^2`, the explicitly proved trace-norm
criterion is

$$
 \|K\|_1\le\frac{\pi^2}{24}
       \|A_{\rm osc,y'}A_{\rm osc,y}k\|_{L^2(\mathbb R^2)}.
 \tag{3.7}
$$

Applying it to (3.1) and to its base derivatives proves

$$
 \sup_{0<h<h_0}\|K_h\|_{C^1(\mathbb T^2;\mathcal S_1)}<\infty.
 \tag{3.8}
$$

The centered deck identity in the Gaussian input makes these
derivatives genuine derivatives on the torus. In particular, no
uncanceled derivative of a rapidly varying uncentered phase is
being included in (3.8).

### 3.2. The graph gains the needed fractional regularity

The normalized projective map is

$$
 g_x(w)=\frac{(I-P)K_h(x)(e_0+w)}{e_0^*K_h(x)(e_0+w)},
 \qquad \|w\|\le2.5\cdot10^{-4}.
 \tag{3.9}
$$

The denominator is at least `1-0.000100025`; the Gaussian input
proves a Lipschitz constant strictly below 0.172 in w. Equation
(3.8) therefore gives a uniform base Lipschitz constant for g_x
on this whole ball. On the compact torus it gives a uniform
base Holder constant of exponent 1/2 as well.

Starting with the zero section, iterate

$$
 w^{(n+1)}(x)=g_{\Psi^{-1}x}
                         (w^{(n)}(\Psi^{-1}x)).
$$

For their Holder seminorms the explicit bound is

$$
 [w^{(n+1)}]_{1/2}
 \le0.172\sqrt8\,[w^{(n)}]_{1/2}+C\sqrt8.
 \tag{3.10}
$$

Since `0.172 sqrt(8)<0.487<1`, the seminorms stay bounded uniformly
in n and h. The existing uniform contraction convergence then
implies the same bound for w_h. Equation (1.3), (3.8), and the
logarithm on the disk `|gamma-1|<0.0002` prove

$$
 \boxed{\displaystyle
 \sup_{0<h<h_0}\|\log\gamma_h\|_{C^{1/2}}<\infty.}
 \tag{3.11}
$$

This is a regularity assertion about the actual scalar, with a
constant independent of N. It does not assert differentiability
of the invariant graph.

## 4. Matched primitive words for the actual map

### 4.1. The concrete coding and a fixed interior loop

Use the twelve-edge Berg coding of Section 1 of the frozen
quantitative-pressure file. Its incidence matrix is

$$
 C=\begin{pmatrix}3&2\\4&3\end{pmatrix},
$$

and its linear factor map satisfies `pi sigma=S pi`. Agreement
of edges at `-n,...,n` gives

$$
 d(\pi x,\pi y)\le10\lambda^{-n}.
 \tag{4.1}
$$

The same estimate holds for the chosen lifts in a common rectangle:
the cylinder construction is an intersection of nested lifted
rectangles, not merely an estimate after minimizing over deck
translations. The coding is one-to-one off all iterates of the
partition boundaries and has fibers of size at most four everywhere.
The primary geometric input and its hypotheses were checked in
that frozen file; the reference is Siemaszko--Wojtkowski,
*Counting Berg partitions*, Nonlinearity 24 (2011), 2383--2403,
Sections 2 and 4, <https://arxiv.org/pdf/1007.3984>.

The stable and unstable boundary spines lie on the stable and
unstable leaves of the origin. All their iterates lie on those
same leaves. The only periodic point on either leaf is the origin:
its appropriate forward or backward iterates tend to zero, whereas
a nonzero finite periodic orbit cannot do so.

The point `(1/2,0)` is fixed by S and is not zero. Thus it lies off
all these boundaries and has a unique itinerary. Since it is
fixed, that itinerary is a single loop edge, denoted 0, at a vertex
i. There are exactly three i-to-i edges. Denote the other two by
a and b. There also exists a two-edge path c from i to the other
vertex j and back to i, since both off-diagonal incidence entries
are positive. Fix one such path.

For every integer R>=1 form the cyclic edge words

$$
 w_R=a0^{2R}b0^{2R}c0^{2R},\qquad
 w'_R=a0^{2R}c0^{2R}b0^{2R}.
 \tag{4.2}
$$

Both lengths are

$$
 m_R=6R+4.
 \tag{4.3}
$$

There is exactly one visit to vertex j per period. Thus neither
word is a repetition of a shorter word. They are not cyclic
permutations of one another: the unique excursion c fixes a cyclic
anchor, and the order of the distinct edges a,b is then reversed.
For `m_R>4`, neither periodic code can represent the origin,
because its shift orbit would contain more than four different
codes in one fiber. They consequently have unique geometric
itineraries and represent different primitive S-orbits of period
m_R. By the homeomorphism H and inversion of time in (1.1), they
give different primitive orbits p_R,p'_R of the actual Psi with
that same period.

### 4.2. Local scalar variation on these codes

The actual coding is `H pi`, with Psi acting as `sigma^-1`.
In lifted coordinates a forward S edge obeys
`S z_j=z_(j+1)+n_e`, with n_e in a fixed finite set. The exact lift
conjugacy and the lattice equivariance of H give

$$
 \Psi(H z_j)=H z_{j-1}-L n_{e_{j-1}}.
 \tag{4.4}
$$

Thus the inverse-edge integers in (2.6) also belong to a fixed
finite set and are constant once the preceding edge is fixed.
There is no m-dependent choice of chart or deck integer in the
local scalar construction.

Combining (4.1) with the spatial 1/2-Holder bound for H shows that
the chosen actual lifts vary by at most `C lambda^(-n/2)` when
the central words agree to n. On the finitely many bounded charts,
the phase in parentheses in (2.6) has bounded first derivatives.
Therefore

$$
 |\eta_N(x)-\eta_N(y)|
 \le C N\lambda^{-n/2}
 \tag{4.5}
$$

when the needed inverse edge is common. An index loss of one in n
is harmless and may be absorbed in C. Equations (3.11) and (4.1)
give also

$$
 |\log\gamma_h(H\pi x)-\log\gamma_h(H\pi y)|
 \le C\lambda^{-n/4}.
 \tag{4.6}
$$

All constants here are independent of N,m,n. Since
`lambda^(-1/4)<2/3`, both right sides may be enlarged by replacing
their decays with `theta^n`, where `theta=2/3`.

### 4.3. The exact matching permutation

Rotate each cyclic word in (4.2) into three cells of the form

$$
 0^Ra0^R,\qquad0^Rb0^R,\qquad0^Rc0^R.
 \tag{4.7}
$$

Match cells of the same type between the two words and positions
with the same offset inside each cell. This gives a permutation
of all m_R positions. For every matched pair of positions, the
corresponding shifted bi-infinite periodic codes agree at all
edges `-R,...,R`. Inside the cell they coincide identically. If
that window passes a cell boundary, it reaches at most the R
zero edges adjacent to the boundary of the next cell, regardless
of the next excursion's type. This proves the agreement including
positions at either end of a cell.

Scalar factors commute. By (2.6), (4.5), and telescoping a product
of unit-modulus scalars,

$$
 \left|\frac{\omega_{p_R,N}}{\omega_{p'_R,N}}-1\right|
 \le C N m_R\theta^R.
 \tag{4.8}
$$

The products can be indexed by forward shifts of the codes,
although Psi corresponds to backward shifts: a full periodic
orbit contains the same list of states in either direction.
Equation (4.6) and the same matching permutation give

$$
 \left|\log\frac{\Gamma_h(p_R,m_R)}
                         {\Gamma_h(p'_R,m_R)}\right|
 \le C m_R\theta^R.
 \tag{4.9}
$$

Here the expression on the left means the difference of the sums
of the fixed local branches `log gamma_h`; exponentiating it is
exact. No assertion about a global branch of the orbit phase is
needed.

For large R with `Nm_R theta^R<=1`, (1.7)--(4.9) prove

$$
 \boxed{\displaystyle
 \left|\frac{a_{p_R,N}}{a_{p'_R,N}}-1\right|
 \le C N m_R(2/3)^R.}
 \tag{4.10}
$$

Choose `R_N=floor(N/6)`. Then `m_N=6R_N+4` lies between `N-1`
and `N+4`; for odd N its possible differences from N are
`-1,1,3`. In particular (4.10) gives an actual pair of different
primitive orbits at a time of order N with relative error

$$
 O\!\left(N^2\exp\left[-\frac{\log(3/2)}6N\right]\right).
 \tag{4.11}
$$

### 4.4. The size of this contribution

Equation (1.4) alone gives, with ample numerical room,

$$
 6^{-m}\le|a_{p,N}|^2\le5^{-m}.
 \tag{4.12}
$$

Indeed `(1-0.0002)^2/lambda>1/6` and
`(1+0.0002)^2/lambda<1/5`. For the pairs just constructed, the
sum of the two ordered cross contributions to `|mathcal P_m|^2`
is `2m^2 Re(a_p conjugate(a_p'))`. Equations (4.10)--(4.12)
therefore bound it, for all sufficiently large N, between

$$
 m_N^2 6^{-m_N}\quad\hbox{and}\quad 2m_N^2 5^{-m_N}.
 \tag{4.13}
$$

It is positive and exponentially small. Establishing a large
number of such pairs with controlled multiplicities, or a
compensating contribution from other pairs, would require an
additional argument. None is silently assumed here.

## 5. The exact doubled transfer for the original matrices

We now work solely in the original finite-dimensional quantum
space. On `M_N(C)` use the Hilbert--Schmidt inner product
`<X,Y>=Tr(X^*Y)` and the orthonormal Weyl basis

$$
 E_v=N^{-1/2}T_N(v),\qquad v\in(\mathbb Z/N\mathbb Z)^2.
$$

Aggregate the actual finite Fourier coefficients of A_N as

$$
 A_N=\sum_u\mathfrak a_N(u)T_N(u).
$$

The support before reduction modulo N is contained in
`|u_1|<=1, |u_2|<=9`. Aliasing, if any, is included in
`mathfrak a_N`; it changes no identity below. The direct Fourier
l1 bound is less than 2: `||r||_(Fourier,l1)<=4`, so the four terms
of f and the subtraction of 1/10 give at most
`1+0.4+0.04+0.04+0.1<2`.

For `sigma(u,v)=u_1 v_2-u_2 v_1`, direct multiplication of the
operators in the question gives

$$
 T_N(u)T_N(v)=e_N(\bar2\sigma(u,v))T_N(u+v).
 \tag{5.1}
$$

Consequently the self-adjoint operator `G_N=ad_(A_N)` has the
finite-hop matrix

$$
 G_NE_v=\sum_u\mathfrak a_N(u)
  \big[e_N(\bar2\sigma(u,v))-e_N(-\bar2\sigma(u,v))\big]
       E_{u+v},\qquad \|G_N\|<4.
 \tag{5.2}
$$

The word self-adjoint here refers to the Hilbert--Schmidt space:
cyclicity of the finite trace proves
`<X,[A_N,Y]>=<[A_N,X],Y>`.

Direct substitution in the kernel M_N proves

$$
 M_NT_N(v)M_N^*=T_N(Sv).
 \tag{5.3}
$$

For completeness, comparing `M_N T_N(a,b)` with
`T_N(a',b') M_N`, the coefficients of the two coordinate
variables give `a'=3a+4b`, `b'=2a+3b`; the remaining constants
then agree by (5.1). All divisions are modular divisions by
units. Let `P_SE_v=E_(Sv)`. The exact doubled transfer is

$$
 \boxed{\displaystyle
 \mathscr C_N:=\operatorname{Ad}U_N
 =\exp(i\tau N G_N)P_S.}
 \tag{5.4}
$$

There is no asymptotic approximation in (5.4). Its trace is

$$
 \operatorname{Tr}_{M_N}\mathscr C_N^m
       =|\operatorname{Tr}U_N^m|^2.
 \tag{5.5}
$$

To see this, diagonalize U_N. On the matrix unit between its jth
and kth eigenvectors, `mathscr C_N` has eigenvalue
`exp(2 pi i(theta_j-theta_k))`; summing their mth powers gives
(5.5), with all multiplicities included.

### 5.1. A rigorous limit of operator-norm contraction

The operator (5.4) is unitary. The vector `I/sqrt(N)` is fixed.
Its orthogonal complement is invariant and nonzero for N>=2,
and on that complement

$$
 \|\mathscr C_N^m\|=1\qquad(m\ge1).
 \tag{5.6}
$$

The entire fixed subspace is the commutant of U_N. Its dimension
is `d_N=sum multiplicity(theta)^2>=N`. Even after this full
subspace is removed, the remaining subspace, when nonzero, is
unitary and has spectral radius one. Thus no bound
`C_N eta^m`, with eta<1 and finite C_N, can hold for every m on
that subspace, in any equivalent norm: an eigenvector with a
unit-modulus eigenvalue already contradicts it as m tends to
infinity.

This rules out a strict long-time norm contraction on the actual
central quantum space (5.4), including after removal of all its
fixed matrices. It does not rule out a contraction on a different
classical transfer space that does not contain this quantum
representation. To obtain the desired quantum conclusion from
such a space, the error or the missing central component would
still have to be estimated. Trace cancellations, unlike norm
contraction, remain possible in (5.5).

## 6. The exact positive resolvent and the first missing estimate

For `0<r<1`, set

$$
 R_N(r)=(I-r\mathscr C_N)^{-1}.
$$

Let `||.||_(HS,sup)` denote the Hilbert--Schmidt norm of a linear
operator on the N^2-dimensional Hilbert--Schmidt space, to
distinguish it from the norm of an N-by-N matrix. Expanding the
two absolutely convergent geometric series and using (5.5)
gives the exact positive identity

$$
 \boxed{\displaystyle
 \|R_N(r)\|_{\mathrm{HS,sup}}^2
 =\frac{N^2+2\sum_{m\ge1}r^m|p_{m,N}|^2}{1-r^2}.}
 \tag{6.1}
$$

In detail, terms with equal powers contribute `N^2/(1-r^2)`.
For a difference m>0, the two possible orders contribute
`2r^m Tr(mathscr C_N^m)/(1-r^2)`. Their traces are real
nonnegative by (5.5), so no conditional convergence is involved.

With `r=exp(-2s/N)`, the boundedness of the Abel pair statistic
for a fixed s>0 is therefore equivalent to

$$
 \boxed{\displaystyle
 \|R_N(e^{-2s/N})\|_{\mathrm{HS,sup}}^2=O_s(N^3).}
 \tag{6.2}
$$

This estimate remains unproved for the original family. The CUE
value asked for in the question would yield the more precise
limit

$$
 N^{-3}\|R_N(e^{-2s/N})\|_{\mathrm{HS,sup}}^2
 \longrightarrow
 \frac{1+(1-e^{-2s})/(2s^2)}{4s}.
 \tag{6.3}
$$

The operator norm of this same resolvent is exactly

$$
 \|R_N(r)\|=(1-r)^{-1},
 \tag{6.4}
$$

since unitarity gives the upper bound and the fixed vector gives
equality. Thus improving that operator norm is not a route to
(6.2). The finite-dimensional elementary bounds are

$$
 \frac{d_N}{(1-r)^2}
 \le\|R_N(r)\|_{\mathrm{HS,sup}}^2
 \le\frac{N^2}{(1-r)^2}.
 \tag{6.5}
$$

At the indicated radius they range from order N^3 to order N^4.
The actual pressure and frame estimates improve the upper bound
to `O_s(N^4/log N)`; they do not give the missing factor
`N/log N` in (6.2). More precisely the frozen frame argument,
with its growth exponent allowed to decrease to P_*, gives

$$
 \limsup_{N\to\infty\atop N\text{ odd}}
 \frac{\log N}{N^4}
 \|R_N(e^{-2s/N})\|_{\mathrm{HS,sup}}^2
 \le\frac{P_*}{4s^2}.
 \tag{6.6}
$$

### 6.1. The exact orbit replacement controls the whole Abel tail

Although the principal trace sum contains exponentially many
orbits, its exact scalar remainder can be removed from this
particular infinite quadratic statistic without an unproved
tail assumption. From (1.5) and `|p_(m,N)|<=N`,

$$
 \big||p_{m,N}|^2-|\mathcal P_{m,N}|^2\big|
 \le4Nq_*^m+4q_*^{2m}.
 \tag{6.7}
$$

For every `0<r<1`, summing gives

$$
 \sum_{m\ge1}r^m
 \big||p_{m,N}|^2-|\mathcal P_{m,N}|^2\big|
 \le\frac{4Nq_*}{1-q_*}
       +\frac{4q_*^2}{1-q_*^2}<3N+1.
 \tag{6.8}
$$

Hence the normalized Abel pair statistic may be replaced by
the full signed principal-orbit sum with error at most
`3/N+1/N^2`, including its infinite tail. This is an actual
approximation theorem for the original family. It supplies no
bound for that signed principal sum itself.

## 7. What this attempt establishes, and where it stops

The fixed nonlinear dynamics have not removed all coherent
distinct-orbit pairs: (4.10) exhibits them explicitly at a
time of order N and retains their exact quantum amplitudes.
Their size (4.13) prevents this observation from becoming a
counterexample to the desired statistics. A count with sufficient
total mass and a control of the remaining pairs are absent.

The exact finite quantum transfer (5.4) also does not have the
strict norm decay that a direct transfer-contraction argument
would need on its central quantum space. Removing invariant
vectors does not fix that difficulty. The quantity that still
could have the required cancellation is the trace, equivalently
the Hilbert--Schmidt resolvent in (6.2).

Equations (6.2) and (6.3) are statements of the first missing
estimate and desired limit, respectively; they are not hypotheses
used in any proof above. Neither the new explicit positive
off-diagonal pairs nor the previously proved pressure gap yields
them. Even (6.2), if proved, would give only boundedness of this
one smoothed pair statistic, not `H_diag` at all orders.
