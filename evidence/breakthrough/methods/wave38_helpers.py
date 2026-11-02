"""Shared helpers for wave 38 task 4 exploration (no module-level work)."""
import numpy as np


def lifts_of_point(y, m_hi, q_hi, q_lo):
    """All lifts of a level-(k-1) point y to level k (copied from wave36_lift)."""
    out = []
    for a in range(4):
        for b in range(4):
            s = np.empty(m_hi, dtype=np.int64)
            s[0] = (int(y[0]) + q_lo * a) % q_hi
            s[1] = (int(y[1]) + q_lo * b) % q_hi
            for i in range(1, m_hi - 1):
                s[i + 1] = (6 * s[i] - s[i - 1]) % q_hi
            if s[0] == (6 * s[-1] - s[-2]) % q_hi and s[1] == (6 * s[0] - s[-1]) % q_hi:
                out.append(s)
    return out


def period_of(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and np.all(np.roll(y, -p) == y):
            return p
    return m


def e_seq(y, q):
    """e_i = (y_{i+1} - 6 y_i + y_{i-1}) / q mod 4, indices mod len(y)."""
    m = len(y)
    yy = y.astype(np.int64)
    num = np.roll(yy, -1) - 6 * yy + np.roll(yy, 1)
    assert np.all(num % q == 0), "recurrence defect not divisible by q"
    return (num // q) % 4
