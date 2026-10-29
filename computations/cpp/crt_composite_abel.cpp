// Independent integer certificate for BGS-TRACE-122.
// Recomputes the exponential bounds, the seven-family polynomial, the
// semiprime corners, the orders below 30, and the sandwich below 100.
// A pass does not prove BGS-TRACE-005.

#include <cstdint>
#include <iostream>
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

Rat partial_sum(Rat z, int n) {
    Rat term = Rat::from_u64(1);
    Rat total = Rat::from_u64(0);
    for (int j = 0; j <= n; ++j) {
        total = total + term;
        term = term * z / Rat::from_u64(static_cast<std::uint64_t>(j + 1));
    }
    return total;
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

Rat ru(Rat z) { return Rat::frac(1, 1) / (partial_sum(z, 8) - Rat::from_u64(1)); }

Rat rl(Rat z) { return Rat::frac(1, 1) / (series_upper(z, 4) - Rat::from_u64(1)); }

struct SBig {
    bool neg = false;
    Big mag = Big::from_u64(0);

    static SBig from_ll(long long v) {
        SBig s;
        if (v < 0) {
            s.neg = true;
            s.mag = Big::from_u64(static_cast<std::uint64_t>(-v));
        } else {
            s.mag = Big::from_u64(static_cast<std::uint64_t>(v));
        }
        if (s.mag.is_zero()) s.neg = false;
        return s;
    }

    static SBig from_big(bool neg, Big mag) {
        SBig s;
        s.neg = mag.is_zero() ? false : neg;
        s.mag = mag;
        return s;
    }

    int cmp(const SBig& o) const {
        if (neg != o.neg) return neg ? -1 : 1;
        int c = mag.cmp(o.mag);
        return neg ? -c : c;
    }

    SBig operator+(const SBig& o) const {
        if (neg == o.neg) return from_big(neg, mag + o.mag);
        if (mag.cmp(o.mag) >= 0) return from_big(neg, mag - o.mag);
        return from_big(o.neg, o.mag - mag);
    }

    SBig operator-() const { return from_big(!neg, mag); }

    SBig operator-(const SBig& o) const { return *this + (-o); }

    SBig operator*(const SBig& o) const {
        return from_big(neg != o.neg, mag * o.mag);
    }
};

struct Poly {
    std::vector<SBig> c;

    Poly(std::initializer_list<long long> raw) {
        c.reserve(raw.size());
        for (long long v : raw) c.push_back(SBig::from_ll(v));
        trim();
    }

    explicit Poly(std::vector<SBig> raw) : c(std::move(raw)) { trim(); }

    void trim() {
        while (c.size() > 1 && c.back().mag.is_zero()) c.pop_back();
    }

    Poly operator+(const Poly& o) const {
        std::vector<SBig> out(std::max(c.size(), o.c.size()), SBig::from_ll(0));
        for (std::size_t i = 0; i < c.size(); ++i) out[i] = out[i] + c[i];
        for (std::size_t i = 0; i < o.c.size(); ++i) out[i] = out[i] + o.c[i];
        return Poly(out);
    }

    Poly operator-() const {
        std::vector<SBig> out;
        for (const auto& v : c) out.push_back(-v);
        return Poly(out);
    }

    Poly operator-(const Poly& o) const { return *this + (-o); }

    Poly operator*(const Poly& o) const {
        std::vector<SBig> out(c.size() + o.c.size() - 1, SBig::from_ll(0));
        for (std::size_t i = 0; i < c.size(); ++i) {
            for (std::size_t j = 0; j < o.c.size(); ++j) out[i + j] = out[i + j] + c[i] * o.c[j];
        }
        return Poly(out);
    }
};

struct RF {
    Poly n;
    Poly d;
    RF operator+(const RF& o) const { return {n * o.d + o.n * d, d * o.d}; }
    RF operator-(const RF& o) const { return *this + RF{-o.n, o.d}; }
};

Big abs_gcd_all(const std::vector<SBig>& coeffs) {
    Big g = Big::from_u64(0);
    for (const auto& c : coeffs) g = Big::gcd(g, c.mag);
    return g;
}

std::vector<SBig> primitive(const Poly& poly) {
    Big g = abs_gcd_all(poly.c);
    require(!g.is_zero(), "zero polynomial");
    std::vector<SBig> out;
    for (const auto& c : poly.c) {
        out.push_back(SBig::from_big(c.neg, Big::divmod(c.mag, g).first));
    }
    if (out.back().neg) {
        for (auto& c : out) c = -c;
    }
    return out;
}

bool same_poly(const std::vector<SBig>& got, const std::vector<long long>& expect) {
    if (got.size() != expect.size()) return false;
    for (std::size_t i = 0; i < got.size(); ++i) {
        if (got[i].cmp(SBig::from_ll(expect[i])) != 0) return false;
    }
    return true;
}

int legendre(int p) { return (p % 8 == 1 || p % 8 == 7) ? 1 : -1; }

int order_of(int p) {
    // The divisibility criterion reduced modulo p. The integers u_m, v_m
    // themselves are checked only through index 29, where they fit in 64 bits.
    int u = 1, v = 0;
    for (int m = 1; m <= p + 1; ++m) {
        int nu = (u + 2 * v) % p;
        int nv = (u + v) % p;
        u = nu;
        v = nv;
        if (((m % 2) ? u : v) == 0) return m;
    }
    throw std::runtime_error("no order");
}

bool is_prime(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; d += d == 2 ? 1 : 2) {
        if (n % d == 0) return false;
    }
    return true;
}

std::string kind_of(int p, int t) {
    int eps = legendre(p);
    int modulus = p - eps;
    if (3 * t <= modulus) return "short";
    if (t == modulus || (eps == -1 && 2 * t == p + 1)) return "long";
    if (eps == 1 && 2 * t == p - 1) return "half";
    throw std::runtime_error("unclassified");
}

Rat ceiling(Rat alpha, Rat gamma, Rat beta, Rat unit, std::uint64_t square) {
    return ru(alpha) + beta + ru(gamma) / Rat::from_u64(square) + unit;
}

void check_orders() {
    const int ps[] = {3, 5, 7, 11, 13, 17, 19, 23, 29};
    const int ts[] = {4, 6, 3, 12, 14, 8, 20, 11, 10};
    const long long witnesses[] = {12, 70, 7, 13860, 80782, 408, 15994428, 8119, 2378};
    const char* kinds[] = {"long", "long", "half", "long", "long", "half", "long", "half", "short"};
    long long u = 1, v = 0;
    std::vector<std::pair<long long, long long>> rows{{u, v}};
    for (int m = 1; m <= 29; ++m) {
        long long nu = u + 2 * v;
        long long nv = u + v;
        u = nu;
        v = nv;
        rows.push_back({u, v});
    }
    for (int i = 0; i < 9; ++i) {
        int p = ps[i], t = ts[i];
        long long witness = (t % 2) ? rows[t].first : rows[t].second;
        require(witness == witnesses[i], "witness");
        require(witness % p == 0, "divisible");
        for (int m = 1; m < t; ++m) {
            long long earlier = (m % 2) ? rows[m].first : rows[m].second;
            require(earlier % p != 0, "smaller index");
        }
        require(kind_of(p, t) == kinds[i], "class");
        require(order_of(p) == t, "order");
    }
}

void check_arithmetic_and_tails() {
    require(4 * 6 * 30 < 5 * 5 * 29, "short corner");
    require(4 * 30 * 32 < 5 * 29 * 31, "both large");
    require(48 * 18 <= 85 * 17, "seventeen");
    require(8 * 30 <= 15 * 29, "three even");
    require(66 * 30 <= 115 * 29, "twenty-three half");
    require(3 * 30 * 34 < 5 * 31 * 33, "half times half");
    require(3 * 30 * 32 < 5 * 29 * 31, "inert gcd");
    require(12 * 12 > 5 * 21 && 12 * 6 <= 5 * 35, "seven products");
    require(12 * 84 > 5 * 195, "three primes");
    require(15 * 5 > 12 * 6, "three gcd 4");
    require(25 * 29 > 24 * 30, "five gcd 3");
    require(25 * 7 > 18 * 8, "five half");
    require(144 < 21 * 7, "eleven gcd 3");
    require(144 <= 76 * 2, "eleven gcd 4");
    require(55 * 13 > 36 * 14, "eleven half");
    require(65 * 13 > 24 * 14, "thirteen gcd 7");
    require(65 * 17 > 42 * 18, "thirteen half");
    require(240 < 140 * 2, "nineteen gcd 4");
    require(95 * 23 > 60 * 24, "nineteen half");
    require(115 * 3 > 66 * 4, "twenty-three half small");
    require(5 * 29 * 31 > 3 * 30 * 32, "inert corner");
    int identity = 5 * 31 * 33 - 3 * 30 * 34;
    require(identity == 2 * 31 * 31 + 4 * 31 + 9 && identity > 0, "split identity");
    require(36LL * 38 * 899 > 840LL * 37 * 39, "full alpha");
    require(37LL * 56 * 31 < 29LL * 72 * 39, "full beta");
    require(39LL * 29 * 30 < 31LL * 37 * 38, "full gamma");
    require(29LL * 31 < 37LL * 39, "full unit");
    require(3LL * 37 * 37 + 5 * 37 + 5 == 4297, "inert numerator");
    require(2LL * 37 * 38 * 39 == 109668, "inert denominator");
    long long left = 4297LL * 1736 * 870 * 1798;
    long long right = 109668LL * (29LL * 870 * 1798 + 31LL * 1736 * 1798 + 1736LL * 870);
    require(left < right, "inert extras");
}

void check_bounds() {
    Rat five = Rat::frac(5, 7);
    Rat kick = Rat::frac(82, 105);
    require((Rat::frac(3, 4) + Rat::frac(13, 420)) == kick, "kick threshold");
    struct Corner {
        Rat alpha, gamma, beta, unit;
        std::uint64_t square;
    };
    Corner corners[] = {
        {Rat::frac(8, 5), Rat::frac(4, 5), Rat::frac(3, 40), Rat::frac(1, 30), 9},
        {Rat::frac(56, 39), Rat::frac(28, 39), Rat::frac(3, 104), Rat::frac(1, 78), 9},
        {Rat::frac(84, 65), Rat::frac(28, 65), Rat::frac(5, 156), Rat::frac(1, 130), 25},
        {Rat::frac(88, 69), Rat::frac(22, 69), Rat::frac(3, 184), Rat::frac(1, 138), 9},
        {Rat::frac(96, 85), Rat::frac(16, 85), Rat::frac(5, 204), Rat::frac(1, 170), 25},
        {Rat::frac(144, 143), Rat::frac(12, 143), Rat::frac(11, 312), Rat::frac(1, 286), 121},
        {Rat::frac(224, 221), Rat::frac(16, 221), Rat::frac(13, 476), Rat::frac(1, 442), 169},
        {Rat::frac(440, 437), Rat::frac(22, 437), Rat::frac(19, 920), Rat::frac(1, 874), 361},
        {Rat::frac(660, 713), Rat::frac(60, 713), Rat::frac(23, 682), Rat::frac(1, 1426), 529},
    };
    for (const auto& c : corners) {
        require(ceiling(c.alpha, c.gamma, c.beta, c.unit, c.square) < five, "corner");
    }
    Rat split = ru(Rat::frac(960, 1023)) + Rat::frac(31, 990) + Rat::frac(33, 1984) + Rat::frac(1, 2046);
    Rat nonsplit = ru(Rat::frac(840, 899)) + Rat::frac(29, 1736) + Rat::frac(31, 870) + Rat::frac(1, 1798);
    require(split < five && nonsplit < five, "tails");

    Rat a21 = Rat::frac(8, 9) * Rat::frac(48, 49);
    Rat low21 = a21 * rl(Rat::frac(8, 7)) + (Rat::frac(8, 9) / Rat::from_u64(49)) * rl(Rat::frac(8, 21))
        + (Rat::frac(48, 49) / Rat::from_u64(9)) * rl(Rat::frac(2, 7))
        + Rat::frac(1, 441) * rl(Rat::frac(2, 21));
    require(low21 == Rat::make(Big::from_u64(1485928284770040951ULL), Big::from_u64(1861068320411356730ULL)), "N=21");
    require(kick < low21, "N=21 kick");
    Rat low3 = (Rat::frac(8, 9) * Rat::frac(840, 841)) * rl(Rat::frac(80, 87))
        + (Rat::frac(840, 841) / Rat::from_u64(9)) * rl(Rat::frac(20, 87));
    require(low3 == Rat::make(Big::from_u64(5704517734146ULL), Big::from_u64(5603750430307ULL)), "three short");
    require(kick < low3, "three short kick");

    Rat e6 = series_upper(Rat::frac(6, 7), 4);
    Rat e2 = series_upper(Rat::frac(2, 7), 4);
    require(e6 == Rat::frac(23441, 9947) && e2 == Rat::frac(45187, 33957), "majorants");
    Rat seven = Rat::frac(48, 49) / (e6 - Rat::from_u64(1)) + Rat::frac(1, 49) / (e2 - Rat::from_u64(1));
    require(seven == Rat::frac(19796077, 25256270), "seven");
    require(Rat::frac(3, 4) < seven - Rat::frac(13, 420), "seven kick");
}

void check_phi() {
    Poly q({0, 1});
    Poly one({1});
    Poly q2 = q * q;
    Poly num_m({-18, 0, 49});
    Poly den_m({0, -42, 49});
    Poly em_num = Poly({23441}) * num_m - Poly({9947}) * den_m;
    Poly a_num = Poly({48LL * 9947}) * (q2 - one) * Poly({-6, 7});
    Poly a_den = Poly({7}) * q * em_num;
    Poly b_num = Poly({8}) * Poly({-6, 7});
    Poly b_den = Poly({49}) * q2;
    Poly num_m3({-2, 0, 49});
    Poly den_m3({0, -14, 49});
    Poly em3 = Poly({45187}) * num_m3 - Poly({33957}) * den_m3;
    Poly c_num = Poly({33957}) * (q2 - one) * Poly({-2, 7});
    Poly c_den = Poly({7}) * q * em3;
    RF phi = RF{a_num, a_den} + RF{b_num, b_den} + RF{c_num, c_den};
    RF diff = phi - RF{Poly({3}), Poly({4})};
    auto num = primitive(diff.n);
    auto den = primitive(diff.d);
    std::size_t shift = 0;
    while (shift < num.size() && shift < den.size() && num[shift].mag.is_zero() && den[shift].mag.is_zero()) {
        ++shift;
    }
    num.erase(num.begin(), num.begin() + static_cast<std::ptrdiff_t>(shift));
    den.erase(den.begin(), den.begin() + static_cast<std::ptrdiff_t>(shift));
    require(same_poly(num, {-610115596992LL, 3854354403900LL, 759755266431LL, -7015097338690LL,
                            -3360079183489LL, 281046183404LL, 200914962101LL}),
            "numerator");
    const long long quad_a[] = {-70323, 69629, 110201};
    const long long quad_b[] = {-45187, 237699, 275135};
    long long product[5] = {};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) product[i + j] += quad_a[i] * quad_b[j];
    }
    require(same_poly(den, {0, 0, product[0], product[1], product[2], product[3], product[4]}), "denominator");
    require(61504580235LL * 169 - 411438267366LL == 9982835792349LL, "quartic gap");
    require(13 * 9982835792349LL - 429495755430LL == 129347369545107LL, "linear gap");
    require(110201LL * 169 - 70323 == 18553646, "quadratic one");
    require(275135LL * 169 - 45187 == 46452628, "quadratic two");
    require(6 * 200914962101LL == 1205489772606LL, "sixth derivative coefficient");
    require(5 * 281046183404LL == 1405230917020LL, "fifth derivative coefficient");
    require(4 * -3360079183489LL == -13440316733956LL, "fourth derivative coefficient");
    require(3 * -7015097338690LL == -21045292016070LL, "third derivative coefficient");
    require(2 * 759755266431LL == 1519510532862LL, "second derivative coefficient");
    require(30 * 200914962101LL == 6027448863030LL, "second derivative leading");
    require(98 * 61504580235LL == 6027448863030LL, "Q leading");
    require(98 * 15505209519LL == 1519510532862LL, "Q constant");
    long long n13 = 200914962101LL;
    const long long down[] = {281046183404LL, -3360079183489LL, -7015097338690LL,
        759755266431LL, 3854354403900LL, -610115596992LL};
    for (long long coeff : down) n13 = n13 * 13 + coeff;
    require(n13 == 962927132597336369LL, "N(13)");
    long long n1 = 1205489772606LL;
    const long long down1[] = {1405230917020LL, -13440316733956LL, -21045292016070LL,
        1519510532862LL, 3854354403900LL};
    for (long long coeff : down1) n1 = n1 * 13 + coeff;
    require(n1 == 454663292137321722LL, "N'(13)");
    long long n2 = 6027448863030LL;
    const long long down2[] = {5620923668080LL, -40320950201868LL, -42090584032140LL, 1519510532862LL};
    for (long long coeff : down2) n2 = n2 * 13 + coeff;
    require(n2 == 177139237609770940LL, "N''(13)");
}

Big pow10(int n) {
    Big r = Big::from_u64(1);
    for (int i = 0; i < n; ++i) r = r.mul_small(10);
    return r;
}

void check_defect() {
    Big left = Big::from_u64(184981).mul_small(420) * pow10(104);
    Big right_scale = pow10(26) - Big::from_u64(2);
    Big right_kick = Big::from_u64(160000) * pow10(80) - Big::from_u64(184981) * pow10(26);
    Big right = Big::from_u64(26) * right_scale * right_kick;
    require(left.cmp(right) < 0, "defect");
}

void check_sandwich() {
    std::vector<int> primes;
    for (int p = 3; p < 100; ++p) {
        if (is_prime(p)) primes.push_back(p);
    }
    std::vector<int> orders(101), kinds_code(101);
    for (int p : primes) {
        orders[p] = order_of(p);
        std::string kind = kind_of(p, orders[p]);
        kinds_code[p] = kind == "short" ? 0 : kind == "long" ? 1 : 2;
    }
    Rat five = Rat::frac(5, 7);
    Rat three = Rat::frac(3, 4);
    for (std::size_t i = 0; i < primes.size(); ++i) {
        for (std::size_t j = i + 1; j < primes.size(); ++j) {
            int p = primes[i], q = primes[j];
            int t = orders[p], s = orders[q];
            int g = t;
            int ss = s;
            while (ss) {
                int r = g % ss;
                g = ss;
                ss = r;
            }
            int order = t / g * s;
            int modulus = p * q;
            bool short_order = 12LL * order <= 5LL * modulus;
            bool seven = (p == 7 || q == 7) && !short_order;
            bool three_short = p == 3 && kinds_code[q] == 0 && !short_order;
            Rat alpha = Rat::make(Big::from_u64(2ULL * order), Big::from_u64(modulus));
            Rat beta = Rat::make(Big::from_u64(2ULL * t), Big::from_u64(modulus));
            Rat gamma = Rat::make(Big::from_u64(2ULL * s), Big::from_u64(modulus));
            Rat ups = Rat::frac(2, static_cast<std::uint64_t>(modulus));
            Rat a = (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(p) * p))
                * (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(q) * q));
            Rat b = (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(p) * p))
                / Rat::from_u64(static_cast<std::uint64_t>(q) * q);
            Rat c = (Rat::from_u64(1) - Rat::frac(1, static_cast<std::uint64_t>(q) * q))
                / Rat::from_u64(static_cast<std::uint64_t>(p) * p);
            Rat d = Rat::frac(1, static_cast<std::uint64_t>(modulus) * modulus);
            if (short_order || seven || three_short) {
                Rat lower = a * rl(alpha) + b * rl(beta) + c * rl(gamma);
                require(three < lower, "sandwich low");
            } else {
                Rat upper = a * ru(alpha) + b * ru(beta) + c * ru(gamma) + d * ru(ups);
                require(upper < five, "sandwich high");
            }
        }
    }
}

}  // namespace

int main() {
    try {
        require((Big::from_u64(100).cmp(Big::from_u64(7)) > 0), "cmp");
        auto split = Big::divmod(Big::from_u64(100), Big::from_u64(7));
        require(split.first.cmp(Big::from_u64(14)) == 0 && split.second.cmp(Big::from_u64(2)) == 0, "divmod");
        check_orders();
        check_arithmetic_and_tails();
        check_bounds();
        check_phi();
        check_defect();
        check_sandwich();
    } catch (const std::exception& ex) {
        std::cerr << "crt-composite-abel: " << ex.what() << "\n";
        return 1;
    }
    std::cout << "crt-composite-abel: pass\n";
    return 0;
}
