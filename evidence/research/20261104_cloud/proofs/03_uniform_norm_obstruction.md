# The uniform step-norm cannot prove an H1 shell

Status: **[P]** as a method obstruction, conditional on the registered step-norm bound N_H ≤ 2.91656 (BGS-TRACE-323, recomputed in the lineN21b audit) and on the H1 shell budget at ρ = 0.28, C = 0.082. The numerical comparison is [CA].

## Statement

Let θ = log_ε 2 and let s(j) = ⌊θ j⌋ + 3, which is an upper bound on the ε-span in shell j (span theorem). Let N_max = 2.91656. Suppose a proof of the shell bound

S_2(j) = Σ_{bad, shell j} |r_A r_B|^2 ≤ C · 2^{j(1−β)}, C = 0.082, β = 2 ln(1/0.28)/ln λ,

proceeds by estimating each summand by N_max raised to twice the number of operator factors, and that this number of factors is at least the span. Then the resulting majorant of a single class is already larger than the whole shell budget for every j ≥ 1.

## Comparison

The ratio of that one-class majorant to the shell budget is

R(j) = N_max^{2 s(j)} / (C · 2^{j(1−β)}).

`numerics/kp_sharp.py` evaluates R in flint ball arithmetic at precision 200. The logarithm satisfies

log_{10} R(1) > 4.009, log_{10} R(6) > 8.396, log_{10} R(11) > 12.784,

and the same lower bound increases by about 4.39 for each further five shells. In particular R(j) > 1 for every j from 1 through 40, which is the range that was computed. The pattern is a fixed positive Lyapunov gap: 2 θ ln N_max + (β − 1) ln 2 > 0, since θ > 0.786, ln N_max > 1.07, and 1 − β < −0.444.

## Reading

Any chain of inequalities that passes through N_max^{2 s(j)} is too coarse to land under the H1 budget, already at the first shell, for one orbit. Extra padding factors, each at most N_max and at least the near-zero steps of the core window, make the majorant larger.

The certified core sums are of a different size. At shell j = 12, Thm A records S_2 ≤ 5.08×10^{-7}, while the one-class majorant is many orders of magnitude above the budget C · 2^{12(1−β)}. The gap is the contraction of the complement of the model channel, which a uniform bound on N_H does not see.

This is the same phenomenon as obstruction O1 on the λ-carry graph, moved to the length scale that the span theorem makes explicit. A proof of H1-bad has to keep the phase, or use a cone that contracts on words with no ε-zero run of length g_0, in the sense of the renewal Lemma R. Inserting 2.91656 on each letter does not.

The obstruction is silent on whether H1 is true.
