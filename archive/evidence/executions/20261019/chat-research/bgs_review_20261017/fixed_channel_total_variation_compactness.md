# Fixed-channel total-variation compactness from the full growing-channel input

17 October 2026. Working proof, subjected to the author checks recorded in
the review and the exact finite Jacobian controls. This is a new
continuation of the attachment's full-rank/absolute-continuity argument
(lines 528--624), not an assertion of a Haar limit. No repository change,
independent referee certification, or priority claim is made.

## 1. Exact statement

For each N, let mu_(N,v), 1<=v<=N, be permutation-invariant laws of unitary
matrices obtained by fresh independent uniform-phase Schur reduction.
In particular they satisfy exact Markov consistency

    mu_(N,v) K_(v->m)=mu_(N,m), v>=m,                    (1)

where K closes all but m specified ports using independent uniform phases.
Uniformly ordered retained labels give the same laws by permutation symmetry.
No invariance under the full unitary group is assumed.

Assume the FULL growing-channel input G: for EVERY u_N->infinity with
u_N/N->0, the entire fixed sampled principal block of sqrt(u_N) S_(N,u_N)
has the iid CN(0,1) limit in all fixed mixed moments. This is the G used in
the attachment; it includes reversed pairs. It is supplied in this program
by the 17 October dimension-uniform working proof, conditional on that
proof's named project local inputs.

**Theorem.** For every fixed m, the sequence (mu_(N,m))_(N->infinity) is
relatively compact in total variation. All its subsequential limits are
absolutely continuous relative to Haar measure H_m. More strongly,

    lim_(delta->0) limsup_(N->infinity)
       sup_(H_m(B)<=delta) mu_(N,m)(B)=0.               (2)

Every weakly convergent subsequence therefore also converges in total
variation to its weak limit. This does NOT identify the limit as Haar.

For two ports the transmission laws are TV relatively compact and obey
the analogous uniform asymptotic absolute continuity relative to Lebesgue
measure on [0,1]. In this class, if the conjectured weak uniform limit is
eventually proved, convergence in TV follows automatically.

## 2. A quantitative-rank good set at a fixed intermediate dimension

Fix the m retained indices A and let W in U(v), E=A^c. Set

    L_e(W)=vec(W_Ae W_eA) in C^(m^2),
    Gamma_v(W)=v sum_(e in E) L_e(W)L_e(W)*,
    C_(v,m)={W: Gamma_v(W)>=I_(m^2)/2}.                (3)

The set C_(v,m) is compact. For any sequence v=u_N in G's regime,
with v eventually at least m+m^2,

    E ||Gamma_v-I_(m^2)||F^2 ->0.                      (4)

Here is the moment verification. An entry is
v sum_e W_ie W_ej conjugate(W_ke W_el). Its expectation tends to
delta_ik delta_jl by the fourth Gaussian moment of a fixed principal block.
In its second moment, e=f contributes O(v^3 v^-4)=O(1/v); for e!=f the
fixed block on A union {e,f} gives the factorized eighth moment. Thus
E|Gamma_ij,kl|^2 tends to the squared modulus of the displayed mean.
There are only m^4 entries. The required repeated-index moment bounds
come from G and Holder, not from an independence assumption at finite v.

Consequently

    lim_(v->infinity) limsup_(N->infinity)
       mu_(N,v)(C_(v,m)^c)=0.                          (5)

Indeed, otherwise choose v_j->infinity and N_j>=j v_j tending to infinity,
with bad-set probability bounded below. Extend u_(N_j)=v_j to a sequence
in G's regime by u_N=floor(sqrt N) off that subsequence. Equation (4) and
Markov contradict that lower bound. This uses G for arbitrary diverging u;
a restriction u>=log(N)^c would not justify choosing arbitrarily large
N_j at fixed v_j.

In fact the theorem and its proof only need exact consistency and the
following rank assumption R, for every fixed m:

    lim_(v->infinity) limsup_(N->infinity)
       mu_(N,v){Gamma_v not >= I/2}=0.

Permutation symmetry and G are a sufficient way to verify R, as proved
above. If R is supplied directly, the compact-kernel argument below does
not require Gaussian moments. The threshold 1/2 can be replaced by any
fixed positive rank lower bound for which this double-limit condition holds.

## 3. TV continuity of the phase kernel on the good set

**Lemma.** At every W_0 for which Gamma_v(W_0) is nonsingular, the map

    W |-> K_(v->m)(W,.)

is continuous in total variation at W_0 (even along W not in the good set).
Its value at W_0 has a Haar density.

Proof. Define the rational holomorphic map

    F_W(z)=W_AA+W_AE(I-ZW_EE)^(-1)Z W_EA.

The common denominator has constant coefficient 1 and never vanishes in
the open polydisk. Its torus zero set has Haar measure zero. Differentiating
at zero gives partial_(z_e)F_W(0)=W_Ae W_eA. Nonsingular Gamma selects a
fixed set J of m^2 internal variables with nonzero complex Jacobian minor
at z=0. After clearing denominators this minor is a nonzero polynomial.
It remains nonzero at almost every point of the entire phase torus.

On the torus F_W is unitary almost everywhere. The m^2 chosen angular
derivatives are complex-linearly independent, hence real-linearly
independent in the real m^2-dimensional tangent space of U(m). Thus F_W0
is a real submersion at almost every input point. Local change of variables,
integrating the remaining input coordinates, gives a Haar density.

The same local argument gives TV CONTINUITY, not just absolute continuity:
exclude the null pole/critical set for W_0. On its complement the map is
jointly smooth in W and all angular coordinates. Around every regular point,
choose a product input box, an output coordinate chart, and a set of m^2
input variables for which the output map is a diffeomorphism with the other
variables and W as parameters. The parameter-dependent inverse function
theorem gives a common smaller box with nonvanishing Jacobian for W near W_0.

For any epsilon>0, finitely many such boxes and smooth nonnegative cutoffs
on them capture phase mass at least 1-epsilon, with cutoff sum <=1. These
cutoffs depend on input angles only and stay fixed as W varies. In each box,
the pushforward density is the integral, over the remaining coordinates,
of the cutoff evaluated at the local inverse divided by the absolute real
Jacobian. The inverse and Jacobian vary continuously in W, the Jacobian is
bounded below on the compact cutoff support, and the support stays inside
fixed charts. Extending by zero outside the local image is harmless because
the cutoff has compact support in the smaller input box. Dominated
convergence proves L1 convergence of these densities as W->W_0.

The omitted input mass is <=epsilon for every W, independently of the map.
The total variation difference between full output measures is therefore
at most 2epsilon plus the finite sum of the local L1 differences. Let W->W_0
and then epsilon->0. This proves the lemma. All full input measures are
normalized Haar phase measures; no conditional mass on a critical set is
discarded without accounting for its size.

## 4. Compact kernel images and mixtures

By the lemma and compactness of C_(v,m),

    M_(v,m)={K_(v->m)(W,.):W in C_(v,m)}

is a compact subset of L1(H_m), viewed as probability densities. Its closed
convex hull is also compact in L1. To see this directly, quantize M_(v,m)
by a finite epsilon-net. Every mixture is within epsilon in TV of a mixture
of those finitely many net points, and the latter mixtures form a compact
finite-dimensional simplex. Thus the convex hull is totally bounded; its
closure is compact since L1 is complete.

For any desired epsilon>0, choose v so large that (5) is <epsilon/2, and
then N_0 so that mu_(N,v)(C^c)<epsilon for all N>=N_0. Split (1) according
to C and C^c. The conditional good-part output lies in the compact convex
hull just described, and the full output mu_(N,m) is at TV distance at most
epsilon from it. This proves asymptotic total boundedness, hence TV relative
compactness. Finitely many initial N do not affect that conclusion.

A compact L1 family is uniformly integrable relative to H_m: this follows
again from a finite net and absolute continuity of the finitely many
integrals. Thus for a Haar-small Borel set B, the good-part output is
uniformly small, while the bad-part mass is at most epsilon. This proves
(2) after epsilon->0 and shows every cluster measure is Haar absolutely
continuous. It does not require transferring absolute continuity through
weak convergence.

Finally, if a subsequence converges weakly to nu but fails to converge to
nu in TV, choose a subsubsequence at TV distance at least c>0. TV relative
compactness gives a further TV-convergent subsequence; its TV limit is also
its weak limit, hence must be nu, a contradiction.

## 5. Two-channel consequences and limits

Pushforward by U|->|U_12|^2 contracts TV. For Haar U(2), that pushforward
is uniform on [0,1]. A Lebesgue-small set pulls back to a Haar-small set,
so (2) gives the asserted transmission regularity. In particular limiting
transmission laws have densities and no endpoint or interior atoms.

The result supplies no L2 density bound growing as o(v^2), no entropy bound
o(log v), no evaluation of fractional eigenvector overlaps, and no uniqueness
of the coherent family. Compactness constants in section 4 depend on the
chosen intermediate v; they have not been bounded uniformly as v->infinity.
Consequently the attachment's L2/entropy contraction theorem cannot yet
be invoked to identify Haar. That remains a precise additional obligation.

## Audit boundary

The input (4) and polynomial nondegeneracy mechanism are reconstructed from
the attachment, with G explicitly retained. The TV parameter-continuity,
compact convex-mixture argument and fixed-channel TV compactness are the
new continuation here. Their proof uses finite-dimensional smooth charts
and elementary probability; it does not import an unverified universality
theorem. Further adversarial review should focus on local chart cutoffs,
real versus complex Jacobian rank, and the order of limits in (5).

## 6. Marked cavity laws and clock-weighted limits

The attachment's exact associativity identity says that any fixed k marked
cavity columns C_1,...,C_k, together with the m-port output Q, are a measurable
phase-kernel image of the (m+k)-port law. Hence, along a subsequence on which
all fixed levels converge weakly, they now converge in TV as joint laws.
The TV assertion follows from the theorem above and contraction of TV by
every measurable Markov kernel; no continuity of the unbounded column map
at degenerate boundary points has to be assumed.

The limiting (m+1)-port law is Haar absolutely continuous. Its internal
coordinate is consequently coupled almost surely: r=1-|V_ee|^2>0. For one
marked column, conditional integration of its own phase gives

    tau=||C||^2=r/|1-z V_ee|^2,
    E_z tau=1_{r>0}.

Thus E tau_limit=1. At finite N, E tau_N=P(r_N>0)<=1, and TV convergence
of the finite cavity laws gives P(r_N=0)->0, since r_limit=0 has probability
zero. The second moments of the complex columns therefore converge to 1.
For k columns, E sum_e ||C_e||^2->k. Joint weak convergence and convergence
of these nonnegative moments imply uniform integrability and W2 convergence
of the column tuples, including the compact output Q if desired.

By subsequence compactness this also proves the unconditional asymptotic
uniform integrability statement

    lim_(R->infinity) limsup_(N->infinity)
       E[tau_N 1_{tau_N>R}]=0

for any fixed number of retained and marked channels under the theorem's
assumptions. This is a first moment statement about tau, not a bound on its
second moment; that second moment can diverge even in a Haar benchmark.

For a Hermitian H define

    psi_H(c)=cc* Tr(H cc*)/||c||^2, psi_H(0)=0.

Its norm is <=||H||op ||c||^2. TV convergence plus the proved uniform
integrability gives, along the chosen subsequence,

    sup_(|h|<=1)
      ||E[h(Q_N) psi_H(C_N)]-E[h(Q) psi_H(C)]|| ->0.      (6)

Here h may be any bounded measurable function on U(m). To prove (6),
truncate at ||C||^2<=R, apply TV convergence to the bounded integrand,
and then remove the uniformly integrable tail. The same reasoning covers
the first-order clock-weighted Ward observables. This closes a passage to
the limit; it does not compute the limiting conditional Stein operator or
make it isotropic. The inverse-Wishart Haar example in the attachment is
consistent with a random, nonisotropic empirical operator whose conditional
mean given Q is isotropic.
