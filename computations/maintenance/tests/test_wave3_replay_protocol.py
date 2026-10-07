"""Wave3 durable bounded replay regression tests; no proof audit."""
import importlib.util,json
from pathlib import Path
import tempfile,unittest
ROOT=Path(__file__).resolve().parents[3]
import sys
sys.path.insert(0,str(ROOT/'computations/verification'))
import wave3_checked_replay as m

class Wave3Protocol(unittest.TestCase):
    def fixture(self,root,body=None,expected_value=1):
        root.mkdir();(root/'record').mkdir();body=body or 'import json\nfrom pathlib import Path\nPath(__file__).with_name("result.json").write_text(json.dumps({"checks":1,"value":1}))\n'
        tasks=[];files=[]
        for i in range(4):
            script=f'check{i}.py';expected=f'expected{i}.json';(root/script).write_text(body);(root/expected).write_text(json.dumps({'checks':1,'value':expected_value}));files.extend([script,expected])
            tasks.append({'name':f'fixture{i}','domain':'synthetic','source':script,'expected':expected,'generated_result':'result.json','provenance_fields':{},'count_field':'checks','declared_check_count':1,'arithmetic_scope':'Synthetic protocol control only','timeout_seconds':10})
        (root/m.CONTRACT).write_text(json.dumps({'schema':'bgs-wave3-replay-contract-v1','tasks':tasks}));files.append(m.CONTRACT)
        (root/m.BINDINGS).write_text(json.dumps({'schema':'bgs-wave3-replay-source-bindings-v1','files':{p:m.digest((root/p).read_bytes()) for p in files}}))
    def test_current_source_closure(self):self.assertGreater(len(m.source_bytes()),8)
    def test_success_keeps_all_raw_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';out=Path(tmp)/'run';self.fixture(root);r=m.run(root,out);self.assertEqual(r['status'],'passed');self.assertEqual(len(r['tasks']),4)
            for i in range(4):
                for suffix in ['expected.raw','actual.raw','stdout','stderr','adapter.json']:self.assertTrue((out/f'fixture{i}.{suffix}').is_file())
    def test_scientific_failure_keeps_terminal_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';out=Path(tmp)/'run';self.fixture(root,expected_value=2)
            with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):m.run(root,out)
            r=json.loads((out/'replay_manifest.json').read_text());self.assertEqual(r['status'],'failed');self.assertEqual(r['tasks'][0]['status'],'failed');self.assertTrue((out/'fixture0.actual.raw').is_file())
    def test_noop_cannot_reuse_old_expected_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';out=Path(tmp)/'run';self.fixture(root,body='pass\n')
            with self.assertRaisesRegex(RuntimeError,'missing/oversized'):m.run(root,out)
            self.assertEqual(json.loads((out/'replay_manifest.json').read_text())['status'],'failed')
    def test_explicit_assert_failure_is_retained(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';out=Path(tmp)/'run';self.fixture(root,body='assert False, "mathematical negative"\n')
            with self.assertRaisesRegex(RuntimeError,'mathematical negative'):m.run(root,out)
            self.assertIn(b'mathematical negative',(out/'fixture0.stderr').read_bytes())
    def test_code_hash_mutation_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';self.fixture(root);(root/'check0.py').write_text('pass\n')
            with self.assertRaisesRegex(RuntimeError,'changed Wave3'):m.source_bytes(root)
    def test_input_symlink_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';self.fixture(root);p=root/'check0.py';p.unlink();p.symlink_to(root/'check1.py')
            with self.assertRaisesRegex(RuntimeError,'nonregular'):m.source_bytes(root)
    def test_source_output_overlap_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'source';self.fixture(root)
            with self.assertRaisesRegex(RuntimeError,'overlaps maintained'):m.run(root,root/'output')
if __name__=='__main__':unittest.main()
