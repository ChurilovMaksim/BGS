# Uniform cancellation of macroscopic coordinate-translation path pairs

Author proof candidate, 7 October 2026. Actual odd-dimensional U_N at literal
tau=10^-80. Separate workspace; no canonical files changed. Independent review
is pending. The full off-charge defect and TRACE-005 remain open.

## 1. Exact selected family and theorem

Use the unchanged matrices of `mathematics/fixed_map_path_model.md` in the
canonical BGS repository. All matrix norms in this note are ordinary induced
l2 norms. Indices in U_N are modulo N. For c in Z/N define

 B_(N,c)(j,k) = U_N(j,k) conjugate(U_N(j+c,k+c)).                 (T1)

For a cyclic word x=(x_0,...,x_(m-1)), let A_U(x)=product_j U_N(x_j,x_(j+1)).
Direct multiplication, with every repeated coordinate retained, gives

 Tr B_(N,c)^m = sum_x A_U(x) conjugate(A_U(x+c)).                (T2)

For every fixed 0<delta<1/2,

 sup_(delta<=c/N<=1-delta) ||B_(N,c)|| -> 0                     (T3)

as odd N tends to infinity. In particular there is an existential N_delta
such that the supremum is at most 1/2 for N>=N_delta. No effective startup
or rate uniform as tau goes to zero is claimed. The conclusion includes all
rational alias points in this closed macroscopic interval.

Consequently, for fixed 0<a<b<infinity, arbitrary sets C_(N,m) contained in
that macroscopic interval, and bounded w supported in [a,b],

 |N^-2 sum_m w(m/N) sum_(c in C_(N,m)) Tr B_(N,c)^m|
                  <= C_(a,b,w) N 2^(-aN) -> 0.                (T4)

This is an aggregate for a growing O(N)-cardinality family, with the original
pair normalization. It follows from cancellation in the actual complex
kernels, not from assigning independent phases to U.

## 2. Exact compression and the cheapest cat counterexample

On End(C^N), with ordinary Hilbert--Schmidt inner product, the N matrix units
E_j^c=|j><j+c| form an orthonormal set. Compression of the unitary superoperator
Ad(U_N) to their span has matrix B_(N,c). Hence ||B_(N,c)||<=1 exactly, at every
finite N. The subspace is not assumed invariant.

At zero coupling, write h=2^-1 modulo N. Direct subtraction of the prescribed
cat quadratic phases gives

 B_c^cat(j,k)=N^-1 e_N(h*c*(j+k+c)).                            (T5)

For c!=0, this has norm 1, while

 (B_c^cat)^2(j,l)=N^-2 e_N(h*c*(j+l+2c)) sum_k e_N(c*k)=0.      (T6)

Thus perturbation in the one-step norm is not the proposed mechanism, and
nothing asserts ||B_c^cat||->0. At fixed nonzero tau the nonlinear mixed phase
provides the different mechanism below. Tiny tau does not justify uniform
entrywise relative closeness when N*tau is large.

## 3. Inherited actual parametrix, with translated indices

The accepted `four_branch_parametrix.md` gives, on enlarged fixed real charts,

 U_N(j,k)=e(3N/8)/(2 sqrt N) sum_(r=0)^3
              e(N S_r(tau,x,y)) a_(r,N)(tau,x,y)+O(N^-3/2),
 x=j/N, y=k/N, a_(r,N)=a_(r,0)+N^-1 a_(r,1),                   (T7)

with all needed finite amplitude derivatives uniformly bounded. Its exact
lattice gluing makes (T7) valid for the lifts j+c,k+c even when these exceed
N. Thus put u=c/N and evaluate the second factor at (x+u,y+u) in [0,2]^2;
no discontinuous branch replacement is needed at lattice wraparound.

Multiplying (T7) and its translated conjugate decomposes B_(N,c) into sixteen
kernels N^-1 b_(r,s,N,u)(x,y)e(N Phi_(r,s,u)(x,y)), plus an entrywise O(N^-2)
remainder, hence an O(N^-1) operator remainder. Amplitudes are uniformly
smooth and bounded for u in [0,1]. The phases are

 Phi_(r,s,u)=S_r(tau,x,y)-S_s(tau,x+u,y+u).                     (T8)

Their initial mixed derivative is zero because (S_r^0)_xy=1/4 for every r.
The initial phase is therefore separable and may be removed by unitary
left and right diagonal multipliers; no operator norm changes.

## 4. Two exact Fourier witnesses eliminate all macroscopic aliases

Write R_r(t,x,y)=S_r(t,x,y)-S_r^0(x,y). The actual HJ equation and initial
condition imply exactly

 R_r(t,x,y)=R_0(t,x,y+r),                                     (T9)

since S_r(t,x,y)=S_0(t,x,y+r). Every R_r is 4-periodic separately in x,y by
the accepted phase gluing. Use normalized Fourier coefficients on [0,4]^2.
Set frequencies

 nu_0=(-3/4,1/4), nu_1=(1/4,1/4).

The actual symbol's momentum-positive coefficients are

 ghat(0,1)=(-3-4i)/1000,
 ghat(1,1)=(3+4i)/2000.                                      (T10)

From S_t(0)=g(x,(y+r-3x)/4)/(2pi), the first time derivatives of the Fourier
coefficients of R_(0,xy) at these two frequencies have moduli

 L_0=3pi/1600, L_1=pi/3200.                                  (T11)

The inherited actual C2 Taylor remainder is at most (10^50/2)t^2. At the
literal tau=10^-80, therefore, both exact Fourier coefficients A_i of
R_(0,xy)(tau) are nonzero and satisfy

 |A_i| >= pi*tau/6400.                                      (T12)

This is a specified-time certificate, not a formal nonzero first derivative.

By (T9) and exact Fourier translation, the corresponding coefficients of
Phi_(r,s,u),xy are exactly

 A_i [ e(r/4)-e(s/4+(i-1/2)u) ], i=0,1.                     (T13)

Crucially the whole nonlinear remainder has the SAME translation factor.
It is not estimated by an error independent of u and branch difference.
Let z=e((s-r)/4-u/2). The two bracket moduli in (T13) are |1-z| and
|1-z e(u)|. The triangle inequality gives

 max(|1-z|,|1-z e(u)|) >= |1-e(u)|/2
                            >=2 dist(u,Z).                  (T14)

Thus at least one coefficient has modulus >=pi*tau*dist(u,Z)/3200.
For every r,s and every u in (0,1), Phi_xy is a nonzero real-analytic function.
In particular there are no exceptional nonintegral rational translation
parameters. On [delta,1-delta] the displayed coefficient lower bound is
uniform. Separately, the same inherited C2 bounds give

 sup_(r,s,u,x,y)|Phi_(r,s,u),xy| <=2*10^9 tau+10^50 tau^2<1/4. (T15)

The lower nonidentity and upper alias-safety bounds have separate roles.

## 5. Uniform-in-translation version of the inherited TT* argument

The accepted local lemma in `four_branch_parametrix.md`, Section 6, states:
for a smooth supported amplitude and real phase with mixed derivative of
one sign between fixed positive c and C<1/4, the matrix
N^-1 a(i/N,j/N)e(N phi(i/N,j/N)) has norm O(sqrt(log(2N)/N)).
The proof controls all discrete aliases by phase increments separated from
integers. Its analytic-zero-set corollary yields norm o(1) for a fixed
nonzero analytic mixed derivative with that upper bound.

Here this corollary is uniform in u in the compact interval. To prove that,
take any sequence u_N in [delta,1-delta] and pass to a convergent subsequence
u_N->u_*. Fix one branch pair. At u_* the analytic zero set of Phi_xy has
area zero by (T13)-(T14). Remove a smooth neighborhood of it and the chart
boundary of arbitrarily small area. The omitted N^-1-amplitude kernel has
limiting ordinary HS norm at most C times the square root of that area,
uniformly in u_N, by the uniform amplitude bounds and Riemann sums.

Cover the remaining compact set by finitely many rectangles with a smooth
partition of unity. At u_* every rectangle has a mixed derivative of fixed
sign bounded away from zero. Continuity in u preserves half that lower bound
for all sufficiently large N in the subsequence. All derivative and amplitude
bounds used by the local TT* proof are uniform there. The sum of the good
pieces is o(1). First let N tend to infinity and then shrink the omitted
area. This gives o(1) for the subsequence. Compactness now proves the uniform
claim for each of sixteen pairs, and their finite sum plus O(N^-1) proves T3.

This argument does not require uniform bounds on the number of zeros or a
finite-type exponent. Analyticity, a nonzero limiting phase at every compact
parameter limit, and the separately verified alias bound suffice.

## 6. Once counting and an actual off-charge subset

The coordinate expansion gives exactly

 |Tr U_N^m|^2-E_theta|Tr(D_theta U_N)^m|^2
 =sum_(x,y: occupation(x)!=occupation(y)) A_U(x) conjugate(A_U(y)). (T16)

For fixed x, x+c determines c uniquely from its first coordinate. Therefore
the ordered-pair union over c in any C_(N,m) in T2 is already once counted;
no cyclic rotations or marked-cut multiplicities are inserted.

Translation by c has order d=N/gcd(c,N), and partitions the coordinate labels
into cycles of size d. If occupation(x+c)=occupation(x), that integer
occupation vector is constant on every such cycle. Hence d divides m.
In particular, if d>m, every pair (x,x+c) in T2 lies in the off-charge set.

For any fixed 0<a<b<1, choose

 C_(N,m)={c:delta<=c/N<=1-delta, gcd(c,N)=1}.

Then d=N>m, so T4 is a genuine aggregate cancellation theorem for an exact
subset of the deterministic off-charge defect throughout this band. More
generally any chosen c with ord(c) not dividing m is admissible. There is
no assumption of independent coordinate phases in the dynamics; their
expectation in T16 merely identifies which actual path pairs are off-charge.

The family may be enlarged to all macroscopic translations in T4 at any
positive time band, but that enlarged signed sum can include balanced pairs.
One cannot then remove the balanced mask without a new argument. In
particular this note makes no off-charge conclusion above the plateau.

## 7. Aggregate, dependence, and precise remaining boundary

For all sufficiently large odd N, T3 implies |Tr B_c^m|<=N*2^-m uniformly
for the chosen c. There are at most N choices of c and O_b(N) relevant m.
Taking absolute values only AFTER the signed path contraction T2 proves T4.
No estimate is claimed for individual |A_U(x) A_U(x+c)| sums.

Prior ownership: the finite-difference WKB construction, amplitude/remainder
bounds, actual-time C2 certificate, and alias-safe local TT* method belong
to the accepted FM-021/FM-022 support. The new specialization is the exact
translated-path compression, the two-mode all-parameter alias exclusion,
and the once-counted off-charge family with its aggregate normalization.
No broad priority claim is made. FM-023 excludes different arithmetic
translation algebras in Weyl operator space; it is not this path-family
statement and is not a dependency of this proof.

The boundary layers c/N->0 or1 are not covered by T3. Other path pairs,
including almost all off-charge pairs, the remaining stationary-label
N-torsion portions, the plateau correction, and every higher factorial
comparison remain unestimated. No dictionary between this actual-U path
family and TRACE-019's WKB stationary-label masks is asserted. This is one
larger uniformly controlled signed family, not a full-sum bound.
