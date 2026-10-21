> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_growing_routing_families.md`. Embedded SHA256: `e89394ca90e1089f9b6c090d24738fd4084307985a89606f8f55aac22b42a120`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit: grouped routing families, Parseval, and closure

21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

Frozen source: `counter_growing_routing_families.md`, SHA-256
`4a78ed247faa8791b34f85b0ee69a6696ac8f9578b7e6d836bf9965f11e30555`.
The complete source was read, its hash checked, and no source was modified.

**Verdict: Sections 1--6 are proved as written, under the exactly stated
inputs (0.1)--(0.3).** The application in Section 3 uses the previously
proved uniform all-pairs compression gap and relative-component
Hilbert--Schmidt bound for the stated divisor range. The limitation of the
conclusion to selected, grouped routes is essential and is correctly stated.

## 1. Selected transitions and individual sparse sums

The projection $\mathcal Q_\nu(E)$ consists exactly of the blocks
$P_{\nu\chi}EP_\chi$. The input blocks are orthogonal, and multiplication
by $\nu$ permutes the output character spaces. Its operator norm is
therefore the maximum norm of one such block, bounded by $\rho=1-g$.
Multiplication by the unitary $M_N$ preserves both its operator and
Hilbert--Schmidt norms. Consequently the three bounds in (1.3) follow from
(0.3); in particular $\|R_{r,j}\|\le1+\rho=2-g$.

The exact metaplectic permutation implies that $K_{r,j}$ maps the character
$\chi$ to $\nu_{r,j}\mathsf S\chi$, with no ambiguity about the order
of the two factors. Since $R_{r,j}$ is the difference between the full
operator and this selected block permutation, its character expansion
contains precisely the other transitions. Thus a sparse term with a specified
set of R positions has the stated interpretation as deviations from the
route, and time dependence of the chosen relative character is harmless.

For $0<g\le1/2$, the source's
$z=g/(2(2-g))$ lies in $(0,1/6]$. Also
$$
0<\delta\le\frac{\log(4/3)}{2\log6}<1.
$$
Thus a retained word of length $n\ge1$ always has a K factor. Putting
one such factor in Hilbert--Schmidt norm and all others in operator norm
gives (1.6), independently of the locations of the factors. The inequality
$\|AXB\|_{\rm HS}\le\|A\|\|X\|_{\rm HS}\|B\|$
justifies its use even in a noncommuting word.

For integers $a\le\delta n$, $z^{-a}\le z^{-\delta n}$. Also
$\rho+(2-g)z=1-g/2$ and
$z^{-\delta}= (1-g/2)^{-1/2}$, by the actual definition of $\delta$.
This proves the binomial bound (1.7) without ignoring a floor or introducing
an asymptotic estimate. Its two norm consequences (1.8) follow, with the
necessary factor $\rho^{-1}$ in the Hilbert--Schmidt version.

## 2. Grouping and the square correction

For disjoint starting groups, the compressed matrices
$P_jS_{n,j}P_j$ have mutually orthogonal input and output spaces.
Therefore their direct sum has operator norm at most $\eta^n$, and the
squared Hilbert--Schmidt norm is the sum of their squared norms. Each
compression decreases Hilbert--Schmidt norm, giving exactly the factor J
in (2.1), hence $\sqrt J$ in normalized trace.

Although $P_j$ may contain many characters, the trace of its compression
equals
$\sum_{\chi\in A_j}\operatorname{Tr}(P_\chi S_{n,j}P_\chi)$.
The blocks between two distinct characters have zero trace. Thus selected
closed histories are counted once, by their starting character, including
when the groups form a full partition. This is not a restriction to the
rank of one character block.

For $p_n=\operatorname{Tr}U_N^n$ and $s_n=\operatorname{Tr}T_n$,
$|p_n|/N\le1$ and $|s_n|/N\le\eta^n\le1$. Expanding the squared
modulus therefore gives
$$
N^{-2}\big||p_n|^2-|p_n-s_n|^2\big|\le3|s_n|/N.
$$
This includes the cross term with the retained trace. Since
$\rho^{-1}\le2$, $1-\sqrt{1-g/2}\ge g/4$, and
$\sum_{n\ge1}\eta^n\le(1-\eta)^{-1}$, summation yields precisely
$$
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
 \big||p_n|^2-|p_n-s_n|^2\big|
\le24W\frac{\sqrt J\,\overline\sigma}{g}.
$$
This proves absolute convergence of the difference series for bounded
weights. It does not assert convergence of either separate unweighted
squared-trace series.

The proof uses the same constants for every chosen partition and route.
It therefore remains valid if the choice changes with n, as the source
claims. It does not allow counting several different routes for the same
starting character in the same trace without an additional estimate.

## 3. Growth condition and application

The condition
$J=o(g^2\min(d^2,N^{1/16}))$ implies separately
$\sqrt J/(gd)\to0$ and
$\sqrt J/(gN^{1/32})\to0$, so it is sufficient for (3.1).
For the proposed choice $J=\lfloor\min(d,N^{1/32})\rfloor$,
$$
\sqrt J\,d^{-1}\le d^{-1/2},\qquad
\sqrt J\,N^{-1/32}\le N^{-1/64}.
$$
In the stated divisor range, $\log d\ge C_2(\log N)^{2/3}$, whereas
$\log(g^{-1})=O((\log N)^{1/3}\log\log N)=o((\log N)^{2/3})$.
Both terms in (3.6) tend to zero. There are enough character blocks to
form the proposed number of groups, since $J\le d\le d^2=q$.
The choice $J=d^2$ is correctly not justified by this bound: its
$d^{-1}$ term would leave $1/g$.

## 4. Parseval identity and exact number of potentially closed routes

The matrices $U_g=H_gEH_g^*M$ are unitary, and the orthogonal character
decomposition gives exactly
$U_g=\sum_\nu\nu(g)K_\nu$. Expanding a product with independent
parameters $g_1,\ldots,g_n$, then applying character orthogonality in
each parameter, proves the vector-valued Parseval identity
$$
\sum_{\boldsymbol\nu}\|B_{\boldsymbol\nu}\|_{\rm HS}^2=N.
$$
Taking trace before applying the same calculation proves (4.5).
These are exact algebraic identities, with no replacement of the original
statistic by a random model.

In additive notation, composition of the selected transitions gives
$$
\chi\longmapsto\mathsf S^n\chi+
 \sum_{j=1}^n\mathsf S^{n-j}\nu_j.
$$
The equation for a fixed starting character therefore has either zero
solutions or a coset of $\ker(\mathsf S^n-I)$, hence exactly $F_n$
solutions in the latter case. Only the corresponding diagonal character
blocks can contribute to trace. Their total rank is $mF_n$, and the
finite-dimensional trace inequality gives
$$
|c_{\boldsymbol\nu}|^2\le mF_n\|B_{\boldsymbol\nu}\|_{\rm HS}^2.
$$
Summing and using $N=mq$ yields $N^2F_n/q$, including the correct
normalization in (4.9).

The map from the $q^n$ routes to the displacement is surjective and
has fibers of size $q^{n-1}$: for every choice of the first $n-1$
relative characters and a desired displacement, the last one is unique.
The image of $I-\mathsf S^n$ has size $q/F_n$, by the kernel-image
formula on a finite group. Exactly $q^n/F_n$ routes therefore pass the
closure condition. They need not have nonzero trace; cancellation inside
a permitted route is still possible, as the source explicitly states.

Cauchy--Schwarz for a collection of L routes gives
$N^{-1}|\sum c|\le\sqrt{LF_n/q}$. For the complete permitted set,
this becomes $q^{(n-1)/2}=d^{n-1}$. All occurrences of q and F_n in
the source are thus correct. No field structure or prime-modulus argument
has been used.

## 5. Both stated limitations are verified

For the first example, $B_j=aP_j$ with rank $N/J$ has operator norm
a and normalized Hilbert--Schmidt norm $a/\sqrt J$, whereas the grouped
sum equals $aI$. Its normalized trace is a. It proves the necessity of
a $\sqrt J$ loss under those individual norm and block assumptions.
It does not assert that these example matrices arise from the original kick.

For the second example, the Fourier normalization $1/d$ is correct in
dimension $d^2$. Summing its intermediate character yields
$\mathcal F_G^2\psi(x)=\psi(-x)$, so $\mathcal F_G^4=I$.
Right multiplication by a unitary monomial matrix preserves entry
magnitudes. Thus $\widetilde E=\mathcal F_GM^{-1}$ has every entry of
modulus $1/d$. Each $\mathcal Q_\nu(\widetilde E)$ has one such
entry per row and column, and its normalized squared Hilbert--Schmidt norm
is $1/d^2$. Relative components are Hilbert--Schmidt orthogonal.
Nevertheless $\widetilde U=\mathcal F_G$ has trace N at time four.
This disproves the proposed norm-only inference in exactly the scope stated;
it does not give a counterexample for $e^{i\tau N A_N}$.

## 6. First remaining step

No gap was found in these finite-dimensional claims. The missing step for
the original spectral problem remains the signed control of the unrestricted
route family and its higher-order counterparts. The source neither assumes
that control nor identifies the auxiliary Fourier example with the original
family.
