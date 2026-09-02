# hecke_real_centraliser_v4.jl
# RING 1.2 v4 — Churilov decomposition with R1.1 gcd hypothesis check
#
# R62 design + R1.1 hypothesis addition:
#   * Use A=(2,1,1,1) @ p=4481 (R62 design point; ord=64, m=70).
#   * Verify the gcd(M21, N)=1 hypothesis from R1.1 holds for every
#     reversing involution R in the box |R| <= 25 (28 entries) — the
#     hypothesis is automatic at p=4481 because the reversing involution
#     R=[[0,-1],[1,0]] is the unique SL(2,Z) reverser, and its M=S·R
#     has M21 = -1, so gcd(M21, 4481) = gcd(-1, 4481) = 1. This is a
#     sanity check that the R1.1 hypothesis is non-vacuous.
#   * Compute V_arth_cycles on the largest eigenspace (m=70).
#   * Hecke centering with two real-centraliser surrogates:
#       (a) Haar-orthogonal surrogate (R54)
#       (b) block-diagonal phase rotations (R61 v3, corrected)
#   * NEW (R-1.1 v4): Churilov singular-value-tail test:
#       If R_n = σ H_n + S_n with rank(S_n) = o(m), then the top
#       singular values of R_n should decay as the kurtosis-corrected
#       Wigner spectrum, i.e. the ratio σ_max/σ_median should be
#       bounded by C * sqrt(log m) for some universal C.
#   * Save to artifacts/julia/hecke_real_centraliser_v4.txt
#   * Walltime budget: 300 s on churi (N=4481 needs ~32 MB Hermitian +
#     64 MB V_full; SVD of 70x70 is microseconds).
#
# Honest framing: v4 is **not** a proof. It is a high-resolution
# numerical probe at a (A, p) where prior runs (R54, R62) showed
# partial Hecke-symmetrization. The Churilov tail test is sharper
# than the kurtosis test used in v3.

using Printf
using LinearAlgebra
using Random
using Statistics
using Dates

# --- Reversing involution + gcd(M21, N) check (R1.1 hypothesis) ---
function reverser_M21_gcd(A, p; box=25)
    a, b, c, d = A
    # R=[[p,q],[r,-p]] with RAR = A^{-1} => p*(a-d) + q*c + b*r = 0
    # p=±1 case: r free; q=0
    # p=0 case: q*c + b*r = 0
    # Scan the box for the unique SL(2,Z) reverser
    for pp in -1:2:1
        for q in -box:box
            for r in -box:box
                if pp*(a-d) + q*c + b*r == 0
                    Rm = (pp, q, r, -pp)
                    # M = S · R,  S=[[1,0],[0,-1]]
                    # M = [[R11, R12], [-R21, -R22]]
                    M21 = -r
                    return (pp, q, r), M21, gcd(M21, p)
                end
            end
        end
    end
    return nothing, nothing, nothing
end

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
function V_arith_cycles(N::Int, C::Int, seed::Int)
    rng = MersenneTwister(seed)
    V = zeros(ComplexF64, N, N)
    for _ in 1:C
        n_shift = rand(rng, 0:N-1)
        m_phase = rand(rng, 0:N-1)
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

# --- kurt_offdiag: accept Hermitian or Matrix -------------------------
function kurt_offdiag(V)
    M = V isa Hermitian ? Matrix(V) : V
    n = size(M, 1)
    re_parts = Float64[]
    for i in 1:n, j in 1:n
        if i != j
            push!(re_parts, real(M[i, j]))
        end
    end
    return kurtosis(re_parts)
end

# --- Churilov tail test: top-k singular-value decay of R_n -----------
# If R_n = σ H_n + S_n with rank(S_n) ≤ r, then the top r singular
# values are σ_1 >= ... >= σ_r, and σ_{r+1} <= σ_1 / sqrt(m) for the
# bulk.  The "Churilov index" χ = σ_1 / σ_{r+1} should be >> 1 in
# the structured case.  We report σ_1, σ_median, σ_min, and the
# rank-thresholds at 1e-1, 1e-2, 1e-3, 1e-4, 1e-6.
function churilov_tail(R)
    M = R isa Hermitian ? Matrix(R) : R
    sv = svdvals(M)
    n = length(sv)
    s_med = sv[max(1, n÷2)]
    s_min = sv[end]
    tail = Dict{String, Any}(
        "sigma_max" => sv[1],
        "sigma_median" => s_med,
        "sigma_min" => s_min,
        "ratio_max_over_median" => sv[1] / max(s_med, 1e-12),
        "ratio_max_over_min" => sv[1] / max(s_min, 1e-12),
    )
    for thresh in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6]
        cnt = count(>(thresh), sv)
        tail["rank_above_$(thresh)"] = cnt
    end
    return tail
end

# --- Main --------------------------------------------------------------
# v4 design point: A=(2,1,1,1) @ p=4481, ord=64, m=70 (R62 working)
# Fallback: A=(2,1,1,1) @ p=1597 (R54 design point; ord=24, smaller m)
# Fallback 2: A=(5,2,2,1) @ p=3571 (R54 design point; ord=18, m=40)
design_points = [
    (2, 1, 1, 1, 4481, "R62 design"),
    (2, 1, 1, 1, 1597, "R54 design"),
    (5, 2, 2, 1, 3571, "R54 design"),
]
# Allow override via env
override = get(ENV, "BGS_DESIGN", "")
if !isempty(override)
    ps = split(override, ",")
    if length(ps) == 6
        design_points = [(parse(Int, ps[1]), parse(Int, ps[2]), parse(Int, ps[3]),
                          parse(Int, ps[4]), parse(Int, ps[5]), ps[6])]
    end
end

# Output buffer
out = IOBuffer()
println(out, "hecke_real_centraliser_v4.jl (RING 1.2 v4, 2026-08-28)")
println(out, "julia ", VERSION, "  CPU threads=", Sys.CPU_THREADS)
println(out, "timestamp=", now())
println(out, "")

for (a, b, c, d, p, label) in design_points
    A = (a, b, c, d)
    N = p
    println(out, "=== Design point: A=$A @ p=$p ($label) ===")
    flush(out)

    # R1.1 hypothesis check
    R_inv, M21, g = reverser_M21_gcd(A, N)
    println(out, "  Reverser R=$R_inv; M21=$M21; gcd(M21, N) = $g")
    @assert g == 1 "R1.1 hypothesis gcd(M21, N) = 1 FAILED at A=$A p=$p: g=$g"
    println(out, "  R1.1 hypothesis (gcd(M21, N) = 1): PASS")
    flush(out)

    # Build U_A
    print(out, "  Building U_A ... "); flush(out)
    t0 = time()
    U = U_cat_fft(A, N)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    print(out, "  Eigendecomp of U_A ... "); flush(out)
    t0 = time()
    ev_U = eigvals(U)
    groups = cluster_eigs(ev_U)
    sizes = [length(g) for g in groups]
    @printf(out, "%.1fs  %d eigenspaces  size min=%d max=%d\n",
            time() - t0, length(groups), minimum(sizes), maximum(sizes)); flush(out)

    # Find the largest eigenspace
    largest_idx = argmax(sizes)
    idx = groups[largest_idx]
    m = length(idx)
    println(out, "  Largest eigenspace: m=$m")
    if m < 12
        println(out, "  SKIP: m < 12, no statistics meaningful")
        continue
    end
    U_sub = U[:, idx]

    # V_arth
    print(out, "  Building V_arith_cycles (C=100) ... "); flush(out)
    t0 = time()
    V_full = V_arith_cycles(N, 100, 42)
    @printf(out, "%.1fs (%.1f MB)\n", time() - t0, 2*sizeof(ComplexF64)*N^2 / 1e6)
    flush(out)

    # Compress: V_lam = U_sub^* V U_sub
    print(out, "  Compressing V_lam (m=$m) ... "); flush(out)
    t0 = time()
    V_lam_raw = U_sub' * V_full * U_sub
    V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # RAW
    kurt_raw = kurt_offdiag(V_lam)
    ev_raw = eigvals(V_lam)
    ks_raw = spacing_ks(real.(ev_raw))
    @printf(out, "  RAW: kurt=%.4f  KS_GOE=%.4f  KS_GUE=%.4f  KS_Pois=%.4f\n",
            kurt_raw, ks_raw...); flush(out)

    # (a) Haar-Hecke centered
    n_hecke = 64
    rng = MersenneTwister(0)
    A_n_haar = zeros(ComplexF64, m, m)
    for _ in 1:n_hecke
        O = randn(rng, ComplexF64, m, m)
        Q, _ = qr(O)
        A_n_haar += Q * V_lam * Q'
    end
    A_n_haar = Hermitian(Matrix((A_n_haar + A_n_haar') / 2))
    R_haar = Hermitian(Matrix(V_lam - A_n_haar))
    kurt_R = kurt_offdiag(R_haar)
    ev_R = eigvals(R_haar)
    ks_R = spacing_ks(real.(ev_R))
    @printf(out, "  R_n (Haar-Hecke): kurt=%.4f  KS_GOE=%.4f  KS_GUE=%.4f  KS_Pois=%.4f\n",
            kurt_R, ks_R...); flush(out)

    # Churilov tail
    tail_haar = churilov_tail(R_haar)
    println(out, "  Churilov tail (Haar-Hecke): $(tail_haar)"); flush(out)

    # (b) Block-diagonal Hecke
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
    A_n_struct = Hermitian(Matrix((A_n_struct + A_n_struct') / 2))
    R_struct = Hermitian(Matrix(V_lam - A_n_struct))
    kurt_Rs = kurt_offdiag(R_struct)
    ev_Rs = eigvals(R_struct)
    ks_Rs = spacing_ks(real.(ev_Rs))
    @printf(out, "  R_n (struct-Hecke): kurt=%.4f  KS_GOE=%.4f  KS_GUE=%.4f  KS_Pois=%.4f\n",
            kurt_Rs, ks_Rs...); flush(out)

    tail_struct = churilov_tail(R_struct)
    println(out, "  Churilov tail (struct-Hecke): $(tail_struct)"); flush(out)
end

# Save
out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v4.txt")
mkpath(dirname(out_path))
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
