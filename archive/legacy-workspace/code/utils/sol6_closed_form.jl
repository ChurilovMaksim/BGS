# sol6_closed_form.jl
# RING 1.3 — Verify closed form `sol6 = 15k^3 - 5k^2 - 170k` for 3|k,
# search for closed form for 3∤k.
#
# Method: enumerate_sols from BGS/src/phase3_r6_families.py (port to Julia),
# then sweep (p, k) and compare observed sol6 with closed form.

using Printf
using Random

# --- Enumerate solutions (Julia port of phase3_r6_families.py) --------
function enumerate_sols(p, H_set)
    Hl = sort(collect(H_set))
    inv = Dict{Int, Int}()
    for h in Hl
        inv[h] = powermod(h, p - 2, p)
    end
    L = Dict{Tuple{Int,Int}, Vector{Tuple{Int,Int,Int}}}()
    for h1 in Hl
        s1 = h1
        t1 = inv[h1]
        for h3 in Hl
            s13 = (s1 + h3) % p
            t13 = (t1 + inv[h3]) % p
            for h5 in Hl
                kk = ((s13 + h5) % p, (t13 + inv[h5]) % p)
                if !haskey(L, kk)
                    L[kk] = Tuple{Int,Int,Int}[]
                end
                push!(L[kk], (h1, h3, h5))
            end
        end
    end
    out = Vector{NTuple{6, Int}}()
    for h2 in Hl, h4 in Hl
        s24 = (h2 + h4) % p
        t24 = (inv[h2] + inv[h4]) % p
        for h6 in Hl
            kk = ((s24 + h6) % p, (t24 + inv[h6]) % p)
            if haskey(L, kk)
                for trip in L[kk]
                    push!(out, (trip[1], trip[2], trip[3], h2, h4, h6))
                end
            end
        end
    end
    return out
end

# --- Test driver -------------------------------------------------------
results = []
ks_3 = [6, 12, 18, 24, 30, 36]      # divisible by 3
ks_not3 = [4, 8, 10, 14, 16, 20, 22, 26, 28]  # NOT divisible by 3
ps_pool = [101, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
           181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
           257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
           337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
           419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
           491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
           587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
           659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
           751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
           839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
           937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013]

# For each (p, k) where (p-1) % k == 0, find primitive root, build H, count sols
function get_H(p, k)
    # find primitive root
    g = 0
    for cand in 2:p-1
        is_prim = true
        for d in 2:Int(floor(sqrt(cand)))+1
            if cand % d == 0 && powermod(cand, (p-1)÷d, p) == 1
                is_prim = false
                break
            end
        end
        if is_prim
            g = cand
            break
        end
    end
    if g == 0
        return Set{Int}()
    end
    alpha = powermod(g, (p-1)÷k, p)
    H = Set{Int}()
    h = 1
    for _ in 1:k
        push!(H, h)
        h = (h * alpha) % p
    end
    return H
end

# Build datasets
for k in [ks_3; ks_not3]
    p_candidates = filter(p -> (p-1) % k == 0, ps_pool)
    if length(p_candidates) < 2
        continue
    end
    # take 2 primes for the (p-1) ≡ 0 check
    selected = p_candidates[1:min(3, length(p_candidates))]
    for p in selected
        H = get_H(p, k)
        if length(H) != k
            continue
        end
        sols = enumerate_sols(p, H)
        sol6 = length(sols)
        skel = 5*k*(3*k*k - 9*k + 8)
        A = sol6 - skel
        @printf("p=%5d k=%2d 3|k=%5s: sol6=%7d skel=%7d A=%6d  (A/40k^2=%.4f)\n",
                p, k, string(k%3==0), sol6, skel, A, A/(40*k*k))
        push!(results, (p, k, k%3==0, sol6, skel, A))
    end
end

# Test 3|k closed form: sol6 = 15k^3 - 5k^2 - 170k
println("\n=== Testing 3|k closed form: sol6 = 15k^3 - 5k^2 - 170k ===")
for (p, k, div3, sol6, skel, A) in results
    if div3
        pred = 15*k*k*k - 5*k*k - 170*k
        match = pred == sol6
        @printf("k=%2d p=%5d: pred=%7d sol6=%7d %s\n", k, p, pred, sol6, match ? "MATCH" : "MISMATCH")
    end
end

# Test 3∤k: try A(k) = c1*k^3 + c2*k^2 + c3*k + c4 (linear in k^3, k^2, k, 1)
# But k=22 has two values. Look at p-stable 3∤k configs (exclude k=22).
println("\n=== 3∤k data (p-stable) ===")
not3_data = [(p, k, sol6, A) for (p, k, div3, sol6, skel, A) in results if !div3 && k != 22]
for (p, k, sol6, A) in not3_data
    @printf("k=%2d p=%5d: sol6=%7d A=%6d  A/k^2=%.4f  A/k^3=%.4f\n", k, p, sol6, A, A/k^2, A/k^3)
end
# If A/k^2 is constant, A is quadratic in k.
# Compare with skel-leading-term: skel = 15k^3 - 45k^2 + 40k.
# For 3|k, A = skel + 40k^2 - 210k; sol6 = 15k^3 - 5k^2 - 170k.
# For 3∤k, what is A?

# Write artifact
open("artifacts/sol6_closed_form.txt", "w") do f
    println(f, "p  k  3|k  sol6  skel  A  A/(40k^2)")
    for r in results
        println(f, r[1], "  ", r[2], "  ", string(r[3]), "  ", r[4], "  ", r[5], "  ", r[6], "  ", r[6]/(40*r[2]*r[2]))
    end
end
println("\nWrote artifacts/sol6_closed_form.txt")
