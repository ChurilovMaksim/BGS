> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md`. Embedded SHA256: `ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d`.
> [Thematic guide](../../topics/histories.md).

# Oscillatory matrix cancellation and the physical reverse-path operator

Round 5, 21 October 2026. Base checkpoint: the unified round-4 proof book,
SHA-256 `e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a`.
This is a new proof route. Its target is an actual coherent path class for the
original matrices, not the full H_diag assertion. This file proves the analytic
matrix lemma and applies it to the four-branch kernel constructed separately.
The precise kernel input is listed in Section 4; the application is conditional
on that input until its raw derivation and audit are attached.

## 1. A sampled oscillatory matrix lemma

Let phi be real analytic on a connected neighborhood of [0,1]^2, and let b be
smooth there. Let a,c belong to {0,1,2,3}. For positive integers N define the
N by N matrix

$$
T_N(x,y)=\frac1N 1_{x\equiv a\ (4)}1_{y\equiv c\ (4)}
 b(x/N,y/N)e^{2\pi iN\phi(x/N,y/N)},\quad 0\le x,y<N.
\tag{1}
$$

Define its rectangular cycle phase by

$$
\Omega(q,q',r,r')=\phi(q,r)-\phi(q',r)
                 +\phi(q',r')-\phi(q,r').
\tag{2}
$$

Assume

$$
\partial_q\partial_r\phi\not\equiv0,\qquad
\max_{j=1,\ldots,4}\|\partial_j\Omega\|_{L^\infty([0,1]^4)}<1/8.
\tag{3}
$$

Then, along all integers N,

$$
\boxed{\|T_N\|_{\mathrm{op}}\longrightarrow0.}
\tag{4}
$$

The assertion is also valid for any finite collection of phases/amplitudes and
residue classes satisfying the assumptions. Neither a rate nor a uniformity
claim over arbitrary analytic phases is made.

### 1.1 Removing the boundaries

Fix epsilon>0 and choose a smooth cutoff chi in C_c^infty((0,1)), with
0<=chi<=1 and chi=1 on [epsilon,1-epsilon]. Replace b(q,r) by
b_epsilon(q,r)=chi(q)chi(r)b(q,r), and call the resulting matrix T_N^epsilon.
All changed entries are in at most 4 epsilon N^2+O(N) positions. Thus

$$
\limsup_{N\to\infty}\|T_N-T_N^\epsilon\|_{\mathrm{op}}
\le\limsup_N\|T_N-T_N^\epsilon\|_{\mathrm{HS}}
\le2\|b\|_\infty\sqrt\epsilon.
\tag{5}
$$

It suffices to prove (4) for each fixed cutoff.

### 1.2 The fourth Schatten power

Direct multiplication gives

$$
\begin{split}
\|T_N^\epsilon\|_{S_4}^4
&=\operatorname{Tr}[(T_N^\epsilon(T_N^\epsilon)^*)^2]\\
&=\frac1{N^4}\sum_{\substack{x,x'\equiv a\ (4)\\y,y'\equiv c\ (4)}}
 B(x/N,x'/N,y/N,y'/N)e^{2\pi iN\Omega(x/N,x'/N,y/N,y'/N)},
\end{split}
\tag{6}
$$

where

$$
B(q,q',r,r')=b_\epsilon(q,r)\overline{b_\epsilon(q',r)}
 b_\epsilon(q',r')\overline{b_\epsilon(q,r')}.
$$

This smooth amplitude has compact support in (0,1)^4. The sum may therefore be
extended to the four full arithmetic progressions in Z without changing it.
The one-dimensional Poisson formula for a Schwartz function, applied in each
coordinate, yields

$$
\|T_N^\epsilon\|_{S_4}^4
=\frac1{4^4}\sum_{k\in\mathbb Z^4}e^{2\pi i k\cdot(a,a,c,c)/4}
\int_{\mathbb R^4}B(z)e^{2\pi iN[\Omega(z)-k\cdot z/4]} dz.
\tag{7}
$$

For completeness, the one-dimensional formula follows by periodizing the
Schwartz function with lattice spacing 4/N, computing its Fourier coefficients
by a change of variables, and evaluating its absolutely convergent smooth
Fourier series at a/N. This also verifies the factor 4^{-4} and the displayed
phase sign. No randomness is introduced by (7).

For k!=0 choose a coordinate j with |k_j|=|k|_infinity. On the support of B,

$$
|\partial_j(\Omega-k\cdot z/4)|
\ge |k_j|/4-1/8\ge |k_j|/8.
\tag{8}
$$

Integrate by parts six times in that coordinate, using
(2 pi i N partial_j(phase))^{-1} partial_j on the exponential. All derivatives
of B and Omega required here are bounded on a fixed compact neighborhood. By
induction on the number of integrations, the resulting integral is bounded by

$$
C_\epsilon N^{-6}(1+|k|_\infty)^{-6}.
\tag{9}
$$

Indeed each differentiated reciprocal of the first phase derivative contains
at least the same number of powers of |k_j| in its denominator as the number
of integration operations, since every higher derivative of the phase is
independent of k. The sum of the right side of (9) over Z^4 is finite: the shell
|k|_infinity=j contains at most C(j+1)^3 points. Therefore all nonzero aliases
in (7), taken together, tend to zero (in fact they are O_epsilon(N^{-6})).

### 1.3 The zero alias

The real analytic function Omega is nonconstant. In fact
partial_q partial_r Omega=partial_q partial_r phi(q,r), which is not identically
zero by (3). Consequently its critical set has Lebesgue measure zero.

Here is the analytic fact used in this last sentence. A nonzero real analytic
function on a connected open set has a zero set of measure zero. Locally,
expand in the last variable. Unless the function vanishes identically on a
box, at least one coefficient, an analytic function in one fewer variable, is
nonzero. By induction its zero set has measure zero. Outside that exceptional
set the one-variable slice is a nonzero analytic function and its zeros are
isolated. Fubini proves the assertion on that box. A countable box cover and
analytic continuation on the connected domain complete the proof. The
one-variable base follows from the first nonzero Taylor coefficient. Apply
this fact to one partial derivative of Omega which is not identically zero;
the critical set is contained in its zero set.

Choose a smooth cutoff eta_delta of |grad Omega|^2 which vanishes for
|grad Omega|^2<=delta and is one for |grad Omega|^2>=2delta. On its support,

$$
\int B\eta_\delta e^{2\pi iN\Omega}
=-\frac1{2\pi iN}\int
 \operatorname{div}\left(B\eta_\delta
              \frac{\nabla\Omega}{|\nabla\Omega|^2}\right)e^{2\pi iN\Omega}.
\tag{10}
$$

The absolute value is O_delta(N^{-1}). The removed part has absolute value at
most the integral of |B| over {|grad Omega|^2<2delta}, which tends to zero as
delta decreases to zero by dominated convergence and the zero-measure result.
Take N to infinity first, then delta to zero. Thus the k=0 integral tends to
zero. Equations (6)--(9) give ||T_N^epsilon||_{S4}->0, hence its operator norm
tends to zero. Finally (5), followed by epsilon->0, proves (4).

## 2. The fixed original symbol and the four elementary phases

Throughout the remaining sections

$$
t=\frac{10^{-80}}{2\pi},\qquad
R(q)=(1+\cos14\pi q)(1-\cos2\pi q),
$$

$$
a(q,p)=V(q)+\frac{R(q)}{100}\cos(2\pi p-\alpha_0),
\tag{11}
$$

where V is the q-only part of the corrected real-half Weyl symbol of the
original A_N. In particular the p-dependent factor is R(q)=r(q+1/2), not r(q).
Set gamma=e^{-i alpha_0}/200. Then

$$
a(q,p)=V(q)+\gamma R(q)e^{2\pi ip}
                  +\overline\gamma R(q)e^{-2\pi ip}.
\tag{12}
$$

The four initial real phases and their initial momenta are

$$
\Phi^0_m(q,r)=-\frac{3q^2-2qr+3r^2}{8}+\frac{mq}{4},
\qquad p_m^0(q,r)=\frac{-3q+r+m}{4},\quad m=0,1,2,3.
\tag{13}
$$

Let Phi_m(s;q,r) be the real analytic Hamilton--Jacobi solutions

$$
\partial_s\Phi_m=a(q,\partial_q\Phi_m),\qquad
\Phi_m(0)=\Phi_m^0,
\tag{14}
$$

and put S_m=Phi_m(t)-Phi_m^0. The kernel input supplies the estimates

$$
\|S_m-t a(q,p_m^0)\|_\infty\le35000t^2,
\quad \|\partial_qS_m\|_\infty\le350t,
\quad \|\partial_rS_m\|_\infty\le50t.
\tag{15}
$$

The bounds hold uniformly on the real plane, and S_m is 4-periodic in both q
and r. To see the periodicity directly from (14), replacing q by q+4 changes
p_m^0 by -3, while replacing r by r+4 changes it by +1. These are integral p
shifts, under which a is invariant. After subtracting Phi_m^0, the same initial
value problem and uniqueness apply. The analytic characteristic construction
in the kernel source verifies uniqueness in the stated small-time class.

We use Fourier coefficients of 4-periodic functions with normalization
(1/16) integral_[0,4]^2 and frequencies in (1/4 Z)^2.
The exact coefficient R_8 of e^{2 pi i 8q} equals -1/4, since

$$
R(q)=1-\cos2\pi q+\cos14\pi q
                    -\tfrac12\cos16\pi q-\tfrac12\cos12\pi q.
\tag{16}
$$

Consequently at the off-axis frequency (29/4,1/4),

$$
\widehat {a(q,p_m^0(q,r))}(29/4,1/4)
                  =-\frac{e^{im\pi/2-i\alpha_0}}{800}.
\tag{17}
$$

The q-only part has r-frequency zero, and the other exponential in (12) has
r-frequency -1/4, so neither contributes to (17).

## 3. Every cross-branch and every reversed branch is nonseparable

### 3.1 Distinct branches of the same orientation

For m!=n, let

$$
\phi_{mn}^{\mathrm{same}}(q,r)=\Phi_m(t;q,r)-\Phi_n(t;q,r).
\tag{18}
$$

Its initial part is (m-n)q/4, a separable function. The coefficient at (29/4,1/4)
of its 4-periodic correction equals

$$
-\frac{t e^{-i\alpha_0}}{800}(i^m-i^n)+e_{mn},
\qquad |e_{mn}|\le70000t^2.
\tag{19}
$$

Because |i^m-i^n|>=sqrt(2), and 70000t<1/1600 at the fixed original parameter,
the absolute value in (19) is at least t/1600. This nonzero off-axis coefficient
implies partial_q partial_r phi_{mn}^{same} is not identically zero. One may
verify the implication by integrating derivatives twice by parts over the
4-torus; the mixed derivative has coefficient -(2pi)^2(29/4)(1/4) times (19).

The rectangular cycle of (18) loses its initial separable part. By (15) every
component of its gradient is bounded by 1400t<1/8. Thus (3) holds.

### 3.2 Oppositely oriented branches, including m=n

For arbitrary m,n in {0,1,2,3}, define

$$
\phi_{mn}^{\mathrm{rev}}(q,r)=\Phi_m(t;q,r)-\Phi_n(t;r,q).
\tag{20}
$$

Its initial part is (mq-nr)/4, again separable. The coefficient at (29/4,1/4)
of a(r,p_n^0(r,q)) vanishes: every p-dependent term in that function has
q-frequency +1/4 or -1/4, and the remaining term depends only on r. Thus the
coefficient of the periodic correction of (20) is

$$
-\frac{t e^{im\pi/2-i\alpha_0}}{800}+e'_{mn},
\qquad |e'_{mn}|\le70000t^2.
\tag{21}
$$

Its absolute value is at least t/1600. Therefore the mixed derivative of (20)
is not identically zero for any of the sixteen ordered branch pairs. Bounds
(15) give at most 800t<1/8 for each component of the rectangular cycle gradient.
Thus (3) holds here too. No approximation of N alpha_0 or averaging over a
parameter occurs in these arguments.

## 4. Exact kernel input and conclusions for the original matrices

The companion kernel construction is required to prove all of the following
for the original modular-half matrices, with every chirp branch retained:

1. Write 8^{-1}=(1+q_N N)/8, where q_N is odd modulo 8, and define
   gamma_N(x)=exp(-2pi i 3 q_N x^2/8). This is 4-periodic on the integers.
   Its discrete Fourier coefficients g_{j,N} on Z/4 have modulus 1/2.
2. There are positive analytic amplitudes B_m(t;q,r), independent of N, with
   |B_m^2-1|<=40000t, such that the matrix

$$
\mathcal V_N(x,y)=\frac{\gamma_N(y)}{\sqrt N}
 \sum_{m=0}^3g_{m-q_Ny,N}\,B_m(t;x/N,y/N)
             e^{2\pi iN\Phi_m(t;x/N,y/N)}
\tag{22}
$$

   satisfies ||U_N-mathcal V_N||_HS<=C N^{-1/2} and the stronger per-column
   l2 error <=C/N. The real phases satisfy (14)--(15) and the exact deck gluing.

This input implies sup_xy |U_N(x,y)|<=C_0/sqrt(N). It also gives, by direct
entrywise multiplication and the HS ideal inequality,

$$
\big\||U_N|^2-|\mathcal V_N|^2\big\|_{\mathrm{HS}}=O(N^{-1}),
\tag{23}
$$

and, on writing Q(W)_{xy}=W_{xy} overline{W_{yx}},

$$
\|Q(U_N)-Q(\mathcal V_N)\|_{\mathrm{HS}}=O(N^{-1}).
\tag{24}
$$

For example, the first term of the difference in (24) is
(U_N-mathcal V_N)_{xy} overline{U_{N,yx}}, whose HS norm is at most
max|U_N| ||U_N-mathcal V_N||_HS. The second term is bounded in the same way.
This uses no independence assumption.

### 4.1 Position transition probabilities mix

Set P_N(x,y)=|U_N(x,y)|^2 and let J_N have every entry 1/N. The diagonal terms
m=n in |mathcal V_N|^2 give the matrix with entries

$$
\frac1{4N}\sum_{m=0}^3 B_m(t;x/N,y/N)^2.
$$

Its difference from J_N has HS norm at most 40000t. Every term m!=n has phase
(18); after splitting row and column residues modulo 4 its coefficient is a
fixed constant times a smooth amplitude. Section 1 and Section 3.1 show that
its operator norm tends to zero. There are only finitely many terms and
residue blocks. Together with (23),

$$
\boxed{\|P_N-J_N\|_{\mathrm{op}}\le40000t+o(1).}
\tag{25}
$$

In particular ||P_N-J_N||<=1/2 for every sufficiently large odd N. Since U_N
is exactly unitary, P_N is doubly stochastic, so P_N J_N=J_N P_N=J_N.
For n>=1,

$$
P_N^n=J_N+(P_N-J_N)^n,
\qquad |\operatorname{Tr}P_N^n-1|\le (N-1)2^{-n}.
\tag{26}
$$

Only the displayed exact bistochastic property is used in (26); a replacement
of coherent powers by powers of P_N is not made.

### 4.2 The reverse-path operator has vanishing norm

Define the actual Hermitian matrix

$$
Q_N(x,y)=U_N(x,y)\overline{U_N(y,x)}.
\tag{27}
$$

Each branch pair in Q(mathcal V_N) has phase (20). The remaining factors,
including gamma_N(y) overline{gamma_N(x)} and the two g coefficients, are
constant on each row/column residue block modulo 4. Section 1 and Section 3.2
apply to all sixteen pairs, and (24) therefore proves

$$
\boxed{\|Q_N\|_{\mathrm{op}}\longrightarrow0.}
\tag{28}
$$

In particular its norm is at most 1/2 for all sufficiently large odd N.
If max_xy P_N(x,y)<=C/N, then

$$
\|Q_N\|_{\mathrm{HS}}^2
=\sum_{x,y}P_N(x,y)P_N(y,x)\le C.
\tag{29}
$$

Hermiticity and the eigenvalue formula for trace give, for n>=2,

$$
|\operatorname{Tr}Q_N^n|
\le\|Q_N\|_{\mathrm{HS}}^2\|Q_N\|_{\mathrm{op}}^{n-2}
\le C\,2^{-(n-2)}.
\tag{30}
$$

Also Tr Q_N=sum_x |U_N(x,x)|^2<=C. Consequently

$$
\boxed{\sum_{n\ge1}n|\operatorname{Tr}Q_N^n|\le7C.}
\tag{31}
$$

This is an all-time bound for a genuine signed phase sum of the original
matrix. Its interpretation as a class of ordered physical path pairs,
including the removal of periodic multiplicities and of its intersection
with the forward diagonal class, is proved in the companion root note.
It does not control every nonreversed off-diagonal pair and does not prove
H_diag.
