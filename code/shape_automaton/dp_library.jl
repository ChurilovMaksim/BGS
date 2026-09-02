# RUN 82: shared library for the relation-count DP of m_t(x) = x^2 - t x + 1.
# ==========================================================================
# Canonical implementation (research_code_standards: one copy, imported).
#
# The reversed-normalized tail automaton (THEORY 16, R79): a relation
# sum_j c_j lambda^j = 0 read top-down carries the state
#   sigma_i = sum_{j >= i} c'_j lambda'^(j-i)  in  Z[lambda],
#   sigma_{i+1} = lambda (sigma_i - c'_i),
# with the co-reachability bound |sigma_i| <= (remaining L1) because
# |sigma_i| <= sum_{j>=i} |c'_j| lambda'^(j-i) <= sum_{j>=i} |c'_j|.
# In coordinates sigma = a + b*lambda (lambda^2 = t*lambda - 1):
#   (a, b) --c--> (-b, a - c + t*b).
#
# Two corrections to the r80/r81 implementations:
#  * the DP key is (a, b, u) -- the old (a, b, u, w) carried a width field
#    that is never read (the accepting record uses the current position
#    p + 1), inflating the cell count by O(R) and causing the large-budget
#    memory exhaustion;
#  * the co-reachability test is EXACT integer arithmetic instead of a
#    Float64 comparison with an ad-hoc slack.

const T_TRACE = 3
const DISC = T_TRACE * T_TRACE - 4       # = 5;  lambda = (t + sqrt DISC)/2

# le_sqrt(B, D)  <=>  B*sqrt(DISC) <= D    for integers B, D
@inline function le_sqrt(B::Int, D::Int)::Bool
    if B <= 0 && D >= 0
        return true
    elseif B > 0 && D < 0
        return false
    elseif B > 0
        return DISC * Int128(B)^2 <= Int128(D)^2
    else
        return DISC * Int128(B)^2 >= Int128(D)^2
    end
end

# |a + b*lambda| <= rem, exactly:  a + b*lambda = ((2a + t b) + b sqrt(DISC))/2
@inline function valok(a::Int, b::Int, rem::Int)::Bool
    rem < 0 && return false
    A = 2a + T_TRACE * b
    M = 2 * rem
    return le_sqrt(b, M - A) && le_sqrt(-b, A + M)
end

@inline trans(a::Int, b::Int, c::Int) = (-b, a - c + T_TRACE * b)

"""
    count_dp(V, rmax; pmax = rmax)

Accepting walks of the automaton (relations), counted in the value type `V`
(`BigInt` for exact, `Float64` for large budgets).  The first letter is taken
positive (the global sign is factored out; the R79/R80 tables carry the
factor 2).  Returns `cnt[(w, R)]`: walks of width `w` and l1 cost `R`.
"""
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
            a2, b2 = trans(a, b, 0)          # free letter 0
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

"""Dense series S(R) = #{relations of cost R, width <= R} and, optionally, a
width-capped series."""
function series(cnt::Dict{Tuple{Int,Int},V}, rmax::Int; cap::Int = 0) where {V}
    dense = Dict{Int,V}()
    capped = Dict{Int,V}()
    for ((w, R), n) in cnt
        R > rmax && continue
        w <= R && (dense[R] = get(dense, R, zero(V)) + n)
        cap > 0 && w <= cap && (capped[R] = get(capped, R, zero(V)) + n)
    end
    return dense, capped
end

"""Window counts: relations of cost R with width <= K."""
function windows(cnt::Dict{Tuple{Int,Int},V}, K::Int) where {V}
    out = Dict{Int,V}()
    for ((w, R), n) in cnt
        w <= K || continue
        out[R] = get(out, R, zero(V)) + n
    end
    return out
end

"""LESSON 81-C: the supermultiplicativity N(R1+R2) >= N(R1) N(R2) is proven
(R81.1) for the true counts, so it is a mandatory self-check of any count DP.
Both factors and the product are read from the SAME run, so no width-cap or
budget mismatch can fake a violation."""
function glue_check(S::Dict{Int,V}, rmax::Int; verbose::Bool = true) where {V}
    bad = Tuple{Int,Int,Float64}[]
    for R1 in 5:rmax, R2 in R1:rmax
        R1 + R2 <= rmax || continue
        n1 = get(S, R1, zero(V)); n2 = get(S, R2, zero(V))
        n12 = get(S, R1 + R2, zero(V))
        (n1 == 0 || n2 == 0) && continue
        prod = Float64(n1) * Float64(n2)
        Float64(n12) < prod * (1 - 1e-9) && push!(bad, (R1, R2, prod / Float64(n12)))
    end
    if verbose
        if isempty(bad)
            println("  GLUE CHECK: PASS (all pairs R1 + R2 <= $rmax)")
        else
            println("  GLUE CHECK: *** FAIL *** ", length(bad),
                    " violating pairs; worst: ", sort(bad, by = x -> -x[3])[1])
        end
    end
    return isempty(bad)
end

jesc(x) = string('"', x, '"')
jdict(d::Dict{Int,<:Any}) =
    "{" * join([jesc(string(k)) * ":" * jesc(string(d[k]))
                for k in sort(collect(keys(d)))], ",") * "}"
