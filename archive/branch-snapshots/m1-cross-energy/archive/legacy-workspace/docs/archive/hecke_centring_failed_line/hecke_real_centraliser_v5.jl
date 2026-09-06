# hecke_real_centraliser_v5.jl
# RING 1.2 v5 — DIAGNOSTIC: what is the true multiplet structure?
#
# R54 said A=(2,1,1,1) @ p=4481 has m=70; R53 audit says projective order
# of A mod p is 32 (after the K-label fix). R62 inherited R54's number.
# This v5 diagnostic computes the true multiplet structure with two
# cluster tolerances and prints the multiplicity of every distinct
# eigenvalue-orbital of the cat-map propagator U_A.

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

# True multiplet = "Weyl orbit" of eigenvalues under cat-map power.
# U_A has ord_p(A) eigenvalues e^{2 pi i j / ord_p(A)} for j = 0, ..., ord-1.
# Each eigenvalue of U_A at order ord is a (k)th root with k = multiplicity.
function true_multiplets(N, A; p=N)
    a, b, c, d = A
    # Projective order of A mod p
    # Try ord from 1 up
    for ord in 1:N
        M = [a b; c d]
        Mn = Matrix{Int}(I, 2, 2)
        for _ in 1:ord
            Mn = Mn * M
        end
        if mod.(Mn, p) == [1 0; 0 1]
            return ord
        end
    end
    return -1
end

design_points = [
    (2, 1, 1, 1, 4481, "R62 design"),
    (2, 1, 1, 1, 1597, "R54 design"),
    (5, 2, 2, 1, 3571, "R54 design"),
    (3, 1, 2, 1, 1597, "alt (3,1,2,1) @ 1597"),
    (3, 1, 2, 1, 3571, "alt (3,1,2,1) @ 3571"),
    (3, 1, 2, 1, 2207, "inert prime 2207"),
    (3, 1, 2, 1, 3001, "small period 3001"),
]

out = IOBuffer()
println(out, "hecke_real_centraliser_v5.jl (RING 1.2 v5 DIAGNOSTIC, 2026-08-28)")
println(out, "julia ", VERSION, "  timestamp=", now())
println(out, "")

for (a, b, c, d, p, label) in design_points
    A = (a, b, c, d)
    N = p
    print(out, "=== A=$A @ p=$p ($label) ===\n"); flush(out)

    # True projective order
    print(out, "  Computing projective order ... "); flush(out)
    t0 = time()
    ord = true_multiplets(N, A)
    @printf(out, "ord_p(A) = %d  (%.1fs)\n", ord, time() - t0); flush(out)

    # Eigenvalues
    print(out, "  Building U_A and eigendecomp ... "); flush(out)
    t0 = time()
    U = U_cat_fft(A, N)
    ev_U = eigvals(U)
    @printf(out, "%.1fs  %d eigs\n", time() - t0, N); flush(out)

    # Multiplet size (the largest repeated eigenvalue's multiplicity)
    # Count exact matches: for each distinct angle, count eigenvalues within 1e-10
    th = angle.(ev_U)
    sort!(th)
    println(out, "  Angle histogram (mod 1, n_buckets=20):")
    buckets = zeros(Int, 20)
    for t in th
        b = floor(Int, mod(t, 2π) / (2π) * 20) + 1
        if b > 20; b = 20; end
        buckets[b] += 1
    end
    for b in 1:20
        @printf(out, "    [%2d] %.2f: %d\n", b, (b-1)/20, buckets[b])
    end

    # Cluster with two tolerances
    for tol in [1e-6, 1e-3, 1e-2, 5e-2]
        groups = cluster_eigs(ev_U; tol=tol)
        sizes = [length(g) for g in groups]
        max_size = maximum(sizes)
        n_groups = length(groups)
        # Number of groups of size >= 12 (statistically meaningful)
        n_big = count(>=(12), sizes)
        @printf(out, "  tol=%.0e: %d groups, max size %d, n(>=12)=%d\n",
                tol, n_groups, max_size, n_big); flush(out)
    end
    println(out, ""); flush(out)
end

out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "hecke_real_centraliser_v5.txt")
open(out_path, "w") do f
    print(f, String(take!(out)))
end
println("Wrote ", out_path)
