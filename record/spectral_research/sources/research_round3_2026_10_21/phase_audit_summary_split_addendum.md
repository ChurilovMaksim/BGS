> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/phase_audit_summary_split_addendum.md`. Embedded SHA256: `8449308fa7cc455cf209a424eb93b77b20e09158d080b7d8392698efe2cc367a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Targeted audit addendum: final split-symmetry passages in the summary

Date: 21 October 2026.

**Verdict: passes without correction.**

This addendum checks only the newly explicit definition of $E_N^s$ at the end of Section 5.4 and the new Section 5.5 of:

Spectral_research_2026-10-21.md  
SHA-256: 388b7c16c198a67d8a7f06358f1c1b8b0ae6e44724e91d91ef679848909bc394.

The summary's hash was checked before and after reading. The source and the previous audit remained unchanged:

- arithmetic_rational_split_affine_reversal.md, SHA-256
  a92061a005e3b219b7564b0714ef469b3fb066da0274e73ebdd1faf411d9d36c.
- phase_audit_rational_split_affine_reversal.md, SHA-256
  8cb78834cfb92c2717a5aa782deaba956d30832a2019b014c07fd71405bfee8b.

## 1. The definition at the end of Section 5.4

The statement
$$
E_N^s:=\exp(is\tau NA_N),\qquad s\in\mathbb R,
$$
correctly fixes the exponential for every real $s$. It does not choose an unspecified branch of a fractional matrix power.

Since all these exponentials have the same generator,
$$
E_N^{c-1}U_NE_N^{1-c}
=E_N^cM_NE_N^{1-c}
=U_{N,c}(\tau).
$$
If an antiunitary $D$ reverses $U_{N,c}(\tau)$, conjugation by this unitary equivalence produces the original-matrix reverser
$E_N^{1-c}D E_N^{c-1}$, in the displayed order. No commutation of $D$ with an exponential is assumed.

The parameter in this particular definition is explicitly $\tau$, and the adjacent identity is explicitly at $z=\tau$. The new theorem in Section 5.5 separately permits general nonzero real algebraic $z_0$; the summary does not incorrectly substitute the $\tau$-definition into that general identity.

## 2. Conditions and coordinate convention in Section 5.5

Theorem 3 retains exactly the checked hypotheses: odd $N\ge75$, rational $c\in[0,1]$, and nonzero real algebraic $z_0$. The final paragraph explicitly preserves the rationality restriction. The scalar $\eta$ in the proposed reversal is eliminated by the already established nonzero trace, as in the full proof.

The change of frequency order is explicit and consistent:
$$
v=(k,l),\qquad W(k,l)=T_N(l,k),\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$
In this convention,
$$
e_1=(1,0)\leftrightarrow T_N(0,1),\qquad
e_2=(0,1)\leftrightarrow T_N(1,0).
$$
The coefficients $u=1/20-i/200$ and
$\gamma=(-3-4i)/1000$ are consequently assigned to the correct two frequencies. The images used in the collision table are
$$
-Se_1=(-3,-4),\quad -Se_2=(-2,-3),\quad
S(-1,-1)=(-5,-7).
$$
There is no transposition or sign mismatch with the preceding $(l,k)$ discussion.

## 3. Transmission of the proof

The summary preserves all load-bearing steps of the checked argument:

1. The antiunitary normalizer induces a linear label map of determinant $-1$ and a character taking values in $\mu_N$.
2. Its conjugation action has an algebraic matrix representative. The nonzero trace gives $\eta=1$, and the exponential-polynomial lemma makes the fixed-parameter relation an identity.
3. The differentiated symmetry preserves $H_c$ through $C=MD$. This crucial operator is explicitly stated.
4. The support union has 62 frequencies in the stated rectangle, so no modular alias occurs for $N\ge75$.
5. For $0<c<1$, the coefficients $cu,c\gamma$ are nonzero and lie in $\mathbb Q(i)$. Their root-of-unity ratios force the normalizer character to be trivial.
6. The complete collision alternatives and both overlap coefficients are transmitted with their correct constants and exceptional parameters.
7. The integer determinants are $1$, $1,3$, or $1,7$, with the correct cases $c=1/2,1/3$. The contradictions use only $N\nmid2,4,8$, and thus apply to composite moduli.
8. Both endpoints are included: uniqueness for $c=1$, and conjugation back to $A_N$ for $c=0$.

The full rational Fourier list is not reprinted in the summary. Its omission is explicitly identified and the reader is directed to the supplied full proof, which the earlier independent audit has checked. The shortened ray argument introduces no new assertion beyond that list and no hidden spectral hypothesis. The combined deliverable therefore retains the complete proof; the summary correctly presents its shortened form.

## 4. Scope and final disposition

The half-kick consequence follows by applying Theorem 3 at $c=1/2,z_0=\tau$ and the prescribed exponential conjugation in Section 5.4. The text does not enlarge the new normalizer theorem to arbitrary algebraic $c$, identify the full arbitrary-phase monomial class with the Weyl normalizer, exclude eigenbasis-defined antiunitaries, or infer spectral universality from symmetry exclusion.

No correction is required to the two reviewed changes. No source file was modified and no additional research branch was opened.

