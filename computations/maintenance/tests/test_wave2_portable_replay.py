"""Adversarial tests for the Wave2 portable Schur-degeneracy replay policy."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations/verification'))
import wave2_checked_replay as v1
import wave2_portable_replay as v2

ALT_SPLIT=(
    {'reverse_norm':0.20000303064356734,
     'P_centered_norm':5.959949522070739e-6},
    {'reverse_norm':0.0909091112638557,
     'P_centered_norm':2.8349934873843053e-8},
)


class PortableSchurNorms(unittest.TestCase):
    def setUp(self):
        contract=json.loads((ROOT/'record/wave2_replay_contract.json').read_text())
        self.task=copy.deepcopy(next(t for t in contract['tasks']
                                     if t['name']=='rounding'))
        self.expected=json.loads((ROOT/self.task['expected']).read_text())
        self.observed=copy.deepcopy(self.expected)

    def use_alternative_basis(self):
        for row, alt in zip(self.observed['floating_split_controls'],ALT_SPLIT):
            row.update(alt)

    def compare(self):
        # v1.compare always deep-copies inputs before replacing only its
        # private normalized projection. Both supplied payloads remain raw.
        self.task['provenance_fields']={}
        with v2.portable_comparison_scope():
            return v1.compare(self.expected,self.observed,self.task,{})

    def test_two_host_realizations_pass_with_raw_values_preserved(self):
        self.use_alternative_basis()
        before=copy.deepcopy(self.observed)
        result=self.compare()
        self.assertEqual(self.observed,before)
        self.assertEqual(len(result['numeric_diagnostics']),len(self.task['numeric_diagnostics']))
        self.assertEqual(sum(
            x.get('comparison')=='basis_invariant_symplectic_fourier_norm_v2'
            for x in result['numeric_diagnostics'].values()),4)
        self.assertFalse(result['numeric_diagnostics'][
            '/floating_split_controls/0/reverse_norm'
        ]['reference_equality_within_v1_tolerance'])
        self.assertIs(v1.compare_numeric_diagnostics,v2.ORIGINAL_NUMERIC_COMPARE)

    def test_historical_reference_passes_without_special_difference(self):
        result=self.compare()
        self.assertTrue(all(
            result['numeric_diagnostics'][f'/floating_split_controls/{i}/{key}']
                 ['reference_equality_within_v1_tolerance']
            for i in range(2) for key in v2.BASIS_FIELDS))

    def test_numeric_relations_and_outside_values_remain_fail_closed(self):
        self.use_alternative_basis()
        self.observed['floating_split_controls'][0]['P_centered_norm']=1e-3
        with self.assertRaisesRegex(RuntimeError,
                                    'original split P-center bound'):
            self.compare()
        self.observed=copy.deepcopy(self.expected)
        self.observed['floating_split_controls'][1]['reverse_norm']=0.2
        with self.assertRaisesRegex(RuntimeError,
                                    'basis-invariant reverse Fourier'):
            self.compare()
        self.observed=copy.deepcopy(self.expected)
        self.observed['floating_norm_controls'][0]['epsilon']+=1e-5
        with self.assertRaisesRegex(RuntimeError,
                                    'numeric diagnostic exceeds declared'):
            self.compare()

    def test_new_numeric_fields_and_wrong_sample_ids_are_rejected(self):
        self.task['numeric_diagnostics']['/floating_split_controls/0/not_listed']={
            'comparison':'finite_nonnegative_reference_difference',
            'absolute_tolerance':1e-12,'relative_tolerance':0.0}
        with self.assertRaisesRegex(RuntimeError,'policy changed'):
            self.compare()
        del self.task['numeric_diagnostics']['/floating_split_controls/0/not_listed']
        self.observed['floating_split_controls'][0]['p']=7
        with self.assertRaisesRegex(RuntimeError,'prime/index'):
            self.compare()

    def test_source_bytes_and_comparison_scope(self):
        self.assertGreater(len(v1.source_bytes()),50)
        with v2.portable_comparison_scope():
            self.assertIs(v1.compare_numeric_diagnostics,v2.portable_numeric_compare)
            with self.assertRaisesRegex(RuntimeError,'already overridden'):
                with v2.portable_comparison_scope():
                    pass
        self.assertIs(v1.compare_numeric_diagnostics,v2.ORIGINAL_NUMERIC_COMPARE)

    def test_exact_symplectic_fourier_row_orthogonality_counts(self):
        # No floating point or Schur decomposition: the reverse-kernel
        # character matrix has exactly orthogonal rows for both primes.
        for p, n in v2.SPLIT_SAMPLES:
            values=[(pow(j % p, 3, p), pow(j // p, 3, p))
                    for j in range(n)]
            self.assertEqual(len(set(values)),n)
            for a in range(p):
                for b in range(p):
                    if a==b==0:
                        continue
                    residue_counts=[0]*p
                    for x,y in values:
                        residue_counts[(2*(a*y-b*x)) % p]+=1
                    self.assertEqual(residue_counts,[p]*p,
                                     (p,a,b,residue_counts))

    def test_analytical_symplectic_fourier_hypotheses(self):
        for p,n in v2.SPLIT_SAMPLES:
            self.assertEqual(n,p*p)
            self.assertEqual(__import__('math').gcd(3,p-1),1)
            self.assertNotEqual(4 % p,0)
        for i,(p,_) in enumerate(v2.SPLIT_SAMPLES):
            bound=v2._split_invariant_bound(self.expected['floating_split_controls'][i],p,i)
            self.assertGreater(bound,0)
            self.assertLess(bound,0.01)


if __name__=='__main__':
    unittest.main()
