# Arbitrary-source phase covariance through rank-one reveal increments

**Stable claim:** BGS-TRACE-057. **State:** PROVED.
**Boundary:** The arbitrary complex source bound is an exact contraction theorem; it does not identify a microscopic reference law.
**Integration and review:** [11 October disposition](../record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/source_covariance.md).


8 October 2026. Self-contained reconstruction of the assertion in the supplied manuscript, Theorem 87.10 / TRACE-044. This is not a novelty claim.

Let F be a deterministic complex n by n strict contraction, D=diag(w_1,...,w_n) with independent uniform unit-circle phases, and

K=(D*−F)^−1=(I−DF)^−1D, H=I−F*F, G=I−FF*.

For every deterministic complex matrix B,

E |Tr(BK)|² ≤ Tr(B H^−1 B*),
E |Tr(BK)|² ≤ Tr(B* G^−1 B).                         (1)

There are no self-adjointness, normality, diagonal-source, or rank assumptions. The statements hold conditionally on past data that fix F and B and leave the phases independent and uniform.

## Rank-one martingale decomposition

Fix an order of the n coordinates, and write E_j for its first j coordinates. Let M_j=E[K | w_i, i in E_j]. Since ||F||<1, the Neumann series is uniformly absolutely convergent in operator norm. Every term has nonnegative powers of all w_i. Averaging an unrevealed phase therefore sets its variable to zero. Consequently M_j is the embedded resolvent (D_{E_j}*−F_{E_j,E_j})^−1, with zero rows and columns outside E_j. In particular M_0=0, M_n=K.

Suppose e is added to E, let R=(D_E*−F_EE)^−1, and put

f=F_ee+F_eE R F_Ee,
p=(R F_Ee,1)^T,
r=(F_eE R,1).

In the ordered coordinates E,e, block inversion gives exactly

Delta M=M_{j}−M_{j−1}=q p r,  q=w_e/(1−w_e f).          (2)

All p,r,f depend only on earlier phases. More quantitatively, writing rho=||F||<1 gives F_{E+e,E+e}p=(D_E* p_E,f), hence 1−|f|²≥(1−rho²)(1+||p_E||²) and |f|≤rho<1. Thus E[q | past]=0. Increments at distinct reveal times are orthogonal entrywise in L². They have rank one.

Equivalently, the covariance E[vec K (vec K)*] is a sum of expected projectors onto vectorizations of rank-one matrices. It is a separable positive operator for the row/column tensor decomposition, hence has positive partial transpose in that decomposition. This assertion concerns the complete strictly absorbed resolvent. Cutting off its power series destroys the rank-one increment formula and is not covered.

## Exact energy identities

From F K=D* K−I and K F=K D*−I,

K* H K=K*D+D*K−I,
K G K*=K D*+D K*−I.

The phase mean E K=0 follows from the same Neumann series. Since D*K=I+F K and K D*=I+K F, averaging yields

E K* H K=I,   E K G K*=I.                            (3)

These are matrix identities, not operator-norm inequalities. Martingale orthogonality and deterministic H,G give

sum_j E[(Delta M_j)* H Delta M_j]=I,
sum_j E[Delta M_j G (Delta M_j)*]=I.                  (4)

## Source bounds, with matrix order retained

For a rank-one matrix X=p v*, weighted Cauchy–Schwarz gives

|Tr(BX)|²=|v* Bp|²
 ≤(p*Hp)(v* B H^−1 B* v)
 =Tr[B H^−1 B* X* H X].

Apply this separately to every martingale increment, sum expectations, and use (4). Scalar martingale orthogonality gives the first bound in (1).

The alternative Cauchy–Schwarz inequality

|v*Bp|² ≤(v*Gv)(p*B*G^−1 Bp)
 =Tr[B*G^−1 B X G X*]

gives the second bound. This avoids any appeal to a general separability criterion.

## The resolvent-minus-identity source

Let Q=(I−DF)^−1−I=KF. Then E Q=0, and Tr(AQ)=Tr(F A K). Substituting B=F A into the first bound gives

E |Tr(AQ)|² ≤ Tr(A H^−1 A* F*F).                     (5)

The second orientation also gives Tr(A* F* G^−1 F A). For F=rU, ||U||≤1 and 0<r<1, (5) implies

E |Tr(AQ)|² ≤ r²/(1−r²) ||A||_F².                  (6)

Indeed H^−1≤(1−r²)^−1 I and F*F≤r² I; these are used in two positive-trace inequalities, without commuting A with either factor. The constant is sharp: take U=I and diagonal A. The scalar functions r w_i/(1−r w_i) are independent and centered and each has variance r²/(1−r²).

## Limits of the result

An adapted reveal order gives the same proof if the next index is selected before revealing its phase, using only already revealed data and independent extra randomness. Sources may depend on an initial sigma field independent of those remaining phases. Sources depending on the remaining phases cannot be substituted into (1). Strict contraction ensures invertibility of H,G and the stated general estimates; particular non-strict contractions can have finite moments, but the general theorem cannot be extended by simply deleting this assumption. No boundary moment estimate, finite-power covariance, microscopic CUE law, or deterministic BGS follows from this lemma alone.

No external theorem beyond finite-dimensional block inversion, geometric series, conditional-expectation orthogonality, and weighted Cauchy–Schwarz is needed for this proof. The separability observation is an equivalent explanation, not an additional assumption.

## Independent check

A separate internal reviewer independently checked the full proof, the noncommuting factor orders, the rank-one covariance tensor indices, both matrix energy identities, and the adapted-order qualification. No substantive error was found. Two overly broad editorial phrases were corrected: strict contraction is sufficient for the theorem rather than necessary for every individual finite-moment example, and the appended 1 prevents p or r from vanishing. This is internal review, not external refereeing.
