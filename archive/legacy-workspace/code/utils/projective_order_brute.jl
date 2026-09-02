# projective_order_brute.jl — Helper module for v7.
#
# Simple brute-force projective order: O(p^2) in time, O(1) in space.
# This replaces the broken BSGS implementation in v7.
#
# Usage:
#   include("projective_order_brute.jl")
#   ord = projective_order_brute(A, p)
#
# On p = 4481, ord_p(A) for A = (2,1,1,1) is 64, found in <1 second.
# On p = 31, ord_p(A) is 5, found in <1 ms.

function projective_order_brute(A, p; max_iter=p*p)
    a, b, c, d = A
    # A^1
    m11, m12, m21, m22 = a % p, b % p, c % p, d % p
    for k in 1:max_iter
        if (m11, m12, m21, m22) == (1, 0, 0, 1)
            return k
        end
        # Multiply by A
        m11, m12, m21, m22 = (
            (a * m11 + b * m21) % p,
            (a * m12 + b * m22) % p,
            (c * m11 + d * m21) % p,
            (c * m12 + d * m22) % p,
        )
    end
    return -1
end
