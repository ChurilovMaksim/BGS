# hecke_real_centraliser_v9_v10.jl
# RING 1.2 v9+v10 — UNIVERSALITY + REPRODUCIBILITY
#
# v9: Hecke-centring collapse at OTHER cat maps (A=(3,1,2,1), (5,2,2,1), (7,3,2,1))
#     Test: is the v6/v8 result universal across hyperbolic A, or specific to (2,1,1,1)?
# v10: Reproducibility across V_arith_cycles seeds.
#     Test: is the reduction factor stable, or a seed artifact?

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

# Find (A, p) with ord_p(A) ∈ [30, 60] for cat maps in {A=(3,1,2,1), (5,2,2,1), (7,3,2,1)}
# (A=(2,1,1,1) already covered by v8).
function find_candidates(A, p_lo, p_hi, ord_lo, ord_hi)
    function sieve_primes(lo, hi)
        is_p = trues(hi - lo + 1)
        for p in 2:isqrt(hi)
            for j in max(p*p, div(lo + p - 1, p) * p):p:hi
                if j >= lo
                    is_p[j - lo + 1] = false
                end
            end
        end
        return [lo - 1 + i for i in 1:length(is_p) if is_p[i]]
    end
    primes = sieve_primes(p_lo, p_hi)
    a, b, c, d = A
    tr = (a + d) % 2  # compute disc = tr^2 - 4 mod 2
    out = []
    for p in primes
        # split check
        disc = (tr * tr - 4) % p
        if disc < 0; disc += p; end
        if disc == 0; continue; end
        if powermod(disc, (p - 1) ÷ 2, p) != 1
            continue
        end
        # ord_p(A)
        ord_A = projective_order_brute(A, p; max_iter=p^2)
        if ord_A < ord_lo || ord_A > ord_hi
            continue
        end
        # k
        k = k_of_p(A, p)
        if k < 1
            continue
        end
        # pred_m
        pred_m = p ÷ ord_A
        if pred_m < 30
            continue
        end
        push!(out, (p, ord_A, k, pred_m))
    end
    return out
end

function run_one(A, p, seed_v; n_hecke=64, C=100, label="")
    N = p
    print("  ord_p(A) (brute) ... "); flush(stdout)
    t0 = time()
    proj_ord = projective_order_brute(A, p; max_iter=p^2)
    @printf("%d  (%.2fs)\n", proj_ord, time() - t0); flush(stdout)

    k_alpha = k_of_p(A, p)
    println("  k = ord_p(α) = $k_alpha")
    if k_alpha < 1 || proj_ord < 1
        println("  SKIP")
        return nothing
    end

    print("  Building U_A ... "); flush(stdout)
    t0 = time()
    U = U_cat_fft(A, N)
    @printf("%.1fs\n", time() - t0); flush(stdout)

    print("  Eigendecomp ... "); flush(stdout)
    t0 = time()
    ev_U = eigvals(U)
    @printf("%.1fs\n", time() - t0); flush(stdout)

    th_U = angle.(ev_U)
    window_width = 2π / proj_ord
    counts = zeros(Int, proj_ord)
    for t in th_U
        j = mod(round(Int, t / window_width), proj_ord) + 1
        counts[j] += 1
    end
    max_count = maximum(counts)
    println("  Multiplet size = $max_count")

    if max_count < 12
        println("  Multiplet too small; SKIP")
        return nothing
    end

    j_max = argmax(counts)
    angle_center = (j_max - 0.5) * window_width
    idx = [i for i in 1:N if abs(angle(ev_U[i]) - angle_center) < window_width / 2]
    m = length(idx)
    if m < 12
        println("  Could not extract m=$m; SKIP"); return nothing
    end
    U_sub = U[:, idx]

    V_full = V_arith_cycles(N, C, seed_v)
    V_lam_raw = U_sub' * V_full * U_sub
    V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))

    kurt_raw = kurt_offdiag(V_lam)
    println("  RAW kurt = $(round(kurt_raw, digits=4))")

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
    factor = abs(kurt_raw) / max(abs(kurt_R), 1e-6)
    println("  R_n kurt = $(round(kurt_R, digits=4)), reduction = $(round(factor, digits=1))x")
    tail = churilov_tail(R_n)
    println("  Churilov tail: $(tail)")

    return Dict(
        "A" => collect(A), "p" => p, "ord_p_A" => proj_ord, "k_alpha" => k_alpha,
        "m" => m, "kurt_raw" => kurt_raw, "kurt_R" => kurt_R,
        "reduction_factor" => factor, "tail" => tail,
        "label" => label, "seed" => seed_v,
    )
end

out = IOBuffer()
println(out, "hecke_real_centraliser_v9_v10.jl (RING 1.2 v9+v10, 2026-08-28)")
println(out, "julia ", VERSION, "  timestamp=", now())
println(out, "")

# === v9: UNIVERSALITY across cat maps ===
println(out, "=" ^ 70)
println(out, "v9 — UNIVERSALITY across cat maps")
println(out, "=" ^ 70)
println(out, "")

v9_results = []
for A in [(3, 1, 2, 1), (5, 2, 2, 1), (7, 3, 2, 1)]
    a, b, c, d = A
    tr = a + d
    disc = tr * tr - 4
    println(out, "")
    println(out, "--- A=$A (tr=$tr, disc=$disc) ---")
    flush(out)

    # disc must be a QR for the prime to be split
    candidates = find_candidates(A, 500, 5000, 30, 60)
    println(out, "  Candidates with ord ∈ [30, 60]: $(length(candidates))")
    for c in candidates[1:min(3, length(candidates))]
        println(out, "    p=$(c[1]) ord=$(c[2]) k=$(c[3]) pred_m=$(c[4])")
    end

    if isempty(candidates)
        println(out, "  NO CANDIDATES — skipping this A")
        continue
    end

    # Take the best (largest pred_m) candidate
    sort!(candidates, by=c->-c[4])
    best = candidates[1]
    p, ord_A, k, pred_m = best
    println(out, "")
    println(out, "  Running Hecke-centring on best (A, p) = ($A, $p), k=$k, pred_m=$pred_m")
    flush(out)
    println(out, "")
    label = "v9 cat-map A=$A @ p=$p"
    res = run_one(A, p, 42; n_hecke=64, C=100, label=label)
    if res !== nothing
        push!(v9_results, res)
    end
end

# === v10: REPRODUCIBILITY across seeds ===
println(out, "")
println(out, "=" ^ 70)
println(out, "v10 — REPRODUCIBILITY across V_arith_cycles seeds")
println(out, "=" ^ 70)
println(out, "")

seeds = [42, 7, 123, 999, 31337, 271828]
A = (2, 1, 1, 1)
p = 3469  # best from v8: k=51, reduction=1294x
println(out, "Design: A=$A @ p=$p (best v8 design point)")
flush(out)

v10_results = []
for seed_v in seeds
    println(out, "")
    println(out, "--- seed=$seed_v ---")
    println(out, "")
    label = "v10 seed=$seed_v"
    res = run_one(A, p, seed_v; n_hecke=64, C=100, label=label)
    if res !== nothing
        push!(v10_results, res)
    end
end

# === Summaries ===
println(out, "")
println(out, "=" ^ 70)
println(out, "v9 SUMMARY: universality across cat maps")
println(out, "=" ^ 70)
println(out, "")
for r in v9_results
    @printf(out, "  A=%s @ p=%d: k=%d, m=%d, RAW=%.4f, R_n=%.4f, reduction=%.1fx\n",
            string(r["A"]), r["p"], r["k_alpha"], r["m"],
            r["kurt_raw"], r["kurt_R"], r["reduction_factor"])
end
if length(v9_results) >= 2
    factors = [r["reduction_factor"] for r in v9_results]
    if all(f > 5 for f in factors)
        println(out, "  VERDICT: Hecke-collapse HOLDS across multiple cat maps (universal).")
    else
        println(out, "  VERDICT: Hecke-collapse is A-DEPENDENT (not universal).")
    end
end

println(out, "")
println(out, "=" ^ 70)
println(out, "v10 SUMMARY: reproducibility across seeds")
println(out, "=" ^ 70)
println(out, "")
factors = Float64[]
ratios = Float64[]
kurt_Rs = Float64[]
tails_ratio = Float64[]
for r in v10_results
    @printf(out, "  seed=%d: kurt_raw=%.4f, kurt_R=%.4f, reduction=%.1fx, churilov=%.2f\n",
            r["seed"], r["kurt_raw"], r["kurt_R"], r["reduction_factor"],
            r["tail"]["ratio_max_over_median"])
    push!(factors, r["reduction_factor"])
    push!(ratios, r["kurt_R"])
    push!(kurt_Rs, r["kurt_R"])
    push!(tails_ratio, r["tail"]["ratio_max_over_median"])
end
println(out, "")
println(out, "Statistics across 6 seeds:")
@printf(out, "  reduction factor: mean=%.1f, std=%.1f, CV=%.1f%%\n",
        mean(factors), std(factors), 100 * std(factors) / max(mean(factors), 1e-6))
@printf(out, "  R_n kurtosis:     mean=%.4f, std=%.4f, range=[%.4f, %.4f]\n",
        mean(kurt_Rs), std(kurt_Rs), minimum(kurt_Rs), maximum(kurt_Rs))
@printf(out, "  Churilov ratio:   mean=%.2f, std=%.2f\n",
        mean(tails_ratio), std(tails_ratio))
println(out, "")

if std(factors) / max(mean(factors), 1e-6) < 0.30
    println(out, "VERDICT: reduction factor is STABLE across seeds (CV < 30%).")
else
    println(out, "VERDICT: reduction factor VARIES significantly across seeds (CV ≥ 30%).")
end

out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v9_v10.txt")
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
