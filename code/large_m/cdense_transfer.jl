# Run 81 (Julia): THE GROWTH CONSTANT OF THE SHAPE LANGUAGE (op:Cdense).
# =======================================================================
# Theorem-shape: the number of accepting walks of cost R in the
# reversed-normalized automaton has an exponential growth constant
#     C_dense = lim_{B->infty} C_B,
# where C_B = 1/x*(B) is the Perron constant of the FINITE truncated
# transfer matrix on the state ellipse |a + b*lambda| <= B with edge
# weight x^|c| (each digit c costs |c|).  Monotone in B; every accepting
# walk of cost R lives in the truncation B = R (upper bound), and walks
# inside a fixed truncation B complete to acceptance with an O(B) cost
# shift (lower bound) — so the limit exists and is computable.
#
# This script computes C_B for a ladder of B and compares with the exact
# DP counts S(R)^(1/R) from r80_julia_bigdp.jl (2.078 @ R=50, 2.179 @ R=80).
#
# Output: artifacts/r81/cdense_transfer.json (+ stdout)

using LinearAlgebra

# The CONTRACTING lambda'-dynamics: t = a + b*lamp (lamp = 1/lam in (0,1)),
# t' = c + lamp*t  <=>  (a, b) --c--> (c - b, a + 3b).
# The relation language: sum c_j lamp^j = 0  <=>  the walk 0 -> ... -> 0.
# The growth constant of the shape language is
#     C_dense = lim_{B->infty} 1/x*(B),   rho(A_B(x*)) = 1,
# where A_B is the cost-weighted adjacency on the truncation
# |a + b*lamp| <= B (returning walks dominate: the truncated graphs are
# essentially strongly connected).

const LAMP = (3 - sqrt(5.0)) / 2

val(s::Tuple{Int,Int}) = s[1] + s[2] * LAMP
trans(s::Tuple{Int,Int}, c::Int) = (c - s[2], s[1] + 3 * s[2])

"states in the slab-ellipse |a + b*lamp| <= B"
function ellipse_states(B::Int)
    st = Tuple{Int,Int}[]
    for b in -ceil(Int, B / LAMP):ceil(Int, B / LAMP)
        lo = ceil(Int, -B - b * LAMP - 1e-9)
        hi = floor(Int, B - b * LAMP + 1e-9)
        for a in lo:hi
            push!(st, (a, b))
        end
    end
    return st
end

"sparse rows of the weighted transfer matrix at parameter x"
function transfer_rows(B::Int, x::Float64, index::Dict{Tuple{Int,Int},Int})
    rows = Vector{Tuple{Int,Float64}}[]
    for s in ellipse_states(B)
        a, b = s
        # targets: val(s') = c + lamp*val(s), so |val(s')| <= B
        # <=>  c in [-B - lamp*val(s), B - lamp*val(s)]
        v0 = LAMP * val(s)
        clo = ceil(Int, -B - v0 - 1e-9)
        chi = floor(Int, B - v0 + 1e-9)
        row = Tuple{Int,Float64}[]
        for c in clo:chi
            s2 = trans(s, c)
            abs(val(s2)) <= B * (1 + 1e-12) + 1e-9 || continue
            push!(row, (index[s2], x ^ abs(c)))
        end
        push!(rows, row)
    end
    return rows
end

"largest eigenvalue by power iteration"
function perron(rows::Vector{Vector{Tuple{Int,Float64}}}; iters::Int = 400)
    n = length(rows)
    v = ones(Float64, n) / sqrt(n)
    rho = 0.0
    for it in 1:iters
        w = zeros(Float64, n)
        for i in 1:n
            ai = rows[i]
            isempty(ai) && continue
            acc = 0.0
            for (j, wgt) in ai
                acc += wgt * v[j]
            end
            w[i] = acc
        end
        nrm = norm(w)
        nrm == 0.0 && return 0.0
        rho = nrm
        v = w ./ nrm
    end
    return rho
end

"C_B: solve rho(M_B(x)) = 1 by bisection; C_B = 1/x*"
function C_B(B::Int; tol::Float64 = 1e-10)
    index = Dict{Tuple{Int,Int},Int}()
    sts = ellipse_states(B)
    for (i, s) in enumerate(sts)
        index[s] = i
    end
    f(x) = perron(transfer_rows(B, x, index); iters = 300) - 1.0
    lo, hi = 0.30, 0.70     # x* near 1/2.2 ~ 0.45; rho increasing in x
    f(lo) <= 0 || error("x* below 0.3 (C_B > 3.3)?")
    f(hi) >= 0 || error("x* above 0.7 (C_B < 1.4)?")
    for _ in 1:60
        mid = 0.5 * (lo + hi)
        if f(mid) <= 0
            lo = mid
        else
            hi = mid
        end
        hi - lo < tol && break
    end
    return 1.0 / (0.5 * (lo + hi)), length(sts)
end

function main()
    out = Dict{String,Any}(
        "meta" => Dict("script" => "src/r81_cdense_transfer.jl",
                       "julia" => string(VERSION), "date" => "2026-08-29"))
    println("B      states     x*          C_B")
    xs = Float64[]; ns = Int[]
    for B in (4, 6, 8, 12, 16, 24, 32, 48, 64)
        t0 = time()
        c, nst = C_B(B)
        println(lpad(B, 4), "  ", lpad(nst, 7), "   ",
                round(1 / c, digits = 6), "   ", round(c, digits = 6),
                "  (", round(time() - t0, digits = 1), " s)")
        push!(xs, c); push!(ns, nst)
        out[string("CB_", length(xs))] = Dict("B" => B, "states" => nst,
                                              "C" => c, "x" => 1 / c)
    end
    # consistency anchors from the exact DP (r80_julia_bigdp.jl)
    println("\nDP anchors:  S(50)^(1/50) = 2.0781   S(80)^(1/80) = 2.1794 (rising)")
    println("extrapolated C_B ladder above; the monotone limit is C_dense.")
    isdir("artifacts/r81") || mkpath("artifacts/r81")
    open("artifacts/r81/cdense_transfer.json", "w") do f
        write(f, jdump(out))
    end
    println("artifact -> artifacts/r81/cdense_transfer.json")
end

# minimal JSON writer
jesc(x::AbstractString) = string('"', replace(replace(x, '\\' => "\\\\"), '"' => "\\\""), '"')
jdump(x) = jesc(string(x))
jdump(x::Int) = string(x)
jdump(x::Float64) = string(x)
function jdump(d::Dict)
    "{" * join([jesc(string(k)) * ":" * jdump(v) for (k, v) in d], ",") * "}"
end

main()
