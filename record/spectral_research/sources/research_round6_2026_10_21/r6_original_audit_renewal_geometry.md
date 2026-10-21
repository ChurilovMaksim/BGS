> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_original_audit_renewal_geometry.md`. Embedded SHA256: `ce222733017771f6d2ae0da2ad3725df48613aa9e3ca757ed83ee84c735086d8`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of exact renewal geometry and long-return energy

Date: 21 October 2026. Reviewer: `r6_original_obstruction`.

Audited source: `r6_dense_renewal_long_return_obstruction.md`, SHA256
`95ea7e37c46b840854853c934eebecbd51ac1cb305d0200a283e68b9f7c3d0b2`.

**Verdict.** All seven mathematical sections are sound as stated.
The energy identities and dimension bounds are exact for every finite
unitary and every phase vector. The original-family conclusion at
phase one follows from the independently audited fixed-power entry
theorem, with no phase average. The auxiliary prime example has the
stated reverse-transfer limitation. The final bounded-run identity
preserves literal rooted multiplicity. This is a mathematical proof
audit, not a formal verification certificate.

## 1. Renewal orientation, centering, and norm bound

Write the unitary doubled transfer on the diagonal and off-diagonal
pair spaces as
$$
W=\begin{pmatrix}P&B\\C&S\end{pmatrix},\qquad
F_1=P,\quad F_r=BS^{r-2}C\ (r\ge2).
$$
The Schur complement gives the formal identity
$$
MW^nM=R_n,\qquad
\sum_{n\ge0}s^nR_n
=\left(I-sP-\sum_{r\ge2}s^rBS^{r-2}C\right)^{-1}.
$$
Both the order of the noncommutative factors and the index shift
are correct. In particular,
$R_n=\sum_{r=1}^nF_rR_{n-r}$.

Each $R_n$ is the entrywise squared modulus of the indicated
unitary product, so it is doubly stochastic. Induction proves
$F_re=e^*F_r=0$ for every $r\ge2$. With $E_n=R_n-J$,
the recurrence becomes
$$
F_r=E_r-E_1E_{r-1}-\sum_{j=2}^{r-1}F_jE_{r-j}.
$$
All $F_j$ are contractions by their compressed-unitary
factorization, and $\|E_1\|\le1$. Taking the Hilbert--Schmidt
norm gives exactly
$\|F_r\|_{\rm HS}\le\sum_{j=1}^r\|E_j\|_{\rm HS}$.
This estimate does not recursively multiply earlier
Hilbert--Schmidt bounds.

## 2. Complete energy and exact tails

Unitarity supplies
$P^*P+C^*C=I$, $B^*B=I-S^*S$, and
$CC^*=I-SS^*$. Thus, for $m\ge1$,
$$
\sum_{r=1}^{m+1}F_r^*F_r
=P^*P+C^*\sum_{j=0}^{m-1}S^{*j}(I-S^*S)S^jC
=I-C^*S^{*m}S^mC.
\tag{2.1}
$$
If $a_m=\|S^m\|_{\rm HS}^2$, then
$$
\|S^mC\|_{\rm HS}^2
=\operatorname{Tr}(S^m(I-SS^*)S^{*m})=a_m-a_{m+1}.
$$
The sequence $a_m$ decreases and converges in fixed finite
dimension, so its differences tend to zero. The positive remainder
in (2.1) tends to zero in norm because its trace does. This proves
$$
\sum_{r\ge1}F_r^*F_r=I,
\qquad\sum_{r\ge1}\|F_r\|_{\rm HS}^2=N.
$$
Applying the same argument to $W^*$ gives the reversed positive
sum $\sum_rF_rF_r^*=I$, since its first returns are precisely
$F_r^*$.

The tail indexing is correct, including its endpoint:
$$
\sum_{r>m}\|F_r\|_{\rm HS}^2
=\|S^{m-1}C\|_{\rm HS}^2=a_{m-1}-a_m,
\qquad m\ge1.
$$
At $m=1$ this is $N-\|P\|_{\rm HS}^2=\|C\|_{\rm HS}^2$.
No recurrence assumption about individual states and no absence of
unitary dark modes have been inserted.

## 3. Weighted identity and the exact singular-value obstruction

For a contraction $S$, if $Sv=\lambda v$ and
$|\lambda|=1$, positivity of $I-S^*S$ implies
$S^*v=\bar\lambda v$. That eigenline is reducing. Splitting
these lines off exhausts the unit-circle spectrum; the remaining
finite matrix has spectral radius less than one, and its powers
vanish by Jordan form. Therefore
$$
\lim_m a_m=\dim\mathcal H_{\rm dark}.
$$
Unitarity then gives $Bv=C^*v=0$ on the dark space. The
nonnegative tail-sum identity and the preceding exact tail yield
$$
\sum_{r\ge1}r\|F_r\|_{\rm HS}^2
=N+a_0-\lim_m a_m
=N^2-\dim\mathcal H_{\rm dark}.
$$
All terms are nonnegative, so the interchange is justified by
monotone convergence.

The doubled transfer fixes
$\Omega=N^{-1/2}\sum_a|a,a\rangle$.
For $v\in O$, every vector $MW^jv$ is orthogonal to
$\Omega$. Hence the conditions $MW^jv=0$, $1\le j\le m$,
impose at most $m(N-1)$ linear constraints on a space of
dimension $N^2-N$. Their common kernel has dimension at least
$(N-1)(N-m)$. On that kernel, induction gives
$S^jv=W^jv$ for $j\le m$, so $S^m$ preserves norm.
Because $I-S^{*m}S^m$ is positive, its zero quadratic form on
this kernel implies it annihilates the whole kernel. Thus at least
$(N-1)(N-m)$ singular values are exactly one, and
$\|S^m\|=1$ for $1\le m<N$. This is a singular-value
statement; no estimate for a signed trace is inferred from it.

## 4. Finite short-return budgets and the physical cutoff 49

If $\|E_j\|_{\rm HS}^2\le h_j$ through $L$, then
$\|P\|_{\rm HS}^2\le1+h_1$, and Cauchy--Schwarz gives
$$
\sum_{r\le L}\|F_r\|_{\rm HS}^2
\le1+h_1+\sum_{r=2}^L r\sum_{j=1}^rh_j=:K_L(h).
$$
Subtracting from total energy $N$ proves the stated two-sided
long-tail estimate. If
$\max|(U^j)_{ab}|\le A_j/\sqrt N$, then
$$
\|R_j-J\|_{\rm HS}^2
=\sum_{a,b}|(U^j)_{ab}|^4-1\le A_j^2-1,
$$
because the squared moduli sum to $N$.

For the original family, the entry theorem in
`r6_original_fixed_powers_49.md` has SHA256
`3f51c6d7de5b559c28271c72ae62c2f2d331f9c606b24a84cdab80751339d019`.
Its independent audit has SHA256
`0953ee6eb3c665fe667fabcb094651eb7284f6250ebfa2c6d535bd98f7da9b61`.
It gives $A_j=2\sqrt{b_j}$ simultaneously for $1\le j\le49$
at all sufficiently large odd dimensions. Consequently the source's
$$
K_{49}^{\rm phys}
=4b_1+\sum_{r=2}^{49}r\sum_{j=1}^r(4b_j-1)
$$
is a finite constant, with the actual fixed kick. Independently
evaluating the integer recurrence
$a_{j+1}=3a_j+2b_j$, $b_{j+1}=4a_j+3b_j$, starting at
$(a_0,b_0)=(1,0)$, gives
$$
\begin{aligned}
b_{49}&=22988051704762092309141120595493810884,\\
K_{49}^{\rm phys}
&=6537475987854975195262578684684149000168.
\end{aligned}
$$
This arithmetic is supplementary; the displayed finite sum already
defines the constant exactly. The conclusion
$$
N-K_{49}^{\rm phys}
\le\sum_{r>49}\|F_r(1)\|_{\rm HS}^2\le N
$$
uses no auxiliary phase averaging and no prime subsequence.

## 5. Phase fourth moment

For a fixed $j$, the product of two positive and two negative
paths has $4j$ entries of $U$. There are $N^2$ endpoint
choices and $N^{2j-2}$ positive internal path choices. Phase
integration forces the two concatenated negative paths to use the
same internal occupation multiset, which has at most
$(2j-2)!$ ordered realizations. With $\max|U_{ab}|^2\le C/N$,
each summand has modulus at most $(C/N)^{2j}$. This proves
the exact upper bound $C^{2j}(2j-2)!$ after cancellation of all
powers of $N$. Repeated labels only reduce the number of ordered
realizations. The concatenation has a fixed split into the two
paths, so there is no extra splitting factor.

For $j=1$, $\sum P_{ab}^2\le C$ is the sharper direct
bound used by the source. Applying the pointwise short-return
inequality and then expectation gives the stated
$N-K_L(C)$ lower bound for every fixed finite $L$.
This expectation bounds an auxiliary positive energy. It is not
presented as an approximation to the original spectral law.

## 6. Prime example and its scope

For
$U_p=\mathcal F_p^*\operatorname{diag}(e_p(k^2))\mathcal F_p$,
the character calculation of the squared Gauss sum is valid for
every $p\nmid j$, since $2j$ is invertible. It gives
$R_j=J$ there, whereas $R_j=I$ for $p\mid j$.
Substitution into the full renewal recurrence, for every positive
length and not just the first period, verifies uniquely
$$
F_1=J,\qquad F_p=I-J,\qquad F_r=0\quad(r\ne1,p).
$$
The energy at time $p$ is $p-1$, and the weighted sum
is $1+p(p-1)$, giving dark dimension $p-1$. The exact tail
formula yields
$a_m=(p-1)(p-m)$ for $0\le m\le p-1$, and
$a_m=p-1$ thereafter. This attains the dimension bound at
every nontrivial time in its range.

Replacing $k$ by $-k$ proves $U_p$ is symmetric, so
its reverse-transfer matrix is indeed $J$ with norm one.
For the more general quadratic flat kernel described in the source,
the reverse-transfer phases factor as a phase in the first index
times its conjugate in the second; its rank is one and its norm
is one. The example therefore supplies exactly the obstruction
claimed, and does not establish the same obstruction subject to a
small reverse-transfer norm. It is not a countersequence for the
prescribed family.

## 7. Literal bounded-run resummation

In a row-indexed trace word, the source's blocks allow transitions
$M\to O_1$, $O_j\to O_{j+1}$, and $O_j\to M$, with
the physical weights $B,S,C$, together with $M\to M$ of
weight $P$. There is no directed cycle wholly among the age
copies. Every physical cyclic pair with an agreement and maximum
disagreement-run length $L$ has a unique age assignment: each
age is its distance from the preceding cyclic agreement. This is
true even when the chosen root lies in a run, physical vertices
repeat, or the word has a smaller period. It proves equality of the
rooted trace expansion with the stated literal class. The class
of pairs with no agreement remains excluded.

Eliminating the strictly upper-triangular age block gives
$$
\det(I-sA_L)
=\det\left(I-sP-\sum_{r=2}^{L+1}s^rBS^{r-2}C\right).
$$
The finite companion has the same determinant. Formal expansion
of $-\log\det$ therefore gives equality of all positive-power
traces. Independent coordinate-phase integration extracts exactly
equal occupations; its subtraction leaves the specified actual
unequal-occupation class. No marking factor, normalization by the
number of agreements, or limiting resolvent is used.

The source correctly stops before asserting a bound on the complete
signed contribution of long runs. Its positive energy lower bounds
and exact unit singular values disallow the particular proposed
argument based on making all omitted return norms small. They
prove neither a positive lower bound for that signed contribution
nor a failure of $H_{\rm diag}$.
