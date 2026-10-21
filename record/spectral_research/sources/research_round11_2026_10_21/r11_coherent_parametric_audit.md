> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round11_2026_10_21/r11_coherent_parametric_audit.md`. Embedded SHA256: `f600be6e7a6f2158ce5e50ef41ccdccca96f0da5ca3c5b4ece8b9b727038422e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/pell.md).

# Independent audit of the parametric route, with an all odd return-curvature bound

21 October 2026. Auditor: `/root/r11_coherent`.

## 0. Verdict and scope

The raw target `root_parametric_eigenphase_dynamics.md` was first read
in full at SHA-256
`bd0e8abdf64df6f0bb1d8d59ff83613ed0418978bdd55b00215e906e0ad54b36`,
together with its exact Python code and result file. The later changes
to its introduction, Pell source reference, and new Section 6.1 were
then read and checked. This audit certifies the resulting file at
SHA-256 `1d9020c850984fcc884c81dfaeb243ea455792a03429436fdb93a9fc8f32dcdb`.
The finite-dimensional derivations and their constants are correct.

In particular, the Weyl covariance uses the stated $S$, with the
inverse in the opposite conjugation direction; the eigenphase
acceleration has no additional factor $2$; the charge and energy
formulas use an ordered sum over unequal pairs; and scalar-return
curvature is correctly centered when $\operatorname{Tr}A\ne0$.
The cubic Taylor remainder and its shrinking range are correct.
The source does not improperly promote a nonzero individual
commutator to a bound on a sum of commutators.

The separate Pell assertion was subsequently checked from
`r11_arithmetic_pell_magnus.md`, Sections 1--5, read in full.
Its covariance, coefficient list, Pell identities, complete two-mode
collision classification, and variance normalization were checked
independently. The formerly pending input
$V_d=d(C_0+2C_1)$ is therefore closed within its stated scope.

Two additions are proved here. A fixed nonzero charge does not
prevent arbitrarily small simple gaps even for an irreducible pair
$A,M$: an exact $3\times3$ example establishes this. For the
original family, for **every odd $N\ge101$** and every scalar return
$M_N^d=\gamma I$, one has the uniform bound

$$
 \operatorname{Tr}B_d^2\ge\frac{81}{200}Nd,\qquad
 B_d=\sum_{r=0}^{d-1}M_N^rA_NM_N^{-r}.
 \tag{0.1}
$$

Its consequence for the exact initial curvature is

$$
 \left.\frac{d^2}{ds^2}
 |\operatorname{Tr}(e^{isA_N}M_N)^d|^2\right|_{s=0}
 \le-\frac{81}{100}N^2d.
 \tag{0.2}
$$

These are local parametric statements. They do not evaluate the
original matrix at $s=N10^{-80}$, prove a microscopic gap bound
there, or establish the fixed-detector pair limit.

## 1. Covariance, coefficients, and exact constants

Use $W_v=T_N(l,k)$ for $v=(k,l)$, and
$S=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$.
The checked kernel comparison gives

$$
 M_N^*T_N(a,b)M_N=T_N(3a-4b,-2a+3b),\qquad
 M_NW_vM_N^*=W_{Sv}.
 \tag{1.1}
$$

In $T(a,b)M$, the linear kernel coefficients relative to $M$ are
$b-3a/4,a/4$. In $MT(a',b')$ they are
$-a'/4,3a'/4+b'$. They imply the first formula. The constants agree:

$$
 ba/2-3a^2/8=-3(a')^2/8-b'a'/2.
$$

These fractions are modular inverses. In Fourier labels the first
conjugation direction has label matrix $S^{-1}$, as required.

The independent coefficient construction used in this audit starts
with

$$
 r_0=1,\quad r_{\pm1}=\frac12,\quad
 r_{\pm7}=-\frac12,\quad r_{\pm6}=r_{\pm8}=-\frac14,
$$

and zero otherwise. For $\gamma_0=(-3-4i)/1000$, it gives

$$
 c_{k,0}=\frac12\mathbf1_{|k|=7}+\frac{r_k}{10}
  -\frac1{10}\mathbf1_{k=0}
  +\frac{r_{k-1}-r_{k+1}}{200i},\qquad
 c_{k,1}=\gamma_0r_k,\quad c_{k,-1}=\overline{\gamma_0}r_k.
 \tag{1.2}
$$

This agrees entry by entry with all 32 coefficients in the target's
JSON output. In particular $c_{\pm7,0}=9/20$.

The Weyl trace rule gives

$$
 \frac1N\operatorname{Tr}A_N^2=\sum_v|c_v|^2,\qquad
 \frac1N\operatorname{Tr}(A_NM_N^*A_NM_N)
 =\sum_v c_vc_{-Sv}.
 \tag{1.3}
$$

The maximum infinity norm of $v+Sw$ over the support is $37$,
so every odd $N\ge39$ suffices to exclude nonzero aliases. When
the trace survives, the two Weyl labels are opposite and their
product phase is one. Thus no midpoint phase is discarded.

The only support pairs $v,Sv$ are
$(1,-1)\mapsto(1,1)$ and $(-1,1)\mapsto(-1,-1)$.
Indeed their second image coordinate $4k+3l$ must have magnitude
at most one, and the support has $l\in\{-1,0,1\}$.
Substitution gives exactly

$$
 C_0=\frac{66033}{160000},\qquad
 C_1=-\frac7{2000000},\qquad
 2(C_0-C_1)=\frac{1650839}{2000000}.
 \tag{1.4}
$$

The target's alternative trigonometric evaluation of $C_0$ was
also checked: the even and odd parts have the stated frequencies,
coefficients, and orthogonal squared norms.

For completeness, the exact trace rule also gives
$\operatorname{Tr}A_3=-3/20$, $\operatorname{Tr}A_7=63/10$,
and zero for every other odd $N\ge3$. The possible remaining
small aliases have purely imaginary conjugate coefficients that
cancel. The target's trace-zero results are stated for $N\ge39$,
so these exceptions do not invalidate them.

## 2. Local eigenphase equations: sign and normalization

Fix a finite Hermitian $A$, a finite unitary $M$, and
$U(s)=e^{isA}M$. On a simple-spectrum interval choose
$UV=V\Lambda$, with

$$
 \Lambda=\operatorname{diag}(\lambda_j),\quad
 \lambda_j=e^{i\varphi_j},\quad a=V^*AV,\quad H=V^*V'.
$$

The necessary local smooth choice is justified as follows. Choose
disjoint circles around the simple eigenvalues at one parameter.
The finite resolvents remain defined on those circles nearby, by
the Neumann series. Their contour integrals are smooth rank-one
spectral projections. Project each initial eigenvector and normalize.
A local argument of each eigenvalue then gives the phases. A scalar
phase change of each eigenvector sets $H_{jj}=0$.
Differentiating $V^*V=I$ gives $H^*=-H$.

Differentiate $UV=V\Lambda$, using $U'=iAU$:

$$
 ia\Lambda+\Lambda H=H\Lambda+\Lambda'.
$$

Its entries give

$$
 \varphi_j'=a_{jj},\qquad
 H_{lj}=\frac{i\lambda_ja_{lj}}{\lambda_j-\lambda_l}\quad(l\ne j).
 \tag{2.1}
$$

Also $a'=-Ha+aH=[a,H]$. Consequently

$$
\begin{aligned}
 \varphi_j''
 &=\sum_{l\ne j}(a_{jl}H_{lj}-H_{jl}a_{lj})\\
 &=\sum_{l\ne j}|a_{jl}|^2
     i\frac{\lambda_j+\lambda_l}{\lambda_j-\lambda_l}\\
 &=\sum_{l\ne j}|a_{jl}|^2
     \cot\frac{\varphi_j-\varphi_l}{2}.
\end{aligned}
 \tag{2.2}
$$

Factoring $e^{i(\varphi_j+\varphi_l)/2}$ verifies the last equality.
There is no extra factor $2$; the small-gap behavior already
contains $2/(\varphi_j-\varphi_l)$ through the cotangent.

An independent two-level check uses
$A=\left(\begin{smallmatrix}0&g\\g&0\end{smallmatrix}\right)$,
$M=\operatorname{diag}(\lambda_1,\lambda_2)$. Its characteristic
polynomial is

$$
 z^2-\cos(gs)(\lambda_1+\lambda_2)z+\lambda_1\lambda_2.
$$

Implicit differentiation at zero gives $\lambda_1'(0)=0$ and

$$
 \lambda_1''(0)=-g^2
 \frac{\lambda_1(\lambda_1+\lambda_2)}{\lambda_1-\lambda_2}.
$$

Dividing by $i\lambda_1$ gives (2.2), with the same coefficient
and sign.

## 3. Charge and the scope of “repulsion”

At every real parameter,

$$
 U(s)^*AU(s)=M^*AM,\qquad D=M^*AM-A.
$$

At any one parameter choose an orthonormal eigenbasis, allowing
multiplicity for this algebraic step. Then

$$
 (V^*DV)_{jl}=(\overline\lambda_j\lambda_l-1)a_{jl},
$$

so the squared Hilbert--Schmidt norm is

$$
 \operatorname{Tr}D^2
 =\sum_{j,l}4\sin^2\frac{\varphi_j-\varphi_l}{2}|a_{jl}|^2.
 \tag{3.1}
$$

This is an ordered sum; a $j<l$ form has coefficient $8$.
Combining it with
$\operatorname{Tr}A^2=\sum_j a_{jj}^2+\sum_{j\ne l}|a_{jl}|^2$
gives, on a simple-spectrum interval,

$$
 \frac12\operatorname{Tr}A^2
 =\frac12\sum_j(\varphi_j')^2+
   \frac18\sum_{j\ne l}
   \frac{|\ell_{jl}|^2}{\sin^2((\varphi_j-\varphi_l)/2)},
 \quad \ell_{jl}=(\overline\lambda_j\lambda_l-1)a_{jl}.
 \tag{3.2}
$$

The source's factor $1/8$ is correct. The original-coordinate
matrix $D$ is fixed, but its moving-basis matrix has derivative
$[V^*DV,H]$. Thus its entries $\ell_{jl}$ are not individual
constant positive couplings.

For pairs of circular angular distance at most $\varepsilon$,
their total contribution to (3.1) is at most
$\varepsilon^2\operatorname{Tr}A^2$, because
$4\sin^2(\delta/2)\le\delta^2$.
The nonzero constant in (1.4) can therefore be supplied by
macroscopic gaps. It does not force a lower microscopic coupling.

## 4. Exact discriminator: nonzero charge and irreducibility permit a collision

This is an auxiliary counterexample to an inference from the
parametric equations, not a counterexample to the original family.

Let

$$
 A=\operatorname{diag}(-1,0,1),\quad
 v=\frac1{\sqrt3}(1,1,1)^T,\quad P=vv^*,\quad M=I+(i-1)P.
 \tag{4.1}
$$

The projection $P$ is orthogonal, so $M$ acts by $i$ on its
range and by $1$ on its complement; hence it is unitary.
A matrix commuting with the simple diagonal $A$ is diagonal.
Every off-diagonal entry of $M$ is $(i-1)/3\ne0$; hence a
diagonal matrix commuting with $M$ must be scalar. Thus this
pair has only a scalar common commutant, and no nontrivial common
reducing subspace.

Since $\langle v,Av\rangle=0$ and $\|Av\|^2=2/3$,

$$
 D=(i-1)AP+(-i-1)PA,\qquad \operatorname{Tr}D^2=\frac83.
 \tag{4.2}
$$

For the norm computation, the two same-orientation products have
zero trace, while each cross product has trace $2\|Av\|^2$.
The charge is the same nonzero matrix at every parameter along
$U(s)=e^{isA}M$. Nevertheless $U(0)$ has a double eigenvalue $1$.

There are arbitrarily close simple pairs nearby. With
$x(s)=1+2\cos s$, direct expansion gives

$$
 \det(zI-U(s))
 =z^3-\frac{2+i}{3}x(s)z^2+\frac{1+2i}{3}x(s)z-i.
 \tag{4.3}
$$

For instance, expand the rank-one determinant
$zI-D_s-(i-1)D_sP$, where
$D_s=\operatorname{diag}(e^{-is},1,e^{is})$.
The first two elementary symmetric functions of the entries of
$D_s$ both equal $x(s)$, and their product is one.
At zero, (4.3) factors as $(z-1)^2(z-i)$.

For a monic cubic $z^3+bz^2+cz+d$, expanding the root product
gives discriminant
$b^2c^2-4c^3-4b^3d-27d^2+18bcd$.
Substitution yields

$$
 \operatorname{disc}
 =-\frac{x-3}{81}(729+243x-189x^2+25x^3)
 =\frac{16}{3}s^2+\frac{20}{9}s^4+O(s^6).
 \tag{4.4}
$$

Thus all eigenvalues are simple for all sufficiently small
nonzero $s$; two tend to $1$, so their gap tends to zero.
More precisely, substitute $z=1+sy$ in (4.3) and divide by
$s^2$. The resulting analytic function at $s=0$ is
$(1-i)(y^2+1/3)$, with two simple roots. The local implicit
function theorem gives

$$
 \lambda_\pm(s)=1\pm is/\sqrt3+O(s^2),\qquad
 \varphi_\pm(s)=\pm s/\sqrt3+O(s^2).
 \tag{4.5}
$$

Their angular gap is $2|s|/\sqrt3+O(s^2)$. This proves the
claimed failure of a lower gap bound from fixed nonzero charge,
even with a fixed generator of norm one and a scalar common
commutant. No such deduction is made in the audited source.

## 5. Trace derivatives and scalar-return curvature through collisions

For $p_m(s)=\operatorname{Tr}U(s)^m$, finite differentiation
and cyclicity give

$$
 p_m'=im\operatorname{Tr}(AU^m),\qquad
 p_m''=-m\sum_{r=0}^{m-1}\operatorname{Tr}(AU^rAU^{m-r}).
 \tag{5.1}
$$

These analytic matrix identities remain valid through collisions.
They involve no division by gaps.

If $M^d=\gamma I$, put $X_r=M^rAM^{-r}$ and
$B_d=\sum_{r=0}^{d-1}X_r$. The adjoint sequence is periodic;
each residue of a difference of two indices occurs $d$ times:

$$
 \operatorname{Tr}B_d^2
 =d\sum_{r=0}^{d-1}\operatorname{Tr}(AM^rAM^{-r}).
$$

Consequently

$$
 p_d(0)=\gamma N,\quad
 p_d'(0)=i\gamma d\operatorname{Tr}A,\quad
 p_d''(0)=-\gamma\operatorname{Tr}B_d^2,
$$

and the unnormalized curvature is exactly

$$
 (|p_d|^2)''(0)
 =2(d\operatorname{Tr}A)^2-2N\operatorname{Tr}B_d^2
 =-2N\operatorname{Tr}
 \left(B_d-\frac{\operatorname{Tr}B_d}{N}I\right)^2.
 \tag{5.2}
$$

This confirms both the source's centered formula and its trace-zero
specialization.

## 6. Additional original-family theorem: every scalar return

**Theorem.** For every odd $N\ge101$ and every integer $d\ge1$
with $M_N^d=\gamma I$, (0.1)--(0.2) hold.

**Proof.** The integral polynomial $Q(k,l)=2k^2-l^2$ satisfies

$$
 Q(3k+2l,4k+3l)=Q(k,l).
 \tag{6.1}
$$

From (1.2), its values on the complete support are

$$
 -1,1,2,8,50,71,72,97,98,127,128,162.
 \tag{6.2}
$$

The only labels with $Q=98$ are $v_0=(7,0)$ and $-v_0$.
Both coefficients equal $c=9/20$.
Moreover $\max_{v\in\mathcal F}|Q(v)-98|=99$.
For $N\ge101$, the congruence $Q(v)\equiv98\pmod N$
therefore selects precisely those two support labels. This uses
no primality assumption.

By exact modular covariance,

$$
 B_d=\sum_{r=0}^{d-1}\sum_{v\in\mathcal F}c_vW_{S^rv}.
 \tag{6.3}
$$

The scalar return implies $S^d=I\pmod N$, because conjugation
by $M_N^d$ fixes every Weyl matrix, and distinct labels are
linearly independent. This follows directly from
$\operatorname{Tr}(W_u^*W_v)=N\mathbf1_{u=v}$.

Let $\mathcal O_+$ be the $S$-orbit of $v_0$, of length $L$.
Then $L\mid d$. The orbit $\mathcal O_-$ of $-v_0$ also has
length $L$, since negation commutes with $S$. These orbits are
equal or disjoint, and $v_0\ne-v_0\pmod N$.

By (6.1)--(6.2), no other coefficient contributes to either orbit
in (6.3). If the two orbits are disjoint, every coefficient on
each orbit is $cd/L$. If they agree, each coefficient on the
common orbit is $2cd/L$. These coefficients are positive real
numbers and cannot be canceled by other generator modes.
Orthogonality of the Weyl basis and Hermiticity of $B_d$ give

$$
 \frac1N\operatorname{Tr}B_d^2\ge
 \begin{cases}
 2c^2d^2/L=\dfrac{81}{200}\,d^2/L,
       &\mathcal O_+\cap\mathcal O_-=\varnothing,\\[4pt]
 4c^2d^2/L=\dfrac{81}{100}\,d^2/L,
       &\mathcal O_+=\mathcal O_-.
 \end{cases}
 \tag{6.4}
$$

Since $L\le d$, both cases imply (0.1). The generator has zero
trace in these dimensions, so (5.2) proves (0.2). $\square$

Positivity was used only for the isolated two-mode orbit
coefficients and the exact Hilbert--Schmidt square afterwards.
No sign assertion about other coherent path or commutator sums
is being made.

## 7. Taylor control and its physical limitation

The original generator satisfies $\|A_N\|\le L_A=79/50$
by the coefficient triangle inequality for every odd $N$.
Distributing $j$ derivatives over the $d$ exponentials gives

$$
 |p_d^{(j)}(s)|\le N(dL_A)^j,\qquad
 \left|\left(\frac{|p_d|^2}{N^2}\right)^{(j)}(s)\right|
 \le(2dL_A)^j.
$$

The first bound uses the multinomial coefficient sum $d^j$;
the second uses the product rule and the binomial sum.
For a trace-zero generator at a scalar return, real Taylor
expansion therefore yields

$$
 q_d(s)=1-V_ds^2+R_d(s),\quad
 q_d=|p_d|^2/N^2,\quad V_d=N^{-1}\operatorname{Tr}B_d^2,\quad
 |R_d(s)|\le\frac43d^3L_A^3|s|^3.
 \tag{7.1}
$$

This verifies the source's remainder and its coefficient.
Since the additional theorem gives $V_d\ge81d/200$,

$$
 |s|\le\frac{243}{1600L_A^3d^2}
 \quad\Longrightarrow\quad
 q_d(s)\le1-\frac{81}{400}d s^2
 \tag{7.2}
$$

for every odd $N\ge101$ and every scalar return. The stated
bound on $s$ makes the remainder in (7.1) at most
$(81d/400)s^2\le V_ds^2/2$.

This explicit local window concerns the original parametric
curve. The physical parameter $s=N10^{-80}$ eventually leaves
it, even without invoking growth of $d$.

### 7.1. Independent check of the Pell input

Sections 1--5 of `r11_arithmetic_pell_magnus.md` were read, through
line 373 of the initial file. For odd $r\ge11$, that source takes
$(1+\sqrt2)^r=x_r+y_r\sqrt2$, $N_r=x_ry_r$, and $d=2r$.
Its identities $S^r\equiv cI\pmod{N_r}$,
$c\equiv1\pmod{x_r}$, $c\equiv-1\pmod{y_r}$, and
$S^{2r}\equiv I\pmod{N_r}$ follow directly from the Pell equation.

The collision classification is sufficient and correctly proved.
Represent a time as $\varepsilon t+\eta r$, with
$t\le(r-1)/2$, and put $z=S^{\varepsilon t}v$.
For $\eta=0$, the explicit bound
$\|z-w\|_\infty<N_r$ excludes a nonzero modular multiple.
The integer equality is then classified by $Q$ and the expanding
linear form $\sqrt2k+l$: only lags $0,\pm1$ survive.

For $\eta=1$, the congruence gives
$z_i-w_i=x_rp_i$, $z_i+w_i=y_rq_i$, with
$|p_i|,|q_i|\le15$.
If $(p_i,q_i)\ne(0,0)$, the irrationality identity and Pell
relation give

$$
 |y_rq_i-x_rp_i|
 \ge\frac{y_r}{15(1+\sqrt2)}
       -\frac{15}{x_r+\sqrt2y_r}>18.
$$

The last bound holds at $r=11$ and increases afterwards. It
contradicts $|2w_i|\le18$. If both pairs vanish, then $w=0$,
which is absent from the support. This completes the classification
at every stated dimension, not just in computed examples.

The surviving lag traces are $C_0$ at lag zero and $C_1$ at
each of the two neighboring lags. The Weyl product phase is one
on the surviving opposite labels, including modular coincidences.
Every cyclic lag occurs $d$ times in the double sum, proving

$$
 V_d=d(C_0+2C_1)
   =d\,\frac{1650797}{4000000}.
 \tag{7.3}
$$

Thus the source's invocation of this Pell identity is verified.
The ratio of the remainder bound in (7.1) to its quadratic term
is proportional to $d^2|s|$. Hence its stated sufficient
condition $d^2|s|\to0$, and failure at $s=N_r10^{-80}$,
are correct. This is a limitation of the bound; it is not a proof
that the actual remainder must be large there.

The final editorial delta in the target's Section 5 was also checked
by comparing its complete text with the preceding audited version.
Only two lines changed: the statement now explicitly concerns the
ratio of the displayed upper bound for the remainder to the quadratic
term. That ratio is exactly a fixed positive constant times
$d^2|s|$, so its convergence to zero requires
$d^2|s|\to0$. This does not assert that the same condition is
necessary for the actual remainder to be relatively small. The revised
wording is correct and makes the scope more precise.

## 8. Full product and commutator caveat

At a scalar return,

$$
 U(s)^d=\left(\prod_{r=0}^{d-1}e^{isX_r}\right)\gamma I,\qquad
 X_r=M_N^rA_NM_N^{-r},
$$

with increasing $r$ from left to right. Comparing second-order
terms with a single exponential gives

$$
 \prod_{r=0}^{d-1}e^{isX_r}-e^{isB_d}
 =-\frac{s^2}{2}\sum_{r<t}[X_r,X_t]+O_{N,d}(s^3).
 \tag{8.1}
$$

Indeed the product has coefficient $-\sum_{r<t}X_rX_t$;
the single exponential has
$-\frac12\sum_{r<t}(X_rX_t+X_tX_r)$.
The sign in the target is therefore correct.

The source correctly distinguishes a nonzero individual
commutator, the sum of all second-order commutators, and the
full finite-$s$ product. The first alone bounds neither of the
latter two quantities.

### 8.1. Audit of the added complete second-order bound

After the target added its Section 6.1, Sections 6--9 of
`r11_arithmetic_pell_magnus.md` were also read in full. The
complete second-order bound was checked from its proof, rather
than inferred from a single commutator.

For the selected endpoint
$b_{\varepsilon,\eta}=(7\varepsilon,0)+c(0,\eta)$, its Lemma
8.1 proves uniqueness of the unordered two-frequency representation
throughout the entire $2r$-period for odd $r\ge25$.
The same-type CRT alternatives force a bounded-coefficient
approximation $yq-xp=2w$ that contradicts the stated
Diophantine lower bound. In the mixed case the proof writes

$$
 \alpha=v_0+\frac{xp+yq}{2},\quad
 L=\sqrt2p+q,\quad
 Q(\alpha)=\frac{y^2}{4}Q(L)+y\mathcal B(v_0,L)+E.
$$

The bounds $|p_i|,|q_i|\le32$, $|E|\le5122$,
$|Q(L)|>1/15360$ when nonzero, and
$|\mathcal B(v_0,L)|>1/1520$ in the nonzero isotropic case
were checked. For $y\ge10^9$ both alternatives contradict
$|Q(\alpha)|\le162$. The remaining case $L=0$ forces
$p=q=0$ by irrationality. The prior integer orbit classification
then gives precisely the claimed seeds and times. The numerical
threshold is supplied by $y_{25}=1311738121$.

The resulting $8r$ labels $S^tb_{\varepsilon,\eta}$ are
distinct: a coincidence, transported by $S^{-t}$, would violate
that uniqueness unless the times and signs coincide. A shift by
$r$ would interchange the two different seed axes and is excluded.
At each label the squared modulus of the unique commutator
coefficient is

$$
 4\frac{81}{400}\frac1{40000}
       \sin^2(7\pi c/N)
 =\frac{81}{4000000}\sin^2(7\pi c/N).
$$

For times beyond $r$ the ordering reverses the coefficient's
sign, which does not affect this square. Weyl orthogonality now
gives

$$
 \frac1N\left\|\sum_{i<j}[X_i,X_j]\right\|_{\mathrm{HS}}^2
 \ge\frac{81r}{500000}\sin^2(7\pi c/N).
$$

Thus the target's added equation (6.3) is correct with its threshold
$r\ge25$. The coefficient of $s^2$ in (8.1), and in the local
matrix logarithm, is half this sum with a minus sign; its squared
norm receives an additional factor $1/4$. This confirms both
normalization and the explicitly stated lack of a lower bound for
the full finite-$s$ remainder.

## 9. Published source scope

The complete five-page primary text of Braun, Gnutzmann, Haake,
Kuś, and Życzkowski, *Level Dynamics and Universality of Spectral
Fluctuations*, arXiv:nlin/0006022v3, was independently opened and
read: [primary PDF](https://arxiv.org/pdf/nlin/0006022).
Page 2 distinguishes parameter averages from statistics at one
parameter value. Its coupling variables are dynamical; the later
collision-scale discussion includes model-specific and numerical
input. It supplies no theorem giving the missing unaveraged limit
for the present matrices. This confirms the source's scope statement.

## 10. Executed checks and provenance

`r11_coherent_parametric_checks.py` constructs (1.2) independently
without importing the target's construction. It verifies all 32
coefficients against the target's output, the exact constants,
the two support overlaps, the alias radius, and the $Q=98$
isolation certificate.

It also sums every transported coefficient over the exact order
of $S\pmod N$ in dimensions $101,105,121,143$. These include a
prime, a square, and composite dimensions. All satisfy (6.4).
These finite checks supplement, and do not replace, the proof
for all odd dimensions in Section 6.

An independent Wolfram Language kernel checked the auxiliary
$3\times3$ charge, characteristic polynomial, discriminant, and
compressed generator polynomial. The submitted code and raw
responses are preserved in `r11_coherent_parametric_wolfram.wl`
and `r11_coherent_parametric_wolfram_record.json`.

A convention was corrected explicitly: the first call used
`CharacteristicPolynomial`, whose odd-dimensional sign was
opposite to the written $\det(zI-U)$ convention. That equality
was not accepted. The corrected call uses
`Det[z IdentityMatrix[3]-U]` and returned residual exactly zero.
The raw record retains both calls. Initial attempts to import
SymPy in two Python runtimes failed because it was absent;
no SymPy computation is asserted.

No numerical spectrum of the original fixed-kick matrix was
replaced by a zero-kick spectrum. The computations check exact
finite identities, modular orbit sums, and the explicitly stated
local derivative results only.

## 11. First unresolved original estimate

None of the verified equations provides the required cancellation

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \left(
 |\operatorname{Tr}[(e^{i10^{-80}NA_N}M_N)^m]|^2
 -\min(m,N)
 \right)\longrightarrow0
 \tag{11.1}
$$

along all odd dimensions. The moving-basis couplings in (2.2)
are not quantitatively controlled at the physical parameter;
the exact local return estimate has not been extended to it.
The stronger all-orders criterion remains unproved.
Neither missing step is assumed as a theorem or hidden in the
word “repulsion.”

The target file, master, and earlier sources were left unchanged.
A separate machine-readable manifest records the actual input
and output hashes and their read scope.


## 12. Input and check hashes

| File | SHA-256 |
|---|---|
| `root_parametric_eigenphase_dynamics.md` | `1d9020c850984fcc884c81dfaeb243ea455792a03429436fdb93a9fc8f32dcdb` |
| `root_parametric_exact_check.py` | `d0b55e0c876eafdbb5e8cdf27fb624ce85b20e2feb1db7308876daa2fbb047fb` |
| `root_parametric_exact_results.json` | `59596b62d273a936255fbf623a05f2635d13a48ab848bbd16c3c4221ed8f7210` |
| `r11_arithmetic_pell_magnus.md` | `83fef65536de1e5528ad8e4d5eebf39a2b42d7da4217274a32c1e4e6dc7707d5` |
| `r11_coherent_parametric_checks.py` | `0e3e67a7439681c699a5421bb5df68449d5a8f750e5da2e8423de083e58a4bf3` |
| `r11_coherent_parametric_checks.json` | `fecda8453e22b32abe78df680f1ac1dc7e0827a4bf82d0791b9ca78fae0f317f` |
| `r11_coherent_parametric_wolfram.wl` | `16642f1f3b14caac317df4ee7544e5f2fb9d529feb7997d88c1ed930c4dde8f9` |
| `r11_coherent_parametric_wolfram_record.json` | `851784289ecfba7b421abf6e0fe8f094a9f582fcef177b62bb18951ac1ba41d4` |
