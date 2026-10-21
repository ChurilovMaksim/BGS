> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_complementary_pair_remainder.md`. Embedded SHA256: `8036002a27161239c15cdf22ae0393a5b9316fcbab8b6b3ffef6c6235c0e7b09`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: complementary raw pair remainder in main §9.1

21 October 2026. Auditor: occupation/cross-phase branch.

This note saves the already completed verification of the complementary-pair formulation in §9.1 of round6_main_report.md. It introduces no further research claim and does not modify the frozen generic-phase audit.

## 1. Exact partition of actual rooted pairs

For the original $U_N$, write
$$
 a_N(x)=\prod_{i\bmod n}(U_N)_{x_i x_{i+1}},
 \qquad P_N=|U_N|^{\circ2}.
$$
Let $T_{n,N}^{[48]}$ be the complete raw class with at least one literal agreement, at least one disagreement, and every cyclic disagreement run of length at most 48.

Let $R_{n,N}^{\rm bad}$ be the sum of $a_N(x)\overline{a_N(y)}$ over actual ordered rooted pairs $x\ne y$ which either have no literal agreement or have a disagreement run of length at least 49.

These classes and the all-agreement class $x=y$ form an exact disjoint partition. In particular, a pair with no agreement belongs to the bad class even if $n\le48$. The all-agreement contribution is
$$
 \sum_x|a_N(x)|^2=\operatorname{Tr}P_N^n.
$$
Therefore, for every positive integer $n$,
$$
 \boxed{
 |\operatorname{Tr}U_N^n|^2
 =\operatorname{Tr}P_N^n+T_{n,N}^{[48]}+R_{n,N}^{\rm bad}.
 }
 \tag{A1}
$$
There is no division by a period, marking multiplicity, or occupation restriction.

The raw-class bound used below is the independently audited theorem:
$$
 \sum_{n\ge1}|T_{n,N}^{[48]}|\le K_{49},
 \qquad K_{49}=1500000000(4b_{49}-1).
 \tag{A2}
$$
Its stronger exponential version is proved in r6_dense_bounded_runs_raw49.md, SHA256 631663c9639c286510125df4806b833d4cfb8344a7a9d0fc36d6c647e83bc9e8, and audited in r6_occupation_audit_bounded_runs_raw49.md, SHA256 251ad2ac4e4bcc96a6b79b30cd3a1c56f222f4390f5aaca2d94522fba55db7a1.

## 2. The constant $56/3$

For all sufficiently large odd $N$, the established original-family estimates give
$$
 \max_{a,b}(P_N)_{ab}\le9/N,\qquad
 E_N=P_N-J_N,\qquad \|E_N\|\le1/4.
$$
Double stochasticity implies
$$
 P_N^n=J_N+E_N^n,\qquad
 \|E_N\|_{\rm HS}^2=\sum_{a,b}(P_N)_{ab}^2-1\le8.
$$
Also $0\le\operatorname{Tr}P_N\le9$, so
$$
 |\operatorname{Tr}E_N|\le8.
$$
For $n\ge2$, the Hilbert--Schmidt trace and ideal inequalities give
$$
 |\operatorname{Tr}E_N^n|
 \le\|E_N\|_{\rm HS}^2\|E_N\|^{n-2}
 \le8(1/4)^{n-2}.
$$
This does not require $E_N$ to be normal. Consequently
$$
 \boxed{
 \sum_{n\ge1}|\operatorname{Tr}P_N^n-1|
 \le8+\frac8{1-1/4}=\frac{56}{3}.
 }
 \tag{A3}
$$

## 3. The finite-band error

For the fixed admissible test $b_*$ in main §9, put
$$
 w(t)=|\widehat b_*(t)|^2,\qquad W=\|w\|_\infty.
$$
Its Fourier support is $[-2,2]$, and the exact pair formula is
$$
 \Delta_{2,N}(b_*)=
 \frac1{N^2}\sum_{1\le n<2N}w(n/N)
 \left(|\operatorname{Tr}U_N^n|^2-\min(n,N)\right).
$$
Define
$$
 B_N=\frac1{N^2}\sum_{1\le n<2N}w(n/N)R_{n,N}^{\rm bad},
 \qquad
 C_N=\frac1{N^2}\sum_{1\le n<2N}w(n/N)\min(n,N).
$$
Substitution of (A1) gives the exact difference
$$
 \Delta_{2,N}(b_*)-(B_N-C_N)
 =\frac1{N^2}\sum_{1\le n<2N}w(n/N)
     \left(\operatorname{Tr}P_N^n+T_{n,N}^{[48]}\right).
$$
The constant part of $\operatorname{Tr}P_N^n$ contributes at most $2W/N$, since there are $2N-1$ terms. Equations (A2)--(A3) bound the remaining contributions. Thus
$$
 \boxed{
 |\Delta_{2,N}(b_*)-(B_N-C_N)|
 \le\frac{2W}{N}
      +\frac{(K_{49}+56/3)W}{N^2}.
 }
 \tag{A4}
$$
All estimates apply along every sufficiently large odd $N$, with the prescribed fixed kick.

## 4. Riemann limit and exact remaining assertion

Since $\min(n,N)=N\min(n/N,1)$,
$$
 C_N=\frac1N\sum_{1\le n<2N}
       w(n/N)\min(n/N,1).
$$
The function $w(t)\min(t,1)$ is continuous on $[0,2]$. Therefore its Riemann sums converge:
$$
 C_N\longrightarrow
 \int_0^2w(t)\min(t,1)\,dt.
$$
Together with (A4), this proves the exact equivalence
$$
 \boxed{
 \Delta_{2,N}(b_*)\longrightarrow0
 \quad\Longleftrightarrow\quad
 \frac1{N^2}\sum_{1\le n<2N}w(n/N)R_{n,N}^{\rm bad}
 \longrightarrow\int_0^2w(t)\min(t,1)\,dt.
 }
$$

This is another precise formulation of the remaining open pair estimate. It removes the complete bounded-run raw class $T^{[48]}$, not its unequal-occupation component. No bound on $\Omega^{[48]}$ or on its complementary same-occupation component is assumed or inferred. The unrestricted bad-class limit remains unproved.

