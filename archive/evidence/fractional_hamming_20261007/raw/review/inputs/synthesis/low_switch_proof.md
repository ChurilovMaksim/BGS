# A growing low-switch family inside the actual deterministic off-charge defect

Author corollary candidate, 7 October 2026. Actual U_N, tau=10^-80. No canonical
edit. This depends on the separately pinned all-translation finite-power
candidate and inherited FM-021 position mixing; independent review pending.
No full off-charge, plateau, or higher factorial conclusion follows.

## L1. Target and first counterexample tests

For two cyclic coordinate words x,y of length m define their difference word
c_j=y_j-x_j in Z/N, its switch count
s(c)=#{j:c_j!=c_(j+1)}, and its modular checksum t(c)=sum_j c_j in Z/N.
The exact once-counted family studied here consists of all pairs with
s(c)<=R_N and t(c)!=0. These conditions depend on the whole difference word,
not on a marked cut or a coordinate mask imposed inside a contraction.

Cheapest tests: a cyclic difference word cannot have exactly one switch;
charge balance must force t(c)=0; and removing the identity inside a run with
c=0 must be killed by adjacent off-diagonal charge blocks. Test all three
before estimating the number of runs. No assertion that t(c)=0 implies
occupation balance is permitted. Constant-translation pairs are included,
so they must not be added again as a disjoint family.

Claim: for every fixed 0<a<b, there exist kappa,eta>0 such that, with
R_N=floor(kappa N/log N), uniformly for aN<=m<=bN,

 |sum_(x,y:s(y-x)<=R_N, t(y-x)!=0) A_U(x)conjugate(A_U(y))|
                           <= C exp(-eta N).                  (L1)

Every pair in L1 is off-charge. Thus its original N^-2 compact-band aggregate
also tends to zero exponentially. R_N grows with N, rather than being a
fixed encounter or block cutoff. The complete complement remains open.

## L2. Exact full coordinate-difference blocks

Decompose End(C^N), with ordinary HS inner product, as the orthogonal sum
H=direct_sum_(c in Z/N) H_c, H_c=span{|j><j+c|:j in Z/N}.
The matrix blocks of the unitary superoperator T=Ad(U_N) are

 B_(c,d)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+d)).                 (L2)

Each block has induced norm at most one. In particular B_(c,c) is the exact
translation kernel already studied; B_(0,0)=P_N=|U_N|^2.
For every difference word c=(c_0,...,c_(m-1)), direct contraction gives

 F(c)=Tr[B_(c_0,c_1) B_(c_1,c_2)...B_(c_(m-1),c_0)]
     =sum_x A_U(x)conjugate(A_U(x+c)).                         (L3)

All x, including repetitions, occur once. Conversely each pair x,y determines
one c=y-x. Therefore any sum over a set of difference words is an exact
once-counted ordered-pair subset, without cut multiplicities.

## L3. Exact isolation of the identity, with no unproved mask cancellation

Let 1 be the constant vector in coordinate space and J=11*/N.
Unitarity gives exactly

 B_(c,0)1=0 for c!=0,       1*B_(0,d)=0 for d!=0,              (L4)
 P1=1,                     1*P=1*.

Equivalently the sole global identity vector belongs to H_0 and is reducing
for T. Remove its rank-one projector. The new diagonal blocks are

 D_0=P-J,  D_c=B_(c,c) for c!=0,                              (L5)

while every c!=d block is unchanged. Call these modified blocks tilde B.
For a nonconstant difference word c, replacement by tilde B in L3 is EXACT.
Indeed every maximal zero-charge run is bordered by off-diagonal blocks.
Its P^ell factors may be expanded as D_0^ell+J when ell>=1, and each J term
is annihilated at either border by L4. If ell=0 there is no factor to replace.
Thus no coordinate-dependent canonical choice or occupation filter has been
inserted. For constant words, only c=(0,...,0) changes, and precisely

 F(0,...,0)=Tr P^m=1+Tr D_0^m.                               (L6)

For a nonzero constant c the blocks are unchanged. This is the exact source
of the identity contribution 1 in the unmasked low-switch sum.

## L4. Uniform diagonal-run decay and switch counting

The pinned all-translation candidate supplies C>=1 and gamma>0 such that
||D_c^ell||<=C exp(-gamma ell) for all ell>=0, c!=0 and sufficiently large
odd N. Decrease gamma to at most log 2 if needed. Inherited FM-021 gives
||D_0||<=1/2 eventually, so the same bound covers c=0. All off-diagonal
blocks have norm at most one.

Suppose a nonconstant difference word has r>=2 switches. Its cyclic run
lengths ell_1,...,ell_r are positive and sum to m. It has r switch blocks
and m-r diagonal steps. Cyclically starting the trace at a switch and
contracting the runs yields

 |F(c)| <= N C^r exp[-gamma(m-r)]
        = N exp(-gamma m) K^r, K=C exp(gamma).                 (L7)

The trace dimension is N, not N^(r+1); the other dimension factors below
count distinct difference words. Zero-length INTERNAL runs ell_i-1=0 are
included, since the decay bound allows ell=0. The zero-charge identity has
already been removed exactly by L3, not bounded by an invalid decay claim.

For specified r>=1 switch edges in the m-cycle, there are r constant runs,
and at most N^r choices of their labels. Enforcing that adjacent labels
really differ only decreases this count. Therefore the number of words
with r switches is at most binom(m,r)N^r. At r=1 the actual number is zero.
There are N constant words at r=0. Combining L6-L7 gives the explicit bound

 |sum_(s(c)<=R) F(c)-1|
 <= C N^2 exp(-gamma m)
      +N exp(-gamma m) sum_(r=1)^R binom(m,r)(KN)^r.           (L8)

The same right side bounds sums over ANY subset of low-switch difference
words not containing the constant zero word. The argument takes absolute
values only after complete signed block contractions; it does not bound
individual paired path magnitudes.

## L5. Growing R_N and the actual off-charge checksum mask

Fix 0<a<b and choose kappa=gamma*a/8. Let R_N=floor(kappa*N/log N).
For sufficiently large N, binom(m,r)<=m^r<=(bN)^r, and
log(KbN^2)<=3 log N. Thus the sum term in L8 is at most

 N(R_N+1) exp[-gamma*a*N+3 R_N log N]
 <= N(R_N+1) exp[-5gamma*a*N/8].                              (L9)

The polynomial prefactor and C N^2 term are absorbed, for sufficiently large
N, into C' exp(-gamma*a*N/2). This is uniform over aN<=m<=bN.
No effective N threshold is claimed; fixed b and K may be large.

If occupation(x)=occupation(y), then sum_j x_j equals sum_j y_j modulo N.
Therefore t(y-x)=0. Its contrapositive shows that EVERY pair with nonzero
checksum is off-charge. This checksum filter depends only on c, so it selects
whole exact contractions F(c), never a partial mask on their internal x sums.
It also excludes the constant zero word. The subset conclusion after L8 and
L9 therefore proves L1, with eta=gamma*a/2 after harmless constant enlargement.

The independent-coordinate-phase identity now places L1 inside the actual
unaveraged defect:

 |Tr U_N^m|^2-E_theta|Tr(D_theta U_N)^m|^2
   =sum_(occupation(x)!=occupation(y)) A_U(x)conjugate(A_U(y)).

No random phases have been imposed on the quantizer. They only express the
standard exact occupation projector. The unmasked low-switch family equals
1+O(exp(-eta N)); the checksum-selected off-charge family is O(exp(-eta N)).
Its N^-2 bounded compact-band sum is O(N^-1 exp(-eta N)).

For r=0, t(c)=m*c mod N is nonzero exactly when ord(c) does not divide m.
Thus this checksum family contains exactly the safe constant-translation
subfamily of the preceding theorem. The new result replaces/enlarges that
family; the two must not be counted as disjoint contributions.

## L6. Limits of the result

The checksum-zero low-switch family may contain both balanced and off-charge
pairs. Nothing here separates its two occupation pieces. Most general pairs
have many more switches, and the entropy estimate does not control r of
positive order N with the available constants. The complete off-charge
signed defect, balanced comparison, plateau compensation, stationary-label
N-torsion complement and higher TRACE-005 hierarchy remain open.

The low-switch counting and identity isolation are exact finite algebra.
Their analytic input is the all-translation finite-power candidate plus the
accepted actual position-chain gap. No new independent mixing or spectral
universality theorem is asserted by this corollary.
