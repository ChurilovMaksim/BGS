"""Fail-closed exact JSON comparison; explicit schema-known provenance only.

The three pinned result schemas contain no runtime/environment fields. Their
allowlists are intentionally empty: Python/library versions belong to execution
provenance and never to mathematical equality. No key-name stripping occurs.
"""
import json
import math

SCHEMAS = {
    'author-exact-v1': (),
    'independent-core-v1': (),
    'independent-switch-v1': (),
}


def _pairs(rows):
    result = {}
    for key, value in rows:
        if key in result:
            raise ValueError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def load_json(path):
    return loads_json(path.read_bytes())


def loads_json(data):
    def invalid(value):
        raise ValueError('Non-finite JSON constant: ' + value)
    return json.loads(data, object_pairs_hook=_pairs,
                      parse_constant=invalid)


def differences(expected, observed, limit=20):
    """Return bounded JSON-pointer paths; bool and int are distinct types."""
    found = []
    total = 0

    def add(path, reason):
        nonlocal total
        total += 1
        if len(found) < limit:
            found.append({'path': path or '/', 'reason': reason})

    def pointer(path, key):
        return path + '/' + str(key).replace('~', '~0').replace('/', '~1')

    def visit(a, b, path=''):
        if type(a) is not type(b):
            add(path, 'type mismatch')
        elif isinstance(a, dict):
            for key in sorted(a.keys() | b.keys()):
                child = pointer(path, key)
                if key not in a:
                    add(child, 'unexpected field')
                elif key not in b:
                    add(child, 'missing field')
                else:
                    visit(a[key], b[key], child)
        elif isinstance(a, list):
            if len(a) != len(b):
                add(path, 'list length mismatch')
            for i in range(min(len(a), len(b))):
                visit(a[i], b[i], pointer(path, i))
        elif a != b:
            add(path, 'value mismatch')

    if type(limit) is not int or limit < 1:
        raise ValueError('Positive exact integer mismatch limit required')
    visit(expected, observed)
    return {'equal': total == 0, 'mismatch_count': total,
            'mismatches': found, 'truncated': total > len(found)}


def compare(schema, expected, observed, expected_provenance, observed_provenance):
    if schema not in SCHEMAS:
        raise ValueError('Unknown scientific result schema: ' + str(schema))
    for side in [expected_provenance, observed_provenance]:
        if 'runtime_seconds' in side:
            value = side['runtime_seconds']
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                raise ValueError('Invalid provenance runtime_seconds')
    # There are no environment/runtime paths in these three exact JSON payloads.
    # A new field named "python", "runtime", "source" or "environment" is an
    # unexpected scientific structure change, never an implicit exemption.
    result = differences(expected, observed)
    return {'schema': schema, 'excluded_runtime_environment_paths': [],
            'scientific_comparison': result,
            'provenance': {'expected': expected_provenance,
                           'observed': observed_provenance}}
