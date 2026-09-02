# hecke_real_centraliser_v8.jl
# RING 1.2 v8 — Hecke-collapse on R54 design points with ord ∈ [40, 60].
#
# find_small_ord_primes.jl found 4 candidates:
#   p=2161, ord=40, k=40, pred_m=54
#   p=2521, ord=60, k=60, pred_m=42
#   p=3001, ord=50, k=50, pred_m=60
#   p=3469, ord=51, k=51, pred_m=68
#
# v8 runs the Hecke-centring collapse on these 4 design points
# and the v6 reference (p=4481, ord=64, k=64, m=68) to map
# the reduction factor as a function of k.

include("projective_order_brute.jl")

using Printf
using LinearAlgebra
using Random
using Statistics
using Dates

function U_cat_fft(A, N)
    a, b, c, d = A
    g = gcd(2c, N)
    if g != 1
        error("2c=$g and N=$N not coprime")
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

function tonelli_shanks(n, p)
    if powermod(n, (p - 1) ÷ 2, p) != 1
        error("not a QR")
    end
    q = p - 1
    s = 0
    while q % 2 == 0
        q ÷= 2
        s += 1
    end
    z = 2
    while powermod(z, (p - 1) ÷ 2, p) != p - 1
        z += 1
    end
    M = s
    c = powermod(z, q, p)
    t = powermod(n, q, p)
    R = powermod(n, (q + 1) ÷ 2, p)
    while true
        if t == 1
            return R
        end
        i = 0
        temp = t
        while temp != 1
            temp = (temp * temp) % p
            i += 1
        end
        b = powermod(c, 1 << (M - i - 1), p)
        M = i
        c = (b * b) % p
        t = (t * c) % p
        R = (R * b) % p
    end
end

function k_of_p(A, p)
    a, b, c, d = A
    tr = (a + d) % p
    disc = (tr * tr - 4) % p
    if disc < 0; disc += p; end
    if powermod(disc, (p - 1) ÷ 2, p) != 1
        return -1
    end
    s = tonelli_shanks(disc, p)
    inv2 = powermod(2, -1, p)
    alpha = ((tr + s) * inv2) % p
    if alpha == 0; return -1; end
    for ord in 1:p
        if powermod(alpha, ord, p) == 1
            return ord
        end
    end
    return -1
end

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

function kurt_offdiag(V)
    M = V isa Hermitian ? Matrix(V) : V
    n = size(M, 1)
    re_parts = Float64[]
    for i in 1:n, j in 1:n
        if i != j
            push!(re_parts, real(M[i, j]))
        end
    end
    if isempty(re_parts)
        return 0.0
    end
    μ = sum(re_parts) / length(re_parts)
    σ² = sum((x - μ)^2 for x in re_parts) / length(re_parts)
    σ⁴ = σ² * σ²
    if σ⁴ < 1e-30
        return 0.0
    end
    m4 = sum((x - μ)^4 for x in re_parts) / length(re_parts)
    return m4 / σ⁴ - 3.0
end

function churilov_tail(R)
    M = R isa Hermitian ? Matrix(R) : R
    sv = svdvals(M)
    n = length(sv)
    if n == 0
        return Dict{String, Any}("sigma_max" => 0, "sigma_median" => 0, "sigma_min" => 0, "ratio_max_over_median" => 0)
    end
    return Dict{String, Any}(
        "sigma_max" => sv[1],
        "sigma_median" => sv[max(1, n÷2)],
        "sigma_min" => sv[end],
        "ratio_max_over_median" => sv[1] / max(sv[max(1, n÷2)], 1e-12),
    )
end

# v8 design points
design_points = [
    ((2, 1, 1, 1), 4481, "v6 ref: k=64, m=68 (R62 design)"),
    ((2, 1, 1, 1), 2161, "R54: k=40, pred_m=54"),
    ((2, 1, 1, 1), 3001, "R54: k=50, pred_m=60"),
    ((2, 1, 1, 1), 3469, "R54: k=51, pred_m=68 (best)"),
    ((2, 1, 1, 1), 2521, "R54: k=60, pred_m=42"),
    ((2, 1, 1, 1), 211, "v7-FIXED: k=21, m=12 (5.3x)"),
]

out = IOBuffer()
println(out, "hecke_real_centraliser_v8.jl (RING 1.2 v8, 2026-08-28)")
println(out, "julia ", VERSION, "  timestamp=", now())
println(out, "")

results = []
for (A, p, label) in design_points
    N = p
    print(out, "=== A=$A @ p=$p ($label) ===\n"); flush(out)

    # ord_p(A) via brute
    print(out, "  ord_p(A) ... "); flush(out)
    t0 = time()
    proj_ord = projective_order_brute(A, p; max_iter=p^2)
    @printf(out, "%d  (%.2fs)\n", proj_ord, time() - t0); flush(out)

    k_alpha = k_of_p(A, p)
    println(out, "  k = ord_p(α) = $k_alpha")
    if k_alpha < 1 || proj_ord < 1
        println(out, "  SKIP"); continue
    end

    # Build U_A
    print(out, "  Building U_A ... "); flush(out)
    t0 = time()
    U = U_cat_fft(A, N)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # Multiplet identification
    print(out, "  Eigendecomp ... "); flush(out)
    t0 = time()
    ev_U = eigvals(U)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    th_U = angle.(ev_U)
    window_width = 2π / proj_ord
    counts = zeros(Int, proj_ord)
    for t in th_U
        j = mod(round(Int, t / window_width), proj_ord) + 1
        counts[j] += 1
    end
    max_count = maximum(counts)
    println(out, "  Multiplet size = $max_count")

    if max_count < 8
        println(out, "  Multiplet too small; SKIP")
        continue
    end

    j_max = argmax(counts)
    angle_center = (j_max - 0.5) * window_width
    idx = [i for i in 1:N if abs(angle(ev_U[i]) - angle_center) < window_width / 2]
    m = length(idx)
    if m < 8
        println(out, "  Could not extract m=$m; SKIP"); continue
    end
    U_sub = U[:, idx]

    V_full = V_arith_cycles(N, 100, 42)
    V_lam_raw = U_sub' * V_full * U_sub
    V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))

    kurt_raw = kurt_offdiag(V_lam)
    println(out, "  RAW kurt = $(round(kurt_raw, digits=4))")

    n_hecke = 64
    rng = MersenneTwister(0)
    A_n = zeros(ComplexF64, m, m)
    for _ in 1:n_hecke
        O = randn(rng, ComplexF64, m, m)
        Q, _ = qr(O)
        A_n += Q * V_lam * Q'
    end
    A_n = Hermitian(Matrix((A_n + A_n') / 2))
    R_n = Hermitian(Matrix(V_lam - A_n))
    kurt_R = kurt_offdiag(R_n)
    println(out, "  R_n (Haar-Hecke) kurt = $(round(kurt_R, digits=4))")
    factor = abs(kurt_raw) / max(abs(kurt_R), 1e-6)
    println(out, "  Reduction factor = $(round(factor, digits=1))x")
    tail = churilov_tail(R_n)
    println(out, "  Churilov tail: $(tail)")

    push!(results, Dict(
        "A" => collect(A), "p" => p,
        "ord_p_A" => proj_ord, "k_alpha" => k_alpha,
        "m" => m, "kurt_raw" => kurt_raw, "kurt_R" => kurt_R,
        "reduction_factor" => factor,
        "tail" => tail,
        "label" => label,
    ))
    println(out, "")
end

println(out, "=== v8 SUMMARY: kurtosis collapse as function of k ===")
println(out, "p, ord, k, m, kurt_raw, kurt_R, reduction")
for r in results
    @printf(out, "%4d %3d %3d %3d %9.4f %9.4f %9.1fx  (%s)\n",
            r["p"], r["ord_p_A"], r["k_alpha"], r["m"],
            r["kurt_raw"], r["kurt_R"], r["reduction_factor"], r["label"])
end

# Threshold analysis
println(out, "")
ks = [r["k_alpha"] for r in results]
factors = [r["reduction_factor"] for r in results]
sorted_pairs = sort(collect(zip(ks, factors)), by=p->p[1])
println(out, "k-threshold mapping (sorted by k):")
for (k, f) in sorted_pairs
    @printf(out, "  k=%d: reduction=%.1fx\n", k, f)
end
println(out, "")
# Smoothness: does reduction grow monotonically in k?
if length(sorted_pairs) >= 3
    pairs = sorted_pairs
    monotone = all(pairs[i][2] <= pairs[i+1][2] * 1.1 for i in 1:length(pairs)-1) ||
               all(pairs[i][2] >= pairs[i+1][2] * 0.9 for i in 1:length(pairs)-1)
    if monotone
        println(out, "VERDICT: reduction factor is roughly monotone in k (consistent with 'larger k → stronger Hecke collapse').")
    else
        println(out, "VERDICT: reduction factor is NOT monotone in k (counterexample to R54 LEDGER R54 'k >= 50 threshold').")
    end
end

out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v8.txt")
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
