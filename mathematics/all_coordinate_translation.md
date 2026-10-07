# Uniform finite-power contraction for every nonzero coordinate translation

Author proof candidate, 7 October 2026. Actual odd-N U_N, fixed tau=10^-80.
Independently reviewed; see record/all_coordinate_translation_review.md. No canonical edit or publication. This enlarges
the frozen macroscopic translated-path family; it does not estimate the full
off-charge defect, plateau, or higher factorial hierarchy.

## A1. Exact statement and inherited inputs

Use B_(N,c)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+c)), c modulo N, with the exact
unchanged quantizer. There exist L in N, 0<rho<1, and N0, depending only on the
fixed actual map, such that

 sup_(c!=0 mod N) ||B_(N,c)^L|| <= rho,  odd N>=N0.             (A1)

Thus there exist C<infinity and gamma>0, independent of N,c,m, with

 |Tr B_(N,c)^m| <= C N exp(-gamma m), m>=1, c!=0.              (A2)

N0, L, rho and gamma are existential; no numerical startup or uniformity as
tau->0 is claimed. The theorem is about powers of each separate compressed
kernel. It is not a bound on products whose offset c changes between steps.

Inputs inherited with their existing review boundaries:
1. `four_branch_parametrix.md`: exact raw four-branch gluing, actual fixed-time
   WKB expansion, smooth amplitudes, O(N^-3/2) entry error and alias-safe TT*.
2. Frozen `../translation_family_proof.md`, SHA256
   49a24af2ca9e9628681ce08fcd023528f9b3bc5fbc578c7ec8cdfa11918b4f23:
   its exact two-mode translated-phase certificate and macroscopic norm
   theorem. That candidate has a separately accepted independent audit. The needed certificate is restated in A2 below.
3. `frozen_operator_transfer_coercivity.md` (FM-018), O8 at j=1 and O9:
   one-step actual-symbol Egorov and normalized trace convergence; O11:
   mixing for normalized area of the ACTUAL nonlinear G, with checked
   Parry--Pollicott source mapping and inherited FM-001/FM-006 prerequisites.
   These are inherited results, not re-audited analytic chains in this note.

The canonical convention is
G=S composed with Phi_g^(tau/(2pi)), S=[[3,4],[2,3]],
Ad(U_N) Op_N(a)=Op_N(a composed with G)+O_op(N^-2 ||a||H5).
The inverse convention is not silently substituted.

## A2. Exact reductions and the nonzero actual phase certificate

Compression of Ad(U_N) to the ordinary-HS orthonormal units |j><j+c| gives
B_(N,c), so ||B_(N,c)||<=1 exactly. Let T_c act on vectors by
(T_c f)(j)=f(j+c). Then direct entries give

 B_(N,-c)=T_(-c) conjugate(B_(N,c)) T_c.                        (A3)

The same relation holds for powers and their norms. It suffices to treat
integers 1<=c< N/2, u=c/N in (0,1/2).

The actual four-branch expansion decomposes B into sixteen kernels

 (4N)^-1 a_(r,N)(x,y) conjugate(a_(s,N)(x+u,y+u))
      e(N[ S_r(x,y)-S_s(x+u,y+u)]),                           (A4)

and an O(N^-1) operator remainder, uniform for u in [0,1/2]. All phases and
amplitudes are at the fixed tau; a_(r,N)=a_(r,0)+N^-1 a_(r,1). The lifted
coordinates x+u,y+u belong to a fixed enlarged chart. Exact lattice gluing
identifies them with the wrapped matrix indices, with no discontinuous
branch reassignment in A4.

Put R_r=S_r-S_r^0. Exact HJ uniqueness gives R_r(x,y)=R_0(x,y+r), and these
corrections are 4-periodic separately in x,y. For
nu_0=(-3/4,1/4), nu_1=(1/4,1/4), the actual Fourier coefficients A_i of
R_(0,xy) obey |A_i|>=pi*tau/6400. Their source is the centered physical g:

ghat(0,1)=(-3-4i)/1000, ghat(1,1)=(3+4i)/2000,

with first-time mixed-phase coefficient moduli 3pi/1600 and pi/3200.
The C2 Taylor remainder is at most (10^50/2)*tau^2, smaller than half the
second signal at tau=10^-80. Therefore the Fourier coefficients of the
mixed derivative of Phi_(r,s,u)=S_r(x,y)-S_s(x+u,y+u) are exactly

 A_i[e(r/4)-e(s/4+(i-1/2)u)].                                (A5)

All nonlinear remainders carry this same translation factor. At u=0 and
r!=s, A5 is nonzero because e(r/4)!=e(s/4). At every u in (0,1), one of the
two coefficients is nonzero: the two bracket phases differ by e(u).
Separately the inherited fixed-time bound gives |Phi_xy|<1/4 uniformly.
These statements retain every raw branch pair and all nonintegral rational
translation parameters.

## A3. Scaled alias-safe TT* with the near-diagonal cutoff retained

Here is the local lemma needed when c grows but c/N shrinks. Let ell be an
integer with 1<=ell<=N/2, and consider

 T_(ij)=N^-1 b_N(i/N,j/N)e(ell psi(i/N,j/N)),

on a fixed rectangular support with uniformly bounded required amplitude and
phase derivatives. Suppose psi_xy has one sign with
0<d0<=|psi_xy|<=d1, and (ell/N)*d1<1/4. Then

 ||T||^2 <= C[ N^-1 + (1+log(2ell))/ell ].                    (A6)

Constants may depend on d0,d1 and the derivative bounds, not on N or ell.

Proof. For distinct rows x=i/N,x'=i'/N put h=|x-x'|=k/N and
f(y)=psi(x,y)-psi(x',y). It has derivative of constant sign between d0*h
and d1*h in modulus. The discrete phase increments of ell*f(j/N) lie
between (ell/N)*d0*h and (ell/N)*d1*h in modulus, all below 1/4. They are
therefore separated from every integer by at least (ell/N)*d0*h.
Their total variation on the column interval is O((ell/N)*h), by the
uniform bound on psi_xyy. The same elementary summation-by-parts proof as
the inherited TT* lemma bounds the weighted unnormalized column sum by
C*N/(ell*h). The amplitude variation is uniform, including the product of
the two row amplitudes. Thus

 |(TT*)_(ii')| <= C/(ell*k), i!=i'.

The trivial absolute column sum is at most C/N for all pairs. Hence

 |(TT*)_(ii')| <= C min(1/N,1/(ell*k)), i!=i',
 (TT*)_(ii)<=C/N.                                            (A7)

Sum the trivial bound for k<=N/ell; its cost is O(1/ell). For the other k,
the harmonic sum starts at order N/ell and ends at N, so costs
O((1+log(2ell))/ell), with no log N. Schur gives A6. Negative mixed
derivatives follow by complex conjugation. This argument is discrete and
retains the sampling factor ell/N; a continuum estimate is not substituted.

The usual analytic-zero-set cutoff extends the conclusion to a family
psi_v converging smoothly to psi_*, provided psi_*,xy is analytic and not
identically zero and ell->infinity, N->infinity, while the local alias
bound holds. Remove a small smooth neighborhood of the limiting zero set,
use A6 on finitely many complementary rectangles, and bound the removed
piece in ordinary HS norm by its uniform amplitude bound times square root
of the removed area. First pass to the sequence limit, then shrink the area.
No uniform lower bound is claimed on the removed region.

## A4. Every growing translation has small one-step norm

Claim: for every sequence of odd N tending to infinity and integers
1<=c_N<N/2 with c_N->infinity,

 ||B_(N,c_N)|| -> 0.                                         (A8)

Pass to any subsequence where u_N=c_N/N converges to u_* in [0,1/2]. If
u_*>0, the frozen macroscopic theorem applies on a compact interval away
from zero and one. Suppose u_*=0.

For r!=s, A5 remains nonzero at u=0, so the parameter-uniform inherited
TT* argument at frequency N makes the corresponding A4 term o(1).
For r=s, write Phi_(r,r,u)=u Psi_(r,u), where the exact integral formula is

 Psi_(r,u)(x,y)=-int_0^1 (partial_x+partial_y)
                            S_r(x+tu,y+tu) dt.               (A9)

This defines a smooth real-analytic family down to u=0. Its initial cat
phase (x+y+r)/2+u/2 is separable, so it does not affect the mixed derivative.
At u=0, the selected mixed-derivative coefficients of Psi are

 -2pi i sigma_i A_i e(r/4), sigma_0=-1/2, sigma_1=1/2.         (A10)

and both are nonzero. In A4 the effective oscillation parameter is now
ell=c_N, since N*u_N=c_N exactly. On each good rectangle the mixed
derivative of Psi has a uniform positive lower bound and bounded upper
bound. Since u_N->0, the sampling alias bound u_N*d1<1/4 holds eventually.
All needed higher derivatives and amplitudes are uniformly bounded by A9
on the fixed enlarged charts. The scaled cutoff lemma gives norm o(1).
The finite branch sum and O(N^-1) remainder prove A8. The subsequence
argument covers every original sequence, including slow c_N growth.

Equivalently, for every epsilon>0 there exist C_epsilon and N_epsilon such
that for all odd N>=N_epsilon and C_epsilon<=c<N/2,

 ||B_(N,c)||<=epsilon.                                       (A11)

If this were false, choose counterexamples with c>=n,N>=n successively;
these contradict A8. This simultaneous two-cutoff quantifier is essential.

## A5. Fixed-c operator-norm limit, including possible escaping aliases

Fix a positive integer c. On l2_N use inner product N^-1 sum_j conjugate(f_j)g_j;
this changes no matrix operator norm. Let J_N:l2_N->L2([0,1]) send a vector
to its constant value on [j/N,(j+1)/N). J_N is an isometry. Extend B by

 mathcal B_(N,c)=J_N B_(N,c) J_N*,

which is zero on the orthogonal complement of the step functions. Then

 ||mathcal B_(N,c)-K_c|| ->0                                 (A12)

in operator norm, where K_c is the integral operator with kernel

 k_c(x,y)=1/4 sum_(r=0)^3 |a_(r,0)(x,y)|^2
                    e(-c(partial_x+partial_y)S_r(x,y)).       (A13)

Proof. For fixed c, u=c/N->0. Every r!=s term is o(1) in operator norm by
the nonzero limiting phase in A5. This removes potential high-frequency
alias vectors; weak Egorov convergence alone would not establish A12.
For r=s, smooth Taylor expansion gives uniformly on the enlarged chart

 N[S_r(x,y)-S_r(x+c/N,y+c/N)]
                =-c(partial_x+partial_y)S_r(x,y)+O_c(N^-1),

a_(r,N)(x,y) conjugate(a_(r,N)(x+c/N,y+c/N))
                =|a_(r,0)(x,y)|^2+O_c(N^-1).

Thus this part of the matrix is N^-1 k_c(j/N,k/N)+O_c(N^-2) entrywise,
whose operator error is O_c(N^-1). Under J_N its piecewise constant integral
kernel converges uniformly to k_c on the fixed square, so the difference
converges in HS, hence operator, norm. The inherited remainder is O(N^-1).
This proves A12 for all odd N, with no fixed residue class required: the
common factor e(3N/8) has canceled, and the sole surviving r=s term has no
remaining N-dependent raw branch phase.

The kernel is smooth on the closed chart, so K_c is compact. In fact it
has the correct circle gluing. Under y->y+1, r is shifted by one; reducing
r modulo four adds a phase whose (partial_x+partial_y) derivative is -2.
Under x->x+1, the exact identity S_r(x+1,y)=S_(r-3)(x,y)-2r-2y+3 gives
another derivative -2, together with a branch relabeling. The transport
amplitudes satisfy the matching gluing. All resulting multipliers are
e(2c)=1 because c is integral. Derivatives glue too. Compactness itself
requires only the bounded smooth square kernel, not this stronger periodicity.

## A6. Identification as the exact classical Koopman compression

Let H=L2(T2,dq dp), with normalized area. Define the isometry

 i_c:L2(T)->H, (i_c f)(q,p)=f(q)e(cp),

and let C_G a=a composed with G. The actual G preserves area, so C_G is
unitary. Then the norm limit in A12 is exactly

 K_c=i_c* C_G i_c.                                           (A14)

Here is a source-bound derivation rather than an assumed amplitude formula.
For a trigonometric polynomial f(q)=sum_b fhat(b)e(bq), exact ordinary Weyl
quantization gives

 Op_N(i_c f)_(j,k)=f((j+c/2)/N) 1_(k=j+c mod N).              (A15)

This follows from W_N(c,b)=(-1)^(bc)T_N(c,b): its entry is exactly
e(b(j/N+c/(2N))). It holds for odd c as well as even c. Write F_N(j) for
the midpoint sample in A15. It has normalized HS norm equal to the l2_N
norm of F_N. The actual compression dictionary gives, for polynomials f,g,

 <F_N,B_(N,c) G_N>_l2_N
 =<Op_N(i_cf),Ad(U_N)Op_N(i_cg)>_normalized-HS.                (A16)

FM-018's one-step O8 and normalized trace O9 take the right side to
<i_c f,C_G i_c g>_H. Both observables are fixed smooth functions, so no
growing-frequency Egorov claim is used here. On the left, J_N F_N->f and
J_N G_N->g in L2, including the O(c/N) midpoint shift; A12 therefore takes
it to <f,K_c g>. Trigonometric polynomials are dense, proving A14.
In particular ||K_c||<=1, also independently inherited from A12 and the
exact quantum contraction. No conjugacy-transported substitute measure is
used: the measure is actual invariant normalized area of G.

## A7. No unit-circle eigenvalues, using the accepted actual mixing scope

FM-018 O11 states exponential correlation decay for smooth zero-mean
observables with product Sobolev norms under this very G and normalized
area. Its checked source is Parry--Pollicott Proposition 2.4 and the
Hölder Markov coding, with the actual area/Gibbs identification inherited
from FM-006. The exact check is `literature/frozen_operator_transfer_sources_20261006.md`;
`literature/external_dependencies.json`, EXT-PP-1990, records that mapping.
This note inherits that verified input; it does not infer area mixing from
topological conjugacy alone.

By approximating zero-mean L2 observables with smooth zero-mean observables,
O11 extends to qualitative mixing on L2: unitarity of C_G bounds the two
approximation errors uniformly in time by Cauchy--Schwarz, and then the
smooth correlation tends to zero.

If K_c f=lambda f with |lambda|=1 and f!=0, put h=i_c f and P_c=i_c i_c*.
By A14, P_c C_G h=lambda h. Orthogonal projection and unitarity give

 ||P_c C_G h||=||h||=||C_G h||,

so the perpendicular component is zero and C_G h=lambda h exactly.
But int h=0 because c is a nonzero integer. Its correlation
<h,C_G^n h>=lambda^n ||h||^2 cannot tend to zero, contradicting L2 mixing.
Thus K_c has no eigenvalue of modulus one.

Since K_c is compact, every nonzero spectral value is an eigenvalue and
nonzero spectral accumulation is impossible. Since it is a contraction,
its spectral radius is strictly less than one. Therefore some finite L_c
satisfies ||K_c^(L_c)||<1/2, by the spectral radius formula. A strict
one-step norm inequality is neither needed nor claimed. For the cat
compression, a fixed even c has norm one and square zero, illustrating
why that distinction matters.

## A8. A common finite power for all N and all nonzero c

Take epsilon=1/2 in A11, and enlarge its C to a positive integer C0.
For each of the finitely many positive c<C0, choose L_c as in A7.
Operator-norm convergence A12 implies convergence of these fixed powers,
so for all sufficiently large odd N,

 ||B_(N,c)^(L_c)||<=3/4, 1<=c<C0.

This follows equally from (mathcal B_N)^ell=J_N B_N^ell J_N* and
J_N*J_N=I; no dimension-dependent eigenvector bound is used.
Choose L=max({1} union {L_c:1<=c<C0}). Since every B is an exact contraction,
its L-th power has norm at most 3/4 for these finitely many c. For c>=C0,
A11 gives ||B^L||<=2^-L<=1/2. Finally A3 covers negative representatives.
After increasing one N0 for the finite list, A1 holds with rho=3/4.

Write m=qL+r, 0<=r<L. Contractivity gives ||B^m||<=rho^q
<=rho^-1 exp[-(-log rho)m/L]. Taking |Tr|<=N|| || yields A2 with
C=rho^-1 and gamma=(-log rho)/L. This step is uniform in c and m.

## A9. Once-counted actual-U family and the valid off-charge masks

At every finite N,m,c, direct matrix multiplication gives

 Tr B_(N,c)^m=sum_(x in (Z/N)^m) A_U(x) conjugate(A_U(x+c)).    (A17)

For fixed x the first coordinate of x+c identifies c uniquely. Therefore
the family over any set of c is once counted with no multiplicity factor.
All repeated word coordinates are retained. No cyclic rotations are added.

For every fixed compact positive band [a,b], every bounded supported w, and
arbitrary sets C_(N,m) contained in nonzero residues,

 |N^-2 sum_m w(m/N) sum_(c in C_(N,m)) Tr B_(N,c)^m|
                        <= C_(a,b,w) N exp(-gamma*a*N).       (A18)

This follows by at most N translations and O_b(N) time indices, after the
complex path sum has been contracted exactly. It is not an absolute bound
on the original individual path weights.

The exact independent-coordinate-phase projector dictionary is

 D_(N,m)=|Tr U_N^m|^2-E_theta|Tr(D_theta U_N)^m|^2
       =sum_(occupation(x)!=occupation(y)) A_U(x)conjugate(A_U(y)).

Translation by c has order d=N/gcd(c,N). If occupation(x+c)=occupation(x),
its counts are constant on each d-cycle of labels, hence d divides m.
Consequently the choice

 C_(N,m)={c!=0: ord(c) does not divide m}                      (A19)

makes A18 a genuine signed-family contribution inside the original
unaveraged deterministic off-charge defect, for EVERY positive band [a,b].
Any subset of A19 is equally valid. Unit shifts have order N, so all unit
shifts are admissible whenever N does not divide m; in particular for m<N.
When d divides m, some words are balanced and some may be off-charge; this
note does not apply an occupation mask inside their trace contraction.
There is no claim that every c with d|m is wholly balanced.

Although A18 also controls the unmasked all-translation family, it cannot
justify deletion of balanced pairs or give their separate contribution.
For times divisible by N, A19 can be empty; this honest mask is not silently
replaced by all c. The normalization remains the prescribed N^-2 pair sum.

## A10. Scope and proof ownership

The gain over the macroscopic candidate is control of every nonzero c by
combining effective-frequency cancellation, a genuine norm limit, classical
mixing on that exact limit, and a uniform finite-power argument. The one-step
small-norm conclusion is asserted only for growing c, not uniformly for all c.
No finite quantum norm computation at a rescaled tau enters the proof.

The target TRACE-005 defect still contains almost all other ordered path
pairs. These translations are not stationary-label homoclinic displacements,
and no dictionary with TRACE-019 masks or N-torsion labels is asserted.
Balanced masked pairs, general off-charge pairs, plateau compensation and
higher factorial orders remain open. Every removed family is a subset
statement, not a full-sum estimate. The inherited WKB/TT*, Egorov, and mixing
proofs retain their own external dependencies and review boundaries; no
claim of a new general oscillatory-integral or mixing theorem is made.
