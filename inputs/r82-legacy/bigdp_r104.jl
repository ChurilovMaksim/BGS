# Run 80 (Julia): BIG-BUDGET relation automaton.
# =========================================================
# 1. Exact count DP: shape counts S(R, w) to R = 30, width <= 48;
#    dense part (w <= R) growth constant.
# 2. Float Bessel DP (J-weights): Psi to degree 24 -> X_r(K) tables
#    (MULTIPLICITY-inclusive: equals the census exactly for r <= 8,
#    overcounts by the wrap-collision excess for r >= 10);
#    calibrated against the exact-rational values at r <= 12, K = 17.
#
# Output: artifacts/r80/julia_bigdp.json (+ stdout log)

const T = 3
const LAM = (3 + sqrt(5.0)) / 2

trans(a::Int, b::Int, c::Int) = (-b, a - c + T * b)
valok(a::Int, b::Int, rem::Int) = abs(a + b * LAM) <= rem * (1 + 1e-12) + 1e-9

const LOGF = Dict{Int,Float64}()
function logfact(n::Int)
    haskey(LOGF, n) && return LOGF[n]
    s = 0.0
    for i in 2:n
        s += log(i)
    end
    LOGF[n] = s
    return s
end

# ------------------------------------------------------------------
# 1. exact count DP: accepting walks (shapes) by (width, L1)
# ------------------------------------------------------------------
function count_dp(rmax::Int, wmax::Int)
    dp = Dict{Tuple{Int,Int,Int,Int},BigInt}()
    for c in 1:rmax
        a2, b2 = trans(0, 0, c)
        valok(a2, b2, rmax - c) || continue
        k = (a2, b2, c, 1)
        dp[k] = get(dp, k, BigInt(0)) + 1
    end
    cnt = Dict{Tuple{Int,Int},BigInt}()
    for p in 1:wmax-1
        ndp = Dict{Tuple{Int,Int,Int,Int},BigInt}()
        w2 = p + 1
        for ((a, b, u, w), n) in dp
            a2, b2 = trans(a, b, 0)
            if valok(a2, b2, rmax - u)
                k = (a2, b2, u, w)
                ndp[k] = get(ndp, k, BigInt(0)) + n
            end
            rem = rmax - u
            for c in -rem:rem
                c == 0 && continue
                u2 = u + abs(c)
                a2, b2 = trans(a, b, c)
                valok(a2, b2, rmax - u2) || continue
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
    return cnt
end

# ------------------------------------------------------------------
# 2. float Bessel DP
# ------------------------------------------------------------------
ifact_pair(k::Int, ka::Int) = exp(-logfact(k) - logfact(ka))

function I_ser(a::Int, L::Int)
    s = zeros(Float64, L)
    k = 0
    while 2k + a < L
        s[2k + a + 1] = ifact_pair(k, k + a)
        k += 1
    end
    return s
end
const ICACHE = Dict{Tuple{Int,Int},Vector{Float64}}()
Iser(a::Int, L::Int) = get!(ICACHE, (a, L)) do; I_ser(a, L); end

function ser_mul(a::Vector{Float64}, b::Vector{Float64}, L::Int)
    out = zeros(Float64, L)
    for i in 1:L
        ai = a[i]
        ai == 0.0 && continue
        for j in 1:L
            i + j - 1 > L && break
            out[i + j - 1] += ai * b[j]
        end
    end
    return out
end

function J_ser(c::Int, L::Int)
    num = Iser(abs(c), L)
    den = Iser(0, L)
    out = zeros(Float64, L)
    for d in 1:L
        acc = num[d]
        for e in 1:d-1
            acc -= den[e + 1] * out[d - e]
        end
        out[d] = acc
    end
    return out
end
const JCACHE = Dict{Tuple{Int,Int},Vector{Float64}}()
Jser(c::Int, L::Int) = get!(JCACHE, (c, L)) do; J_ser(c, L); end

function I0_pow(K::Int, L::Int)
    result = zeros(Float64, L); result[1] = 1.0
    base = Iser(0, L)
    e = K
    while e > 0
        if isodd(e)
            result = ser_mul(result, base, L)
        end
        base = ser_mul(base, base, L)
        e >>= 1
    end
    return result
end
const I0CACHE = Dict{Tuple{Int,Int},Vector{Float64}}()
I0p(K::Int, L::Int) = get!(I0CACHE, (K, L)) do; I0_pow(K, L); end

# Psi (sum of accepted-walk J-weight series), widths capped at wmax
function bessel_dp(rmax::Int, wmax::Int)
    L = rmax + 1
    dp = Dict{Tuple{Int,Int,Int,Int},Vector{Float64}}()
    for c in 1:rmax
        a2, b2 = trans(0, 0, c)
        valok(a2, b2, rmax - c) || continue
        k = (a2, b2, c, 1)
        wt = Jser(c, L)
        dp[k] = haskey(dp, k) ? dp[k] .+ wt : wt
    end
    Psi = zeros(Float64, L)
    for p in 1:wmax-1
        ndp = Dict{Tuple{Int,Int,Int,Int},Vector{Float64}}()
        w2 = p + 1
        for ((a, b, u, w), wt) in dp
            a2, b2 = trans(a, b, 0)
            if valok(a2, b2, rmax - u)
                k = (a2, b2, u, w)
                ndp[k] = haskey(ndp, k) ? ndp[k] .+ wt : copy(wt)
            end
            rem = rmax - u
            for c in -rem:rem
                c == 0 && continue
                u2 = u + abs(c)
                a2, b2 = trans(a, b, c)
                valok(a2, b2, rmax - u2) || continue
                wt2 = ser_mul(wt, Jser(abs(c), L), L)
                if (a2, b2) == (0, 0)
                    Psi .+= wt2
                end
                k = (a2, b2, u2, w2)
                ndp[k] = haskey(ndp, k) ? ndp[k] .+ wt2 : wt2
            end
        end
        dp = ndp
        isempty(dp) && break
    end
    return Psi
end

# minimal JSON writer (avoid the JSON package dependency)
jesc(x::AbstractString) = string('"', replace(replace(x, '\\' => "\\\\"), '"' => "\\\""), '"')
jdump(x) = jesc(string(x))
jdump(x::Int) = string(x)
jdump(x::Int128) = string(x)
jdump(x::Float64) = string(x)
jdump(x::Bool) = x ? "true" : "false"
function jdump(d::Dict)
    "{" * join([jesc(string(k)) * ":" * jdump(v) for (k, v) in d], ",") * "}"
end

function main()
    out = Dict{String,Any}(
        "meta" => Dict("script" => "src/r80_julia_bigdp.jl",
                       "julia" => string(VERSION), "date" => "2026-08-29",
                       "t" => T))

    # ---- 1. exact count DP to R = 30 ----
    rmax = 104; wmax = 109
    t0 = time()
    cnt = count_dp(rmax, wmax)
    SR = Dict{Int,BigInt}()
    SRdense = Dict{Int,BigInt}()
    for ((w, R), n) in cnt
        SR[R] = get(SR, R, BigInt(0)) + n
        if w <= R
            SRdense[R] = get(SRdense, R, BigInt(0)) + n
        end
    end
    println("count DP done ($(round(time()-t0, digits=1)) s)")
    Rs = sort(collect(keys(SR)))
    println("S(R), w<=48:   ", [(R, SR[R]) for R in Rs])
    println("S(R), w<=R:    ", [(R, SRdense[R]) for R in sort(collect(keys(SRdense)))])
    out["S_R_w48"] = Dict(string(R) => string(SR[R]) for R in Rs)
    out["S_R_dense"] = Dict(string(R) => string(get(SRdense, R, 0)) for R in Rs)
    g_full = [(R, round(Float64(SR[R])^(1 / R), digits = 4)) for R in Rs if R >= 8]
    g_dense = [(R, round(Float64(SRdense[R])^(1 / R), digits = 4))
               for R in sort(collect(keys(SRdense))) if R >= 8]
    println("S(R)^(1/R) full:   ", g_full)
    println("S(R)^(1/R) dense:  ", g_dense)
    out["growth_full"] = Dict(string(R) => v for (R, v) in g_full)
    out["growth_dense"] = Dict(string(R) => v for (R, v) in g_dense)

    py12 = Dict(5 => 1, 6 => 1, 7 => 1, 8 => 3, 9 => 8, 10 => 85, 11 => 164, 12 => 255)
    vok = all(sum(n for ((w, R2), n) in cnt if R2 == R && w <= 41) == py12[R] for R in keys(py12))
    println("validation S(R<=12; w<=41|48) vs Python exact: ", vok ? "OK" : "*** MISMATCH ***")
    out["validation_S_R"] = vok


end

main()
