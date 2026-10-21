> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/counter_audit_character_collision.md`. Embedded SHA256: `a7178db036314745a95efe79c0d48ba64a77b05ec41259a3d5b1d715141202f4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit of the relative-character collision identity

21 October 2026. Audited source: root_character_collision_and_routing_audit.md, SHA-256 05bc62f64f2e7b51106c04f1f6b458dd77aa11bbff7c8fda8bb64fb868bc6bb4. This audit concerns its new Sections 2--3. Its separately audited analytic echo estimate is the only analytic input.

Let $D=d^2$, let $E=E_N$, and normalize the Hilbert--Schmidt inner product by $N^{-1}$. The mutually orthogonal projections
$$
\mathcal Q_\nu(X)=D^{-1}\sum_{g\in G}\overline{\nu(g)}H_gXH_g^*
$$
sum to the identity on the space of matrices. Since $E$ is unitary, the nonnegative numbers
$$
p_\nu=N^{-1}\|\mathcal Q_\nu(E)\|_{\rm HS}^2
$$
therefore sum to one. The projection identity gives exactly
$$
p_\nu=D^{-1}\sum_g\overline{\nu(g)}e_g,\qquad
e_g=N^{-1}\operatorname{Tr}(E^*H_gEH_g^*).
$$
At the identity $g=0$, $e_0=1$. Consequently
$$
\begin{aligned}
\sum_\nu|p_\nu-D^{-1}|^2
&=D^{-2}\sum_{g,h\ne0}e_g\overline{e_h}
       \sum_\nu\overline{\nu(g)}\nu(h)\\
&=D^{-1}\sum_{g\ne0}|e_g|^2.
\end{aligned}
$$
This derivation checks the normalization directly: precisely one factor $D^{-1}$ remains on the right. Since the $p_\nu$ are real and sum to one, the left side is also $\sum_\nu p_\nu^2-D^{-1}$.

For the nonidentity grid points $z_g=(s/d,-u/d)$, use the supplied echo bound
$$
|e_g|\le C(1+N\operatorname{dist}(z_g,0))^{-1/16}+C N^{-1}.
$$
Squaring it costs only a fixed factor:
$$
|e_g|^2\le C N^{-1/8}\operatorname{dist}(z_g,0)^{-1/8}
          +C N^{-2}.
$$
Choose centered representatives and shells with
$j=\max(|s|,|u|)$. For $j\ge1$, their cardinality is at most $8j$, and their Euclidean torus distance is at least $j/d$. Hence
$$
D^{-1}\sum_{g\ne0}\operatorname{dist}(z_g,0)^{-1/8}
\le C d^{-15/8}\sum_{1\le j\le(d-1)/2}j^{7/8}\le C'.
$$
For $d=1$, the sum is empty. This proves uniformly
$$
0\le\sum_\nu p_\nu^2-d^{-2}\le C N^{-1/8}.
$$

Cauchy--Schwarz gives
$$
\tfrac12\sum_\nu|p_\nu-d^{-2}|
\le\tfrac12 D^{1/2}
\left(\sum_\nu|p_\nu-d^{-2}|^2\right)^{1/2}
\le C dN^{-1/16}.
$$
The reciprocal collision mass obeys
$$
\left(\sum_\nu p_\nu^2\right)^{-1}
\ge(d^{-2}+CN^{-1/8})^{-1}
\ge c\min(d^2,N^{1/8}),
$$
because $x+y\le2\max(x,y)$. Jensen's inequality for the convex function $-\log$, with weights $p_\nu$, gives the stated Shannon-entropy consequence after omitting zero weights.

**Verdict.** The exact normalization, rates $N^{-1/8}$ and $dN^{-1/16}$, and the lower bound $c\min(d^2,N^{1/8})$ are proved as written in the audited source. No temporal independence, stochastic replacement, or control of coherent multi-step sums follows from this argument. The source makes no such claim.
