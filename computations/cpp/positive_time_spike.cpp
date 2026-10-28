// Independent integer certificate for BGS-TRACE-119.
// Recomputes the archimedean mode bound, the norm block at diameter 186,
// the gap comparison 4860 beta^5 < 1, the window activities, and the
// cleared Abel comparison at N = u_205. A pass does not prove BGS-TRACE-005.

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

    Big pow(std::uint64_t e) const {
        Big result = from_u64(1);
        Big base = *this;
        while (e) {
            if (e & 1U) result = result.mul(base);
            e >>= 1U;
            if (e) base = base.mul(base);
        }
        return result;
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

struct Pell {
    Big u, v;
};

std::vector<Pell> pell_through(int n) {
    std::vector<Pell> rows;
    rows.push_back({Big::from_u64(1), Big::from_u64(0)});
    Big u = Big::from_u64(1);
    Big v = Big::from_u64(0);
    for (int m = 1; m <= n; ++m) {
        Big u2 = u.add(v.mul_small(2));
        Big v2 = u.add(v);
        u = u2;
        v = v2;
        Big norm = u.mul(u);
        Big two_vv = v.mul(v).mul_small(2);
        int sign = (m % 2) ? -1 : 1;
        if (sign == 1) {
            if (norm.cmp(two_vv) <= 0 || norm.sub(two_vv).cmp(Big::from_u64(1)) != 0)
                throw std::runtime_error("pell norm");
        } else {
            if (two_vv.cmp(norm) <= 0 || two_vv.sub(norm).cmp(Big::from_u64(1)) != 0)
                throw std::runtime_error("pell norm");
        }
        rows.push_back({u, v});
    }
    return rows;
}

long long r_coeff(int k) {
    if (k == 0) return 1000;
    if (std::abs(k) == 1) return 500;
    if (std::abs(k) == 7) return -500;
    if (std::abs(k) == 6 || std::abs(k) == 8) return -250;
    return 0;
}

bool square_positive(long long a, long long b) {
    // a + b sqrt(2) > 0
    if (b >= 0) {
        if (a >= 0) return !(a == 0 && b == 0);
        return 2 * b * b > a * a;
    }
    return a > 0 && a * a > 2 * b * b;
}

bool abs_le_18(long long p, long long q) {
    long long aa = p * p + 2 * q * q - 324;
    long long bb = 2 * p * q;
    return !square_positive(aa, bb);
}

int mode_bound() {
    int count = 0;
    for (int k = -9; k <= 9; ++k) {
        for (int ell = -1; ell <= 1; ++ell) {
            long long re = 0, im = 0;
            if (ell == 0) {
                if (std::abs(k) == 7) re += 500000;
                re += r_coeff(k) * 100;
                im += (r_coeff(k + 1) - r_coeff(k - 1)) * 5;
                if (k == 0) re -= 100000;
            } else {
                long long rc = r_coeff(k);
                re = rc * -3;
                im = rc * (ell == 1 ? -4 : 4);
            }
            if (re == 0 && im == 0) continue;
            ++count;
            if (!abs_le_18(2L * k, ell) || !abs_le_18(2L * k, -ell))
                throw std::runtime_error("mode exceeds 18");
        }
    }
    if (count != 32) throw std::runtime_error("mode count");
    return count;
}

void pigeonhole() {
    int worst = 0;
    for (int m = 1; m <= 11; ++m) {
        int ceiling = (205 + m - 1) / m;
        if ((ceiling - 1) * m >= 205 || ceiling * m < 205)
            throw std::runtime_error("ceiling");
        worst = std::max(worst, 205 - ceiling);
    }
    if (worst != 186) throw std::runtime_error("pigeonhole");
}

void norm_block(const std::vector<Pell>& rows) {
    const Big& u = rows[372].u;
    const Big& v = rows[372].v;
    const Big& capital = rows[205].u;
    Big c = Big::from_u64(198ULL * 198ULL);
    Big left = capital.mul(capital).mul_small(2);
    if (c.mul(u).cmp(left) >= 0) throw std::runtime_error("norm side");
    Big diff = left.sub(c.mul(u));
    Big rhs = c.mul(v);
    rhs = rhs.mul(rhs).mul_small(2);
    if (diff.mul(diff).cmp(rhs) <= 0) throw std::runtime_error("norm block");
}

void gap_block(const std::vector<Pell>& rows) {
    if (rows[10].u.cmp(Big::from_u64(3363)) != 0 || rows[10].v.cmp(Big::from_u64(2378)) != 0)
        throw std::runtime_error("pell 10");
    Big c = Big::from_u64(4860);
    Big right = c.mul(rows[10].u).sub(Big::from_u64(1));
    Big left = c.mul(rows[10].v);
    left = left.mul(left).mul_small(2);
    if (left.cmp(right.mul(right)) <= 0) throw std::runtime_error("gap");
    int worst = 0;
    for (int k = 1; k <= 10; ++k)
        for (int t = 1; t <= 11 - k; ++t)
            worst = std::max(worst, k * t);
    if (worst != 30) throw std::runtime_error("KT");
}

std::uint64_t upow(std::uint64_t a, int e) {
    std::uint64_t r = 1;
    for (int i = 0; i < e; ++i) r *= a;
    return r;
}

std::uint64_t factorial(int n) {
    std::uint64_t r = 1;
    for (int i = 2; i <= n; ++i) r *= static_cast<std::uint64_t>(i);
    return r;
}

void activity(const Big& capital) {
    const std::uint64_t bnum = 184981ULL;
    const std::uint64_t bden = 160000ULL;
    Big ten = Big::from_u64(10);
    Big scale = capital.mul_small(bnum);
    // x < 7/2: 410 * N * bNum < 7 * bDen * 10^80
    Big left = capital.mul_small(410ULL * bnum);
    Big right = ten.pow(80).mul_small(7ULL * bden);
    if (left.cmp(right) >= 0) throw std::runtime_error("x scale");

    // Phi2 < 9/100: 61500 (N bNum)^2 < 18 * 10^160 * bDen^2
    Big phi2_left = scale.mul(scale).mul_small(61500);
    Big phi2_right = ten.pow(160).mul_small(bden).mul_small(bden).mul_small(18);
    if (phi2_left.cmp(phi2_right) >= 0) throw std::runtime_error("phi2");

    Big num = Big::from_u64(0);
    const std::uint64_t fact11 = factorial(11);
    for (int m = 3; m <= 11; ++m) {
        // 205*(41^11 - 40^11) does not fit in uint64, so the window
        // difference is computed in the base-10^9 type.
        const auto w = static_cast<std::uint64_t>(4 * (m - 1) + 1);
        Big comb = Big::from_u64(w).pow(static_cast<std::uint64_t>(m));
        comb = comb.sub(Big::from_u64(w - 1).pow(static_cast<std::uint64_t>(m)));
        Big term = Big::from_u64(205).mul(comb).mul(scale.pow(static_cast<std::uint64_t>(m)));
        term = term.mul_small(fact11 / factorial(m));
        term = term.mul(ten.pow(static_cast<std::uint64_t>(80 * (11 - m))));
        term = term.mul(Big::from_u64(bden).pow(static_cast<std::uint64_t>(11 - m)));
        num = num.add(term);
    }
    Big den = Big::from_u64(fact11).mul(ten.pow(880)).mul(Big::from_u64(bden).pow(11));
    if (num.mul_small(23).cmp(den) >= 0) throw std::runtime_error("phi3");

    // 100 * 7^12 * 26 < 12! * 2^12 * 19
    std::uint64_t tleft = 100ULL * upow(7, 12) * 26ULL;
    std::uint64_t tright = factorial(12) * upow(2, 12) * 19ULL;
    if (tleft >= tright) throw std::runtime_error("tail");
    if (!(9 * 23 + 100 < 7 * 46 && 12 * 2097 < 32890))
        throw std::runtime_error("coarse chain");
}

void abel(const Big& capital) {
    Big ten = Big::from_u64(10);
    Big den = ten.pow(166).mul_small(8);
    Big num = capital.mul(capital).mul_small(205ULL * 1650797ULL);
    Big eleven = den.mul_small(11);
    Big twelve_num = num.mul_small(12);
    if (eleven.cmp(twelve_num) <= 0) throw std::runtime_error("center");
    Big gap = eleven.sub(twelve_num);
    Big left = capital.sub(Big::from_u64(410)).mul_small(4).mul(gap).mul(gap);
    Big twelve_den = den.mul_small(12);
    Big right = capital.mul_small(3).mul(twelve_den).mul(twelve_den);
    if (left.cmp(right) <= 0) throw std::runtime_error("abel");
}

}  // namespace

int main() {
    try {
        int modes = mode_bound();
        pigeonhole();
        auto rows = pell_through(372);
        norm_block(rows);
        gap_block(rows);
        activity(rows[205].u);
        abel(rows[205].u);
        std::cout << "positive_time_spike passed u_205_digits="
                  << rows[205].u.decimal().size()
                  << " modes=" << modes << " gap<=4 error<1/12\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "positive_time_spike failed: " << ex.what() << "\n";
        return 1;
    }
}
