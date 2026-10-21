> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/arithmetic_seven_chain_discriminant_checkpoint.md`. Embedded SHA256: `eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Seven-chain minors: proved block statement and the unresolved confluent term

Research continuation, 20 October 2026. This note records the next exact
arithmetic step and the precise obstruction to extending the proved
simple-spectrum theorem to all dimensions divisible by 7. It does not
assert such an extension.

## 1. A block theorem valid in every dimension divisible by 7

Write N=7n, with n odd. Let h=(N+1)/2 and put

$$
y_s=h+sn,\qquad x_{s,j}=y_s+j\pmod N,
\qquad 0\le s<7,\quad 0\le j<n.
\tag{1.1}
$$

The seven zero hopping edges split A_N into these seven paths. On
each path, gauging by D_n=diag(omega^j), omega=(-3+4i)/5, gives the
real symmetric Jacobi matrix L_s=200 D_n^* A_{N,s}D_n, with diagonal
d_(s,j)=200 V(x_(s,j)/N) and positive internal off-diagonals b_(s,j).
Each L_s has n distinct real algebraic eigenvalues.

**Block theorem.** Fix any two paths s,t, possibly equal. Express the
coordinate block of M_N from path t to path s in orthonormal
eigenbases of L_t and L_s, including the above gauge. Every square
minor of this n-by-n overlap matrix is nonzero.

This allows arbitrary row and column eigenvalue subsets within their
respective paths. No assumption about coincidences between the spectra
of different paths is made.

Here is the full reduction to the proved valuation inequalities. At
the valuation extending 1+2i with v(omega)=1, all d_(s,j) are integral
and every nonzero b_(s,j) has valuation in [0,1/2], by the root-of-unity
factorization of r in the frozen p-adic proof. For a k-element
eigenvalue set E in path s, its arbitrary coordinate minor, divided
by the last-k-coordinate minor, has valuation at least

$$
-\frac12\left(\sum I_0-\sum I\right),
\qquad I_0=\{n-k,\ldots,n-1\}.
\tag{1.2}
$$

For a k-element eigenvalue set F in path t, division by the
first-k-coordinate minor gives at least

$$
-\frac12\left(\sum J-\sum J_0\right),
\qquad J_0=\{0,\ldots,k-1\}.
\tag{1.3}
$$

Both denominators are nonzero by the monic Jacobi recurrence, with
endpoint normalization factors cancelled exactly. The relevant
coordinate block of M_N is, up to row and column roots of unity,

$$
N^{-1/2}\bigl(\zeta_N^{cij}\bigr)_{0\le i,j<n},
\qquad c=\overline4\pmod N.
\tag{1.4}
$$

Its extreme I_0,J_0 minor is an ordinary nonzero Vandermonde. The
valuation of every other minor divided by it is nonnegative:
the Schur-polynomial quotient is integral, and consecutive row
indices minimize all the congruence-collision counts
C_d(I)=sum_(a mod d) binom(m_a(I),2). This minimization applies even
though the available indices form only an n-element interval inside
Z/NZ. A consecutive k-element interval already attains the absolute
minimum of every C_d among all k-element integer sets.

In the double Cauchy--Binet expansion the unique smallest power of
omega is at I_0,J_0 and equals -k(n-k). If g is the increase of
that exponent, (1.2), (1.3), and (1.4) show that every other term
divided by the extreme term has valuation at least g/2>0.
The sum cannot vanish. This proves the block theorem, including
5 dividing N and n=1. The factor N^(-k/2) cancels in minor ratios,
and no assertion that it is a valuation unit is used.

In particular every overlap between any one eigenvector of one path
and any one eigenvector of another path is nonzero. The theorem does
not state total nonsingularity after mixing eigenvectors from
different paths in one row or column subset.

## 2. The exact first mixed obstruction when 49 divides N

Assume now 7 divides n. Choose one real eigenvector phi_s of L_s and
one phi_t of L_t, s!=t, normalized to have first coordinate 1.
Write their eigenvalues as mu_s, mu_t. Put

$$
x_s=y_s+n-1,\qquad
z_s=\zeta_7^{cs},\qquad c=\overline4\pmod7,
$$

$$
\alpha_s=\frac{\mu_s-d_{s,n-1}}{b_{s,n-2}},
\qquad
\beta_s=\frac{\mu_s-d_{s,0}}{b_{s,0}},
\tag{2.1}
$$

and similarly for t. The path length is now at least 7, so all
denominators displayed in (2.1) exist and are positive. They are
the backward and forward endpoint ratios
phi_s(n-2)/phi_s(n-1) and phi_s(1), respectively.

The endpoint Fourier block has rank one:

$$
M_N(x_s,y_t)M_N(x_0,y_0)
   =M_N(x_s,y_0)M_N(x_0,y_t).
\tag{2.2}
$$

Indeed the only nonseparable block-index phase is
zeta_N^(c n^2 st), and N=7n divides n^2. Thus the extreme
two-by-two Fourier determinant is exactly zero.

For bookkeeping, replace omega only in the explicit gauge by an
indeterminate w. Keep the Jacobi eigenvectors and the cat matrix
fixed. This is an auxiliary Laurent-polynomial identity, not a
replacement of the original parameter. Divide row s of the overlap
matrix by phi_s(n-1), and divide rows and columns by the nonzero
separable factors in (2.2). After removing w^(-(n-1)) from each
entry, the normalized kernel is

$$
G_{st}(w)
 =1+w\left(
       \eta_A\alpha_s z_s^3z_t^{-1}
       +\eta_B\beta_t z_s z_t^{-3}
      \right)+O(w^2),
\tag{2.3}
$$

where the exact modular phases are

$$
\eta_A=e_N\!\left(\overline8(6n-7)\right),\qquad
\eta_B=e_N\!\left(\overline8(2n-7)\right).
\tag{2.4}
$$

To verify these phases, decreasing the row coordinate by 1
multiplies the kernel by
e_N(overline8*(6x_s-2y_t-3)); increasing the column coordinate by
1 multiplies it by e_N(overline8*(2x_s-6y_t-3)).
Substituting y_s=h+sn and x_s=y_s+n-1 gives (2.3)--(2.4).
The two changes just listed are the only contributions at order w.

Consequently the first candidate coefficient of the normalized
principal two-by-two minor is

$$
\det G_{\{s,t\},\{s,t\}}(w)
       =wF_{st}+O(w^2),
$$

$$
\boxed{
F_{st}=(z_s-z_t)
\left[
\eta_B\left(\beta_s z_s^{-3}-\beta_t z_t^{-3}\right)
-\frac{\eta_A}{z_s z_t}
 \left(\alpha_s z_s^3-\alpha_t z_t^3\right)
\right].}
\tag{2.5}
$$

The derivation uses
det(ones(2)+wE)=w(E_ss+E_tt-E_st-E_ts)+O(w^2).
Thus (2.5) is a sum of four endpoint contributions. A statement
that the next coefficient is merely a single nonzero Vandermonde
would omit these other terms and their possible cancellations.

## 3. The exact unproved step in this route

We have not proved that (2.5) is nonzero for every pair of actual
Jacobi eigenvalues, nor the valuation estimate needed to make its
term dominate at the actual w=omega.

The distinction is material. If 5 does not divide N, after the
normalizations above all further coefficients of G are integral:
the endpoint recurrences divide only by valuation units. Therefore
v(F_st)<1 would suffice for the wF_st term to dominate all terms
of degree at least 2 when v(w)=1. Mere F_st!=0 does not supply
this estimate. If 5 divides N, endpoint divisions can additionally
cost up to one half per step; the bound on a degree-g contribution
at w=omega is only g/2 before cancellations. No required
coefficient lower or upper valuation has been hidden in a
genericity assumption.

Higher mixed minors and repeated eigenvalues across paths create
further internal block questions. The proved all-minor theorem for
7 not dividing N and the block theorem of Section 1 alone do not
resolve them. In particular they do not establish nonidentity of
the full discriminant for every remaining N.

## 4. A short trace corollary in the already solved dimensions

For completeness, the audited large-real-time argument also gives
one exact statement directly about quantum traces. For odd N>=3
with 7 not dividing N and nonzero algebraic complex z, the set

$$
\boxed{\{1,\operatorname{Tr}U_N(z),
             \operatorname{Tr}U_N(z)^2,
             \operatorname{Tr}U_N(z)^3,\ldots\}}
\tag{4.1}
$$

is linearly independent over the algebraic numbers.

Indeed the largest eigenvalue a_1 of A_N is at least
<delta_0,A_N delta_0>=9/10. Let b_1!=0 be the first principal
minor of M_N in decreasing A_N eigenvalue order. The proved
asymptotics at z=-it/N give

$$
\operatorname{Tr}(e^{tA_N}M_N)^m
      =b_1^m e^{mta_1}(1+o(1)),
\qquad m\ge1.
\tag{4.2}
$$

In any finite algebraic linear combination with highest positive
index M and nonzero coefficient at that index, the term in (4.2)
with m=M dominates the others, including a constant term.
That combination is a nonzero algebraic exponential polynomial.
Lindemann--Weierstrass, with distinct frequencies collected, makes
its value nonzero at every nonzero algebraic z. A combination
containing only a nonzero constant is already nonzero. This proves
(4.1). In particular every positive-time trace is nonzero and
transcendental.

Statement (4.1) is qualitative. It supplies no lower bound on
these traces or on their algebraic linear combinations and no
control of the signed sums in H_diag.

## 5. Frozen inputs

| File | SHA-256 |
|---|---|
| arithmetic_padic_jacobi_simplicity.md | f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df |
| arithmetic_transcendental_eigenvalue_ratios.md | 334b97d4659d2f29ed22c7615252cdb88e7d2d4c99e1a896083cea993475e0a5 |

The valuation, Jacobi recurrence, Fourier-minor minimization, and
Lindemann--Weierstrass hypotheses used here are all proved or
checked in those inputs. The first-confluent-term identity
(2.5) is proved above from the original exact kernel. No numerical
sample is used to establish any theorem in this note.
