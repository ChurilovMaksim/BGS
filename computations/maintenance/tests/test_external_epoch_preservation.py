"""Negative controls for historical external-leaf preservation.

The sealed 39-row leaf admits reviewed succession only through
record/external_epoch_amendments.json: a sealed contract passes iff it is
byte-identical to the sealed record (apart from the provenance-only
metadata_audit pointer) or differs only in recorded fields at exactly the
recorded values. Scratch amendments below live only in temporary roots. The scratch
registry is built from the sealed baseline (see fixture), so the
controls stay valid after waves land their own reviewed rows in
the committed store (first: P2-MATH wave 4, five rows).
"""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations/verification'))
from wave2_integration_audit import check_external_epoch, check_prior_claims


class ExternalEpochPreservation(unittest.TestCase):
    def fixture(self,root):
        epoch=json.loads((ROOT/'record/claim_integration_epochs.json').read_text())
        relative=epoch['external_dependency_extension']['historical_registry']
        destination=root/relative
        destination.parent.mkdir(parents=True)
        destination.write_bytes((ROOT/relative).read_bytes())
        (root/'literature').mkdir()
        # Sealed baseline, not the live registry: once a wave lands reviewed
        # amendment rows, the live registry already differs from the sealed
        # rows, and scratch stores (save_store replaces the committed store)
        # would leave those landed differences unrecorded. Building the
        # scratch registry from the sealed snapshot plus the live
        # admitted-later rows keeps every scratch control independent of
        # which waves have landed; admitted rows are not byte-compared.
        sealed=json.loads(destination.read_text())['dependencies']
        sealed_ids={row['id'] for row in sealed}
        live=json.loads((ROOT/'literature/external_dependencies.json').read_text())
        registry={'schema':live['schema'],'updated':live.get('updated'),
                  'dependencies':sealed+[row for row in live['dependencies']
                                         if row['id'] not in sealed_ids]}
        self.save(root,registry)
        (root/'record').mkdir(exist_ok=True)
        store=ROOT/'record/external_epoch_amendments.json'
        if store.is_file():
            (root/'record/external_epoch_amendments.json').write_bytes(store.read_bytes())
        return epoch,registry,destination

    def save(self,root,registry):
        (root/'literature/external_dependencies.json').write_text(json.dumps(registry))

    def save_store(self,root,rows):
        (root/'record/external_epoch_amendments.json').write_text(json.dumps(
            {'schema':'bgs-external-epoch-amendment-v1','amendments':rows}))

    def sealed_row(self,root):
        snapshot=json.loads((root/'archive/evidence/executions/20261011/chat-research/baselines/external_dependencies_20261007.json').read_text())
        return next(row for row in snapshot['dependencies'] if row['id']=='EXT-SOSH-2000')

    def amendment(self,sealed,field,new_value,**overrides):
        row={'id':'EXT-SOSH-2000','field':field,'old_value':sealed[field],
             'new_value':new_value,
             'historical_contract_sha256':hashlib.sha256(json.dumps(
                 sealed,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),
             'wave':'scratch control (never committed)',
             'disposition':'Temporary control row only.',
             'review':'scratch'}
        row.update(overrides)
        return row

    def relocated_registry(self,registry,field,new_value):
        for row in registry['dependencies']:
            if row['id']=='EXT-SOSH-2000':
                row[field]=new_value
        return registry

    def test_current_epoch_preserves_39_contracts(self):
        epoch=json.loads((ROOT/'record/claim_integration_epochs.json').read_text())
        self.assertEqual(check_external_epoch(ROOT,epoch),(39,25))

    def test_historical_claim_amendments_are_exact_and_explicit(self):
        epoch=json.loads((ROOT/'record/claim_integration_epochs.json').read_text())
        historical=ROOT/'evidence/wave2_checked_20261007/raw/provenance/base_navigation/record/claims.json'
        previous=json.loads(historical.read_text())['claims']
        current={c['id']:c for c in json.loads((ROOT/'record/claims.json').read_text())['claims']}
        check_prior_claims(previous,current,epoch)
        mutated=copy.deepcopy(current)
        mutated['BGS-CAYLEY-001']['boundary']+=' unreviewed change'
        with self.assertRaisesRegex(RuntimeError,'outside reviewed amendment'):
            check_prior_claims(previous,mutated,epoch)
        mutated=copy.deepcopy(epoch)
        mutated['historical_claim_amendments'][0]['historical_row_sha256']='0'*64
        with self.assertRaisesRegex(RuntimeError,'provenance differs'):
            check_prior_claims(previous,current,mutated)

    def test_modified_old_locator_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,registry,_=self.fixture(root)
            registry['dependencies'][0]['locator']='weakened locator'
            self.save(root,registry)
            with self.assertRaisesRegex(RuntimeError,'historical external contract changed'):
                check_external_epoch(root,epoch)

    def test_undeclared_new_dependency_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,registry,_=self.fixture(root)
            extra=copy.deepcopy(registry['dependencies'][-1]);extra['id']='EXT-UNREVIEWED'
            registry['dependencies'].append(extra);self.save(root,registry)
            with self.assertRaisesRegex(RuntimeError,'undeclared external dependency'):
                check_external_epoch(root,epoch)

    def test_changed_historical_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,_,snapshot=self.fixture(root)
            snapshot.write_bytes(snapshot.read_bytes()+b'\n')
            with self.assertRaisesRegex(RuntimeError,'historical external leaf changed'):
                check_external_epoch(root,epoch)

    def test_automatic_extension_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,_,_=self.fixture(root)
            epoch['external_dependency_extension']['added_ids'].append('EXT-UNREVIEWED')
            with self.assertRaisesRegex(RuntimeError,'explicit epoch review'):
                check_external_epoch(root,epoch)

    def test_reviewed_amendment_admitted_at_exact_value(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,registry,_=self.fixture(root)
            sealed=self.sealed_row(root)
            new=[path.replace('mathematics/return_trace_obstruction.md',
                              'mathematics/returns/return_trace_obstruction.md')
                 for path in sealed['project_sources']]
            self.save_store(root,[self.amendment(sealed,'project_sources',new)])
            self.save(root,self.relocated_registry(registry,'project_sources',new))
            self.assertEqual(check_external_epoch(root,epoch),(39,25))

    def test_tampered_amended_value_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,registry,_=self.fixture(root)
            sealed=self.sealed_row(root)
            new=[path.replace('mathematics/return_trace_obstruction.md',
                              'mathematics/returns/return_trace_obstruction.md')
                 for path in sealed['project_sources']]
            self.save_store(root,[self.amendment(sealed,'project_sources',new)])
            tampered=list(new);tampered[-1]='mathematics/returns/elsewhere.md'
            self.save(root,self.relocated_registry(registry,'project_sources',tampered))
            with self.assertRaisesRegex(RuntimeError,'historical external contract changed'):
                check_external_epoch(root,epoch)

    def test_tamper_outside_amended_field_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,registry,_=self.fixture(root)
            sealed=self.sealed_row(root)
            new=[path.replace('mathematics/return_trace_obstruction.md',
                              'mathematics/returns/return_trace_obstruction.md')
                 for path in sealed['project_sources']]
            self.save_store(root,[self.amendment(sealed,'project_sources',new)])
            registry=self.relocated_registry(registry,'project_sources',new)
            for row in registry['dependencies']:
                if row['id']=='EXT-SOSH-2000':
                    row['locator']='tampered locator'
            self.save(root,registry)
            with self.assertRaisesRegex(RuntimeError,'historical external contract changed'):
                check_external_epoch(root,epoch)

    def test_unknown_and_admitted_later_amendment_ids_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,_,_=self.fixture(root)
            sealed=self.sealed_row(root)
            for identifier in ('EXT-UNREVIEWED','EXT-BR-1975'):
                row=self.amendment(sealed,'project_sources',sealed['project_sources'])
                row['id']=identifier
                self.save_store(root,[row])
                with self.assertRaisesRegex(RuntimeError,'unknown external amendment id'):
                    check_external_epoch(root,epoch)

    def test_amendment_old_value_and_provenance_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,_,_=self.fixture(root)
            sealed=self.sealed_row(root)
            new=list(sealed['project_sources'])
            self.save_store(root,[self.amendment(sealed,'project_sources',new,
                                                 old_value=['wrong old value'])])
            with self.assertRaisesRegex(RuntimeError,'old value differs'):
                check_external_epoch(root,epoch)
            self.save_store(root,[self.amendment(sealed,'project_sources',new,
                                                 historical_contract_sha256='0'*64)])
            with self.assertRaisesRegex(RuntimeError,'provenance differs'):
                check_external_epoch(root,epoch)

    def test_malformed_amendments_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);epoch,_,_=self.fixture(root)
            sealed=self.sealed_row(root)
            new=[path.replace('mathematics/return_trace_obstruction.md',
                              'mathematics/returns/return_trace_obstruction.md')
                 for path in sealed['project_sources']]
            good=self.amendment(sealed,'project_sources',new)
            malformed=[{key:value for key,value in good.items() if key!='review'},
                       self.amendment(sealed,'metadata_audit','pointer'),
                       self.amendment(sealed,'id','EXT-OTHER'),
                       self.amendment(sealed,'project_sources',sealed['project_sources'])]
            for row in malformed:
                self.save_store(root,[row])
                with self.assertRaisesRegex(RuntimeError,'malformed|invalid|vacuous'):
                    check_external_epoch(root,epoch)
            self.save_store(root,[good,good])
            with self.assertRaisesRegex(RuntimeError,'duplicate external amendment'):
                check_external_epoch(root,epoch)
            (root/'record/external_epoch_amendments.json').write_text('{not json')
            with self.assertRaisesRegex(RuntimeError,'.'):
                check_external_epoch(root,epoch)


if __name__=='__main__':
    unittest.main()
