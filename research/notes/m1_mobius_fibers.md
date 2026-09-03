# M1 note — Möbius fibers, character orders and exceptional divisors

The historical fiber map is

`v_d(u)=((d-1)u+1)/(d+1-u)`.

Its projective matrix is `[[d-1,1],[-1,d+1]]`.  Both its determinant and the resultant of numerator and denominator equal `d^2`.  Thus the Möbius transformation itself degenerates exactly at `d=0`.  Wolfram symbolic evaluation independently confirms the zero `u=1/(1-d)`, the pole `u=d+1`, and the special forms listed below.  The old proof text gave the pole as `d-1`; that was incorrect.

## The character group that actually appears

Put `L=N-1=K m` and choose a primitive root `g`.  Write `a=g^ell` with `ord(a)=K`.  Then

`gcd(ell,L)=m`.

For the standard character `chi_k(g)=exp(2 pi i k/L)`, the condition `chi_k(a)=1` is equivalent to `K | k`.  Hence

`S=H^perp={chi_(K j): j mod m}`.

If `rho=chi_K`, then `rho` has exact order `m`.  This is the character order relevant to a Weil-type perfect-power exclusion.  The historical phrase “perfect K-th power” confuses the torus order `K` with the annihilator-character order `m`.

## Generic divisor

Write a twist pair as `(rho^r,rho^s)`, with `r,s` modulo `m`, and combine the characters into

`R_(r,s,d)(u)=u^r v_d(u)^s`.

For `d` outside `{0,1,-1}`, the four support points are distinct:

- `0`,
- infinity,
- `alpha_d=1/(1-d)` (zero of `v_d`),
- `beta_d=d+1` (pole of `v_d`).

The divisor is

`div R = r[0] - r[infinity] + s[alpha_d] - s[beta_d]`.

If this rational function were an `m`-th power, every valuation would be divisible by `m`.  Since `0<=r,s<m`, this forces `r=s=0`.  Therefore **there is no nontrivial perfect-power exception on a generic fiber**.

This argument is only the divisor obstruction needed before invoking a character-sum bound; the exact theorem and its constant still have to be cited and checked against our omitted points/conventions.

## Special fibers

### `d=1`

`v_1(u)=1/(2-u)` and

`div R = r[0] + (s-r)[infinity] - s[2]`.

Divisibility by `m` again forces `r=s=0`.  No new nontrivial twist family appears.

### `d=-1`

`v_{-1}(u)=2-1/u=(2u-1)/u` and

`div R = (r-s)[0] - r[infinity] + s[1/2]`.

Again `r=s=0` is forced.

### `d=0`

After cancellation, `v_0(u)=1` in the function field, so

`R_(r,s,0)(u)=u^r`.

This is an `m`-th power exactly when `r=0 mod m`; `s` is unrestricted.  Thus the exceptional family is precisely

`psi_1 = 1`, `psi_2 arbitrary`.

For nontrivial `psi_2`, the implemented fiber sum has

`A_(1,psi_2)(0)=N-2`,

matching the complete Python/C++ scan at `N=53` and `N=199`.

## Consequence for M1

The perfect-power/fiber problem is now reduced to one explicit exceptional fiber rather than an unspecified genericity claim:

1. extract `d=0` exactly;
2. keep `d=±1` as low-support but nondegenerate special cases;
3. apply a verified rational-function character-sum theorem only to the remaining generic fibers;
4. then address the genuinely harder problem: cancellation of the full cross-Gram sum.

This classification does **not** prove M1.  It removes one previously hidden failure mode and gives a precise hypothesis boundary for the next analytic estimate.
