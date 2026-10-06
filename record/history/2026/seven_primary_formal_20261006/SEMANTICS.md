# Executable semantics and self-review

This is an implementation explanation and author self-review, not the required
fresh semantic promotion audit and not a general Lean correctness proof.

Arrays represent sum a[i] X^i with canonical residues 0..4 and no terminal zero.
The empty array represents zero. Addition/subtraction and multiplication reduce
modulo5 after each scalar operation. `trim` removes terminal zero coefficients.
`inv5 a = a^3 mod5` is inversion for each nonzero GF(5) element.

`rem5` scans all coefficient indices from highest to lowest. At n>=deg b it
subtracts leading(r)*inverse(leading(b))*X^(n-deg b)*b. Thus the current leading
term vanishes before the next index. The algorithm permits nonmonic divisors,
which occur in Euclidean gcd. All actual callers give canonical, nonzero divisors.
An empty divisor returns the dividend; this is only a total-function convention,
not a claimed division operation by zero.

`gcd5` runs Euclid and normalizes its final nonzero result to monic. Its explicit
fuel is size(a)+size(b)+1, greater than the number of strict degree descents for
well-formed inputs. Fuel exhaustion with nonzero v returns [], so it cannot
silently pass the required comparison to [1]. The tested inputs always begin
with a positive-degree monic polynomial.

`frob5` inserts four zeros between consecutive coefficients, then reduces. Over
GF(5), this is the fifth-power map. `subX` subtracts X even if the remainder has
size0 or1. `rabinChecks` rejects empty, constant, nonmonic and non-residue inputs.
It iterates Frobenius from X mod f exactly d times; at each k|d for which d/k is
prime it performs gcd(f,h-X)=1. A trial-division predicate computes primality
inside Lean, and thus no supplied cut list is trusted. The final remainder must
equal X mod f. These are precisely the computational hypotheses of the standard
Rabin criterion, but that general criterion is not proved in this package.

`factorCheck` also rejects zero multiplicity. `productCheck` computes the full
product, including unit and repetitions. `degreeCheck` separately checks each
listed degree modulo42. Exact lists and multiplicities are bound to reviewed
inputs by the separate source-literal parser. No JSON pass flag, stated degree,
stated prime divisor, or precomputed Frobenius identity is used as evidence by
Lean. Degree is actual coefficient-array size minus1.

Smoke.lean/log records positive controls, reducible/repeated-factor negatives,
and malformed-input rejection. These controls are limited tests; they do not
substitute for a fresh algorithmic and dictionary audit before promotion.
