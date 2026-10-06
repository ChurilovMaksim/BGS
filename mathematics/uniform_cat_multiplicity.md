# Uniform bounded cat eigenspaces on N=7*5^e

Status: independently accepted project proof within the stated component scope. It is not a simplicity assertion about the kicked U_N.

## Prime-power cat spectrum is simple

Let P=5^(e-1), n=5^e and R=6P. The actual cat matrix S=[[3,4],[2,3]] has order6 modulo5. Moreover

    (S^6-I)/5 = [[3920,5544],[2772,3920]]

has invertible reduction modulo5. Binomial expansion then gives
S^(6j)-I=5^(1+v5(j)) B_j, where B_j is integral and invertible modulo5, for j!=0 before the return. This is a common matrix factor, not equality of every individual entry valuation. Thus the order modulo5^e is exactlyR.

The maintained raw-Weyl identity is

    |Tr M_n^k|²=|ker(S^k-I modulo n)|.

For 0<=k<R this equals1 when6 does not divide k. For k=6j, j!=0, it is5^(2(1+v5(j))); at k=0 it is5^(2e). Therefore

    sum_(k=0)^(R-1)|Tr M_n^k|²
      =5P+5^(2e)+sum_(s=0)^(e-2)4*5^(e-2-s)*5^(2s+2)
      =6*5^(2e-1)=R*n.

Since M_n^R is scalar, rescale it by a scalar phase to have order dividingR. Character orthogonality on this finite cyclic group gives

    sum_lambda multiplicity(lambda)²
      =(1/R)sum_(k=0)^(R-1)|Tr M_n^k|²=n.

The multiplicities are nonnegative integers summing to n. Hence every nonzero multiplicity is1: M_(5^e) is simple for all e>=1. The argument applies to every primitive-root version of the raw kernel, because exact Weyl covariance and the fixed-point count are unchanged.

## CRT gives a seven-dimensional bound

The Chinese remainder permutation of coordinates for N=7n factors the raw quadratic kernel into a tensor product of the raw kernels for7 and n, each evaluated at a primitive-root power determined by the CRT idempotents. Cross quadratic terms vanish moduloN. Dividing by positive sqrt(N)=sqrt(7)sqrt(n) gives the same unitary tensor factorization. No unspecified metaplectic phase convention is needed.

The seven-dimensional factor has three eigenvalues, proportional to1,omega,omega², with multiplicities3,2,2. The n-dimensional factor is simple by the preceding trace computation. A given product eigenvalue can use at most one n-factor eigenvalue for each of the three seven-factor eigenvalues. Consequently

    every M_(7*5^e) eigenspace has dimension at most7.

This is a uniform exact bound, not extrapolation from N35 and175.

## Exact multiplicity distribution

The full cat still has scalar return orderR. Modulo7, S has order3. In the same trace sum, the k congruent3 modulo6 contribute49 instead of1, and k divisible6 contribute49 times their5-primary fixed-point count. The other four classes modulo6 contribute1. Hence

    (1/R)sum_(k=0)^(R-1)|Tr M_(7n)^k|²=49n-32.

Let E be the set of the n distinct eigenvalues of the prime-power factor, after a common scalar normalization. Multiplication by omega permutes the ambient Rth-root coset, since3 dividesR. On an orbit of size3, the occupancy of E is0,1,2,or3. The tensor multiplicities contributed are:

- occupancy0: none;
- occupancy1: (3,2,2), total dimension7, square sum17;
- occupancy2: (4,5,5), total dimension14, square sum66;
- occupancy3: (7,7,7), total dimension21, square sum147.

Each partial orbit has deficit32 between seven times its total dimension and its square sum; full orbits have deficit zero. The global deficit is
7*(7n)-(49n-32)=32. Therefore exactly one orbit is partial. Since n=5^e is2 modulo3 for e odd and1 modulo3 for e even:

- e odd: n-2 eigenspaces have dimension7, and the remaining three have dimensions4,5,5;
- e even: n-1 eigenspaces have dimension7, and the remaining three have dimensions3,2,2.

Thus the exact first-order discriminant problem reduces to a family of matrices of size at most7, with only one exceptional three-block orbit at each depth. Their entries and spectra still need actual coefficient control; this multiplicity result does not prove any compression simple.

## Source boundary

The trace fixed-point identity is the existing raw-Weyl theorem in mathematics/frozen_arithmetic_trace_rigidity.md. The N7 multiplicities use the separately reviewed characteristic-zero raw-kernel certificate. The CRT factorization is direct substitution in the unchanged quadratic kernel. No external torus/Weil multiplicity theorem is invoked, and none is needed for this bound.

## Publication and dependency scope

This exact source has its separately pinned independent review in the
cat/jet promotion map. The final accepted combined FM-026 statement is in
[the theorem owner](literal_time_multiplicity_bounds.md). Conditional sector
premises retain their historical proof structure and are used only where
the separately accepted premise is explicitly bound. No unpublished CRT or
first-old-layer diagnostic is a new theorem input or extra U dimension.
