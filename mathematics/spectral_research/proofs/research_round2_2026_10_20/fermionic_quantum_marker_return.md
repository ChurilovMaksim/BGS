> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_quantum_marker_return.md`. Embedded SHA256: `31c247eba33f35cdee9123dfbbaf9f711f1a2d47ed257b83e6136bda8793046e`.
> [Thematic guide](../../topics/dephasing.md).

# Exact quantum marker returns and the surviving phase problem

Research continuation, 20 October 2026. The unitary in every
formula below is the original $U_N$, at its unchanged fixed
parameter. This note tries to pass from the completed signed
encounter calculation to a quantum first-return calculation.
It proves exact return-energy bounds and identifies the specific
comparison and feedback steps that are still unproved.

## 1. What is proved

For an explicit finite Fourier detector of area $O(N^{-1})$,
let $0\le E_N\le I$ be its effect operator. Its trace is of
order one and its limiting eigenvalue profile is the sine
compression on a finite interval. Put

$$
 a_N=(I-E_N)^{1/2},\quad b_N=E_N^{1/2},\quad
 D_N=a_NU_N,\quad
 F_{m,N}=b_NU_ND_N^{m-1}b_N\quad(m\ge1).
 \tag{1.1}
$$

These are exact finite matrices, not classical orbit amplitudes.
They satisfy

$$
 \boxed{\displaystyle
 \sum_{m\ge1}\|F_{m,N}\|_{\rm HS}^2=\operatorname{Tr}E_N,\qquad
 \sum_{m\ge1}m\|F_{m,N}\|_{\rm HS}^2
             =\dim\mathcal H_{{\rm seen},N}\le N.}
 \tag{1.2}
$$

The seen space is the smallest reducing subspace of $U_N$
containing the range of $b_N$. In particular, for every fixed
$s>0$,

$$
 \boxed{\displaystyle
 \frac1{N^2}\sum_{m\ge1}e^{-2sm/N}m^2
                  \|F_{m,N}\|_{\rm HS}^2\le\frac1{2es}.}
 \tag{1.3}
$$

All matrix-path cross terms inside each $F_{m,N}$ have already
been summed in these identities. They do not bound the separate
absolute values of path contributions.

The exact Schur return function is

$$
 \Theta_N(z)=-a_N+\sum_{m\ge1}z^mF_{m,N}.
 \tag{1.4}
$$

It is contractive for $|z|<1$, and its feedback determinant is

$$
 \boxed{\displaystyle
 \det(I-zU_N)
  =\det(I-zD_N)\,
       \frac{\det(I-\Theta_N(z))}{\det(I+a_N)}.}
 \tag{1.5}
$$

More strongly, with $c_N=b_N(I+a_N)^{-1}$,

$$
 \boxed{\displaystyle
 (I+\Theta_N(z))(I-\Theta_N(z))^{-1}
   =c_N(I+zU_N)(I-zU_N)^{-1}c_N.}
 \tag{1.6}
$$

Thus the feedback denominator is visibly the original spectral
resolvent. The return-energy estimate (1.3) does not remove it.

The finite Fourier detector is not asserted to be a quantization
of the nonlinear stable/unstable marker used in the encounter
proof. Section 7 states that comparison problem precisely.
Equal area and the same limiting sine operator alone do not
identify their dynamics.

## 2. A concrete finite-dimensional detector

Let $\mathcal F_N$ be the normalized discrete Fourier matrix.
Choose consecutive coordinate and frequency windows $I_N,J_N$
of respective cardinalities $r_N,s_N$, with

$$
 c_0\sqrt N\le r_N,s_N\le C_0\sqrt N,\qquad
 L_N=\frac{r_Ns_N}{N}.
 \tag{2.1}
$$

Their centers may be chosen at the nearest coordinate and
frequency grid points to the actual fixed point $z_*$.
Only a harmless unitary phase depends on these centers in the
following spectral computation. For all large $N$ the windows
can be represented by consecutive integer lifts. Define

$$
 E_N=P_{I_N}\mathcal F_N^*P_{J_N}
                   \mathcal F_NP_{I_N}.
 \tag{2.2}
$$

It is a positive contraction. Its trace is exactly

$$
 \operatorname{Tr}E_N=r_Ns_N/N=L_N.
 \tag{2.3}
$$

After removing the frequency-center diagonal phase, its
coordinate-window matrix has entries

$$
 (E_N)_{ij}
  =\frac{\sin(\pi s_N(i-j)/N)}
          {N\sin(\pi(i-j)/N)},\qquad i,j\in I_N,
 \tag{2.4}
$$

with diagonal value $s_N/N$. A half-integer center, when a
window cardinality is even, changes only the removed phase;
the displayed amplitude remains exact.

### 2.1. Uniform sine-compression approximation

Identify the coordinate basis of $I_N$, in order, with the
normalized indicator functions of the $r_N$ equal cells of
$[-1/2,1/2]$. Denote this isometry by $V_N$, and extend
$V_NE_NV_N^*$ by zero on the orthogonal complement of the
step functions. Its kernel on two cells is $r_N(E_N)_{ij}$.
At their midpoints $x_i,x_j$, equation (2.4) becomes

$$
 L_N\,\frac{\sin(\pi L_N(x_i-x_j))}
                {\pi L_N(x_i-x_j)}
    \frac{\pi(i-j)/N}{\sin(\pi(i-j)/N)}.
 \tag{2.5}
$$

The last factor is $1+O(N^{-1})$, uniformly, because
$|i-j|=O(\sqrt N)$. Moving within a cell changes the first
factor by $O(r_N^{-1})$, uniformly for $L_N$ in its fixed
compact positive interval. Consequently

$$
 \boxed{\displaystyle
 \|V_NE_NV_N^*-\widetilde{\mathsf S}_{L_N}\|_{\rm HS}
                            \le C N^{-1/2},}
 \tag{2.6}
$$

where the fixed-space integral kernel is

$$
 \widetilde{\mathsf S}_L(x,y)
       =L\,\frac{\sin(\pi L(x-y))}{\pi L(x-y)}
       \quad(-1/2\le x,y\le1/2).
 \tag{2.7}
$$

It is unitarily equivalent to the sine compression
$\mathsf S_L$ on an interval of length $L$. Its trace is
$L$, its operator norm is at most one, and its
Hilbert--Schmidt norm is bounded on compact $L$-intervals.
For example it is the compression of the orthogonal Fourier
projection to frequencies in $[-1/2,1/2]$, after rescaling.

For each fixed $j\ge2$, telescope the $j$-th powers and
use the trace inequality for two Hilbert--Schmidt factors.
Equation (2.6) gives

$$
 \operatorname{Tr}(E_N^j)
       -\operatorname{Tr}(\mathsf S_{L_N}^j)=O_j(N^{-1/2}).
 \tag{2.8}
$$

For $j=1$ the two traces are exactly $L_N$.
These statements require no convergence of $L_N$; all
bounds are uniform on its stated compact interval.

### 2.2. A nonvanishing projection defect at the critical scale

For every finite $L>0$, the norm of $\mathsf S_L$ is strictly
less than one. Indeed, an eigenvector with eigenvalue one would
be supported on a finite position interval and be band limited.
The Fourier transform of a compactly supported $L^2$ function
is entire, by its defining finite-interval integral and
Cauchy--Schwarz. Vanishing on an open frequency interval forces
it to vanish identically. Thus no such eigenvector exists.
The positive operator is compact, so norm one would give an
eigenvector with that eigenvalue. Its norm is therefore below
one. It is also nonzero, since its trace is $L>0$.

It follows that $\mathsf S_L-\mathsf S_L^2\ne0$.
Continuity of (2.7), in Hilbert--Schmidt norm, shows that

$$
 \min_{L\in[L_-,L_+]}
      \|\mathsf S_L-\mathsf S_L^2\|_{\rm HS}>0
       \quad(0<L_-<L_+<\infty).
 \tag{2.9}
$$

Equations (2.6) and the contraction bounds imply that the
same defect of $E_N$ has a fixed positive lower bound.
For every orthogonal projection $P$ on $\mathbb C^N$,

$$
 \|E_N-E_N^2\|_{\rm HS}
  \le\|E_N-P\|_{\rm HS}+\|E_N^2-P^2\|_{\rm HS}
  \le3\|E_N-P\|_{\rm HS}.
 \tag{2.10}
$$

Hence

$$
 \boxed{\displaystyle
 \inf_{P=P^*=P^2}\|E_N-P\|_{\rm HS}\ge c>0}
 \tag{2.11}
$$

for all sufficiently large $N$.
This is a leading-order obstruction to replacing this joint
position/frequency effect by a hard quantum hole at the same
critical scale. It is not an asymptotically vanishing boundary
correction.

## 3. Exact first-return energy identities

The following proof works for any positive contraction $E$
and any finite unitary $U$; it therefore applies directly
to (2.2) and the original $U_N$. Suppress their subscripts.
Put

$$
 a=(I-E)^{1/2},\quad b=E^{1/2},\quad
 A=-a,\quad B=bU,\quad C=b,\quad D=aU.
 \tag{3.1}
$$

The block matrix

$$
 \mathcal U=
 \begin{pmatrix} A&B\\ C&D\end{pmatrix}
 =\begin{pmatrix}-a&bU\\ b&aU\end{pmatrix}
 \tag{3.2}
$$

is unitary. Its diagonal norm identities use $a^2+b^2=I$;
the off-diagonal ones use $ab=ba$.
The return coefficients are $F_m=BD^{m-1}C$.

Set $e_j=\|D^jb\|_{\rm HS}^2$. Since
$B^*B=I-D^*D$, one has the exact scalar telescoping identity

$$
 \|F_m\|_{\rm HS}^2=e_{m-1}-e_m.
 \tag{3.3}
$$

It follows that

$$
 \sum_{m=1}^M\|F_m\|_{\rm HS}^2
                 =\operatorname{Tr}E-e_M.
 \tag{3.4}
$$

For the weighted sum, discrete summation by parts and
$E=I-DD^*$ give

$$
 \begin{split}
 \sum_{m=1}^M m\|F_m\|_{\rm HS}^2
     &=\sum_{j=0}^{M-1}e_j-Me_M\\
     &=N-\|D^M\|_{\rm HS}^2-M\|D^Mb\|_{\rm HS}^2
       \le N.
 \end{split}
 \tag{3.5}
$$

To justify the asserted infinite equalities, let
$\mathcal H_{\rm dark}$ be the largest reducing subspace of
$U$ contained in $\ker E$. On it $D=U$ is unitary
and $b=0$. Conversely, if $Dv=\zeta v$ with $|\zeta|=1$,
the contraction norm equality forces $EUv=0$, hence
$Uv=\zeta v$ and $Ev=0$. A unit-modulus eigenvector of
a contraction is reducing, since norm equality gives
$D^*v=\bar\zeta v$. Their span is its entire unitary part.
On its orthogonal complement $D$ has spectral radius strictly
below one. In finite dimension its powers decay there
exponentially up to a fixed polynomial Jordan factor.

The range of $b$ is orthogonal to the dark space. Thus
$D^Mb\to0$, $M\|D^Mb\|_{\rm HS}^2\to0$, and
$\|D^M\|_{\rm HS}^2\to\dim\mathcal H_{\rm dark}$.
Equations (3.4)--(3.5) give

$$
 \sum_{m\ge1}\|F_m\|_{\rm HS}^2=\operatorname{Tr}E,\qquad
 \sum_{m\ge1}m\|F_m\|_{\rm HS}^2=N-\dim\mathcal H_{\rm dark}.
 \tag{3.6}
$$

The orthogonal complement of the dark space is exactly the
reducing cyclic span of the range of $b$, proving (1.2).
No uniform decay rate in $N$ was used to take these exact
finite-dimensional infinite sums.

Finally
$$
 \sup_{m\ge1}m e^{-2sm/N}\le N/(2es).
$$
Multiplying (3.6) by this bound proves (1.3), including its
entire infinite tail.

## 4. The Schur function and its exact spectral feedback

For $|z|<1$ the return series is

$$
 \Theta(z)=A+zB(I-zD)^{-1}C.
 \tag{4.1}
$$

Its defect follows directly from (3.2). Apply that unitary to
the vector $(v,w)$, where
$w=z(I-zD)^{-1}Cv$. The internal output is $w/z$, so
the norm identity gives, also by continuity at $z=0$,

$$
 \boxed{\displaystyle
 I-\Theta(z)^*\Theta(z)
    =(1-|z|^2)C^*(I-\bar zD^*)^{-1}(I-zD)^{-1}C.}
 \tag{4.2}
$$

Thus the return function is contractive. This statement allows
the eigenvalue $-1$ on $\ker E$; it supplies no positive
distance from the eigenvalue $+1$ near the circle.

Let $K=I-A=I+a$, which is invertible even when $E$ is
singular. The feedback identity is

$$
 D+CK^{-1}B
   =aU+b(I+a)^{-1}bU=U,
 \tag{4.3}
$$

because $b(I+a)^{-1}b=I-a$.
Taking the determinant of the corresponding block Schur
complement, or using the finite-dimensional determinant lemma,
proves

$$
 \det(I-zU)=\det(I-zD)\frac{\det(I-\Theta(z))}{\det K}.
 \tag{4.4}
$$

Both resolvents are invertible for $|z|<1$; therefore
$I-\Theta(z)$ is invertible there as well.
Woodbury's identity, verified by multiplication if desired, gives

$$
 (I-\Theta(z))^{-1}
      =K^{-1}+zK^{-1}B(I-zU)^{-1}CK^{-1}.
 \tag{4.5}
$$

Since $c=bK^{-1}$,
$$
 2K^{-1}-I=c^2.
$$
Multiplying out $2(I-\Theta)^{-1}-I$ now proves the exact
Cayley formula (1.6). In particular,

$$
 \operatorname{Re}
  [(I+\Theta)(I-\Theta)^{-1}]
   =(1-|z|^2)c(I-\bar zU^*)^{-1}(I-zU)^{-1}c.
 \tag{4.6}
$$

The positive right side is the original spectral Poisson
operator, compressed by $c$. This displays the missing
spectral amplification directly.

The return-energy identities do control a derivative norm.
For example, if $r_N=e^{-s/N}$, Parseval and (3.6) give

$$
 \begin{split}
 \frac1{2\pi}\int_0^{2\pi}
            \|\Theta'(r_Ne^{it})\|_{\rm HS}^2\,dt
   &=\sum_{m\ge1}m^2r_N^{2m-2}\|F_m\|_{\rm HS}^2\\
   &\le C_sN^2.
 \end{split}
 \tag{4.7}
$$

But the exact logarithmic derivative relevant to traces is

$$
 \sum_{m\ge1}z^m\operatorname{Tr}(U^m)
  =z\operatorname{Tr}\bigl(D(I-zD)^{-1}\bigr)
    +z\operatorname{Tr}
                  \bigl((I-\Theta(z))^{-1}\Theta'(z)\bigr).
 \tag{4.8}
$$

Thus (4.7) alone is not the required trace estimate. The
feedback inverse and the internal open determinant both remain.
Their two contributions may also cancel, so separating their
absolute values is not justified as a route to the sharp limit.

## 5. The open spectrum retains the Heisenberg scale

For the concrete detector (2.2), $\|E_N\|<1$ already at each
sufficiently large finite $N$. If an eigenvector had
eigenvalue one, it would be supported in both the coordinate
window and the Fourier window. Its Fourier values are, after
a monomial phase, values of a polynomial of degree at most
$r_N-1$ on the $N$-th roots of unity. Vanishing outside
the frequency window gives $N-s_N\ge r_N$ distinct roots
for large $N$, forcing that polynomial to be zero.

Moreover (2.6), compactness of the $L_N$-interval, and the
strict continuum norm bound give a common $q<1$ with
$\|E_N\|\le q$ eventually. The logarithmic determinant series
then converges uniformly:

$$
 \log\det(I-E_N)
       =-\sum_{j\ge1}\frac{\operatorname{Tr}(E_N^j)}j.
 \tag{5.1}
$$

Its tail is bounded uniformly by a constant times $q^J$,
using $\operatorname{Tr}E_N=L_N=O(1)$.
The fixed-power convergence (2.8) therefore proves

$$
 \log\det(I-E_N)
     =\log\det(I-\mathsf S_{L_N})+o(1),
 \tag{5.2}
$$

uniformly. The Fredholm determinant on the right is positive,
continuous in $L$, and bounded away from zero on the compact
interval. These assertions follow from the same uniformly
convergent trace series and the norm bound; no gap-probability
interpretation is required.

Since $D_N=a_NU_N$,

$$
 |\det D_N|^2=\det(I-E_N).
 \tag{5.3}
$$

The largest modulus of an eigenvalue is at least their
geometric mean. Consequently, with
$c(L)=-\tfrac12\log\det(I-\mathsf S_L)>0$,

$$
 \boxed{\displaystyle
 r_{\rm sp}(D_N)\ge
        \exp[-c(L_N)/N+o(N^{-1})]
         =1-\frac{c(L_N)}N+o(N^{-1}).}
 \tag{5.4}
$$

In particular no $N$-independent open spectral gap is available.
For $r_N=e^{-s/N}$, take the phase of $z$ opposite to an
eigenvalue of maximal modulus in (5.4). The resolvent has
norm at least its spectral radius, giving

$$
 \sup_{|z|=r_N}\|(I-zD_N)^{-1}\|
                         \ge c_s N
 \tag{5.5}
$$

for a fixed positive $c_s$ and all large $N$.
This is an exact obstruction inside the circle, rather than
an issue caused by deforming a contour through unitary poles.

For a hard rank-$d$ hole, a stronger early-time norm obstruction
also follows by elementary dimension counting:
$\bigcap_{j=0}^m U^{-j}\ker P$ has dimension at least
$N-(m+1)d$, and the corresponding compressed $m$-step
evolution is isometric on that subspace. The soft effect
(2.2) was used precisely so that no hard-hole approximation
or norm-decay assumption enters (1.2).

## 6. The common cell phases survive between different collections

Here are exact inputs from the completed actual encounter proofs.

| Input | SHA-256 |
|---|---|
| fermionic_signed_three_cell_profile.md | edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5 |
| fermionic_six_connection_cancellation.md | 4661fed89558f03c58e085ec70df919b14056ff4ec5e3e765e6564ce35fbb865 |

For a cluster $\mathcal C$ of three labelled cells, let
$$
 Y_{\mathcal C,N}=\sum_{\rho\in S_3}C_{\rho,N}
$$
be the exact six-term Euler sum from the second input.
Its proof gives the uniform pointwise approximation

$$
 Y_{\mathcal C,N}
  =-a_{{\rm ref},\mathcal C,N}
       e^{-it_N\sum_jS_jU_{\rho_0(j)}}
              \det[e^{it_NS_iU_j}]
       +R_{\mathcal C,N},\qquad
 |R_{\mathcal C,N}|\le\eta_N|a_{{\rm ref},\mathcal C,N}|,
 \quad\eta_N\to0.
 \tag{6.1}
$$

The modulus of the reference weight obeys

$$
 \sum_{\mathcal C\text{ of length }m}
              |a_{{\rm ref},\mathcal C,N}|^2\asymp N^{-1},
 \qquad N\le m\le3N/2.
 \tag{6.2}
$$

This is why (6.1) could be squared within each cluster and then
summed with a controlled $o(N^{-1})$ error. It is not a bound
on the unpaired sum over different clusters.

Indeed the actual unstable multiplier of every period-$m$
orbit is at least $5^m$, and the exact scalar modulus error
is $O(mh^2)$. Hence
$$
 \max_{\mathcal C}|a_{{\rm ref},\mathcal C,N}|
                            \le C5^{-m/2}.
$$
Using (6.2) proves the concrete lower bound

$$
 \boxed{\displaystyle
 \sum_{\mathcal C\text{ of length }m}
          |a_{{\rm ref},\mathcal C,N}|
                      \ge c\,5^{m/2}/N.}
 \tag{6.3}
$$

Thus a uniform pointwise $o(1)$ error before pairing does
not supply a summable error after taking the entire unpaired
collection sum. The available absolute majorant has exponential
size. This statement does not say that the exact remainders
fail to cancel; it says that their required cancellation has
not been proved.

The large scalar phases left in
$a_{{\rm ref},\mathcal C,N}$ include
$\sum_{e\in\mathcal C}W_e(q_*,q_*)/h$.
These constants cancel between permutations of one collection,
but not between different collections. The sine-compression
calculation determines neither those relative phases nor the
sum of the remainders in (6.1).

For example, an attempted use of the six-term stationary
approximation in an unpaired coefficient calculation would
first need a genuine bound on

$$
 \sum_{N\le m\le3N/2}w(m/N)
       \left|\sum_{\mathcal C\text{ of length }m}
                              R_{\mathcal C,N}\right|^2,
 \tag{6.4}
$$

such as $o(1)$ for the proposed unit-scale coefficient
comparison, followed by a signed estimate for the leading
unpaired sums themselves. Neither estimate follows from
(6.1)--(6.3), and neither has been established here.
Expression (6.4) specifies the first unproved error sum of
this particular attempted transfer; it is not a hypothesis
used in any result above.

## 7. What the first-return route has and has not connected

The detector (2.2) is a concrete operator acting on the original
Hilbert space, and all return identities apply to the original
$U_N$. They give an unconditional $O(N^2)$ bound on the
weighted full return energy in (1.3), including its tail.
This is a completed quantum estimate for that detector.

The encounter marker, however, is a nonlinear local-product
rectangle with tangent axes
$(1,s_{\rm s})$ and $(1,s_{\rm u})$. Its limiting operator
was shown in arithmetic_endpoint_laws_and_sine_compression.md
to be a sine compression. Matching the area $L_N/N$ in (2.2)
does not prove that successive measurements with (2.2) reproduce
the exact classical forbidden-word weights for that rectangle.
No finite-$N$ intertwining or weighted error estimate for this
identification has been proved in this note.

Even after choosing and quantizing a suitable local canonical
coordinate change, the first unresolved dynamical transition
would be the comparison of the complete, phase-retaining
first-return kernels over $m\asymp N$ with the monitored
coefficients $F_{m,N}$. The fixed-cylinder positive renewal
theorem does not provide that comparison. At critical windows
the projection defect (2.11) is already nonvanishing, so a
replacement by sharp successive classical membership tests
needs a separate argument with its exact quantum effect retained.

Finally, an eventual control of that comparison would still
have to preserve the feedback expression (4.8). Equations
(1.6), (4.6), and (5.4)--(5.5) show explicitly where the original
unit-circle spectral information remains. No estimate for the
complete weighted trace statistic, or for $H_{\rm diag}$, is
deduced by discarding that denominator.

This attempt therefore yields exact detector return-energy
identities, a precise critical-scale nonprojection obstruction,
and an explicit open-spectrum bound at the Heisenberg scale.
The missing signed phase comparison between distinct interior
collections is exposed in (6.4), rather than supplied as a
hidden assumption.
