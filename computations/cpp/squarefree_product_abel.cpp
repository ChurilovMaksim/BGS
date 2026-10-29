// Independent integer certificate for BGS-TRACE-123.
// Recomputes the ten orders, the corner integers, the finite-table
// least common multiples, and the degree-four lower bounds.
// A pass does not prove BGS-TRACE-005.

#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

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
            b.d.push_back(static_cast<std::uint32_t>(v));
            v >>= 32;
        }
        return b;
    }

    static Big from_dec(const std::string& s) {
        if (s.empty()) throw std::runtime_error("empty decimal");
        Big b = from_u64(0);
        for (char c : s) {
            if (c < '0' || c > '9') throw std::runtime_error("decimal");
            b = b.mul_small(10) + from_u64(static_cast<std::uint64_t>(c - '0'));
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

    Big operator+(const Big& o) const {
        Big r;
        r.d.assign(std::max(d.size(), o.d.size()) + 1, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < r.d.size(); ++i) {
            carry += i < d.size() ? d[i] : 0;
            carry += i < o.d.size() ? o.d[i] : 0;
            r.d[i] = static_cast<std::uint32_t>(carry);
            carry >>= 32;
        }
        r.trim();
        return r;
    }

    Big operator-(const Big& o) const {
        if (cmp(o) < 0) throw std::runtime_error("negative");
        Big r;
        r.d.assign(d.size(), 0);
        std::int64_t borrow = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::int64_t cur = static_cast<std::int64_t>(d[i]) - borrow;
            if (i < o.d.size()) cur -= o.d[i];
            if (cur < 0) {
                cur += (std::int64_t(1) << 32);
                borrow = 1;
            } else {
                borrow = 0;
            }
            r.d[i] = static_cast<std::uint32_t>(cur);
        }
        r.trim();
        return r;
    }

    Big shl1() const {
        Big r;
        r.d.assign(d.size() + 1, 0);
        std::uint32_t carry = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::uint32_t bit = d[i] >> 31;
            r.d[i] = (d[i] << 1) | carry;
            carry = bit;
        }
        r.d.back() = carry;
        r.trim();
        return r;
    }

    int bit_length() const {
        if (is_zero()) return 0;
        int top = 31;
        while (top > 0 && ((d.back() >> top) & 1U) == 0) --top;
        return static_cast<int>((d.size() - 1) * 32 + top + 1);
    }

    bool bit(int i) const {
        if (i < 0) return false;
        std::size_t limb = static_cast<std::size_t>(i) / 32;
        if (limb >= d.size()) return false;
        return ((d[limb] >> (i % 32)) & 1U) != 0;
    }

    Big mul_small(std::uint32_t m) const {
        Big r;
        r.d.assign(d.size() + 2, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            carry += static_cast<std::uint64_t>(d[i]) * m;
            r.d[i] = static_cast<std::uint32_t>(carry);
            carry >>= 32;
        }
        std::size_t i = d.size();
        while (carry) {
            r.d[i++] = static_cast<std::uint32_t>(carry);
            carry >>= 32;
        }
        r.trim();
        return r;
    }

    Big operator*(const Big& o) const {
        Big r;
        r.d.assign(d.size() + o.d.size() + 1, 0);
        for (std::size_t i = 0; i < d.size(); ++i) {
            std::uint64_t carry = 0;
            for (std::size_t j = 0; j < o.d.size() || carry; ++j) {
                if (i + j >= r.d.size()) r.d.push_back(0);
                std::uint64_t prod = j < o.d.size()
                    ? static_cast<std::uint64_t>(d[i]) * o.d[j]
                    : 0;
                std::uint64_t sum = static_cast<std::uint64_t>(r.d[i + j])
                    + static_cast<std::uint32_t>(prod)
                    + static_cast<std::uint32_t>(carry);
                r.d[i + j] = static_cast<std::uint32_t>(sum);
                carry = (prod >> 32) + (carry >> 32) + (sum >> 32);
            }
        }
        r.trim();
        return r;
    }

    static std::pair<Big, Big> divmod(Big a, const Big& b) {
        if (b.is_zero()) throw std::runtime_error("div0");
        if (a.cmp(b) < 0) return {from_u64(0), a};
        Big q = from_u64(0);
        Big r = from_u64(0);
        for (int i = a.bit_length() - 1; i >= 0; --i) {
            r = r.shl1();
            if (a.bit(i)) r = r + from_u64(1);
            if (r.cmp(b) >= 0) {
                r = r - b;
                int limb = i / 32;
                int shift = i % 32;
                if (static_cast<int>(q.d.size()) <= limb) q.d.resize(limb + 1, 0);
                q.d[limb] |= (1U << shift);
            }
        }
        q.trim();
        return {q, r};
    }

    static Big gcd(Big a, Big b) {
        while (!b.is_zero()) {
            Big r = divmod(a, b).second;
            a = b;
            b = r;
        }
        return a;
    }
};

struct Rat {
    Big n;
    Big d;

    static Rat from_u64(std::uint64_t v) { return {Big::from_u64(v), Big::from_u64(1)}; }

    static Rat make(Big num, Big den) {
        if (den.is_zero()) throw std::runtime_error("zero den");
        Big g = Big::gcd(num, den);
        auto nq = Big::divmod(num, g).first;
        auto dq = Big::divmod(den, g).first;
        return {nq, dq};
    }

    static Rat frac(std::uint64_t a, std::uint64_t b) {
        return make(Big::from_u64(a), Big::from_u64(b));
    }

    static Rat dec(const std::string& num, const std::string& den) {
        return make(Big::from_dec(num), Big::from_dec(den));
    }

    Rat operator+(const Rat& o) const {
        return make(n * o.d + o.n * d, d * o.d);
    }

    Rat operator-(const Rat& o) const {
        if ((n * o.d).cmp(o.n * d) < 0) throw std::runtime_error("rat negative");
        return make(n * o.d - o.n * d, d * o.d);
    }

    Rat operator*(const Rat& o) const { return make(n * o.n, d * o.d); }

    Rat operator/(const Rat& o) const { return make(n * o.d, d * o.n); }

    bool operator<(const Rat& o) const { return (n * o.d).cmp(o.n * d) < 0; }
    bool operator==(const Rat& o) const { return n.cmp(o.n) == 0 && d.cmp(o.d) == 0; }
};

void require(bool cond, const std::string& message) {
    if (!cond) throw std::runtime_error(message);
}

Rat series_upper(Rat z, int n) {
    Rat term = Rat::from_u64(1);
    Rat total = Rat::from_u64(0);
    for (int j = 0; j < n; ++j) {
        total = total + term;
        term = term * z / Rat::from_u64(static_cast<std::uint64_t>(j + 1));
    }
    Rat denom = Rat::from_u64(1) - z / Rat::from_u64(static_cast<std::uint64_t>(n + 1));
    return total + term / denom;
}

Rat rl(Rat z) { return Rat::frac(1, 1) / (series_upper(z, 4) - Rat::from_u64(1)); }

int legendre(int p) { return (p % 8 == 1 || p % 8 == 7) ? 1 : -1; }

std::pair<int, std::int64_t> order_and_witness(int p) {
    int modulus = p - legendre(p);
    std::int64_t u = 1;
    std::int64_t v = 0;
    for (int m = 1; m <= modulus; ++m) {
        std::int64_t nu = u + 2 * v;
        std::int64_t nv = u + v;
        u = nu;
        v = nv;
        std::int64_t value = (m % 2) ? u : v;
        if (modulus % m == 0 && value % p == 0) return {m, value};
    }
    throw std::runtime_error("order missing");
}

void prefix_clear(int p, int t) {
    std::int64_t u = 1;
    std::int64_t v = 0;
    for (int m = 1; m < t; ++m) {
        std::int64_t nu = u + 2 * v;
        std::int64_t nv = u + v;
        u = nu;
        v = nv;
        std::int64_t value = (m % 2) ? u : v;
        require(value % p != 0, "smaller index");
    }
}

int lcm(int a, int b) { return a / std::gcd(a, b) * b; }

int lcm3(int a, int b, int c) { return lcm(lcm(a, b), c); }

const int PRIMES[] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
const int ORDERS[] = {4, 6, 3, 12, 14, 8, 20, 11, 10, 15};
const std::int64_t WITNESSES[] = {
    12, 70, 7, 13860, 80782, 408, 15994428, 8119, 2378, 275807};

int order_of(int p) {
    for (int i = 0; i < 10; ++i) {
        if (PRIMES[i] == p) return ORDERS[i];
    }
    throw std::runtime_error("unknown prime");
}

void check_orders() {
    for (int i = 0; i < 10; ++i) {
        auto got = order_and_witness(PRIMES[i]);
        require(got.first == ORDERS[i], "order");
        require(got.second == WITNESSES[i], "witness");
        require(got.second % PRIMES[i] == 0, "divisible");
        prefix_clear(PRIMES[i], ORDERS[i]);
        require((PRIMES[i] - legendre(PRIMES[i])) % ORDERS[i] == 0, "splitting");
    }
}

void check_corners() {
    require(4 * 6 * 8 * 12 <= 3 * 3 * 5 * 7 * 11, "four primes");
    require(4 * 6 * 8 * 12 * 14 <= 6 * 3 * 5 * 7 * 11 * 13, "five primes");
    require(2 * 6 * 8 * 12 <= 3 * 5 * 7 * 11, "primes at least five");
    require(4 * 8 * 12 <= 5 * 7 * 11, "three times a prime at least seven");
    require(72 * 30 <= 75 * 29, "three times five, tail");
    require(3 * 29 - 72 == 15, "three times five, slope");
    require(48 * 12 <= 63 * 11, "three times seven, tail");
    require(15 * 11 - 48 == 117, "three times seven, slope");
    require(8 * 12 * 38 <= 9 * 11 * 37, "eleven tail");
    require(9 * 11 - 8 * 12 == 3, "eleven slope");
    require(8 * 14 * 24 <= 9 * 13 * 23, "thirteen tail");
    require(9 * 13 - 8 * 14 == 5, "thirteen slope");
    require(8 * 18 * 20 <= 9 * 17 * 19, "seventeen tail");
    require(17 - 8 == 9, "seventeen slope");
    require(4 * 38 * 185 == 152 * 5 * 37, "return corner");
    require(20 * 37 == 740, "return slope");
    require(152 < 5 * 185, "wide ratio below five");
    require(88 < 5 * 115, "narrow ratio below five");
    require(168 < 5 * 195, "subset ratios below five");
}

void check_explicit_products() {
    const int pure[][4] = {
        {3, 5, 7, 12}, {3, 5, 11, 12}, {3, 5, 13, 84},
        {3, 5, 17, 24}, {3, 5, 19, 60}, {3, 5, 23, 132},
    };
    const bool short_flag[] = {true, true, false, true, true, true};
    for (int i = 0; i < 6; ++i) {
        int order = lcm3(order_of(pure[i][0]), order_of(pure[i][1]), order_of(pure[i][2]));
        int modulus = pure[i][0] * pure[i][1] * pure[i][2];
        require(order == pure[i][3], "pure lcm");
        require((12 * order <= 5 * modulus) == short_flag[i], "pure flag");
    }
    const int kicked[][4] = {
        {3, 5, 7, 12}, {3, 5, 11, 12}, {3, 5, 17, 24}, {3, 5, 19, 60},
        {3, 5, 29, 60}, {3, 5, 31, 60}, {3, 11, 13, 84}, {3, 11, 17, 24},
        {3, 11, 19, 60}, {3, 11, 23, 132}, {3, 11, 29, 60}, {3, 11, 31, 60},
        {3, 13, 17, 56}, {3, 13, 19, 140},
    };
    for (const auto& row : kicked) {
        int order = lcm3(order_of(row[0]), order_of(row[1]), order_of(row[2]));
        int modulus = row[0] * row[1] * row[2];
        require(order == row[3], "kick lcm");
        require(8 * order <= 3 * modulus, "kick flag");
    }
    require(8 * 132 > 3 * 345, "345 misses the strong shortness");
    require(8 * 84 > 3 * 195, "195 misses the strong shortness");
}

Rat lower_at_195() {
    const int primes[] = {3, 5, 13};
    const int orders[] = {4, 6, 14};
    Rat total = Rat::from_u64(0);
    for (int mask = 0; mask < 8; ++mask) {
        Rat coeff = Rat::from_u64(1);
        int step = 1;
        for (int k = 0; k < 3; ++k) {
            if (mask & (1 << k)) {
                coeff = coeff * Rat::frac(
                    static_cast<std::uint64_t>(primes[k] * primes[k] - 1),
                    static_cast<std::uint64_t>(primes[k] * primes[k]));
                step = lcm(step, orders[k]);
            } else {
                coeff = coeff * Rat::frac(1, static_cast<std::uint64_t>(primes[k] * primes[k]));
            }
        }
        require(2 * step < 5 * 195, "subset ratio");
        total = total + coeff * rl(Rat::frac(static_cast<std::uint64_t>(2 * step), 195));
    }
    return total;
}

}  // namespace

int main() {
    try {
        check_orders();
        check_corners();
        check_explicit_products();
        Rat kick = Rat::frac(82, 105);
        require(Rat::frac(3, 4) + Rat::frac(13, 420) == kick, "kick threshold");
        Rat wide = rl(Rat::frac(152, 185));
        Rat narrow = rl(Rat::frac(88, 115));
        require(wide == Rat::frac(4894346125ULL, 6236939544ULL), "152/185 fraction");
        require(narrow == Rat::frac(740666125ULL, 851428424ULL), "88/115 fraction");
        require(kick < wide && kick < narrow, "return bounds clear the kick margin");
        Rat low = lower_at_195();
        require(low == Rat::dec(
            "54421025909829591004375115797555753149956840906272969117235",
            "53966707446709005093212565207656544939196850800058844271758"),
            "N=195 fraction");
        require(kick < low, "N=195 clears the kick margin");
    } catch (const std::exception& ex) {
        std::cerr << "squarefree-product-abel: " << ex.what() << "\n";
        return 1;
    }
    std::cout << "squarefree-product-abel: pass\n";
    return 0;
}
