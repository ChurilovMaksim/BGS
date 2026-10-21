> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round8_2026_10_21/r8_weyl_audit_uniform_self_overlap.md`. Embedded SHA256: `33111324edb6f838823e7159d9994d6874fa5debc0b3093666ca88972eb03d37`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: the largest original Weyl self-overlap

21 October 2026. Independent Weyl branch audit.

## 1. Frozen target and verdict

Audited in full:

`r8_original_uniform_weyl_self_overlap.md`

SHA-256:

`7ad8afb5fa2f9098111166b70398aad2fc95bf10de508f47ae661ec25080755d`.

**Verdict:** no mathematical error found in the new proof. In particular,
the density expansion with its stated error, the maximum exchange over
all modular labels, the unique limiting maximizing pair, its eventual
finite-dimensional identification, and the resulting
$O_\tau(N^{-2})$ asymptotic all follow from the explicit quantum
tail and fixed-label inputs.

The three quoted round-4 source hashes were verified and agree with
the target. Their precise tail and fixed-label conclusions were checked
in the named source; the full earlier center-phase construction was
not re-proved from scratch in this audit. This is an independent
internal audit of the new argument, not a publication claim or formal
verification.

## 2. Normalizations and modular signs

The physical parameter and classical time are correctly related by
$t=\tau/(2\pi)$ when the vector field is $Z=J\nabla a$.
Equivalently, the time is $\tau$ for
$X=J\nabla a/(2\pi)$. The exact ordinary-half symbol includes
$r(q+1/2)$ in its momentum-dependent term.

The frequency transport is
$S_f=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$,
whereas the matrix in the displacement map is its transpose
$S_c=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$.
Thus the fixed-label integral is

$$
\int e^{2\pi i((S_fv)\cdot\Phi_t(x)-v\cdot x)}\,dx
=\widehat g_t(-v).
$$

The sign of the Fourier index does not affect its modulus. Moreover
$S_f\equiv I\pmod2$, so the original and ordinary-half basis
signs at $v$ and $S_fv$ cancel exactly even before taking the
modulus. No congruence restriction beyond odd $N$ is used.

The direct check at $v=(4,-8)$ is also correct:
$v-S_fv=(8,0)$ and $\omega((8,0),S_fv)=64$. The exact
commutator derivative is therefore

$$
-2N a_{8,0}\sin(64\pi/N)
\longrightarrow-128\pi a_{8,0}
=\frac{8\pi}{25}(10-i).
$$

It agrees in both magnitude and phase with the density calculation.

## 3. The maximum over all modular labels

The reused estimate controls the output label:

$$
|C^E_{w,u}|\le C_*(1+|w|_N)^{-1/17}+C_*/N.
$$

For a self-overlap one has $w=v$, $u=S_fv$, so this gives
the required tail directly. There is no need to compare the centered
sizes of $S_fv$ and $v$, nor to prove an Egorov theorem for
growing labels.

For every prescribed error, a fixed integer radius makes this tail
small uniformly in all sufficiently large odd dimensions. Inside that
radius only finitely many labels remain and the fixed-label limits
are uniform. This proves the claimed supremum limit. The argument
is valid even if the constant $C_*$ is extremely large, since
$\tau$ is fixed before every limit.

Once the classical maximum has a positive gap, the same tail argument
reduces every sufficiently large quantum maximum to that finite set.
Uniform convergence on the set eliminates the other modes. The
opposite maximizing labels have exactly equal finite-dimensional
moduli by adjointness and trace cyclicity. Thus the eventual argmax
claim is justified.

The fixed-label Egorov error is $O(N^{-2})$. Its trace pairing
has aliases that decay faster than any fixed negative power, because
the paired classical symbol is smooth and both labels are fixed.
Consequently the stated $O_\tau(N^{-2})$ error for the maximum
does follow after the maximizing labels have become fixed. This is
not an asserted uniform rate for all labels or a bound on the
enormous unspecified threshold.

## 4. Symbol and flow constants

The direct derivative bounds on $r$ and $a$ in the target
check by the product rule. For example,

$$
\|r''\|_\infty
\le(392+56+8)\pi^2=456\pi^2,
$$

and

$$
\|a_{qq}\|_\infty
\le(196+45.6+6+4.56)\pi^2=252.16\pi^2.
$$

The maximum row sum in $DZ$ is at most
$(252.16+0.64)\pi^2<2600$. The Fourier bound on its next
derivative is comfortably below $3\cdot10^6$ in the stated
bilinear maximum norm.

For $s\le10^{-12}$, the variational equation yields
$\|D\Phi_s-I\|\le2601s$. The first-order displacement error
is bounded by $78000t^2$. For the derivative error, the exact
majorant before integration is

$$
(360000000+6762600)s,
$$

whose integral is $183381300t^2<2\cdot10^8t^2$.

The matrices are

$$
B=\begin{pmatrix}2&4\\2&2\end{pmatrix},
\qquad
R=B^{-1}S_c=\begin{pmatrix}1/2&1\\1/2&1/2\end{pmatrix},
\qquad\|R\|_\infty=3/2.
$$

Therefore all bounds in (4.5) of the target follow with the
displayed constants. The lift $G_t=I+Y_t$ is globally invertible
by a contraction on $\mathbb R^2$; periodicity gives a torus
diffeomorphism. The factorization $F_t=B\circ G_t$ is exact,
and $\det B=-4$ gives four sheets. The orientation of $G_t$
is positive, since its derivative remains connected to the identity
inside the invertible matrices.

## 5. Jacobian, inverse density, and coordinate shift

The trace error in replacing $DY_t$ by $tDY$ is at most
$6\cdot10^8t^2$. For a two-by-two matrix with maximum row
sum at most $3902t$, the determinant has absolute value at
most $3902^2t^2$. Thus the exact combined remainder is bounded
by

$$
(600000000+15225604)t^2
=615225604t^2<6.2\cdot10^8t^2.
$$

The further estimate $|J_t-1|\le7801t<1/2$ is valid on the
stated time interval. The reciprocal identity gives the error bound

$$
(620000000+2\cdot7801^2)t^2
=741711202t^2<7.5\cdot10^8t^2.
$$

The Lipschitz bound for $D=\operatorname{div}(RZ)$ is at most
twice the vector-valued bilinear bound for $D^2(RZ)$, namely
$9\cdot10^6$. The inverse-coordinate displacement is at most
$90t$, so multiplying their product by the external factor
$t$ costs at most $8.1\cdot10^8t^2$.

The sum of the last two errors is below $1.56\cdot10^9t^2$,
strictly below the declared $3\cdot10^9t^2$. The larger bound
is therefore safe.

The sign also checks:

$$
RJ=\begin{pmatrix}-1&1/2\\-1/2&1/2\end{pmatrix},
\qquad\operatorname{div}(RZ)=-a_{qq}+a_{pp}/2.
$$

Pushing forward through $G_t$ gives density
$1-t\operatorname{div}(RZ)+O(t^2)$, hence through $B$
gives the claimed plus sign in front of
$tP_B(a_{qq}-a_{pp}/2)$. The averaging formula for the four
inverse branches and
$\widehat{P_Bh}(v)=\widehat h(B^Tv)$ are valid for the
negative-degree cover, since densities use the absolute Jacobian.

## 6. Surviving modes and error conversion

The exact pure-position Fourier expansion and its coefficients at
$2,6,8$ check. Both coordinates of $B^Tv$ are even;
the momentum support of $a$ is only $-1,0,1$. Therefore
the surviving nonzero first-order modes satisfy
$v=m(1,-2)$, with $m=\pm1,\pm3,\pm4$.

Their moduli are exactly

$$
L_1=\pi^2/25,\qquad
L_3=9\pi^2\sqrt{101}/25,\qquad
L_4=16\pi^2\sqrt{101}/25.
$$

The gap $L_4-L_3>25$, while each Fourier coefficient of the
remainder has modulus at most its supremum norm. The difference
between the largest pair and every other mode is thus at least
$25t-6\cdot10^9t^2>0$. This establishes the claimed unique
maximizing pair, without an asymptotic assertion about a generic
small perturbation.

Finally

$$
L_4t=\frac{8\pi\sqrt{101}}{25}\tau,
\qquad
3\cdot10^9t^2<10^8\tau^2.
$$

The resulting interval $9\tau<\Gamma_t<11\tau$ follows
with a large strict margin at the exact prescribed $\tau$.
The normalized Hilbert--Schmidt distance formula in the target
has the correct factor $2-2|\langle X,Y\rangle|$.

## 7. Scope conclusion

No correction is requested. The theorem gives a precise, almost
orthogonal one-step bound for each individual Weyl operator,
uniform over all nonidentity labels. It does not concern coherent
linear combinations of those operators or control long powers of
the adjoint matrix. The target explicitly retains that distinction
and the unresolved original signed pair functional.
