> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_all_odd_endpoint_fiber_identity.md`. Embedded SHA256: `ec36b997ef3a38dd464d468833f78a3934b45bdc57dbc36f54987aa42a649b70`.
> [Thematic guide](../../topics/dephasing.md).

# An all-odd, all-time endpoint-fiber identity for the full Weyl path square

21 October 2026. This addendum removes the invertibility restriction
from the endpoint factorization in
`r8_weyl_full_weight_relative_path_cancellation.md` (frozen SHA256
`038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109`).
That source has already passed an independent full audit.

The result is an exact classification of every endpoint sector.
It remains a refinement of the conjugation-trace identity, and
provides no unproved replacement for the Heisenberg-scale signed
estimate required in the question.

## 1. Notation

All labels are in $\Lambda_N=(\mathbb Z/N\mathbb Z)^2$,
where $N$ is any odd integer. Use exactly the original modular
Weyl convention

$$
W(k,l)=T_N(l,k),\qquad
\omega((k,l),(k',l'))=lk'-kl',\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$

Thus
$W(u)W(v)=e_N(\overline2\omega(u,v))W(u+v)$
and $M_NW(v)M_N^{-1}=W(Sv)$, with $\overline2$
the modular inverse of two. Fix any positive integer $m$, and
write

$$
R=S^m,\qquad K=\ker(R-I),\qquad
g_m(\lambda)=\operatorname{Tr}(W(\lambda)M_N^m).
$$

No invertibility of $R-I$ will be assumed.

## 2. The terminal cross formula without a Gauss-sum assumption

**Theorem 1.** For every $\lambda,\Gamma\in\Lambda_N$,

$$
\boxed{
g_m(\lambda)\overline{g_m(\lambda+\Gamma)}
=\sum_{v:\ (R-I)v=\Gamma}
 e_N\!\left(\omega(\lambda,v+\overline2\Gamma)
                  +\overline2\omega(\Gamma,v)\right).}
\tag{2.1}
$$

An empty fiber means the right side is zero.

**Proof.** For any two $N\times N$ matrices $A,B$,
the trace on matrix space of the linear map $X\mapsto AXB$
equals $\operatorname{Tr}A\operatorname{Tr}B$. In the
matrix-unit basis, its diagonal coefficient at $E_{xy}$ is
$A_{xx}B_{yy}$, proving this formula directly.

Apply it to

$$
\mathcal L(X)=W(\lambda)M_N^m X M_N^{-m}W(-\lambda-\Gamma).
$$

Its trace is the left side of (2.1). On a Weyl basis element,

$$
\mathcal L(W(v))=W(\lambda)W(Rv)W(-\lambda-\Gamma).
$$

A diagonal coefficient in the Weyl basis occurs precisely when
$\lambda+Rv-\lambda-\Gamma=v$, equivalently
$(R-I)v=\Gamma$. Under that condition its Weyl phase is

$$
\begin{split}
\overline2[\omega(\lambda,Rv)
               -\omega(\lambda+Rv,\lambda+\Gamma)]
 &=\overline2[2\omega(\lambda,v)
                  +\omega(\lambda,\Gamma)+\omega(\Gamma,v)]\\
 &=\omega(\lambda,v+\overline2\Gamma)
                   +\overline2\omega(\Gamma,v).
\end{split}
$$

Summing these diagonal coefficients proves (2.1) for every odd
modulus and every time. No estimate or evaluation of a quadratic
Gauss sum is used. $\square$

For $\Gamma=0$, the theorem recovers

$$
|g_m(\lambda)|^2=\sum_{v\in K}e_N(\omega(\lambda,v)).
\tag{2.2}
$$

In particular, if $R-I$ is invertible then the sum in (2.1)
has the unique solution $v=(R-I)^{-1}\Gamma$, and the
nondegenerate quadratic phase law in the companion source follows.

## 3. The full signed background sum in every relative-path sector

Expand the exact original kick, without a Taylor approximation,
as

$$
E_N=e^{i\tau NA_N}=\sum_{\eta\in\Lambda_N}d(\eta)W(\eta),
\qquad \tau=10^{-80}.
$$

For a background path $\eta$ and a fixed relative path
$\delta$, retain the notation

$$
\begin{gathered}
x_j=S^j\eta_j,\quad a_j=S^j\delta_j,\quad
A_{<j}=\sum_{i<j}a_i,\quad\Gamma=\sum_ja_j,\quad
\lambda=\sum_jx_j,\\
\mathcal A(\eta)=\sum_{i<j}\omega(x_i,x_j),\qquad
\mathcal A(\delta)=\sum_{i<j}\omega(a_i,a_j).
\end{gathered}
$$

Let $\mathcal T_m(\delta)$ denote the full background sum
in the trace square:

$$
\begin{split}
\mathcal T_m(\delta)=\sum_\eta
&\left[\prod_jd(\eta_j)\overline{d(\eta_j+\delta_j)}\right]
e_N\!\left(-\overline2[
     \mathcal A(\eta+\delta)-\mathcal A(\eta)]\right)\\
&\quad\cdot g_m(\lambda)\overline{g_m(\lambda+\Gamma)}.
\end{split}
\tag{3.1}
$$

This is a finite sum for each $N,m$, regardless of their
relative size. Also define the exact Weyl-adjoint matrix

$$
C^E_{u,v}=\frac1N\operatorname{Tr}(W(u)^*E_NW(v)E_N^*).
$$

**Theorem 2.** For each fixed relative path $\delta$,

$$
\boxed{
\mathcal T_m(\delta)=
\sum_{v_0:\ (R-I)v_0=\Gamma}
        \prod_{j=0}^{m-1}C^E_{w_j,Sw_{j+1}},
\qquad
w_j=S^{-j}(A_{<j}+v_0),\quad w_m=w_0=v_0.}
\tag{3.2}
$$

The indicated $w_m$ equals $w_0$ because
$S^{-m}(\Gamma+v_0)=v_0$ on the specified fiber.

**Proof.** Use the exact area expansion

$$
\mathcal A(\eta+\delta)-\mathcal A(\eta)
=\mathcal A(\delta)+\sum_j\omega(2A_{<j}+a_j-\Gamma,x_j).
\tag{3.3}
$$

It is obtained by expanding the pairs and collecting the terms
containing each $x_j$, as proved in the companion source.
Insert (2.1) into (3.1), and fix one $v_0$ in its fiber.
The full phase independent of the background is

$$
-\overline2\mathcal A(\delta)
                    +\overline2\omega(\Gamma,v_0).
\tag{3.4}
$$

Combining the linear background phase from (3.3) with that from
(2.1) gives, at site $j$, exactly

$$
\omega(x_j,A_{<j}+v_0+\overline2a_j)
       =\omega(\eta_j,w_j+\overline2\delta_j).
$$

Thus the background sum factorizes into the local ambiguity sums

$$
F_d(\delta_j,w_j+\overline2\delta_j),\quad
F_d(\delta,z)=\sum_\eta d(\eta)\overline{d(\eta+\delta)}
                                          e_N(\omega(\eta,z)).
$$

The direct Weyl multiplication identity established in the
companion source, and obtained again by multiplying
$W(\eta)W(w_j+\delta_j)W(-\eta-\delta_j)$, is

$$
F_d(\delta_j,w_j+\overline2\delta_j)
 =e_N(\overline2\omega(w_j,\delta_j))
                              C^E_{w_j,w_j+\delta_j}.
\tag{3.5}
$$

Here $w_j+\delta_j=Sw_{j+1}$. The remaining local scalar
phases satisfy

$$
\begin{split}
\sum_j\omega(w_j,\delta_j)
 &=\sum_j\omega(A_{<j}+v_0,a_j)\\
 &=\mathcal A(\delta)+\omega(v_0,\Gamma)\\
 &=\mathcal A(\delta)-\omega(\Gamma,v_0).
\end{split}
\tag{3.6}
$$

Their contribution in (3.5) cancels (3.4) exactly. The surviving
factors give (3.2), after summation over the finite fiber.
$\square$

Every nonzero closed relative path $\Gamma=0$ has a
vanishing contribution from the fiber element $v_0=0$.
Indeed its corresponding product in (3.2) starts at the identity
Weyl label. Exact conjugation has
$C^E_{0,u}=C^E_{u,0}=\mathbf1_{u=0}$, so its first
nonzero relative increment forces a zero factor. For singular
$R-I$, the terms from $v_0\in K\setminus\{0\}$
remain; they are not declared zero by this argument.

## 4. The complete endpoint-fiber classification

Let $C^U$ be the Weyl matrix of conjugation by
$U_N=E_NM_N$, so $C^U_{u,v}=C^E_{u,Sv}$.
Define the endpoint sector

$$
\mathcal S_m(\Gamma)
 =\sum_{\delta:\ \sum_jS^j\delta_j=\Gamma}\mathcal T_m(\delta).
$$

The change of variables in Theorem 2 is bijective for each choice
of $v_0$ in the fiber: its inverse is
$\delta_j=Sw_{j+1}-w_j$, and its endpoint constraint follows
by telescoping. Therefore

$$
\boxed{
\mathcal S_m(\Gamma)
   =\sum_{v:\ (S^m-I)v=\Gamma}((C^U)^m)_{v,v}
\qquad\text{for every odd }N\text{ and every }m\ge1.}
\tag{4.1}
$$

This proves all of the following exact statements.

- If $\Gamma\notin\operatorname{im}(S^m-I)$, its
  endpoint sector is zero. Indeed its terminal product in (2.1)
  is identically zero before any background sum.
- Every nonempty fiber has cardinality $|K|$, and hence
  $|\mathcal S_m(\Gamma)|\le|K|$ by unitarity of
  $C^U$. This is an estimate of the fully signed sector,
  but contains no asymptotic decay.
- The endpoint-preserving sector is exactly
  $\mathcal S_m(0)=\sum_{v\in K}((C^U)^m)_{v,v}$.
  It equals $1$ when $K=\{0\}$; in general its
  additional fixed-label terms must remain.
- Summing all fibers recovers
  $\sum_\Gamma\mathcal S_m(\Gamma)
   =\operatorname{Tr}((C^U)^m)=|\operatorname{Tr}U_N^m|^2$.

The fixed-label sum in the third item is real and nonnegative.
This has a direct positive representation. Write

$$
L_m=E_0E_1\cdots E_{m-1}=U_N^mM_N^{-m}
          =\sum_\lambda v_m(\lambda)W(\lambda).
$$

The equal-endpoint part of the original trace square is

$$
\mathcal S_m(0)=\sum_\lambda|v_m(\lambda)|^2|g_m(\lambda)|^2.
\tag{4.2}
$$

By finite-character orthogonality in (2.2), this is

$$
\mathcal S_m(0)=|K|\sum_{\lambda\in K^{\perp_\omega}}
                                      |v_m(\lambda)|^2,
\qquad
K^{\perp_\omega}=\{\lambda:\omega(\lambda,v)=0\ (\bmod N)
                                         \ \forall v\in K\}.
\tag{4.3}
$$

For the character orthogonality used here: a nontrivial character
on a finite subgroup has sum zero by translating the sum by an
element on which the character is not one; a trivial character
has sum $|K|$. Thus (4.3) requires no theorem about the
classification of submodules over a composite ring.

Equivalently, the finite average

$$
\mathsf P_K(B)=\frac1{|K|}\sum_{v\in K}W(v)^*BW(v)
$$

is the orthogonal Weyl projection retaining precisely the labels
in $K^{\perp_\omega}$. In normalized Hilbert--Schmidt norm,

$$
\boxed{\mathcal S_m(0)=|K|\,\|\mathsf P_K(L_m)\|_{2,N}^2,
\qquad\|B\|_{2,N}^2=\frac1N\operatorname{Tr}(B^*B).}
\tag{4.4}
$$

Thus $0\le\mathcal S_m(0)\le|K|$, with no presumption
that it equals $|K|$. At the opposite extreme $R=I$,
all endpoint sectors except $\Gamma=0$ vanish, and (4.1)
assigns the entire trace square to that one sector. This correctly
retains metaplectic recurrence times rather than extending the
nondegenerate value $1$ to them.

## 5. Exact limit of this advance

The identities establish the endpoint-sector resummation with all
modular degeneracies included. They do not supply the signed
Heisenberg-time estimate

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
       \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\to0.
$$

After resummation, the remaining quantities are coherent diagonal
matrix elements of $(\operatorname{Ad}U_N)^m$, collected
over explicitly known arithmetic fibers. The previously available
individual-entry estimates do not control these powers at times
of order $N$. No omitted estimate is promoted to a hypothesis
or asserted as a proved consequence of the identities.

