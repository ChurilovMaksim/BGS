# Combining the odd newest sector and residual-125 core

Status: independently checked combination of accepted component theorems. This
short corollary adds no local splitting theorem, external input, or new matrix
certificate. Its source and review bindings are in
`record/odd_sector_count_combination_review.md`.

Let e be odd, n=5^e, N=7n, and U_N(t)=exp(itA_N)M_N in the unchanged raw model.
At every nonzero real algebraic t, including t=10^(-80)N, U_N(t) has at least

- 24N/25 simple eigenvalues for odd e>=3;
- 24N/25+35 simple eigenvalues for odd e>=5;
- 24N/25+875 simple eigenvalues for odd e>=7.

The last addend is 875=840+35. It replaces the second addend, so the deepest
35 dimensions must not be counted twice.

## Proof of disjointness and addition

Write W_k=H7 tensor J_k H_(5^(e-2k)). The accepted oldform theorem says each
W_k is a sum of complete M_N eigenspaces. Composition of its displayed
isometries gives J_j=J_1 J_(j-1), with the second map at modulus n/25.
Consequently W_j is contained in W_1 for every j>=1 in its allowed range.

The accepted odd newest-sector theorem splits every complete cat group in
W_1-perpendicular at first order, accounting for 24N/25 dimensions. For e>=5,
the accepted deepest odd core is W_r with r=(e-1)/2>=2. It is contained in W_1
and has six complete groups of dimensions 7,7,7,4,5,5. Their independently
proved simple second-order phase matrices add 35 dimensions.

For e>=7, put j=(e-3)/2>=2. Then W_j=H7 tensor J_j H125 has dimension 875.
Its subspace W_(j+1)=H7 tensor J_(j+1) H5 is exactly the deepest odd core of
dimension 35. The accepted residual-125 theorem splits the 120 complete
seven-dimensional groups in W_j minus W_(j+1), a total of 840 dimensions,
at second order. The deepest-core theorem splits the remaining six complete
groups. These are disjoint complete groups within W_1. None can share an
initial cat eigenvalue with a group in W_1-perpendicular: completeness and
orthogonality would otherwise require one full eigenspace to lie in both.

For each fixed N there are finitely many initial cat eigenvalues. Distinct
ones remain separated for sufficiently small real t. Within each selected
group, the accepted simple first- or second-order leading phase matrix
separates all local branches for sufficiently small nonzero real t. Choose
one such t for all selected groups. The number of simple eigenvalues of the
full unitary U_N(t) is therefore at least 24N/25+840+35.

Apply the already accepted rank-transfer theorem to
B(t)=chi_t'(U_N(t)). At real t its rank is precisely the number of simple
eigenvalues. Each minor is a finite exponential polynomial with algebraic
coefficients and collected algebraic frequencies, so the inherited registered
Lindemann-Weierstrass theorem transfers this witnessed rank bound to every
nonzero real algebraic t. The first two bounds follow in the same way from
their indicated subsets of complete groups.

This proof counts branches originating in complete cat groups. It does not
assert that the oldform spaces stay invariant at the target time. It gives
no full simplicity, quantitative gap, spacing statistic, or BGS conclusion.
The first-old follow-on is not a premise.
