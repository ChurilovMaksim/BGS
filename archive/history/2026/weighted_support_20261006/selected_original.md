# One fully weighted homoclinic coefficient and its cyclic TRACE-005 subsum

Assembled theorem, 6 October 2026, frozen for an independent interface review.
The physical W1–W15, quantum Q1–Q10 and classical EQ dependencies each have
separate positive independent verdicts. The proof below combines those exact
inputs and states its representation and bandwidth limits. No canonical edits.

## 1. Representation, quantifiers, and exact coefficient

Keep the actual odd-N quantizer, tau=10^-80, and any fixed finite WKB order
J>=0. Let V_(N,J) be the prescribed one-step four-branch WKB matrix. The exact
Gaussian-reciprocity representation defines alpha_(N,m,J) on
G_m=Fix(S^m on T²), D_m=|G_m|, by

 Tr V_(N,J)^m=zeta_(N,m) D_m^-1/2 sum_z e(NQ_m(z))alpha_(N,m,J)(z).

Define its SELECTED REPRESENTATION COEFFICIENT

 A_(N,m,J)(d)=e(NQ_m(d)) D_m^-1 sum_z alpha(z+d)conjugate(alpha(z))
                                                   e(N b_m(z,d)).  (S1)

Then |Tr V_(N,J)^m|²=sum_(d in G_m) A_(N,m,J)(d), exactly. This is a
representation-dependent coefficient of V_(N,J), not an intrinsic summand
or observable assigned to U_N's spectrum. The table remains nonunitary.

Let d_m=(S^m-I)^-1(0,1) mod Z². For every fixed 0<a0<=b0<=2, the assembled
claim is

 sup_(a0 N<=m<=b0 N) |A_(N,m,J)(d_m)| <=C_(J,a0,b0) N^-1/2,          (S2)

through odd N, for sufficiently large N. Constants may depend on the fixed
model, J and the band. J never grows with N. No gcd restriction is imposed.
In fact the proof gives, uniformly for 1<=m<=2N,

 |A_(N,m,J)(d_m)|<=C_J[N^-1/2+N e^-cm+sqrt(N)e^(-4N/5)].            (S3)

Local exact-box coefficients have the same Heisenberg conclusion in any fixed
positive m/N band. The global Fresnel coefficient comparison used in S1–S3
is certified here only in the conservative m<=2N contour band.

## 2. Leading weight and the physical marked observable

W1–W3 identify the positive leading amplitude exactly as

 w_0(z)^2=D_m rho_m(z),
 rho_m(z)=|det(I-DF^m(chi(z)))|^-1.

Write Z_m^cl=sum_z rho_m(z). The norm-uniform classical EQ gives
Z_m^cl=1+O(e^-cm), in particular sup_m Z_m^cl<infinity.
The leading selected coefficient is

 A_0=e(NQ_m(d_m)) sum_z rho_m(z)
       sqrt(rho_m(z+d_m)/rho_m(z)) e(N[q+D_m(z)]).                   (S4)

The geometric mean is retained. W4–W11 identify its homoclinic limit in
physical coordinates x=chi(z):

 A(x)=integral_0^1 Q_s(x)ds,
 Psi_d(x)=(Q_1(x),p_s(Q_1(x);x)) mod1,
 J_d=det D Psi_d>0.

Here Q_s solves p_u(Q_s;x)-p_s(Q_s;x)=s on the specified lifted leaves.
The independently checked physical estimates give A-q-1/(2sqrt(2)) in
C^(1,1/2), partial_q A>=1/2, and sqrt(J_d) in C^(0,1/2), with fixed bounds.
The finite phase and ratio in S4 differ uniformly from
sqrt(J_d(x))e(NA(x)) by O(N e^-cm), after decreasing c>0 if necessary.

Its C^(0,1/2) norm is O(1+N), so the NORM-UNIFORM EQ applies to this changing
oscillatory test. It yields

 A_0=integral_(T²)sqrt(J_d(x))e(NA(x)) dx+O(N e^-cm).                 (S5)

Changing variable q->A(q,p) on each fibre produces a C^(0,1/2) density with
uniform norm. A half-period Fourier translation proves that the integral is
O(N^-1/2). Thus the leading coefficient obeys the first two terms of S3.
This uses invariant physical area and the homoclinic half-density. It does
not reuse the Haar-label pushforward mu_tau as if it were the same measure.

## 3. Exact finite-h quantum factor; no orbit-count loss

Use h=(2*pi*N)^-1; the finite amplitude polynomial is
sum_(ell=0)^J (2*pi*h)^ell a_ell. The exact-box coefficient has

 alpha_box(z)=e(NDelta_m(z))w_0(z)P_z Z_z,

where P_z is the full Gaussian probability of the retained box and Z_z is
the exact conditioned expectation. Q1–Q10 establish

 ell_1(z) is imaginary,
 ell_1(z+d_m)-ell_1(z)=O_J(1),
 P_(z+d_m)P_z Z_(z+d_m)conjugate(Z_z)=1+O_J(N^-1/2)                 (S6)

uniformly for m<=2N. They use the actual Weyl transport, literal winding
interpolation and finite connected Wick contractions. The individual Z_z
is not replaced by one; its first extensive phase can remain O(1).
Nonvanishing for large N follows from the accepted relative first-loop
estimate, not from an assumed denominator bound.

Cauchy–Schwarz, applied to the already normalized selected coefficient, gives

 |A_box-A_0|<=C_J N^-1/2 sum_z sqrt(rho_m(z+d_m)rho_m(z))
             <=C_J N^-1/2 Z_m^cl=O_J(N^-1/2).                       (S7)

No exponential count of classes multiplies this estimate. Only the bounded
positive mass is used here; full EQ was needed earlier for S5.

The global contour proof's SUMMED ABSOLUTE tails imply
D_m^-1/2 sum_z |alpha_global(z)-alpha_box(z)|
 <=C_J sqrt(N)e^(-4N/5). Their normalized l2 norm is bounded by the same
quantity. Meanwhile the normalized l2 norm of alpha_box is bounded by S6
and Z_m^cl. The shift in S1 is an l2 isometry. A two-factor Cauchy–Schwarz
comparison therefore bounds the global-versus-box selected coefficient by
C_J sqrt(N)e^(-4N/5). This completes S3 and hence S2.

## 4. A growing full-weight displacement subsum on the target normalization

Let O_m={S^j d_m:0<=j<m} union {-S^j d_m:0<=j<m}, counting each distinct
physical displacement ONCE. Thus |O_m|<=2m. Exact cyclic relabelling of the
branch integrals gives alpha(Sz)=alpha(z). Q and b are S-invariant, so

 A(S^j d_m)=A(d_m),  A(-d_m)=conjugate(A(d_m)).                       (S8)

For n=(S^m-I)z in Z², the direct refinement calculation gives
Q_m(Sz)-Q_m(z)=-3n_q²-10n_q n_p-6n_p² modulo integers. Cyclic
permutation preserves the product measure, leading/global amplitudes, centered
Abel regularization and retained boxes; integer gluing introduces no extra
amplitude factor. These facts justify alpha(Sz)=alpha(z), including the
exact global integral convention. The negative identity follows by changing
z to z-d in the autocorrelation. No new analytic estimate is required. The orbit lies
outside ker N for odd N: N S^j d_m=0 would imply Nd_m=0, contrary to its
p-coordinate -1/2. The complete resonant sector is not discarded.

For every fixed smooth w compactly supported in (0,2), S2 and |O_m|<=2m give

 N^-2 sum_m w(m/N) sum_(d in O_m) A_(N,m,J)(d)=O_(J,w)(N^-1/2).       (S9)

This is the ORIGINAL unnormalized outer displacement sum on this family,
followed by the TRACE-005 time normalization. It is not a displacement
average. In particular it applies to the central pair window w supported
in (0,1/2). It controls a growing full-weight family of at most 2m terms;
it says nothing comparable about exponentially many other displacements.

## 5. Aggregate transfer to U and the remaining target

For fixed J>=1, the accepted operator telescoping estimate in m<=2N is

 |Tr U_N^m-Tr V_(N,J)^m|<=C_J N^(3/2-J),
 |Tr V_(N,J)^m|<=2N for large N.

Consequently the normalized compact-time pair aggregate differs by
O_(J,w)(N^(3/2-J)). For J>=2 this is O(N^-1/2). Combining with S9 reduces
the central U pair comparison, at this error, to the V representation sum
on G_m\O_m, with its CUE benchmark unchanged. This is an aggregate comparison;
there is no asserted orbitwise decomposition for U itself. Higher fixed
factorial orders still use the separate J>=k trace-table theorem.

The complement contains the N-torsion projection, dense/multiple defects,
and the signed cancellations needed for the m benchmark. This theorem does
not settle TRACE-005, the factorial hierarchy or BGS.

## 6. Source and audit boundary for the final version

- Physical W1–W15 review: 8d64e064a3a4aa66be6391ff15bdbb50b117dc8d6957f9d255691dcda80ba059.
- Quantum Q1–Q10 review: fbebcb9aebad1ab23a2fb97c53f11ea63f099bfee4c03c7284128263f77ff7c2.
- Classical EQ final review: 9a6a9faf045de64ceb46a37f11a1bfc3f7d2ca1d519e02da1efc435b80e02e8e.
- Entropy provenance must cite the actually verified Mane1981 formula,
  printed p.95 equation(2), together with mandatory Mane1983 errata pp.159–160.
  The old Pesin1977 Thm5.1/p.81 locator remains unretrieved/unverified; the
  replacement source does not retroactively verify that locator.

The entropy formula is sourced to Ricardo Mañé, *A proof of Pesin's formula*,
ETDS 1 (1981), printed p.95 equation(2), DOI
https://doi.org/10.1017/S0143385700001188, read with his mandatory *Errata*,
ETDS 3 (1983), printed pp.159–160, DOI
https://doi.org/10.1017/S0143385700001863. Both cached primary PDFs and the
classical review are pinned in `selected_weighted_sources.json`. The periodic
transfer source is Parry–Pollicott (1990), Theorem5.5(ii) and its proof, plus
AppendixIII, with exact locators/source mapping in the classical EQ proof.

Exact finite controls `check_selected_cyclic_family.py` and its JSON record
cover m=1,...,64, including short orbit overlaps and composite odd-N tests.
They check algebraic family bookkeeping only; the analytic bounds are proved
above from the separately audited inputs.
