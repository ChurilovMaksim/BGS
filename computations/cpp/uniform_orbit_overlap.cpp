// Independent integer certificate for BGS-TRACE-125.
// Recomputes the Fourier mass, the lag-1 overlap, the exponent-1 box count,
// the archimedean and quadratic seeds, and the support scan at N = u_5.
// Norms of large Pell numbers are compared in explicit 128-bit products.
// A pass does not prove BGS-TRACE-005.

#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

namespace {

struct Wide {
    std::uint64_t hi;
    std::uint64_t lo;
};

Wide mul_u64(std::uint64_t a, std::uint64_t b) {
    const std::uint64_t a0 = a & 0xffffffffULL;
    const std::uint64_t a1 = a >> 32;
    const std::uint64_t b0 = b & 0xffffffffULL;
    const std::uint64_t b1 = b >> 32;
    const std::uint64_t p0 = a0 * b0;
    const std::uint64_t p1 = a0 * b1;
    const std::uint64_t p2 = a1 * b0;
    const std::uint64_t p3 = a1 * b1;
    const std::uint64_t mid = (p0 >> 32) + (p1 & 0xffffffffULL) + (p2 & 0xffffffffULL);
    Wide out;
    out.lo = (p0 & 0xffffffffULL) | (mid << 32);
    out.hi = p3 + (p1 >> 32) + (p2 >> 32) + (mid >> 32);
    return out;
}

int cmp_wide(Wide a, Wide b) {
    if (a.hi != b.hi) {
        return a.hi < b.hi ? -1 : 1;
    }
    if (a.lo != b.lo) {
        return a.lo < b.lo ? -1 : 1;
    }
    return 0;
}

Wide add_small(Wide a, std::uint64_t b) {
    const std::uint64_t lo = a.lo + b;
    if (lo < a.lo) {
        a.hi += 1;
    }
    a.lo = lo;
    return a;
}

void check_norm(std::int64_t u, std::int64_t v, int sign) {
    if (u < 0 || v < 0) {
        throw std::runtime_error("negative Pell number");
    }
    const Wide uu = mul_u64(static_cast<std::uint64_t>(u), static_cast<std::uint64_t>(u));
    Wide vv = mul_u64(static_cast<std::uint64_t>(v), static_cast<std::uint64_t>(v));
    // 2 v^2
    const std::uint64_t carry = vv.hi >> 63;
    vv.hi = (vv.hi << 1) | (vv.lo >> 63);
    vv.lo <<= 1;
    if (carry != 0) {
        throw std::runtime_error("norm product overflow");
    }
    if (sign == 1) {
        if (cmp_wide(uu, add_small(vv, 1)) != 0) {
            throw std::runtime_error("norm +1 failed");
        }
    } else if (cmp_wide(add_small(uu, 1), vv) != 0) {
        throw std::runtime_error("norm -1 failed");
    }
}

std::vector<std::pair<std::int64_t, std::int64_t>> pell_through(int n) {
    std::vector<std::pair<std::int64_t, std::int64_t>> rows;
    rows.reserve(static_cast<std::size_t>(n + 1));
    std::int64_t u = 1;
    std::int64_t v = 0;
    rows.push_back({u, v});
    check_norm(u, v, 1);
    for (int m = 1; m <= n; ++m) {
        const std::int64_t nu = u + 2 * v;
        const std::int64_t nv = u + v;
        u = nu;
        v = nv;
        if ((u % 2) == 0) {
            throw std::runtime_error("u parity failed");
        }
        check_norm(u, v, (m % 2) == 0 ? 1 : -1);
        rows.push_back({u, v});
    }
    return rows;
}

std::int64_t r_num(int k) {
    const int ak = k < 0 ? -k : k;
    if (k == 0) {
        return 4;
    }
    if (ak == 1) {
        return 2;
    }
    if (ak == 7) {
        return -2;
    }
    if (ak == 6 || ak == 8) {
        return -1;
    }
    return 0;
}

struct Coeff {
    int k;
    int ell;
    std::int64_t re;
    std::int64_t im;
};

Coeff f_num(int k, int ell) {
    Coeff c{k, ell, 0, 0};
    if (ell == 0) {
        const int ak = k < 0 ? -k : k;
        c.re = (ak == 7 ? 2000 : 0) + r_num(k) * 100;
        if (k == 0) {
            c.re -= 400;
        }
        c.im = 5 * (r_num(k + 1) - r_num(k - 1));
    } else if (ell == 1) {
        c.re = -3 * r_num(k);
        c.im = -4 * r_num(k);
    } else if (ell == -1) {
        c.re = -3 * r_num(k);
        c.im = 4 * r_num(k);
    }
    return c;
}

std::vector<Coeff> modes() {
    std::vector<Coeff> found;
    for (int k = -9; k <= 9; ++k) {
        for (int ell = -1; ell <= 1; ++ell) {
            const Coeff c = f_num(k, ell);
            const Coeff h = f_num(-k, -ell);
            if (h.re != c.re || h.im != -c.im) {
                throw std::runtime_error("Hermitian symmetry failed");
            }
            if (c.re != 0 || c.im != 0) {
                found.push_back(c);
            }
        }
    }
    if (found.size() != 32) {
        throw std::runtime_error("mode count");
    }
    return found;
}

std::int64_t sigma_num(const std::vector<Coeff>& rows) {
    std::int64_t total = 0;
    for (const Coeff& c : rows) {
        total += c.re * c.re + c.im * c.im;
    }
    return total;
}

int box_count(bool forward, bool origin, bool first, bool second) {
    int count = 0;
    bool saw_origin = false;
    bool saw_first = false;
    bool saw_second = false;
    for (int k = -9; k <= 9; ++k) {
        for (int ell = -1; ell <= 1; ++ell) {
            const int x = forward ? 3 * k + 2 * ell : 3 * k - 2 * ell;
            const int y = forward ? 4 * k + 3 * ell : -4 * k + 3 * ell;
            const int ax = x < 0 ? -x : x;
            const int ay = y < 0 ? -y : y;
            if (ax <= 9 && ay <= 1) {
                ++count;
                if (k == 0 && ell == 0) {
                    saw_origin = true;
                }
                if (forward && k == 1 && ell == -1) {
                    saw_first = true;
                }
                if (forward && k == -1 && ell == 1) {
                    saw_second = true;
                }
                if (!forward && k == 1 && ell == 1) {
                    saw_first = true;
                }
                if (!forward && k == -1 && ell == -1) {
                    saw_second = true;
                }
            }
        }
    }
    if (count != 3 || saw_origin != origin || saw_first != first || saw_second != second) {
        throw std::runtime_error("box count");
    }
    return count;
}

std::int64_t modp(std::int64_t n, std::int64_t x) {
    std::int64_t r = x % n;
    if (r < 0) {
        r += n;
    }
    return r;
}

struct Mat {
    std::int64_t a, b, c, d;
};

Mat matrix_power(int r) {
    Mat m{1, 0, 0, 1};
    for (int i = 0; i < r; ++i) {
        const Mat n{3 * m.a + 2 * m.c, 3 * m.b + 2 * m.d, 4 * m.a + 3 * m.c, 4 * m.b + 3 * m.d};
        m = n;
    }
    return m;
}

void scan_one(int n, const std::vector<std::pair<std::int64_t, std::int64_t>>& pell,
              const std::vector<Coeff>& rows) {
    const std::int64_t modulus = pell[static_cast<std::size_t>(n)].first;
    for (int r = 1; r < n; ++r) {
        const Mat m = matrix_power(r);
        int count = 0;
        std::int64_t real = 0;
        std::int64_t imag = 0;
        for (const Coeff& z : rows) {
            const std::int64_t x = modp(modulus, -(m.a * z.k + m.b * z.ell));
            const std::int64_t y = modp(modulus, -(m.c * z.k + m.d * z.ell));
            for (const Coeff& w : rows) {
                if (modp(modulus, w.k) == x && modp(modulus, w.ell) == y) {
                    real += w.re * z.re - w.im * z.im;
                    imag += w.re * z.im + w.im * z.re;
                    ++count;
                }
            }
        }
        if (imag != 0) {
            throw std::runtime_error("imaginary overlap");
        }
        const bool edge = r == 1 || r == n - 1;
        if (edge) {
            if (count != 2 || real != -56) {
                throw std::runtime_error("missing lag-1 overlap");
            }
        } else if (count != 0 || real != 0) {
            throw std::runtime_error("unexpected overlap");
        }
    }
}

void algebraic_seeds(const std::vector<std::pair<std::int64_t, std::int64_t>>& pell) {
    if (pell[4] != std::pair<std::int64_t, std::int64_t>(17, 12) ||
        pell[5] != std::pair<std::int64_t, std::int64_t>(41, 29) ||
        pell[7] != std::pair<std::int64_t, std::int64_t>(239, 169)) {
        throw std::runtime_error("Pell seeds");
    }
    if (104 * 104 * 2 - 128 * 128 != 5248) {
        throw std::runtime_error("archimedean integer");
    }
    if (66033 * 25 - 28 != 1650797 || 160000 * 25 != 4000000) {
        throw std::runtime_error("coefficient identity");
    }
    if (49 * 17 * 17 - 144 * 17 - 243 != 11470) {
        throw std::runtime_error("quadratic seed");
    }
    if (98 * 17 - 95 != 1571) {
        throw std::runtime_error("quadratic step");
    }
    if (7 * (7 * 17 * 17 - 10 * 17 + 19) != (7 * 17 - 5) * (7 * 17 - 5) + 108) {
        throw std::runtime_error("positivity identity");
    }
    if (2 * (2 * 4 * 9 + 5) != 154) {
        throw std::runtime_error("right-hand side");
    }
    if (!(163 < pell[7].first && 154 < pell[7].first)) {
        throw std::runtime_error("middle threshold");
    }
    if (81 - 2 * 16 != 49 || -2 * 72 != -144 || -81 - 2 * 81 != -243) {
        throw std::runtime_error("squared Pell comparison");
    }
    if (49 * 2 - 98 != 0 || 49 - 144 + 95 != 0) {
        throw std::runtime_error("difference coefficients");
    }
    for (int n = 5; n <= 31; n += 2) {
        const auto um = pell[static_cast<std::size_t>(n - 3)];
        const std::int64_t left_x = pell[static_cast<std::size_t>(n)].first - (10 * um.first + 9);
        const std::int64_t right_x =
            2 * um.first + 5 * pell[static_cast<std::size_t>(n - 4)].first - 9;
        const std::int64_t left_y =
            pell[static_cast<std::size_t>(n)].first - (um.first + 18 * um.second + 1);
        const std::int64_t right_y = 2 * pell[static_cast<std::size_t>(n - 5)].first - 1;
        if (left_x != right_x || left_y != right_y || left_x < 2 || left_y < 1) {
            throw std::runtime_error("size identity");
        }
        if (n >= 7) {
            const auto mid = pell[static_cast<std::size_t>(n - 1)];
            if (9 * mid.first + mid.second + 9 >= 5 * pell[static_cast<std::size_t>(n)].first) {
                throw std::runtime_error("|a| room");
            }
            if (mid.first + 18 * mid.second + 1 >= 6 * pell[static_cast<std::size_t>(n)].first) {
                throw std::runtime_error("|b| room");
            }
        }
    }
    for (int a = 1; a <= 4; ++a) {
        for (int b = 0; b <= 5; ++b) {
            if (b * b == 2 * a * a) {
                throw std::runtime_error("2-adic exception");
            }
        }
    }
}

}  // namespace

int main() {
    try {
        const auto pell = pell_through(40);
        const auto rows = modes();
        const std::int64_t mass = sigma_num(rows);
        constexpr std::int64_t den2 = 4000LL * 4000LL;
        if (mass * 160000 != 66033LL * den2) {
            throw std::runtime_error("sigma");
        }
        std::int64_t real = 0;
        std::int64_t imag = 0;
        int count = 0;
        for (const Coeff& z : rows) {
            const int x = -(3 * z.k + 2 * z.ell);
            const int y = -(4 * z.k + 3 * z.ell);
            for (const Coeff& w : rows) {
                if (w.k == x && w.ell == y) {
                    real += w.re * z.re - w.im * z.im;
                    imag += w.re * z.im + w.im * z.re;
                    ++count;
                }
            }
        }
        if (count != 2 || imag != 0 || real != -56) {
            throw std::runtime_error("lag-1 coefficient");
        }
        if ((mass + 2 * real) * 4000000 != 1650797LL * den2) {
            throw std::runtime_error("effective mass");
        }
        box_count(true, true, true, true);
        box_count(false, true, true, true);
        algebraic_seeds(pell);
        for (int n : {5, 7, 9, 11}) {
            scan_one(n, pell, rows);
        }
    } catch (const std::exception& err) {
        std::cerr << err.what() << '\n';
        return 1;
    }
    std::cout << "uniform-orbit-overlap: pass\n";
    return 0;
}
