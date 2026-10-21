"""Independent exact check of the last-exit construction.

The complete proof is audited in dual_audit_exponential_coherent_edge_classes.md.
This finite enumeration is only a consistency check, using a weaker local
eligibility condition than the good-vertex condition in the theorem.
"""

from collections import Counter, defaultdict
from itertools import product


def check_word(word):
    n = len(word)
    root = word[0]
    exits = defaultdict(list)
    for j, v in enumerate(word):
        exits[v].append(j)
    last = {v: indices[-1] for v, indices in exits.items() if v != root}
    for v in last:
        current = v
        seen = set()
        while current != root:
            assert current not in seen
            seen.add(current)
            edge = last[current]
            nxt = word[(edge + 1) % n]
            if nxt != root:
                assert last[nxt] > edge
            current = nxt
    # Distinct successors are exactly what the injectivity proof needs.
    # The additional good-vertex hypotheses are used only for its weighted mean.
    eligible = [v for v, indices in exits.items()
                if v != root and len(indices) == 3 and
                len({word[(j + 1) % n] for j in indices}) == 3]
    original_edges = Counter((word[j], word[(j+1) % n]) for j in range(n))
    partners = set()
    for bits in product((0, 1), repeat=len(eligible)):
        lists = {v: indices[:] for v, indices in exits.items()}
        for v, bit in zip(eligible, bits):
            if bit:
                lists[v][0], lists[v][1] = lists[v][1], lists[v][0]
            assert lists[v][-1] == last[v]
        used_counts = Counter()
        used_edges = set()
        current = root
        partner = []
        while used_counts[current] < len(lists[current]):
            partner.append(current)
            edge = lists[current][used_counts[current]]
            used_counts[current] += 1
            assert edge not in used_edges and word[edge] == current
            used_edges.add(edge)
            current = word[(edge + 1) % n]
            assert len(partner) <= n
        assert current == root and len(partner) == n and len(used_edges) == n
        partner = tuple(partner)
        assert Counter((partner[j], partner[(j+1) % n]) for j in range(n)) == original_edges
        assert partner not in partners
        partners.add(partner)
    assert len(partners) == 2**len(eligible)
    return len(partners), len(eligible)


if __name__ == "__main__":
    words = tours = eligible_words = 0
    for n in range(3, 9):
        for word in product(range(3), repeat=n):
            count, eligible = check_word(word)
            words += 1
            tours += count
            eligible_words += eligible > 0
    print("Words / complete distinct tours / words with a binary choice:",
          words, tours, eligible_words)
    assert eligible_words > 0
    print("All exact last-exit and injectivity checks passed.")
