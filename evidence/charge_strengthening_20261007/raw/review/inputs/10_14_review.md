# Independent review of the growing low-switch off-charge family

## Normalized claim and primary verdict

**Proved as written, relative to the expressly inherited and now independently
accepted analytic inputs.** In the repository's vocabulary: **verified in
stated scope**. This is independent internal review, not an external referee
certificate or analytic formalization.

For the unchanged actual odd-dimensional U_N at fixed tau=10^-80, let
A_U(x)=product_j U_N(x_j,x_(j+1)) for a rooted cyclic coordinate word of positive
length m. For c=y-x modulo N, let s(c) be its number of cyclic switch edges
and t(c)=sum_j c_j modulo N. For every fixed 0<a<b, there are kappa,eta>0
such that, uniformly at aN<=m<=bN and sufficiently large odd N,

|sum_(x,y: s(y-x)<=floor(kappa N/log N), t(y-x)!=0)
       A_U(x) conjugate(A_U(y))| <= C exp(-eta N).

The sum is a once-counted ordered-pair subset of the actual off-charge defect.
For any bounded weight w supported in [a,b], its original N^-2 weighted time
aggregate is O_(a,b,w)(N^-1 exp(-eta N)). It contains the previously accepted
occupation-admissible constant-translation family, so the two families must
not be added as disjoint contributions. The full off-charge defect remains open.

### Exact pins and inherited boundary

- Audited proof: `frozen/low_switch_extension/low_switch_proof.md`, SHA256
  `f8780f4c15d677d9ded64ff29884780526ef86ca5c4b9ed58e770b14b231ad95`.
- Audited candidate manifest: SHA256
  `e55fe9d397368090258c40380f532b778a7b2b47c1ba37fb21dfd887da399e45`.
- Uniform all-translation proof: SHA256
  `c0059f000b4642de174097b3e971d22ba0eac09cdff684289f72ae11db00a7c7`.
- Its independent acceptance: `frozen/accepted_all_translation_review/review.md`,
  SHA256 `7b046dd79bdb000a0d84c150a1949d517fdb2043c3a3c81d6929e8c5e2ae17b4`;
  acceptance manifest SHA256
  `78568d92065e9dcfe314053b42b185999f36a83c05afcaae4be0e95ecdf0a93c`.
- FM-021 position-chain input: SHA256
  `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`.

The analytic input was an explicit assumption at the start of this audit.
The separately delivered acceptance was subsequently read, hash-verified,
and frozen. This final verdict inherits that acceptance; it does not claim
another independent proof of its analytic chain. In particular it inherits
FM-018 O8 at one step, O9 and O11 for the same actual nonlinear
G=S composed with Phi_g^(tau/(2pi)) and its actual normalized invariant area.
The FM-001/FM-006, Markov-coding, Ruelle/Pesin and checked Parry--Pollicott
source-review boundaries remain exactly as recorded in that acceptance.
Neither topological conjugacy alone nor a changed invariant measure is used.

Only the resulting uniform bound on powers of a fixed charge block is used
here. The new changing-charge product estimate is proved below from the run
decomposition. FM-021 supplies the eventual norm bound ||P_N-J_N||<=1/2.
Its analytic chain is inherited, not numerically re-established.

## 1. Dependency graph and proof obligations

1. Actual unitarity -> orthogonal charge decomposition of End(C^N), exact
   blocks, compression norms, doubly stochastic P, and identity annihilation.
2. Exact rooted coordinate expansion -> one full contraction F(c) for each c,
   and a bijection (x,c) <-> (x,y).
3. Identity annihilation -> exact replacement of zero-charge diagonal runs by
   powers of P-J for every nonconstant difference word.
4. Accepted uniform fixed-charge power decay + inherited FM-021 -> decay of
   all diagonal runs, including their zero internal lengths.
5. Contractive switch blocks + N-dimensional trace inequality -> L7.
6. Exact cyclic switch-word counting -> L8 and every whole-fiber subset bound.
7. R_N=floor(kappa N/log N) with kappa=gamma a/8 -> L9 and exponential decay.
8. Occupation balance -> zero modular checksum -> the stated safe off-charge
   subset, exact phase-projector interpretation, and aggregate normalization.

Obligation outcomes: block formula, compression norms, local identity removal,
cyclic orientation, zero internal lengths, r=0/r=1 counts, trace dimension,
subset estimate, entropy constants, checksum direction, injective counting,
constant-family overlap and N^-2 normalization all **passed**. The analytic
diagonal decay is an **accepted inherited input**, with its stated boundaries.
Full signed complement, plateau, stationary-label identification and higher
factorial hierarchy are **out of scope and still open**.

## 2. Exact charge blocks, norms and identity

For E_(d,k)=|k><k+d|, direct conjugation gives

U E_(d,k) U* = sum_(j,c) U_(j,k) conjugate(U_(j+c,k+d)) E_(c,j).

The E_(c,j) form an orthonormal basis for the ordinary Hilbert--Schmidt inner
product. Thus B_(c,d)=P_c Ad(U) I_d has precisely the candidate's formula and
maps H_d to H_c. Ad(U) is unitary and both orthogonal projection and inclusion
have norm one. Therefore every block, including every switch block, has
operator norm at most one. Entrywise absolute-value estimates are unnecessary.

An exact independent finite certificate is sum_c B_(c,d)* B_(c,d)=I_N. For
each fixed c,d, the residual I_N-B_(c,d)*B_(c,d) is the sum of the remaining
Gram matrices, hence is positive semidefinite. This is a true induced-norm
certificate, not an entrywise or numerically estimated spectral norm.

Row and column orthogonality of U give B_(c,0)1=0 when c!=0 and
1*B_(0,d)=0 when d!=0. The directions matter: the first kills a right
constant vector, the second a left one. Also P1=1 and 1*P=1*, so
PJ=JP=J and D_0=P-J obeys D_0 J=J D_0=0. For ell>=1,

P^ell=D_0^ell+J.

For ell=0, the identity is instead P^0=D_0^0=I. There is no extra J term.
In particular D_0^0 is I, not I-J. The candidate correctly handles this
distinction and does not misuse FM-021's convention for P^0-J.

A maximal nonconstant-word zero-charge run, read in the displayed block-product
order, is bordered as

B_(q,0) P^(ell-1) B_(0,q'), q!=0, q'!=0.

For ell>=2 the J summand is zero from either border. For ell=1 no diagonal
factor exists and nothing is removed. Multiple zero runs are handled one
at a time. This proves fiberwise identity removal without inserting any
coordinate-dependent mask. Only the all-zero constant word changes, by
Tr P^m-Tr D_0^m=Tr J=1 for m>=1. Nonzero constant words are unchanged.
Equivalently the full operator Ad(U) minus its reducing global identity
projector is a contraction; this alone does not replace the fiberwise check.

## 3. Rooted contractions and oriented runs

The ordinary trace of the displayed cyclic product is

F(c)=sum_(x_0,...,x_(m-1)) product_j
 U_(x_j,x_(j+1)) conjugate(U_(x_j+c_j,x_(j+1)+c_(j+1))).

Thus it is exactly sum_x A_U(x) conjugate(A_U(x+c)). Every coordinate tuple
including every repeated tuple occurs once. The indices are rooted at the
fixed positions 0,...,m-1; taking a cyclic rotation to estimate the trace
does not add the rotated word as another representation of the same pair.
Conversely each ordered pair has exactly one difference tuple c=y-x.

For a nonconstant word, choose a start immediately after a switch. Let its
cyclic run labels be q_1,...,q_r and lengths ell_1,...,ell_r>=1. The trace,
after identity removal, is the trace of

D_(q_1)^(ell_1-1) B_(q_1,q_2) ...
D_(q_r)^(ell_r-1) B_(q_r,q_1).

There are exactly r switch blocks and sum_i(ell_i-1)=m-r diagonal steps.
This order preserves the source/target charge orientation. No commuting of
unrelated blocks or power bound for changing offsets is asserted.

Choose C>=1 and gamma>0 from the accepted uniform power input, decreasing
gamma to min(gamma,log 2). Then ||D_q^h||<=C exp(-gamma h) for every charge
q and h>=0, eventually uniformly in odd N. For q=0 use FM-021 and for h=0
use C>=1. Submultiplicativity and |Tr M|<=N||M|| give exactly

|F(c)| <= N C^r exp[-gamma(m-r)]
       = N exp(-gamma m) K^r, K=C exp(gamma).

The product is still one N by N matrix. A factor N per run would be an
unjustified weakening; no such factor appears in L7. The additional powers
of N below count distinct charge words, not internal trace indices.

## 4. Exact switch count and the whole-fiber subset estimate

For r=0 there are precisely N constant words. For r>=1 choose the exact
set of r switch edges in the labeled m-cycle. These define r nonempty cyclic
runs, so the number of assignments is the number of proper N-colorings of
a labeled r-cycle. With K_N the N by N all-ones matrix,

number of words with exactly r switches
 = binom(m,r) Tr[(K_N-I)^r]
 = binom(m,r)[(N-1)^r+(-1)^r(N-1)].

The trace formula also gives zero for r=1 and N(N-1) for r=2, where the
two cycle edges impose the same inequality. There is no division by r or
extra marked-cut multiplicity. In particular this count is at most
binom(m,r)N^r, exactly as needed in the candidate. The formula is valid for
1<=r<=m, including m=1; a nonconstant cyclic word indeed cannot have one switch.

For constant words the all-zero contribution is 1 plus its centered trace;
the other N-1 traces each obey C N exp(-gamma m). Hence their combined
centered absolute bound is C N^2 exp(-gamma m). Summing L7 over nonconstant
words proves L8. It also proves the same bound for every subset of difference
words that excludes the all-zero word, since one can sum absolute values
of the full complex numbers F(c). A subset need not be invariant under c->-c.

This argument does not authorize an arbitrary restriction on x inside a
fiber F(c). In particular it cannot keep only the off-charge terms of a
checksum-zero fiber. The distinction is essential and retained in the proof.

## 5. Entropy constants and normalization

Let gamma denote the possibly decreased exponent above and set
kappa=gamma a/8. For fixed K,b and sufficiently large N,
log(K b N^2)<=3 log N and K b N^2>=1. Also R_N<m eventually, since
R_N/N<=kappa/log N and m/N>=a. The switch contribution in L8 is bounded by

N(R_N+1) exp[-gamma aN+3R_N log N]
 <= N(R_N+1) exp[-5gamma aN/8].

The polynomial factor can be absorbed in exp(gamma aN/8), leaving
C' exp(-gamma aN/2). The constant-word term C N^2 exp(-gamma aN) is bounded
by the same envelope. Thus eta=gamma a/2 works after an N-independent
constant enlargement and a noneffective startup threshold. The floor only
improves the estimate. The choices depend on fixed a,b and the fixed actual
map; there is no tau->0 uniformity or numerical threshold claim.

There are at most (b-a)N+2 relevant integer powers m. Multiplying their
uniform bound by ||w||_infinity and the prescribed N^-2 gives
O_(a,b,w)(N^-1 exp(-eta N)). No missing time-count or trace-dimension factor
remains. The argument estimates signed full contractions before taking
absolute values, and is not an absolute individual-path estimate.

## 6. Checksum mask, phase projector and overlap

Equal occupation vectors imply equal integer sums of the chosen coordinate
representatives. Their difference modulo N is exactly t(y-x). Therefore
t(y-x)!=0 implies occupation mismatch. The converse fails even inside one
nonconstant difference fiber. At N=3,m=2,c=(1,2):

- x=(0,1), y=(1,0) is balanced;
- x=(0,0), y=(1,2) is off-charge;
- both have checksum zero and two switches.

For the independent dense complex unitary, their nonzero weights are,
respectively, 120448/3258025 and
(644512+300576 i)/16290125. Thus the failure of the converse is not supported
only on zero-weight paths.

Independent coordinate phases multiply A_U(x) by product_j exp(i theta_(x_j)).
Integration of each phase kills a pair precisely when its occupation
vectors differ. Subtracting this balanced projection from |Tr U^m|^2 gives
the exact off-charge defect. No phases are imposed on or substituted for
the actual quantizer. Since checksum is determined by c alone, the proposed
mask selects whole exact contractions and excludes the all-zero word.

For a constant c, checksum is m c modulo N. It is nonzero precisely when
ord(c)=N/gcd(c,N) does not divide m. This is exactly the accepted safe
constant-translation mask, including composite N and divisible-time empty
cases. The new family contains that family and must replace or enlarge it,
not be added to it as a disjoint deletion. It is genuinely larger eventually:
the difference word (1,0,...,0) has checksum 1 and two switches for m>=2,
and lies in the new family once R_N>=2, while not being constant.

The checksum-zero low-switch family can contain both balanced and off-charge
pairs. The unmasked low-switch contraction is 1+O(exp(-eta N)); its safe
checksum-selected off-charge part is O(exp(-eta N)). Neither fact separates
the two occupation pieces of the checksum-zero remainder.

## 7. Independent finite evidence and reproduction

`check_independent.py` was written from the definitions and imports no author
or repository verifier. It uses exact Gaussian-integer numerators and common
positive denominators for two dense complex unitaries obtained as products
of two Householder reflections and diagonal fourth-root phases. It explicitly
constructs Ad(U) by applying U E U* to all matrix units, independently of
the proposed block-entry formula.

Finite coverage:

- N=3, all m=1,...,5; N=5, all m=1,...,3;
- 82,704 literal ordered-pair controls and 518 full difference contractions;
- exact full-superoperator unitarity and compression Gram sum certificates;
- exact global identity-projector reduction and every restricted fiber check;
- 132 long nonconstant zero-charge runs and 300 singleton zero-charge runs;
- all oriented cyclic run products and all cyclic cut orientations in range;
- 494 genuinely nonreal contractions; dropping conjugation is detected in
  67 explicitly tested cases;
- every low-switch threshold R=0,...,m compared with the direct pair mask;
- independent phase-character versus occupation projection and both types
  of checksum-zero witnesses;
- exact switch counts through N=2:m<=8, N=3:m<=7, N=4:m<=6, N=5:m<=5,
  N=6:m<=4 and N=9:m<=3, including composite translation orders;
- a literal identity-unitary negative control: N=3,m=4 has safe constant
  family sum 6, showing unitarity alone does not imply analytic decay.

The original author checker is replayed separately from a copied source.
Its result is compared to the pinned author result after removing only the
elapsed-time field. The independent normal and optimized Python runs must
produce byte-identical results. An injected failure must still fail under
Python -O; correctness checks do not disappear with assertions disabled.

Reproduction commands, from this review directory:

    python3 run_checks.py
    python3 validate_manifest.py computation_manifest.json --root .

The version-2 computation manifest records actual subprocess commands,
before/after input hashes, declared result hashes, logs, Python version and
resource caps. POSIX address-space, CPU-time and CPU-affinity caps are applied;
numerical-library thread caps are cooperative. No external packages, random
sampling, floating tolerance, rescaled tau experiment or actual-U numerical
simulation enter these finite controls.

Finite checks support the stated algebra only. The uniform N-limit follows
from the proof and accepted analytic input, not the observed test count.

## 8. Exact remaining gap and strongest safe conclusion

No missing implication was found in L1-L9 relative to the accepted uniform
charge-power input and inherited FM-021. No proof edit is required. The sharper
exact counting formula is supplementary verification; the candidate's looser
count already suffices.

The strongest safe conclusion is the stated exponentially small once-counted
checksum-nonzero low-switch family, and its normalized compact positive-band
aggregate, for the unchanged actual fixed-coupling map. Almost all general
high-switch pairs and the off-charge portion of checksum-zero fibers remain
uncontrolled. There is no full signed defect, plateau, stationary-label
N-torsion or higher factorial conclusion. TRACE-005 and BGS remain open.

This audit made no canonical, publication, commit or remote changes. The
canonical working tree was already dirty due to concurrent work; its observed
status and source snapshots are provenance, not an assertion that the entire
repository was frozen or independently re-audited.
