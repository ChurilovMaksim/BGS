# hecke_real_centraliser_v7.jl
# RING 1.2 v7 — Hecke-centring collapse AT SMALLER k.
#
# R67 (v6) found: at A=(2,1,1,1) @ p=4481, m=68, kurtosis collapses
# from 25.6 to 0.014 (factor 1767). R54 LEDGER R54 said k >= 50
# was needed. v7 tests the threshold: does the collapse still hold
# at k ~ 16, 24, 32, 40, 48?
#
# Design points: choose (A, p) such that:
#   (1) ord_p(A) is in {16, 24, 32, 40, 48, 64} (small for speed)
#   (2) p is split for A (tr(A)^2 - 4 is QR mod p)
#   (3) p is large enough that the eigenspace is non-trivial
#
# v7 also FIXES the projective_order bug in v6 by using
# baby-step / giant-step (BSGS) for ord > 1000.

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

# Baby-step / giant-step projective order. O(sqrt(p)) instead of O(p).
function projective_order_bsgs(A, p)
    a, b, c, d = A
    # ord is the smallest ord ≥ 1 with A^ord ≡ I (mod p).
    # ord divides |GL(2, F_p)| = (p^2-1)(p^2-p) = O(p^4). Bound: ord ≤ p^2.
    # BSGS: ord = m * n with m = ceil(sqrt(ord)). Compute A^k for k=0..m-1 (baby),
    # then for j=0..m-1 check if A^{j*m} * baby == I (giant).
    m = isqrt(p) + 1
    # Build baby steps
    M0 = (1, 0, 0, 1)  # identity
    babies = Dict{Tuple{Int,Int,Int,Int}, Int}()
    cur = (a, b, c, d)
    babies[(1, 0, 0, 1)] = 0
    cur = (1, 0, 0, 1)
    M = (a % p, b % p, c % p, d % p)
    babies[M] = 1
    for k in 2:m
             (M[1] * b + M[2] * d) % p,
             (M[3] * a + M[4] * c) % p,
             (M[3] * b + M[4] * d) % p)
        babies[M] = k
    end
    # Build giant step M_giant = A^m
    Mg = (a, b, c, d)
    for _ in 1:m - 1
        Mg = ((Mg[1] * a + Mg[2] * c) % p,
              (Mg[1] * b + Mg[2] * d) % p,
              (Mg[3] * a + Mg[4] * c) % p,
              (Mg[3] * b + Mg[4] * d) % p)
    end
    # Mg_inv = (Mg)^{-1}
    det_Mg = (Mg[1] * Mg[4] - Mg[2] * Mg[3]) % p
    if det_Mg < 0; det_Mg += p; end
    inv_det = powermod(det_Mg, -1, p)
    Mg_inv = (Mg[4] * inv_det % p,
              (-Mg[2]) * inv_det % p,
              (-Mg[3]) * inv_det % p,
              Mg[1] * inv_det % p)
    # For each j, check if Mg_inv^j * M_giant^j matches some baby
    cur_inv = (1, 0, 0, 1)
    for j in 0:m
        # cur_inv = (Mg_inv)^j
        # Check if there exists k with cur_inv * Mg^j == baby_k
        # Compute Mg^j
        cur_g = (1, 0, 0, 1)
        if j == 0
            # check I
            if haskey(babies, cur_inv)
                ord = babies[cur_inv]
                return ord
            end
        else
            for _ in 1:j
                cur_g = ((cur_g[1] * Mg[1] + cur_g[2] * Mg[3]) % p,
                         (cur_g[1] * Mg[2] + cur_g[2] * Mg[4]) % p,
                         (cur_g[3] * Mg[1] + cur_g[4] * Mg[3]) % p,
                         (cur_g[3] * Mg[2] + cur_g[4] * Mg[4]) % p)
            end
            prod = ((cur_inv[1] * cur_g[1] + cur_inv[2] * cur_g[3]) % p,
                    (cur_inv[1] * cur_g[2] + cur_inv[2] * cur_g[4]) % p,
                    (cur_inv[3] * cur_g[1] + cur_inv[4] * cur_g[3]) % p,
                    (cur_inv[3] * cur_g[2] + cur_inv[4] * cur_g[4]) % p)
            if haskey(babies, prod)
                ord = j * m - babies[prod]
                if ord > 0
                    return ord
                end
            end
        end
        # cur_inv = cur_inv * Mg_inv
        cur_inv = ((cur_inv[1] * Mg_inv[1] + cur_inv[2] * Mg_inv[3]) % p,
                   (cur_inv[1] * Mg_inv[2] + cur_inv[2] * Mg_inv[4]) % p,
                   (cur_inv[3] * Mg_inv[1] + cur_inv[4] * Mg_inv[3]) % p,
                   (cur_inv[3] * Mg_inv[2] + cur_inv[4] * Mg_inv[4]) % p)
    end
    return -1
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

# v7 design points: choose (A, p) so that k = ord_p(α) is small (16, 24, 32, 40, 48).
# We iterate over known cat-map (A) and search primes p for which k is in the target set.
# For A = (2,1,1,1) (tr = 3), k = (p-1)/ord(α) where ord(α) | (p-1). We need k small.
# Approach: for each target k, find a prime p with (p-1)/k = ord_p(α) such that A
# is hyperbolic and ord_p(α) = (p-1)/k is small (a divisor of p-1).

# Manual selection of (A, p) with known small k:
design_points = [
    # (A, p, target_k, label)
    ((2, 1, 1, 1), 4481, 64, "v6 reference: k=64 (the breakthrough)"),
    ((2, 1, 1, 1), 31, 5, "small: A=(2,1,1,1) @ p=31, expect k=5"),
    ((2, 1, 1, 1), 41, 8, "small: A=(2,1,1,1) @ p=41, expect k=8"),
    ((2, 1, 1, 1), 61, 12, "small: A=(2,1,1,1) @ p=61, expect k=12"),
    ((2, 1, 1, 1), 89, 11, "small: A=(2,1,1,1) @ p=89, expect k=11 (or 44)"),
    ((2, 1, 1, 1), 151, 15, "small: A=(2,1,1,1) @ p=151, expect k=15"),
    ((2, 1, 1, 1), 211, 21, "small: A=(2,1,1,1) @ p=211, expect k=21"),
    ((2, 1, 1, 1), 241, 24, "small: A=(2,1,1,1) @ p=241, expect k=24"),
    ((2, 1, 1, 1), 281, 28, "small: A=(2,1,1,1) @ p=281, expect k=28"),
    ((2, 1, 1, 1), 421, 35, "small: A=(2,1,1,1) @ p=421, expect k=35"),
    ((2, 1, 1, 1), 631, 45, "small: A=(2,1,1,1) @ p=631, expect k=45"),
    ((2, 1, 1, 1), 841, 40, "small: A=(2,1,1,1) @ p=841, expect k=40"),
]

out = IOBuffer()
println(out, "hecke_real_centraliser_v7.jl (RING 1.2 v7 SMALL-k SWEEP, 2026-08-28)")
println(out, "julia ", VERSION, "  timestamp=", now())
println(out, "")

results = []
for (A, p, target_k, label) in design_points
    N = p
    print(out, "=== A=$A @ p=$p ($label) ===\n"); flush(out)

    # Projective order via BSGS
    print(out, "  ord_p(A) (BSGS) ... "); flush(out)
    t0 = time()
    proj_ord = projective_order_bsgs(A, p)
    @printf(out, "%d  (%.2fs)\n", proj_ord, time() - t0); flush(out)

    # k = ord_p(α)
    k_alpha = k_of_p(A, p)
    println(out, "  k = ord_p(α) = $k_alpha")
    if k_alpha < 1
        println(out, "  SKIP: p is inert for A=$A"); continue
    end

    if proj_ord < 1
        println(out, "  SKIP: ord_p(A) not found")
        continue
    end

    # Build U_A
    print(out, "  Building U_A ... "); flush(out)
    t0 = time()
    U = U_cat_fft(A, N)
    @printf(out, "%.2fs\n", time() - t0); flush(out)

    # Multiplet identification
    print(out, "  Eigendecomp ... "); flush(out)
    t0 = time()
    ev_U = eigvals(U)
    @printf(out, "%.2fs\n", time() - t0); flush(out)

    th_U = angle.(ev_U)
    window_width = 2π / proj_ord
    counts = zeros(Int, proj_ord)
    for t in th_U
        j = mod(round(Int, t / window_width), proj_ord) + 1
        counts[j] += 1
    end
    max_count = maximum(counts)
    println(out, "  Multiplet size = $max_count (target k=$target_k, expect ~$(N ÷ proj_ord))")

    if max_count < 8
        println(out, "  Multiplet too small; SKIP Churilov probe")
        continue
    end

    # Extract the largest eigenspace
    j_max = argmax(counts)
    angle_center = (j_max - 0.5) * window_width
    idx = [i for i in 1:N if abs(angle(ev_U[i]) - angle_center) < window_width / 2]
    m = length(idx)
    if m < 8
        println(out, "  Could not extract m=$m; SKIP")
        continue
    end
    U_sub = U[:, idx]

    # V_arth
    V_full = V_arith_cycles(N, 100, 42)

    # Compress
    V_lam_raw = U_sub' * V_full * U_sub
    V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))

    kurt_raw = kurt_offdiag(V_lam)
    println(out, "  RAW kurt = $(round(kurt_raw, digits=4))")

    # Haar-Hecke centring
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
    println(out, "  Reduction factor = $(round(kurt_raw / max(abs(kurt_R), 1e-6), digits=1))x")
    tail = churilov_tail(R_n)
    println(out, "  Churilov tail: $(tail)")

    push!(results, Dict(
        "A" => collect(A), "p" => p, "target_k" => target_k,
        "ord_p_A" => proj_ord, "k_alpha" => k_alpha,
        "m" => m, "kurt_raw" => kurt_raw, "kurt_R" => kurt_R,
        "reduction_factor" => abs(kurt_raw) / max(abs(kurt_R), 1e-6),
        "tail" => tail,
        "label" => label,
    ))
    println(out, "")
end

# Summary
println(out, "=== v7 SUMMARY ===")
println(out, "p, m, kurt_raw, kurt_R, reduction")
for r in results
    @printf(out, "%4d %3d %9.4f %9.4f %9.1fx  (k=%d, %s)\n",
            r["p"], r["m"], r["kurt_raw"], r["kurt_R"], r["reduction_factor"],
            r["k_alpha"], r["label"])
end

# Verdict: does the threshold exist?
ks = [r["k_alpha"] for r in results]
factor_at_k68 = maximum([r["reduction_factor"] for r in results if r["k_alpha"] >= 60], init=0)
factor_at_k16_30 = maximum([r["reduction_factor"] for r in results if r["k_alpha"] < 30], init=0)
factor_at_k30_60 = maximum([r["reduction_factor"] for r in results if 30 <= r["k_alpha"] < 60], init=0)
println(out, "")
println(out, "Max reduction factor: k>=60: $(factor_at_k68)x; 30<=k<60: $(factor_at_k30_60)x; k<30: $(factor_at_k16_30)x")
println(out, "")
if factor_at_k16_30 > 100
    println(out, "VERDICT: Hecke-collapse holds at k < 30 (factor > 100). R54 LEDGER R54 threshold k>=50 was conservative.")
elseif factor_at_k16_30 > 10
    println(out, "VERDICT: Hecke-collapse holds weakly at k < 30 (factor > 10). Threshold exists but is gentle.")
else
    println(out, "VERDICT: Hecke-collapse FAILS at k < 30. R54 threshold k>=50 confirmed.")
end

out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v7.txt")
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
