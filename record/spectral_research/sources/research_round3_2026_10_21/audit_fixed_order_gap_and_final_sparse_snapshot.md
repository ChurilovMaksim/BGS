> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_fixed_order_gap_and_final_sparse_snapshot.md`. Embedded SHA256: `baa6321547e3ab0aa40d210ee9e55554718f37497de1bac3f1c20abab4892b5d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of fixed-order arithmetic escape

Date: 21 October 2026.

## 0. Snapshot, verdict, and the final sparse-history binding

The audited primary source is arithmetic_comb_fixed_order_gap.md,
SHA-256
e43296774f12851d7150e0d501afd1de76fd4feb11161e9f30692f1866cd1bf8.
The author confirmed this snapshot is frozen.

**Verdict:** the stated theorem passes independent reconstruction.
For every fixed integer $r\ge2$, the exact kick has a positive
input/output character escape gap, uniformly for all sufficiently
large odd dimensions with $N=d^2m,\ d\ge N^{1/r}$.
The constants and dimension threshold may depend on $r$.
The argument does not allow $r$ to grow with $N$.

This audit also records the final metadata change in
phase_sparse_character_histories.md.
Its final SHA-256 is
8bc8ecddf8b5b684eeff3b31ab9e8f99a864a50413bcbe8b3edd1791f04200bd.
Relative to the previously audited snapshot
33e39b8eca7f331db2bf78671d57d60cdebf18c1c3702cf7734da01de663a761,
the changes update the rescaled-input SHA and remove an unnecessary
comment about numerical rate size. The proof formulas are unchanged;
the changed passages were read directly.
The verdict in audit_rescaled_gap_and_sparse_histories.md,
SHA-256
3dc9d2822133c2b6108216834f36d8e29801fdad9332bf05088f095a11b6f950,
therefore applies to this final sparse-history snapshot.
The rescaled input remains at SHA-256
898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f.

## 1. Uniform quantum-to-classical symbol convergence

Write $h=(2\pi N)^{-1}$, $t=\tau/(2\pi)$, and
$E_h=e^{itQ_h(a)/h}$, with the actual corrected physical symbol.
The support of $a$ lies in $|k|+|l|\le9$, and its coefficient
one-norm is less than two.

For the quantum derivation
$$
 Q_h(L_hb)=(-i/h)[Q_h(a),Q_h(b)]
$$
and its classical limit $L_0b=\{a,b\}$, the Fourier multipliers are
respectively
$$
 \frac2h\sin(2\pi^2h\omega),\qquad4\pi^2\omega.
$$
At the $j$-th bracket, the input support has size at most $9j$.
Hence $|\omega|\le81j$, and the full one-norm multiplier is at most
$648\pi^2j<7000j$. The starting norm is
$\|a_q\|_0<36\pi<120$. It follows that
$$
 \|L_h^na_q\|_0,\ \|L_0^na_q\|_0
 \le120\,7000^n n!.
$$
Both output supports have size at most $9(n+1)$.

The sine remainder is globally bounded by
$$
 \left|\frac2h\sin(2\pi^2h\omega)-4\pi^2\omega\right|
 \le\frac83\pi^6h^2|\omega|^3.
$$
Including the coefficient norm of $a$, one exceptional bracket at
position $j$ costs at most
$$
 \frac{16}{3}\pi^6\,81^3h^2j^3
 <(7000j)\,10^6h^2j^2.
$$
The numerical inequalities can be checked with the elementary bound
$\pi<13/4$: the ordinary step bound becomes $13689/2<7000$,
and the exceptional ratio to $7000\cdot10^6$ is at most
$$
 \frac{855054733923}{1792000000000}<1.
$$
The bound $\pi<13/4$ follows, for example, from the circumscribed
regular twelve-gon.

Telescoping $L_h^n-L_0^n$ gives $n$ such terms.
At every ordinary step the same support and $7000j$ bound applies,
regardless of which derivation appears there.
Since $\sum_{j=1}^n j^2\le n^3$,
$$
 \|(L_h^n-L_0^n)a_q\|_s
 \le120\,7000^n n!\,10^6h^2n^3\,
             10^s(n+1)^s.
$$
Summing after multiplication by $t^{n+1}/(n+1)!$ proves
$$
 \|v_h-v_0\|_s\le C_s h^2t^2
$$
for every fixed Fourier weight $s$.
The remaining series is a geometric series with parameter
$7000|t|$, times a fixed polynomial in $n$.
The convergence time therefore does not shrink when one asks for a
higher fixed derivative order. Its constant does grow with that order.

For each fixed $h$, the quantized convergent series solves the
bounded-operator Heisenberg equation uniquely. Integrating the bounded
commutator with $P=-ih\partial_q$ gives the exact identity
$$
 E_h^*PE_h=P+Q_h(v_h).
$$
Thus the symbol being approximated is attached to the actual
Schrödinger exponential.

## 2. A fixed nonzero coefficient survives every derivative order

The classical series satisfies
$$
 \|v_0-ta_q\|_0\le2\cdot10^6t^2.
$$
The actual Fourier coefficient is
$$
 \widehat{a_q}(7,0)=2\pi i\cdot7\cdot\frac9{20}
 =\frac{63\pi i}{10}.
$$
At the prescribed $t=10^{-80}/(2\pi)$, its leading magnitude
exceeds the error by a strict margin, giving
$|\widehat v_0(7,0)|>t>0$.

Consequently $\partial_q^{r-1}v_0$ is nonconstant for every fixed
integer $r\ge2$: its coefficient at $(7,0)$ is the same nonzero
coefficient multiplied by $(14\pi i)^{r-1}$.
This reasoning does not subtract high-derivative remainder bounds
from high-derivative leading terms. It is the crucial reason that
arbitrarily large fixed $r$ is allowed.

## 3. The general finite-word estimate

Let $H_0=-P$ and $H_1=-P-Q_h(v_h)$.
Every first nonzero mixed scaled commutator of these two operators is
a derivative of $Q_h(v_h)$.
A further commutator with $H_0$ costs one Fourier weight and a factor
$2\pi$. A further commutator with the bounded part of $H_1$ is
controlled by
$$
 \|(-i/h)[Q_h(v_h),Q_h(b)]\|_s
 \le40\|v_h\|_{s+1}\|b\|_{s+1}.
$$
For any fixed $r$, the preceding series supplies
$\|v_h\|_r\le V_r|t|$, uniformly for $|t|\le10^{-12}$.
All mixed commutators of depth $r$ are therefore bounded by
$$
 2\pi V_r(2\pi+40V_r10^{-12})^{r-1}|t|.
$$
Finiteness is sufficient; this expression need not be small.

The word $C_{r-1}(u)$ has
$L_r=3\cdot2^{r-1}-2$ factors and $2^{r-1}$ occurrences of the
conjugated translation or its inverse.
Its left logarithmic generator is a sum of signed $H_j$'s
conjugated by finite prefixes.
Expanding those conjugations from right to left to total degree
$r-1$, each discarded remainder involves exactly $r$ original
scaled brackets. Any later prefix conjugates that remainder unitarily.
Thus the remainder is $O_r(|t||u|^r)$ in operator norm.

This argument uses bounded commutators after the first bracket.
It does not take an operator-norm Taylor series of an unbounded
translation generator. The operations hold first on the common
Schwartz core; bounded remainders then extend to the whole Hilbert space.
The common linear terms cancel in the logarithmic generator.

The formal universal coefficients identify the finite Taylor
polynomial: a group commutator with $e^{uX}$ raises the leading
degree by one and replaces the leading term by its bracket with $X$.
Hence
$$
 \frac h i C_{r-1}'(u)C_{r-1}(u)^*
 =r u^{r-1}K_{r,h}+O_r(|t||u|^r),
$$
$$
 K_{r,h}=(i/h)^{r-1}\operatorname{ad}_{-P}^{r-1}H_1
 =(-1)^rQ_h(\partial_q^{r-1}v_h).
$$
Unitary Duhamel comparison gives
$$
 \|C_{r-1}(\delta)-e^{i\delta^rK_{r,h}/h}\|
 \le C_r|t|\delta^{r+1}/h,\qquad0\le\delta\le1.
$$
The number of prefixes and derivatives is finite for each fixed $r$.
No estimate uniform in growing $r$ has been claimed or established.

## 4. Endpoint descent and ordinary phase quantization

For $d\ge N^{1/r}$, choose
$$
 b=\lfloor dN^{-1/r}\rfloor,\quad
 \delta=b/d,\quad \beta=N\delta^r.
$$
Then $b\ge1$, $\delta\le N^{-1/r}$, and
$2^{-r}\le\beta\le1$, because $\lfloor x\rfloor\ge x/2$ for $x\ge1$.
The integer $N\delta=bdm$ ensures exact descent of the endpoint word
to the finite torus.

The explicit Zak decomposition in the source is unitary by Parseval.
Its integer Fourier-mode fibers are continuous, and the trivial fiber
is exactly the stated odd Weyl matrix
$Q_N(e^{2\pi i(kq+lp)})=(-1)^{kl}T_N(l,k)$.
The smooth symbol series converge absolutely, so their quantizations
and bounded exponentials have continuous fibers.
The endpoint translation is an integer shift in these fibers.
A line norm estimate therefore passes from almost every fiber to
every fiber by continuity. This includes the trivial one; no estimate
on distributional combs is assumed.

With the fixed smooth real phase
$$
 G_{r,\beta}=2\pi\beta(-1)^r\partial_q^{r-1}v_0,
$$
the previous bounds yield
$$
 C_{r-1}(\delta)=e^{iQ_N(G_{r,\beta})}
       +O_r(\tau\delta+h^2t^2).
$$
The exact Weyl product estimate
$$
 \|Q_h(b)Q_h(c)-Q_h(bc)\|
 \le2\pi^2h\|b\|_1\|c\|_1
$$
holds on the line and on the finite torus, for all integer Fourier
modes including those that alias.
Comparing the equations for $Q_h(e^{iuG})$ and $e^{iuQ_h(G)}$
and integrating their product error proves
$$
 e^{iQ_N(G_{r,\beta})}=Q_N(e^{iG_{r,\beta}})+O_{r,\tau}(h).
$$
All weighted norms are uniform for $\beta\in[2^{-r},1]$ by smoothness
and compactness. The operator $Q_N(G)$ is self-adjoint, so its
evolution in this comparison is unitary.
There is no expansion of the bounded exponential in $\tau$.

## 5. Positive defect and compression, uniformly in all parameters

Every $G_{r,\beta}$, for $\beta>0$, is a nonconstant real continuous
function on the connected torus. If $e^{iG_{r,\beta}}$ were identically
one, continuity would force $G_{r,\beta}$ to be a constant multiple
of $2\pi$, a contradiction.
Thus its squared defect integral is strictly positive at each
$\beta\in[2^{-r},1]$. That integral is continuous in $\beta$, so
$$
 \mu_r=\min_{\beta\in[2^{-r},1]}
       \int|e^{iG_{r,\beta}}-1|^2>0.
$$
The compact interval has a strictly positive lower endpoint for every
fixed $r$. This is another place where growing $r$ is not covered.

Let $z_\beta=e^{iG_{r,\beta}}-1$.
Exact character orthogonality kills a Fourier mode upon compression
to $P_\chi$ unless $d$ divides both mode indices.
All surviving nonconstant modes therefore belong to the Fourier tail
of size at least $d$, giving
$$
 \left\|P_\chi Q_N(f)P_\chi-\left(\int f\right)P_\chi\right\|
 \le d^{-1}\|f\|_1.
$$
The estimate is uniform in $\chi$; aliased modes are included in
the same tail and cause no exception.
The product estimate applied to $Q_N(z_\beta)^*Q_N(z_\beta)$ gives
$$
 \|Q_N(z_\beta)v\|^2
 \ge\mu_r-C_{r,\tau}(h+d^{-1})
$$
for every unit $v\in P_\chi$, uniformly in $\beta$.
Combining this with the endpoint word error yields, for one
divisor-independent threshold $N_r$,
$$
 \|(C_{r-1}(\delta)-I)v\|\ge\tfrac12\sqrt{\mu_r}.
$$

For an arbitrary output character $\psi$, normalize the translation
$R$ by its input scalar and $B=E_N^*RE_N$ by its output scalar.
The normalized $R$ fixes $v$; each normalized $B$ or its inverse
has residual at most $2\|(I-P_\psi)E_Nv\|$.
Independent scalar phases cancel from the nested commutator.
There are $2^{r-1}$ such $B$ factors, so
$$
 \|(C_{r-1}-I)v\|
 \le2^r\|(I-P_\psi)E_Nv\|.
$$
Consequently the exact all-pair escape constant is
$$
 c_r=2^{-(r+1)}\sqrt{\mu_r}>0,
 \qquad \|P_\psi E_NP_\chi\|\le\sqrt{1-c_r^2}.
$$

## 6. Quantifiers and surviving conclusion

Since $\mu_r\le4$, one has $c_r\le2^{-r}\le1/4$.
The pure-character trace summation therefore has
$\rho_r\lambda>1$, with
$\rho_r=\sqrt{1-c_r^2}$ and $\lambda=3+2\sqrt2$.
The source's exact character permutation, fixed-character count,
and geometric splitting prove the stated complete signed pair error
$O_r(d^{-\kappa_r})$, where
$\kappa_r=-2\log\rho_r/\log\lambda>0$.
All times are included, and the cross-term with complementary traces
is retained in the estimate.

For any fixed positive polynomial exponent, one may choose a single
fixed $r$ with $1/r$ no larger than that exponent.
The threshold and gap then work simultaneously for every allowed
divisor in that range. This gives no uniform assertion for
subpolynomial divisors or for orders increasing with the dimension.

The remaining inter-character trace histories, their CUE comparison,
and every higher fixed-order correlation required by $H_{\rm diag}$
remain unevaluated. The result excludes the specified growing
character-sector mechanism for the original family; it does not
establish universal spectral statistics.
