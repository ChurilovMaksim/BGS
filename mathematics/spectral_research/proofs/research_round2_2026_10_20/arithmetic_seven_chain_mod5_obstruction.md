> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_seven_chain_mod5_obstruction.md`. Embedded SHA256: `5e19c3d9569a98f8583b10f6b044b876d5009b47d41c57f61d4554bfd77e2acc`.
> [Thematic guide](../../topics/arithmetic.md).

# A verified failure of first-confluent dominance in the actual N=49 family

Research continuation, 20 October 2026. This is a rigorous finite
obstruction to one proposed extension of the p-adic proof. It is
not an obstruction to H_diag and not a repeated-eigenvalue claim.

## 1. Precise conclusion

Use the valuation v extending 1+2i, normalized by v(1+2i)=1, so
v(5)=v(omega)=1. For the actual N=49 Jacobi paths, the candidate
first-confluent coefficient F_st of the mixed two-by-two minor,
defined in equation (2.5) of the checkpoint, satisfies

$$
\boxed{v(F_{st})\ge1}
\tag{1.1}
$$

for seven distinct pairs of actual eigenvalues for each of the
three path pairs

$$
(s,t)=(0,6),(1,5),(2,4).
\tag{1.2}
$$

Thus the proposed sufficient estimate v(F_st)<1 is false even
within the exact original family. A second-order term can have
the same lower valuation 2 as omega F_st. One cannot discard
that term using the previous bounds.

This does not assert that the full minor vanishes. In particular,
N=49 already has a separate exact certificate of simple U_N
spectrum. It is the proposed first-confluent proof of a stronger
minor property that encounters the cancellation in (1.1).

## 2. A structural congruence of the seven paths

The following identity holds for every odd N=7n. Reflection of
the torus coordinate x to -x sends

$$
(s,j)\longmapsto(6-s,n-1-j).
\tag{2.1}
$$

Let R reverse a path and C=diag((-1)^j) change the sign on alternating
sites. The exact off-diagonal coefficients are invariant under this
reflection, whereas

$$
200V(q)\equiv2r(q)\sin(2\pi q)\pmod5
\tag{2.2}
$$

is odd in q. Consequently

$$
\boxed{L_{6-s}\equiv-CRL_sRC\pmod5.}
\tag{2.3}
$$

The congruence means that corresponding matrix differences belong
to 5 times the valuation ring. The diagonal terms not shown in
(2.2) are 200cos(14pi q)+20r(q)-20, all divisible by 5. Reflection
leaves b unchanged because r is even and 2h=1 modulo N; the
alternating-sign conjugation supplies precisely the required minus
sign for the off-diagonals.

For the monic degree-n characteristic polynomial P_s of L_s,
(2.3) gives

$$
P_{6-s}(-X)\equiv(-1)^n P_s(X)\pmod5.
\tag{2.4}
$$

This congruence is not an exact chiral symmetry in characteristic
zero. The even part of the prescribed diagonal potential survives
there, and is essential to later terms.

## 3. Minimal exact finite calculation at N=49

The residue of i at 1+2i is 2 in F_5. A primitive 49th root is
represented by x in

$$
\mathbb F_5[x]/(1+x^7+x^{14}+\cdots+x^{42}).
\tag{3.1}
$$

This quotient is a field. The order of 5 modulo 49 is 42, which
the script checks by successive multiplication. The Frobenius
orbit of a primitive 49th root therefore has 42 elements, so its
minimal polynomial is the displayed degree-42 cyclotomic
polynomial.

The seven degree-7 characteristic polynomials are computed by the
explicit monic Jacobi recurrence

$$
P_{j+1}(X)=(X-d_j)P_j(X)-b_{j-1}^2P_{j-1}(X),
\quad P_0=1,\quad P_1=X-d_0.
\tag{3.2}
$$

All seven Euclidean-algorithm calculations give

$$
\gcd(\overline P_s,\overline P_s')=1.
\tag{3.3}
$$

The same calculation additionally finds
gcd(overline P_s,overline P_t)=1 for s!=t. Only (3.3) and the
structural congruence (2.4) are needed for (1.1).

The supplied program uses pure integer arithmetic. Field
multiplication is polynomial multiplication followed by reduction
by the explicit polynomial in (3.1). A packing radix 2^16 is
used for convolution: every intermediate convolution coefficient
is at most 42*4*4=672, so no digit can carry into its neighbour.
Every field inverse is checked by multiplication. Polynomial
remainders and the Euclidean algorithm are written explicitly in
the source. The zero gcd degrees in the JSON are therefore
reproducible exact identities, not eigenvalue approximations.

The program also independently checks (2.4) for the three pairs
(1.2), and verifies by direct substitution that the reduction of
F_st/(z_s-z_t) is a nonzero scalar times mu_s+mu_t.

## 4. Lifting the cancelling pairs to actual algebraic eigenvalues

Choose any actual algebraic eigenvalue mu_s of one of paths
s=0,1,2. It is integral because L_s is integral and its
characteristic polynomial is monic. By (3.3),
P_s'(mu_s) is a valuation unit.

Put t=6-s and a_0=-mu_s. Equations (2.4) and (3.3) give

$$
v(P_t(a_0))\ge1,\qquad v(P_t'(a_0))=0.
\tag{4.1}
$$

The Newton sequence a_(j+1)=a_j-P_t(a_j)/P_t'(a_j) stays integral.
Taylor expansion over the valuation ring shows that the error
valuation at least doubles at every step and that the derivative
remains a unit. Its increments have valuations tending to infinity,
so the sequence converges in the completed algebraic closure to a
root mu_t of P_t with

$$
\boxed{v(\mu_s+\mu_t)\ge1.}
\tag{4.2}
$$

This root is one of the original algebraic eigenvalues: P_t
already splits into its finitely many linear factors over the
algebraic closure, and substituting the limit into that finite
factorization forces equality with one of those roots.
Distinct roots of P_s have distinct reductions by (3.3).
Their matched roots of P_t are therefore distinct. Hence this
constructs seven pairs for each of (1.2).

The Newton argument proves the stronger distance estimate (4.2)
directly. No unproved assertion about a fractional or unramified
valuation of the eigenvalue field is being used.

## 5. Evaluation of the first-confluent coefficient

For 49 dividing N, use the notation of the checkpoint:

$$
z_s=\zeta_7^{\overline4s},\qquad
\chi=\zeta_7^{\overline4},\qquad
\eta_B=e_N(\overline8(2n-7)).
$$

For t=6-s, the identities z_s z_t=chi^(-1) and
eta_A=eta_B chi^2 are exact. Reflection also gives
b_(t,n-2)=b_(s,0) and b_(t,0)=b_(s,n-2). Thus the exact
four-term expression simplifies to

$$
F_{st}=(z_s-z_t)\eta_B
\left[
\frac{(\mu_s+\mu_t-D_0)z_s^{-3}}{b_{s,0}}
-\frac{(\mu_s+\mu_t-D_1)\chi^3z_s^3}{b_{s,n-2}}
\right],
\tag{5.1}
$$

where

$$
D_0=d_{s,0}+d_{t,n-1},\qquad
D_1=d_{s,n-1}+d_{t,0}.
$$

At either corresponding position q and -q,

$$
200V(q)+200V(-q)
 =400\cos(14\pi q)+40r(q)-40.
\tag{5.2}
$$

Both D_0 and D_1 consequently have valuation at least 1.
For N=49 the nonzero b's are valuation units, since their
root-of-unity factors have order prime to 5. Equations (4.2),
(5.1), and (5.2) prove (1.1).

The mechanism is now explicit: the modulo-5 reflected spectral
pairing forces the first coefficient to be small at the same
arithmetic place at which omega is small. Terms of the next
order in omega and the first surviving even diagonal terms must
be kept together.

## 6. Exact boundary of the result

The calculation does not produce a repeated eigenvalue of U_49,
a zero overlap minor, a lower bound for Delta_(k,N), or an
infinite counterexample to H_diag. It disproves only the uniform
first-coefficient estimate v(F_st)<1 that would otherwise have
completed this particular dominance argument.

The next unproved step is a noncancellation statement after combining
omega F_st with the omega^2 coefficient at their actual joint
valuation. Higher-dimensional repeated or mixed spectral blocks
require a corresponding argument. No result from a generic phase
or a nearby matrix is transferred to the fixed omega.

## 7. Files and reproducibility

| File | SHA-256 |
|---|---|
| arithmetic_seven_chain_discriminant_checkpoint.md | eee2b4caa27349a81e5cf3113d53ff1f88164e44b748c2eb99754f6e07fc6a8f |
| arithmetic_seven_chain_mod5_probe.py | d0ee9caff9707778c84c8e55568ef3f3ce602d22da339942acd94e7bc18fd9eb |
| arithmetic_seven_chain_mod5_probe.json | 1fbc20d0fcac661a5db4e6677394e63fd784035c95bae1c585ae2eb96222c623 |

The JSON additionally records the exact coefficients of the
three degree-7 cancelling gcds. The script may be rerun directly
with Python 3 and has no third-party dependencies.
