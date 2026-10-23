# Exact fresh-phase drift of the two-step intensity kernel

**Claim:** BGS-TRACE-075. **Status:** project proof with independent internal
reconstruction after an explicit frozen-label correction. Finite controls
have separate scope; priority is not established.

The theorem gives a one-step restoring mean estimate for large two-step
peaks. It does not prove trajectory concentration or all-time entry
flatness. Its main inequality is self-contained; TRACE-074 is used only
for the final constructed-witness application.

## 1. State, randomness and exact convention

Let \(S\in U(u)\), \(u\ge3\), and put
\[
 P_{k\ell}=|S_{k\ell}|^2,\qquad K=P^2,\qquad
 \delta=\max_{k,\ell}P_{k\ell}<1.
 \tag{1}
\]
Fix distinct labels \(i,j\). Choose \(e\) uniformly among **all** \(u\)
labels and an independent uniform \(w\in\mathbb T\). If \(e=i\) or \(e=j\),
set \(K'_{ij}=K_{ij}\). Otherwise form the survivor unitary
\[
 S'_{k\ell}=S_{k\ell}+q_e S_{ke}S_{e\ell},\quad
 q_e=\frac{w}{1-S_{ee}w},\quad k,\ell\ne e,
 \qquad K'_{ij}=\sum_{k\ne e}|S'_{ik}|^2|S'_{kj}|^2.
 \tag{2}
\]
The denominator is nonzero because \(|S_{ee}|<1\).
All expectations below are conditional on the input \(S\).

Define
\[
 c(\delta)=\frac{2\delta}{(1-\delta)^2}
          +\frac{\delta(1+\delta)}{(1-\delta)^3},\qquad
 d(\delta)=\frac4{1-\delta}+\frac{2\delta}{(1-\delta)^2}.
 \tag{3}
\]
Then
\[
 u\,\mathbb E(K'_{ij}-K_{ij}\mid S)
 \le -(1-c(\delta))K_{ij}+2\delta P_{ij}
                     +d(\delta)(P^3)_{ij}.
 \tag{4}
\]
In particular, if \(\delta\le1/16\),
\[
 \boxed{\mathbb E(K'_{ij}-K_{ij}\mid S)
 \le\frac{-K_{ij}/2+5(P^3)_{ij}+2\delta P_{ij}}u.}
 \tag{5}
\]

## 2. Exact phase average, including the deleted diagonal

Fix \(e\notin\{i,j\}\) and \(k\ne e\). Write \(a=S_{ee}\) and
\(\eta_e=1-|a|^2\), and introduce
\[
 A=S_{ie}S_{ek}\overline{S_{ik}},\quad B=P_{ie}P_{ek},\qquad
 C=S_{ke}S_{ej}\overline{S_{kj}},\quad D=P_{ke}P_{ej}.
 \tag{6}
\]
The two updated intensities are
\[
 P'_{ik}=P_{ik}+qA+\bar q\bar A+|q|^2B,\qquad
 P'_{kj}=P_{kj}+qC+\bar q\bar C+|q|^2D.
 \tag{7}
\]
Geometric Fourier series, absolutely convergent for \(|a|<1\), give
\[
 \mathbb Eq=\mathbb Eq^2=0,\quad
 \mathbb E|q|^2=\eta_e^{-1},\quad
 \mathbb E(q|q|^2)=\bar a\,\eta_e^{-2},\quad
 \mathbb E|q|^4=(1+|a|^2)\eta_e^{-3}.
 \tag{8}
\]
For example, the last two sums are
\(\bar a\sum_{m\ge0}(m+1)|a|^{2m}\) and
\(\sum_{m\ge0}(m+1)^2|a|^{2m}\).
Multiplying (7) and using (8) yields the exact formula
\[
 \begin{split}
 F_{e,k}:=\mathbb E_w(P'_{ik}P'_{kj})
 ={}&P_{ik}P_{kj}
       +\frac{P_{ik}D+P_{kj}B}{\eta_e}
       +\frac{2\operatorname{Re}(A\bar C)}{\eta_e}\\
    &+\frac{2\operatorname{Re}\{\bar a(AD+CB)\}}{\eta_e^2}
       +\frac{(1+|a|^2)BD}{\eta_e^3}.
 \end{split}
 \tag{9}
\]

The correct coordinate average for the frozen-label convention is
\[
 u\,\mathbb E(K'_{ij}-K_{ij}\mid S)
 =\sum_{e\notin\{i,j\}}
       \left[\sum_{k\ne e}F_{e,k}-K_{ij}\right].
 \tag{10}
\]
The subtraction is inside this sum. Averaging only the survivor cases
and then subtracting \(K_{ij}\) once would lose the frozen cases'
\(2K_{ij}/u\) contribution. Conditioning on survival is a different
convention with denominator \(u-2\).

## 3. The complete coherent term is a path-swap pairing

Let
\[
 T_{e,k}=S_{ie}S_{ek}S_{kj},\qquad
 \mathcal D=\{(e,k):e\notin\{i,j\},\ k\ne e\}.
 \tag{11}
\]
Then \(A\bar C=T_{e,k}\overline{T_{k,e}}\). Although \(\mathcal D\)
need not be invariant under the swap \((e,k)\mapsto(k,e)\), both
\[
 \sum_{\mathcal D}|T_{e,k}|^2\le(P^3)_{ij},\qquad
 \sum_{\mathcal D}|T_{k,e}|^2\le(P^3)_{ij}
 \tag{12}
\]
hold because each is a subsum of the complete nonnegative three-step
path sum. Since \(\eta_e\ge1-\delta\), weighted Cauchy--Schwarz gives
\[
 \left|\sum_{\mathcal D}\frac{A\bar C}{\eta_e}\right|
 \le\frac{(P^3)_{ij}}{1-\delta}.
 \tag{13}
\]
This estimate controls the entire coherent sum without discarding its
phases term by term. It uses the same three-step intensity kernel that
can be controlled by the positive singular-norm estimate of TRACE-074.

## 4. Bounds for the remaining terms

The base part of (10) is exactly
\[
 -\sum_{e\notin\{i,j\}}P_{ie}P_{ej}
 =-K_{ij}+P_{ij}(P_{ii}+P_{jj})
 \le-K_{ij}+2\delta P_{ij}.
 \tag{14}
\]
The two positive quadratic terms in (9), summed over \(\mathcal D\),
are at most
\[
 \frac1{1-\delta}
 \sum_{e,k}(P_{ik}P_{ke}P_{ej}+P_{kj}P_{ie}P_{ek})
 =\frac{2(P^3)_{ij}}{1-\delta}.
 \tag{15}
\]

The nonzero-\(a\) cubic phase terms require separate control. Factor
\(\sqrt{P_{ee}P_{ke}}\le\delta\) to obtain
\[
 |aAD|
 \le\delta P_{ej}\sqrt{P_{ie}P_{ek}P_{ik}P_{ke}}
 \le\frac\delta2 P_{ej}(P_{ie}P_{ek}+P_{ik}P_{ke}).
 \tag{16}
\]
Summing and using row/column sums equal to one yields
\[
 \sum_{\mathcal D}|aAD|
 \le\frac\delta2\{K_{ij}+(P^3)_{ij}\}.
 \tag{17}
\]
Similarly, factor \(\sqrt{P_{ee}P_{ek}}\le\delta\):
\[
 |aCB|\le\frac\delta2 P_{ie}(P_{ke}P_{ej}+P_{kj}P_{ek}),\qquad
 \sum_{\mathcal D}|aCB|
 \le\frac\delta2\{K_{ij}+(P^3)_{ij}\}.
 \tag{18}
\]
Their total contribution to an upper bound is therefore at most
\[
 \frac{2\delta}{(1-\delta)^2}\{K_{ij}+(P^3)_{ij}\}.
 \tag{19}
\]
Finally,
\(\sum_{k\ne e}P_{ek}P_{ke}\le(P^2)_{ee}\le\delta\), so the quartic
term is at most
\[
 \frac{\delta(1+\delta)}{(1-\delta)^3}K_{ij}.
 \tag{20}
\]
Adding (13)--(20) proves (4). Both functions in (3) increase on
\([0,1)\); direct evaluation gives
\[
 c(1/16)=752/3375<1/2,\qquad d(1/16)=992/225<5.
 \tag{21}
\]
This proves (5).

## 5. A genuine restoring drift for the constructed peaks

For \(\rho=\|P-J_u\|_{\rm op}\), the higher-step bound proved in
[TRACE-074](unitary_two_step_obstruction_20261012.md) implies
\[
 (P^3)_{ij}\le1/u+\rho(\delta-1/u).
 \tag{22}
\]
Consequently (5) also yields
\[
 \mathbb E(K'_{ij}-K_{ij}\mid S)
 \le-\frac{K_{ij}}{2u}+\frac5{u^2}
       +\frac{5\rho(\delta-1/u)}u+\frac{2\delta P_{ij}}u.
 \tag{23}
\]
Logarithmic flatness alone does not make the third term \(O(u^{-2})\);
one would additionally need a bound such as \(\rho\log u=O(1)\).
We have not proved that condition for the maintained evolving map.

At the specific TRACE-074 witnesses,
\[
 P_{ij}=0,\quad K_{ij}=1/\lfloor u/\log(2u)\rfloor,\quad
 (P^3)_{ij}=(1+o(1))/u,\quad \delta\le8\log(2u)/u.
 \tag{24}
\]
Thus \(\delta\le1/16\) eventually and, for all sufficiently large \(u\),
\[
 \mathbb E(K'_{ij}-K_{ij}\mid S)\le-\frac{K_{ij}}{4u}<0.
 \tag{25}
\]
In fact the exact base term is \(-K_{ij}\), and the absolute sum of all
other contributions in (10) is bounded by
\(c(\delta)K_{ij}+d(\delta)(P^3)_{ij}=o(K_{ij})\).
Therefore these witnesses obey the sharper asymptotic
\[
 \mathbb E(K'_{ij}-K_{ij}\mid S)
 =-(1+o(1))K_{ij}/u.
 \tag{26}
\]
This is a one-step mean statement for each constructed input. It does
not assert that the hypotheses persist, that a typical sample decreases,
or that no new peaks are created elsewhere.

## 6. Review, computation and the remaining implication

The [review packet](../archive/evidence/executions/20261012/two-step-drift/README.md)
preserves the original candidate and the correction to its averaging
sentence. The core proof uses only the finite feedback formula, circle
Fourier moments, bistochasticity, weighted Cauchy--Schwarz and AM--GM.
Its witness corollary uses TRACE-074; no other conditional result or
external concentration theorem is an input.

Independent exact controls use complex rational residue calculations
with nonzero deleted diagonals, and four ordered pairs in an explicit
64-dimensional real unitary with intensity bound \(1/50\). Those finite
checks do not prove the general theorem or a probability estimate.

The estimate identifies a restoring mechanism that is absent from a
purely static argument. Higher-moment control and concentration for the
coupled evolving entry and two-step kernels remain open. No all-time
flatness probability, physical microscopic cavity law, full TRACE-055,
signed TRACE-005, global BGS, analytic Lean or priority claim is made.
