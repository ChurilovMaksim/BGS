> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_weyl_return_windows.md`. Embedded SHA256: `d9f9236b57eab1728ba4f1905b4f382af8dc53fa698d6a3fb92487f2c9c86643`.
> [Thematic guide](../../topics/dephasing.md).


# A uniform time-window bound for all Weyl return energies

Research continuation, 20 October 2026. This note concerns the original
`U_N`, with fixed `tau=10^-80` and all sufficiently large odd dimensions.
It is an actual consequence of the new twisted pressure theorem; it
does not use a comparison family or a statistical replacement.

The frozen input is `fermionic_twisted_pressure.md`, SHA-256
`9bfc9b4a27e8cd7d23bc1693d439f7cb0be31321fbe1947875d9bb8271649bd5`.
It proves that, for each fixed eta>0 and `a=exp(P_*+eta)>1`, there
are constants C and N_0 such that

$$
\sup_v {1\over N}|\operatorname{Tr}(T_N(v)^*U_N^d)|
\le C a^{|d|}/N\qquad(d\in\mathbb Z\setminus\{0\},\ N\ge N_0).
\tag{1}
$$

The negative-time version follows by adjunction and cyclicity from
the positive-time theorem. The exact exponentially small residual
has been absorbed into C. The pressure satisfies
`0<P_*<log(lambda)/2`, `lambda=3+2sqrt(2)`.

Define the maximal squared Weyl overlap

$$
Q_N(m)=\max_{v\in(\mathbb Z/N\mathbb Z)^2}
     {|\operatorname{Tr}(T_N(v)^*U_N^m)|^2\over N^2}.
\tag{2}
$$

Unitarity gives `0<=Q_N(m)<=1` and `Q_N(0)=1`.

## 1. A finite frame with a Weyl index chosen at every time

For every integer m and every integer L>=1,

$$
\boxed{
\sum_{j=0}^{L-1}Q_N(m+j)
\le 1+{2C\over N}\sum_{d=1}^{L-1}a^d.
}
\tag{3}
$$

**Proof.** Give the matrix space its normalized Hilbert--Schmidt
inner product ` <A,B>=Tr(A^*B)/N `. Choose, for each j, a Weyl index
v_j attaining the maximum in (2) at time m+j. Put

`A_j=T_N(v_j)U_N^(-j)`, `f=U_N^m`.

All these matrices have norm one. Cyclicity of the trace gives

$$
|\langle A_j,f\rangle|^2=Q_N(m+j).
\tag{4}
$$

The exact Weyl product and another cyclic permutation give, for j!=k,

$$
|\langle A_j,A_k\rangle|
={1\over N}|\operatorname{Tr}(T_N(v_k-v_j)U_N^{j-k})|
\le C a^{|j-k|}/N.
\tag{5}
$$

Only the modulus is asserted in the middle expression; the omitted
Weyl-product scalar has modulus one. The Gram matrix G of these L
unit vectors consequently has

$$
\lambda_{\max}(G)\le1+{2C\over N}\sum_{d=1}^{L-1}a^d.
$$

This follows either from row sums of `G-I` or directly from
`2|z_j z_k|<=|z_j|^2+|z_k|^2`. For an arbitrary finite family of
vectors, its analysis operator has squared norm lambda_max(G).
Applying this to f and using (4) proves (3). QED.

The maximum in Q is allowed to select a different Weyl operator at
every time. This point uses the uniformity over all Weyl indices in
(1); a scalar trace bound alone would not justify (5).

For

$$
L_N=\left\lfloor{\log N-2\log\log N\over P_*+\eta}\right\rfloor,
\tag{6}
$$

the geometric sum in (3) is `O((log N)^(-2))`. Thus

$$
\boxed{
\sup_{m\in\mathbb Z}\sum_{j=0}^{L_N-1}Q_N(m+j)
\le1+O_\eta((\log N)^{-2}).
}
\tag{7}
$$

In particular (7) is uniform over window locations m of order N,
or arbitrarily larger m. There is no Egorov assertion at those
locations: only differences of nearby times enter the Gram matrix.

## 2. Finite intervals and an infinite exponentially weighted sum

Let `epsilon_N=O_eta((log N)^(-2))` be the error in (7). Partition
an arbitrary interval of K integer times into blocks of length L_N,
padding its last block if necessary. Nonnegativity gives

$$
\sum_{m=M}^{M+K-1}Q_N(m)
\le(1+\epsilon_N)\left\lceil{K\over L_N}\right\rceil
\quad(M\in\mathbb Z,\ K\ge1).
\tag{8}
$$

Similarly, for every fixed s>0, group all positive times in blocks
starting at `1+jL_N` and bound each weight by its largest value on
the block. The infinite geometric sum converges and gives

$$
\sum_{m\ge1}e^{-2sm/N}Q_N(m)
\le{(1+\epsilon_N)e^{-2s/N}\over1-e^{-2sL_N/N}}.
\tag{9}
$$

Consequently, taking the N limsup first and then eta decreasing to
zero,

$$
\boxed{
\limsup_{N\to\infty\atop N\ {
m odd}}
 {\log N\over N}\sum_{m\ge1}e^{-2sm/N}
 \max_v {|\operatorname{Tr}(T_N(v)^*U_N^m)|^2\over N^2}
\le {P_*\over2s}.
}
\tag{10}
$$

The full infinite tail is included. The scalar trace energy is one
of the terms permitted inside the maximum, so (10) implies the
previous scalar upper bound. Its new content is the time-dependent
maximum over the complete Weyl family.

## 3. All repeats of the bare Pell time

Let

$$
N_r={\lambda^r-\lambda^{-r}\over4\sqrt2},\qquad
V_r=U_{N_r}^{2r},\qquad r\to\infty\ {
m odd}.
$$

The twisted pressure theorem gives, for every fixed
`0<delta<2Delta/log(lambda)`, where `Delta=log(lambda)/2-P_*`,

$$
\varepsilon_r:=\max_v
 {1\over N_r}|\operatorname{Tr}(T_{N_r}(v)^*V_r)|
=O(N_r^{-\delta}).
\tag{11}
$$

Write `q_k=Q_(N_r)(2rk)`. The two-vector version of the argument in
Section 1, with a separately maximizing Weyl index at each of two
consecutive powers of V_r, gives

$$
q_k+q_{k+1}\le1+\varepsilon_r
\quad(k\in\mathbb Z),\qquad q_1=\varepsilon_r^2.
\tag{12}
$$

This conclusion concerns successive maximal Weyl returns even if
their maximizing translations are different. It does not bound q_2
away from one.

For `t=exp(-4sr/N_r)`, separate the first power and group the rest
as even-odd pairs. From `0<=q_k<=1` and (12),

$$
t^{2j}q_{2j}+t^{2j+1}q_{2j+1}
\le t^{2j}(1+\varepsilon_r t).
$$

Thus the exact complete-tail estimate is

$$
\boxed{
\sum_{k\ge1}e^{-4srk/N_r}Q_{N_r}(2rk)
\le t\varepsilon_r^2
       +{t^2(1+\varepsilon_r t)\over1-t^2}.
}
\tag{13}
$$

As `r/N_r->0` and epsilon_r->0, this implies

$$
\boxed{
\limsup_{r\to\infty\atop r\ {
m odd}}
 {r\over N_r}\sum_{k\ge1}e^{-4srk/N_r}
     \max_v {|\operatorname{Tr}(T_{N_r}(v)^*U_{N_r}^{2rk})|^2
                    \over N_r^2}
\le {1\over8s}.
}
\tag{14}
$$

The trivial unitarity bound would give `1/(4s)`. Formula (14)
quantifies a loss of return energy over all repetitions for the
actual family. It neither proves smallness of the second repeat
individually nor makes the complete sum bounded as r grows.

## 4. What has not been proved

These positive-frame bounds use exact unitarity and short time
differences. They do not exploit or estimate the phases of distinct
periodic orbits in the same long-time trace. Their total upper bound
is still of order `N/log N` for the normalized scalar energy, whereas
even a boundedness result relevant to the microscopic pair problem
would require order one. The degree-N determinant cutoff does not
appear in (3)--(14); no assertion is made that it improves them.



---

