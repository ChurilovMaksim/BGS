# RUN 82 (Julia) -- op:dpbug: an EXACT, self-checking count DP for the
# relation language of m_t(x) = x^2 - 3x + 1.
#
# Defects of the r80/r81 DP that this script removes:
#
#  (D1) DEAD STATE DIMENSION.  The old key was (a, b, u, w) with w = position
#       of the last nonzero letter.  w is never read: the accepting record uses
#       w2 = p + 1 (the current position), so carrying w only multiplied the
#       cell count by O(R) -- the direct cause of the memory exhaustion that
#       made the large-budget runs untrustworthy.  Key here: (a, b, u).
#
#  (D2) FLOAT CO-REACHABILITY FILTER.  |a + b*lambda| <= rem was evaluated in
#       Float64 with an ad-hoc 1e-9 slack.  Here the test is exact integer
#       arithmetic: with lambda = (3 + sqrt 5)/2,
#           a + b*lambda = ((2a + 3b) + b*sqrt 5) / 2,
#       so |a + b*lambda| <= rem  <=>  |A + B*sqrt 5| <= 2*rem with
#       A = 2a + 3b, B = b, decided by integer comparisons of 5B^2 against
#       squares.  No slack, no boundary ambiguity.
#
#  (D3) NO SELF-CHECK.  LESSON 81-C: the supermultiplicativity
#       N(R1 + R2) >= N(R1)*N(R2) (proven, R81.1) is now a built-in assertion
#       over ALL admissible pairs, and the budget-independence of every row is
#       verified by re-running at a second budget.
#
# Two arithmetic modes:
#   exact  -- BigInt cells; used for the validation window and the glue check.
#   float  -- Float64 cells; used for the growth series at large budgets
#             (relative error ~1e-13, irrelevant for S(R)^(1/R)).
#
# Output: artifacts/r82/dp_exact.json  (+ stdout log)

const T = 3          # trace of the cat map: lambda^2 = T*lambda - 1
const SQ5 = 5        # lambda = (T + sqrt(T^2-4))/2 = (3 + sqrt 5)/2

# ---------------------------------------------------------------- exact filter
# le_sqrt5(B, D)  <=>  B*sqrt(5) <= D          (B, D integers)
@inline function le_sqrt5(B::Int, D::Int)::Bool
    if B <= 0 && D >= 0
        return true
    elseif B > 0 && D < 0
        return false
    elseif B > 0            # both >= 0
        return SQ5 * Int128(B)^2 <= Int128(D)^2
    else                    # B <= 0, D < 0:  (-B)sqrt5 >= -D > 0
        return SQ5 * Int128(B)^2 >= Int128(D)^2
    end
end

# |a + b*lambda| <= rem, exactly
@inline function valok(a::Int, b::Int, rem::Int)::Bool
    rem < 0 && return false
    A = 2a + T * b
    B = b
    M = 2 * rem
    return le_sqrt5(B, M - A) && le_sqrt5(-B, A + M)
end

@inline trans(a::Int, b::Int, c::Int) = (-b, a - c + T * b)

# ------------------------------------------------------------------- the DP
# Counts accepting walks (relations) of the reversed-normalized tail automaton:
# start at sigma = 0, first letter c >= 1 (the sign is factored out), letters
# are integers, cost = sum |c|, accept when sigma returns to 0 on a nonzero
# letter.  Returns cnt[(w, R)] = number of walks of width w and cost R,
# for all w <= pmax, R <= rmax.
function count_dp(::Type{V}, rmax::Int; pmax::Int = rmax) where {V}
    dp = Dict{Tuple{Int,Int,Int},V}()
    for c in 1:rmax
        a2, b2 = trans(0, 0, c)
        valok(a2, b2, rmax - c) || continue
        k = (a2, b2, c)
        dp[k] = get(dp, k, zero(V)) + one(V)
    end
    cnt = Dict{Tuple{Int,Int},V}()
    for p in 1:pmax-1
        ndp = Dict{Tuple{Int,Int,Int},V}()
        w2 = p + 1
        for ((a, b, u), n) in dp
            # free letter 0: position advances, cost and width do not
            a2, b2 = trans(a, b, 0)
            if valok(a2, b2, rmax - u)
                k = (a2, b2, u)
                ndp[k] = get(ndp, k, zero(V)) + n
            end
            rem = rmax - u
            for c in -rem:rem
                c == 0 && continue
                u2 = u + abs(c)
                a2, b2 = trans(a, b, c)
                valok(a2, b2, rmax - u2) || continue
                if a2 == 0 && b2 == 0
                    key = (w2, u2)
                    cnt[key] = get(cnt, key, zero(V)) + n
                end
                k = (a2, b2, u2)
                ndp[k] = get(ndp, k, zero(V)) + n
            end
        end
        dp = ndp
        isempty(dp) && break
    end
    return cnt
end

# S_dense(R) = # relations of cost R and width <= R;  S_cap(R) = width <= cap
function series(cnt::Dict{Tuple{Int,Int},V}, rmax::Int; cap::Int = 0) where {V}
    dense = Dict{Int,V}()
    capped = Dict{Int,V}()
    for ((w, R), n) in cnt
        R > rmax && continue
        if w <= R
            dense[R] = get(dense, R, zero(V)) + n
        end
        if cap > 0 && w <= cap
            capped[R] = get(capped, R, zero(V)) + n
        end
    end
    return dense, capped
end

# window count S_win(R; K) = relations of cost R and width <= K
function windows(cnt::Dict{Tuple{Int,Int},V}, K::Int) where {V}
    out = Dict{Int,V}()
    for ((w, R), n) in cnt
        w <= K || continue
        out[R] = get(out, R, zero(V)) + n
    end
    return out
end

# ------------------------------------------------------------------ self-checks
function glue_check(S::Dict{Int,V}, rmax::Int; verbose::Bool = true) where {V}
    bad = Tuple{Int,Int,Float64}[]
    for R1 in 5:rmax, R2 in R1:rmax
        R1 + R2 <= rmax || continue
        n1 = get(S, R1, zero(V)); n2 = get(S, R2, zero(V)); n12 = get(S, R1 + R2, zero(V))
        (n1 == 0 || n2 == 0) && continue
        prod = Float64(n1) * Float64(n2)
        if Float64(n12) < prod * (1 - 1e-9)
            push!(bad, (R1, R2, prod / Float64(n12)))
        end
    end
    if verbose
        if isempty(bad)
            println("  GLUE CHECK: PASS (all pairs R1+R2 <= $rmax)")
        else
            println("  GLUE CHECK: *** FAIL *** ", length(bad), " violating pairs; worst: ",
                    sort(bad, by = x -> -x[3])[1])
        end
    end
    return isempty(bad)
end

jesc(x) = string('"', x, '"')
function jdict(d::Dict{Int,<:Any})
    "{" * join([jesc(string(k)) * ":" * jesc(string(d[k])) for k in sort(collect(keys(d)))], ",") * "}"
end

function main()
    println("RUN 82 -- exact self-checking relation-count DP (t = $T)")
    println(repeat("=", 70))

    # ---- 1. exact window counts, validation against Theorem H (R79/R80) ----
    println("\n[1] EXACT validation window: rmax = 20, K = 17 and K = 20")
    t0 = time()
    cnt20 = count_dp(BigInt, 20; pmax = 21)
    w17 = windows(cnt20, 17)
    w20 = windows(cnt20, 20)
    ref17 = Dict(5 => 30, 6 => 28, 7 => 26, 8 => 76, 9 => 200, 10 => 624,
                 11 => 1064, 12 => 1760, 13 => 3262, 14 => 7366, 15 => 13292)
    ref20 = Dict(5 => 36, 6 => 34, 7 => 32, 8 => 94)
    # the R79/R80 tables count both signs of the leading letter
    ok17 = all(2 * get(w17, R, BigInt(0)) == ref17[R] for R in sort(collect(keys(ref17))))
    ok20 = all(2 * get(w20, R, BigInt(0)) == ref20[R] for R in sort(collect(keys(ref20))))
    println("  S_win(R;17), R=5..15 (x2): ",
            [Int(2 * get(w17, R, BigInt(0))) for R in 5:15])
    println("  reference (R79/R80)      : ", [ref17[R] for R in 5:15])
    println("  K=17 match: ", ok17 ? "11/11 EXACT" : "*** MISMATCH ***")
    println("  S_win(R;20), R=5..8 (x2) : ",
            [Int(2 * get(w20, R, BigInt(0))) for R in 5:8], "  vs ",
            [ref20[R] for R in 5:8], "  ", ok20 ? "4/4 EXACT" : "*** MISMATCH ***")
    println("  ($(round(time()-t0, digits=1)) s)")

    # ---- 2. exact dense series + glue check at a moderate budget ----
    println("\n[2] EXACT dense series, rmax = 56 (BigInt) + supermultiplicativity")
    t0 = time()
    cnt56 = count_dp(BigInt, 56)
    d56, _ = series(cnt56, 56)
    println("  S_dense(R) for R = 5..56:")
    for R in 5:56
        print("   ", R, ":", get(d56, R, BigInt(0)))
        R % 4 == 0 && println()
    end
    println()
    g56 = glue_check(d56, 56)
    println("  S(R)^(1/R): ", [(R, round(Float64(get(d56, R, BigInt(1)))^(1 / R), digits = 5))
                               for R in (20, 30, 40, 48, 56)])
    println("  ($(round(time()-t0, digits=1)) s)")

    # ---- 3. budget-independence: rmax = 40 must reproduce rows R <= 40 ----
    println("\n[3] BUDGET INDEPENDENCE: rmax = 40 vs rmax = 56 on R <= 40")
    cnt40 = count_dp(BigInt, 40)
    d40, _ = series(cnt40, 40)
    same = all(get(d40, R, BigInt(0)) == get(d56, R, BigInt(0)) for R in 5:40)
    println("  rows R = 5..40 identical: ", same ? "YES (36/36)" : "*** NO ***")
    if !same
        for R in 5:40
            a = get(d40, R, BigInt(0)); b = get(d56, R, BigInt(0))
            a == b || println("    R=$R: rmax40=$a  rmax56=$b")
        end
    end

    # ---- 4. float series at a large budget, with the same self-checks ----
    println("\n[4] FLOAT dense series at rmax = 130 (self-checked)")
    t0 = time()
    cntF = count_dp(Float64, 130)
    dF, _ = series(cntF, 130)
    relerr = maximum(abs(Float64(get(d56, R, BigInt(0))) - get(dF, R, 0.0)) /
                     Float64(get(d56, R, BigInt(1))) for R in 5:56)
    println("  max relative deviation vs the exact rows R <= 56: ", relerr)
    gF = glue_check(dF, 130)
    println("  S(R)^(1/R): ", [(R, round(get(dF, R, 1.0)^(1 / R), digits = 5))
                               for R in (60, 70, 80, 90, 100, 110, 120, 130)])
    println("  ($(round(time()-t0, digits=1)) s)")

    open(joinpath(dirname(dirname(abspath(@__FILE__))), "artifacts", "r82", "dp_exact.json"), "w") do io
        println(io, "{")
        println(io, "  \"meta\": {\"script\": \"src/r82_dp_exact.jl\", \"julia\": ", jesc(string(VERSION)),
                    ", \"date\": \"2026-08-30\", \"t\": ", T, "},")
        println(io, "  \"validation_S_win_K17\": ", ok17, ",")
        println(io, "  \"validation_S_win_K20\": ", ok20, ",")
        println(io, "  \"glue_exact_56\": ", g56, ",")
        println(io, "  \"budget_independent_40_vs_56\": ", same, ",")
        println(io, "  \"glue_float_130\": ", gF, ",")
        println(io, "  \"float_vs_exact_relerr\": ", relerr, ",")
        println(io, "  \"S_dense_exact\": ", jdict(d56), ",")
        println(io, "  \"S_dense_float\": ", jdict(dF))
        println(io, "}")
    end
    println("\nartifact written: artifacts/r82/dp_exact.json")
end

main()
