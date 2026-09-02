"""
FAST APPLICATION OF THE WEIL PROPAGATOR  (O(N log N) instead of O(N^2)),
which lets us reach multiplicities an order of magnitude larger.

  (U psi)(x) = N^{-1/2} sum_y w^{ (2c)^{-1} (d x^2 - 2 x y + a y^2) } psi(y)
             = N^{-1/2} w^{ icb d x^2 } * ghat( (-c1 x) mod N ),
  where  icb = (2c)^{-1} mod N,  g(y) = w^{icb a y^2} psi(y),
         c1  = (-2 icb) mod N,   ghat(k) = sum_y g(y) e^{-2 pi i k y / N}  (numpy FFT).

Since gcd(c1, N) = 1 the map x -> (-c1 x) mod N is a permutation, so one FFT plus
two chirp multiplications per application.  Verified against the explicit matrix.
"""
import numpy as np, math, os, json

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


class FastWeil:
    def __init__(self, M, N):
        a, b, c, d = [int(x) % N for x in M]
        self.N = N
        icb = pow((2*c) % N, -1, N)
        xs = np.arange(N, dtype=np.int64)
        self.pre = np.exp(2j*np.pi*((icb*a*xs*xs) % N)/N)          # chirp in y
        self.post = np.exp(2j*np.pi*((icb*d*xs*xs) % N)/N)/math.sqrt(N)
        c1 = (-2*icb) % N
        self.idx = ((-c1)*xs) % N                                   # output permutation

    def apply(self, X):
        """X: (N,) or (N,k) complex array."""
        if X.ndim == 1:
            g = self.pre*X
            gh = np.fft.fft(g)
            return self.post*gh[self.idx]
        g = self.pre[:, None]*X
        gh = np.fft.fft(g, axis=0)
        return self.post[:, None]*gh[self.idx, :]


def U_explicit(M, N):
    a, b, c, d = [int(x) % N for x in M]
    icb = pow((2*c) % N, -1, N)
    xs = np.arange(N)
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    Q = (icb*(d*X*X - 2*X*Y + a*Y*Y)) % N
    return np.exp(2j*np.pi*Q/N)/math.sqrt(N)


def verify(Ns=(11, 101, 257), Ms=((2, 1, 1, 1), (3, 1, 2, 1), (1, 0, 1, 1))):
    worst = 0.0
    for N in Ns:
        for M in Ms:
            Ue = U_explicit(M, N)
            F = FastWeil(M, N)
            X = np.eye(N, dtype=complex)
            worst = max(worst, np.linalg.norm(F.apply(X)-Ue)/np.linalg.norm(Ue))
    return worst


if __name__ == "__main__":
    w = verify()
    print(f"fast vs explicit propagator: max relative error = {w:.3e}")
    import time
    for N in (1009, 10007, 100003):
        F = FastWeil((2, 1, 1, 1), N)
        X = (np.random.default_rng(0).normal(size=(N, 8)) +
             1j*np.random.default_rng(1).normal(size=(N, 8)))
        t0 = time.time()
        for _ in range(20): X = F.apply(X)
        print(f"  N={N:7d}: 20 block applications (8 vectors) in {time.time()-t0:.3f} s")
    json.dump({"fast_weil_rel_error": float(w)},
              open(os.path.join(ART, "fast_weil_check.json"), "w"))
