# A q-divided-power lattice reduction for the remaining ramified higher-seven family

Base: BGS d4132ccee82849b644520d88c953cb9b33382a59, unchanged actual matrices. New candidate proof, pending independent audit. Accepted earlier proofs are untouched. No canonical writes.

## Claim and exact dependencies

For every odd N with245|N, the actual pair(A_N,M_N) has scalar complex common commutant.

Together with the independently reviewed first-seven theorem including all5-ramification, the reviewed unramified higher-seven theorem, and FM-008 away from7, this would establish the full subsidiary statement for every odd N>=3 except the genuine exception N7. It would not establish spectral simplicity in the seven-divisible family or microscopic BGS.

The new load-bearing input is the normalized-lattice lemma below. The finite shifted49-dimensional certificates alone do not prove the claim. No generic unitarity or unspecified flatness principle is used.

Write N=5^e n, e>=1,5∤n, n=7m with7|m. Put P=5^e and L=Pm=N/7. Let q=zeta_N, Q=q^7, w=q^L, and let bars denote reduction at the Gaussian prime over5 with i reducing to2. Then bar q has exact order n, bar Q has order m, and omega=bar q^m has order7. The original w reduces to omega^P.

## 1. A normalized-lattice lemma from the actual Jacobi recurrence

Work over a finite5-adic extension E containing the actual coefficients and sigma with v(sigma)=−3/4, with v(5)=1. Put B=1000A. Use the actual seven chains with depths0,...,L−1 and starts a=1−2^(-1) modulo N. The upper/lower coefficient valuations are0 and2 respectively. For every internal bond,

0<=v(r_u)<=1/2,

independently of the chain label. Normalize by D_(t,j)=lambda_t U_t(j), where

lambda_t=product_(u=1)^t [4q^(8u)/(sigma(3+4i)(q^(7u)−1)^2)],
U_t(j)=w^(jt)/product_(u=1)^t(1+q^u w^j)^2.

Every U_t(j) is a5-adic unit. The normalized B'=sigma D^(-1)BD has upper blocks I_7, diagonal blocks of valuation at least1/4, and lower blocks of valuation at least1/2.

Define

F(t)=2 sum_(u=1)^t v(1−Q^u),  v(lambda_t)=3t/4−F(t).

Every increment of F lies in[0,1/2]. For r+d<L,

lambda_r lambda_d/lambda_(r+d)
 =q^(−8rd) [r+d choose r]_Q^2.                       (1)

The Gaussian binomial is an integer polynomial in Q, so(1) is integral. In particular

F(r+d)>=F(r)+F(d).                                  (2)

Let X be any integral actual common commuter and put S=D^(-1)XD. Write C_d=S_(0,d), where each entry is a7-by-7 chain block. Since D_0=I,

Ctilde_d=C_d/lambda_d=X_(0,d) U_d

is integral.

The exact equation[S,B']=0 recursively determines every row from this first row. With V_r the diagonal block and W_r the lower block of B', it reads

S_(r+1,s)=S_(r,s−1)+S_(r,s)V_s−V_rS_(r,s)
          +S_(r,s+1)W_s−W_(r−1)S_(r−1,s),            (3)

with out-of-range entries zero. In this recurrence, the unique term of degree d=s−r is C_d. Every correction using C_d has h=d−s+r>0; diagonal insertions add1 to h and lower insertions add2. Its coefficient therefore has valuation at least h/4.

Conjugate S by the scalar depth matrix lambda, obtaining

Shat=lambda S lambda^(-1)=U^(-1)XU.

For a correction of grade h, its valuation after this conjugation is at least

h−F(d)+F(s)−F(r).                                   (4)

If s>=r, use(2) and the increment bound to see that(4) is at least h/2. If s<r, use F(d)<=d/2 and F(r)−F(s)<=(r−s)/2, obtaining the same strict positive bound. Thus every correction disappears in the residue field. The exact leading formula is

Shat_bar_(r,s)=bar q^(−8r(s−r))
              [s choose r]_(bar Q)^2 Ctilde_bar_(s−r), s>=r,

and it is zero for s<r. The Gaussian binomial here is evaluated as a polynomial; no vanishing denominator is divided after reduction.

This is a statement about reductions of actual commuters. The upper-bond matrix has not been substituted for the actual generator: the discarded diagonal/lower contributions were controlled by the strict bounds(4).

## 2. Elementary q-Lucas decomposition

Write an index t as

t=t_0+m(t_1+5t_2+...+5^(e−1)t_e),
0<=t_0<m, 0<=t_h<5 for h>=1.

For bar Q of odd order m, the elementary q-binomial product identity gives

[s choose r]_(bar Q)
 =binom(floor(s/m),floor(r/m)) [s_0 choose r_0]_(bar Q).

One way to verify it is to group the product of(1+bar Q^u z) into complete m-blocks, each equal to1+z^m, and compare coefficients. The usual phase factor cancels because m is odd. In characteristic5, expanding(1+z)^S digitwise gives Lucas's factorization of the ordinary binomial into the base-five digits.

Put

f_t=product_(u=1)^(t_0)(1−bar Q^u)^2
    times product_(h=1)^e(t_h!)^2.

Every f_t is a nonzero residue-field element. The squared Gaussian binomial vanishes when addition r+(s−r) has a carry in these mixed digits. Otherwise it equals f_s/(f_r f_(s−r)).

Conjugate Shat_bar successively by the scalar depth diagonals bar q^(4t²) and f_t^(-1). The phase in(1) cancels, leaving a multivariate upper-Toeplitz matrix

Y=sum_d J_m^(d_0) tensor J_5^(d_1) tensor...tensor J_5^(d_e)
       tensor Chat_d,                               (5)

up to the harmless ordering of tensor factors, where

Chat_d=bar q^(4d²) f_d^(-1) Ctilde_bar_d.

This identifies the leading algebra explicitly. It does not assume that a ramified Fourier matrix keeps full rank.

The simultaneously transformed raw Fourier kernel is

K_N=D_eff^(-1) G(bar q) D_eff,
D_eff(t,j)=U_bar_t(j) bar q^(4t²)/f_t.                (6)

The matrix Y commutes with K_N.

## 3. An invertible base block of the singular Fourier kernel

Reorder the chain labels by j'=Pj modulo7; this is a permutation. In these labels,

U_bar_t(j')=omega^(j't)/product_(u=1)^t(1+bar q^u omega^j')^2.

Group the space by the e high base-five digits, each high block having dimension n=7m. In(5), let Y_0 be the coefficient with all high degrees zero. It commutes with J_m tensor I_7.

Let E be the n-by-n block of K_N from the highest high-digit row(all digits4) to the lowest high-digit column(all digits0). Set

r=(P−1) modulo7, so r is one of0,...,5.

Define the chain-only invertible matrix H_r by

(H_r v)_j=h_r(j) v_(j+r),
h_r(j)=product_(u=1)^(mr)(1+bar q^u omega^j)^2.        (7)

Let K_n be the dimension-n kernel with the base gauge

D_eff,n(s,j)=omega^(js) bar q^(4s²)
 /[product_(u=1)^s(1+bar q^u omega^j)^2
   product_(u=1)^s(1−bar Q^u)^2], 0<=s<m.

Direct substitution gives

E=4^floor((P−1)/7) (I_m tensor H_r) K_n.              (8)

Here is the cancellation behind(8). At the highest digits t=m(P−1)+s, their factorial contribution is(4!)^(2e)=1 modulo5. The shift in the raw position is m(P−1), hence a chain shift r modulo7. The U gauge contributes omega^(−(P−1)s), which is cancelled by the cross term in bar q^(4t²). Since7|m, the other phase terms are1. Finally, every full n-block in the product of(1+bar q^u omega^j)^2 contributes4, independently of j. Thus only the partial product(7) remains.

All factors in(8) are invertible: bar q has exact order n and5∤n, so its raw n-dimensional Fourier kernel is invertible. This invertible block exists although the full N-dimensional reduced kernel is singular.

The same dictionary was checked exactly at N=245,1225,735,3675, comparing only the relevant49- or147-dimensional blocks and159,670 q-Lucas coefficient identities. Those checks corroborate(1)–(8), not replace their uniform derivations.

## 4. Shifted base commutants

It remains to show that J_m tensor I_7 and H_r K_n have scalar common commutant for every odd n divisible by49,5∤n, and r=0,...,5.

The gauge defining K_n turns the actual reduced upper bonds in dimension n into a common nonzero scalar multiple of J_m. A scalar geometric depth gauge converts it to the standard unit-upper normalization. H_r acts only on chain labels and commutes with this geometric depth gauge.

For m>=21, the accepted unramified higher-seven proof applies with the following explicit extension. Multiplying the kernel on the left by H_r sends each endpoint column u_s to H_r u_s, preserving their independence, and leaves its right rows v_s unchanged. The penultimate row still has form

alpha Q u_0 v_0^T Z^(−2),

but its pole matrix becomes

Q=diag((1+omega^(r+1) bar q^(−1) omega^j)^(−2)).

The coefficient omega^(r+1) is primitive seventh because r+1≠0 modulo7. The accepted bounded polynomial certificate already proves the required diagonal contraction nonzero for **every primitive seventh pole parameter**, independently of the primitive seventh root used as the evaluation grid: after the grid Fourier matrix is removed, the polynomial coefficient matrix depends only on bar q, while the pole parameter is the separate variable in the certified norm/resultant. The right-row coefficients y_j are unchanged. Thus the two-row leading argument again forces C0 scalar.

The minimal-tail argument is unchanged: H_r is a common invertible left factor of the endpoint columns; right Fourier rows and the weighted Casoratian retain their independence. This kills all higher Toeplitz coefficients when m>=21.

The only shorter allowable case is m=7,n=49. ramified_higher_base_variants.py directly constructs the six matrices H_r K_49^unit in F5[q]/Phi49, where K_49^unit is the simultaneous kernel in the actual unit-upper gauge. This differs from the effective K_49 in(6) by the geometric depth gauge described above: the effective upper generator is cJ with c=4 bar q^(−4), and the geometric gauge sends cJ to J while commuting with H_r. For each r=0,...,5, the matrix T=J+H_r K_49^unit has a cyclic vector at depth-major index24, with cyclic rank49 and rank48 of the commutator-column matrix with J. Hence each unit-upper shifted base commutant is scalar. Simultaneous geometric conjugation transfers this to(cJ,H_r K_49), and rescaling the first generator transfers it to(J,H_r K_49). No claim about the literal effective-gauge witness J+H_r K_49 is required. Phi49 is irreducible over F5, so the certificate covers every primitive49th root by Frobenius conjugation. The field arithmetic is exact.

An initial endpoint-vector attempt had commutator-column rank42 and was insufficient; it was retained separately and replaced by the interior cyclic vector, not treated as a counterexample.

## 5. Killing every high-digit coefficient

In the high-digit block form of(5), the highest row has only the diagonal coefficient Y_0. The lowest column has only that same coefficient. Commutation with the block E in(8) gives

[Y_0,E]=0.

Since Y_0 commutes with J_m tensor I_7, Section4 implies Y_0 is scalar.

Now induct on the total high-digit degree of the remaining coefficients Y_D. In the highest row and column D of[Y,K_N]=0, the scalar Y_0 terms cancel. All proper smaller-degree coefficients vanish by induction, leaving

E Y_D=0.

Since E is invertible, Y_D=0. This works for all e and all5^e high blocks; there is no dimension cutoff or unproved induction over ramification levels. Hence Y is scalar.

## 6. The normalized-lattice conclusion

Let C be the actual common commutant over E and let L=C intersect M_N(O_E). This is a full saturated O_E lattice in C. For every X in L, Sections1–5 show that its reduction, after invertible unit conjugations and a permutation, is scalar. Thus its original reduction is scalar too.

The kernel of reduction on L is exactly pi L: if every entry of X is divisible by a uniformizer pi, then X/pi is still an integral common commuter. Since L is a finite free lattice of rank dim_E C, its reduction dimension equals that rank. Its image is contained in the one-dimensional scalar subspace, while the identity lies in L. Therefore dim_E C=1.

This is the required normalized-lattice argument. It does not assert that an arbitrary nonscalar idempotent remains nonscalar after reduction, and it does not replace the actual generator by its upper part. The actual recurrence controls the reduction of every integral commuter.

Finally, ranks of the algebraic commutator equations are unchanged under extension to E or C. This proves the stated actual-family claim if the new lattice/tensor argument passes independent review.

## Reproduction and scope

- ramified_higher_base_variants.py / .json: six exact shifted49-dimensional bases.
- check_ramified_tensor_dictionary.py: squared q-Lucas and endpoint-block dictionary controls.
- ramified_tensor_dictionary_results.json: the four declared finite regimes and counts.
- The accepted unramified_actual_commutant.md and its completed bounded polynomial certificates supply only the base two-row nonvanishing inputs used in Section4.

The original all-N commutant goal would be closed only after independent review of this new argument and combination with the other exact families. The signed microscopic BGS target remains a different open obligation.
