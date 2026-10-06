# Candidate once-counted reduced four-block cancellation

Checkpoint RECONNECT-20261006-G. NEW CONDITIONAL RESEARCH PROOF pending independent audits of anchor_localization_symbolic.md and rank_two_finite_reduction.md. No repository change or full BGS claim.

## Claim and inputs

Let U_N be unitary, P_xy=|U_xy|², q=max P_xy<=C/N and ||P^L-J||op<=2^-L for all L>=0 and sufficiently large N. These generic matrix hypotheses are supplied for the actual frozen operator by FM-021; they are not a spectral-universality criterion.

Let T_m^(4) be the SET of rooted ordered coordinate-word pairs for which x admits four nonempty cyclic blocks A,B,C,D, with pairwise distinct INITIAL VERTEX VALUES, and y is a cyclic rotation of A D C B. This is the unique genuinely reduced four-block ordering. Count each pair once, regardless of witnesses. Write W(x,y)=a(x)conjugate(a(y)).

Subject to the two named new proof inputs, for every smooth compactly supported w in (0,infinity),

N^-2 sum_m w(m/N) sum_((x,y) in T_m^(4)) W(x,y) ->0.

With K=ceil(log N), the bound is O_w(K^10/N), plus O_w(N^10(C/N)^(K/2)) and exponentially small terms. No noise or phase average is involved. The claim remains one fixed-complexity family, possibly overlapping other families; it does not exhaust the deterministic trace expansion or justify a growing-complexity truncation.

## 1. Marked and local-overlap sums

Let M_m=m² sum_(L1+...+L4=m-4) E_sigma(L), sigma(i)=i-1 mod4, with distinct starting ports. The general reduced fixed-r estimate gives |E_sigma(L)|<=C^4N2^-max Li, so the normalized M_m band sum is O_w(N^5 2^(-(aN-4)/4)).

Define O_m as the subcollection of this marked sum in which A=(a), B=(b,a,b), with C,D arbitrary nonempty shared blocks. Thus

O_m=m² sum_(LC+LD=m-6; LC,LD>=0) E_local(LC,LD),

where the explicit local contraction in rank_two_finite_reduction.md uses P_ba P_ab, the two C,D propagators and eight connector amplitudes. It obeys

|E_local|<=C^6 N^-1 2^-max(LC,LD)<=C^6 N^-1 2^(-(m-6)/2).

Hence the normalized O_m band sum is exponentially small too. Importantly, O_m is a literal subset of the marked parameter tuples defining M_m; imposing this local pattern does not enlarge their positive absolute mass.

## 2. K-unique words and high-rank exceptional mass

The repeated-K-substring estimate for r=4 bounds the complete non-K-unique marked absolute band mass by O_w(N^10q^(K/2)), superpolynomially small. Any unmarked exceptional pair has at least one marked parameter tuple, so its absolute weight is bounded by that marked exceptional mass. O_m's exceptional absolute mass is also bounded by it, since O_m is a marked subcollection. Thus all comparisons below may first be made on K-unique x, then extended with only a constant multiple of that superpolynomial error, without assumptions on periodic exceptional words.

K-unique x and all its four-block outputs are primitive once m>8K: at least m-4(K-1)>m/2 output K-substrings lie inside shared blocks and are distinct. For such a fixed rooted ordered pair let r(x,y) be the number of admissible unordered cut sets. Each cut set gives exactly FOUR marked parameter tuples, from cyclic block labels, and no extra root stabilizer.

The symbolic note proves:

- if three original blocks have length>=5K, their fixed common anchors force uniqueness;
- every competing cut lies O(K) from some original cut, so there are O(K^4) alternatives;
- a deterministic long common source interval uniquely fixes the cyclic alignment.

Therefore an ambiguous original representation has two short lengths, giving O(K²m) original length quadruples. Each alternative imposing equality rank>=3 costs at most C^4q³, by exposing the four starts first. Together with O(K^4) alternatives, m² trace roots and the normalized band sum, the absolute marked mass of representations participating in at least one rank>=3 relation is

B=O_w(N²K^6q³)=O_w(K^6/N).

Every pair has r(x,y)<=R_K=O(K^4), by localization relative to any one of its cut sets.

## 3. Rank-two representation graph and absence of triangles

For one K-unique rooted pair make a graph whose vertices are its admissible cut sets; join two vertices when their relative positional equality rank is2. Distinct vertices cannot have rank0, and rank1 is excluded by the general predecessor-transposition argument. All nonedges therefore have rank>=3.

The finite-reduction classification says every edge is a local abab flip, with relative permutation

tau_s=(s,s+2)(s+1,s+3)

on four consecutive source positions. Its cut sets are {s,s+1,s+4,z} and {s,s+3,s+4,z}. For m>8 the start s is unique, so the marked local-overlap subcollection O_m counts each UNORDERED graph edge exactly once: choose the endpoint having the singleton A and the length-three B. The two independent trace roots are then uniquely determined by the rooted pair's primitive words.

This graph has no triangle. Relative permutations along two distinct edges from one vertex are tau_s,tau_t. If s=t, the other vertices coincide, since their aligned positional outputs coincide. For distinct s,t, their product has rank4 unless the starts are cyclic neighbors. In the neighbor case the product is a3-cycle, of rank2; that relative type is forbidden by the same rank-two classification. These possibilities follow directly by multiplying the two products of transpositions: displacement1 gives one3-cycle, displacement2 gives two3-cycles, displacement3 gives a3-cycle and two transpositions, and disjoint supports give four transpositions. Negative cyclic displacements are inverses of these cases. Thus no third rank-two edge can close a triangle.

## 4. Exact once-counting correction and error control

Call a pair good if no two of its representations have rank>=3. Its representation graph is complete, hence by triangle-freeness it has r=1 or2. If e is its number of rank-two edges, then r-e=1. Consequently its once-counted contribution equals its contribution to M_m/4 minus its contribution to O_m.

For a bad pair, let r_hi be the number of graph vertices incident to a rank>=3 relation. At most one vertex can have no such relation: two vertices adjacent by rank2 to every other vertex would form a rank-two triangle with any third. Thus r_hi>=r-1>=r/2 (the case r=2 with a high-rank relation has both vertices participating). The high-rank marked bound B therefore controls the entire bad-pair marked mass up to a factor2.

For any bad pair,

|1-r+e|<=1+r+binom(r,2)<=O(R_K)r.

Summing these errors costs O(R_K)B=O_w(K^10/N). No universal division by four is used on the bad set, and no unproved truncation of inclusion-exclusion is needed.

On non-K-unique pairs, compare the actual once-counted sum directly with M_m/4-O_m. Each of its three absolute masses is bounded by the complete exceptional marked mass, the last because O_m is a literal marked subcollection. This remains valid for periodic words and varying root multiplicities. The extra error stays O_w(N^10q^(K/2)).

Combining with the exponential marked and local-overlap estimates proves the scoped claim, CONDITIONAL ON INDEPENDENT ACCEPTANCE of the symbolic anchor/localization note and the rank-two finite reduction/kernel classification. The earlier accepted three-block theorem is unchanged.

## Boundary and next task

This would close T_m^(4) only. Repeated genuine ports, arbitrary non-permutation path pairs, overlaps among different fixed-complexity families, r>=5 short-cluster unmarking, growing encounter complexity and the super-Heisenberg plateau remain open. Fixed-family cancellation cannot be promoted to the full signed joint-trace hierarchy.
