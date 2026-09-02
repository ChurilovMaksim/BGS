# linn_h3_subgroup.jl
# RING 1.1 / R57 — Test whether Linn 2024 stratification (Adv. Math. 499
# 111058, arXiv:2412.04976) restricts cleanly to multiplicative subgroup
# H^3 ⊂ (U(Z_p))^3 for the GL_3 Weyl element of length 2.
#
# Method (R57 plan sub-steps a-d):
#   (a) Construct Linn stratification of C(n) for GL_3, w of length 2.
#   (b) Restrict each stratum's variable set to H = <alpha> ⊂ F_p^×.
#   (c) Bound each restricted stratum by iterated Weil for GL_2 on H.
#   (d) Numerically measure the resulting bound.
#
# Honest scope: this script is the NUMERICAL DISCRIMINATOR (d). Steps
# (a-c) are paper-text only; the actual research move is to verify
# whether the iterated Weil argument transfers.

using Printf

# --- Linn setup ---------------------------------------------------------
# GL_3 Weyl element of length 2, admissible form (per Linn §1):
#   w = [[1, 1, 0],
#        [0, 1, 0],
#        [0, 0, 1]]
# (i.e. s_1; the simple reflection swapping 1<->2).
# Linn's bound (Theorem 1, N=2, l(w)=2):
#   Kl_p(ψ,ψ',n) << p^{r_k (1 - 4*2/6 + eps)} * C^{l(w)/2}
#               = p^{r_k (1/3 + eps)} * C
# For modulus c = diag(p^{-r_1}, p^{r_1-r_2}, p^{r_2}) the stratum
# r-vector is r = (r_1, r_2). Linn's C depends on character heights.

# --- Linn-style Kloosterman sum over H^3 -------------------------------
# Sum over (u_1, u_2, u_3) ∈ H^3 of
#   e_p( a*u_1 + b*u_2 + c*u_3 + d*u_1*u_2 + e*u_2*u_3 + f*u_1*u_2*u_3 )
# with (a,b,c,d,e,f) characters, p prime, H = <alpha> of order k.
function linn_h3_sum(p, H_set, chrs)
    a, b, c, d, e, f = chrs
    s_re = 0.0
    s_im = 0.0
    two_pi_over_p = 2 * pi / p
    for u1 in H_set
        for u2 in H_set
            for u3 in H_set
                phase = (a*u1 + b*u2 + c*u3 + d*u1*u2 + e*u2*u3 + f*u1*u2*u3) % p
                ang = two_pi_over_p * phase
                s_re += cos(ang)
                s_im += sin(ang)
            end
        end
    end
    return ComplexF64(s_re, s_im)
end

# --- Test driver --------------------------------------------------------
# Test cases: small primes, varied k, generic characters.
# We measure |sum| and check whether Linn's 1/3 power saving empirically
# holds in the H^3 (subgroup) case.
results = []
for (p, k) in [(101, 5), (101, 10), (211, 7), (401, 8), (401, 16), (401, 20),
               (1009, 4), (1009, 8), (2003, 7), (2003, 11), (3571, 17), (3571, 34)]
    # Sanity: k must divide p-1 (necessary for H to exist).
    if (p - 1) % k != 0
        @printf("SKIP p=%d k=%d (k does not divide p-1)\n", p, k)
        continue
    end
    # Find an element of EXACT order k in F_p^×.
    alpha = 0
    for g in 2:p-1
        cand = powermod(g, (p-1)÷k, p)
        if cand == 1
            continue
        end
        good = true
        for d in 1:k-1
            if k % d == 0 && powermod(cand, d, p) == 1
                good = false
                break
            end
        end
        if good
            alpha = cand
            break
        end
    end
    if alpha == 0
        @printf("SKIP p=%d k=%d (no element of order k)\n", p, k)
        continue
    end
    # Build H = <alpha>
    H_set = Set{Int}()
    h = 1
    for _ in 1:k
        push!(H_set, h)
        h = (h * alpha) % p
    end
    # Generic characters: random nonzero residues
    chrs = (rand(1:p-1), rand(1:p-1), rand(1:p-1),
            rand(1:p-1), rand(1:p-1), rand(1:p-1))
    s = linn_h3_sum(p, H_set, chrs)
    mag = abs(s)
    push!(results, (p, k, alpha, mag, mag/k, mag/k^(2/3), mag/sqrt(k)))
    @printf("p=%d k=%d |sum|=%.4f |sum|/k=%.4f |sum|/k^{2/3}=%.4f |sum|/sqrt(k)=%.4f\n",
            p, k, mag, mag/k, mag/k^(2/3), mag/sqrt(k))
end

# Write artifact (plain text)
open("artifacts/linn_h3_subgroup.txt", "w") do f
    println(f, "p  k  alpha  |sum|  |sum|/k  |sum|/k^{2/3}  |sum|/sqrt(k)")
    for r in results
        println(f, r[1], "  ", r[2], "  ", r[3], "  ", r[4], "  ",
                r[5], "  ", r[6], "  ", r[7])
    end
end
@printf("Wrote %d results to artifacts/linn_h3_subgroup.txt\n", length(results))

# Verdict: if |sum| ~ k^{2/3+eps} (Linn transfer), then mag/k^{2/3}
# is bounded. If |sum| ~ k (trivial Weil on inner), then mag/sqrt(k)
# ~ sqrt(k) and the obstruction remains.
max_ratio_k23 = maximum(r[6] for r in results)
max_ratio_sqrt = maximum(r[7] for r in results)
@printf("Max |sum|/k^{2/3} = %.4f (Linn transfer: bounded)\n", max_ratio_k23)
@printf("Max |sum|/sqrt(k) = %.4f (Trivial: should grow as sqrt(k))\n", max_ratio_sqrt)
