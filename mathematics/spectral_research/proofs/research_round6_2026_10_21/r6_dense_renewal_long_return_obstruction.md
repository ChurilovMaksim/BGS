> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_dense_renewal_long_return_obstruction.md`. Embedded SHA256: `95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2`.
> [Thematic guide](../../topics/histories.md).

# Exact renewal geometry and the obstruction to cutting off long mismatch runs

21 October 2026. This note treats the exact doubled transfer of a finite
unitary matrix. It proves a complete first-return identity, an exact
weighted return identity, a macroscopic isometric-subspace bound, and
quantitative lower bounds for the energy in long first returns.
The latter bounds apply to the prescribed deterministic family.
An auxiliary prime-dimensional example shows that even exact mixing
of every shorter physical power does not exclude a coherent first return
at time equal to the dimension.

These are statements about operator norms and positive return energies.
They do not prove a lower bound for a signed trace sum, do not refute
H_diag, and do not replace the missing estimate for the original
unequal-occupation remainder.

## 1. Doubled transfer and first returns

Let U be an N by N unitary matrix, N at least 2. Set
$$
 P_{ab}=|U_{ab}|^2,\qquad
 e=N^{-1/2}(1,\ldots,1)^T,\qquad J=ee^*.
$$
For coordinate phases $z=(z_1,\ldots,z_N)$, define
$$
 Z=\operatorname{diag}(z),\qquad
 W(z)=(ZU)\otimes\overline{ZU}.
$$
The pair space has dimension $N^2$. Let M be the orthogonal projection
onto the diagonal pair states $(a,a)$, and let $O=I-M$.
We identify the range of M with $\mathbb C^N$. Relative to this
orthogonal decomposition,
$$
 W=\begin{pmatrix}P&B\\ C&S\end{pmatrix},
 \qquad S=OWO.                                      \tag{1.1}
$$
Here and below a displayed block denotes the corresponding map between
the indicated subspaces. The first-return operators on M are
$$
 F_1=P,\qquad F_r=BS^{r-2}C\quad(r\ge2).             \tag{1.2}
$$
Thus $F_r$ has r transfer edges and exactly $r-1$ consecutive
off-diagonal internal pair states.

The unrestricted returns are
$$
 R_0=I_M,\qquad R_n=MW^nM
   =|U Z U\cdots ZU|^{\circ2}\quad(n\ge1),           \tag{1.3}
$$
with n copies of U and $n-1$ inner copies of Z on the right.
The omitted leftmost Z in $(ZU)^n$ has no effect on entry moduli.
Every R_n is doubly stochastic, because its underlying matrix is
unitary. Splitting a path at its first return to M gives the exact
noncommutative renewal relation
$$
 R_n=\sum_{r=1}^n F_rR_{n-r}.                        \tag{1.4}
$$
Equivalently, as a formal power series,
$$
 R(s)=\sum_{n\ge0}s^nR_n
  =\left(I-\sum_{r\ge1}s^rF_r\right)^{-1}.          \tag{1.5}
$$
These identities also follow by the Schur complement of $I-sW$;
they require no spectral limit.

### Vanishing on constants

For every phase vector,
$$
 F_re=0,\qquad e^*F_r=0\qquad(r\ge2).                \tag{1.6}
$$
Indeed, $R_ne=e$, $e^*R_n=e^*$, and $F_1=P$ preserves constants
on both sides. Equation (1.4) proves (1.6) by induction. This is an exact
consequence of bistochasticity, rather than a mixing assumption.

Write $E_n=R_n-J$, $n\ge1$. Using (1.6), (1.4) gives
$$
 F_r=E_r-E_1E_{r-1}
       -\sum_{j=2}^{r-1}F_jE_{r-j}\quad(r\ge2).     \tag{1.7}
$$
All F_r are contractions, since every factor in (1.2) is a compression
of a unitary. A doubly stochastic matrix is an $\ell^2$ contraction:
Jensen's inequality bounds each squared row average, and its column
sums give the result after summation. Thus $\|E_1\|_{\rm op}\le1$.
Consequently,
$$
 \boxed{\ \|F_r\|_{\rm HS}
        \le\sum_{j=1}^r\|E_j\|_{\rm HS}\quad(r\ge2).\ }              \tag{1.8}
$$
For example $F_2=R_2-P^2$, the exact two-step defect used in the
isolated-substitution calculation.

## 2. Complete first-return energy: no hidden recurrence hypothesis

Unitarity in (1.1) gives
$$
 P^*P+C^*C=I_M,\qquad B^*B+S^*S=I_O,\qquad
 CC^*+SS^*=I_O.                                    \tag{2.1}
$$
For $m\ge1$, a finite telescoping calculation yields
$$
 \sum_{r=1}^{m+1}F_r^*F_r
  =I_M-C^*S^{*m}S^mC.                              \tag{2.2}
$$
To justify that the remainder tends to zero, put
$$
 a_m=\|S^m\|_{\rm HS}^2,\qquad m\ge0.
$$
The sequence a_m is nonnegative and nonincreasing. The last identity
in (2.1) gives the exact equality
$$
 \|S^mC\|_{\rm HS}^2
 =\operatorname{Tr}\bigl(S^m(I-SS^*)S^{*m}\bigr)
 =a_m-a_{m+1}\longrightarrow0.                     \tag{2.3}
$$
Differences of a convergent monotone real sequence tend to zero.
The positive remainder in (2.2) therefore tends to zero in norm.
This proves, without assuming the absence of dark states,
$$
 \boxed{\ \sum_{r\ge1}F_r^*F_r=I_M,\qquad
          \sum_{r\ge1}\|F_r\|_{\rm HS}^2=N.\ }       \tag{2.4}
$$
Applying the same argument to $W^*$, whose first returns are
$F_r^*$, also proves
$$
 \sum_{r\ge1}F_rF_r^*=I_M.                          \tag{2.5}
$$
All sums of positive matrices converge in the finite-dimensional
operator norm.

For $m\ge1$, (2.2) also gives the useful exact tail formula
$$
 \boxed{\ \sum_{r>m}\|F_r\|_{\rm HS}^2
       =\|S^{m-1}C\|_{\rm HS}^2
       =a_{m-1}-a_m.\ }                            \tag{2.6}
$$

## 3. Weighted return identity and the dark subspace

Let $\mathcal H_{\rm dark}$ be the maximal reducing subspace of S
on which S is unitary. It lies inside O. We establish directly that
$$
 \lim_{m\to\infty}\|S^m\|_{\rm HS}^2
       =\dim\mathcal H_{\rm dark}.                 \tag{3.1}
$$
If $Sv=\lambda v$, $|\lambda|=1$, contractivity implies
$\langle v,(I-S^*S)v\rangle=0$. Positivity therefore gives
$S^*Sv=v$, and hence $S^*v=\overline\lambda v$.
The line spanned by v is reducing. Iterating on its orthogonal
complement splits off every unit-circle eigenvalue. The remaining
finite-dimensional restriction has spectral radius strictly less
than one, so its powers tend to zero. For completeness, this last
claim follows from Jordan form: every block is a fixed-degree
polynomial in m times $\lambda^m$, which tends to zero when
$|\lambda|<1$. This proves (3.1).

For a vector v in the unitary subspace, (2.1) implies $Bv=0$
and $C^*v=0$. Thus these states are both unreachable from M
and unable to return to M. The above argument also proves that they
are the entire obstruction to decay of S itself.

Using the elementary tail-sum identity for a nonnegative sequence,
(2.4), (2.6), and monotone convergence,
$$
\begin{aligned}
 \sum_{r\ge1}r\|F_r\|_{\rm HS}^2
 &=N+\sum_{m\ge1}\sum_{r>m}\|F_r\|_{\rm HS}^2\\
 &=N+\sum_{m\ge1}(a_{m-1}-a_m)\\
 &=N+(N^2-N)-\dim\mathcal H_{\rm dark}.
\end{aligned}
$$
Therefore
$$
 \boxed{\ \sum_{r\ge1}r\|F_r\|_{\rm HS}^2
          =N^2-\dim\mathcal H_{\rm dark}\le N^2.\ } \tag{3.2}
$$
This is a finite-dimensional return identity. It does not imply
a negligible tail after a fixed number of returns: its immediate
bound is only
$$
 \sum_{r>L}\|F_r\|_{\rm HS}^2\le N^2/(L+1).        \tag{3.3}
$$

## 4. Exact isometric subspaces through times of order N

The vector
$$
 \Omega=N^{-1/2}\sum_a|a,a\rangle
$$
belongs to M and is fixed by W. This follows directly from
$(ZU)(ZU)^*=I$. Define
$$
 \mathcal E_m
 =\{v\in O:MW^jv=0,\ 1\le j\le m\},
 \qquad m\ge0.                                    \tag{4.1}
$$
Because $W\Omega=\Omega$, each condition in (4.1) has its image
inside the $(N-1)$-dimensional space
$M\cap\Omega^\perp$. It imposes at most $N-1$ independent
linear conditions on O. Thus
$$
 \boxed{\ \dim\mathcal E_m
       \ge (N^2-N)-m(N-1)=(N-1)(N-m).\ }            \tag{4.2}
$$
For $v\in\mathcal E_m$, induction gives
$S^jv=W^jv$ for $0\le j\le m$, because no projection at an
intermediate step removes any component. In particular
$\|S^mv\|=\|v\|$.

The matrix $I-S^{*m}S^m$ is positive semidefinite. Its quadratic
form vanishes on $\mathcal E_m$, so it annihilates that subspace.
Hence at least $(N-1)(N-m)$ singular values of $S^m$ are
exactly one. For every $1\le m<N$ and every phase vector,
$$
 \boxed{\ \|S^m\|_{\rm op}=1,\qquad
          \|S^m\|_{\rm HS}^2\ge(N-1)(N-m).\ }       \tag{4.3}
$$
Thus operator-norm contraction of the propagation inside O cannot
be deduced from fast mixing of P. The obstruction persists on
subspaces of dimension proportional to $N^2$, up to times
proportional to N with proportionality constant less than one.
This statement concerns singular values and makes no claim about
the signed value of $\operatorname{Tr}S^m$.

## 5. Almost all return energy is beyond every fixed cutoff

### 5.1 A deterministic short-return estimate

Suppose numbers $h_1,\ldots,h_L\ge0$ satisfy
$$
 \|R_j-J\|_{\rm HS}^2\le h_j,\qquad1\le j\le L.
$$
By (1.8) and Cauchy--Schwarz,
$$
 \sum_{r=1}^L\|F_r\|_{\rm HS}^2
 \le K_L(h):=
 1+h_1+\sum_{r=2}^L r\sum_{j=1}^r h_j.             \tag{5.1}
$$
Combining with (2.4) gives the exact consequence
$$
 \boxed{\ N-K_L(h)
       \le\sum_{r>L}\|F_r\|_{\rm HS}^2\le N.\ }     \tag{5.2}
$$
In particular, if every $h_j$, $j\le L$, is bounded independently
of N, the long-return energy divided by N tends to one.

If a physical power has entry bound
$$
 \max_{a,b}|(U^j)_{ab}|\le A_j/\sqrt N,
$$
then at $z=1$,
$$
 \|R_j-J\|_{\rm HS}^2
 =\sum_{a,b}|(U^j)_{ab}|^4-1
 \le A_j^2-1.                                     \tag{5.3}
$$
Indeed the sum of $|(U^j)_{ab}|^2$ is N, and its largest term
is at most $A_j^2/N$. This verifies all hypotheses of (5.2)
from finitely many entry estimates.

### 5.2 An unconditional phase-averaged estimate for every fixed cutoff

Assume only
$$
 \max_{a,b}|U_{ab}|^2\le C/N,\qquad C\ge1.          \tag{5.4}
$$
Let the coordinate phases be independent and uniform on the unit
circle, used only as an auxiliary exact Fourier variable.
For each fixed $j\ge1$, expansion of four copies of a matrix
element in (1.3) gives
$$
 \mathbb E_z\sum_{a,b}
    |(U ZU\cdots ZU)_{ab}|^4
       \le C^{2j}(2j-2)!.                         \tag{5.5}
$$
Here is a direct count proving the inequality. Each of the two
positive phase paths has $j-1$ internal positions, so there
are $N^{2j-2}$ choices for their concatenation. Phase
orthogonality forces the concatenation of the two negative paths
to have the same occupation multiset. It has at most
$(2j-2)!$ possible ordered realizations. There are $N^2$
endpoint choices. Each product has $4j$ entries of U in total,
and its modulus is at most $(C/N)^{2j}$. The product of these
four bounds is precisely (5.5). Taking absolute values here is
legitimate for this positive fourth-moment bound; it is not being
used to estimate a spectral form factor.

For every doubly stochastic R,
$\|R-J\|_{\rm HS}^2=\sum_{a,b}|R_{ab}|^2-1$.
Set
$$
 h_1(C)=C-1,\qquad
 h_j(C)=C^{2j}(2j-2)!-1\quad(j\ge2),
$$
$$
 K_L(C)=C+\sum_{r=2}^L r\sum_{j=1}^r h_j(C).        \tag{5.6}
$$
The $j=1$ estimate uses the sharper direct inequality
$\sum P_{ab}^2\le C$. Equations (1.8), (2.4), and (5.5)
prove, for every N and fixed finite L,
$$
 \boxed{\ N-K_L(C)
 \le \mathbb E_z\sum_{r>L}\|F_r(z)\|_{\rm HS}^2
 \le N.\ }                                        \tag{5.7}
$$
The constant grows rapidly with L, but is finite and independent
of N. Therefore every flat family satisfying (5.4) obeys
$$
 \lim_{N\to\infty}\frac1N
       \mathbb E_z\sum_{r>L}\|F_r(z)\|_{\rm HS}^2=1
 \quad\text{for each fixed }L.                    \tag{5.8}
$$
The already established entry bound $C=9$ for the prescribed
family verifies (5.4) on all sufficiently large odd N. Thus
(5.7)--(5.8) apply to that same family, without changing its kick
parameter or restricting to primes.

These auxiliary-phase energies are not a substitute random spectral
model. The conclusion is a proved obstruction to a proposed norm
estimate for exactly the doubled operators of the original U.

### 5.3 The original matrix at the original phase vector

The direct fixed-power entry theorem, in the companion source
of the original-family branch, gives
$$
 \max_{a,b}|(U_N^j)_{ab}|
   \le\frac{2\sqrt{b_j}}{\sqrt N},
       \qquad1\le j\le49,                          \tag{5.9}
$$
for all sufficiently large odd N. The integers $b_j>0$ are
the upper-right entries of
$$
 \begin{pmatrix}3&4\\2&3\end{pmatrix}^{j}
 =\begin{pmatrix}a_j&b_j\\c_j&a_j\end{pmatrix}.
$$
This paragraph uses only (5.9), not any quantum decorrelation
claim. Define the explicit finite constant
$$
 K^{\rm phys}_{49}
 =4b_1+\sum_{r=2}^{49}r
           \sum_{j=1}^r(4b_j-1).                  \tag{5.10}
$$
Equations (5.2)--(5.3) give, at $z=(1,\ldots,1)$,
$$
 \boxed{\ N-K^{\rm phys}_{49}
       \le\sum_{r>49}\|F_r(1)\|_{\rm HS}^2\le N.\ } \tag{5.11}
$$
Consequently the energy beyond 49 tends to N in relative terms
for the actual prescribed matrix, with no phase average.
The full physical-entry proof and its independent audit are listed
with frozen hashes below. Only their explicit entry estimate
is used in this implication.

## 6. A sharp delayed-return example

This section is an auxiliary example, not a replacement for the
specified family. Let p be an odd prime, let
$e_p(t)=\exp(2\pi i t/p)$, and set
$$
 (\mathcal F_p)_{ak}=p^{-1/2}e_p(ak),\qquad
 U_p=\mathcal F_p^*\operatorname{diag}(e_p(k^2))\mathcal F_p.
                                                               \tag{6.1}
$$
This is unitary and $U_p^p=I$. Its powers have entries
$$
 (U_p^j)_{ab}
 =p^{-1}\sum_{k\bmod p}e_p(jk^2+(b-a)k).            \tag{6.2}
$$
If p does not divide j, the squared modulus of the unnormalized
sum equals
$$
 \sum_{h\bmod p}e_p(jh^2+(b-a)h)
                   \sum_{\ell\bmod p}e_p(2jh\ell)=p.
                                                               \tag{6.3}
$$
Only $h=0$ survives, since $2j$ is invertible modulo p.
If p divides j, (6.2) is the Kronecker delta. Therefore at $z=1$,
$$
 R_n=
 \begin{cases}
 I,&p\mid n,\\
 J,&p\nmid n.
 \end{cases}                                       \tag{6.4}
$$
In particular $P=J$, and every physical power strictly before p
is exactly flat.

Uniqueness in the renewal recursion proves
$$
 \boxed{\ F_1=J,\quad F_p=I-J,\quad
               F_r=0\ (r\ne1,p).\ }               \tag{6.5}
$$
For a direct verification, the right side of (1.4) with these
proposed first returns equals J, plus $I-J$ exactly when p
divides n. At $n=1$ it equals J as well. It therefore reproduces
every R_n in (6.4), proving (6.5) for all n, rather than just
through the first period.

Thus a coherent first return of norm one and energy $p-1$
occurs at time p, while all first returns from 2 through $p-1$
vanish exactly. Both entry flatness and complete mixing of every
fixed list of short physical powers hold for all sufficiently
large primes in this example.

Its weighted return identity is
$$
 \sum_r r\|F_r\|_{\rm HS}^2=1+p(p-1)=p^2-p+1,
$$
so $\dim\mathcal H_{\rm dark}=p-1$. More precisely, (2.6)
and (6.5) give
$$
 \|S^m\|_{\rm HS}^2=
 \begin{cases}
 (p-1)(p-m),&0\le m\le p-1,\\
 p-1,&m\ge p-1.
 \end{cases}                                       \tag{6.6}
$$
In the first line at $m=0$, the value is $p^2-p$,
the dimension of O. The universal bound (4.3) is therefore
sharp throughout its full nontrivial time range.

**Scope of the example.** The matrix in (6.1) is symmetric, so
the reverse-transfer matrix
$$
 Q_{ab}=U_{ab}\overline{U_{ba}}
$$
equals J and has norm one. Thus this example does not satisfy
any additional upstream hypothesis asserting a small reverse-transfer
norm. It specifically disproves the implication from short R_n,
flat entries, and mixing of P to a negligible long-return norm.
It is not a counterexample to H_diag for the original family.
Nor can a one-dimensional quadratic metaplectic shear remove this
qualification: a flat kernel
$p^{-1/2}e_p(Aa^2+Bab+Db^2)$ has
$Q_{ab}=p^{-1}e_p((A-D)(a^2-b^2))$, a rank-one matrix of norm one.

## 7. Exact bounded-run resummation without marking multiplicity

The geometry above can be attached to an actual class of rooted
path pairs. Fix an integer $L\ge1$. Let $\mathcal C_{n,L}$
consist of all ordered rooted cyclic pairs
$(x_0,\ldots,x_{n-1};y_0,\ldots,y_{n-1})$ that have at least
one agreement $x_i=y_i$, and for which every consecutive cyclic
run of disagreements has length at most L. Physical vertex
labels may repeat arbitrarily. Each pair is included exactly once.

On $M\oplus O_1\oplus\cdots\oplus O_L$, where each O_j is a
copy of O, form the block matrix A_L with nonzero blocks
$$
 (A_L)_{00}=P,\quad (A_L)_{0,1}=B,\quad
 (A_L)_{j,0}=C\ (1\le j\le L),\quad
 (A_L)_{j,j+1}=S\ (1\le j<L).                     \tag{7.1}
$$
The copies O_j record the length of the current disagreement run.
Every closed walk of A_L visits M, since motion confined to the
O copies strictly increases the age and cannot close.
For every physical pair in $\mathcal C_{n,L}$, all ages are
uniquely forced by its most recent cyclic agreement. Thus there
is exactly one lift for the specified root; there is no division
by the number of agreements or any choice of a marked one.

With $a(x)=\prod_iU_{x_i x_{i+1}}$ and occupation vector d(x),
the exact identity is
$$
 \operatorname{Tr}A_L(z)^n
 =\sum_{(x,y)\in\mathcal C_{n,L}}
       a(x)\overline{a(y)}\,z^{d(x)-d(y)}.          \tag{7.2}
$$
Consequently
$$
 \operatorname{Tr}A_L(1)^n-\mathbb E_z\operatorname{Tr}A_L(z)^n
 =\sum_{\substack{(x,y)\in\mathcal C_{n,L}\\d(x)\ne d(y)}}
        a(x)\overline{a(y)}.                     \tag{7.3}
$$
This is an exact class of the actual unequal-occupation remainder.
The all-agreement terms cancel automatically. Pairs having no
agreement anywhere are excluded explicitly, and must not be
silently assigned to this class.

Eliminating the upper-triangular O block proves the finite
determinant identity
$$
 \det(I-sA_L)
 =\det\left(I-sP-\sum_{r=2}^{L+1}s^rF_r\right).
                                                               \tag{7.4}
$$
The companion matrix on $L+1$ copies of $\mathbb C^N$,
with top block row $F_1,F_2,\ldots,F_{L+1}$ and identity
subdiagonal, has the same determinant. The formal identity
$$
 -\log\det(I-sA)=\sum_{n\ge1}s^n\operatorname{Tr}(A^n)/n
$$
then proves equality of all power traces, exactly and without a
spectral approximation. For $L=1$ this is the previously proved
isolated-substitution resummation.

Sections 2--6 explain the obstruction to extending an argument
by simply increasing a fixed cutoff L and taking norms of the
omitted returns. Almost the entire first-return energy can remain
beyond L, including for the prescribed family. Its propagation
also has exactly unit singular values until times of order N.
Additional phase cancellation involving those long runs is needed;
neither (7.4) nor short-power flatness supplies it.

## 8. What is proved and what remains open

The proved conclusions are:

1. Complete first-return energy, the weighted return identity, and
   the exact tail formula for every finite unitary and every phase.
2. At least $(N-1)(N-m)$ exactly unit singular values of $S^m$
   for each $m<N$.
3. For every flat family, and hence the prescribed one, the
   auxiliary-phase averaged energy after each fixed cutoff is
   $N-O_L(1)$. The physical fixed-power estimate (5.9) likewise
   implies $N-O(1)$ energy after 49 at the original phase vector.
4. A sharp explicit delayed-return example satisfying exact
   mixing of all shorter physical powers, with the stated
   reverse-transfer limitation.
5. An exact unmarked bounded-run identity for a genuine class
   of the original unequal-occupation remainder.

No norm or energy identity here controls the signed contribution
of all long runs to the original form factor. The first unresolved
step in this route is a cancellation estimate for that complementary
class on times $n\asymp N$, with all repeated labels allowed.
The positive lower bounds above prohibit replacing that estimate
by an assertion that the omitted first-return norms are small.
There is no claim of H_diag, Sine_2 convergence, or their negation.

## Source and verification record

All finite-dimensional statements in this note are proved here.
The original-family input and complete proof dependencies are:

- For the bound $\max|U_N|^2\le9/N$, valid for all sufficiently
  large odd N: research_round5_2026_10_21/dual_physical_four_branch_kernel.md,
  SHA256 0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c.
- For (5.9): research_round6_2026_10_21/r6_original_fixed_powers_49.md,
  theorem (1.8), with the integer hypothesis check in §7,
  SHA256 3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019.
  Its explicit condition $51200t\Sigma_R^2\le1$, at the exact
  original $t=10^{-80}/(2\pi)$, is proved there for each
  $1\le R\le49$; the same finite collection has a common eventual
  threshold in odd N.
- Independent audit of the latter complete proof:
  research_round6_2026_10_21/r6_occupation_audit_fixed_powers_49.md,
  SHA256 0953ee6eb3c665fe667fabcb094651eb7284f6250ebfa2c6d535bd98f7da9b61.

The weaker choice C=16 in (5.4) follows already from the R=1
case of the fixed-power theorem, if one wishes to use that
single source for both original-family applications.

Exact finite algebra checks are recorded separately in
r6_dense_renewal_exact_checks.py and
r6_dense_renewal_exact_checks_result.md.
They completed successfully on four exact rational block cases,
38,188 rooted pairs with formal Laurent coordinate phases,
and 746 exact Gauss modulus identities in cyclotomic rings.
The checks include block renewal, finite energy remainders,
isometric ranks, twelve full companion determinant comparisons,
all mismatch-count coefficients in bounded-run rooted counting,
and delayed-return identities for primes 3, 5, 7, 11, and 13.
They verify finite algebra, rather than a spectral asymptotic.
