"""Negative controls for historical external-leaf preservation."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations/verification'))
from wave2_integration_audit import check_external_epoch


class ExternalEpochPreservation(unittest.TestCase):
    def fixture(self,root):
        epoch=json.loads((ROOT/'record/claim_integration_epochs.json').read_text())
        relative=epoch['external_dependency_extension']['historical_registry']
        destination=root/relative
        destination.parent.mkdir(parents=True)
        destination.write_bytes((ROOT/relative).read_bytes())
        (root/'literature').mkdir()
        registry=json.loads((ROOT/'literature/external_dependencies.json').read_text())
        self.save(root,registry)
        return epoch,registry,destination

    def save(self,root,registry):
        (root/'literature/external_dependencies.json').write_text(json.dumps(registry))

    def test_current_epoch_preserves_39_contracts(self):
        epoch=json.loads((ROOT/'record/claim_integration_epochs.json').read_text())
        self.assertEqual(check_external_epoch(ROOT,epoch),(39,12))

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


if __name__=='__main__':
    unittest.main()
