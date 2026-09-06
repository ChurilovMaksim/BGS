# AUDIT CROSS-CHECK (Julia key) - BGS resonance counters
# Independent second-language verification of:
#   V1 matched identity  sol+-+- = 2k^2-k (odd k) / 3k(k-1) (even k)
#   V2 zero counts       Z2=p-1, Z3=(p-1)(p-2)
#   V4 tail-bound spot checks on a fresh grid

function prime_factors(n::Int)
    d = 2; fs = Int[]
    while d * d <= n
        while n % d == 0
            push!(fs, d); n = n ÷ d
        end
        d += 1
    end
    n > 1 && push!(fs, n)
    return unique(fs)
end

function subgroup(p::Int, k::Int)
    g = 2
    fs = prime_factors(p - 1)
    while any(powermod(g, (p - 1) ÷ q, p) == 1 for q in fs)
        g += 1
    end
    a = powermod(g, (p - 1) ÷ k, p)
    H = Int[]; x = 1
    for _ in 1:k
        push!(H, x); x = x * a % p
    end
    @assert length(H) == k
    return H
end

"""sol+-+- by (sum,invsum) hashing, labels all 1, signs (+,-,+,-)."""
function sol4_hash(p::Int, H::Vector{Int})
    invH = Dict(h => powermod(h, p - 2, p) for h in H)
    pair = Dict{Tuple{Int,Int},Int}()
    for h1 in H, h3 in H
        key = (mod(h1 + h3, p), mod(invH[h1] + invH[h3], p))
        pair[key] = get(pair, key, 0) + 1
    end
    cnt = 0
    for h2 in H, h4 in H
        key = (mod(h2 + h4, p), mod(invH[h2] + invH[h4], p))
        cnt += get(pair, key, 0)
    end
    return cnt
end

function sol4_brute(p::Int, H::Vector{Int})
    invH = Dict(h => powermod(h, p - 2, p) for h in H)
    cnt = 0
    for h1 in H, h2 in H, h3 in H, h4 in H
        if mod(h1 - h2 + h3 - h4, p) == 0 &&
           mod(invH[h1] - invH[h2] + invH[h3] - invH[h4], p) == 0
            cnt += 1
        end
    end
    return cnt
end

function n3_count(p::Int, H::Vector{Int}, a::Vector{Int}, b::Vector{Int})
    invH = Dict(h => powermod(h, p - 2, p) for h in H)
    ia4 = powermod(a[4], p - 2, p)
    right = Set{Tuple{Int,Int}}()
    for u2 in H, u3 in H
        push!(right, (u2, u3))
    end
    rightset = Set(right)
    cnt = 0
    for u2 in H, u3 in H
        num = mod(a[1] - a[2] * u2 + a[3] * u3, p)
        u4 = num * ia4 % p
        (u4 in rightset) === false && continue
        # membership check via dictionary of H:
        haskey(invH, u4) || continue
        lhs = mod(b[1] - b[2] * invH[u2] + b[3] * invH[u3], p)
        rhs = b[4] * invH[u4] % p
        if lhs == rhs
            cnt += 1
        end
    end
    return cnt
end

generic_ok(p, a, b) =
    (a[1]*b[3] - a[3]*b[1]) % p != 0 &&
    (a[2]*b[4] - a[4]*b[2]) % p != 0 &&
    (a[1]*b[2] - a[2]*b[1]) % p != 0 &&
    (a[1]*b[4] - a[4]*b[1]) % p != 0 &&
    (a[2]*b[3] - a[3]*b[2]) % p != 0 &&
    (a[3]*b[4] - a[4]*b[3]) % p != 0

function main()
    println("=== JULIA CROSS-CHECK (independent key) ===")
    fails = 0

    # ---- V1 matched identity ----
    checked = 0
    for (p, kmax) in [(101, 25), (211, 30), (401, 40), (601, 50)]
        ks = [d for d in 2:min(kmax, p - 2) if (p - 1) % d == 0]
        for k in ks
            H = subgroup(p, k)
            fast = sol4_hash(p, H)
            pred = iseven(k) ? 3k * (k - 1) : 2k * k - k
            global fails
            if fast != pred
                global fails += 1
                println("V1 FAIL p=$p k=$k got=$fast want=$pred")
            end
            checked += 1
        end
    end
    println("V1 matched identity: $checked configs, fails=$fails")

    # ---- V2 zero counts Z2, Z3 ----
    zfails = 0
    for p in [101, 211, 401]
        brute2 = sum(1 for x in 1:p-1 for y in 1:p-1 if (x + y) % p == 0)
        brute3 = sum(1 for x in 1:p-1 for y in 1:p-1 for z in 1:p-1
                     if (x + y + z) % p == 0)
        w2 = p - 1
        w3 = (p - 1) * (p - 2)
        okk = brute2 == w2 && brute3 == w3
        okk || (zfails += 1)
        println("V2 p=$p: Z2 $brute2/$w2  Z3 $brute3/$w3  $(okk ? "OK" : "FAIL")")
    end

    # ---- V4 tail bound spot checks ----
    tfails = 0
    tchecked = 0
    maxn3 = 0
    rngseed = 20260826
    state = rngseed
    myrand(p) = (state = mod(state * 48271, 2147483647); 1 + state % (p - 1))
    for p in [353, 719, 1447]
        ks = [d for d in 3:p-1 if (p - 1) % d == 0]
        isempty(ks) && continue
        for k in unique([first(ks), last(ks), ks[length(ks) ÷ 2]])
            H = subgroup(p, k)
            mx = 0
            trials = 150
            for _ in 1:trials
                a = [myrand(p) for _ in 1:4]
                b = [myrand(p) for _ in 1:4]
                generic_ok(p, a, b) || continue
                n = n3_count(p, H, a, b)
                n > mx && (mx = n)
            end
            bound = k * k ÷ p + 2
            tchecked += 1
            if mx > bound
                tfails += 1
                println("V4 VIOLATION p=$p k=$k max=$mx bound=$bound")
            end
        end
    end

    total = fails + zfails + tfails
    println(total == 0 ? "JULIA KEY: ALL PASS" : "JULIA KEY: FAILURES=$total")
end

main()
