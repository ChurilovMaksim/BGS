# Exact fourth-moment reduction

This note records only algebraic identities that are exact over the finite field.

## Pair coordinates

For \(x,y\in\mathbf F_N\setminus\{0,1\}\),
\[
u=x/y,\qquad v=(x-1)/(y-1),\qquad d=x-y.
\]
If \(x\ne y\), then \(u,v\ne1\), \(u\ne v\), and
\[
y=\frac{1-v}{u-v},\qquad
x=\frac{u(1-v)}{u-v},\qquad
d=\frac{(u-1)(v-1)}{v-u}.
\]
If \(x=y\), every one of the \(N-2\) admissible pairs has key \((1,1)\) and \(d=0\).

## Coupled key distribution

A key record has multiplicity \(n_r\). Define
\[
B(t)=\sum_{r,s}n_rn_s
1_H(u_ru_s)1_H(v_rv_s)1_{d_r+d_s=t}.
\]

The ordered coupling classes are diagonal/diagonal, diagonal/off, off/diagonal, and off/off. Inclusion--exclusion on the off/off partner conditions yields
\[
V_{\rm off}
=K^2(N-2)(N-3)-3K(K-1)(N-3)+2(K-1)(K-2),
\]
hence
\[
\sum_tB(t)
=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K.
\]

## Character orthogonality

Let \(S=H^\perp\). For
\[
A_{\chi,\psi}(d)
=\sum_{r:d_r=d}n_r\chi(u_r)\psi(v_r),
\]
orthogonality over \(S\) gives
\[
\sum_{\chi,\psi\in S}(A_{\chi,\psi}*A_{\chi,\psi})(t)=m^2B(t),
\quad m=(N-1)/K.
\]

Equivalently, after the unnormalized additive Fourier transform,
\[
\sum_{\chi,\psi\in S}\widehat A_{\chi,\psi}(\xi)^2
=m^2\widehat B(\xi).
\]

For the twisted Jacobi sums used in the matrix-element model this becomes
\[
\sum_{\chi,\psi\in S}|J(\chi,\psi;q)|^4=m^2\Sigma_4(q),
\quad
\Sigma_4(q)=\widehat B(-q).
\]

## Fourier duality

For \(V=\sum_tB(t)\) and \(Z=B(0)\),
\[
\mathbf E_{q\ne0}\Sigma_4(q)=\frac{NZ-V}{N-1}.
\]
Subtracting the nonzero-\(t\) mean and using finite Fourier orthogonality gives
\[
\operatorname{Var}_{q\ne0}\Sigma_4(q)
=N\operatorname{Var}_{t\ne0}B(t).
\]

No asymptotic estimate enters this identity. The entire M1 fluctuation problem is therefore reduced to an \(L^2\) estimate for one finite-field difference distribution.

## Finite regression anchors

The exact values currently retained in `results/verified/fourth_moment_factorization.json` agree with an independent reconstruction performed during the repository rebuild:

| \(N\) | \(K\) | \(V_4\) | \(B(0)\) | \(\|B\|_2^2\) |
|---:|---:|---:|---:|---:|
| 23 | 11 | 48621 | 2609 | 103156981 |
| 53 | 13 | 423879 | 12063 | 3410502105 |
| 199 | 11 | 4681821 | 96641 | 115589503389 |
| 461 | 23 | 111147915 | 641799 | 26960554630421 |

The finite anchors support the implementation; they are not a proof of an asymptotic theorem.
