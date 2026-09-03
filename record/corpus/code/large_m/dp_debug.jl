# Run 81-debug: WHERE does the large-budget count DP break?
# The supermultiplicativity check N(R1+R2) >= N(R1)*N(R2) fails on the
# r80/r81 count DP at R ~ 122-124 (e.g. N(124) = 1.09e40 < N(62)^2 = 5.0e40).
# Fekete forbids this for the TRUE counts, so the DP has a bug that
# activates at large budgets.  Bisect it:
#   (a) restricted alphabet |c| <= cmax: glue-check n(124) >= n(62)^2
#       per cmax = 1, 2, 3, ...  -> locates whether large digits or the
#       core bookkeeping is at fault;
#   (b) float-slack sensitivity: slack 1e-9 vs 1e-6 vs exact-rational
#       bound check at rmax = 124;
#   (c) the u/w cell census at the two budgets.

function valok(a::Int, b::Int, rem::Float64; slack::Float64 = 1e-9)
    return abs(a + b * ((3 + sqrt(5.0)) / 2)) <= rem * (1 + 1e-12) + slack
end

trans(a::Int, b::Int, c::Int) = (-b, a - c + 3b)

function count_dp(rmax::Int, wmax::Int; cmax::Int = 10^9,
                  slack::Float64 = 1e-9)
    dp = Dict{Tuple{Int,Int,Int,Int},BigInt}()
    for c in 1:min(rmax, cmax)
        a2, b2 = trans(0, 0, c)
        valok(a2, b2, Float64(rmax - c); slack = slack) || continue
        k = (a2, b2, c, 1)
        dp[k] = get(dp, k, BigInt(0)) + 1
    end
    cnt = Dict{Tuple{Int,Int},BigInt}()
    for p in 1:wmax-1
        ndp = Dict{Tuple{Int,Int,Int,Int},BigInt}()
        w2 = p + 1
        for ((a, b, u, w), n) in dp
            a2, b2 = trans(a, b, 0)
            if valok(a2, b2, Float64(rmax - u); slack = slack)
                k = (a2, b2, u, w)
                ndp[k] = get(ndp, k, BigInt(0)) + n
            end
            rem = min(rmax - u, cmax)
            for c in -rem:rem
                c == 0 && continue
                u2 = u + abs(c)
                a2, b2 = trans(a, b, c)
                valok(a2, b2, Float64(rmax - u2); slack = slack) || continue
                if (a2, b2) == (0, 0)
                    key = (w2, u2)
                    cnt[key] = get(cnt, key, BigInt(0)) + n
                end
                k = (a2, b2, u2, w2)
                ndp[k] = get(ndp, k, BigInt(0)) + n
            end
        end
        dp = ndp
        isempty(dp) && break
    end
    S = Dict{Int,BigInt}()
    for ((w, R), n) in cnt
        S[R] = get(S, R, BigInt(0)) + n
    end
    return S, length(dp)
end

function main()
    for cmax in (2, 1000)
        t0 = time()
        S62, _ = count_dp(62, 63; cmax = cmax)
        println("cmax=$cmax: n(62)=$(get(S62, 62, BigInt(0)))  ($(round(time()-t0,digits=1)) s)")
        flush(stdout)
        t0 = time()
        S124, _ = count_dp(124, 125; cmax = cmax)
        n62 = get(S62, 62, BigInt(0))
        n124 = get(S124, 124, BigInt(0))
        ok = n124 >= n62 * n62
        println("cmax=$cmax: n(124)=$n124  glue ok: $ok  "
                * (ok ? "" : "(deficit $(Float64(n62^2 / n124))x)"))
        println("   S124 at R=100: $(get(S124, 100, BigInt(0)))  R=110: $(get(S124, 110, BigInt(0)))  R=118: $(get(S124, 118, BigInt(0)))")
        flush(stdout)
    end
end

main()
