# hecke_real_centraliser_v3.jl
# RING 1.2 v3 — Churilov decomposition on the Hecke-centered residual
#
# Design (R61): R49-A measured heavy eigenvalue outliers, not SVD-rank.
# Correct decomposition: V_arth = σH + S + A with
#   A_n = Hecke average (deterministic correction, R49-A kurtosis
#         mechanism: subtracting A_n removes the entry-correlation
#         structure; residual R = V_arth - A_n has Gaussian entries
#         in the off-diagonal)
#   R_n = V_arth - A_n  (Wigner-candidate after centering)
#   Test: does R_n = σH_n + S_n with rank(S_n) = o_P(n) hold?
#
# Target: p=4481, m=70. Haar surrogate for the centraliser first
# (R54-style), then upgrade to structured block-diagonal real
# centraliser.

using Printf
using LinearAlgebra
using Random
using Statistics

# --- FFT cat map propagator (handles N up to ~10^4 in ~2 GB) -----------
function U_cat_fft(A, N)
    a, b, c, d = A
    g = gcd(2c, N)
    if g != 1
        error("2c=$g and N=$N not coprime; cat-map requires gcd(2c,N)=1")
    end
    icb = powermod(2c, -1, N)
    phase = zeros(Float64, N, N)
    for x in 0:N-1, y in 0:N-1
        phase[x+1, y+1] = 2π * ((icb * (d*x*x - 2*x*y + a*y*y)) % N) / N
    end
    D = ComplexF64.(cos.(phase) .+ im .* sin.(phase))
    # F is the unitary DFT; F = F^* for our convention.
    F = (1/sqrt(N)) * [exp(-2π*im*(i*j)/N) for i in 0:N-1, j in 0:N-1]
    return F * Diagonal(D) * F
end

function cluster_eigs(ev::Vector{ComplexF64}; tol=1e-6)
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

# --- V_arth: low-rank Hermitian Weyl combination (C cycles) -------------
# Memory: O(C·N) for the sum, O(N²) for V_final (Hermitian, ~256 MB
# for N=4481). C=100 gives a low-rank-enough perturbation.
function V_arith_cycles(N::Int, C::Int, seed::Int)
    rng = MersenneTwister(seed)
    V = zeros(ComplexF64, N, N)
    for _ in 1:C
        n_shift = rand(rng, 0:N-1)
        m_phase = rand(rng, 0:N-1)
        # T(n_shift, m_phase) = w^{2^{-1} n_shift m_phase} X^{n_shift} Z^{m_phase}
        w = exp(2π * im / N)
        b2 = powermod(2, -1, N)
        phase = w^((b2 * n_shift * m_phase) % N)
        for j in 0:N-1
            j_to = (j + n_shift) % N
            V[j+1, j_to+1] += phase * w^((m_phase * j) % N)
        end
    end
    V /= C
    return Hermitian((V + V') / 2)
end

# --- Spacing test ------------------------------------------------------
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

# --- Main --------------------------------------------------------------
p = 1009
A = (4, 1, 1, 3)
N = p
println("Cat map p=$p A=$A")
# Build U_A
@time U = U_cat_fft(A, N)
@time ev_U = eigvals(U)
@time groups = cluster_eigs(ev_U)
sizes = [length(g) for g in groups]
println("Eigenspaces: ", length(groups), "  size stats: min=", minimum(sizes),
        " max=", maximum(sizes))

# Largest eigenspace
largest_idx = argmax(sizes)
idx = groups[largest_idx]
m = length(idx)
println("Largest eigenspace: m=$m")
U_sub = U[:, idx]

# V_arth
@time V_full = V_arith_cycles(N, 100, 42)
@printf("V_full: %d×%d dense (%.1f MB)\n", size(V_full)..., 2*sizeof(ComplexF64)*N^2 / 1e6)

# Compress: V_lam_raw = U_sub^* V U_sub
@time V_lam_raw = U_sub' * V_full * U_sub
V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))
println("V_lam size: ", size(V_lam))

# RAW: measure kurtosis + spacing
kurt_raw = kurt_offdiag(V_lam)
ev_raw = eigvals(V_lam)
ks_raw = spacing_ks(ev_raw)
@printf("RAW: Re kurt=%.4f KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        kurt_raw, ks_raw...)

# --- Step 1: Hecke mean A_n (Haar surrogate first) ---
# A_n = (1/K) Σ_{j=0}^{K-1} O_j V_lam O_j^T  where O_j is Haar-orthogonal
n_hecke = 64
rng = MersenneTwister(0)
A_n_haar = zeros(ComplexF64, m, m)
for _ in 1:n_hecke
    O = randn(rng, ComplexF64, m, m)
    Q, _ = qr(O)
    A_n_haar += Q * V_lam * Q'
end
A_n_haar /= n_hecke
A_n_haar = Hermitian(Matrix((A_n_haar + A_n_haar') / 2))

# Residual: R_n = V_lam - A_n
R_n_haar = Hermitian(Matrix(V_lam - A_n_haar))
kurt_R = kurt_offdiag(R_n_haar)
ev_R = eigvals(R_n_haar)
ks_R = spacing_ks(ev_R)
@printf("R_n (Haar-Hecke centered): Re kurt=%.4f KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        kurt_R, ks_R...)

# --- Step 2: Test Churilov rank(S_n) ---
# In the Churilov decomposition, R_n = σH_n + S_n with rank(S_n) = o(n).
# We test: does the singular value spectrum of R_n decay fast?
@time sv_R = svdvals(Matrix(R_n_haar))
n_sv = length(sv_R)
println("Singular value spectrum of R_n: max=", round(sv_R[1], digits=2),
        " median=", round(sv_R[n_sv÷2], digits=4),
        " min=", round(sv_R[end], digits=6),
        " ratio max/median=", round(sv_R[1] / max(sv_R[n_sv÷2], 1e-12), digits=2))

# Rank: count of singular values above various thresholds
for thresh in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6]
    cnt = count(>(thresh), sv_R)
    @printf("  rank(>%.0e) = %d / %d\n", thresh, cnt, n_sv)
end

# --- Step 3: structured (block-diagonal) centraliser ---
# For A=(2,1,1,1) at p=4481, ord=64, k=64, m=70=m_hecke.
# Approximation: real centraliser acts as block-diagonal phase rotations
# on the Hecke basis (k_hecke blocks of size m/k_hecke = 70/64 ≈ 1).
# We use m blocks of size 1 (just per-coordinate phase rotations).
ord_a = 64
k_hecke = ord_a
block_size = max(1, m ÷ k_hecke)
A_n_struct = zeros(ComplexF64, m, m)
for j_ in 0:n_hecke-1
    O = Matrix{ComplexF64}(I, m, m)
    for b in 0:k_hecke-1
        phase = exp(2π * im * j_ * b / k_hecke)
        for r in 1:min(block_size, m - b*block_size)
            col = b * block_size + r
            if col <= m
                O[col, col] = phase
            end
        end
    end
    A_n_struct += O * V_lam * O'
end
A_n_struct /= n_hecke
A_n_struct = Hermitian(Matrix((A_n_struct + A_n_struct') / 2))

R_n_struct = Hermitian(Matrix(V_lam - A_n_struct))
kurt_Rs = kurt_offdiag(R_n_struct)
ev_Rs = eigvals(R_n_struct)
ks_Rs = spacing_ks(ev_Rs)
@printf("R_n (struct-Hecke centered): Re kurt=%.4f KS_GOE=%.4f KS_GUE=%.4f KS_Pois=%.4f\n",
        kurt_Rs, ks_Rs...)

@time sv_Rs = svdvals(Matrix(R_n_struct))
println("Singular value spectrum of R_n (struct): max=", round(sv_Rs[1], digits=2),
        " median=", round(sv_Rs[length(sv_Rs)÷2], digits=4),
        " ratio max/median=", round(sv_Rs[1] / max(sv_Rs[length(sv_Rs)÷2], 1e-12), digits=2))

# Write artifact
open("artifacts/hecke_real_centraliser_v3.txt", "w") do f
    println(f, "p=$p m=$m n_hecke=$n_hecke k_hecke=$k_hecke")
    println(f, "RAW: Re kurt=$kurt_raw; KS_GOE=$(ks_raw[1]) KS_GUE=$(ks_raw[2]) KS_Pois=$(ks_raw[3])")
    println(f, "R_n (Haar-Hecke centered): Re kurt=$kurt_R; KS_GOE=$(ks_R[1]) KS_GUE=$(ks_R[2]) KS_Pois=$(ks_R[3])")
    println(f, "  singular values: max=$(sv_R[1]) median=$(sv_R[n_sv÷2]) ratio=$(sv_R[1]/max(sv_R[n_sv÷2],1e-12))")
    println(f, "R_n (struct-Hecke centered): Re kurt=$kurt_Rs; KS_GOE=$(ks_Rs[1]) KS_GUE=$(ks_Rs[2]) KS_Pois=$(ks_Rs[3])")
    println(f, "  singular values: max=$(sv_Rs[1]) median=$(sv_Rs[length(sv_Rs)÷2]) ratio=$(sv_Rs[1]/max(sv_Rs[length(sv_Rs)÷2],1e-12))")
end
println("Wrote artifacts/hecke_real_centraliser_v3.txt")
