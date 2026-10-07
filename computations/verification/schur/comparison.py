"""Fail-closed comparison of this exact, fixed result schema.

Only the three documented TOP-LEVEL provenance fields are separated. Arbitrary
nested keys, extra root keys, changed types and scientific strings remain part
of equality. This is a provenance separator, not recursive key filtering.
"""
import hashlib
import json
import math

PROVENANCE_FIELDS = ('runtime_seconds', 'python', 'sympy')
ROOT_KEYS = {
    'author': {'status', 'arithmetic', 'inputs', 'counts', 'full_B_through_6',
               'scalar_moments', 'same_minors_distinct_B2', 'caps', 'nonclaims',
               *PROVENANCE_FIELDS},
    'independent': {'status', 'arithmetic', 'counts', 'fixtures', 'nonclaims',
                    *PROVENANCE_FIELDS},
}
WALL_CAP = {'author': 70, 'independent': 180}
MAX_MISMATCHES = 12


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate JSON key: ' + key[:120])
            result[key] = value
        return result

    def invalid(token):
        raise ValueError('non-finite JSON token: ' + token)

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)


def separate(result, family):
    require(family in ROOT_KEYS, 'unknown result family')
    require(type(result) is dict, 'result root must be an object')
    require(set(result) == ROOT_KEYS[family], 'result root schema mismatch')
    elapsed = result['runtime_seconds']
    require(type(elapsed) in (int, float) and math.isfinite(elapsed)
            and 0 <= elapsed <= WALL_CAP[family], 'invalid runtime_seconds')
    for key in ('python', 'sympy'):
        require(type(result[key]) is str and 0 < len(result[key]) <= 4096,
                'invalid environment provenance: ' + key)
    provenance = {key: result[key] for key in PROVENANCE_FIELDS}
    scientific = {key: value for key, value in result.items()
                  if key not in PROVENANCE_FIELDS}
    return scientific, provenance


def mismatch_paths(expected, observed):
    found = []

    def record(path, kind):
        if len(found) < MAX_MISMATCHES:
            found.append({'path': path[:240], 'kind': kind})

    def visit(a, b, path):
        if len(found) >= MAX_MISMATCHES:
            return
        if type(a) is not type(b):
            record(path, 'type')
        elif isinstance(a, dict):
            for key in sorted(a.keys() | b.keys()):
                child = path + '/' + key.replace('~', '~0').replace('/', '~1')
                if key not in a:
                    record(child, 'unexpected key')
                elif key not in b:
                    record(child, 'missing key')
                else:
                    visit(a[key], b[key], child)
                if len(found) >= MAX_MISMATCHES:
                    break
        elif isinstance(a, list):
            if len(a) != len(b):
                record(path, 'length')
            for index, (x, y) in enumerate(zip(a, b)):
                visit(x, y, path + '/' + str(index))
                if len(found) >= MAX_MISMATCHES:
                    break
        elif a != b:
            record(path, 'value')

    visit(expected, observed, '')
    return found


def scientific_bytes(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
                       allow_nan=False, separators=(',', ':')) + '\n').encode()


def compare(expected_bytes, observed_bytes, family):
    expected, prior = separate(parse_json(expected_bytes), family)
    observed, current = separate(parse_json(observed_bytes), family)
    mismatches = mismatch_paths(expected, observed)
    require(not mismatches, 'scientific output mismatch: '
            + json.dumps(mismatches, separators=(',', ':')))
    result_bytes = scientific_bytes(observed)
    return result_bytes, {
        'separated_paths': ['/' + name for name in PROVENANCE_FIELDS],
        'expected_provenance': prior,
        'observed_provenance': current,
        'expected_raw_sha256': hashlib.sha256(expected_bytes).hexdigest(),
        'observed_raw_sha256': hashlib.sha256(observed_bytes).hexdigest(),
        'scientific_sha256': hashlib.sha256(result_bytes).hexdigest(),
        'scientific_equality': True,
    }
