// C++ check with __int128 (no boost on this VM) for Pell C1, m up to 30.
// (1+sqrt2)^m = u + v*sqrt2 ; x,y from x_{n+1}=3x+8y, y_{n+1}=x+3y, x0=1,y0=0.
// Checks: u^2-2v^2=(-1)^m, D=2(x-1), gp = 2u (odd m) or 4v (even m),
// D=gp^2 (odd) or 2D=gp^2 (even).
#include <iostream>
#include <string>
#include <algorithm>
using i128 = __int128_t;
std::string str(i128 v) {
  if (v == 0) return "0";
  bool neg = v < 0; if (neg) v = -v;
  std::string s; while (v > 0) { s.push_back('0' + int(v % 10)); v /= 10; }
  if (neg) s.push_back('-');
  std::reverse(s.begin(), s.end()); return s;
}
int main() {
  i128 u = 1, v = 0, x = 1, y = 0;
  for (int m = 1; m <= 30; ++m) {
    i128 nu = u + 2*v, nv = u + v; u = nu; v = nv;
    i128 nx = 3*x + 8*y, ny = x + 3*y; x = nx; y = ny;
    i128 norm = u*u - 2*v*v;
    i128 expected_norm = (m % 2 == 1) ? i128(-1) : i128(1);
    i128 D = 2*(x - 1);
    i128 gp = (m % 2 == 1) ? 2*u : 4*v;
    bool ok = (norm == expected_norm) &&
              ((m % 2 == 1) ? (D == gp*gp) : (2*D == gp*gp));
    if (!ok) { std::cout << "FAIL m=" << m << "\n"; return 1; }
    std::cout << "m=" << m << " D=" << str(D) << " gp=" << str(gp) << " OK\n";
  }
  std::cout << "ALL C++ CHECKS PASS m=1..30\n";
  return 0;
}
