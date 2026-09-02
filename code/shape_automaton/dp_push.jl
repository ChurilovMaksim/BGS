# RUN 82b (Julia): push the validated relation-count DP to large budgets.
#
# Same automaton, same exact integer co-reachability filter and the same
# built-in supermultiplicativity self-check as src/r82_dp_exact.jl (which
# reproduced the R80.2 position-DP rows 3/8/37/68/111 at L1 = 8..12, w <= 17
# and the R80.4 dense rows S(30) = 301160711, S(50) = 7.6399e15,
# S(80)^(1/80) = 2.17936).  Purpose here: the best rigorous LOWER bound on
#
#     C_dense = lim N(R)^(1/R) = sup_R N(R)^(1/R)     (R81.1, Fekete)
#
# which requires ONE exactly computed row at the largest affordable R.
#
# Usage: julia src/r82b_dp_push.jl [rmax_exact] [rmax_float]
# Output: artifacts/r82/dp_push.json (+ log)

include(joinpath(@__DIR__, "r82_dp_lib.jl"))

function report(S::Dict{Int,V}, rmax::Int, label::String) where {V}
    println("[$label] rmax = $rmax")
    ok = glue_check(S, rmax)
    best = (0, 0.0)
    for R in sort(collect(keys(S)))
        R < 10 && continue
        g = Float64(S[R])^(1 / R)
        g > best[2] && (best = (R, g))
    end
    for R in filter(r -> r % 20 == 0 || r == rmax, sort(collect(keys(S))))
        println("  S($R) = ", S[R], "   ^(1/R) = ", round(Float64(S[R])^(1 / R), digits = 6))
    end
    println("  sup_R S(R)^(1/R) attained at R = ", best[1], ": ", round(best[2], digits = 6))
    return ok, best
end

function dump_json(dE, dF, rmaxE, rmaxF, okE, okF, relerr, bestE, bestF)
    open(joinpath(dirname(@__DIR__), "artifacts", "r82", "dp_push.json"), "w") do io
        println(io, "{")
        println(io, "  \"meta\": {\"script\": \"src/r82b_dp_push.jl\", \"julia\": \"", VERSION,
                    "\", \"date\": \"2026-08-30\"},")
        println(io, "  \"rmax_exact\": ", rmaxE, ", \"rmax_float\": ", rmaxF, ",")
        println(io, "  \"glue_exact\": ", okE, ", \"glue_float\": ", okF, ",")
        println(io, "  \"float_vs_exact_relerr\": ", relerr, ",")
        println(io, "  \"sup_exact_R\": ", bestE[1], ", \"sup_exact_value\": ", bestE[2], ",")
        println(io, "  \"sup_float_R\": ", bestF[1], ", \"sup_float_value\": ", bestF[2], ",")
        println(io, "  \"S_dense_exact\": ", jdict(dE), ",")
        println(io, "  \"S_dense_float\": ", jdict(dF))
        println(io, "}")
    end
end

function main()
    rmaxE = length(ARGS) >= 1 ? parse(Int, ARGS[1]) : 140
    rmaxF = length(ARGS) >= 2 ? parse(Int, ARGS[2]) : 240
    println("RUN 82b -- DP push (exact rmax = $rmaxE, float rmax = $rmaxF)")
    println(repeat("=", 70))

    t0 = time()
    cntE = count_dp(BigInt, rmaxE)
    dE, _ = series(cntE, rmaxE)
    okE, bestE = report(dE, rmaxE, "EXACT BigInt")
    println("  ($(round(time()-t0, digits=1)) s)")
    # dump immediately: a killed float stage must not lose the exact series
    dump_json(dE, Dict{Int,Float64}(), rmaxE, 0, okE, false, NaN, bestE, (0, 0.0))
    println("  artifact written (exact stage)")
    flush(stdout)

    t0 = time()
    cntF = count_dp(Float64, rmaxF)
    dF, _ = series(cntF, rmaxF)
    relerr = maximum(abs(Float64(dE[R]) - dF[R]) / Float64(dE[R])
                     for R in 10:rmaxE if haskey(dE, R) && haskey(dF, R))
    println("[FLOAT] max relative deviation vs the exact rows: ", relerr)
    okF, bestF = report(dF, rmaxF, "FLOAT")
    println("  ($(round(time()-t0, digits=1)) s)")

    dump_json(dE, dF, rmaxE, rmaxF, okE, okF, relerr, bestE, bestF)
    println("\nartifact written: artifacts/r82/dp_push.json")
end

main()
