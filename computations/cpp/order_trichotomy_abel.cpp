// Independent integer certificate for BGS-TRACE-121.
// Recomputes the exponential bounds, the cleared comparisons, the 10^25
// window, the Pell count through u_207, the order witnesses, a kernel
// sample, the trichotomy through modulus 500, and the half-order
// congruences through 10^6.
// A pass does not prove BGS-TRACE-005.

#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

constexpr std::uint32_t BASE = 1000000000U;

struct Big {
    std::vector<std::uint32_t> d{0};

    static Big from_u64(std::uint64_t v) {
        Big b;
        b.d.clear();
        if (v == 0) {
            b.d.push_back(0);
            return b;
        }
        while (v) {
            b.d.push_back(static_cast<std::uint32_t>(v % BASE));
            v /= BASE;
        }
        return b;
    }

    void trim() {
        while (d.size() > 1 && d.back() == 0) d.pop_back();
    }

    int cmp(const Big& o) const {
        if (d.size() != o.d.size()) return d.size() < o.d.size() ? -1 : 1;
        for (std::size_t i = d.size(); i-- > 0;) {
            if (d[i] != o.d[i]) return d[i] < o.d[i] ? -1 : 1;
        }
        return 0;
    }

    Big operator+(const Big& o) const {
        Big r;
        r.d.assign(std::max(d.size(), o.d.size()) + 1, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < r.d.size(); ++i) {
            carry += (i < d.size() ? d[i] : 0);
            carry += (i < o.d.size() ? o.d[i] : 0);
            r.d[i] = static_cast<std::uint32_t>(carry % BASE);
            carry /= BASE;
        }
        r.trim();
        return r;
    }

    Big operator-(const Big& o) const {
        Big r;
        r.d.assign(d.size(), 0);
        std::int64_t borrow = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::int64_t cur = static_cast<std::int64_t>(d[i]) - borrow;
            if (i < o.d.size()) cur -= o.d[i];
            if (cur < 0) {
                cur += BASE;
                borrow = 1;
            } else {
                borrow = 0;
            }
            r.d[i] = static_cast<std::uint32_t>(cur);
        }
        if (borrow) throw std::runtime_error("negative");
        r.trim();
        return r;
    }

    Big mul_small(std::uint64_t m) const {
        Big r;
        r.d.assign(d.size() + 4, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            carry += static_cast<std::uint64_t>(d[i]) * m;
            r.d[i] = static_cast<std::uint32_t>(carry % BASE);
            carry /= BASE;
        }
        std::size_t i = d.size();
        while (carry) {
            if (i >= r.d.size()) r.d.push_back(0);
            r.d[i++] = static_cast<std::uint32_t>(carry % BASE);
            carry /= BASE;
        }
        r.trim();
        return r;
    }

    Big mul(const Big& o) const {
        Big r;
        r.d.assign(d.size() + o.d.size() + 1, 0);
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::uint64_t carry = 0;
            for (std::size_t j = 0; j < o.d.size() || carry; ++j) {
                std::uint64_t cur = r.d[i + j] + carry;
                if (j < o.d.size()) cur += static_cast<std::uint64_t>(d[i]) * o.d[j];
                r.d[i + j] = static_cast<std::uint32_t>(cur % BASE);
                carry = cur / BASE;
            }
        }
        r.trim();
        return r;
    }

    int digits() const {
        if (d.size() == 1 && d[0] == 0) return 1;
        int count = static_cast<int>((d.size() - 1) * 9);
        std::uint32_t top = d.back();
        int extra = 0;
        while (top) {
            top /= 10;
            ++extra;
        }
        return count + extra;
    }
};

Big pow10(int e) {
    Big r = Big::from_u64(1);
    for (int i = 0; i < e; ++i) r = r.mul_small(10);
    return r;
}

struct Frac {
    __int128 n = 0;
    __int128 d = 1;

    static __int128 igcd(__int128 a, __int128 b) {
        if (a < 0) a = -a;
        if (b < 0) b = -b;
        while (b) {
            __int128 t = a % b;
            a = b;
            b = t;
        }
        return a == 0 ? 1 : a;
    }

    void norm() {
        if (d < 0) {
            n = -n;
            d = -d;
        }
        __int128 g = igcd(n, d);
        n /= g;
        d /= g;
    }

    static Frac make(__int128 n, __int128 d) {
        Frac f{n, d};
        f.norm();
        return f;
    }

    Frac operator+(Frac o) const { return make(n * o.d + o.n * d, d * o.d); }
    Frac operator-(Frac o) const { return make(n * o.d - o.n * d, d * o.d); }
    Frac operator*(Frac o) const { return make(n * o.n, d * o.d); }
    Frac operator/(Frac o) const { return make(n * o.d, d * o.n); }
    bool operator==(Frac o) const { return n == o.n && d == o.d; }
    bool operator<(Frac o) const { return n * o.d < o.n * d; }
    bool operator>(Frac o) const { return o < *this; }
};

void fail(const char* message) { throw std::runtime_error(message); }

Frac series_upper(Frac z, int n) {
    Frac term = Frac::make(1, 1);
    Frac total = Frac::make(0, 1);
    for (int j = 0; j < n; ++j) {
        total = total + term;
        term = term * z / Frac::make(j + 1, 1);
    }
    return total + term / (Frac::make(1, 1) - z / Frac::make(n + 1, 1));
}

Frac partial_sum(Frac z, int n) {
    Frac term = Frac::make(1, 1);
    Frac total = Frac::make(0, 1);
    for (int j = 0; j <= n; ++j) {
        total = total + term;
        term = term * z / Frac::make(j + 1, 1);
    }
    return total;
}

void check_series() {
    Frac ey = series_upper(Frac::make(6, 7), 4);
    Frac ea = series_upper(Frac::make(2, 7), 4);
    Frac eb = series_upper(Frac::make(6, 49), 4);
    Frac half = partial_sum(Frac::make(16, 17), 4);
    if (!(ey == Frac::make(23441, 9947))) fail("e6/7");
    if (!(ea == Frac::make(45187, 33957))) fail("e2/7");
    if (!(eb == Frac::make(31780817, 28118111))) fail("e6/49");
    if (!(half == Frac::make(213457, 83521))) fail("partial");
    if (!(213457 * 667 > 83521 * 1687)) fail("1687");
    Frac seven = Frac::make(48, 49) / (ey - Frac::make(1, 1))
        + Frac::make(1, 49) / (ea - Frac::make(1, 1));
    Frac tower = Frac::make(48, 49) / (ey - Frac::make(1, 1))
        + Frac::make(1, 49) / (eb - Frac::make(1, 1));
    if (!(seven == Frac::make(19796077, 25256270))) fail("L7");
    if (!(tower == Frac::make(7238798455LL, 8237425794LL))) fail("L49");
    if (!(seven > Frac::make(3, 4) && tower > Frac::make(3, 4))) fail("gap");
    Frac kick = Frac::make(13, 420);
    if (!(seven - kick > Frac::make(3, 4))) fail("kick7");
    if (!(tower - kick > Frac::make(3, 4))) fail("kick49");
    if (!(Frac::make(667, 1020) + Frac::make(1, 34) == Frac::make(41, 60))) fail("41/60");
    Frac pure = Frac::make(83521, 129936) + Frac::make(17, 256) + Frac::make(1, 578);
    if (!(pure == Frac::make(427139065, 600824064))) fail("ceiling");
    if (!(pure < Frac::make(5, 7))) fail("ceiling side");
    Frac long_tower = Frac::make(7, 12) + Frac::make(11, 120) + Frac::make(1, 242);
    if (!(long_tower == Frac::make(3287, 4840))) fail("long");
    if (!(long_tower + kick == Frac::make(72173, 101640))) fail("long sum");
    if (!(Frac::make(72173, 101640) < Frac::make(5, 7))) fail("long side");
    Frac p3 = Frac::make(1, 6) + Frac::make(3, 16) + Frac::make(1, 18);
    Frac p5 = Frac::make(1, 6) + Frac::make(5, 48) + Frac::make(1, 50);
    if (!(p3 == Frac::make(59, 144) && p3 + kick < Frac::make(5, 7))) fail("p3");
    if (!(p5 == Frac::make(349, 1200) && p5 + kick < Frac::make(5, 7))) fail("p5");
    if (5 * 25 - 12 * 5 - 12 != 53) fail("square");
}

void check_window() {
    const std::uint64_t margin_num = 14146865ULL;
    const std::uint64_t margin_den = 4205768448ULL;
    Big n = pow10(25);
    Big ten80 = pow10(80);
    Big left = Big::from_u64(184981).mul(n).mul(n).mul(n).mul(n).mul_small(margin_den);
    Big right_scale = ten80.mul_small(160000) - n.mul_small(184981);
    Big right = Big::from_u64(14146865).mul_small(2).mul(n - Big::from_u64(2)).mul(right_scale);
    if (margin_num != 14146865ULL) fail("margin");
    if (!(left.cmp(right) < 0)) fail("window");
}

int valuation(std::uint64_t n, int p) {
    int count = 0;
    while (n % static_cast<std::uint64_t>(p) == 0) {
        n /= static_cast<std::uint64_t>(p);
        ++count;
    }
    return count;
}

void check_witnesses_and_pell() {
    __int128 u = 1;
    __int128 v = 0;
    std::vector<__int128> us{1};
    std::vector<__int128> vs{0};
    for (int n = 1; n <= 30; ++n) {
        __int128 nu = u + 2 * v;
        __int128 nv = u + v;
        u = nu;
        v = nv;
        us.push_back(u);
        vs.push_back(v);
    }
    if (valuation(static_cast<std::uint64_t>(vs[8]), 3) != 1) fail("d3");
    if (us[12] != 19601 || vs[12] != 13860) fail("lam6");
    if (valuation(static_cast<std::uint64_t>(vs[12]), 5) != 1) fail("d5");
    if (us[6] != 99 || vs[6] != 70) fail("lam3");
    if (valuation(static_cast<std::uint64_t>(vs[6]), 7) != 1) fail("d7");
    if (us[1] % 13 == 0 || vs[2] % 13 == 0 || us[7] % 13 == 0 || vs[14] != 13 * 6214)
        fail("t13");
    if (valuation(static_cast<std::uint64_t>(vs[28]), 13) != 2) fail("d13");
    if (us[15] != 31 * 8897) fail("u15");
    if (us[1] % 31 == 0 || us[3] % 31 == 0 || us[5] % 31 == 0) fail("31 small");
    if (valuation(static_cast<std::uint64_t>(vs[30]), 31) != 2) fail("d31");

    Big U = Big::from_u64(1);
    Big V = Big::from_u64(0);
    std::vector<Big> hist{U};
    for (int n = 1; n <= 207; ++n) {
        Big nU = U + V.mul_small(2);
        V = U + V;
        U = nU;
        hist.push_back(U);
        if (n >= 4 && U.cmp(hist[static_cast<std::size_t>(n - 2)].mul_small(5)) < 0)
            fail("growth");
        if (n >= 5 && n % 2 == 1) {
            Big bound = U.mul_small(5);
            Big left = Big::from_u64(static_cast<std::uint64_t>(12 * n));
            if (left.cmp(bound) > 0) fail("pell short");
        }
    }
    if (U.digits() != 79 || U.cmp(pow10(39)) <= 0) fail("u207");
}

bool prime(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; ++d)
        if (n % d == 0) return false;
    return true;
}

int matrix_order(int p) {
    int a = 1, b = 0, c = 0, d = 1;
    for (int t = 1; t <= p + 1; ++t) {
        int na = (3 * a + 4 * b) % p;
        int nb = (2 * a + 3 * b) % p;
        int nc = (3 * c + 4 * d) % p;
        int nd = (2 * c + 3 * d) % p;
        a = na;
        b = nb;
        c = nc;
        d = nd;
        if (a == 1 && b == 0 && c == 0 && d == 1) return t;
    }
    fail("order");
    return 0;
}

std::pair<std::uint64_t, std::uint64_t> lam_pow(int m, std::uint64_t mod) {
    std::uint64_t u = 1, v = 0, bu = 3 % mod, bv = 2 % mod;
    int e = m;
    while (e) {
        if (e & 1) {
            std::uint64_t nu = (u * bu + 2 * v * bv) % mod;
            std::uint64_t nv = (u * bv + v * bu) % mod;
            u = nu;
            v = nv;
        }
        std::uint64_t nbu = (bu * bu + 2 * bv * bv) % mod;
        std::uint64_t nbv = (2 * bu * bv) % mod;
        bu = nbu;
        bv = nbv;
        e >>= 1;
    }
    return {u, v};
}

int brute_kernel(std::uint64_t u, std::uint64_t v, int modulus) {
    int a = static_cast<int>((u + modulus - 1) % static_cast<std::uint64_t>(modulus));
    int b = static_cast<int>(v % static_cast<std::uint64_t>(modulus));
    int count = 0;
    for (int x = 0; x < modulus; ++x) {
        int rhs = static_cast<int>((static_cast<long long>(-a) * x % modulus + modulus) % modulus);
        if (b == 0) {
            if (rhs != 0) continue;
            if (a == 0) {
                count += modulus;
            } else {
                int aa = a, bb = modulus;
                while (bb) {
                    int t = aa % bb;
                    aa = bb;
                    bb = t;
                }
                count += aa;
            }
        } else {
            int aa = b, bb = modulus;
            while (bb) {
                int t = aa % bb;
                aa = bb;
                bb = t;
            }
            int g = aa;
            if (rhs % g != 0) continue;
            int inv = 0;
            int b1 = b / g;
            int n1 = modulus / g;
            for (int i = 1; i < n1; ++i) {
                if ((static_cast<long long>(b1) * i) % n1 == 1) {
                    inv = i;
                    break;
                }
            }
            int y0 = static_cast<int>((static_cast<long long>(rhs / g) * inv) % n1);
            for (int step = 0; step < g; ++step) {
                int y = y0 + n1 * step;
                long long second = (2LL * b * x + 1LL * a * y) % modulus;
                if (second < 0) second += modulus;
                if (second == 0) ++count;
            }
        }
    }
    return count;
}

int closed_kernel(int p, int k, int delta, int t, int m) {
    if (m % t != 0) return 1;
    int j = 0;
    int q = m / t;
    while (q % p == 0) {
        q /= p;
        ++j;
    }
    int rho = std::min(k, delta + j);
    int value = 1;
    for (int i = 0; i < 2 * rho; ++i) value *= p;
    return value;
}

int order_of_lambda(int p, int eps) {
    int modulus = eps == 1 ? (p - 1) / 2 : p + 1;
    int t = modulus;
    int n = modulus;
    for (int d = 2; d * d <= n;) {
        if (n % d == 0) {
            while (t % d == 0) {
                auto [u, v] = lam_pow(t / d, static_cast<std::uint64_t>(p));
                if (u == 1 && v == 0) t /= d;
                else break;
            }
            while (n % d == 0) n /= d;
        }
        d += d == 2 ? 1 : 2;
    }
    if (n > 1) {
        while (t % n == 0) {
            auto [u, v] = lam_pow(t / n, static_cast<std::uint64_t>(p));
            if (u == 1 && v == 0) t /= n;
            else break;
        }
    }
    return t;
}

void check_half_order() {
    constexpr int limit = 1000000;
    std::vector<char> prime_s(static_cast<std::size_t>(limit) + 1, 1);
    prime_s[0] = prime_s[1] = 0;
    for (int p = 2; p * p <= limit; ++p) {
        if (!prime_s[static_cast<std::size_t>(p)]) continue;
        for (int q = p * p; q <= limit; q += p) prime_s[static_cast<std::size_t>(q)] = 0;
    }
    for (int p = 3; p <= limit; p += 2) {
        if (!prime_s[static_cast<std::size_t>(p)]) continue;
        int eps = (p % 8 == 1 || p % 8 == 7) ? 1 : -1;
        if (eps == 1) {
            auto [u, v] = lam_pow((p - 1) / 2, static_cast<std::uint64_t>(p));
            if (u != 1 || v != 0) fail("split congruence");
        } else {
            auto [u, v] = lam_pow((p + 1) / 2, static_cast<std::uint64_t>(p));
            if (u + 1 != static_cast<std::uint64_t>(p) || v != 0) fail("inert congruence");
        }
        int t = order_of_lambda(p, eps);
        if (p <= 500 && t != matrix_order(p)) fail("order agreement");
        if (2 * t == p + 1) fail("half order");
        if (eps == 1) {
            if (((p - 1) / 2) % t != 0 || t == p - 1) fail("split scan");
        } else if (((p + 1) / t) % 2 == 0 || t % 2 != 0) {
            fail("inert scan");
        }
        if (p >= 5 && 3 * t <= p - eps) {
            int order_3q = (t % 4 == 0) ? t : (t % 2 == 0 ? 2 * t : 4 * t);
            if (12LL * order_3q > 15LL * p) fail("three short");
        }
    }
}

void check_primes() {
    bool saw_seven = false;
    for (int p = 3; p <= 500; ++p) {
        if (!prime(p)) continue;
        int t = matrix_order(p);
        int eps = (p % 8 == 1 || p % 8 == 7) ? 1 : -1;
        int modulus = p - eps;
        if (modulus % t != 0) fail("div");
        if (2 * t == p + 1) fail("vacuous half");
        if (eps == 1) {
            if (((p - 1) / 2) % t != 0 || t == p - 1) fail("split divisor");
        } else if (((p + 1) / t) % 2 == 0) {
            fail("inert cofactor");
        }
        bool half = eps == 1 && 2 * t == p - 1;
        bool long_order = t == modulus;
        bool short_order = 3 * t <= modulus;
        int classes = static_cast<int>(half) + static_cast<int>(long_order) + static_cast<int>(short_order);
        if (classes != 1) fail("class");
        if (long_order && eps != -1) fail("long split");
        if (short_order && p >= 5 && 12 * t > 5 * p) fail("short ineq");
        if (long_order && t != p + 1) fail("long ineq");
        if (half && p == 7) saw_seven = true;
        if (half && p < 17 && p != 7) fail("small half");
    }
    if (!saw_seven) fail("missing 7");
    check_half_order();

    for (int p = 3; p <= 80; ++p) {
        if (!prime(p)) continue;
        int t = matrix_order(p);
        std::uint64_t mod = 1;
        for (int i = 0; i < 4; ++i) mod *= static_cast<std::uint64_t>(p);
        auto [uu, vv] = lam_pow(t, mod);
        int delta = vv == 0 ? 4 : valuation(vv, p);
        if (delta < 1) fail("depth");
        for (int k = 1; k <= 3; ++k) {
            int modulus = 1;
            for (int i = 0; i < k; ++i) modulus *= p;
            if (modulus > 1000) continue;
            int limit = std::min(modulus, std::min(4 * p, 2 * t * p));
            for (int m = 1; m <= limit; ++m) {
                auto [u, v] = lam_pow(m, static_cast<std::uint64_t>(modulus));
                int got = brute_kernel(u, v, modulus);
                int expect = closed_kernel(p, k, delta, t, m);
                if (got != expect) fail("kernel");
            }
        }
    }
}

}  // namespace

int main() {
    try {
        check_series();
        check_window();
        check_witnesses_and_pell();
        check_primes();
    } catch (const std::exception& ex) {
        std::cerr << "order-trichotomy-abel: " << ex.what() << "\n";
        return 1;
    }
    std::cout << "order-trichotomy-abel: pass\n";
    return 0;
}
