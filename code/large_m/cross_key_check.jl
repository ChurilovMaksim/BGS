# R87 — Phase 5 cross-key Julia spot check.
#
# Computes Tr(M_q^4) for (N=461, K=23, m=20) at q in {1, 2, 3} via Julia
# eigvalsh, and prints the centered value Delta_4(q) so the Python
# pipeline (src/large_m/trace_fluctuation.py) can be cross-validated.
#
# Note: kurtosis is not exported by Statistics in Julia 1.11; we use
# direct sums of e^k.

using LinearAlgebra
using Random
using Printf

const N = 461
const K = 23
const a = 23
const T_TRACE = 3
const M = 20   # m_+ = (N-1) / (2K) for K=23, N=461 is 10, but principal coset is 2*10 = 20

# Use the principal coset (chi_k(a) = 1). Build the dlog table.
function primitive_root(p::Int)
    g = 2
    while true
        if all(powermod(g, (p - 1) ÷ f, p) != 1 for f in factor_distinct(p - 1))
            return g
        end
        g += 1
    end
end

function factor_distinct(n::Int)
    # returns distinct prime factors of n
    out = Int[]
    d = 2
    while d * d <= n
        if n % d == 0
            push!(out, d)
            while n % d == 0
                n ÷= d
            end
        end
        d += 1
    end
    if n > 1
        push!(out, n)
    end
    return out
end

function dlog_table(p::Int, g::Int)
    tab = zeros(Int, p)
    x = 1
    for s in 0:(p - 2)
        tab[x + 1] = s
        x = x * g % p
    end
    return tab
end

function index_coset(p::Int, K::Int, a::Int, dlog::Vector{Int})
    # characters chi_k with chi_k(a) = 1, i.e. k * dlog[a] = 0 mod (p-1).
    ks = Int[]
    da = dlog[a + 1]
    for k in 0:(p - 2)
        if (k * da) % (p - 1) == 0
            push!(ks, k)
        end
    end
    return ks
end

function jacobi_matrix(p::Int, K::Int, a::Int, dlog::Vector{Int}, ks::Vector{Int}, q::Int)
    xs = [x for x in 1:(p - 1) if x != 1]   # exclude x = 0 and x = 1
    # The Python module excludes x = 0 AND x = 1 from the J sum, then uses
    # dlog[x] with dlog[0] = 0. We'll match that: x in 0..p-1, x != 0, x != 1.
    # Note: the dlog table has dlog[0] = 0 by construction; dlog is only valid
    # for nonzero x.
    # Use xs = [x for x in 0:(p-1) if x != 0 && x != 1]  (range 0 to p-1).
    # Re-derive properly:
    xs = collect(0:(p - 1))
    filter!(x -> x != 0 && x != 1, xs)
    dl_x = [dlog[x + 1] for x in xs]
    dl_xm1 = [dlog[((x - 1) % p) + 1] for x in xs]
    m = length(ks)
    nxs = length(xs)
    W = [exp(-2im * pi * ks[i + 1] * dl_x[j] / (p - 1)) for i in 0:(m - 1), j in 1:nxs]
    Vv = [exp(2im * pi * ks[i + 1] * dl_xm1[j] / (p - 1)) for i in 0:(m - 1), j in 1:nxs]
    ph = [exp(2im * pi * (q * xs[j] % p) / p) for j in 1:nxs]
    return (W .* ph') * Vv'
end

function build_M(p::Int, K::Int, a::Int, dlog::Vector{Int}, ks::Vector{Int}, q::Int)
    J = jacobi_matrix(p, K, a, dlog, ks, q)
    inv2 = powermod(2, p - 2, p)
    C = [exp(-2im * pi * ((inv2 * q) % p) / p)] .* J ./ (p - 1)
    Mc = C .+ C'
    return real.(Mc)
end

function main()
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    m = length(ks)
    @printf("N=%d K=%d a=%d  m (principal coset) = %d\n", N, K, a, m)
    @assert m == M "mismatch"

    for q in (1, 2, 3)
        M_q = build_M(N, K, a, dlog, ks, q)
        e = eigvals(Hermitian(M_q))
        tr2 = sum(e .^ 2)
        tr4 = sum(e .^ 4)
        sigma2 = tr2 / m
        # Catalan_4 = 2
        expected_4 = 2.0 * (sigma2 ^ 2) * m
        delta_4 = tr4 - expected_4
        @printf("q=%d  tr2=%.6e  tr4=%.6e  expected_tr4=%.6e  Delta_4=%.6e  C_4=%.6e\n",
                q, tr2, tr4, expected_4, delta_4, abs(delta_4) / sqrt(m))
    end
end

main()
