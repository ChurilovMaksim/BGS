// Independent integer certificate for BGS-TRACE-120.
// Recomputes the exponential majorants, the cleared comparisons, the two
// digit windows, the gcd of C^t-I through t=40, and the agreement of the
// divisibility order with matrix powering for every odd modulus through 300.
// A pass does not prove BGS-TRACE-005.

#include <algorithm>
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

    bool is_zero() const { return d.size() == 1 && d[0] == 0; }

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

    Big add(const Big& o) const {
        Big r;
        r.d.assign(std::max(d.size(), o.d.size()) + 1, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < r.d.size(); ++i) {
            carry += i < d.size() ? d[i] : 0;
            carry += i < o.d.size() ? o.d[i] : 0;
            r.d[i] = static_cast<std::uint32_t>(carry % BASE);
            carry /= BASE;
        }
        r.trim();
        return r;
    }

    Big sub(const Big& o) const {
        if (cmp(o) < 0) throw std::runtime_error("negative subtraction");
        Big r;
        r.d.assign(d.size(), 0);
        std::int64_t borrow = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::int64_t cur = static_cast<std::int64_t>(d[i]) - borrow
                - (i < o.d.size() ? static_cast<std::int64_t>(o.d[i]) : 0);
            if (cur < 0) {
                cur += BASE;
                borrow = 1;
            } else {
                borrow = 0;
            }
            r.d[i] = static_cast<std::uint32_t>(cur);
        }
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

std::uint64_t isqrt_u64(std::uint64_t n) {
    if (n < 2) return n;
    std::uint64_t x = 1;
    while (x < n && x <= n / x) {
        if (x > (UINT64_MAX >> 1)) break;
        x <<= 1;
    }
    for (;;) {
        std::uint64_t z = (x + n / x) / 2;
        if (z >= x) break;
        x = z;
    }
    while (x > 0 && x > n / x) --x;
    if ((x + 1) != 0 && (x + 1) <= n / (x + 1))
        throw std::runtime_error("isqrt undershot");
    return x;
}

Frac r_coeff(int k) {
    int a = k < 0 ? -k : k;
    if (k == 0) return Frac::make(1, 1);
    if (a == 1) return Frac::make(1, 2);
    if (a == 7) return Frac::make(-1, 2);
    if (a == 6 || a == 8) return Frac::make(-1, 4);
    return Frac::make(0, 1);
}

std::pair<Frac, Frac> f_coeff(int k, int ell) {
    Frac re = Frac::make(0, 1), im = Frac::make(0, 1);
    if (ell == 0) {
        if (k == 7 || k == -7) re = re + Frac::make(1, 2);
        re = re + r_coeff(k) / Frac::make(10, 1);
        im = im + (r_coeff(k + 1) - r_coeff(k - 1)) / Frac::make(200, 1);
        if (k == 0) re = re - Frac::make(1, 10);
    } else if (ell == 1) {
        Frac rc = r_coeff(k);
        re = re + rc * Frac::make(-3, 1000);
        im = im + rc * Frac::make(-4, 1000);
    } else if (ell == -1) {
        Frac rc = r_coeff(k);
        re = re + rc * Frac::make(-3, 1000);
        im = im + rc * Frac::make(4, 1000);
    }
    return {re, im};
}

void check_majorant() {
    Frac total = Frac::make(0, 1);
    int count = 0;
    bool saw = false;
    for (int k = -9; k <= 9; ++k) {
        for (int ell = -1; ell <= 1; ++ell) {
            auto [re, im] = f_coeff(k, ell);
            if (re.n == 0 && im.n == 0) continue;
            ++count;
            Frac mag2 = re * re + im * im;
            if (mag2.d <= 0 || mag2.n < 0) throw std::runtime_error("mag2");
            __int128 pq = mag2.n * mag2.d;
            if (pq > static_cast<__int128>(~0ULL)) throw std::runtime_error("mag2 width");
            std::uint64_t root = isqrt_u64(static_cast<std::uint64_t>(pq));
            total = total + Frac::make(static_cast<__int128>(root) + 1, mag2.d);
            if (k == 7 && ell == 0) {
                if (!(re.n == 9 && re.d == 20 && im.n == 0)) throw std::runtime_error("mode 7,0");
                saw = true;
            }
        }
    }
    if (count != 32 || !saw || !(total.n == 184981 && total.d == 160000))
        throw std::runtime_error("majorant");
}

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
    if (!(series_upper(Frac::make(5, 6), 2) == Frac::make(361, 156)))
        throw std::runtime_error("5/6 majorant");
    if (!(series_upper(Frac::make(3, 4), 2) == Frac::make(17, 8)))
        throw std::runtime_error("3/4 majorant");
    if (!(partial_sum(Frac::make(1, 1), 6) == Frac::make(1957, 720)))
        throw std::runtime_error("e partial");
    if (!(partial_sum(Frac::make(2, 1), 5) == Frac::make(109, 15)))
        throw std::runtime_error("e^2 partial");
    if (!(partial_sum(Frac::make(6, 7), 4) == Frac::make(5647, 2401)))
        throw std::runtime_error("6/7 partial");
    Frac q = Frac::make(8, 17);
    Frac geo = Frac::make(0, 1);
    Frac term = Frac::make(1, 1);
    for (int k = 1; k <= 4; ++k) {
        term = term * q;
        geo = geo + term;
    }
    if (!(geo == Frac::make(70600, 83521))) throw std::runtime_error("four-term sum");
    if (!(361 * 3 < 156 * 7)) throw std::runtime_error("7/3");
    if (!(1957 * 7 > 720 * 19)) throw std::runtime_error("19/7");
    if (!(109 > 15 * 7)) throw std::runtime_error("e^2>7");
    if (!(7 * 7 < 12 * 5)) throw std::runtime_error("7/12");
    if (!(5 * 4 < 7 * 3)) throw std::runtime_error("5/7");
    if (!(41 * 7 < 5 * 60)) throw std::runtime_error("41/60");
    if (!(361LL * 70600 > 300LL * 83521)) throw std::runtime_error("activity");
    if (!(2401 * 4 < 3246 * 3)) throw std::runtime_error("p=7 ladder");
    if (!(156 * 4 > 205 * 3)) throw std::runtime_error("156/205");
    if (!(47 * 3 > 35 * 4)) throw std::runtime_error("one return");
}

__int128 igcd(__int128 a, __int128 b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        __int128 t = a % b;
        a = b;
        b = t;
    }
    return a;
}

void check_gcd() {
    __int128 u = 1, v = 0;
    for (int t = 1; t <= 40; ++t) {
        __int128 nu = u + 2 * v;
        __int128 nv = u + v;
        u = nu;
        v = nv;
        __int128 sign = (t % 2) ? -1 : 1;
        if (u * u - 2 * v * v != sign) throw std::runtime_error("norm");
        if ((u & 1) == 0) throw std::runtime_error("parity");
        __int128 u2 = u * u + 2 * v * v;
        __int128 v2 = 2 * u * v;
        __int128 g = igcd(igcd(u2 - 1, v2), 2 * v2);
        __int128 expect = (t % 2) ? 2 * u : 2 * v;
        if (g != expect || igcd(u, v) != 1) throw std::runtime_error("gcd");
    }
    __int128 uu = 1, vv = 0;
    int u6 = 0, v6 = 0, u3 = 0, u5 = 0;
    for (int t = 1; t <= 6; ++t) {
        __int128 nu = uu + 2 * vv;
        __int128 nv = uu + vv;
        uu = nu;
        vv = nv;
        if (t == 3) u3 = static_cast<int>(uu);
        if (t == 5) u5 = static_cast<int>(uu);
        if (t == 6) {
            u6 = static_cast<int>(uu);
            v6 = static_cast<int>(vv);
        }
    }
    if (u3 != 7 || u5 != 41 || u6 != 99 || v6 != 70) throw std::runtime_error("witness pell");
}

int divisibility_order(int n) {
    int u = 1, v = 0;
    for (int t = 1; t <= 20000; ++t) {
        int nu = static_cast<int>((u + 2LL * v) % n);
        int nv = static_cast<int>((u + 1LL * v) % n);
        u = nu;
        v = nv;
        if ((t % 2 == 1 && u == 0) || (t % 2 == 0 && v == 0)) return t;
    }
    throw std::runtime_error("divisibility order missing");
}

int matrix_order(int n) {
    int a = 1, b = 0, c = 0, d = 1;
    const int c00 = 3 % n, c01 = 2 % n, c10 = 4 % n, c11 = 3 % n;
    for (int t = 1; t <= 20000; ++t) {
        int na = static_cast<int>((1LL * a * c00 + 1LL * b * c10) % n);
        int nb = static_cast<int>((1LL * a * c01 + 1LL * b * c11) % n);
        int nc = static_cast<int>((1LL * c * c00 + 1LL * d * c10) % n);
        int nd = static_cast<int>((1LL * c * c01 + 1LL * d * c11) % n);
        a = na;
        b = nb;
        c = nc;
        d = nd;
        if (a == 1 && b == 0 && c == 0 && d == 1) return t;
    }
    throw std::runtime_error("matrix order missing");
}

bool prime_odd(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; ++d)
        if (n % d == 0) return false;
    return true;
}

void check_orders() {
    int short_count = 0, long_count = 0;
    for (int n = 3; n <= 300; n += 2) {
        int div = divisibility_order(n);
        int mat = matrix_order(n);
        if (div != mat) throw std::runtime_error("order mismatch");
        if (12 * div <= 5 * n) ++short_count;
        if (prime_odd(n) && (n == 3 || 2 * div >= n + 1)) ++long_count;
    }
    if (short_count < 1 || long_count < 1) throw std::runtime_error("census empty");
    if (divisibility_order(35) != 6 || matrix_order(35) != 6)
        throw std::runtime_error("N=35");
    if (divisibility_order(5) != 6 || divisibility_order(7) != 3 || matrix_order(3) != 4)
        throw std::runtime_error("small orders");
    if (12 * 3 <= 5 * 7 || 2 * 3 >= 8) throw std::runtime_error("p=7 hypotheses");
    // C ≡ [[0,2],[1,0]] (mod 3), and that square is -I.
    const int s00 = (0 * 0 + 2 * 1) % 3;
    const int s01 = (0 * 2 + 2 * 0) % 3;
    const int s10 = (1 * 0 + 0 * 1) % 3;
    const int s11 = (1 * 2 + 0 * 0) % 3;
    if (!(s00 == 2 && s01 == 0 && s10 == 0 && s11 == 2))
        throw std::runtime_error("C^2 mod 3");
}

void check_windows() {
    Big ten39 = pow10(39);
    Big ten80 = pow10(80);
    Big ten26 = pow10(26);
    Big b = Big::from_u64(184981);
    Big left = b.mul(ten39).mul(ten39.mul_small(30).add(Big::from_u64(1)));
    Big right = pow10(80).mul_small(160000);
    if (left.cmp(right) >= 0) throw std::runtime_error("short window");
    Big p4 = ten26.mul(ten26).mul(ten26).mul(ten26);
    Big long_left = b.mul(p4).mul_small(420);
    Big long_right = ten26.sub(Big::from_u64(2));
    long_right = long_right.mul_small(26);
    Big den = ten80.mul_small(160000).sub(b.mul(ten26));
    long_right = long_right.mul(den);
    if (long_left.cmp(long_right) >= 0) throw std::runtime_error("long window");
    (void)ten80;
}

}  // namespace

int main() {
    try {
        check_majorant();
        check_series();
        check_gcd();
        check_orders();
        check_windows();
    } catch (const std::exception& ex) {
        std::cerr << "order-ladder-abel: " << ex.what() << "\n";
        return 1;
    }
    std::cout << "order-ladder-abel: pass majorant=184981/160000 windows=10^39,10^26\n";
    return 0;
}
