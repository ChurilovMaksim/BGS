// Independent integer certificate for BGS-TRACE-118.
// Recomputes the Fourier mass, the support resonances modulo u_203,
// the cleared quadrature gap, and the vacuous remainder at n=205.
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
                if (j < o.d.size())
                    cur += static_cast<std::uint64_t>(d[i]) * o.d[j];
                r.d[i + j] = static_cast<std::uint32_t>(cur % BASE);
                carry = cur / BASE;
            }
        }
        r.trim();
        return r;
    }

    Big mod(const Big& n) const {
        if (n.is_zero()) throw std::runtime_error("mod 0");
        if (cmp(n) < 0) return *this;
        Big rem = from_u64(0);
        for (std::size_t i = d.size(); i-- > 0;) {
            Big cur = rem.mul_small(BASE).add(from_u64(d[i]));
            std::uint64_t lo = 0, hi = static_cast<std::uint64_t>(BASE) + 2;
            while (lo + 1 < hi) {
                std::uint64_t mid = lo + (hi - lo) / 2;
                if (n.mul_small(mid).cmp(cur) <= 0) lo = mid;
                else hi = mid;
            }
            rem = cur.sub(n.mul_small(lo));
            if (rem.cmp(n) >= 0) throw std::runtime_error("mod reduction failed");
        }
        return rem;
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

Big add_mod(const Big& a, const Big& b, const Big& n) {
    Big s = a.add(b);
    if (s.cmp(n) >= 0) s = s.sub(n);
    if (s.cmp(n) >= 0) s = s.sub(n);
    return s;
}

Big mul_int_mod(const Big& a, int k, const Big& n) {
    if (k == 0 || a.is_zero()) return Big::from_u64(0);
    int ak = k < 0 ? -k : k;
    Big p = a.mul_small(static_cast<std::uint64_t>(ak));
    p = p.mod(n);
    if (k < 0 && !p.is_zero()) p = n.sub(p);
    return p;
}

bool is_neg(const Big& x, int k2, const Big& n) {
    if (k2 == 0) return x.is_zero();
    if (k2 > 0) return x.cmp(n.sub(Big::from_u64(static_cast<std::uint64_t>(k2)))) == 0;
    return x.cmp(Big::from_u64(static_cast<std::uint64_t>(-k2))) == 0;
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

    static __int128 safemul(__int128 a, __int128 b) {
        if (a == 0 || b == 0) return 0;
        bool neg = (a < 0) != (b < 0);
        if (a < 0) a = -a;
        if (b < 0) b = -b;
        const unsigned __int128 limit = (static_cast<unsigned __int128>(1) << 127) - 1;
        auto ua = static_cast<unsigned __int128>(a);
        auto ub = static_cast<unsigned __int128>(b);
        if (ub != 0 && ua > limit / ub)
            throw std::runtime_error("int128 overflow");
        __int128 p = a * b;
        return neg ? -p : p;
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

    Frac operator+(Frac o) const {
        __int128 g = igcd(d, o.d);
        __int128 d1 = d / g;
        __int128 d2 = o.d / g;
        return make(safemul(n, d2) + safemul(o.n, d1), safemul(d1, o.d));
    }
    Frac operator-(Frac o) const {
        __int128 g = igcd(d, o.d);
        __int128 d1 = d / g;
        __int128 d2 = o.d / g;
        return make(safemul(n, d2) - safemul(o.n, d1), safemul(d1, o.d));
    }
    Frac operator*(Frac o) const { return make(safemul(n, o.n), safemul(d, o.d)); }
    Frac operator/(Frac o) const { return make(safemul(n, o.d), safemul(d, o.n)); }
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

Big pow_small(std::uint64_t base, int e) {
    Big r = Big::from_u64(1);
    for (int i = 0; i < e; ++i) r = r.mul_small(base);
    return r;
}

}  // namespace

int main() {
    try {
        if (104 * 104 * 2 <= 128 * 128) throw std::runtime_error("archimedean");
        if (34 - 24 != 10 || -17 + 24 != 7) throw std::runtime_error("expansion");

        std::vector<std::pair<int, int>> box_hits;
        for (int k = -9; k <= 9; ++k) {
            for (int ell = -1; ell <= 1; ++ell) {
                int ck = 3 * k + 2 * ell;
                int cl = 4 * k + 3 * ell;
                if (ck >= -9 && ck <= 9 && cl >= -1 && cl <= 1)
                    box_hits.push_back({k * 10 + ell, ck * 10 + cl});
            }
        }
        if (box_hits.size() != 3) throw std::runtime_error("lag-one box count");

        Frac total = Frac::make(0, 1);
        Frac sigma = Frac::make(0, 1);
        int count = 0;
        bool saw70 = false;
        std::vector<std::pair<int, int>> modes;
        for (int k = -9; k <= 9; ++k) {
            for (int ell = -1; ell <= 1; ++ell) {
                auto [re, im] = f_coeff(k, ell);
                auto [cre, cim] = f_coeff(-k, -ell);
                if (cre.n != re.n || cre.d != re.d || cim.n != -im.n || cim.d != im.d)
                    throw std::runtime_error("hermitian");
                if (re.n == 0 && im.n == 0) continue;
                ++count;
                modes.push_back({k, ell});
                Frac mag2 = re * re + im * im;
                sigma = sigma + mag2;
                __int128 pq = Frac::safemul(mag2.n, mag2.d);
                if (pq < 0 || pq > static_cast<__int128>(~0ULL))
                    throw std::runtime_error("mag2 range");
                std::uint64_t root = isqrt_u64(static_cast<std::uint64_t>(pq));
                total = total + Frac::make(static_cast<__int128>(root) + 1, mag2.d);
                if (k == 7 && ell == 0) {
                    if (!(re.n == 9 && re.d == 20 && im.n == 0))
                        throw std::runtime_error("mode (7,0)");
                    saw70 = true;
                }
            }
        }
        if (count != 32 || !saw70) throw std::runtime_error("mode count");
        if (!(total.n == 184981 && total.d == 160000)) throw std::runtime_error("majorant");
        if (!(sigma.n == 66033 && sigma.d == 160000)) throw std::runtime_error("sigma");

        auto [r11, i11] = f_coeff(1, 1);
        auto [rm11, im11] = f_coeff(-1, 1);
        auto [rm1m1, im1m1] = f_coeff(-1, -1);
        auto [r1m1, i1m1] = f_coeff(1, -1);
        auto mul = [](Frac ar, Frac ai, Frac br, Frac bi) {
            return std::pair<Frac, Frac>{ar * br - ai * bi, ar * bi + ai * br};
        };
        auto p1 = mul(r11, i11, rm11, im11);
        auto p2 = mul(rm1m1, im1m1, r1m1, i1m1);
        Frac gre = p1.first + p2.first;
        Frac gim = p1.second + p2.second;
        if (gim.n != 0 || gre.n != -7 || gre.d != 2000000)
            throw std::runtime_error("hand gamma");
        Frac sigma_eff = sigma + gre + gre;
        if (!(sigma_eff.n == 1650797 && sigma_eff.d == 4000000))
            throw std::runtime_error("sigma_eff");

        std::vector<Big> us, vs;
        us.push_back(Big::from_u64(1));
        vs.push_back(Big::from_u64(0));
        Big u = Big::from_u64(1), v = Big::from_u64(0);
        for (int m = 1; m <= 410; ++m) {
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
            vs.push_back(v);
        }
        if (us[5].cmp(Big::from_u64(41)) || us[7].cmp(Big::from_u64(239))
            || us[9].cmp(Big::from_u64(1393)))
            throw std::runtime_error("bases");

        const Big& N = us[203];
        if (!(Big::from_u64(10).mul(us[200]).add(Big::from_u64(9)).cmp(N) < 0))
            throw std::runtime_error("size X 100");
        if (!(us[200].add(vs[200].mul_small(18)).add(Big::from_u64(1)).cmp(N) < 0))
            throw std::runtime_error("size Y 100");
        if (!(us[202].mul_small(9).add(vs[202]).add(Big::from_u64(9)).cmp(N.mul_small(5)) < 0))
            throw std::runtime_error("size X 101");
        if (!(us[202].add(vs[202].mul_small(18)).add(Big::from_u64(1)).cmp(N.mul_small(6)) < 0))
            throw std::runtime_error("size Y 101");
        if (N.cmp(Big::from_u64(326)) <= 0) throw std::runtime_error("u_203 small");

        if (us[406].sub(Big::from_u64(1)).mod(N).is_zero() == false
            || !vs[406].mod(N).is_zero())
            throw std::runtime_error("C^n not I");

        std::vector<Big> umod(405), vmod(405);
        for (int m = 0; m <= 404; ++m) {
            umod[m] = us[m].mod(N);
            vmod[m] = vs[m].mod(N);
        }
        int hits = 0;
        for (int r = 1; r <= 202; ++r) {
            Frac gr = Frac::make(0, 1), gi = Frac::make(0, 1);
            const Big& uu = umod[2 * r];
            const Big& vv = vmod[2 * r];
            for (auto [k, ell] : modes) {
                Big x = add_mod(mul_int_mod(uu, k, N), mul_int_mod(vv, ell, N), N);
                Big y = add_mod(mul_int_mod(uu, ell, N), mul_int_mod(vv, 2 * k, N), N);
                for (auto [k2, ell2] : modes) {
                    if (!is_neg(x, k2, N) || !is_neg(y, ell2, N)) continue;
                    ++hits;
                    auto [rw, iw] = f_coeff(k, ell);
                    auto [rv, iv] = f_coeff(k2, ell2);
                    gr = gr + (rv * rw - iv * iw);
                    gi = gi + (rv * iw + iv * rw);
                }
            }
            if (r != 1 && r != 202) {
                if (gr.n != 0 || gi.n != 0) throw std::runtime_error("unexpected gamma");
            } else if (gi.n != 0 || gr.n != -7 || gr.d != 2000000) {
                throw std::runtime_error("endpoint gamma");
            }
        }
        if (hits != 4) throw std::runtime_error("hit count");

        const int n = 203;
        Big den2 = pow10(166).mul_small(8);
        Big num2 = N.mul(N).mul_small(1650797).mul_small(n);
        Big den3 = pow10(240).mul_small(6).mul(Big::from_u64(160000).mul(Big::from_u64(160000)).mul(Big::from_u64(160000)));
        Big num3 = N.mul(N).mul(N).mul_small(184981).mul_small(184981).mul_small(184981)
                       .mul_small(n).mul_small(n).mul_small(n);
        Big scale = pow_small(2, 96).mul(pow_small(5, 86)).mul_small(3);
        if (scale.mul(den2).cmp(den3) != 0) throw std::runtime_error("scale");
        Big num_e = num2.mul(scale).add(num3);
        if (den3.cmp(num_e) <= 0) throw std::runtime_error("eps>=1");
        Big gap_l = den3.sub(num_e);
        gap_l = gap_l.mul(gap_l).mul_small(4).mul(N.sub(Big::from_u64(406)));
        Big gap_r = den3.mul(den3).mul(N).mul_small(3);
        if (gap_l.cmp(gap_r) <= 0) throw std::runtime_error("quadrature gap");

        Big xden = pow10(80).mul_small(160000);
        Big xnum = N.mul_small(184981);
        bool one_term = false;
        if (xden.cmp(xnum.mul_small(204)) > 0) {
            Big a = xden.sub(xnum.mul_small(204));
            Big b = xden.sub(xnum);
            Big left = a.mul(a).mul_small(4).mul(N.sub(Big::from_u64(406)));
            Big right = b.mul(b).mul(N).mul_small(3);
            one_term = left.cmp(right) > 0;
        }
        if (one_term) throw std::runtime_error("one-term still beats 3/4");

        Big u205 = us[205];
        Big sent_l = u205.mul(u205).mul(u205).mul_small(205).mul_small(205).mul_small(205)
                         .mul_small(184981).mul_small(184981).mul_small(184981);
        Big sent_r = pow10(240).mul_small(6).mul(Big::from_u64(160000).mul(Big::from_u64(160000)).mul(Big::from_u64(160000)));
        if (sent_l.cmp(sent_r) < 0) throw std::runtime_error("sentinel not vacuous");

        if (!(N.mul(N).mul_small(1650797).mul_small(203).mul_small(1000).cmp(pow10(166).mul_small(8)) < 0))
            throw std::runtime_error("coarse eps2");
        Big c3l = N.mul(N).mul(N).mul_small(203).mul_small(203).mul_small(203)
                      .mul_small(184981).mul_small(184981).mul_small(184981).mul_small(25);
        Big c3r = pow10(240).mul_small(6).mul(Big::from_u64(160000).mul(Big::from_u64(160000)).mul(Big::from_u64(160000)));
        if (c3l.cmp(c3r) >= 0) throw std::runtime_error("coarse eps3");
        if (N.cmp(Big::from_u64(406000)) <= 0) throw std::runtime_error("coarse delta");
        // 4*999*959^2 > 3*1000^3
        unsigned long long coarse_l = 4ULL * 999ULL * 959ULL * 959ULL;
        unsigned long long coarse_r = 3ULL * 1000ULL * 1000ULL * 1000ULL;
        if (coarse_l <= coarse_r) throw std::runtime_error("coarse product");

        std::cout << "orbit_orthogonal_spike passed u_203_digits=" << N.decimal().size()
                  << " hits=4 gamma=-7/2000000 quadrature=above one_term=below sentinel_205=vacuous\n";
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "orbit_orthogonal_spike failed: " << ex.what() << "\n";
        return 1;
    }
}
