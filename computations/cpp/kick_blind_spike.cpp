// Independent integer certificate for BGS-TRACE-117.
// Recomputes u_n through n=203, the Fourier majorant, the uniform rational
// comparison, and the direct Abel gap at every odd n from 5 through 201.
// The direct gap at n=203 is required to fail while rho stays below 1.
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
    std::vector<std::uint32_t> d{0};  // little-endian, base 10^9

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

    bool odd() const { return (d[0] % 2U) != 0U; }

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
            carry += (i < d.size() ? d[i] : 0);
            carry += (i < o.d.size() ? o.d[i] : 0);
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
                - (i < o.d.size() ? o.d[i] : 0);
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
        r.d.assign(d.size() + 3, 0);
        std::uint64_t carry = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            carry += static_cast<std::uint64_t>(d[i]) * m;
            r.d[i] = static_cast<std::uint32_t>(carry % BASE);
            carry /= BASE;
        }
        std::size_t i = d.size();
        while (carry) {
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
                if (j < o.d.size())
                    cur += static_cast<std::uint64_t>(d[i]) * o.d[j];
                r.d[i + j] = static_cast<std::uint32_t>(cur % BASE);
                carry = cur / BASE;
            }
        }
        r.trim();
        return r;
    }

    std::string decimal() const {
        if (is_zero()) return "0";
        Big x = *this;
        std::string rev;
        while (!x.is_zero()) {
            std::uint64_t rem = 0;
            for (std::size_t i = x.d.size(); i-- > 0;) {
                std::uint64_t cur = rem * BASE + x.d[i];
                x.d[i] = static_cast<std::uint32_t>(cur / 10);
                rem = cur % 10;
            }
            x.trim();
            rev.push_back(static_cast<char>('0' + rem));
        }
        return std::string(rev.rbegin(), rev.rend());
    }
};

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
};

std::uint64_t isqrt_u64(std::uint64_t n) {
    if (n < 2) return n;
    std::uint64_t x = 1;
    while (x < n && x <= (n / x)) {
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

Big pow10(int e) {
    Big r = Big::from_u64(1);
    for (int i = 0; i < e; ++i) r = r.mul_small(10);
    return r;
}

const Big& x_den() {
    static Big den = pow10(80).mul_small(160000);
    return den;
}

bool rho_contractive(const Big& capital_n, int n) {
    return x_den().cmp(capital_n.mul_small(184981).mul_small(static_cast<std::uint64_t>(n + 1))) > 0;
}

bool direct_gap(const Big& capital_n, int n) {
    if (!rho_contractive(capital_n, n)) return false;
    Big x_num = capital_n.mul_small(184981);
    Big num = x_den().sub(x_num.mul_small(static_cast<std::uint64_t>(n + 1)));
    Big den = x_den().sub(x_num);
    Big left = num.mul(num).mul_small(4).mul(capital_n.sub(Big::from_u64(static_cast<std::uint64_t>(2 * n))));
    Big right = den.mul(den).mul(capital_n).mul_small(3);
    return left.cmp(right) > 0;
}

}  // namespace

int main() {
    try {
        std::vector<Big> us;
        us.push_back(Big::from_u64(1));
        Big u = Big::from_u64(1), v = Big::from_u64(0);
        for (int m = 1; m <= 203; ++m) {
            Big nu = u.add(v.mul_small(2));
            Big nv = u.add(v);
            u = std::move(nu);
            v = std::move(nv);
            Big uu = u.mul(u);
            Big two_vv = v.mul(v).mul_small(2);
            if (m % 2) {
                if (uu.add(Big::from_u64(1)).cmp(two_vv) != 0)
                    throw std::runtime_error("odd norm");
            } else if (uu.sub(Big::from_u64(1)).cmp(two_vv) != 0) {
                throw std::runtime_error("even norm");
            }
            if (!u.odd()) throw std::runtime_error("u parity");
            us.push_back(u);
            if (m >= 3) {
                Big pred = us[m - 2].mul_small(5).add(us[m - 3].mul_small(2));
                if (pred.cmp(us[m]) != 0) throw std::runtime_error("recurrence identity");
            }
        }
        if (us[5].cmp(Big::from_u64(41)) != 0 || us[7].cmp(Big::from_u64(239)) != 0)
            throw std::runtime_error("base values");
        const std::string dec = us[201].decimal();
        if (dec.size() != 77 || (dec.back() - '0') % 2 == 0)
            throw std::runtime_error("u_201 digits or parity");

        Frac total = Frac::make(0, 1);
        int count = 0;
        bool saw70 = false;
        for (int k = -9; k <= 9; ++k) {
            for (int ell = -1; ell <= 1; ++ell) {
                auto [re, im] = f_coeff(k, ell);
                if (re.n == 0 && im.n == 0) continue;
                ++count;
                Frac mag2 = re * re + im * im;
                if (mag2.d <= 0 || mag2.n < 0) throw std::runtime_error("mag2");
                __int128 pq = mag2.n * mag2.d;
                if (pq > static_cast<__int128>(~0ULL))
                    throw std::runtime_error("mag2 does not fit uint64");
                std::uint64_t root = isqrt_u64(static_cast<std::uint64_t>(pq));
                Frac upper = Frac::make(static_cast<__int128>(root) + 1, mag2.d);
                total = total + upper;
                if (k == 7 && ell == 0) {
                    if (!(re.n == 9 && re.d == 20 && im.n == 0))
                        throw std::runtime_error("mode (7,0)");
                    saw70 = true;
                }
            }
        }
        if (count != 32 || !saw70) throw std::runtime_error("mode count");
        if (!(total.n == 184981 && total.d == 160000))
            throw std::runtime_error("majorant");

        int odd_count = 0;
        for (int n = 5; n <= 201; n += 2) {
            if (!direct_gap(us[n], n)) throw std::runtime_error("direct gap");
            ++odd_count;
            if (n < 201) {
                if (us[n].mul_small(static_cast<std::uint64_t>(n + 2)).cmp(
                        us[n + 2].mul_small(static_cast<std::uint64_t>(n))) >= 0)
                    throw std::runtime_error("delta not decreasing");
                Big x_n = us[n].mul_small(184981);
                Big x_p = us[n + 2].mul_small(184981);
                Big left = x_n.mul_small(static_cast<std::uint64_t>(n)).mul(x_den().sub(x_p));
                Big right = x_p.mul_small(static_cast<std::uint64_t>(n + 2)).mul(x_den().sub(x_n));
                if (left.cmp(right) >= 0) throw std::runtime_error("rho not increasing");
            }
        }
        if (odd_count != 99) throw std::runtime_error("odd count");

        Big x_num = us[201].mul_small(184981);
        if (x_den().cmp(x_num.mul_small(202)) <= 0) throw std::runtime_error("rho_201");
        Big num = x_den().sub(x_num.mul_small(202));
        Big den = x_den().sub(x_num);
        if (num.mul(num).mul_small(300).cmp(den.mul(den).mul_small(239)) <= 0)
            throw std::runtime_error("uniform gap");

        Big x5 = Big::from_u64(41ULL * 184981ULL);
        if (x_den().cmp(x5.mul_small(6)) <= 0) throw std::runtime_error("rho_5");
        Big num5 = x_den().sub(x5.mul_small(6));
        Big den5 = x_den().sub(x5);
        if (num5.mul(num5).mul_small(124).cmp(den5.mul(den5).mul_small(123)) <= 0)
            throw std::runtime_error("n5 gap");

        if (!rho_contractive(us[203], 203) || direct_gap(us[203], 203))
            throw std::runtime_error("sentinel 203");

        std::cout << "kick_blind_spike passed u_201_digits=" << dec.size()
                  << " odd_n=5..201 count=" << odd_count
                  << " majorant=184981/160000 sentinel_203=below\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "kick_blind_spike failed: " << ex.what() << "\n";
        return 1;
    }
}
