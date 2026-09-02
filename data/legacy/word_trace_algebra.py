"""Word-trace computation in the partial-isometry algebra (Theorem 91.5 proof)."""
import itertools


def reduce_once(w):
    i = 0
    while i < len(w) - 1:
        a, b = w[i], w[i + 1]
        if a == 'V' and b == 'V*':
            w[i:i + 2] = ['I', 'E']; return True
        if a == 'V*' and b == 'V':
            w[i:i + 2] = ['I', 'F']; return True
        if a == 'E' and b == 'V':
            w[i:i + 2] = ['V', 'F']; return True
        if a == 'F' and b == 'V*':
            w[i:i + 2] = ['V*', 'E']; return True
        if a == 'E' and b == 'E':
            w[i:i + 2] = ['E']; return True
        if a == 'F' and b == 'F':
            w[i:i + 2] = ['F']; return True
        if a == 'E' and b == 'F':
            w[i:i + 2] = ['0']; return True
        if a == 'F' and b == 'E':
            w[i:i + 2] = ['0']; return True
        if a == 'I':
            w[i:i + 1] = []; return True
        i += 1
    if len(w) >= 2:
        if w[-1] == 'V' and w[0] == 'V*':
            w[-1:] = []; w[0:0] = ['I', 'F']; return True
        if w[-1] == 'V*' and w[0] == 'V':
            w[-1:] = []; w[0:0] = ['I', 'E']; return True
        if w[-1] == 'E' and w[0] == 'V':
            w[-1:] = []; w[0:0] = ['V', 'F']; return True
        if w[-1] == 'F' and w[0] == 'V*':
            w[-1:] = []; w[0:0] = ['V*', 'E']; return True
    return False


def reduce_word(w):
    w = list(w)
    guard = 0
    while guard < 10000:
        if '0' in w:
            return ('0',)
        if not reduce_once(w):
            break
        guard += 1
    return tuple(w)


def trace_word(w):
    """Return 0, 1, or 'm' for Tr of the reduced word."""
    w = reduce_word(w)
    if w == ('0',):
        return 0
    if not w:
        return 'm'
    if all(t in ('E', 'F') for t in w):
        r = reduce_word(w)
        if r == ('0',):
            return 0
        if r == ('E',) or r == ('F',):
            return 1
        if not r:
            return 'm'
        return 0
    if w.count('V') != w.count('V*'):
        return 0
    return '?UNBAL?'


def moment(s):
    """Tr(M^{2s}) with M = V + V*; m = Tr(I) handled symbolically."""
    coef_m = 0     # coefficient of 'm'
    const = 0
    for bits in itertools.product(['V', 'V*'], repeat=2 * s):
        t = trace_word(list(bits))
        if t == 'm':
            coef_m += 1
        elif isinstance(t, (int, float)):
            const += t
        elif t == '?UNBAL?':
            raise RuntimeError(f"unbalanced leftover at s={s}")
    return coef_m, const


if __name__ == "__main__":
    for s in range(1, 8):
        cm, cc = moment(s)
        print(f"s={s}: Tr(M^(2s)) = {cm}*m + ({cc})")
