// Independent C++ reconstruction and replay for the resonance
// nondegeneracy certificate (BGS-RES-022), written from the specification in
// mathematics/resonance_nondegeneracy_and_hessian.md, Sections 2.1--2.3.
//
// Construction mode:
//   resonance_complex_replay <radius>
// prints {"modes": ..., "rows": ...} as JSON on stdout, reconstructing the
// orbit equations of (5)--(6) independently. Frequencies are canonicalized
// by the quadratic-ring window method of Section 2.2: for a frequency
// k = (x, y) put beta = y + x*sqrt(2) in Q(sqrt(2)); under T^j the
// beta-coordinate is lambda^j * beta with lambda = 3 + 2*sqrt(2), so the
// energy (7) is enumerated exactly over the window -16 <= j <= 16 and the
// (energy, lexicographic) minimum over the signed orbit is the
// representative. The program fails closed if a minimizer sits at the
// window boundary. A contribution whose frequency reaches the
// representative with the negative orientation bit belongs to the
// conjugate orbit (Section 2.2) and is not accumulated; the two
// orientations contribute conjugate orbit sums in (1), which is the
// factor 2 in (6).
//
// Replay mode:
//   resonance_complex_replay <radius> --proof <file>
// parses the RESONANCE_COMPLEX_V1 text serialization and replays it
// against the self-constructed rows under the four rules of Section 2.3
// (P: sole surviving cross monomial records a zero product; S: a sole
// square or a sign-definite Hermitian-square sum kills its variables;
// D: a recorded zero product with a currently assumed nonzero factor
// kills the other factor; F: a temporary nonzero assumption whose child
// reaches an actual contradiction kills the pivot). It prints
// {"status": "PASS", "rules": {...}} only if every variable is
// eliminated. Any malformed stream, inadmissible deduction, or
// incomplete elimination exits nonzero.
//
// All arithmetic is exact (boost::multiprecision::cpp_int); orbit
// energies reach ~10^29 inside the window. No floating point is used.
// Scope: exact coefficient construction and real-algebra proof replay
// for the fixed Pell matrix T = [[3, 2], [4, 3]]; no BGS claim.

#include <boost/multiprecision/cpp_int.hpp>

#include <algorithm>
#include <array>
#include <climits>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;

namespace {

[[noreturn]] void fail(const std::string& message) {
  std::cerr << "resonance_complex_replay: " << message << '\n';
  std::exit(1);
}

// ---------------------------------------------------------------------
// Exact arithmetic in Q(sqrt(2)): an element is p + q*sqrt(2).
// ---------------------------------------------------------------------
struct Ring {
  cpp_int p;  // rational part
  cpp_int q;  // sqrt(2) coefficient
};

Ring ring_mul(const Ring& a, const Ring& b) {
  return {a.p * b.p + 2 * a.q * b.q, a.p * b.q + a.q * b.p};
}

// lambda^j for j in [-16, 16]; lambda = 3 + 2 sqrt(2) has norm 1, so
// lambda^{-j} is the conjugate of lambda^j.
std::array<Ring, 33> lambda_powers() {
  std::array<Ring, 33> powers;
  const Ring lambda{3, 2};
  powers[16] = Ring{1, 0};
  for (int j = 1; j <= 16; ++j) powers[16 + j] = ring_mul(powers[16 + j - 1], lambda);
  for (int j = 1; j <= 16; ++j) {
    const Ring& pos = powers[16 + j];
    powers[16 - j] = Ring{pos.p, -pos.q};
  }
  return powers;
}

using Vec = std::pair<long long, long long>;  // a frequency (x, y)

long long to_ll(const cpp_int& value, const char* what) {
  if (value > cpp_int(LLONG_MAX) || value < cpp_int(LLONG_MIN))
    fail(std::string("integer overflow converting ") + what);
  return value.convert_to<long long>();
}

// ---------------------------------------------------------------------
// Signed-orbit canonicalization by the window method of Section 2.2.
// Returns {representative, orientation}: the representative is the
// (energy, lexicographic) minimum over {+-T^j k : -16 <= j <= 16}, and
// the orientation is +1 when the representative lies in the oriented
// orbit of k, -1 when it lies in the conjugate orbit. Fails closed if
// an energy minimizer sits at the window boundary.
// ---------------------------------------------------------------------
std::pair<Vec, int> canonicalize(Vec k, const std::array<Ring, 33>& powers) {
  const Ring beta{k.second, k.first};  // beta = y + x sqrt(2)
  struct Candidate {
    cpp_int energy;
    Vec v;
    int j;
  };
  std::vector<Candidate> candidates;
  candidates.reserve(33);
  cpp_int best_energy;
  bool have_best = false;
  for (int j = -16; j <= 16; ++j) {
    const Ring bj = ring_mul(powers[16 + j], beta);
    // For a vector (X, Y), beta = Y + X sqrt(2); hence T^j k has
    // X = sqrt(2)-coefficient of lambda^j beta, Y = its rational part.
    const cpp_int energy = 2 * bj.q * bj.q + bj.p * bj.p;  // 2 X^2 + Y^2, eq. (7)
    candidates.push_back(
        {energy, {to_ll(bj.q, "orbit coordinate"), to_ll(bj.p, "orbit coordinate")}, j});
    if (!have_best || energy < best_energy) {
      best_energy = energy;
      have_best = true;
    }
  }
  Vec representative{0, 0};
  bool have_rep = false;
  for (const Candidate& c : candidates) {
    if (c.energy != best_energy) continue;
    if (c.j == 16 || c.j == -16)
      fail("orbit energy minimizer at the window boundary");
    for (int sign = 0; sign < 2; ++sign) {
      const Vec v = sign == 0 ? c.v : Vec{-c.v.first, -c.v.second};
      if (!have_rep || v < representative) {
        representative = v;
        have_rep = true;
      }
    }
  }
  int orientation = 0;
  for (const Candidate& c : candidates) {
    if (c.v == representative) orientation = 1;
    if (Vec{-c.v.first, -c.v.second} == representative) {
      if (orientation == 1) fail("frequency lies in both oriented orbits");
      orientation = -1;
    }
  }
  if (orientation == 0) fail("canonical representative not attained");
  return {representative, orientation};
}

// ---------------------------------------------------------------------
// Coefficient construction from (5)--(6).
// A term is (i, e, j, f, a): the coefficient a of z_i^e z_j^f, where the
// exponent sign +1 denotes the variable and -1 its conjugate. For an
// ordered pair of modes (u, v) and signs (e, f), the bracket
// coefficient (5) at the frequency e*u + f*T*v carries the monomial
// z_i^e z_j^f with coefficient -e*f*det(u, T*v).
// ---------------------------------------------------------------------
struct System {
  std::vector<Vec> modes;
  // Rows keyed by orbit representative, in lexicographic key order.
  std::vector<Vec> keys;
  std::vector<std::vector<std::array<long long, 5>>> rows;
};

System construct(int radius) {
  const std::array<Ring, 33> powers = lambda_powers();
  System system;
  for (long long a = 0; a <= radius; ++a)
    for (long long b = -radius; b <= radius; ++b)
      if (a > 0 || b > 0) system.modes.push_back({a, b});
  const int n = static_cast<int>(system.modes.size());
  // Terms are accumulated per row in a map keyed by the monomial with its
  // two factors in nondecreasing (variable, exponent) order: a monomial
  // is a commutative product, so this is the canonical serialization of
  // the polynomial (6), and the two spellings of one monomial merge.
  std::map<Vec, std::map<std::array<long long, 4>, long long>> by_key;
  for (int i = 0; i < n; ++i) {
    const Vec u = system.modes[i];
    for (int j = 0; j < n; ++j) {
      const Vec v = system.modes[j];
      const Vec w{3 * v.first + 2 * v.second, 4 * v.first + 3 * v.second};  // T v
      const long long det = u.first * w.second - u.second * w.first;
      if (det == 0) continue;
      for (int e : {1, -1}) {
        for (int f : {1, -1}) {
          const Vec k{e * u.first + f * w.first, e * u.second + f * w.second};
          const auto [rep, orientation] = canonicalize(k, powers);
          if (orientation < 0) continue;  // conjugate orbit, see header
          const long long coef = -static_cast<long long>(e * f) * det;
          std::array<long long, 4> monomial{i, e, j, f};
          if (std::pair<long long, long long>(j, f) <
              std::pair<long long, long long>(i, e))
            monomial = {j, f, i, e};
          by_key[rep][monomial] += coef;
        }
      }
    }
  }
  for (auto& [key, term_map] : by_key) {
    std::vector<std::array<long long, 5>> terms;
    for (const auto& [monomial, coef] : term_map) {
      if (coef == 0) continue;
      terms.push_back({monomial[0], monomial[1], monomial[2], monomial[3], coef});
    }
    if (terms.empty()) continue;
    system.keys.push_back(key);
    system.rows.push_back(std::move(terms));
  }
  return system;
}

void print_construction(const System& system) {
  std::ostringstream out;
  out << "{\"modes\":[";
  for (size_t t = 0; t < system.modes.size(); ++t) {
    if (t) out << ',';
    out << '[' << system.modes[t].first << ',' << system.modes[t].second << ']';
  }
  out << "],\"rows\":[";
  for (size_t r = 0; r < system.rows.size(); ++r) {
    if (r) out << ',';
    out << "{\"key\":[" << system.keys[r].first << ',' << system.keys[r].second
        << "],\"terms\":[";
    const auto& terms = system.rows[r];
    for (size_t t = 0; t < terms.size(); ++t) {
      if (t) out << ',';
      out << '[' << terms[t][0] << ',' << terms[t][1] << ',' << terms[t][2] << ','
          << terms[t][3] << ',' << terms[t][4] << ']';
    }
    out << "]}";
  }
  out << "]}";
  std::cout << out.str() << '\n';
}

// ---------------------------------------------------------------------
// Proof replay: the four rules of Section 2.3 over the wire format.
// A fact state records known zero variables, known zero products
// (stored in the factor orientation of the P term that recorded
// them), and the currently assumed nonzero variables.
// ---------------------------------------------------------------------
struct Instruction {
  char op = 0;  // 'P', 'S', 'D', 'F'
  int x = 0;    // row index (P, S), first variable (D), pivot (F)
  int y = 0;    // second variable (D)
  std::vector<Instruction> child;  // F only
};

long long parse_int_strict(const std::string& token) {
  if (token.empty()) fail("empty integer in proof stream");
  size_t pos = 0;
  bool negative = false;
  if (token[0] == '-') {
    negative = true;
    pos = 1;
  }
  if (pos == token.size()) fail("malformed integer in proof stream");
  long long value = 0;
  for (; pos < token.size(); ++pos) {
    const char c = token[pos];
    if (c < '0' || c > '9') fail("malformed integer in proof stream");
    value = value * 10 + (c - '0');
    if (value > INT_MAX) fail("integer out of range in proof stream");
  }
  return negative ? -value : value;
}

std::vector<std::vector<std::string>> tokenize_lines(const std::string& text) {
  std::vector<std::vector<std::string>> lines;
  std::istringstream stream(text);
  std::string line;
  while (std::getline(stream, line)) {
    std::istringstream line_stream(line);
    std::vector<std::string> tokens;
    std::string token;
    while (line_stream >> token) tokens.push_back(token);
    lines.push_back(std::move(tokens));
  }
  return lines;
}

// Parses one block: instructions until 'E' (nested block) or 'X' (root).
// Advances pos past the terminator line.
std::vector<Instruction> parse_block(const std::vector<std::vector<std::string>>& lines,
                                     size_t& pos, bool root) {
  std::vector<Instruction> block;
  while (true) {
    if (pos >= lines.size()) fail("proof stream ends without a terminator");
    const std::vector<std::string>& tokens = lines[pos];
    if (tokens.empty()) fail("empty line in proof stream");
    const std::string& head = tokens[0];
    if (head == "X") {
      if (!root || tokens.size() != 1) fail("misplaced X in proof stream");
      ++pos;
      return block;
    }
    if (head == "E") {
      if (root || tokens.size() != 1) fail("misplaced E in proof stream");
      ++pos;
      return block;
    }
    if (head == "P" || head == "S") {
      if (tokens.size() != 2) fail("malformed row instruction in proof stream");
      Instruction ins;
      ins.op = head[0];
      ins.x = static_cast<int>(parse_int_strict(tokens[1]));
      block.push_back(std::move(ins));
      ++pos;
    } else if (head == "D") {
      if (tokens.size() != 3) fail("malformed division instruction in proof stream");
      Instruction ins;
      ins.op = 'D';
      ins.x = static_cast<int>(parse_int_strict(tokens[1]));
      ins.y = static_cast<int>(parse_int_strict(tokens[2]));
      block.push_back(std::move(ins));
      ++pos;
    } else if (head == "F") {
      if (tokens.size() != 2) fail("malformed refutation in proof stream");
      Instruction ins;
      ins.op = 'F';
      ins.x = static_cast<int>(parse_int_strict(tokens[1]));
      ++pos;
      ins.child = parse_block(lines, pos, false);
      block.push_back(std::move(ins));
    } else {
      fail("unknown opcode in proof stream");
    }
  }
}

struct Facts {
  std::set<int> zeros;
  std::set<std::pair<int, int>> products;  // orientation as recorded by P
  std::set<int> nonzero;                   // temporary F assumptions
};

struct Counters {
  long long p = 0, s = 0, d = 0, f = 0;
};

void replay_block(const std::vector<Instruction>& block, Facts& facts,
                  const System& system, Counters& counters) {
  const int dimension = static_cast<int>(system.modes.size());
  const int row_count = static_cast<int>(system.rows.size());
  for (const Instruction& ins : block) {
    for (int z : facts.zeros)
      if (facts.nonzero.count(z))
        fail("instructions continue after a contradiction");
    if (ins.op == 'P' || ins.op == 'S') {
      if (ins.op == 'P') ++counters.p; else ++counters.s;
      if (ins.x < 0 || ins.x >= row_count) fail("row index out of range");
      std::vector<const std::array<long long, 5>*> remaining;
      for (const auto& term : system.rows[ins.x]) {
        const int i = static_cast<int>(term[0]);
        const int j = static_cast<int>(term[2]);
        if (facts.zeros.count(i) || facts.zeros.count(j)) continue;
        if (facts.products.count({i, j})) continue;
        remaining.push_back(&term);
      }
      if (remaining.empty()) fail("an empty equation proves no new fact");
      if (ins.op == 'P') {
        if (remaining.size() != 1 || (*remaining[0])[0] == (*remaining[0])[2])
          fail("not a sole cross monomial");
        facts.products.insert({static_cast<int>((*remaining[0])[0]),
                               static_cast<int>((*remaining[0])[2])});
      } else {
        const bool single_square =
            remaining.size() == 1 && (*remaining[0])[0] == (*remaining[0])[2];
        bool hermitian_squares = true;
        bool all_positive = true, all_negative = true;
        for (const auto* term : remaining) {
          if ((*term)[0] != (*term)[2] || (*term)[1] != -(*term)[3])
            hermitian_squares = false;
          if ((*term)[4] > 0) all_negative = false;
          if ((*term)[4] < 0) all_positive = false;
          if ((*term)[4] == 0) { all_positive = false; all_negative = false; }
        }
        const bool common_sign = all_positive || all_negative;
        if (!single_square && !(hermitian_squares && common_sign))
          fail("not a sole complex square or sign-definite Hermitian squares");
        for (const auto* term : remaining)
          facts.zeros.insert(static_cast<int>((*term)[0]));
      }
    } else if (ins.op == 'D') {
      ++counters.d;
      const int i = ins.x, j = ins.y;
      if (i < 0 || i >= dimension || j < 0 || j >= dimension)
        fail("invalid variable indices in division");
      if (!facts.nonzero.count(i)) fail("division has no assumed nonzero pivot");
      const std::pair<int, int> key = i < j ? std::make_pair(i, j) : std::make_pair(j, i);
      if (!facts.products.count(key)) fail("division has no recorded zero product");
      if (facts.zeros.count(j)) fail("division repeats an existing fact");
      facts.zeros.insert(j);
    } else if (ins.op == 'F') {
      ++counters.f;
      const int i = ins.x;
      if (i < 0 || i >= dimension) fail("invalid refutation pivot");
      if (facts.zeros.count(i) || facts.nonzero.count(i))
        fail("invalid refutation pivot");
      Facts child = facts;
      child.nonzero.insert(i);
      replay_block(ins.child, child, system, counters);
      bool contradiction = false;
      for (int z : child.zeros)
        if (child.nonzero.count(z)) contradiction = true;
      if (!contradiction) fail("refutation does not reach a contradiction");
      facts.zeros.insert(i);
    } else {
      fail("unknown deduction rule");
    }
  }
}

int parse_radius(const char* arg) {
  const std::string token = arg;
  const long long value = parse_int_strict(token);
  if (value < 1 || value > 12) fail("radius out of supported range");
  return static_cast<int>(value);
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 2 && argc != 4) {
    std::cerr << "usage: resonance_complex_replay <radius> [--proof <file>]\n";
    return 2;
  }
  const int radius = parse_radius(argv[1]);
  const System system = construct(radius);
  if (argc == 2) {
    print_construction(system);
    return 0;
  }
  if (std::string(argv[2]) != "--proof") {
    std::cerr << "usage: resonance_complex_replay <radius> [--proof <file>]\n";
    return 2;
  }
  std::ifstream in(argv[3], std::ios::binary);
  if (!in) fail("cannot open proof file");
  std::ostringstream buffer;
  buffer << in.rdbuf();
  const auto lines = tokenize_lines(buffer.str());
  if (lines.empty() || lines[0].size() != 2 || lines[0][0] != "RESONANCE_COMPLEX_V1" ||
      parse_int_strict(lines[0][1]) != radius)
    fail("bad proof header");
  size_t pos = 1;
  const std::vector<Instruction> root = parse_block(lines, pos, true);
  if (pos != lines.size()) fail("trailing content after X in proof stream");
  Facts facts;
  Counters counters;
  replay_block(root, facts, system, counters);
  const int dimension = static_cast<int>(system.modes.size());
  if (static_cast<int>(facts.zeros.size()) != dimension)
    fail("the proof does not eliminate all coefficients");
  for (int v = 0; v < dimension; ++v)
    if (!facts.zeros.count(v)) fail("the proof does not eliminate all coefficients");
  std::cout << "{\"status\":\"PASS\",\"rules\":{\"P\":" << counters.p
            << ",\"S\":" << counters.s << ",\"D\":" << counters.d
            << ",\"F\":" << counters.f << "}}\n";
  return 0;
}
