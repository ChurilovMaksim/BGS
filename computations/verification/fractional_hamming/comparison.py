"""Exact JSON comparison with fixed, top-level Hamming provenance schemas.

Version and timing fields stay in the receipt. No nested field, scientific
string, unknown root field, boolean/integer difference, or non-finite value is
silently removed. Split independent cases have no provenance exclusions.
"""
import hashlib
import json
import math

SCIENCE_KEYS = {
    'author': {'arithmetic', 'cases', 'physical_range_split',
               'entropy_certificates', 'nonclaims'},
    'independent': {'full_end', 'top_gram', 'torus', 'network',
                    'offcharge_bound'},
    'synthesis': {'arithmetic', 'pair_families', 'all_radii', 'mask_cases'},
}
VERSION_KEYS = {'author': ('python', 'sympy'), 'independent': (), 'synthesis': ()}
TIMING_KEYS = {'author': ('elapsed_seconds',),
               'independent': ('runtime_seconds',), 'synthesis': ()}
CASES = {'full_end_2_1', 'full_end_2_2', 'full_end_2_3', 'full_end_3_2',
         'top_gram', 'torus', 'network', 'offcharge_bound'}


def parse_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result

    def invalid(value):
        raise ValueError('Non-finite JSON constant: ' + value)

    def finite_float(value):
        parsed = float(value)
        if not math.isfinite(parsed):
            raise ValueError('Non-finite JSON number: ' + value)
        return parsed

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid,
                      parse_float=finite_float)


def separate(data, family, expected=False):
    if family not in SCIENCE_KEYS or type(data) is not dict:
        raise ValueError('Unknown Hamming result family or non-object root')
    required = SCIENCE_KEYS[family] | set(VERSION_KEYS[family])
    optional = set(TIMING_KEYS[family])
    if expected:
        required |= optional
    if not required <= set(data) or set(data) - required - optional:
        raise ValueError('Hamming result root schema mismatch: ' + family)
    provenance = {}
    for key in VERSION_KEYS[family]:
        value = data[key]
        if type(value) is not str or not 0 < len(value) <= 4096:
            raise ValueError('Invalid top-level version provenance: ' + key)
        provenance[key] = value
    for key in TIMING_KEYS[family]:
        if key in data:
            value = data[key]
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                raise ValueError('Invalid top-level timing provenance: ' + key)
            provenance[key] = value
    return {key: data[key] for key in SCIENCE_KEYS[family]}, provenance


def differences(expected, observed, limit=20):
    found = []
    count = 0

    def add(path, reason):
        nonlocal count
        count += 1
        if len(found) < limit:
            found.append({'path': path or '/', 'reason': reason})

    def pointer(path, key):
        return path + '/' + str(key).replace('~', '~0').replace('/', '~1')

    def visit(a, b, path=''):
        if type(a) is not type(b):
            add(path, 'type mismatch')
        elif type(a) is dict:
            for key in sorted(a.keys() | b.keys()):
                child = pointer(path, key)
                if key not in a:
                    add(child, 'unexpected field')
                elif key not in b:
                    add(child, 'missing field')
                else:
                    visit(a[key], b[key], child)
        elif type(a) is list:
            if len(a) != len(b):
                add(path, 'list length mismatch')
            for index, (x, y) in enumerate(zip(a, b)):
                visit(x, y, pointer(path, index))
        elif a != b:
            add(path, 'value mismatch')

    if type(limit) is not int or limit < 1:
        raise ValueError('Positive exact integer mismatch limit required')
    visit(expected, observed)
    return {'equal': count == 0, 'mismatch_count': count, 'mismatches': found,
            'truncated': count > len(found)}


def scientific_bytes(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
                       allow_nan=False, separators=(',', ':')) + '\n').encode()


def compare(expected_raw, observed_raw, family, case=None):
    expected, prior = separate(parse_json(expected_raw), family, expected=True)
    observed = parse_json(observed_raw)
    if case is None:
        observed, current = separate(observed, family)
    else:
        if family != 'independent' or case not in CASES:
            raise ValueError('Unknown independent Hamming case')
        name = 'full_end' if case.startswith('full_end_') else case
        expected = expected[name]
        if case.startswith('full_end_'):
            n, m = map(int, case.removeprefix('full_end_').split('_'))
            expected = [row for row in expected if (row['N'], row['m']) == (n, m)]
        # There are no environment/timing exemptions in a split case object.
        current = {}
    report = {
        'schema': 'bgs-fractional-hamming-exact-provenance-v1',
        'family': family, 'case': case,
        'expected_provenance': prior, 'observed_provenance': current,
        'separated_top_level_paths': ([] if case is not None else
            ['/' + key for key in VERSION_KEYS[family] + TIMING_KEYS[family]]),
        'expected_raw_sha256': hashlib.sha256(expected_raw).hexdigest(),
        'observed_raw_sha256': hashlib.sha256(observed_raw).hexdigest(),
        'scientific_comparison': differences(expected, observed),
    }
    return expected, observed, report
