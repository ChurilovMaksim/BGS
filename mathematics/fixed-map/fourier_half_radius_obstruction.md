# Exact half-radius obstruction under a one-step singular gap

Separate author addendum, 7 October 2026. This is not an input to frozen `candidate_v1.md`, and it makes no claim about the actual frozen BGS map. It shows that the radius boundary of the one-step mechanism is genuine, even for perfectly flat actual unitary matrices rather than abstract block-unitary surrogates. Independently reviewed; see record/half_radius_obstruction_review.md.

## Claim

Let F_N(a,b)=N^(-1/2) exp(2pi i ab/N), N>=2, and let O_r be the literal off-charge coordinate-Hamming projector in candidate Section1. For every m>=4 divisible by4, at r=m/2,

 Tr_E[R O_(m/2) Ad(F_N^tensor m)]
   >=2(N-1)(1-1/N).                                        (B1)

The quantity is real and nonnegative. Yet P_(F_N)=J exactly, so the one-step singular norm t is zero. In particular, no theorem based only on small one-step t can assert exponential cyclic-trace decay for every such unitary at radius m/2, including on m~N with N odd.

## Proof

Use the local p/q decomposition from the frozen candidate: p projects onto traceless diagonals D0, q onto offdiagonal matrices O, A=Ad(F_N)|_V, and d=N-1. Because F_N is flat,

 p A p=0.

As in the candidate, proper traceless supports contribute zero to the off-charge full-cycle trace. On the top support, write the raw Hamming projector F as a sum of p/q position patterns with at most r=m/2 marked q positions.

In the cyclic local product for any pattern, two adjacent p positions force a p A p factor, so that pattern contributes zero. A cyclic binary word of even length m with at least m/2 p positions and no adjacent p must have exactly m/2 of each symbol and alternate. There are precisely two alternating patterns. Since A p lies in ran q, and F_N^2=R_N is the coordinate reflection a->-a,

 Tr[R F A^tensor m]
   =2 Tr_(D0)[(p A^2 p)^(m/2)]
   =2d,                                                    (B2)

because m/2 is even and Ad(R_N)^2=I.

Now insert exact total-charge balance Pi=integral D_z^tensor m dz, with Z=diag(z_0,...,z_(N-1)) and independent uniform unit phases z_j. Since pD_z=p, two adjacent p positions still kill the corresponding balanced integrand. The two alternating patterns give

 Tr[R Pi F A^tensor m]
   =2 integral Tr_(D0)[(p A D_z A p)^(m/2)] dz.             (B3)

Indeed q commutes with D_z and A p lies in q, so the q in p A q D_z A p can be removed. The compression in (B3) is exactly

 T_z=P_(F_N Z F_N)-J restricted to D0.

Define

 w_s=|N^(-1) sum_j z_j exp(2pi i sj/N)|^2,
 c_k=N^(-1) sum_j z_j conjugate(z_(j-k)),

with all indices modulo N. Then P_(F_N Z F_N)(a,b)=w_(a+b). It is the product of the circulant matrix C(a,b)=w_(a-b) and reflection R_N. Its Fourier coefficients are c_k (up to the harmless sign convention), with c_0=1 and c_-k=conjugate(c_k). Therefore, for every even q>=2,

 Tr_(D0) T_z^q=sum_(k=1)^(N-1) |c_k|^q.                   (B4)

This remains true at an even-N self-opposite mode: its Fourier coefficient is real and its even power equals its absolute even power. In particular the trace in (B3) is nonnegative.

Each |c_k|<=1. For k!=0, independent phase integration gives exactly

 integral |c_k|^2 dz=1/N.                                  (B5)

To verify (B5), expand its N² terms. A term indexed j,l survives only when the exponent multisets {j,l-k} and {j-k,l} agree. Since k!=0, this forces j=l, leaving N terms each equal to1/N². There is no extra self-opposite-mode term.

Since q=m/2 is even and q>=2, (B4)–(B5) yield

 0<=Tr[R Pi F A^tensor m]<=2(N-1)/N.                       (B6)

Subtract (B6) from (B2), using the exact raw identity O_(m/2)=(I-Pi)F, to obtain (B1).

At m=4, equality holds in (B1), because q=2. This equality supplies the smallest nontrivial exact check.

## Meaning and boundary

This gives an exact sharp obstruction at the half-coordinate threshold to any proposed extension using only the one-step position-chain singular norm. It neither refutes the frozen actual BGS map nor says that no other mechanism can cross half. The Fourier matrix has F_N^2 equal to a coordinate permutation, so its two-step compression p Ad(F_N)^2 p has norm1. In particular, stronger estimates on p Ad(U_N)^k p for actual quantum powers k>=2 could distinguish this obstruction. Such estimates concern |(U_N)^k|^2, not the Markov power (|U_N|^2)^k; they are not provided by FM021 and are not assumed in the fixed-fraction theorem.

The separate actual FM022 reverse-path input may also distinguish this symmetric Fourier obstruction, but no implication from it to arbitrary high-Hamming trace control is proved here.
