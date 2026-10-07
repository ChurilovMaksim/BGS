"""Run one unchanged independent exact family with an explicit output path."""
import argparse
import importlib.util
import json
from pathlib import Path

CASES = {'full_end': 'full_end_controls', 'top_gram': 'top_gram_control',
         'torus': 'torus_controls', 'network': 'network_controls',
         'offcharge_bound': 'exact_offcharge_bound',
         **{'full_end_' + str(n) + '_' + str(m): 'full_end_controls' for n, m in [(2, 1), (2, 2), (2, 3), (3, 2)]}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=sorted(CASES), required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    path = Path(__file__).with_name('independent_checks.py')
    spec = importlib.util.spec_from_file_location('independent_hamming', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if args.case.startswith('full_end_'):
        n, m = map(int, args.case.removeprefix('full_end_').split('_'))
        data = module.full_end_controls([(n, m)])
    else:
        data = getattr(module, CASES[args.case])()
    args.output.write_text(json.dumps(data, indent=2, default=str) + '\n')


if __name__ == '__main__':
    main()
