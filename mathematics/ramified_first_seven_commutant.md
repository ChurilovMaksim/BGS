# Chain-trace closure at the first seven-primary level, including ramification at 5

Maintained supporting extension of FM-024, accepted after fresh independent
internal review on 6 October 2026. Exact finite controls and the universal
valuation/augmented-rank proof have separate scopes. Original hashes and
status records are retained; this is the integrated first-seven chain-trace component.
No external peer review or Lean formalization is asserted.

## Claim and boundary

For every odd N>7 with 7|N and 49∤N, including arbitrarily large powers of 5 dividing N, the actual pair (A_N,M_N) has scalar complex common commutant.

Combined with the separately reviewed higher-seven-primary theorem for 49|N,5∤N and FM-008 for 7∤N, this leaves only odd multiples of 245 in the uniform algebraic question. N=7 is the genuine known exception. No spectral-simplicity, quantitative spectral gap, Heisenberg comparison or BGS conclusion is made.

Unlike the unramified direct-reduction proof, this argument does not require the reduced full Fourier matrix to be invertible. It retains a rank-seven endpoint block and an additional integral linear consequence of the actual commutator equation.

## 1. Uniform valuation setup

Write N=7L, with L>=3 odd and 7∤L. Work in a finite extension E of the 5-adic completion of Q(i,zeta_N), at the Gaussian prime with i reducing to2. Normalize v(5)=1 and enlarge E to contain sigma with v(sigma)=−3/4. Let B=1000A_N and let G=sqrt(N)M_N be the raw quadratic kernel.

Set h=2^(-1) modulo N, a=1−h=h modulo N, t=zeta_N^h, and

eta=Phi_7(t)^2.

Since t has order N>7, eta is nonzero. If n=N/5^(v5(N))>7, then t reduces to a primitive nth root and v(eta)=0. If n=7, write N=7*5^e, e>=1. The standard root-of-unity valuation gives

c:=v(eta)=1/(2*5^(e−1)) <=1/2.

Thus in all cases0<=c<=1/2.

The actual seven upper bonds, at depth u−1 to u of chain j, are

b_u(j)=(-3−4i) r((u+jL)/N),
r(z)=−(z^7−1)^2(z+1)^2/(4z^8),

with 1<=u<L. For every nonzero internal bond,

c<=v(r_u)<=1/2,                                      (10)

and this valuation is independent of j. The upper bound is the same elementary 5-adic cyclotomic estimate used in FM-008: only a 5-power root can have1−z^7 of positive valuation, and its valuation is at most1/4. The factor1+z is always a unit because its residue has odd order. For c>0, every z^7 is a power of a primitive5^e root, so its distance from1 has valuation at least that of the primitive root. For c=0 the lower bound is automatic. The unchanged coefficients satisfy v(-3−4i)=0 and v(-3+4i)=2.

Normalize each chain with D_(0,j)=1 and

D_(u,j)=D_(u−1,j)/(sigma b_u(j)).

The common depth valuations d_u=v(D_(u,j)) strictly increase, since

d_u−d_(u−1)=3/4−v(r_u) is in[1/4,3/4].

Then B'=sigma D^(-1)BD is integral with upper bonds exactly1. Its lower bonds have valuation

1/2+2v(r_u),

and its diagonal is sigma times the original diagonal of B. Consequently its reduction is J=I_7 tensor J_L in chain-major order.

## 2. The endpoint reduction still has full seven-dimensional rank

Let beta=D_(L−1,0) and G'=beta D^(-1)GD. The strict depth valuation inequalities make G' integral. Only its last-row-depth/first-column-depth blocks survive reduction. Its reduction is

G'_bar=E tensor (e_(L−1)e_0^T),

where E is an invertible7-by-7 diagonal-Fourier-diagonal matrix. Indeed its mixed chain coefficient is 2L modulo 7, which is nonzero; the primitive seventh root w=zeta_N^L retains order7 even when 5|N. The endpoint normalizing factors are units after beta is removed.

Let S be any integral matrix commuting with B' and G'. Its reduction commutes with J, hence has upper block-Toeplitz coefficients C_0,...,C_(L−1). Commutation with G'_bar kills every C_d for d>=1: the off-corner block of S_bar G'_bar is C_d E, while G'_bar S_bar has no entry there. Invertibility of E forces C_d=0. Thus

S_bar=C_0 tensor I_L, and [C_0,E]=0.                  (11)

This step uses only the endpoint block, not invertibility of the full reduced G.

## 3. An integral first-order consequence of the actual commutator

Put alpha=5 sigma eta and

R_pert=(B'−J)/alpha.

This is integral. The lower entries have valuation at least

(1/2+2c)−(1/4+c)=1/4+c>0,

while the diagonal entries are B_(x,x)/(5 eta). All diagonal terms except2r(x)sin(2pi x/N)/eta have positive valuation after this normalization: the coefficients1000,100 and−100 give valuation margins at least2−c,1 and 1−c respectively. Thus R_pert reduces to a diagonal matrix with entries

d_x=overline(2r(x/N)sin(2pi x/N)/eta).

For a matrix written in seven-by-seven blocks of size L, let tau take the trace of each L-by-L block. The identity

tau([S,J])=0

holds for **every** S, because J has the same J_L on each chain. Therefore [S,B']=0 implies the exact additional linear constraint

tau([S,R_pert])=0.                                  (12)

Reducing(12) and using(11) gives

[C_0,T]=0,  T=diag(T_0,...,T_6),
T_j=sum_(u=0)^(L−1) d_(a+u+jL).                    (13)

The division by alpha is performed before reduction and is justified by integrality. This is the extra constraint absent from the naive reduction of the pair. It is not an assumption that every commuter of the reduced pair lifts.

## 4. The normalized chain trace has only two nontrivial harmonics

Let x denote a formal variable. Reduction of the actual diagonal Fourier coefficients of B/5 at i=2 gives, at positive labels1,2,5,6,8,9, respectively

3,4,2,4,1,3,

with the negative coefficients their negatives and the label7 coefficient zero. The author certificate derives these from the maintained coefficients d_v=4000c_v; the independent portable verifier reconstructs them directly from the literal Laurent model.

Define over F5(x)

a(x)=3x/(1−x²)+4x^6/(1−x^12)+x^8/(1−x^16),
b(x)=4x²/(1−x^4)+2x^5/(1−x^10)+3x^9/(1−x^18).

After cancellation of numerator/denominator common factors, both numerators are divisible by Phi_7(x)^2. Let a_0/d_a and b_0/d_b be the resulting rational functions after this factor is removed. The exact polynomial certificate gives

gcd(a_0,b_0)=x,                                      (14)

with an explicit Bezout identity. The denominator d_a divides the product of 1−x^(2k) for k=1,6,8, and d_b divides the corresponding product for k=2,5,9. Hence both are nonzero at every root whose order is divisible by 7.

Writing bar t for the residue of t and retaining w for the primitive seventh residue root, finite geometric summation along each chain gives

T_j=A(w^j−w^(−j−1))+B(w^(2j)−w^(−2j−2)),             (15)
A=(1−w) a_0(bar t)/d_a(bar t),
B=(1−w²) b_0(bar t)/d_b(bar t).

Here(a,b) were normalized by eta=Phi_7(t)^2 **before** reduction. Formula(15) remains valid when bar t has order7: reducing the Gaussian coefficients incurs errors of valuation at least1, and division by eta loses at most1/2. Thus those errors still vanish. The exact polynomial divisibility modulo 5 computes the reduced quotient. It would be invalid simply to substitute a primitive seventh root into the unnormalized trace, which vanishes there.

For completeness, the geometric identity used for a positive frequency k is

t^k (1−w^k)/(1−t^(2k));

its negative-frequency partner produces the bracket w^(kj)−w^(−k(j+1)). Grouping labels modulo 7 leaves only residues±1,±2 and gives exactly the displayed a,b. All denominators are units at bar t. Since bar t is nonzero and its order is divisible by 7, (14) implies(A,B)≠(0,0).

The independent direct local-expansion replay compares (15) with the direct order-two local expansion for N=7*5^e in all six residue classes of e modulo 6. This is corroboration of the normalization, not the uniform proof.

## 5. Seven-point partition lemma

Put xi_j=w^j−w^(−j−1) and zeta_j=w^(2j)−w^(−2j−2). The xi_j are all distinct. For B=0,A≠0, (15) therefore has seven singleton eigenspaces.

For B≠0, collisions in(15) occur only when A/B equals one of the 21 pairwise ratios

(zeta_k−zeta_j)/(xi_j−xi_k), j<k.

Exact reduction in F5[w]/Phi7 shows there are precisely nine distinct ratios. Three give a partition with sizes3,1,1,1,1; six give sizes2,2,1,1,1. This exhaustive7-point classification, including all ratio equalities and inequalities, is recorded in the pinned compact certificate. Outside those nine values the partition is all singletons. Frobenius conjugation covers every primitive seventh root and arbitrary residue-field extensions.

In every case the number k of singleton groups is at least the size of every other group, and every group has size at most3.

## 6. The required Fourier minors do not vanish in characteristic5

Every minor of a seventh-root Fourier matrix of size at most3 is nonzero. Sizes1 and 2 are immediate. For size 3, subtract row/column exponents so the sets are{0,a,b} and{0,c,d}, with a,b,c,d nonzero modulo 7 and a≠b,c≠d. After nonzero phase factors the determinant is

(w^(ac)−1)(w^(bd)−1)−(w^(ad)−1)(w^(bc)−1).

Reduce its exponent polynomial modulo z^7−1 to degree at most6. If it vanished at w in characteristic5, irreducibility of Phi7 over F5 would make it a scalar multiple of Phi7. Its value at 1 is zero, while Phi7(1)=7≠0 modulo 5, so that scalar is zero. Its integer coefficients have absolute value at most3, hence all coefficients would already be zero over the integers.

That would equate the exponent multisets{ac+bd,ad,bc} and{ad+bc,ac,bd} modulo 7. The first exponent ac+bd cannot equal ac or bd, so it must equal ad+bc. The remaining matching would force either d=c or a=b, a contradiction. This proves the size 3 assertion. Here Phi7 is irreducible because ord_7(5)=6.

Diagonal unit factors and permutation of columns preserve this property, so it applies to E in(11).

## 7. Scalarity and return to characteristic zero

By(13), C_0 is block diagonal on the eigenspace partition of T. At a singleton coordinate j, it acts by a scalar lambda_j. Commutation with E and the nonzero entries between singleton coordinates force every lambda_j to equal a common lambda.

For any other group I of size m<=3, choose m singleton coordinates J. Then

(C_(0,I,I)−lambda I_m) E_(I,J)=0.

The minor E_(I,J) is invertible by Section 6, so that block is scalar too. Therefore C_0=lambda I and S_bar is scalar.

This reduction can be used rigorously in either of two equivalent ways. The integral linear system consisting of [S,B']=0, [S,G']=0 and(12) has the same characteristic-zero kernel as the original common-commutator equations. Its reduced kernel is scalar by the preceding argument. A nonzero(N²−1)-minor of this **augmented** system therefore lifts and proves scalar common commutant over E. Alternatively, the lattice of integral actual commuters is saturated; repeatedly subtracting a scalar residue and dividing by a uniformizer forces every off-diagonal entry and every difference of diagonal entries to vanish. No nonintegral idempotent is silently specialized.

Finally, ranks of the algebraic linear equations are unchanged under extension from their number field to E or to C. Conjugating by D and multiplying either matrix by nonzero scalars do not change the common commutant. This proves the stated actual-family claim; the valuation/trace argument and exact certificate passed fresh independent review.

## Remaining scope

When 49|N, the endpoint transfer block has rank one rather than seven, so Step 2 no longer kills all higher Toeplitz coefficients. The separately accepted unramified higher-seven proof still applies when 5∤N, but the ramified family245|N remains open. N=7 has eta=0 and a scalar kick, and is excluded throughout.

## Portable verification and trust boundary

Run computations/verification/ramified_first_seven_trace.py normally and
with Python -O. It uses explicit checks, silent imports, a pinned 5,510-byte
certificate and independent F5[w]/Phi7 tuple arithmetic. It reconstructs the
normalized rational identities, all nine partitions, 49/441/1225 Fourier
minors, all 900 normalized exponent configurations, and direct chain sums
for e=1,...,6. The six dimensions corroborate normalization, not an
infinite-family extrapolation. The separately reviewed valuation and
augmented linear-system argument supplies the universal scope.
