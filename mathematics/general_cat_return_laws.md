# Return laws and a sharp regularity boundary for every hyperbolic toral automorphism

**Status.** Project derivation. The arithmetic, quantization, estimate
transfer, regularity counterexample and Gevrey extension have limited
independent internal review; the proof below records the changes needed
from the previously checked special matrix.
External priority, external refereeing, and Lean formalization are open.
The statements concern arithmetic subsequences and global laws at
vanishing classical perturbation. They do not establish microscopic BGS.

The analytic gas estimates used below are proved in
[the phase-space note](phase_space_return_gas.md). The normalized
Hilbert--Schmidt normal form is proved in
[the periodic-point note](periodic_point_trace_comparison.md).
This note removes the restriction to the particular matrix in those notes.

## 1. The arithmetic subsequence and the statements

Fix any $A\in SL(2,\mathbb Z)$ with $|t|>2$, where $t=\operatorname{Tr}A$.
Write
$$
 \Delta=t^2-4,\qquad
 \lambda=\frac{|t|+\sqrt\Delta}{2}>1,\qquad
 b_0=0,\quad b_1=1,\quad b_{n+1}=tb_n-b_{n-1}.
$$
Define the fixed positive integer $q_A$ and allowed integers $m$ by
$$
 \begin{array}{c|c|c}
 &q_A& m\\ \hline
 t\ {\rm even}&1&\text{positive odd integers}\\
 t\ {\rm odd}&2^{v_2(t^2-1)}&3\ell,\quad\ell\text{ positive odd}
 \end{array}
 \qquad K=2m,\qquad N=b_m/q_A.                            \tag{U1}
$$
Retain only $N\ge3$. These are odd positive integers and
$N\asymp_A\lambda^{K/2}$, including when $t<0$.

Use the Weyl convention and the unitary $U_{0,N}$ constructed in Section 2,
with $U_{0,N}^K=I$. For real $f$ let
$$
 U_{\epsilon,f}=e^{i\epsilon\operatorname{Op}_N(f)}U_{0,N},
 \qquad
 X_K(f)=\frac1{\sqrt K}\sum_{j=0}^{K-1}
              U_{0,N}^j\operatorname{Op}_N(f)U_{0,N}^{-j}.
$$
Let $T=A^{\mathsf T}$. For an absolutely summable mean-zero Fourier
series put
$$
 \sigma_A^2(f)=\sum_{\mathcal O}
                   \left|\sum_{v\in\mathcal O}\widehat f_v\right|^2,
 \qquad
 \mathcal L_\beta(f)=\sum_{v\ne0}
               |\widehat f_v|[\log(2+\|v\|_1)]^\beta,       \tag{U2}
$$
where $\mathcal O$ ranges over oriented nonzero $A$-orbits.
The variance equals the absolutely convergent Green--Kubo sum for
real $f$.

**Theorem 1 (Gevrey return law).** Suppose $f$ is fixed, real, mean zero,
and for some $\rho>0$ and $0<\alpha\le1$ satisfies
$$
             F_{\rho,\alpha}(f)=\sum_v|\widehat f_v|
                          e^{\rho\|v\|_1^\alpha}<\infty .
$$
If $\sigma_A^2(f)>0$, there are positive constants
$s_0,C,c$, depending on $A,f,\rho,\alpha$, such that for all the dimensions (U1),
all positive integers $r$, and $s=r|\epsilon|\le s_0$,
$$
 |\tau_N U_{\epsilon,f}^{rK}|
             \le e^{-\sigma_A^2(f)Ks^2/4}+Ce^{-cK},        \tag{U3}
$$
$$
 |\tau_N U_{\epsilon,f}^{rK}
                   -e^{-\sigma_A^2(f)Ks^2/2}|
             \le C K^{-1/2}+Ce^{-cK}.                    \tag{U4}
$$
Here $\tau_N=N^{-1}\operatorname{Tr}$.
If $\sigma_A^2(f)=0$, instead
$$
             \|U_{\epsilon,f}^{rK}-I\|_{\rm op}
                           \le C_{A,f}Ks^2/(rN).         \tag{U5}
$$
For even $f$, (U3)–(U5) also hold on the odd block with its own
normalized trace. Constants are not uniform as $A$ or $f$ varies.

Consequently, for $\epsilon_K\to0$ and positive variance the global
return eigenphase law is Haar exactly when $K\epsilon_K^2\to\infty$;
when $K\epsilon_K^2\to v<\infty$ it is wrapped Gaussian with variance
$v\sigma_A^2(f)$. With $\hbar_N=(2\pi N)^{-1}$, the classical action
parameter is $\kappa=\hbar_N\epsilon=\epsilon/(2\pi N)$.

**Theorem 2 (averaged-observable CLT).** For fixed real mean-zero
$f_1,\ldots,f_J$ with $\mathcal L_{1/2}(f_j)<\infty$ and fixed
$u_1,\ldots,u_J\in\mathbb R$,
$$
 \tau_N\prod_{j=1}^J e^{iu_jX_K(f_j)}
       \longrightarrow
       e^{-\frac12\sigma_A^2(\sum_j u_j f_j)}.             \tag{U6}
$$
In particular the empirical spectral law of $X_K(f)$ tends weakly
to $N(0,\sigma_A^2(f))$. The same statements hold on the odd block
when all symbols are even.

**Theorem 3 (sharpness, including quantum centering).** For every
such $A$ there is one fixed real even continuous mean-zero $f$ with
$\mathcal L_\beta(f)<\infty$ for every $\beta<1/2$, such that the
empirical spectral laws of
$$
             X_K(f)-\tau_N X_K(f)\,I                     \tag{U7}
$$
are not tight along (U1). The conclusion also holds after restriction
to the odd block and subtraction of its own quantum mean.
The exponent $1/2$ is therefore sharp as a sufficient guarantee
for these weighted Fourier classes. It is not asserted to be a
necessary condition for each individual observable.

## 2. Arithmetic and quantization for general A

The Cayley--Hamilton identities give
$$
 A^m=b_mA-b_{m-1}I,\qquad
 A^{2m}-I=b_mA^m(2A-tI),\qquad
 |\det(A^{2m}-I)|=\Delta b_m^2.                           \tag{U8}
$$
For negative $t$, $b_m$ has sign $(-1)^{m-1}$ times the corresponding
positive-trace sequence, so every allowed $b_m$ is positive.
If $t$ is even, parity of the recurrence gives $b_m$ odd for odd $m$,
and $2A-tI$ is an even matrix.
If $t$ is odd, $b_3=t^2-1$ and
$$
 b_{3\ell}=b_3 u_\ell,\qquad
 u_0=0,\quad u_1=1,\quad
 u_{\ell+1}=(\operatorname{Tr}A^3)u_\ell-u_{\ell-1}.
$$
Since $\operatorname{Tr}A^3=t^3-3t$ is even, $u_\ell$ is odd
for odd $\ell$. This proves precisely the power of two removed
in (U1). In particular $q_A\ge8$ for odd $t$.
It follows in both cases that
$$
       A^K=I\bmod2N,\qquad
       |\det(A^K-I)|=D_A N^2,\quad D_A=\Delta q_A^2.       \tag{U9}
$$

The usual odd-$N$ finite Weyl operators $W_N(v)$ use the inverse
of two modulo $N$ and depend only on $v\bmod N$.
Introduce the quadratic refinement
$$
 q_*(v)=v_1v_2+v_1+v_2\bmod2,\qquad
 \mathcal W_N^*(v)=(-1)^{q_*(v)}W_N(v).                   \tag{U10}
$$
The function $q_*$ equals one on every nonzero vector of
$\mathbb F_2^2$; thus $q_*(Av)=q_*(v)$ for every integer unimodular
$A$. Its polarization is the symplectic form modulo two. Consequently
$$
 \mathcal W_N^*(v)\mathcal W_N^*(w)
       =e^{\pi i\omega(v,w)/N}\mathcal W_N^*(v+w),\qquad
 \mathcal W_N^*(2Nv)=I.                                  \tag{U11}
$$
In contrast, $\mathcal W_N^*(Nv)=(-1)^{q_*(v)}I$.
In particular the central character at $(N,0)$ is $-I$.

The assignment $W_N(v)\mapsto W_N(Av)$ extends to a star automorphism
of the full matrix algebra: Weyl multiplication is symplectically
invariant, and the $N^2$ residue operators form an orthogonal basis.
Every star automorphism of a finite full matrix algebra is implemented
by a unitary. One elementary verification is to map a complete family
of rank-one matrix units, choose unit vectors in the image diagonal
projections, and fix their phases using the image off-diagonal units.
This constructs $U_{0,N}$ with exact Egorov for $W_N$, and invariance
of $q_*$ gives exact Egorov for $\mathcal W_N^*$.
Equation (U9) implies that $U_{0,N}^K$ commutes with the entire
matrix algebra, so a scalar phase makes it the identity.

Parity $R|x\rangle=|-x\rangle$ commutes with $U_{0,N}$:
its conjugate implements the same Weyl automorphism $v\mapsto-v$,
so differs from $R$ by a scalar; $\operatorname{Tr}R=1$ fixes that
scalar. Quantization of even symbols also commutes with parity.
These statements require odd $N$, not primality of $N$.

The refinement $v_1v_2$ used for the earlier special matrix is also
invariant when $A=I\bmod2$. The present choice supplies a common
convention for all $A$; its different central sign is retained below.

## 3. Uniform lattice and gas estimates

For cyclic vector sequences define
$$
 (\mathcal D_Ap)_j=p_j-Ap_{j+1},\qquad
 \mathcal C_K=\{c\in\mathbb Z^{2K}:\sum_jA^jc_j=0\bmod N\}.
$$
The map to $(\mathbb Z/N\mathbb Z)^2$ is onto through $c_0$.
Together with (U9), the determinant of $\mathcal D_A$ therefore gives
$$
 [\mathcal C_K:\mathcal D_A\mathbb Z^{2K}]=D_A,\qquad
       \mathcal D_A^{-1}c\in D_A^{-1}\mathbb Z^{2K}.       \tag{U12}
$$
For the second assertion, telescope to
$(I-A^K)p_0=N z$. By (U8), $I-A^K$ has all entries divisible
by $b_m=q_A N$. Its inverse formula shows that $p_0$ has
denominator dividing $\Delta q_A$, hence dividing $D_A$.
The recurrence and integrality of $A^{-1}$ propagate this denominator.

Let $P_s,P_u$ be the real spectral projections of $A$.
For periodically extended forcing, its unique bounded preimage is
$$
 p_j=\sum_{\ell\ge0}A^\ell P_s c_{j+\ell}
                      -\sum_{\ell\ge1}A^{-\ell}P_u c_{j-\ell}.
$$
Both geometric series converge absolutely, even with negative
eigenvalues. Summation over one period yields
$$
                         \|p\|_1\le C_A\|c\|_1.          \tag{U13}
$$
No constant in this estimate grows with $K$.

The integral quadratic form $Q_A(v)=\omega(v,Av)$ does not vanish
on a nonzero rational vector. A rational eigenline would give a
rational algebraic-integer eigenvalue; its reciprocal is also an
algebraic integer, forcing an eigenvalue $1$ or $-1$, contrary to
hyperbolicity. Thus $|Q_A(p)|\ge D_A^{-2}$ on the nonzero lattice
in (U12). Eigen-coordinate decomposition and the arithmetic-geometric
mean inequality now give, for a homogeneous gap of length $d$,
$$
       \|p_{\rm left}\|_1+\|p_{\rm right}\|_1
                              \ge c_A\lambda^{(d-1)/2}.
$$
As in (R5), every endpoint is counted at most twice. By (U13),
$$
          \|c\|_1\ge \gamma_A
                       \sum_{\rm gaps}\lambda^{(d-1)/2},
                        \qquad\gamma_A>0.                \tag{U14}
$$
This applies to internal gaps of finite nonzero integer runs and
to all gaps of winding configurations. Noninteger preimages have
no zero coordinate and hence belong to the latter class.

For $\alpha>0$ put
$h_{\alpha,A}(d)=\exp[-\alpha\gamma_A\lambda^{(d-1)/2}/2]$.
Its generating series is entire. Splitting the exponential Fourier
weight in half, the component enumeration from (R6) gives
$$
 \sum_{c\in\mathcal C_K}\eta^{q(c)}e^{-\alpha\|c\|_1}
                   \le e^{C_{\alpha,A}K\eta^2}+(3/4)^K   \tag{U15}
$$
for a sufficiently small fixed $\eta\ge0$.
The winding count is still
$K2^{-K}\sum_{a\ge1}(\eta b_\alpha H_{\alpha,A}(2))^a/a$.
It counts forcing vectors with unique preimages and already includes
all $D_A$ classes. There is no unaccounted multiplicity depending on $K$.

All exact reordering identities (R8)–(R9) use only (U11),
symplecticity, and period reduction (U9). Their signs are unchanged.
The centered interaction kernel satisfies
$$
 \frac{2\pi}{N}\sum_{d=1}^{K-1}
                \max|A^{\operatorname{center}(d)}|
                                  \le C_A,               \tag{U16}
$$
since $\max|A^j|\le C_A\lambda^{|j|}$ and
$N\asymp_A\lambda^{K/2}$. No antipodal phase is discarded.

Analytic cohomology is unchanged: choose minimal representatives
in the adapted eigen-coordinate norm, paired for negative orbits,
to write $f=b+g-g\circ T$ with analytic $b,g$ and
$\int b^2=\sigma_A^2(f)$. The Fourier support of $b$ meets each
oriented orbit at most once. The quantum conjugacy error over $rK$
steps is $C_{A,f}Ks^2/(rN)$, proving (U5) when $b=0$.

For $b\ne0$, (U16) and the original onsite estimate (R12) give
the conditional clean-gas bound (R15), with constants depending
on $A,b$. Use the positive analytic Fourier-atom majorant (R16)
and replace (R6) by (U15). Its finite-component generating function
has no degree-two coefficient: two atoms at distinct forcing sites
would contradict the orbit-representative property. It is therefore
$O_{A,b}(s^3)$ on a fixed disk. These are exactly the inputs to
(R18)–(R19); all integer and winding classes have been retained.

Finally the physical scalarization error remains
$C_{A,b}Ks^2e^{KsF_0(b)}/(rN)$, by (U11).
Choose $s_0$ small enough that $s_0F_0(b)<\frac14\log\lambda$.
This error, the conjugacy error, and the odd-trace correction
are exponentially small in $K$. Equations (U3)–(U4) follow.
This proof uses no unproved classical CLT.
It proves the analytic case $\alpha=1$ of Theorem 1.
Section 6 supplies the changes for every $0<\alpha<1$.

## 4. The weighted normal form and low-regularity limit

Here are the inputs for carrying the polynomial argument of (P31)–(P32)
to general $A$. For frequencies of norm at most $M$, equality between
two ordered pair sums modulo $N$ gives at most four forcing atoms
of total norm at most $4M$. If $K>C_A M$, (U12)–(U13) force
the preimage to be integer and to have a zero coordinate.
Every nonzero run has length at most $C_A M$.

The resulting local grouping argument of (P20) therefore bounds
the number of representations of each nonzero output key by
$$
               C_A M^2 |S|^2,                           \tag{U17}
$$
where $S$ is the frequency support. The zero output key contributes
no commutator: the symplectic area of opposite residues vanishes
modulo $N$. Centered kernel summation gives the other inputs,
$$
 \sum_d a_d(v,w)\le C_A\|v\|_1\|w\|_1,\qquad
 \sum_d |c_d|a_d(v,w)\le
                    C_A\|v\|_1\|w\|_1/K,
$$
where $a_d=|e^{2\pi i\omega(v,A^dw)/N}-1|$ and
$c_d=(K-1-2d)/(2K)$ with $0\le d<K$.
The second estimate uses cancellation of $c_d$ near the antipodal
time and exponential decay of $a_d$ away from it.

For Fourier shells of radius $M$, $|S|=O(M^2)$. The
Cauchy--Schwarz argument with (U17) and the subsequent dyadic
sum are consequently the same as in (P24a): with
$F_a(f)=\sum_v(1+\|v\|_1)^a|\widehat f_v|$,
$$
 \|[G_f,\overline H_h]\|_{2,N}
       \le C_A K^{-1/2}(F_0(f)F_4(h)+F_4(f)F_0(h)).
$$
The operator commutator estimates and unitary Duhamel therefore give
(P31)–(P32) with constants depending on $A$.
Together with (U4), or (U5) at zero variance, they prove (U6)
for fixed Fourier polynomials.

For an early return $A^dv=v\bmod N$, $0<d<K$, apply (U14) to
the two forces $-v,v$. Their preimage cannot have a zero:
an integer finite component would give $A^e v=v$ for a nonzero
$|e|<K$. Thus both cyclic gaps are included, and
$$
        \|v\|_1\ge c_A\lambda^{K/4},\qquad
        K\le C_A\log(2+\|v\|_1).                         \tag{U18}
$$
Weyl orthogonality gives $\|X_K(e_v)\|_{2,N}=1$ when all orbit
residues are distinct, and the elementary bound $\sqrt K$ suffices
otherwise. Hence
$$
 \|X_K(e_v)\|_{2,N}\le C_A\sqrt{\log(2+\|v\|_1)},\qquad
 \sup_K\|X_K(f)\|_{2,N}\le C_A\mathcal L_{1/2}(f).         \tag{U19}
$$
Finite Fourier cutoffs now approximate the unitary characteristic
traces uniformly in $K$. First taking $K\to\infty$ at fixed cutoffs,
then removing the cutoffs, proves (U6). The orbit variance is
continuous in the absolute Fourier norm. On the odd block the
normalized Hilbert--Schmidt norm costs only the bounded factor
$\sqrt{2N/(N-1)}$. This proves Theorem 2.

## 5. A centered counterexample for every A

The needed fixed odd prime always exists. The integer
$$
                 B=b_5=t^4-3t^2+1
$$
is odd and greater than five. If $5\mid B$, then $t^2=4+5a$
for some integer $a$, giving $B=5+25a+25a^2$; thus $v_5(B)=1$.
Consequently $B$ has a prime divisor $p\ne5$, and $p$ is odd.
Since $B=5\bmod\Delta$, this prime does not divide $\Delta$.

Modulo $p$, (U8) gives $A^5=\alpha I$ with $\alpha^2=1$.
Therefore the order $h$ of $A$ modulo $p$ divides ten.
It cannot divide two: over a field of odd characteristic,
$A^2=I$ and $\det A=1$ would force $A=I$ or $-I$, and then
$p\mid\Delta$. Thus $h=5$ or $10$.
Moreover
$$
                         p^2\mid b_{5p}.                 \tag{U20}
$$
Indeed $b_{5p}=b_5u_p$ for the recurrence with trace
$\operatorname{Tr}A^5$. Modulo $p$, this trace is $2\alpha$
and its solution is $u_\ell=\ell\alpha^{\ell-1}$.
In particular $u_p=0\bmod p$.

Let $c=5p$ for even $t$, and $c=15p$ for odd $t$. Set
$$
 \begin{gathered}
 L_j=c(4\cdot2^{\,2^j}+2),\quad
 M_j=b_{L_j/2}/q_A,\quad d_j=M_j/p,\quad a_j=j/\sqrt{L_j},
 \\ f(z)=2\sum_{j\ge1}a_j\cos(2\pi d_jz_1).
 \end{gathered}                                          \tag{U21}
$$
All $L_j$ belong to (U1). The divisibility $b_u\mid b_{u\ell}$,
which follows from the same recurrence identity, and (U20)
show that $p^2\mid M_j$; division by the power of two $q_A$
does not remove this factor.
The series defines one fixed real even continuous function.
Since $\log d_j\asymp_A L_j$ and the $L_j$ grow doubly
exponentially, $\mathcal L_\beta(f)<\infty$ for all $\beta<1/2$.
Different positive multiples of $(1,0)$ belong to different
$A$-orbits, so its classical variance is $2\sum_j a_j^2>0$.

At $M=M_j=p^2t_j$, put $d=M/p$ and use the ordinary clock and
shift operators
$$
             C|x\rangle=e^{2\pi ix/p}|x\rangle,\qquad
             S|x\rangle=|x+d\rangle .
$$
They commute, both have order $p$, and all $p^2$ joint characters
have equal multiplicity $M/p^2$, by Weyl trace orthogonality.
The integer $t_j$ is odd. For every integer vector $v$,
$$
                  \mathcal W_M^*(dv)=(-1)^{q_*(v)}C^{v_1}S^{v_2}.
$$
Every $A^\ell(1,0)$ is primitive, hence nonzero modulo two,
so its sign here is minus one. Define the Hermitian contraction
$$
 H_j=\frac1h\sum_{\ell=0}^{h-1}
       \operatorname{Re}\left(C^{(A^\ell(1,0))_1}
                             S^{(A^\ell(1,0))_2}\right).
                                                               \tag{U22}
$$
Its full trace is zero because all these frequencies are nonzero
modulo $p$, and $H_j=1$ on the joint $C=S=1$ subspace.
Since $h\mid L_j$, the contribution of the $j$th mode to
$X_{L_j}(f)$ is exactly $-2jH_j$.

By (U18), every earlier frequency has the full $L_j$ modular period
for all sufficiently large $j$. Their contribution $Y_j$ has
zero trace and uniformly bounded normalized Hilbert--Schmidt norm.
The later modes contribute $E_j$ with $\|E_j\|_{\rm op}\to0$:
the ratio $a_{j+1}/a_j$ is eventually at most one half, and
$\sqrt{L_j}a_{j+1}=(j+1)\sqrt{L_j/L_{j+1}}\to0$.
Thus the centered operator is $-2jH_j+D_j$ with
$\sup_j\|D_j\|_{2,M_j}<\infty$.

Intersect the $H_j=1$ subspace with the spectral subspace
$|D_j|\le j$. The intersection has dimension at least
$M_j/p^2-M_j\|D_j\|_{2,M_j}^2/j^2$.
Its quadratic form is at most $-j$, so min-max gives
$$
 \frac1{M_j}\#\{\text{eigenvalues of the centered }
                  X_{L_j}(f)\text{ at most }-j\}
                    \ge\frac1{p^2}-\frac{C_{A,f}}{j^2}.  \tag{U23}
$$
The resulting sequence is not tight.

For the odd block, a basis of the joint vacuum is
$p^{-1/2}\sum_{\ell=0}^{p-1}|pa+\ell d\rangle$,
$a\in\mathbb Z/t_j\mathbb Z$. Parity sends $a$ to $-a$,
giving odd dimension $(t_j-1)/2$ and asymptotic relative
dimension $1/p^2$. The odd trace of $H_j$ is $O(M_j^{-1})$.
Subtracting this mean costs $O(j/M_j)=o(1)$; the remaining
centered perturbation still has bounded odd Hilbert--Schmidt norm.
The same min-max argument, with threshold $-j/2$, proves the
odd version. This completes Theorem 3.

## 6. Removing spatial analyticity: every finite Gevrey order

The linear charge penalty in (R15) is unnecessarily costly for
nonanalytic symbols. The interaction is a unit-modulus phase, and
its difference from one is bounded by two. Retaining this saturation
permits the stated stretched-exponential Fourier weights.

Write $l(\boldsymbol v)=\sum_\nu\|v_\nu\|_1$ and
$L(\boldsymbol v)=1+\log(1+l(\boldsymbol v))$ for a nonvacuum
clean particle. By (U16), its Mayer interaction with another particle
satisfies, away from same-site exclusion,
$$
 |e^{i\theta_d(\boldsymbol v,\boldsymbol w)}-1|
 \le\min\{2,C_A\lambda^{-|d-m|}l(\boldsymbol v)l(\boldsymbol w)\}.
$$
Split the geometric sum where its argument crosses two to get
$$
 \sum_d|e^{i\theta_d(\boldsymbol v,\boldsymbol w)}-1|
                  \le C_A L(\boldsymbol v)L(\boldsymbol w). \tag{U24}
$$
Indeed the left side is bounded by
$C_A[1+\log(1+l(\boldsymbol v)l(\boldsymbol w))]$, and this
is at most a constant times the displayed product.
The same-site exclusion adds at most one and obeys the same bound.

For any fixed $\beta>0$ the absolute clean activity has moment
$$
 M_\beta=\sum_{\boldsymbol v\ne0}
               |w(\boldsymbol v)|L(\boldsymbol v)
                        e^{\beta L(\boldsymbol v)}
                              \le C_{b,\beta}s^2.         \tag{U25}
$$
Only a fixed polynomial Fourier moment is required here.
To verify this, bound the weight by
$C_\beta(1+l)^{\beta+1}$ and use
$1+\sum_\nu\|v_\nu\|\le\prod_\nu(1+\|v_\nu\|)$.
Each nonvacuum clean profile has at least two nonzero replica entries.
The weighted sum of one such entry is $O_b(|\epsilon|)$;
the binomial factors are absorbed by $r|\epsilon|=s$.
Vacuum normalization contributes at most $e^{C_b r\epsilon^2}$.
Gevrey symbols have all the polynomial moments used here.

Absolute activities are identical at all available clean sites:
the onsite factor and the external fields only change their phase.
It is therefore valid to sum the spatial kernel in (U24) before
summing the second particle's mark. For the rooted tree criterion
choose the size function
$a_s(\boldsymbol v)=D s^2 L(\boldsymbol v)$.
For a sufficiently large fixed $D$ and then small $s_0$,
$D s^2\le\beta$ and (U24)–(U25) give
$$
 \sum_{\text{sites, marks }\boldsymbol w}
       |w(\boldsymbol w)|\,|e^{i\theta}-1|\,
                               e^{a_s(\boldsymbol w)}
                         \le a_s(\boldsymbol v).
$$
The tree identity already proved in the phase-space argument applies.
Its connected logarithm after the one-particle term is bounded by
$$
 K\sum_{\boldsymbol v}|w(\boldsymbol v)|
                     (e^{D s^2L(\boldsymbol v)}-1)
                      \le C_{A,b}Ks^4.                  \tag{U26}
$$
The $s^2$ in the chosen tree size is essential to this fourth-order
remainder; using only a fixed size $\beta L$ would be insufficient.

The dirty-site estimate improves as well. For a real smooth $b$,
$\|b(\cdot+h)-b\|_2\le C_b\min(1,\|h\|)$.
The field from a dirty site $i$ at a clean site $j$ is bounded by
$C_A\lambda^{-|\delta_{ij}-m|}l_i$, where
$\delta_{ij}=(j-i\bmod K)\in\{0,\ldots,K-1\}$.
The inequality $\min(1,\sum_i x_i)\le\sum_i\min(1,x_i)$ and the
same capped geometric summation yield
$$
 \sum_{\text{clean }j}\max_\nu\min(1,\|h_{\nu j}\|)
                           \le C_A\sum_{\text{dirty }i}L_i .
$$
The variance lower bound used in (R13) now gives the conditional
partition estimate
$$
 |\mathcal Q_{B,\boldsymbol h}|
 \le\exp\left[-\tfrac12\sigma_A^2(b)Ks^2
       +C_{A,b}K(s^3+s^2/N)
       +C_{A,b}s^2\sum_{i\in B}L_i\right].               \tag{U27}
$$
The deleted-site cost is included because $L_i\ge1$.
This logarithmic profile penalty replaces the linear-mass penalty
in (R15), uniformly in the replica count.

It can be absorbed into the positive atom majorant
$$
 B_s(z)=\sum_{v\ne0}|\widehat b_v|(1+\|v\|_1)^{D s^2}e_v(z),
 \qquad a_c(s)=e^{D s^2}[e^{sB_s}]_c,\quad c\ne0,         \tag{U28}
$$
after increasing $D$ if necessary.
The log of one plus the total profile mass is at most the sum
of the logs of one plus the original atom norms, including atoms
that cancel within a replica. The remaining constant per dirty site
is the factor outside the exponential.

For $0<\alpha\le1$, the weight $e^{\rho\|v\|^\alpha}$ is
submultiplicative on frequency sums. Polynomial weights in (U28)
can be absorbed by decreasing $\rho$. Thus $a_c(s)$ is normally
analytic on a fixed complex disk, has nonnegative Taylor
coefficients, and obeys
$$
                a_c(s)\le C_{A,b}s e^{-\rho'\|c\|_1^\alpha}
                        \quad(0\le s\le s_*).            \tag{U29}
$$

The corresponding full lattice bound is also available.
Subadditivity of the power $\alpha$ applied to the Green series
in Section 3 gives
$$
 \sum_j\|p_j\|_1^\alpha
                   \le C_{A,\alpha}\sum_j\|c_j\|_1^\alpha.
$$
Raising the homogeneous endpoint inequality to this power and
counting endpoints at most twice yields
$$
 \sum_j\|c_j\|_1^\alpha
       \ge\gamma_{A,\alpha}
                 \sum_{\rm gaps}\lambda^{\alpha(d-1)/2}. \tag{U30}
$$
Split each stretched-exponential forcing weight in half. The vector
sum $\sum_{v\ne0}e^{-\rho'\|v\|^\alpha/2}$ is finite, and the gap
series with weights
$\exp[-\rho'\gamma_{A,\alpha}\lambda^{\alpha(d-1)/2}/2]$
is entire. The finite-component and winding enumeration therefore
gives (U15) with $\sum\|c_j\|^\alpha$ in the exponent.
All arithmetic classes remain included.

Finally the minimal-orbit transfer construction preserves a positive
stretched-exponential Fourier weight with the same $\alpha$:
the logarithmic number of intervening orbit sites is absorbed by a
decrease of $\rho$. Thus $b,g$ have the assumed regularity.
Combine (U27)–(U30), the unchanged vanishing of the degree-two
component coefficient, and the clean estimate (U26).
This recovers (R18)–(R19), with exponential error in $K$, and
proves (U3)–(U5) for every $0<\alpha\le1$.

The conclusion covers every fixed finite Gevrey order $1/\alpha$.
It does not automatically cover all smooth symbols: smoothness alone
does not imply any stretched-exponential Fourier bound.
No constant is asserted to remain bounded as $\alpha\downarrow0$.

For example, the same nonanalytic function
$$
 f(z)=2\sum_{n\ge1}e^{-\sqrt n}\cos(2\pi nz_1),\qquad
                 \sigma_A^2(f)=2\sum_{n\ge1}e^{-2\sqrt n} \tag{U31}
$$
works for every hyperbolic $A$. Its Fourier coefficients satisfy the
assumption with $\alpha=1/2$ and any $0<\rho<1$, but with no
analytic exponential weight. Distinct multiples of $(1,0)$
belong to different $A$-orbits, which gives the displayed variance.

## 7. Verification and the remaining boundary

Run the companion verifier from the repository root with NumPy available:

    OPENBLAS_NUM_THREADS=1 python computations/verification/general_cat_return_laws.py \
      --output build/general-cat-return-laws-precheck.json

The [verification program](../computations/verification/general_cat_return_laws.py)
passed on 2026-09-12. It enumerates 72 hyperbolic unimodular matrices
with entries between minus four and four. Their reductions cover all
six matrices in $SL(2,\mathbb F_2)$. The 200 retained dimension cases
include positive and negative, odd and even traces; 16 occurrences
of $N=1$ are explicitly excluded.
There are 800 exact cyclic-preimage checks and 3,200 exact Weyl-phase
checks. Prime-square lifting is checked at all 28 integer traces
$3\le|t|\le16$, and eight large-modulus cases check the centered
counterexample's own and earlier periods.

Another 72 rational-arithmetic checks sum an infinite dyadic envelope
of the capped interaction kernel exactly, including particle masses
as large as $2^{200}$. They test the logarithmic bound; the tree
criterion, Gevrey quasi-norm bound, and limiting theorems are proved
analytically above.

Independent physical intertwiners are constructed at $N=3,15,35,323$.
Unitarity, exact-Egorov targets, parity and the normalized return
period are tested separately from integer arithmetic.
The largest double-precision matrix residual is below
$1.4\cdot10^{-10}$. These are numerical diagnostics, not
interval-certified matrix identities.

Limited independent internal review checked the arithmetic
subsequence, universal refinement, composite-modulus construction,
negative traces, the transfer of the normal-form estimates, and
the centered prime-square counterexample. A separate pass checked
the capped interaction and conditional-field estimates used in
Section 6. The review required explicit exclusion of $N=1$,
retention of the negative central sign, and the
$a_s=D s^2L$ tree size for the fourth-order connected remainder.
The final proofs include these points.

Generality over $A$ means every fixed hyperbolic element of
$SL(2,\mathbb Z)$ on the specified subsequence; it does not mean
all dimensions or all nonlinear chaotic systems.
Generality over Gevrey order means every fixed $0<\alpha\le1$,
with constants that may deteriorate as $\alpha$ tends to zero.
The proof does not extend by taking that endpoint.
Theorem 2 has a lower regularity requirement because it concerns
averaged observables rather than the actual kicked propagator.

For the BGS programme the remaining target is still local,
desymmetrized spectral correlation at Heisenberg times for a fixed
nonzero classical perturbation. Here $K$ is logarithmic in $N$,
the replica amplitude obeys $r|\epsilon|\le s_0$, and the classical
action parameter is $\kappa=\epsilon/(2\pi N)$. The estimates above do not
supply that missing comparison. External priority has not been established.
These proofs are included in the canonical manuscript through a generated
TeX chapter; the analytic limit theorems are not Lean-formalized.
