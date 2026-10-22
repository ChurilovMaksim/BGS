# Independent semantic/code audit: seven-primary finite Lean certificate

## Claim and verdict

**Primary verdict: computationally verified only in the stated finite range.** The semantic/code promotion gate passes for the 22 executable assertions in the exact source identified below. No defect was found in the array algorithms on their actual canonical-input domain. This is not a formal proof of the general array-to-polynomial interpretation, Rabin's theorem, the universal root-order exclusion, or the actual commutant theorem.

Reviewed source: `/workspace/shared/bgs_seven_primary_lean/SevenPrimary.lean`, SHA256 `431e5d111238a962ec2bb994f21d4cb1ac17df250379651aa4e8fcd065604cb4`.
Frozen mathematical input: `unramified_actual_commutant.md`, SHA256 `47b2692f034a23888d4223e73120a685609a6ca58c2a983293310bc735e42d4f`.

The review was performed independently of the implementation author. README and SEMANTICS were treated as claims to inspect, not as evidence establishing correctness. All writes are in this separate review directory; no canonical or certificate source was edited.

## Dependency graph and exact Lean statements

Frozen numerator/norm coefficients and factor lists → external literal binding → seven Lean Entry literals → array multiplication/remainder/gcd/Frobenius predicates → 22 `native_decide` theorems.

For each i=0,...,6, Lean proves exactly:

- `productCheck entryi = true`: multiply the singleton unit array by each factor, repeated exactly its multiplicity, and compare the final array with the polynomial literal.
- `factorCheck entryi = true`: every listed multiplicity is positive and every factor passes `rabinChecks`.
- `degreeCheck entryi = true`: each coefficient-array size minus one is nonzero modulo 42.

The remaining theorem is `order49Check = true`: 5^42 mod 49 equals 1 and no exponent 1 through 41 has that property. Exponent zero is expressly skipped. This is sufficient finite arithmetic to identify the order as 42; the abstract group-order statement is not the theorem's Lean type.

There are 46 factor-list occurrences, not necessarily 46 globally distinct polynomials. Their degrees and multiplicities are recorded in `result.json`. Polynomial degrees are 126,134,143,153,164,176,828. The largest two factor degrees are 246 and 366. Multiplicity-weighted degree sums and units were independently verified.

## Semantic obligations

**Representation — passed on actual domain.** A canonical array contains residues 0,...,4 and either is empty or has nonzero last coefficient. Its interpretation is the ascending coefficient sum. Empty is zero. `trim` tests the current final position at most the original length, so it removes exactly the trailing zero suffix. It does not normalize arbitrary Nat coefficients modulo 5. All seven polynomial literals, units, and 46 monic factors satisfy the required canonical constraints.

**Scalar arithmetic, addition/subtraction — passed.** There is no standalone general add/sub operation to audit. Multiplication accumulates `(r[i+j]+a[i]*b[j])%5`. Remainder subtraction uses `(r[i]+5-(c*b[j])%5)%5`; the subtracted number is at most 4, so Nat's truncated subtraction is never activated. `subX` extends arrays of size below two with zeros, subtracts one from coefficient 1 as `(r[1]+4)%5`, then trims. Empty and constant inputs are handled correctly.

**Multiplication — passed.** The allocated length a.size+b.size−1 contains every i+j index. Both loops visit every coefficient pair exactly once. Empty input short-circuits to zero; trim produces the canonical result. Arbitrary precision Nat prevents machine overflow in source semantics.

**Inversion/remainder — passed with nonzero canonical divisor.** For a nonzero residue b, b^3 mod 5 is its inverse. At descending position n≥d, the algorithm subtracts `leading(r)*inverse(leading(b))*X^(n−d)*b`. Every accessed index n−d+j lies in [0,n] and within the original dividend allocation. The coefficient at n is canceled and no higher coefficient is disturbed. The loop processes every possible position down through d, leaving degree below d. No dynamic array shortening occurs until the end. Nonmonic divisors arising during Euclid are supported. A nonzero constant divisor leaves zero. When the divisor has larger degree, the dividend is simply trimmed.

**Euclid — passed on actual domain.** Each nonzero canonical divisor produces a remainder of smaller degree. There can be at most one initial degree-order swap, then strict descent; size(a)+size(b)+1 fuel is more than sufficient. The final nonzero u is multiplied by inverse leading coefficient to give monic gcd. If fuel is exhausted while v is nonempty, the result is empty and cannot equal the required singleton [1]. Actual Rabin calls begin with a nonzero positive-degree f, so the final u is nonempty, including when the second input is zero.

**Frobenius — passed.** Inserting four zeros between coefficients maps sum a_i X^i to sum a_i X^(5i). Over GF(5) this is precisely the fifth power, since a_i^5=a_i and cross terms vanish. Modular reduction is the checked division algorithm above. Repetition starts at X mod f; after loop index k, h represents X^(5^k) mod f.

**Rabin predicate — passed as an executable predicate.** Input guards reject zero, constants, nonmonic encodings, trailing-zero encodings and coefficients ≥5. The half-open loop [1:d+1] visits precisely 1,...,d. `primeTrial` rejects 0 and 1 and checks every possible divisor 2,...,p−1 for p≥2. The condition d%k=0 and primeTrial(d/k) selects exactly k=d/p for each prime p dividing d. `gcd5 f (subX h)=[1]` is the required coprimality test, and the final equality h=x is the full Frobenius congruence. Degree-one factors correctly need no proper-divisor gcd test; X itself passes despite zero constant term. The final congruence also excludes repeated factors through the squarefreeness of X^(5^d)−X in the usual mathematical criterion.

**Products, units and degrees — passed for these entries.** The units are nonzero residues, every multiplicity is positive, and every factor is canonical monic positive degree. `degreeCheck` alone would not establish those properties, and neither `productCheck` nor `factorCheck` validates arbitrary Entry metadata in isolation. Their conjunction plus literal inspection has the advertised meaning for these seven entries. No claimed degree, JSON Boolean flag, or stored Rabin-cut list enters Lean's decision.

## Malformed-input limits

The low-level operations are not a public verified API for arbitrary arrays. In particular, `rem5 a #[]` returns a unchanged by convention; a trailing-zero nonempty divisor is invalid; `trim` does not reduce residue encodings; and `gcd5 #[] #[]` attempts a bang-index lookup in an empty final u and is outside the audited domain. None of these cases is reachable in the seven factor certificates. The guarded Rabin entry point rejects malformed factor encodings before arithmetic. Empty factor lists make all-list predicates vacuous, and a zero or out-of-range unit is not explicitly rejected by `productCheck`; the actual literal lists and units avoid those cases. These are scope restrictions, not counterexamples to the stated finite theorems.

## Independent computation and provenance

`audit.py` independently parses the actual Lean literals, enforces ordered entry indices 0,...,6, checks all frozen-input hashes and available source-review bindings, compares numerator expressions and norm coefficients with the embedded arrays, and checks factor coefficients/multiplicities/units against the frozen certificate. Its calculations use coefficients, not the stored pass flags. With SymPy 1.14.0 it independently verifies every factor's irreducibility, all seven products, all factor degree exclusions, the weighted degree sums and all exponents needed for order 42. This fresh replay passed.

The same script generates `IndependentControls.lean` by copying the exact implementation prefix from the hash-checked source, followed by 1,896 reference assertions: all 780 monic polynomials of degrees 1 through 4 tested against SymPy irreducibility; 220 deterministic random input pairs, each checking multiplication, remainder, monic gcd, Frobenius and subtraction of X against SymPy (including nonmonic and constant divisors and zero dividends); 11 malformed/reducible negatives; and five multiplicity/trim/subX boundary controls. This is additional adversarial evidence, not a universal correctness proof. The fresh control compilation passed with exit code 0 in 13.891970 seconds (995424 KiB peak child RSS); its log is empty. See `controls_receipt.json` for command and source/log hashes.

The original full build was not repeated. The existing successful build receipt records 136.579852 seconds, exit code zero, and the exact reviewed source hash. I freshly verified every file digest in `artifact_hashes.json`, including the build log and receipt, and inspected all 22 printed axiom lists. No user-declared axiom, sorry/admit placeholder, unsafe implementation override, or precomputed certificate Boolean is present in the Lean source. The printed dependencies are standard `propext`/`Quot.sound` where used, plus the per-theorem generated `native_decide` axiom. Trust in native compilation/evaluation is explicit. This must not be described as pure small-kernel arithmetic reduction.

The optional compatibility shim was inspected: its sole interception redirects a readlink of /proc/<own-pid>/exe to /proc/self/exe and otherwise delegates unchanged. It does not replace polynomial code or decision results.

## Remaining formal gaps and safe publication language

Generic correctness lemmas connecting arrays to abstract GF(5)[X], termination/correctness of the fuelled Euclidean algorithm, the Rabin equivalence, finite-field/minimal-polynomial and multiplicative-order arguments, and the universal root-order exclusion are not formalized here. Neither are the bounded-polynomial derivations, resultant/norm interpretation, two-row commutant argument, residue-field construction, rank lift, N49 base, tail argument, or BGS. Their prior external reviews are not upgraded to Lean proofs by this audit.

Safe statement: “The seven-primary finite polynomial certificate has compiled Lean `native_decide` proofs of its explicit array predicates, independent coefficient binding and GF(5) replay, and an independent semantic/code audit. The interpretation by generic polynomial and finite-field theorems remains mathematical rather than formalized in Lean.”

The semantic review gate for that wording is closed by this review. The cheapest next formalization step is to prove the canonical-array remainder and gcd interpretation and a Rabin-soundness bridge, rather than adding more finite examples or presenting compilation alone as semantic proof.
