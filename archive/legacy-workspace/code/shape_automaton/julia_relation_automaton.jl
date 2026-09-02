# Run 79: the REVERSED-NORMALIZED relation automaton for x^2 - 3x + 1 (Julia).
# ==========================================================================
# Formulation (R79): a relation sum_j c_j lambda^j = 0, read from the TOP
# (c'_i = c_{D-i}), has the normalized tail state
#     sigma_i = sum_{j>=i} c'_j lambda'^{j-i}  in  Z[lambda],
# with the transition  sigma_{i+1} = lambda (sigma_i - c'_i)  and the a-priori
# bound  |sigma_i| <= phi * (remaining L1 budget),  phi = 1/(1-lambda') = the
# golden ratio, because lambda' < 1.  Start sigma_0 = 0; accept sigma = 0 after
# the last nonzero digit.  Each accepting path with sum |c'| = R and first/last
# digits nonzero is EXACTLY one shape (support-normalised multiple of m_t).
#
# This script:
#   1. BFS the reachable states under the budget bound (finiteness test);
#   2. if finite: DP over (state, degree) for the shape counts S_win(R,K)
#      (paths that stay within a window of K digit positions, gaps allowed);
#   3. validate against the exact census numbers
#      X^Z_6(17)=5040, X^Z_8(17)=4454240, X^Z_10(17)=3107822760,
#      X^Z_12(17)=2093152388976  (linear-placement part of Theorem H).
#
# Coordinates: sigma = a + b*lambda, lambda^2 = 3 lambda - 1.
# lambda(sigma - c):  sigma - c = (a - c) + b lambda;
#   lambda((a-c) + b lambda) = (a-c) lambda + b lambda^2
#                            = (a-c) lambda + b(3 lambda - 1)
#                            = -b + (a - c + 3b) lambda.
# So the transition is  (a, b) --c--> (-b, a - c + 3b),  cost |c|.

const T = 3
const LAM = (3 + sqrt(5.0)) / 2      # 2.618...
const LAMP = 1 / LAM                 # 0.382
const PHI = 1 / (1 - LAMP)           # 1.618...

struct St
    a::Int
    b::Int
end
val(s::St) = s.a + s.b * LAM
trans(s::St, c::Int) = St(-s.b, s.a - c + T * s.b)

function main(rmax::Int)
    t0 = time()
    println("R79 reversed-normalized automaton, rmax = $rmax")
    # BFS over (state, minimal-used): a state is admissible at used u if
    # |sigma| <= phi * (rmax - u).  Track the minimal u per state.
    best = Dict{St,Int}(St(0, 0) => 0)
    frontier = [St(0, 0)]
    # NOTE: the first digit must be nonzero, and the empty walk sits at (0,0).
    maxstates = 2_000_000
    layer = 0
    while !isempty(frontier)
        layer += 1
        newfront = St[]
        for s in frontier
            u0 = best[s]
            for c in -rmax:rmax
                c == 0 && s == St(0, 0) && continue   # no leading zeros
                u = u0 + abs(c)
                u > rmax && continue
                s2 = trans(s, c)
                abs(val(s2)) > PHI * (rmax - u) && continue
                if !haskey(best, s2) || best[s2] > u
                    best[s2] = u
                    push!(newfront, s2)
                end
            end
        end
        unique!(newfront)
        frontier = newfront
        if length(best) > maxstates
            println("STATE EXPLOSION at layer $layer: $(length(best)) states")
            return nothing
        end
    end
    println("  reachable states: $(length(best))  ($(round(time()-t0, digits=1)) s)")
    return best
end

# DP: count accepting paths by (state, used, position-in-window) with
# polynomial (degree) weights collapsed to L1-degree first: S_win(R, K) =
# number of shapes with L1 = R and width <= K (gaps included).
function shape_counts(best::Dict{St,Int}, rmax::Int, Kmax::Int)
    # dp[(s, u)] = set of degree-counts? -> too big; instead track counts per
    # (state, used, degree) with degree = L1 used so far; used == degree here
    # because every nonzero digit costs its |c| and zeros cost nothing but
    # consume a window position.  So track (state, used, pos).
    # dp[state][used][pos] — sparse dictionaries per (used, pos).
    t0 = time()
    # dp: Dict{St, Dict{Tuple{Int,Int},Int}}  state -> (used,pos) -> count
    dp = Dict{St,Dict{Tuple{Int,Int},Int}}()
    dp[St(0, 0)] = Dict{Tuple{Int,Int},Int}((0, 0) => 1)
    for pos in 0:Kmax-1
        ndp = Dict{St,Dict{Tuple{Int,Int},Int}}()
        for (s, tbl) in dp, ((u, p), cnt) in tbl
            p == pos || continue
            for c in -rmax:rmax
                c == 0 && s == St(0, 0) && continue
                u2 = u + abs(c)
                u2 > rmax && continue
                s2 = trans(s, c)
                abs(val(s2)) > PHI * (rmax - u2) && continue
                tbl2 = get!(ndp, s2) do; Dict{Tuple{Int,Int},Int}(); end
                tbl2[(u2, pos + 1)] = get(tbl2, (u2, pos + 1), 0) + cnt
            end
            # zero digit (gap): allowed at any state except staying is fine
            if !(s == St(0, 0)) || true
                s2 = trans(s, 0)
                abs(val(s2)) > PHI * (rmax - u) && continue
                tbl2 = get!(ndp, s2) do; Dict{Tuple{Int,Int},Int}(); end
                tbl2[(u, pos + 1)] = get(tbl2, (u, pos + 1), 0) + cnt
            end
        end
        dp = ndp
    end
    # accept: state (0,0), last digit nonzero — handled by excluding the
    # zero-digit transition INTO (0,0): trans(s,0) = (0,0) requires
    # -b = 0 and a + 3b = 0 => s = (0,0): the zero-digit self-loop at (0,0)
    # was excluded only at the start; mid-walk the (0,0)->(0,0) zero step
    # must also be excluded (it would be a trailing/leading zero pair).
    total = Dict{Int,Int}()
    for (s, tbl) in dp, ((u, p), cnt) in tbl
        s == St(0, 0) || continue
        total[u] = get(total, u, 0) + cnt
    end
    println("  DP done ($(round(time()-t0, digits=1)) s)")
    return total
end

# The zero-digit transition into (0,0) from (0,0) is the only self-loop; the
# DP above must exclude it globally (leading-zero strip).  We enforce this by
# construction: trans((0,0),0) = (0,0); in the loop the branch runs for all s,
# including (0,0) — fix by skipping it there.
function shape_counts_fixed(best::Dict{St,Int}, rmax::Int, Kmax::Int)
    # DP over (sigma, started) with (used, pos) keys.
    # leading zeros: excluded until started; trailing zeros: allowed.
    t0 = time()
    # dp[(u, pos)][(sigma, started)] = count
    dp = Dict{Tuple{Int,Int},Dict{Tuple{St,Bool},Int}}()
    dp[(0, 0)] = Dict{Tuple{St,Bool},Int}((St(0, 0), false) => 1)
    for pos in 0:Kmax-1
        ndp = Dict{Tuple{Int,Int},Dict{Tuple{St,Bool},Int}}()
        for ((u, p), tbl) in dp
            p == pos || continue
            for ((s, started), cnt) in tbl
                # zero digit
                if !started
                    # leading gap: state stays (0,0), not started
                    get!(ndp, (u, pos + 1)) do; Dict{Tuple{St,Bool},Int}(); end
                    k = (St(0, 0), false)
                    ndp[(u, pos + 1)][k] = get(ndp[(u, pos + 1)], k, 0) + cnt
                else
                    s2 = trans(s, 0)
                    abs(val(s2)) > PHI * (rmax - u) && continue
                    get!(ndp, (u, pos + 1)) do; Dict{Tuple{St,Bool},Int}(); end
                    k = (s2, true)
                    ndp[(u, pos + 1)][k] = get(ndp[(u, pos + 1)], k, 0) + cnt
                end
                # nonzero digits
                for c in -rmax:rmax
                    c == 0 && continue
                    u2 = u + abs(c)
                    u2 > rmax && continue
                    s2 = trans(s, c)
                    abs(val(s2)) > PHI * (rmax - u2) && continue
                    get!(ndp, (u2, pos + 1)) do; Dict{Tuple{St,Bool},Int}(); end
                    k = (s2, true)
                    ndp[(u2, pos + 1)][k] = get(ndp[(u2, pos + 1)], k, 0) + cnt
                end
            end
        end
        dp = ndp
    end
    total = Dict{Int,Int}()
    for ((u, p), tbl) in dp, ((s, started), cnt) in tbl
        (s == St(0, 0) && started) || continue
        total[u] = get(total, u, 0) + cnt
    end
    println("  DP done ($(round(time()-t0, digits=1)) s)")
    return total
end

function main2(rmax::Int, Kmax::Int)
    t0 = time()
    println("R79 shape counts, rmax=$rmax, Kmax=$Kmax")
    best = main(rmax)
    best === nothing && return
    total = shape_counts_fixed(best, rmax, Kmax)
    ks = sort(collect(keys(total)))
    println("  S_win(R; K=$Kmax): ", [(r, total[r]) for r in ks if total[r] > 0])
    println("  ($(round(time()-t0, digits=1)) s total)")
    return total
end
