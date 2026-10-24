---
title: "Poisson rigidity of analytic observables under a hyperbolic toral automorphism"
author: "BGS research programme"
date: "5 September 2026"
---

# Statement and status

This note reviews the regular-gradient lemma already recorded in the project
and adds its quantitative quantum commutator consequence. The classical lemma
is not counted as a new result of this pass. It is not an assertion of priority
or a complete Lean formalization. It separates the
smooth support-separated construction from a real analytic one. In particular,
it does not identify vanishing of a Green--Kubo variance with vanishing of its
symbol: those are different conditions.

Let $S\in\mathrm{SL}(2,\mathbb Z)$ satisfy $|\operatorname{tr}S|>2$ and act on
$\mathbb T^2$ with normalized Haar measure. For real $C^1$ functions put
$\{f,h\}=f_qh_p-f_ph_q$.

**Theorem 1 (regular-gradient rigidity).** If $g\in C^1(\mathbb T^2)$ is
nonconstant and its critical set $\{dg=0\}$ has measure zero, then
$$
                  \{g,g\circ S\}\not\equiv0.                 \tag{R1}
$$
Consequently every real analytic $g$ satisfying $\{g,g\circ S\}=0$ is constant.
No parity assumption is needed. Equivalently a nonconstant $C^1$ observable
commuting with its next iterate must have a positive-measure critical set.

The analytic conclusion uses the standard measure-zero theorem for zeros of a
nontrivial real analytic function, not a new unique-continuation theorem. A short
primary reference is Boris Mityagin, *The Zero Set of a Real Analytic Function*,
[arXiv:1512.07276](https://arxiv.org/abs/1512.07276), Proposition 0.

# Proof

Suppose that $\{g,g\circ S\}=0$ and $dg\ne0$ almost everywhere. Remove the
union of all forward and backward images of the null critical set. On the
remaining invariant full-measure set define a measurable projective line
$$
                    L(x)=[\nabla g(x)]\in\mathbb {RP}^1.
$$
The chain rule and the zero determinant of the two gradients give
$$
       L(Sx)=S^{-\mathsf T}L(x).                             \tag{R2}
$$
Both gradients in this assertion are nonzero; this is exactly where the
critical-set hypothesis is required.

Push Haar measure forward by L. Equation (R2) gives an invariant probability
measure for the hyperbolic projective map $P=S^{-\mathsf T}$. Every such
probability is supported on its two eigenlines. Indeed, in an eigenbasis, the
slope away from those lines is multiplied by a fixed number $c$ with $c>1$
after possibly replacing P by its inverse. The disjoint sets
$$
          \{c^n\leq |z|<c^{n+1}\},\qquad n\in\mathbb Z,
$$
all have the same measure, so they each have measure zero. Their union is the
complement of the two eigenlines. Negative eigenvalues cause no problem:
their ratio is positive, or one may square the projective map.

The toral automorphism S is ergodic. This can be seen directly: if an $L^2$
function is invariant, its Fourier coefficients are constant along each orbit
of $S^{\mathsf T}$ on $\mathbb Z^2\setminus\{0\}$. Each such orbit is infinite,
so square summability forces every nonzero coefficient to vanish. The sets
where L equals the two eigenlines are invariant by (R2); hence one of them has
full measure. Thus $\nabla g$ lies in a single fixed eigencovector line almost
everywhere.

Let w be a nonzero vector annihilated by that covector. Its slope is irrational:
a rational eigendirection would give a rational eigenvalue of the monic
polynomial $z^2-(\operatorname{tr}S)z+1$, hence an integer eigenvalue dividing
one, contrary to hyperbolicity. We have $w\cdot\nabla g=0$ almost everywhere,
and therefore everywhere by continuity. Fourier integration by parts yields
$$
             (w\cdot v)\widehat g(v)=0\quad(v\in\mathbb Z^2).
$$
For every nonzero integer v the factor $w\cdot v$ is nonzero. All nonconstant
Fourier coefficients vanish and g is constant, the desired contradiction.

For a nonconstant real analytic g at least one of its partial derivatives is
not identically zero. Its zero set has measure zero by the analytic zero-set
theorem, and the critical set is a subset. The preceding argument proves the
analytic conclusion. This finishes the proof.

# A quantum consequence, and an important non-consequence

Specialize now to the project's $T=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$,
$S=T^{\mathsf T}$ and odd-dimensional physical Weyl quantization
$$
 Q_N(a,b)=(-1)^{ab}W_N(a,b),\qquad
 Q_N(v)Q_N(w)=e^{\pi i\omega(v,w)/N}Q_N(v+w),\qquad
 \hbar_N=(2\pi N)^{-1}.
$$
For a fixed smooth real g set $d=g\circ S$ and $h=\{g,d\}$. Then
$$
 [\operatorname{Op}_N(g),\operatorname{Op}_N(d)]
       =-i\hbar_N\operatorname{Op}_N(h)+O_g(N^{-3})
                  \quad\hbox{in operator norm}.             \tag{R3}
$$
For clarity the remainder is elementary: in the exact Fourier commutator
expand $2i\sin(\pi\omega/N)$ through its linear term and use
$|\sin u-u|\leq |u|^3/6$. The norm bound is
$\pi^3 M_3(g)M_3(d)/(3N^3)$, where
$M_j(a)=\sum_v|\widehat a(v)|\,|v|^j$.

The normalized Hilbert--Schmidt norm obeys, for every fixed smooth h,
$$
       \|\operatorname{Op}_N(h)\|_{2,N}\longrightarrow\|h\|_{L^2},
       \qquad \|B\|_{2,N}^2=N^{-1}\operatorname{Tr}(B^*B).
$$
One proof truncates its absolutely convergent Fourier series at a fixed radius;
for sufficiently large N the finite Weyl matrices are exactly orthonormal,
and the remaining norm is bounded by the Fourier l1 tail. Alternatively,
modular aliases involve at least one frequency of size at least N/2 and their
contribution is smaller than every inverse power for a fixed smooth h.
Together with (R3),
$$
 \boxed{\displaystyle
 \lim_{N\to\infty}\hbar_N^{-1}
 \|[\operatorname{Op}_N(g),\operatorname{Op}_N(g\circ S)]\|_{2,N}
                         =\|\{g,g\circ S\}\|_{L^2}.}        \tag{R4}
$$
For nonconstant analytic g the right side is strictly positive by Theorem 1.
In particular this pair of quantized observables cannot commute to every
inverse power of N. Since $\|B\|_{\mathrm{op}}\geq\|B\|_{2,N}$, it also has
an operator-norm lower bound $c_g/N$ for all sufficiently large N.

For $g=b_{(1,0)}=2\cos(2\pi q)$, direct algebra gives
$$
 \|\{g,g\circ S\}\|_2=32\pi^2,
 \quad \hbar_N^{-1}\|[\operatorname{Op}_N(g),\operatorname{Op}_N(g\circ S)]\|_{2,N}
       =8\pi N|\sin(4\pi/N)|
$$
whenever the indicated finite frequencies are distinct modulo N. This is
retained as a numerical normalization check.

**The boundary matters.** The theorem proves $\{g,g\circ S\}\ne0$, not
$\sigma^2(\{g,g\circ S\})>0$. A nonzero bracket could still be a coboundary.
Also (R4) does not exclude every conceivable unitary conjugacy at an isolated
nonzero kick strength: exponentials can have cancellations that an individual
commutator does not detect. The result excludes the all-orders commuting-
observable mechanism for a nonconstant analytic generator. It is not positive
BGS universality, nor a general classification of analytic spectral statistics.

# Relation to the smooth flat construction

The all-orders note constructs nonconstant smooth functions supported in two
small boxes whose images are disjoint from those boxes. Their derivatives
vanish on a nonempty open set, so their critical sets have positive measure.
They are precisely outside the regular-gradient hypothesis above. This yields
an explicit smooth-versus-analytic distinction without an appeal to a formal
infinite BCH or Moyal series.

Numerical checks and their scope are in `pell_flat_quantum_check.py`. The
projective measure and analytic zero-set arguments are analytic proofs, not
claims certified by finite matrices. No assertion of priority follows from
targeted searches failing to locate the exact statement.
