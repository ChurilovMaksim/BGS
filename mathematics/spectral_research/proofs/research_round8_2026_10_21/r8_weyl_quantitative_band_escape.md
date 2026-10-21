> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_quantitative_band_escape.md`. Embedded SHA256: `9982f37ec0faa8e6628dcb8d80b18fdb1005f2c2af119727526634a5c941f54a`.
> [Thematic guide](../../topics/approximation.md).

# Quantitative escape from sublinear bands for the original kick

21 October 2026. Round 8, Weyl branch. This is a separate addendum;
the earlier independently audited qualitative source remains unchanged.

## 1. The strengthened theorem

Use the notation of `r8_weyl_sublinear_polynomial_obstruction.md`:

$$
E_N=e^{i\tau NA_N},\qquad \tau=10^{-80},\qquad
m_{N,d}=\frac1N\sum_{\operatorname{dist}_N(x,y)\le d}|(E_N)_{xy}|^2.
$$

**Theorem 1.** There is a finite constant $C_\tau$, independent
of the odd dimension and of $d$, such that for every sufficiently
large odd $N$ and every nonnegative integer $d$,

$$
\boxed{m_{N,d}\le C_\tau
       \left[\left(\frac dN\right)^{1/2}+N^{-2/11}\right].}
\tag{1.1}
$$

Consequently, for $\mathcal B_{N,d}$, the space of matrices of
cyclic bandwidth at most $d$,

$$
1-C_\tau\left[(d/N)^{1/2}+N^{-2/11}\right]
\le\inf_{B\in\mathcal B_{N,d}}\|E_N-B\|_{\mathrm{op}}\le1.
\tag{1.2}
$$

The same lower and upper bounds hold for the best normalized
Hilbert--Schmidt approximation error, and for either error when
$B$ is restricted to polynomials $p(A_N)$ of degree at most
$d$. They also hold after right multiplication by $M_N$.

The constant is allowed to depend on the fixed exact $\tau$.
No useful numerical threshold at this tiny time is claimed. The
exponent $2/11$ comes from a deliberately elementary Fourier
estimate and is not claimed optimal. The theorem remains an
approximation obstruction for the original kick, not a statement
about $H_{\mathrm{diag}}$.

## 2. Exact classical factorization at the vanishing hopping amplitude

The ordinary-half symbol, verified from the modular quantization in
the companion proof, is

$$
a(q,p)=V(q)+\frac{R(q)}{100}\cos(2\pi p-\alpha_0),
\quad
R(q)=r(q+1/2)=4\cos^2(7\pi q)\sin^2(\pi q).
\tag{2.1}
$$

Let $\Phi_s=(Q_s,P_s)$ be the lifted flow of
$X=(a_p,-a_q)/(2\pi)$, and put
$\delta(q,p)=Q_\tau(q,p)-q$. In particular,

$$
\dot Q_s=-\frac{R(Q_s)}{100}\sin(2\pi P_s-\alpha_0).
\tag{2.2}
$$

We will prove the exact factorization

$$
\delta(q,p)=\tau R(q)H_\tau(q,p),
\tag{2.3}
$$

where the real smooth periodic function $H_\tau$ satisfies

$$
\left|H_\tau(q,p)+\frac{\sin(2\pi p-\alpha_0)}{100}\right|
\le\tau,
\tag{2.4}
$$

$$
\left|\partial_pH_\tau(q,p)
          +\frac{2\pi\cos(2\pi p-\alpha_0)}{100}\right|
\le100\tau.
\tag{2.5}
$$

These statements include positions where $R(q)=0$; division
by a vanishing amplitude will not be assumed.

The finite Fourier bounds in the companion proof give

$$
\|X\|_\infty\le18,\quad \|DX\|_\infty<1100,
\quad \|R'\|_\infty<101,\quad \|R''\|_\infty<4600.
\tag{2.6}
$$

For the last two bounds one may differentiate
$r=(1-\cos14\pi q)(1+\cos2\pi q)$, obtaining
$\|r'\|\le32\pi$, $\|r''\|\le456\pi^2$.
For $0\le s\le\tau$, the flow and variational equations imply

$$
\|\Phi_s-\operatorname{id}\|_\infty\le18s,
\quad\|D\Phi_s\|_\infty\le2,
\quad\|D\Phi_s-I\|_\infty\le2200s.
\tag{2.7}
$$

Define the smooth positive function

$$
B_s(q,p)=\exp\!\left[-\frac1{100}
 \int_0^s R'(Q_u(q,p))\sin(2\pi P_u(q,p)-\alpha_0)\,du\right].
\tag{2.8}
$$

If $R(q)>0$, uniqueness of the smooth flow and the invariant
lines $Q=q_*$, $R(q_*)=0$, imply that the trajectory cannot
reach a zero of $R$ in finite time. Differentiating its logarithm
along the trajectory gives
$R(Q_s)/R(q)=B_s$. Integrating (2.2) then yields

$$
H_\tau(q,p)= -\frac1{100\tau}\int_0^\tau
        B_s(q,p)\sin(2\pi P_s(q,p)-\alpha_0)\,ds.
\tag{2.9}
$$

This formula defines a smooth periodic function at every position,
including $R(q)=0$. The two sides of (2.3) are continuous, so
the identity extends from the dense set $R(q)>0$ to the entire
torus. One could also extend the identity
$R(Q_s)=R(q)B_s$ first.

To prove the uniform estimates, (2.6)--(2.8) give

$$
|\log B_s|\le2s,\quad |B_s|\le2,
\quad |B_s-1|\le4s.
\tag{2.10}
$$

In (2.9), replacing $B_s\sin(2\pi P_s-\alpha_0)$ by
$\sin(2\pi p-\alpha_0)$ costs at most
$(4+7\cdot18)s=130s$. Its integral divided by $100\tau$
is at most $0.65\tau$, proving (2.4).

For the derivative, differentiating the exponent in (2.8) gives

$$
|\partial_p\log B_s|
\le\int_0^s(101200u+14.14)\,du\le15s.
$$

Here $|\partial_pQ_u|\le2200u$,
$|\partial_pP_u|\le2$, and $2\pi<7$ were used. The last
inequality holds at the stated exact $s\le10^{-80}$.
Consequently $|\partial_pB_s|\le30s$. In differentiating
the integrand of (2.9), its difference from
$2\pi\cos(2\pi p-\alpha_0)$ is bounded by

$$
\begin{split}
&30s+(4s)\cdot7\cdot2
        +7\cdot2200s+7^2\cdot18s\\
&\hspace{20mm}=16368s<20000s.
\end{split}
$$

Integration and division by $100\tau$ prove (2.5).

## 3. A quantitative sublevel estimate for the displacement

For fixed $q$, on the complement of the two arcs where
$|\sin(2\pi p-\alpha_0)|\le1/2$, (2.4) implies
$|H_\tau|>1/250$. On each of those two arcs,
$|\cos(2\pi p-\alpha_0)|\ge\sqrt3/2>4/5$.
By (2.5), the derivative of $H_\tau$ has a fixed sign and
absolute value at least $1/25$.

It follows that, for every $a>0$,

$$
\operatorname{Leb}\{p:|H_\tau(q,p)|\le a\}
\le\min(1,250a),
\tag{3.1}
$$

uniformly in $q$. Indeed for $a<1/250$, the sublevel set
lies in the two indicated monotonicity arcs, each contributing
length at most $2a/(1/25)=50a$. For larger $a$, the
trivial bound by one suffices.

The eight zeros of $R$ are

$$
Z=\{0\}\cup\{(2j+1)/14:0\le j\le6\}\pmod1.
$$

Let $d_0=\operatorname{dist}_{\mathbb T}(q,0)$ and
$d_1=\operatorname{dist}_{\mathbb T}(q,Z\setminus\{0\})$.
Then

$$
|\sin\pi q|\ge2d_0,
\quad |\cos7\pi q|\ge14d_1,
\quad d_0+d_1\ge1/14.
$$

The first two inequalities follow from
$\sin u\ge2u/\pi$ for $0\le u\le\pi/2$, and the last
from the distance between zero and the other seven zeros. Hence

$$
R(q)\ge3136d_0^2d_1^2
\ge4\operatorname{dist}_{\mathbb T}(q,Z)^2.
\tag{3.2}
$$

Let $\mu$ be the classical transition measure, the pushforward
of $dq\,dp$ by $(q,p)\mapsto(q,Q_\tau(q,p))$, as in the
companion proof. Since $|\delta|\le18\tau<1/2$, its mass
within angular position distance $\epsilon<1/2$ of the
diagonal is exactly $\operatorname{Leb}\{|\delta|\le\epsilon\}$.
For almost every $q$, combine (2.3), (3.1), and (3.2):

$$
\operatorname{Leb}_p\{|\delta(q,p)|\le\epsilon\}
\le\min\!\left(1,
       \frac{(250/4)\epsilon}
            {\tau\operatorname{dist}_{\mathbb T}(q,Z)^2}\right).
$$

On a Voronoi cell about one of the eight zeros, integration is at
most twice the integral over the nonnegative half-line. For $A>0$,

$$
\int_0^\infty\min(1,A/u^2)\,du=2\sqrt A.
$$

Thus, for the closed diagonal tube $D_\epsilon$,

$$
\boxed{\mu(D_\epsilon)
\le\min\left(1,32\sqrt{(250/4)\epsilon/\tau}\right)
\le\min\left(1,300\sqrt{\epsilon/\tau}\right).}
\tag{3.3}
$$

This argument proves a rate for the zero-displacement set directly
from the concrete factor $R$. It does not merely use the
qualitative zero-set theorem for an analytic function.

## 4. A quantitative comparison for Fourier position tests

Keep the original odd quantization, expressed in the ordinary-half
basis $\widetilde W_N(k,l)=(-1)^{kl}W_N(k,l)$. The exact Weyl
law and symbol identity are those proved in the companion source.
Let

$$
D_{n,N}=\operatorname{diag}(e^{2\pi inx/N})_{x\bmod N},
$$

and define the two quantities

$$
c_{n,N}=\frac1N\operatorname{Tr}
              (D_{-n,N}E_ND_{n,N}E_N^*),
\quad
c_n=\int_{\mathbb T^2}e^{2\pi in(Q_\tau(q,p)-q)}\,dq\,dp.
\tag{4.1}
$$

Both have modulus at most one. We prove, uniformly for integers
$|n|\le N/4$,

$$
|c_{n,N}-c_n|
\le C_\tau\left[N^{-2}(1+|n|)^5
                     +N^{-6}(1+|n|)^6\right].
\tag{4.2}
$$

The exact commutator proof from the companion source gives, for
any smooth $F$,

$$
\|iN[A_N,\operatorname{Op}_N(F)]
       -\operatorname{Op}_N(X\cdot\nabla F)\|_{\mathrm{op}}
\le\frac C{N^2}\sum_{v\in\mathbb Z^2}(1+|v|)^3|\widehat F(v)|.
\tag{4.3}
$$

It follows by subtracting $-2\pi\omega$ from the exact
multiplier $-2N\sin(\pi\omega/N)$, and using the finite
support of $a$. No restriction on the size of the Fourier
indices is imposed in (4.3).

Cauchy--Schwarz and Parseval give

$$
\sum_v(1+|v|)^3|\widehat F(v)|
\le C\|F\|_{H^5(\mathbb T^2)},
\tag{4.4}
$$

since the sum of $(1+|v|^2)^{-2}$ converges in dimension two.
For $F_{n,s}=e^{2\pi inQ_s}$, repeated ordinary differentiation
up to order five, and bounded derivatives of the smooth flow on
the fixed compact time interval, imply

$$
\sup_{0\le s\le\tau}\|F_{n,s}\|_{H^5}
\le C_\tau(1+|n|)^5.
\tag{4.5}
$$

The constants in these flow derivative bounds are independent of
$n,N$; their finiteness follows by successively differentiating
the fixed smooth ODE and using the integral equation on the compact
time interval. Duhamel's formula applied to (4.3)--(4.5) now gives

$$
\|E_ND_{n,N}E_N^*
             -\operatorname{Op}_N(F_{n,\tau})\|_{\mathrm{op}}
\le C_\tau N^{-2}(1+|n|)^5.
\tag{4.6}
$$

It remains to check the trace aliases quantitatively. In the pairing
of $D_{-n,N}$ with $\operatorname{Op}_N(F_{n,\tau})$, a
nonzero trace requires a Fourier label of the form
$(n+Na,Nb)$, $a,b\in\mathbb Z$. All accompanying Weyl
phases have modulus one. The term $(a,b)=(0,0)$ has phase
one and equals exactly $c_n$.

Applying $(1-\Delta)^3$ before taking Fourier coefficients,
and differentiating the same smooth exponential up to order six,
gives

$$
|\widehat F_{n,\tau}(k,l)|
\le C_\tau(1+|n|)^6(1+k^2+l^2)^{-3}.
$$

When $|n|\le N/4$ and $(a,b)\ne(0,0)$, the length of
$(n+Na,Nb)$ is at least $(3N/4)\sqrt{a^2+b^2}$. Summing
the resulting convergent lattice series proves that all nonzero
aliases contribute at most $C_\tau(1+|n|)^6N^{-6}$. This and
(4.6) prove (4.2) with every odd wrap and composite modulus included.

## 5. Smooth diagonal tube and optimization

Fix a smooth function $0\le\chi\le1$ on $\mathbb R$, equal
to one on $[-1,1]$, supported in $[-2,2]$. For
$0<\eta\le1/8$, periodize it as

$$
\chi_\eta(u)=\sum_{\ell\in\mathbb Z}
                        \chi((u+\ell)/\eta).
$$

Its Fourier coefficient at $n$ is
$\eta\widehat\chi(\eta n)$. Rapid Fourier decay, obtained
by repeated integration by parts, gives for every fixed integer
$j\ge0$

$$
\sum_n\eta|\widehat\chi(\eta n)|(1+|n|)^j
\le C_j\eta^{-j}.
\tag{5.1}
$$

For $\eta N\ge1$, the same decay gives, for each fixed
integer $K\ge1$,

$$
\sum_{|n|>N/4}\eta|\widehat\chi(\eta n)|
\le C_K(\eta N)^{-K}.
\tag{5.2}
$$

For example these follow by using a Schwartz bound of order
larger than $j+2$, respectively $K+2$, and comparing the
positive tail sum with its integral.

Let $\mu_N=N^{-1}\sum_{x,y}|(E_N)_{xy}|^2
\delta_{(x/N,y/N)}$. Its tube test is, exactly,

$$
\int\chi_\eta(s-q)\,d\mu_N(q,s)
=\sum_n\eta\widehat\chi(\eta n)c_{n,N}.
\tag{5.3}
$$

The classical version has $c_n$ in place of $c_{n,N}$.
Apply (4.2) to $|n|\le N/4$, (5.1) to its two weighted
sums, and $|c_{n,N}-c_n|\le2$ together with (5.2) to the
remaining indices. This proves

$$
\left|\int\chi_\eta(s-q)\,d(\mu_N-\mu)(q,s)\right|
\le C_\tau\left[N^{-2}\eta^{-5}
                     +N^{-6}\eta^{-6}+(\eta N)^{-4}\right].
\tag{5.4}
$$

If $d/N\le\eta$, the cutoff dominates the indicator of
the discrete band, while its classical integral is at most
$\mu(D_{2\eta})$. Equations (3.3) and (5.4) therefore give

$$
m_{N,d}\le300\sqrt{2\eta/\tau}
 +C_\tau\left[N^{-2}\eta^{-5}
                +N^{-6}\eta^{-6}+(\eta N)^{-4}\right].
\tag{5.5}
$$

Choose

$$
\eta=\max(d/N,N^{-4/11}).
$$

When this is at most $1/8$, the three quantum errors in
(5.5) are bounded respectively by constants times
$N^{-2/11}$, $N^{-42/11}$, and $N^{-28/11}$.
Also
$\sqrt\eta\le\sqrt{d/N}+N^{-2/11}$.
This proves (1.1) in that case, absorbing the fixed factor
$\tau^{-1/2}$ into $C_\tau$.

For all sufficiently large $N$, if $\eta>1/8$, then
$d/N>1/8$; the elementary bound $m_{N,d}\le1$ proves
(1.1) after increasing the constant. Thus every nonnegative
integer $d$ is covered.

Finally, the companion proof gives the exact best banded
Hilbert--Schmidt error $\sqrt{1-m_{N,d}}$, the lower bound
of this quantity on the best operator-norm error, and the upper
bound one furnished by the zero matrix. Since
$\sqrt{1-m}\ge1-m$ for $0\le m\le1$, (1.2) follows.
Every degree-$d$ polynomial in the original nearest-neighbour
matrix $A_N$ has cyclic bandwidth at most $d$, so its
approximation error obeys the same lower bound. Unitary invariance
gives the assertion after right multiplication by $M_N$.
This completes the proof.

## 6. Exact limit of the conclusion

The theorem supplies a quantitative original-family obstruction to
replacing the full kick by a polynomial of degree $o(N)$.
It does not prevent cancellations in an observable without such
an operator approximation, and it gives no lower bound on the
original $\Delta_{k,N}(b)$. The signed Heisenberg-time
functional remains unresolved after this addendum.
