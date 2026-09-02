# find_small_ord_primes.jl
# RING 1.2 v8 — Find (A, p) with ord_p(A) in [30, 60] for the Hecke-collapse sweep.
#
# v7-FIXED found Hecke-collapse at k=21 (A=(2,1,1,1) @ p=211, reduction 5.3x).
# v7-FIXED found collapse at k=64 (A=(2,1,1,1) @ p=4481, reduction 295x).
# Gap: k=30-60 design points were not reached (multiplets too small).
#
# v8 sweeps primes p ∈ [500, 5000] and finds (A, p) with ord_p(A) in [30, 60]
# and ord_p(α) in [10, 30] — these give moderate multiplets and k in the
# intermediate range.

include("projective_order_brute.jl")

using Printf
using Dates

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

# Search primes p ∈ [500, 5000] for A = (2,1,1,1) with ord in [30, 60].
# The candidate primes must be:
#   (1) prime
#   (2) split for A = (2,1,1,1), i.e. tr(A)^2 - 4 = 5 is a QR mod p
#   (3) ord_p(A) ∈ [30, 60]
#   (4) ord_p(α) ∈ [10, 30] (so k = ord_p(α) is moderate, and the multiplet
#       of size m ≈ p/ord_p(A) ≥ 50)

A = (2, 1, 1, 1)

# Generate primes in [500, 5000] using a simple sieve
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

primes = sieve_primes(500, 5000)
println("Generated ", length(primes), " primes in [500, 5000]")

# A = (2,1,1,1), tr = 3, tr^2 - 4 = 5.
# split iff (5/p) = 1 iff p ≡ ±1 (mod 5).

candidates = []
for p in primes
    # Split check
    if p % 5 == 0
        continue  # p = 5
    end
    if powermod(5, (p - 1) ÷ 2, p) != 1
        continue  # inert
    end
    # Compute ord_p(A)
    ord_A = projective_order_brute(A, p; max_iter=p^2)
    if ord_A < 30 || ord_A > 60
        continue
    end
    # Compute k = ord_p(α)
    k = k_of_p(A, p)
    if k < 1
        continue
    end
    # Predicted multiplet: m ≈ p/ord_A
    pred_m = p ÷ ord_A
    if pred_m < 30
        continue
    end
    push!(candidates, (p, ord_A, k, pred_m))
end

println("Found ", length(candidates), " (p, ord_A, k) candidates with ord_A ∈ [30, 60]")
println()
println("p, ord_p(A), k=ord_p(α), pred_m=p/ord")
for c in candidates
    @printf("  %5d  %3d  %3d  %4d\n", c[1], c[2], c[3], c[4])
end
println()
println("Best 5 candidates (largest pred_m):")
sort!(candidates, by=c->-c[4])
for c in candidates[1:min(5, length(candidates))]
    println("  A=$A @ p=$(c[1]): ord=$(c[2]), k=$(c[3]), pred_m=$(c[4])")
end

# Write to artifact
out_path = joinpath(@__DIR__, "..", "artifacts", "julia", "find_small_ord_primes.txt")
open(out_path, "w") do f
    println(f, "find_small_ord_primes.jl (RING 1.2 v8, 2026-08-28)")
    println(f, "julia ", VERSION, "  timestamp=", now())
    println(f, "")
    println(f, "Found ", length(candidates), " (p, ord_A, k) candidates with ord_A ∈ [30, 60]")
    println(f, "")
    println(f, "All candidates:")
    for c in candidates
        @printf(f, "  %5d  %3d  %3d  %4d\n", c[1], c[2], c[3], c[4])
    end
    println(f, "")
    println(f, "Best 5 candidates (largest pred_m):")
    for c in candidates[1:min(5, length(candidates))]
        println(f, "  A=$A @ p=$(c[1]): ord=$(c[2]), k=$(c[3]), pred_m=$(c[4])")
    end
end
println("Wrote ", out_path)
