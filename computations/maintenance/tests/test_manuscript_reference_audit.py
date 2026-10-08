"""Adversarial tests for the LaTeX source and bibliography index."""
from __future__ import annotations
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import audit_manuscript_references as ref


class ManuscriptReferenceAudit(unittest.TestCase):
    def make_corpus(self, root:Path,chapter=r'\section{A}\label{sec:a}\cite{Key}'):
        d=root/'manuscript'
        d.mkdir()
        (d/'BGS_unified.tex').write_text(
            r'\input{chapter.tex}\input{bib.tex}',encoding='utf-8')
        (d/'chapter.tex').write_text(chapter,encoding='utf-8')
        (d/'bib.tex').write_text(
            r'\begin{thebibliography}{99}\bibitem{Key} Source'
            r'\end{thebibliography}',encoding='utf-8')
        return d

    def test_positive_inline_and_preserved_escaped_percent(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.make_corpus(root,
                r'\section{A}\label{sec:a}\ref{sec:a}'
                '\n'+r'\% text % \cite{missing}'+'\n'+r'\cite{Key}')
            report=ref.audit(root)
            self.assertEqual(report['errors'],[])
            self.assertEqual(report['input_files'],2)
            self.assertEqual(report['cited_keys'],1)
            self.assertEqual(report['unresolved_labels'],[])

    def test_missing_citation_source_and_duplicate_bibitem_fail(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            d=self.make_corpus(root,r'\cite{Unknown}\input{missing.tex}')
            with (d/'bib.tex').open('a') as f:
                f.write('\n'+r'\bibitem{Key} Duplicate')
            errors=ref.audit(root)['errors']
            self.assertTrue(any('Unresolved citation Unknown' in e for e in errors))
            self.assertTrue(any('Missing TeX include' in e for e in errors))
            self.assertTrue(any('Duplicate bibliography key Key' in e for e in errors))

    def test_literal_verbatim_and_comment_are_ignored(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.make_corpus(root,
                r'\cite{Key} % \cite{NotUsed}'+'\n'
                r'\begin{verbatim}'+'\n'
                r'\input{not-a-file.tex} \cite{Other}'+'\n'
                r'\end{verbatim}')
            report=ref.audit(root)
            self.assertEqual(report['errors'],[])
            self.assertEqual(report['cited_keys'],1)

    def test_include_cycle_and_duplicate_labels_reported(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            d=self.make_corpus(root,
                r'\label{dup}\label{dup}\ref{never}\input{BGS_unified.tex}')
            report=ref.audit(root)
            self.assertTrue(any('Cyclic TeX include:' in e for e in report['errors']))
            self.assertEqual(report['duplicate_labels'],['dup'])
            self.assertEqual(report['unresolved_labels'],['never'])


if __name__ == '__main__':
    unittest.main()
