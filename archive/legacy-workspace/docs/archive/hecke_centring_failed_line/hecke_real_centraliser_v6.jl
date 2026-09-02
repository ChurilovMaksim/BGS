# hecke_real_centraliser_v6.jl
# RING 1.2 v6 — ROBUST multiplet identification (uses true ord_p(A) computation)
#
# RING 1.2 v5 showed: with tol=1e-6, ALL design points have m=1 (no
# multiplet detected). RING 1.2 v6 uses a different approach: explicitly
# compute the projective order ord_p(A) using matrix exponentiation
# (not O(N^2) lattice walk) — for ord < 100 this is fast. Then:
#   * U_A^ord = I (mod p) on the lattice
#   * The eigenvalues of U_A are ord-th roots of unity
#   * A multiplet of size m is a single eigenspace of U_A^ord
#     (i.e., a Frobenius eigenspace)
#   * The true multiplicity is the dimension of that eigenspace,
#     which equals the number of lattice vectors (x, y) with
#     the same U_A^ord-eigenvalue (in the metaplectic model).
#
# Honest caveat: the metaplectic propagator U_A on L^2(Z/NZ) has
# eigenvalues that are (ord/th^ord)th roots of unity for the
# Theta-function interpretation. The "multiplet m" in R54 was
# apparently the *degeneracy* of one such eigenspace, not the
# *number* of distinct eigenvalues. So the R54 measurement was
# probably correct in spirit but wrong in scale (the right number
# is m = k · K where k is the projective order and K is the
# multiplicity of each U_A^ord-eigenspace in the metaplectic model).
#
# v6 design: compute U_A^ord exactly on the lattice, find the
# eigenvalues of U_A restricted to the lattice, identify multiplets
# of size m ≥ 8. Test the Churilov tail on the m=8-32 multiplets.

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

function projective_order(A, p)
    """Find the smallest ord ≥ 1 with A^ord ≡ I (mod p)."""
    a, b, c, d = A
    for ord in 1:min(2 * p, 1000)  # bound for safety
        # A^ord
        m11, m12, m21, m22 = 1, 0, 0, 1  # identity
        for _ in 1:ord
            m11, m12, m21, m22 = (
                (a * m11 + b * m21) % p,
                (a * m12 + b * m22) % p,
                (c * m11 + d * m21) % p,
                (c * m12 + d * m22) % p,
            )
        end
        if (m11, m12, m21, m22) == (1, 0, 0, 1)
            return ord
        end
    end
    return -1
end

function k_of_p(A, p)
    """k = ord_p(alpha) where alpha is the split eigenvalue of A mod p.
    The split eigenvalue is a root of x^2 - tr(A) x + 1 = 0 in F_p.
    """
    a, b, c, d = A
    tr = (a + d) % p
    disc = (tr * tr - 4) % p
    # x = (tr ± sqrt(disc))/2 mod p
    # Use Legendre symbol for sqrt
    if disc < 0; disc += p; end
    # Check Legendre
    ls = powermod(disc, (p - 1) ÷ 2, p)
    if ls != 1
        return -1  # inert
    end
    # Tonelli-Shanks for sqrt(disc) mod p
    s = tonelli_shanks(disc, p)
    inv2 = powermod(2, -1, p)
    alpha = ((tr + s) * inv2) % p
    if alpha == 0; return -1; end
    # ord_p(alpha)
    for ord in 1:p
        if powermod(alpha, ord, p) == 1
            return ord
        end
    end
    return -1
end

function tonelli_shanks(n, p)
    """Tonelli-Shanks sqrt mod p. Returns r with r^2 ≡ n (mod p)."""
    if powermod(n, (p - 1) ÷ 2, p) != 1
        error("not a QR")
    end
    # Factor out 2s
    q = p - 1
    s = 0
    while q % 2 == 0
        q ÷= 2
        s += 1
    end
    # Find z with Legendre symbol -1
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

# V_arith and kurt_offdiag (corrected for Hermitian)
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
    # Manual excess kurtosis: E[(X-mu)^4] / sigma^4 - 3
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
    s_med = sv[max(1, n÷2)]
    s_min = sv[end]
    tail = Dict{String, Any}(
        "sigma_max" => sv[1],
        "sigma_median" => s_med,
        "sigma_min" => s_min,
        "ratio_max_over_median" => sv[1] / max(s_med, 1e-12),
    )
    for thresh in [1e-1, 1e-2, 1e-3, 1e-4]
        cnt = count(>(thresh), sv)
        tail["rank_above_$(thresh)"] = cnt
    end
    return tail
end

design_points = [
    (2, 1, 1, 1, 4481, "R62 design"),
    (2, 1, 1, 1, 1597, "R54 design (ord=34)"),
    (3, 1, 2, 1, 1597, "alt (3,1,2,1) @ 1597"),
    (5, 2, 2, 1, 3571, "R54 design (5,2,2,1)"),
    (3, 1, 2, 1, 3001, "alt (3,1,2,1) @ 3001"),
    (3, 1, 2, 1, 2207, "inert prime 2207"),
]

out = IOBuffer()
println(out, "hecke_real_centraliser_v6.jl (RING 1.2 v6 ROBUST, 2026-08-28)")
println(out, "julia ", VERSION, "  timestamp=", now())
println(out, "")

for (a, b, c, d, p, label) in design_points
    A = (a, b, c, d)
    N = p
    print(out, "=== A=$A @ p=$p ($label) ===\n"); flush(out)

    # True projective order
    print(out, "  Computing projective order ... "); flush(out)
    t0 = time()
    proj_ord = projective_order(A, p)
    @printf(out, "ord_p(A) = %d  (%.2fs)\n", proj_ord, time() - t0); flush(out)
    if proj_ord < 1
        println(out, "  SKIP: ord_p(A) not found in 1..1000"); flush(out); continue
    end

    # ord_p(alpha) = split eigenvalue order
    print(out, "  Computing k = ord_p(alpha) ... "); flush(out)
    t0 = time()
    k_alpha = k_of_p(A, p)
    @printf(out, "k = %d  (%.2fs)\n", k_alpha, time() - t0); flush(out)
    if k_alpha < 1
        println(out, "  SKIP: p is inert for this A"); continue
    end

    # Multiplicity: in the metaplectic model, the "multiplet size" m
    # for the eigenspace of U_A^proj_ord with eigenvalue ζ^proj_ord
    # is the dimension of the corresponding eigenspace of U_A^proj_ord
    # on L^2(Z/NZ). For the cat map, this is exactly proj_ord.
    # But R54 measured m=70 at p=4481 with ord=64. So R54 must have
    # been using m = (proj_ord · k) / gcd(proj_ord, k) or similar.
    m_predicted_1 = proj_ord
    m_predicted_2 = k_alpha
    m_predicted_3 = lcm(proj_ord, k_alpha)
    @printf(out, "  predicted multiplet sizes: ord=%d, k=%d, lcm=%d\n",
            m_predicted_1, m_predicted_2, m_predicted_3); flush(out)

    # Build U_A
    print(out, "  Building U_A ... "); flush(out)
    t0 = time()
    U = U_cat_fft(A, N)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # Multiplets from U_A^proj_ord eigenspace
    print(out, "  Eigendecomp of U_A ... "); flush(out)
    t0 = time()
    ev_U = eigvals(U)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # The eigenspace of U_A for eigenvalue ζ^j (j=0,...,proj_ord-1) is
    # a multiplet.  Find the largest one.
    # Sort eigenvalues by angle and look for the largest cluster
    # within angular distance 2π/proj_ord * 1.1 (a single multiplet
    # has angles within 2π/proj_ord).
    th_U = angle.(ev_U)
    sort_idx = sortperm(th_U)
    th_U_sorted = th_U[sort_idx]
    # Compute the gap pattern: for j=0..proj_ord-1, find the
    # number of eigs in the j-th angular window of width
    # 2π/proj_ord.
    window_width = 2π / proj_ord
counts = zeros(Int, proj_ord)
    for t in th_U
        # Julia is 1-based; angle(t) in [-pi, pi], so
        # round(Int, t / window_width) may be negative.
        # mod(x, n) in Julia returns value in [0, n), so +1 is the fix.
        j = mod(round(Int, t / window_width), proj_ord) + 1
        counts[j] += 1
    end
    max_count = maximum(counts)
    @printf(out, "  Multiplet size (max window count) = %d (expect ~N/proj_ord = %d)\n",
            max_count, N ÷ proj_ord); flush(out)

    # Now: build a Churilov probe if the multiplet is big enough
    if max_count < 12
        println(out, "  Multiplet too small; skipping Churilov probe")
        continue
    end

    # Find the eigenspace of U_A for the eigenvalue with the
    # most-counts window.  Use the centroid angle.
    j_max = argmax(counts)
    angle_center = (j_max + 0.5) * window_width
    idx = [i for i in 1:N if abs(angle(ev_U[i]) - angle_center) < window_width / 2]
    m = length(idx)
    if m < 12
        println(out, "  Could not reconstruct multiplet (m=$m)")
        continue
    end
    @printf(out, "  Reconstructed multiplet: m=%d\n", m); flush(out)
    U_sub = U[:, idx]

    # V_arth
    print(out, "  Building V_arith_cycles ... "); flush(out)
    t0 = time()
    V_full = V_arith_cycles(N, 100, 42)
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # Compress
    print(out, "  Compressing V_lam ... "); flush(out)
    t0 = time()
    V_lam_raw = U_sub' * V_full * U_sub
    V_lam = Hermitian(Matrix((V_lam_raw + V_lam_raw') / 2))
    @printf(out, "%.1fs\n", time() - t0); flush(out)

    # RAW stats
    kurt_raw = kurt_offdiag(V_lam)
    println(out, "  RAW: kurt=$(round(kurt_raw, digits=4))")

    # Haar-Hecke centered
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
    println(out, "  R_n (Haar-Hecke): kurt=$(round(kurt_R, digits=4))")
    tail_haar = churilov_tail(R_haar)
    println(out, "  Churilov tail (Haar): $(tail_haar)")
    println(out, "")
end

out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v6.txt")
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
