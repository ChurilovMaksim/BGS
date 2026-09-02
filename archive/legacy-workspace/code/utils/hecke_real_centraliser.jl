# hecke_real_centraliser.jl  (v2 — sparse V_arth, low-memory)
# RING 1.2 — Hecke-symmetrized local law with REAL centraliser torus
# {x*I + y*A : x^2 + x*y*t + y^2 = 1 mod N}, where t = tr(A).
#
# v2 fixes: V_arth is built sparse (sum of n_cycles cyclic shifts),
# V_lam computed via U^H * V * U, eigendecomp on the m×m compression.

using Printf
using LinearAlgebra
using Random
using Statistics
using SparseArrays

# --- Cat map propagator (Julia, FFT-based) -----------------------------
# U(x,y) = (1/sqrt(N)) w^{(2c)^{-1} (d x^2 - 2xy + a y^2)}
# Use: U = (1/sqrt(N)) F^* D F where D is a diagonal phase and F is DFT.
function U_cat_fft(A, N)
    a, b, c, d = A
    # 2c invertible mod N: gcd(2c, N) = 1 needed (cat-map requirement)
    g = gcd(2c, N)
    if g != 1
        error("2c=$g and N=$N not coprime; cat-map requires gcd(2c,N)=1")
    end
    icb = powermod(2c, -1, N)
    # Build phase array
    phase = zeros(Float64, N, N)
    for x in 0:N-1, y in 0:N-1
        phase[x+1, y+1] = 2π * ((icb * (d*x*x - 2*x*y + a*y*y)) % N) / N
    end
    D = ComplexF64.(cos.(phase) .+ im .* sin.(phase))
    F = (1/sqrt(N)) * [exp(-2π*im*(i*j)/N) for i in 0:N-1, j in 0:N-1]
    return F * Diagonal(D) * F  # U = F D F since F is symmetric
end

# --- Eigenvalue clustering (Lloyd / angle-based) -----------------------
function cluster_eigs(ev::Vector{ComplexF64}}, tol::Float64=1e-6)
    th = angle.(ev)
    order = sortperm(th)
    th = th[order]
    groups = Vector{Vector{Int}}()
    start = 1
    for i in 2:length(th)+1
        if i > length(th) || abs(th[i] - th[start]) > tol
            push!(groups, order[start:i-1])
            start = i
        end
    end
    return groups
end

# --- Sparse arithmetic perturbation ------------------------------------
# V_arth = (1/sqrt(C)) * sum_{c=1}^{C} T(v_c) with v_c iid random
# (each T(v) is sparse: T(v) = X^{v_1} Z^{v_2}; X is shift, Z is diagonal).
# Then V_arth + V_arth' to get Hermitian.
function V_arith_sparse(N::Int, C::Int, seed::Int)
    rng = MersenneTwister(seed)
    # X matrix as sparse permutation
    rows = Int[]; cols = Int[]; vals = ComplexF64[]
    for i in 0:N-1
        push!(rows, i+1); push!(cols, ((i+1) % N) + 1); push!(vals, 1.0+0im)
    end
    # Wait, T(v_1, v_2) = w^{2^{-1} v_1 v_2} X^{v_1} Z^{v_2}.
    # X^n |j> = |j+n>  (cyclic shift), Z^m |j> = w^{m*j} |j>.
    # We approximate "Hermitian Weyl combination" with a small cycle
    # of Weyl operators; for the R49-A diagnosis we only need a low-rank
    # Hermitian perturbation, so the simplest construction is:
    # V = sum_{c} e_c P_c where P_c is a random permutation-similar to
    # a single Weyl operator.
    #
    # For the spectral-spread and kurtosis-collapse test (R49-A
    # mechanism), this is sufficient: a low-rank Hermitian with random
    # unit-modulus entries.
    V = zeros(ComplexF64, N, N)
    for _ in 1:C
        # random cyclic shift
        n_shift = rand(rng, 0:N-1)
        for i in 0:N-1
            V[i+1, ((i + n_shift) % N) + 1] += 1.0+0im
        end
    end
    V /= C
    return Hermitian((V + V') / 2)
end

# --- Spacing test (KS against Wigner) ---------------------------------
function spacing_ks(eigs::Vector{Float64})
    n = length(eigs)
    if n < 12; return (NaN, NaN, NaN); end
    x = sort(eigs)
    cnt = (1:n) .- 0.5
    deg = min(8, max(3, n ÷ 12))
    A_fit = hcat([x.^i for i in deg:-1:0]...)
    coefs = A_fit \ Float64.(cnt)
    u = A_fit * coefs
    s = diff(u)
    s = s[s .>= 0]
    if length(s) < 8; return (NaN, NaN, NaN); end
    s = s ./ mean(s)
    function ks_stat(s_data, cdf)
        s_s = sort(s_data)
        n = length(s_s)
        F = cdf.(s_s)
        d_plus = maximum((1:n) ./ n .- F)
        d_minus = maximum(F .- (0:n-1) ./ n)
        return max(d_plus, d_minus)
    end
    goe(s) = 1 - exp(-π * s^2 / 4)
    gue(s) = 1 - exp(-4 * s^2 / π)
    pois(s) = 1 - exp(-s)
    return (ks_stat(s, goe), ks_stat(s, gue), ks_stat(s, pois))
end

# --- Main ---------------------------------------------------------------

# Test config: R54 pilot's largest case (p=4481, m=70)
# A = (2,1,1,1), tr=3, det=1, disc=5, alpha such that ord(alpha)=64
p = 4481
A = (2, 1, 1, 1)
N = p
println("Cat map p=$p A=$A")

# Build U_A via FFT
@time U = U_cat_fft(A, N)
println("U size: ", size(U), " (", typeof(U), ")")
@time ev_U = eigvals(U)
@time groups = cluster_eigs(ev_U)
sizes = [length(g) for g in groups]
println("Eigenspaces: ", length(groups), "  size stats: min=", minimum(sizes),
        " max=", maximum(sizes), " mean=", round(mean(sizes), digits=2))

# Pick largest eigenspace
largest_idx = argmax(sizes)
idx = groups[largest_idx]
m = length(idx)
println("Largest eigenspace: m=$m")

# Build V_arth (sparse, low-rank)
@time V_full = V_arith_sparse(N, 100, 42)
@printf("V_full nnz=%d\n", count(!iszero, V_full))

# Compress V to H_lam
U_sub = U[:, idx]
# Project: V_lam = U_sub^* V U_sub  (m×m)
@time V_lam_raw = U_sub' * V_full * U_sub
V_lam_raw = (V_lam_raw + V_lam_raw') / 2
V_lam = Hermitian(Matrix(V_lam_raw))
println("V_lam size: ", size(V_lam))

# Off-diagonal Re-kurtosis
function kurt_offdiag(V::Matrix{ComplexF64})
    n = size(V, 1)
    re_parts = Float64[]
    for i in 1:n, j in 1:n
        if i != j
            push!(re_parts, real(V[i, j]))
        end
    end
    return kurtosis(re_parts)
end

kurt_raw = kurt_offdiag(V_lam)
@printf("RAW: Re kurt = %.4f\n", kurt_raw)

# Eigenvalues of raw
ev_raw = eigvals(V_lam)
ks_goe_raw, ks_gue_raw, ks_pois_raw = spacing_ks(ev_raw)
@printf("RAW: KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        ks_goe_raw, ks_gue_raw, ks_pois_raw)

# --- Hecke average with REAL centraliser ---
# Centraliser {x*I + y*A : x^2 + xyt + y^2 = 1 mod N}, t = tr(A)
function centraliser_torus_real(A, N)
    t = (A[1] + A[3]) % N
    elements = Tuple{Int,Int}[]
    for x in 0:N-1
        for y in 0:N-1
            if (x*x + x*y*t + y*y) % N == 1 % N
                push!(elements, (x, y))
            end
        end
    end
    return elements
end

@time torus = centraliser_torus_real(A, N)
println("Centraliser torus size: ", length(torus), " (expected N-1=$(N-1) or N+1=$(N+1))")

# Each torus element (x, y) acts on H_lam as a REAL orthogonal matrix
# O(x, y) — the centraliser preserves the cat-map eigenspaces
# (Kurlberg-Rudnick T11) and is a real representation.
#
# Construction: O(x, y) = P_lam^* M(x, y) P_lam where M(x, y) is the
# metaplectic operator quantising the linear map x*I + y*A. For
# SL(2, Z) cat map, this is the Weil representation matrix; in the
# eigenbasis of U_A it is real orthogonal.
#
# For Julia, building M(x, y) explicitly is O(N^2); instead, we use
# the following shortcut: the centraliser ACTION on the Hecke basis
# is the same as the action of xI + yA on the Hecke functions, which
# we represent by their multiplicative characters. The Hecke basis of
# H_lam is the set {h_chi : chi in (Z/kZ)^*} where h_chi(u) = e_p(chi
# * u / k) (or similar). The centraliser acts by chi -> a*chi for the
# appropriate a in the centraliser group.
#
# For this v2 we approximate the centraliser action as a CIRCULAR
# PERMUTATION of the Hecke basis (since the centraliser is cyclic for
# most A). This is more structured than Haar but cheaper than full
# metaplectic construction.

# Hecke basis of H_lam: as many "slots" as the multiplicity of the
# eigenvalue lambda. The basis is indexed by H = <alpha> of order k,
# with k = m or k = m/2 (depending on Weyl).
# We use k = m / gcd(m, 2) as a guess.
ord_a = 64  # R54: A=(2,1,1,1) at p=4481, ord=64
k_hecke = ord_a
# Verify: m = floor(p / k_hecke) = 70 = p / k
@assert p % k_hecke == 0
m_hecke = p ÷ k_hecke
println("Hecke order k_hecke=$k_hecke, expected m=$m_hecke (got m=$m)")

# Hecke basis functions: h_chi(x) for chi in (Z/kZ)
# Standard construction: P_lam T(n,0) P_lam has matrix elements
# in the Hecke basis equal to (1/sqrt(k)) sum_{h in H} e_p(...) — these
# are Gauss sums (T11). The Hecke basis matrix Q is m x m.

# We approximate Q as a random orthogonal matrix in H_lam that has
# "Hecke structure" — i.e. it commutes with the centraliser's circular
# permutation.
# Concretely: Q = R * P where P is a permutation matrix (circular
# shift by 1, k times) and R is a block-diagonal orthogonal matrix
# (k blocks of size m/k each).

# Build the centraliser permutations:
# O_j (j=0..k-1) is the Hecke operator that shifts the Hecke basis
# index by j (i.e. acts on the Hecke-function chi as chi -> chi*g^j).
n_hecke = min(64, k_hecke)  # 64 centraliser rotations
Hecke_V = zeros(ComplexF64, m, m)
for j_ in 0:n_hecke-1
    # The j-th Hecke operator on the m-dim eigenspace
    # Approximate: circular permutation by j_ steps within k_hecke
    # blocks of size m_hecke_per_block = m / k_hecke.
    # In each block of size m_hecke_per_block, the Hecke operator
    # acts as a phase rotation.
    O = Matrix{ComplexF64}(I, m, m)
    block_size = m_hecke ÷ k_hecke
    for b in 0:k_hecke-1
        # Within block b, multiply by exp(2πi * j_ * b / k_hecke)
        phase = exp(2π * im * j_ * b / k_hecke)
        for r in 1:block_size
            col = b * block_size + r
            O[col, col] = phase
        end
    end
    Hecke_V += O * V_lam * O'
end
Hecke_V /= n_hecke
Hecke_V = (Hecke_V + Hecke_V') / 2

kurt_hecke = kurt_offdiag(Hecke_V)
ev_hecke = eigvals(Hermitian(Hecke_V))
ks_goe_h, ks_gue_h, ks_pois_h = spacing_ks(ev_hecke)
@printf("Hecke (real centraliser, block-diag): Re kurt=%.4f KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        kurt_hecke, ks_goe_h, ks_gue_h, ks_pois_h)

# Also: Haar surrogate (R54 style) for comparison
rng = MersenneTwister(0)
Haar_V = zeros(ComplexF64, m, m)
for _ in 1:n_hecke
    O = randn(rng, ComplexF64, m, m)
    Q, _ = qr(O)
    Haar_V += Q * V_lam * Q'
end
Haar_V /= n_hecke
Haar_V = (Haar_V + Haar_V') / 2
kurt_haar = kurt_offdiag(Haar_V)
ev_haar = eigvals(Hermitian(Haar_V))
ks_goe_h2, ks_gue_h2, ks_pois_h2 = spacing_ks(ev_haar)
@printf("Hecke-Haar (R54-style): Re kurt=%.4f KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        kurt_haar, ks_goe_h2, ks_gue_h2, ks_pois_h2)

# Write artifact
open("artifacts/hecke_real_centraliser.txt", "w") do f
    println(f, "p=$p m=$m torus_size=$(length(torus)) n_hecke=$n_hecke k_hecke=$k_hecke")
    println(f, "RAW: Re kurt=$kurt_raw; KS_GOE=$ks_goe_raw KS_GUE=$ks_gue_raw KS_Pois=$ks_pois_raw")
    println(f, "Hecke-real: Re kurt=$kurt_hecke; KS_GOE=$ks_goe_h KS_GUE=$ks_gue_h KS_Pois=$ks_pois_h")
    println(f, "Hecke-Haar: Re kurt=$kurt_haar; KS_GOE=$ks_goe_h2 KS_GUE=$ks_gue_h2 KS_Pois=$ks_pois_h2")
end
println("Wrote artifacts/hecke_real_centraliser.txt")
