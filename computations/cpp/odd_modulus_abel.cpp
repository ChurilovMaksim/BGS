// Independent integer certificate for BGS-TRACE-124.
// Recomputes the fourteen orders, the ceiling majorants, the tail
// identities, the degree-four lower bounds, the inert table, and the
// defect endpoint at 2*10^26.
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

int lcm_int(int a, int b) { return a / std::gcd(a, b) * b; }

const int PRIMES[] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
const int ORDERS[] = {4, 6, 3, 12, 14, 8, 20, 11, 10, 15, 38, 5, 44, 23};
const std::int64_t WITNESSES[] = {
    12,
    70,
    7,
    13860,
    80782,
    408,
    15994428,
    8119,
    2378,
    275807,
    124145519261542LL,
    41,
    24580185800219268LL,
    318281039LL};

Rat K_factor(int r) {
    auto rr = static_cast<std::uint64_t>(r);
    return Rat::frac(rr * (rr + 1), rr * rr + rr + 1);
}

Rat one_plus_recip(int r) {
    return Rat::from_u64(1) + Rat::frac(1, static_cast<std::uint64_t>(r));
}

Rat tower_majorant(int p, int q, Rat alpha) {
    Rat gamma = one_plus_recip(p) * one_plus_recip(q);
    return gamma / alpha - Rat::frac(1, 2) +
           (alpha / Rat::from_u64(12)) * K_factor(p) * K_factor(q);
}

Rat envelope_majorant(int p, int q, int coef) {
    Rat alpha = Rat::frac(static_cast<std::uint64_t>(coef) * static_cast<std::uint64_t>(q - 1),
                          static_cast<std::uint64_t>(p) * static_cast<std::uint64_t>(q));
    Rat gamma = one_plus_recip(p) * one_plus_recip(q);
    return gamma / alpha - Rat::frac(1, 2) + (alpha / Rat::from_u64(12)) * K_factor(p);
}

void check_orders() {
    for (int i = 0; i < 14; ++i) {
        auto got = order_and_witness(PRIMES[i]);
        require(got.first == ORDERS[i], "order");
        require(got.second == WITNESSES[i], "witness");
        require(got.second % PRIMES[i] == 0, "divisible");
        prefix_clear(PRIMES[i], ORDERS[i]);
        require((PRIMES[i] - legendre(PRIMES[i])) % ORDERS[i] == 0, "splitting");
    }
}

void check_partners_of_23() {
    const int qs[] = {29, 31, 41, 43, 47};
    const int ts[] = {10, 15, 5, 44, 23};
    for (int i = 0; i < 5; ++i) {
        int order = lcm_int(11, ts[i]);
        require(12 * order <= 5 * 23 * qs[i], "23 times short");
    }
    require(lcm_int(11, 38) == 418, "23 times 37 order");
    require(12 * 418 > 5 * 851, "23 times 37 non-short");
    require(Rat::frac(2 * 418, 851) == Rat::frac(836, 851), "23 times 37 ratio");
}

void check_explicit_ceilings() {
    Rat five = Rat::frac(5, 7);
    struct Row {
        int p;
        int q;
        std::uint64_t an;
        std::uint64_t ad;
        std::uint64_t un;
        std::uint64_t ud;
    };
    const Row rows[] = {
        {3, 5, 8, 5, 499, 806},
        {3, 13, 56, 39, 8705, 14274},
        {5, 13, 84, 65, 2283, 3782},
        {11, 13, 168, 143, 1383, 2318},
        {23, 37, 836, 851, 11512715, 17117562},
    };
    for (const Row& row : rows) {
        Rat got = tower_majorant(row.p, row.q, Rat::frac(row.an, row.ad));
        require(got == Rat::frac(row.un, row.ud), "majorant");
        require(got < five, "majorant below 5/7");
    }
    Rat corner = tower_majorant(3, 23, Rat::frac(88, 69));
    require(corner == Rat::frac(108945, 158158), "3 times 23 majorant");
    Rat gap = five - corner;
    require(gap == Rat::frac(575, 22594), "3 times 23 gap");
    require(gap < Rat::frac(13, 420), "3 times 23 gap does not absorb the defect");
}

std::int64_t num3(int q) { return 61LL * q * q - 1097LL * q - 56; }
std::int64_t diff3(int q) { return 2 * (61LL * q - 518); }
std::int64_t num5(int q) { return 51LL * q * q - 877LL * q - 42; }
std::int64_t diff5(int q) { return 2 * (51LL * q - 413); }
std::int64_t num11(int q) { return 33LL * q * q - 541LL * q - 24; }
std::int64_t diff11(int q) { return 2 * (33LL * q - 254); }
std::int64_t num13(int q) { return 961LL * q * q - 15647LL * q - 686; }
std::int64_t diff13(int q) { return 2 * (961LL * q - 7343); }
std::int64_t num19(int q) { return 2029LL * q * q - 32633LL * q - 1400; }
std::int64_t diff19(int q) { return 2 * (2029LL * q - 15302); }
std::int64_t num23(int q) { return 533LL * q * q - 26109LL * q - 968; }
std::int64_t diff23(int q) { return 2 * (533LL * q - 12788); }

void check_one_tail(int p, int coef, int q0, std::int64_t (*num)(int), std::int64_t (*diff)(int),
                    int second, int den_factor) {
    Rat five = Rat::frac(5, 7);
    std::int64_t n0 = num(q0);
    std::int64_t n1 = num(q0 + 1);
    std::int64_t n2 = num(q0 + 2);
    require(n0 > 0, "tail numerator");
    require(n1 - n0 == diff(q0) && diff(q0) > 0, "tail first difference");
    require(n2 - 2 * n1 + n0 == second && second > 0, "tail second difference");
    const int qs[] = {q0, q0 + 1, q0 + 10};
    for (int q : qs) {
        std::uint64_t n = static_cast<std::uint64_t>(num(q));
        std::uint64_t d = static_cast<std::uint64_t>(den_factor) * static_cast<std::uint64_t>(q) *
                          static_cast<std::uint64_t>(q - 1);
        Rat got = five - envelope_majorant(p, q, coef);
        require(got == Rat::frac(n, d), "tail identity");
        require(Rat::from_u64(0) < got, "tail positive");
    }
}

void check_tails() {
    check_one_tail(3, 4, 23, num3, diff3, 122, 546);
    check_one_tail(5, 6, 19, num5, diff5, 102, 434);
    check_one_tail(11, 12, 17, num11, diff11, 66, 266);
    check_one_tail(13, 14, 17, num13, diff13, 1922, 7686);
    check_one_tail(19, 20, 23, num19, diff19, 4058, 16002);
    check_one_tail(23, 22, 50, num23, diff23, 1066, 12166);
}

Rat large_u1(int p, int q) {
    Rat alpha = (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(p))) *
                (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(q)));
    Rat gamma = one_plus_recip(p) * one_plus_recip(q);
    return gamma / alpha - Rat::frac(1, 2) + alpha / Rat::from_u64(12);
}

std::int64_t large_num(int p) {
    auto x = static_cast<std::int64_t>(p);
    return 11 * x * x * x - 311 * x * x - 701 * x - 7;
}

std::uint64_t large_den(int p) {
    auto x = static_cast<std::uint64_t>(p);
    return 84ULL * x * (x - 1) * (x + 2);
}

void check_large_primes() {
    Rat five = Rat::frac(5, 7);
    const int ps[] = {31, 37, 100};
    for (int p : ps) {
        int q = p + 2;
        require(five - large_u1(p, q) == Rat::frac(static_cast<std::uint64_t>(large_num(p)), large_den(p)),
                "large identity");
    }
    require(large_num(31) == 7092 && large_num(31) > 0, "large numerator");
    auto diff = [](int p) -> std::int64_t {
        auto x = static_cast<std::int64_t>(p);
        return 33 * x * x - 589 * x - 1001;
    };
    require(large_num(32) - large_num(31) == diff(31) && diff(31) == 12453, "large first difference");
    require(diff(32) - diff(31) == 66 * 31 - 556 && 66 * 31 - 556 == 1490, "large second difference");
    require(1490 > 0, "large second difference positive");
}

Big pow10(int exponent) {
    Big value = Big::from_u64(1);
    for (int i = 0; i < exponent; ++i) value = value.mul_small(10);
    return value;
}

void check_drop_and_radical() {
    require(5 * 5 * 5 * 5 - 12 * 5 * 5 - 24 * 5 - 12 == 193, "drop base");
    require(15 * 5 * 5 - 9 * 5 - 31 == 299, "drop step");
    require(21 * 5 - 24 == 81, "raise three");
    require(15 * 5 * 5 - 48 * 5 - 48 == 87, "raise the partner of three");
    require(12 * 84 < 5 * 195 * 3, "195 drop");
    require(12 * 84 > 5 * 195, "195 itself is not short");
    require(12 * 12 <= 5 * 105, "radical 105 is short");
    require(8 * 12 <= 3 * 105, "radical 105 is strongly short");
    require(8 * 12 <= 3 * 315, "315 inherits strong shortness");
    Rat ten24 = Rat::make(pow10(24), Big::from_u64(1));
    require(Rat::frac(4, 5) + (Rat::from_u64(1) / ten24) < Rat::frac(81, 100), "return threshold");
    require((Rat::from_u64(4) / (Rat::from_u64(5) * ten24)) < (Rat::from_u64(1) / ten24),
            "large fifteen ratio");
    require(pow10(24).cmp(Big::divmod(pow10(26), Big::from_u64(15)).first) < 0,
            "fifteen partner past 10^26");
    require(81 < 5 * 100, "81/100 lies below five");
}

Rat lower_terms(const std::vector<std::pair<Rat, Rat>>& terms) {
    Rat total = Rat::from_u64(0);
    for (const auto& term : terms) {
        require(Rat::from_u64(0) < term.second && term.second < Rat::from_u64(5), "degree-four domain");
        total = total + term.first * rl(term.second);
    }
    return total;
}

void check_lower_bounds() {
    Rat kick = Rat::frac(82, 105);
    Rat three = Rat::frac(3, 4);
    Rat at21 = lower_terms({
        {Rat::frac(383, 441), Rat::frac(8, 7)},
        {Rat::frac(1, 49), Rat::frac(8, 49)},
        {Rat::frac(1, 9), Rat::frac(2, 7)},
    });
    require(at21 == Rat::frac(265028515609711ULL, 309078510309860ULL), "21");
    require(kick < at21, "21 kick margin");
    Rat at195 = lower_terms({
        {Rat::frac(24, 25), Rat::frac(56, 65)},
        {Rat::frac(1, 25), Rat::frac(56, 325)},
    });
    require(at195 == Rat::frac(50134551873841695ULL, 54792051773384968ULL), "195");
    require(kick < at195, "195 kick margin");
    Rat inert_a2 = lower_terms({
        {Rat::frac(48, 49), Rat::frac(12, 13)},
        {Rat::frac(1, 49), Rat::frac(12, 91)},
    });
    require(inert_a2 == Rat::frac(26832108548323ULL, 33947639168772ULL), "inert-a2");
    require(kick < inert_a2, "inert-a2 kick margin");
    Rat short_a1 = lower_terms({
        {Rat::frac(8, 9), Rat::frac(80, 87)},
        {Rat::frac(1, 9), Rat::frac(20, 87)},
    });
    require(short_a1 == Rat::frac(114226176533733ULL, 112075008606140ULL), "three-short-a1");
    require(kick < short_a1, "three-short-a1 kick margin");
    Rat short_a2 = lower_terms({
        {Rat::frac(8, 9), Rat::frac(80, 87)},
        {Rat::frac(1, 9), Rat::frac(80, 261)},
    });
    require(short_a2 == Rat::frac(2228970493853307ULL, 2479202684534320ULL), "three-short-a2");
    require(kick < short_a2, "three-short-a2 kick margin");
    Rat scaled = Rat::frac(1599, 1600) * lower_terms({
        {Rat::frac(48, 49), Rat::frac(123, 140)},
        {Rat::frac(1, 49), Rat::frac(41, 140)},
    });
    require(scaled == Rat::frac(13146189928817400ULL, 17402756940259603ULL), "inert tail scale");
    require(three < scaled, "inert tail above 3/4");
    require(scaled < kick, "inert tail does not clear the kick");
}

Rat inert_subsum(int q) {
    auto qq = static_cast<std::uint64_t>(q);
    Rat alpha = Rat::frac(6 * (qq + 1), 7 * qq);
    Rat gamma = Rat::frac(2 * (qq + 1), 7 * qq);
    require(alpha < Rat::from_u64(5) && (gamma / Rat::from_u64(qq)) < Rat::from_u64(5), "inert domain");
    Rat top = Rat::frac(48, 49) * rl(alpha) + Rat::frac(1, 49) * rl(gamma);
    Rat low = Rat::frac(48, 49) * rl(alpha / Rat::from_u64(qq)) +
              Rat::frac(1, 49) * rl(gamma / Rat::from_u64(qq));
    return (Rat::from_u64(1) - Rat::frac(1, qq * qq)) * top + Rat::frac(1, qq * qq) * low;
}

void check_inert_table() {
    Rat kick = Rat::frac(82, 105);
    Rat corner = inert_subsum(13);
    require(corner == Rat::dec("16323101582366123785899971", "20875800430500088687646340"),
            "inert q=13 fraction");
    for (int q = 13; q <= 39; ++q) {
        require(kick < inert_subsum(q), "inert kick");
    }
}

Rat ten_to(int exponent) { return Rat::make(pow10(exponent), Big::from_u64(1)); }

void check_defect_endpoint() {
    Rat low = rl(Rat::frac(81, 100));
    require(low == Rat::frac(3352000000ULL, 4183386507ULL), "81/100 fraction");
    Rat margin = low - Rat::frac(3, 4);
    require(margin == Rat::frac(857840479ULL, 16733546028ULL), "return margin");
    Rat B = Rat::frac(184981, 160000);
    Rat n_value = Rat::from_u64(2) * ten_to(26);
    Rat ten80 = ten_to(80);
    require(B * n_value < ten80, "defect formula applies at 2e26");
    Rat n4 = n_value * n_value * n_value * n_value;
    Rat defect = (B * n4) / (Rat::from_u64(2) * (n_value - Rat::from_u64(2)) * (ten80 - B * n_value));
    require(defect < margin, "defect at 2e26 stays under the return margin");
    Rat huge = ten_to(78);
    require(Rat::from_u64(2) * huge * ten80 < B * huge * huge * huge * huge,
            "majorant exceeds 1 at 10^78");
    require(B * ten_to(79) < ten80, "majorant still defined at 10^79");
}

}  // namespace

int main() {
    try {
        check_orders();
        check_partners_of_23();
        check_explicit_ceilings();
        check_tails();
        check_large_primes();
        check_drop_and_radical();
        check_lower_bounds();
        check_inert_table();
        check_defect_endpoint();
    } catch (const std::exception& ex) {
        std::cerr << "odd-modulus-abel: " << ex.what() << "\n";
        return 1;
    }
    std::cout << "odd-modulus-abel: pass\n";
    return 0;
}
