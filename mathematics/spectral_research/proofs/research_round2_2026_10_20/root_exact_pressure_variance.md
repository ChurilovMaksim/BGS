> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_exact_pressure_variance.md`. Embedded SHA256: `124d807b0e7cb180b4296bdb5309d805e8920b55aabf52c0ac1188f77c43db4b`.
> [Thematic guide](../../topics/classical_trace.md).

# Exact first-variation variance for the specified perturbation

## Status

This is an exact calculation for the ordinary Weyl symbol of the matrix
family in the question. It gives the quadratic coefficient in the
pressure expansion. The independent quantified pressure theorem is now
proved and audited in `fermionic_quantitative_pressure.md`, SHA-256
`d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2`.
Combining the two proves the fixed-parameter estimate in Section 4.
Neither this variance calculation nor that pressure theorem proves
the Heisenberg-time trace decorrelation needed for H_diag.

Throughout, the torus carries normalized Lebesgue measure, and

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
\lambda=3+2\sqrt2,\qquad h_0=\log\lambda.
$$

## 1. The symbol and the first variation

For odd N the ordinary real-half Weyl operator is

$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
$$

Indeed the inverse of 2 modulo N is represented by `(N+1)/2`.
Substituting this in the given T_N formula proves the identity
directly, for all integer k,l. Thus the ordinary symbol of A_N is

$$
a(q,p)=V(q)+\frac{r(q+1/2)}{100}
                  \cos(2\pi p-\alpha_0),
$$

$$
V(q)=\cos(14\pi q)+\frac{r(q)}{10}
  +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10},\qquad
r(q+1/2)=(1+\cos(14\pi q))(1-\cos(2\pi q)).
\tag{1.1}
$$

In particular, the p-dependent term must use `r(q+1/2)`, not r(q).

Let `X=(a_p,-a_q)/(2 pi)`, and let Phi_s be its Hamiltonian flow.
For the family `F_s=S Phi_s`, select the unstable vector with its
unstable coordinate equal to one, after conjugating the base to S.
The logarithmic coordinate multiplier, denoted psi_s, has first variation

$$
\xi=\left.\partial_s\psi_s\right|_0
       =\frac{a_{pp}-2a_{qq}}{4\pi\sqrt2}.
\tag{1.2}
$$

Here is the algebra behind (1.2). Take
`ell_u=(1,sqrt(2))` and `e_u=(1/2,1/(2 sqrt(2)))`, so
`ell_u e_u=1`, `ell_u S=lambda ell_u`, and `S e_u=lambda e_u`.
At zero the derivative cocycle is the constant S. Differentiating
its coordinate expansion gives `ell_u (DX)e_u`; the derivative of
the structural conjugacy contributes zero because DS is constant,
and the first derivative of the normalized direction is killed
by ell_u. Since

$$
DX=\frac1{2\pi}
\begin{pmatrix}a_{pq}&a_{pp}\\-a_{qq}&-a_{qp}\end{pmatrix},
$$

matrix multiplication proves (1.2). The invariant-section existence
and its parameter differentiability are proved separately in
`arithmetic_pressure_analytic_potential.md`; this calculation does
not assume that the structural conjugacy is differentiable in space.

Writing `a=sum a_hat(k,l) exp(2 pi i(kq+lp))`, (1.2) gives

$$
\widehat\xi(k,l)=\frac\pi{\sqrt2}(2k^2-l^2)\widehat a(k,l).
\tag{1.3}
$$

Its mean is zero. The exact finite Fourier table is as follows.
For l=0 and positive k, the nonzero entries are

| k | a_hat(k,0) |
|---:|:---|
| 1 | 1/20 - i/200 |
| 2 | -i/400 |
| 5 | -i/800 |
| 6 | -1/40 - i/400 |
| 7 | 9/20 |
| 8 | -1/40 + i/400 |
| 9 | i/800 |

The negative k entries are their complex conjugates. For l=1:

| k | a_hat(k,1) |
|---:|:---|
| 0 | -3/1000 - i/250 |
| +1, -1 | 3/2000 + i/500 |
| +6, -6 | 3/4000 + i/1000 |
| +7, -7 | -3/2000 - i/500 |
| +8, -8 | 3/4000 + i/1000 |

The l=-1 entries are the complex conjugates of the l=1 entries
at the same k. All other entries vanish. The table follows by
expanding (1.1), using
`exp(-i alpha_0)=(-3-4i)/5`. It contains 32 nonzero modes.

## 2. Complete classification of the frequency intersections

Put `Q(k,l)=2k^2-l^2`. Direct substitution gives

$$
S^{\mathsf T}(k,l)=(3k+2l,4k+3l),\qquad
Q(S^{\mathsf T}(k,l))=Q(k,l).
\tag{2.1}
$$

Every mode in (1.3) has `|l|<=1`. If both n=(k,l) and
`(S^T)^j n=(k',l')` belong to the support, equality of Q implies

$$
2(k^2-k'^2)=l^2-l'^2.
$$

The right side belongs to {-1,0,1}, whereas the left side is even.
Hence `|l|=|l'|` and `|k|=|k'|`.

The real linear functional

$$
z(k,l)=\sqrt2 k+l
$$

satisfies `z(S^T n)=lambda z(n)`. If l=0, the candidate target
is n or -n, neither possible at a nonzero time because lambda^j
is positive and different from one. If k=0 and |l|=1, the same
argument applies.

It remains to consider k nonzero and |l|=1. Multiplying n by -1
if needed lets us take k>=1. Both possible z values are positive,
so k' must also equal k. For a positive time j, the only possible
change is `(k,-1)` to `(k,1)`, requiring

$$
\lambda^j=\frac{\sqrt2 k+1}{\sqrt2 k-1}.
\tag{2.2}
$$

For k=1 this ratio is lambda; for k>=2 it lies strictly between
one and lambda. Therefore the only positive-time intersections are

$$
j=1:\quad(1,-1)\mapsto(1,1),\qquad
(-1,1)\mapsto(-1,-1).
\tag{2.3}
$$

This proves the classification at **all** times; a finite numerical
search over j is not being used.

## 3. Exact variance

Define

$$
C_j=\int_{\mathbb T^2}\xi(x)\xi(S^j x)\,dx.
$$

Fourier orthogonality and reality give

$$
C_j=\sum_n\widehat\xi(n)
                  \overline{\widehat\xi((S^{\mathsf T})^j n)}.
\tag{3.1}
$$

Section 2 proves `C_j=0` for every `|j|>=2`, and invariance of
Lebesgue measure gives `C_-j=C_j`.

For j=0, substituting the table in (1.3) gives the following
contributions to `C_0/pi^2`. Each l=0 row includes both signs of k;
each remaining row includes both signs of l and of nonzero k.

| group | contribution to C_0/pi^2 |
|:---|---:|
| l=0, k=+/-1 | 101/10000 |
| l=0, k=+/-2 | 1/2500 |
| l=0, k=+/-5 | 1/256 |
| l=0, k=+/-6 | 8181/2500 |
| l=0, k=+/-7 | 194481/100 |
| l=0, k=+/-8 | 6464/625 |
| l=0, k=+/-9 | 6561/160000 |
| l=+/-1, k=0 | 1/40000 |
| l=+/-1, k=+/-1 | 1/80000 |
| l=+/-1, k=+/-6 | 5041/320000 |
| l=+/-1, k=+/-7 | 9409/80000 |
| l=+/-1, k=+/-8 | 16129/320000 |

Their sum is

$$
C_0=\frac{313386243}{160000}\pi^2.
\tag{3.2}
$$

For j=1 only the two intersections (2.3) contribute. Here Q=1.
With `c=3/2000+i/500`, their sum before the factor pi^2/2 is

$$
c^2+\overline c^{\,2}
=2\left[\left(\frac3{2000}\right)^2-
         \left(\frac1{500}\right)^2\right]
=-\frac7{2000000}.
$$

Thus

$$
C_1=C_{-1}=-\frac7{4000000}\pi^2.
\tag{3.3}
$$

Expanding the square of a Birkhoff sum, for every n>=1 one obtains

$$
\int\left(\sum_{r=0}^{n-1}\xi(S^r x)\right)^2dx
=nC_0+2(n-1)C_1.
$$

Consequently the variance limit exists with the exact value

$$
\boxed{\sigma^2(\xi)=
\lim_{n\to\infty}\frac1n\int
 \left(\sum_{r=0}^{n-1}\xi(S^r x)\right)^2dx
=\frac{7834656061}{4000000}\pi^2>0.}
\tag{3.4}
$$

This is also an explicit obstruction to xi being a square-integrable
coboundary `v-v circ S`: such a coboundary has Birkhoff-sum L2 norm
at most `2||v||_2`, contradicting (3.4).

## 4. The proved pressure expansion and its logical boundary

The independently audited quantitative pressure theorem specified
at the beginning of this note supplies differentiation and a
numerical Cauchy remainder. Write
`psi_s=h_0+s xi+s^2 zeta/2+O(s^3)` and

$$
p_t(s)=P_S(-t\psi_s).
$$

The first and second derivative identities, proved directly by
differentiating the simple transfer-operator eigenvalue in Section 6
of that theorem, read

$$
p_t'(0)=-t\int\xi=0,\qquad
p_t''(0)=t^2\sigma^2(\xi)-t\int\zeta.
\tag{4.1}
$$

For the actual area-preserving family, the exact endpoint identity
`p_1(s)=0` for real small s implies `int zeta=sigma^2(xi)`. Hence

$$
\frac{h_0}{2}-p_{1/2}(s)
=\frac{\sigma^2(\xi)}8s^2+O(s^3),
\qquad
\boxed{\frac{\sigma^2(\xi)}8
=\frac{7834656061\pi^2}{32000000}
\simeq2416.404873145844.}
\tag{4.2}
$$

The same theorem constructs a holomorphic pressure branch on the
complex parameter disk of radius `2*10^-24`, bounded by `1/12` on
the circle of radius `10^-24`. It proves the explicit remainder

$$
\boxed{\left|\frac{h_0}{2}-p_{1/2}(s)
       -\frac{7834656061\pi^2}{32000000}s^2\right|
\le10^{72}|s|^3,\qquad |s|\le5\cdot10^{-25}.}
\tag{4.3}
$$

Thus at the fixed `tau=10^-80` the error is at most
`10^-8 tau^2`; in particular the actual forward and inverse pressure
gaps are at least `2000 tau^2`. This conclusion uses the now-proved
quantitative remainder, not an unspecified small-parameter asymptotic.
The operator construction, its explicit spectral gap, the identification
with torus pressure, and the inverse-map convention are all given in
the cited frozen proof. No unproved universality assumption is involved.

## 5. Computational certificate

`root_exact_pressure_variance.py` reconstructs the finite polynomial
from the original r, sin, and cosine factors using pairs of rational
numbers. It checks the displayed table, the invariant Q identity, the
exact variance values, and the grouped sum. The all-time intersection
claim is proved in Section 2, rather than inferred from this finite
calculation.
