> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/phase_all_character_signed_trace_removal.md`. Embedded SHA256: `4ed112e52f896bc88e5950710cc038f9e1f3c26afe7dbbdb41e324bd74011564`.
> [Thematic guide](../../topics/arithmetic.md).

# Signed removal of all histories following the arithmetic character permutation

Research continuation, 21 October 2026.

**Status.** The exact trace sector treated here occupies all $N$ dimensions, not one oldspace. Uniform arithmetic-comb escape, together with an elementary count of fixed characters, proves that this entire sector and its cross-term against the remaining trace can be removed from the pair functional at all positive times with an explicit error $O(d^{-\kappa})=o(1)$. No short-time cutoff or logarithmic-time dispersion input is needed. Histories with at least one transition away from the unperturbed character permutation remain uncontrolled. This does not prove $H_{\rm diag}$.

The dimensions covered are the odd $N=d^2m$ with $m\le\sqrt N$, uniformly over such divisors $d$. This statement does not assert that every odd dimension admits such a divisor.

The analytic input is the stronger numerical compression gap in
*arithmetic_comb_rescaled_gap.md*, Sections 1--3, snapshot SHA-256
898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f.
It holds for $N\ge10^{140}$, with $\rho=\sqrt{4095/4096}$, at the original fixed $\tau$. That source records the underlying fourth-difference proof and independent audit. Its current audit gate remains attached to this input. The extension to every character and the full finite-dimensional signed estimate are checked below, rather than inferred from an independence model. The companion Section 4 independently obtains the same fixed-character improvement.

## 1. The complete orthogonal character decomposition

Let $N=d^2m$ be odd and put $D_0=N/d=dm$.
The operators

$$
T_G(u,v):=T_N(D_0u,D_0v),\qquad (u,v)\in G:=(\mathbb Z/d\mathbb Z)^2
$$

form a unitary representation of the finite abelian group $G$.
Indeed the Weyl cocycle is trivial on this subgroup: every symplectic product of two label vectors is divisible by
$D_0^2=Nm$, hence by $N$, also after multiplication by the modular inverse of two.
The order-$d$ relations follow from $dD_0=N$.

For every character $\chi:G\to\mathbb S^1$, define

$$
P_\chi=\frac1{d^2}\sum_{g\in G}\overline{\chi(g)}T_G(g).
\tag{1}
$$

Finite character orthogonality gives

$$
P_\chi^*=P_\chi,\qquad
P_\chi P_\psi=\mathbf1_{\chi=\psi}P_\chi,\qquad
\sum_{\chi\in\widehat G}P_\chi=I.
\tag{2}
$$

The trace of a nonidentity Weyl operator is zero, so

$$
\operatorname{rank}P_\chi=\operatorname{Tr}P_\chi=N/d^2=m.
\tag{3}
$$

In particular all $d^2$ character spaces occur and their total dimension is $N$. The trivial-character space is the canonical oldspace used in the companion manuscript.

## 2. The escape estimate is uniform in the character

Write $E_N=e^{i\tau N A_N}$, and use the ordinary symbol $a$ and
$g=\partial_q^4a$ from the arithmetic manuscript. Set

$$
\sigma_g^2=\sum_{k,l}|\widehat g(k,l)|^2.
$$

For every character, the same exact Fourier compression identity gives

$$
P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma_g^2P_\chi
\qquad(d>18).
\tag{4}
$$

Here is the check. Conjugation of $W_N(k,l)=(-1)^{kl}T_N(l,k)$ by $T_G(u,v)$ multiplies it by the character determined by $(k,l)\pmod d$.
Thus $P_\chi W_N(k,l)P_\chi=0$ unless both $d\mid k$ and $d\mid l$.
The differences of two frequencies of $g$ satisfy
$|k-k'|\le18$, $|l-l'|\le2$.
For $d>18$, only the zero difference survives in $Q_N(g)^*Q_N(g)$; its coefficient is $\sigma_g^2$. This proves (4), including all Weyl phases.

The translation used in the fourth-difference proof belongs to $G$.
It therefore acts on $\operatorname{Ran}P_\chi$ as a scalar
$r_\chi\in\mathbb S^1$, which need not be one.
For a unit vector $v\in\operatorname{Ran}P_\chi$, put

$$
\epsilon=\|(I-P_\chi)E_Nv\|,\qquad B=E_N^*RE_N.
$$

Since $R=r_\chi I$ on this character space,

$$
\|(B-r_\chi I)v\|
=\|(R-r_\chi I)E_Nv\|\le2\epsilon,
\tag{5}
$$

and the analogous bound holds for
$B^{-1}-\overline{r_\chi}I$.
In the fixed nested commutator word $C_3$ from the arithmetic proof, every scalar phase cancels. Its eight occurrences of $B$ or $B^{-1}$, together with the exact scalar action of $R^{\pm1}$, therefore give the same telescoping estimate

$$
\|(C_3-I)v\|\le16\epsilon.
\tag{6}
$$

The operator comparison for $C_3$ is uniform on the whole finite Hilbert space and does not depend on $\chi$. The rescaled auxiliary translation in the companion Sections 1--3 yields
$\|(C_3-I)v\|>13/50$ for every such vector. It uses (4) and retains the full leading exponential; the original kick is unchanged. Combining this comparison with (6) gives the uniform numerical conclusion

$$
\boxed{\displaystyle
\|(I-P_\chi)E_Nv\|>13/800>1/64,\qquad
\|P_\chi E_NP_\chi\|\le\rho,
\quad
\rho=\sqrt{4095/4096}<1.}
\tag{7}
$$

The threshold $N\ge10^{140}$ and $\rho$ are uniform in $d,m,\chi$ in the stated range. This is the required extension from the trivial character to the complete orthogonal decomposition.

## 3. The metaplectic factor permutes those spaces exactly

For the matrix in the question, a direct kernel calculation gives

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b).
\tag{8}
$$

For completeness, the left-hand kernel phase, after subtracting the common quadratic phase of $M_N$, has linear coefficients
$b-3a/4$ in $x$, $a/4$ in $y$, and constant
$-3a^2/8+ab/2$, with all fractions interpreted modulo odd $N$.
On the right, putting $A=3a-4b$, $B=-2a+3b$, these coefficients are
$-A/4$, $3A/4+B$, and $-3A^2/8-AB/2$.
Substitution makes all three equal. This proves (8) with no unspecified scalar.

Let

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},
\qquad
\mathsf S\chi=\chi\circ L
$$

on $G$.
Since $L$ is invertible modulo $d$, $\mathsf S$ is a permutation of the characters.
Equation (8) gives

$$
M_NP_\chi=P_{\mathsf S\chi}M_N.
\tag{9}
$$

Define the following concrete operator on the full $N$-dimensional space:

$$
K_N=\sum_{\chi\in\widehat G}P_{\mathsf S\chi}U_NP_\chi
=\left(\sum_{\psi\in\widehat G}P_\psi E_NP_\psi\right)M_N.
\tag{10}
$$

The second identity uses (9) and the fact that $\mathsf S$ permutes all characters.
The parenthesized operator is block diagonal in the orthogonal decomposition (2).
By (7),

$$
\boxed{\displaystyle
\|K_N\|\le\rho<1,\qquad
|c_n|:=|\operatorname{Tr}K_N^n|\le N\rho^n.}
\tag{11}
$$

No statement of contractivity is made about $U_N$ or $\operatorname{Ad}_{U_N}$, which remain unitary.

## 4. The finite trace-word partition identifies the entire removed sector

Write $p_n=\operatorname{Tr}U_N^n$.
Inserting (2) between all $n$ factors gives exactly

$$
p_n=
\sum_{\chi_0,\ldots,\chi_{n-1}}
\operatorname{Tr}
\left(
P_{\chi_0}U_NP_{\chi_{n-1}}U_N\cdots
 P_{\chi_1}U_NP_{\chi_0}
\right).
\tag{12}
$$

In cyclic order, these terms describe the transitions
$\chi_j\to\chi_{j+1}$, with $\chi_n=\chi_0$.
The subset satisfying

$$
\chi_{j+1}=\mathsf S\chi_j
\qquad\text{at every step}
\tag{13}
$$

sums exactly to $\operatorname{Tr}K_N^n=c_n$, by multiplying the blocks in (10).
If $\mathsf S^n\chi_0\ne\chi_0$, the corresponding product has zero trace, as also follows from the orthogonality of its initial and final character spaces.

Therefore

$$
q_n:=p_n-c_n
\tag{14}
$$

is exactly the sum of all terms in (12) with at least one transition violating (13).
This is a deterministic finite matrix identity, not a stochastic path expansion.

## 5. Counting the closed character histories

Let

$$
F_n(d)=\#\{\chi\in\widehat G:\mathsf S^n\chi=\chi\}.
$$

Only these initial character spaces contribute to the trace of $K_N^n$. Each has dimension $m=N/d^2$, and every block of $K_N^n$ has norm at most $\rho^n$. Consequently

$$
|c_n|\le \frac{N}{d^2}F_n(d)\rho^n.
\tag{15}
$$

Identify a character with $v\in(\mathbb Z/d\mathbb Z)^2$ through
$\chi_v(u)=e_d(v\cdot u)$. Then

$$
F_n(d)=\#\ker((L^T)^n-I\pmod d).
\tag{16}
$$

The following elementary lattice bound works for every modulus, including composite $d$:

$$
\#\ker(A\pmod d)\le|\det A|
\quad\text{for every nonsingular integer matrix }A\in M_2(\mathbb Z).
\tag{17}
$$

To prove it, choose an integer representative $v$ of an element of the kernel, so $Av=dw$ for an integer vector $w$, and map

$$
[v]\longmapsto[w]\in\mathbb Z^2/A\mathbb Z^2.
$$

Changing $v$ by $dz$ changes $w$ by $Az$, so the map is well defined. If its value is zero, then $w=Az$, and nonsingularity gives $v=dz$; hence the map is injective. Finally $\mathbb Z^2/A\mathbb Z^2$ has order $|\det A|$. For a direct two-dimensional verification of this last fact, use Bezout row operations of determinant one to put the first column of $A$ in the form $(g,0)^T$, $g>0$. The resulting upper triangular matrix has diagonal entries $g,c\ne0$; successively reducing the second and first coordinates gives exactly $|gc|=|\det A|$ quotient classes. This proves (17).

For
$\lambda=3+2\sqrt2$, the eigenvalues of $L$ are $\lambda,\lambda^{-1}$, so

$$
|\det(L^n-I)|=\lambda^n+\lambda^{-n}-2<\lambda^n
\qquad(n\ge1).
$$

Combining (15)--(17) with the trivial count $F_n(d)\le d^2$ proves

$$
\boxed{\displaystyle
\frac{|c_n|}{N}\le
\rho^n\min\left\{1,\frac{\lambda^n}{d^2}\right\}.}
\tag{18}
$$

This fixed-character bound is the point that permits removal at all positive times.

## 6. The full signed pair correction and an explicit rate

For any bounded $w:[0,\infty)\to\mathbb C$, define the termwise correction

$$
\mathcal R_{N,w}
=\frac1{N^2}\sum_{n\ge1}w(n/N)
 \left(|p_n|^2-|p_n-c_n|^2\right).
\tag{19}
$$

For an arbitrary bounded nondecaying weight, this difference series is absolutely convergent, although the two individual series need not be. For compactly supported or exponentially decaying weights, it equals their ordinary difference. Every bound below is also uniform under finite upper time cutoffs.

Put $a_n=\rho^n\min\{1,\lambda^n/d^2\}\le1$.
Since $|p_n|\le N$, (18) and the identity
$|p|^2-|p-c|^2=2\operatorname{Re}(p\overline c)-|c|^2$ give

$$
\frac1{N^2}
\left||p_n|^2-|p_n-c_n|^2\right|
\le2a_n+a_n^2\le3a_n.
\tag{20}
$$

Thus

$$
|\mathcal R_{N,w}|
\le3\|w\|_\infty
\sum_{n\ge1}\rho^n
 \min\left\{1,\frac{\lambda^n}{d^2}\right\}.
\tag{21}
$$

Already dominated convergence proves that (21) tends to zero: $d\ge N^{1/4}\to\infty$, each fixed summand tends to zero, and $\sum\rho^n<\infty$.

There is also an explicit power bound. Here $\rho=\sqrt{4095/4096}>1/2$, so $\lambda\rho>1$. Define

$$
\kappa=-\frac{2\log\rho}{\log\lambda}>0,\qquad
J=\left\lfloor\frac{2\log d}{\log\lambda}\right\rfloor.
$$

Splitting the positive sum in (21) at $J$ gives

$$
\begin{aligned}
\sum_{n\ge1}\rho^n\min\{1,\lambda^n/d^2\}
&\le \frac1{d^2}\sum_{n=1}^{J}(\lambda\rho)^n
       +\sum_{n>J}\rho^n\\
&\le \rho^J\left[
 \frac{\lambda\rho}{\lambda\rho-1}
 +\frac{\rho}{1-\rho}
 \right]\\
&\le \rho^{-1}d^{-\kappa}
 \left[
 \frac{\lambda\rho}{\lambda\rho-1}
 +\frac{\rho}{1-\rho}
 \right].
\end{aligned}
\tag{22}
$$

Therefore

$$
\boxed{\displaystyle
|\mathcal R_{N,w}|
\le
3\|w\|_\infty\,\rho^{-1}
\left[
 \frac{\lambda\rho}{\lambda\rho-1}
 +\frac{\rho}{1-\rho}
\right]d^{-\kappa}
=O_{\tau,a,w}(N^{-\kappa/4}).}
\tag{23}
$$

All constants and $\kappa$ are fixed, uniformly over the allowed divisors and over weights with a fixed supremum bound. Here
$\kappa=-\log(4095/4096)/\log(3+2\sqrt2)>0$.
The estimate removes the entire sector and its cross-term; it is not only a bound on the self-pair sum $\sum|c_n|^2$.

## 7. Meaning for the original pair functional

For any admissible $b$,

$$
M_{2,N}^U(b)
=\frac{\widehat b(0)^2}{2}\left(1-\frac1N\right)
 +\frac1{N^2}\sum_{n\ge1}
 |\widehat b(n/N)|^2(|p_n|^2-N).
\tag{24}
$$

Replace $p_n$ in the last sum by $q_n=p_n-c_n$, keeping every other term unchanged.
Equation (23) says that the resulting algebraic functional differs from the original factorial moment by $O(d^{-\kappa})=o(1)$.
It removes the entire class (13) at all positive times, including its cross-term against all other words in (12).
The same holds for the exponential pair weight in the question.

The replacement is not asserted to be the spectrum or factorial moment of another unitary matrix.
Most importantly, the remaining traces are the mixed-transition sums (14). No estimate showing CUE behavior for those sums is supplied here.
The fourth-difference escape gap does not turn them into a contractive evolution, and the fixed-character count does not estimate their coherent sum at times of order $N$.
Thus (23) is an actual signed estimate for a complete full-dimensional trace sector, while the original first pair discrepancy and all higher required orders remain unresolved.

