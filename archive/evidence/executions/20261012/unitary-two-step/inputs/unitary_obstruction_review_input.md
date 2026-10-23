# Unistochastic two-step obstruction by two unitary corrections

Research candidate, 11 October 2026. This concerns a shortcut for entry-flatness,
not a counterexample to random Schur evolution or BGS.

For every sufficiently large n there exists an n-by-n unitary S with
P_kl=|S_kl|^2, max P_kl<=8 log(2n)/n, ||P-J_n||_op->0 along the sequence,
but n(P^2)_ij grows at least like log(2n), for two distinct indices i,j.
Thus unitarity, all-entry flatness at log(n)/n and a vanishing intensity
singular norm do not imply an O(1/n) two-step kernel.

Fix B disjoint from i,j, b=floor(n/log(2n)), and unit vectors a,bvec
supported on B with all nonzero entries equal to b^(-1/2).
Require e_i^*S=a^*, S e_j=bvec. These constraints are compatible since
a_j=(bvec)_i=0. Every unitary satisfying them has
(P^2)_ij=sum_{e in B}(1/b)^2=1/b exactly.

Construct S from a Haar unitary Z. For unit vectors c,d define
H(c,d)=I-(c-d)(c-d)^*/(1-d^*c), except H(c,c)=I.
It is unitary, maps c to d, and H-I has rank at most one. Indeed
||c-d||^2=(1-d^*c)+(1-c^*d); this gives H^*H=I, and Hc=d.
Set L=H(Z e_j,bvec), W=LZ. Then W e_j=bvec and r=W^*e_i
is a unit vector orthogonal to e_j. Set R=H(a,r) and S=WR.
R fixes e_j, R a=r, hence S e_j=bvec and S a=e_i, so
e_i^*S=a^*. The difference S-Z=(L-I)Z+LZ(R-I) has rank at most two,
operator norm at most two and Hilbert--Schmidt norm at most 2 sqrt(2).

The remaining block of S is a Haar unitary map from
{e_j,a}^perp to {bvec,e_i}^perp, of dimension n-2. Proof: given the
first Haar column c=Ze_j, the other columns form a uniform unitary
isomorphism onto c^perp. Multiplying by the deterministic L(c) gives
the corresponding uniform conditional law with column bvec. The
conditional residual is uniform given r=W^*e_i; the deterministic
R(r) sends a to r and fixes e_j, so it transports that residual Haar
isomorphism to the two fixed orthogonal complements.

Consequently S=bvec e_j^*+e_i a^*+V, where V is that uniform partial
unitary. For k!=i, l!=j, its entry is V_kl: both prescribed terms
vanish there. Each V_kl has the law of a scalar entry of a Haar
unitary of dimension n-2 times deterministic projection norms <=1.
Therefore for 0<t<1,
P(|V_kl|^2>t)<=(1-t)^(n-3).
The forced row and column entries are at most 1/b. For
t_n=8 log(2n)/n and large n, 1/b<=t_n and union bounds give
P(max |S_kl|^2>t_n)<=n^2 exp(-(n-3)t_n)->0.
Likewise P(max |Z_kl|^2>t_n)<=n^2 exp(-(n-1)t_n)->0.

We also derive, rather than import, the needed Haar intensity singular bound.
Let P_Z=|Z|^2 entrywise and E_Z=P_Z-J_n. Since P_Z is doubly stochastic,
Tr[(E_Z E_Z^*)^2]=Tr[(P_Z P_Z^*)^2]-1.
For one Haar row, p_l=|Z_1l|^2 has the Dirichlet(1,...,1) law.
Writing s_r=sum_l p_l^r,
E s_2=2/(n+1),
E s_3=6/[(n+1)(n+2)],
E s_2^2=4(n+5)/[(n+1)(n+2)(n+3)].
Given that row, a second orthogonal Haar row has projector Pi=I-aa^*.
Its sphere second moment gives
E[(sum_l p_l |Z_2l|^2)^2 |p]
=[(Tr(D_p Pi))^2+Tr(D_p Pi D_p Pi)]/[n(n-1)]
=[1-s_2-2s_3+2s_2^2]/[n(n-1)].
Summing the n same-row and n(n-1) different-row contributions yields
E Tr[(E_Z E_Z^*)^2]
=2(n-1)(n+4)/[(n+1)(n+2)(n+3)]<=C/n.
Thus P(||E_Z||_op>n^(-1/8))<=C n^(-1/2)->0.

On the two entry-flat events,
||P-P_Z||_op<=||P-P_Z||_HS
 <=(max |S_kl|+max |Z_kl|)||S-Z||_HS
 <=4 sqrt(2t_n).
Hence with probability tending to one the constructed S obeys
||P-J_n||_op<=n^(-1/8)+4 sqrt(2t_n)->0,
max P<=t_n, but (P^2)_ij=1/b on every such completion.
There is therefore a witness for every sufficiently large n.

Furthermore (P-J_n)^2_ij=1/b-1/n. Since max P<=t_n and b~n/log(2n),
no universal bound |(P-J_n)^2_ij|<=C ||P-J_n||_op max P can hold.
Both failed implications are now refuted inside the unistochastic class.

The construction changes a Haar unitary by rank at most two. It illustrates
that a rare row--column overlap can create a logarithmic two-step peak
while the global intensity singular norm still vanishes. It does not
supply a trajectory of the random Schur process, a chaotic quantization,
or a BGS counterexample. Proofs for that process must use more than these
three static properties, such as an additional dynamic correlation estimate.
