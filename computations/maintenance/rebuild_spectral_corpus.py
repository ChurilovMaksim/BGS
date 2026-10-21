#!/usr/bin/env python3
"""Reconstruct/check the final imported corpus from its lossless source archive.

No network or third-party dependencies. The archive preserves historical bytes;
Markdown projections make only the explicitly listed presentation repairs.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / 'record/spectral_research/catalog.json'
POLICY = {
    'explicit_delimiters': r'Unescaped \(...\), \[...\] become $...$, $$...$$ outside code.',
    'small_matrices': 'psmallmatrix becomes pmatrix (same entries and parentheses).',
    'repeated_arguments': r'Group ((\xi^a)^{[m_a]}) before indexing the tuple a=0,...,n-1.',
    'source_links': 'Resolve original source-relative links and master source-ID anchors to their individual edition targets.',
    'unchanged': 'Code fences, inline code, raw archived bytes, code and author evidence.',
}

def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def safe_path(rel: str) -> Path:
    p = ROOT / rel
    if Path(rel).is_absolute() or '..' in Path(rel).parts:
        raise ValueError('Unsafe corpus path: ' + rel)
    return p

def project_md(s: str) -> str:
    out: list[str] = []; block: list[str] = []; fence = None
    def flush() -> None:
        if not block: return
        parts = re.split(r'(`+[^`\n]*`+)', ''.join(block))
        for i in range(0, len(parts), 2):
            t = parts[i]
            # Negative lookbehind protects TeX row spacings such as \\[4pt].
            t = re.sub(r'(?<!\\)\\[\[\]]', '$$', t)
            t = re.sub(r'(?<!\\)\\[()]', '$', t)
            t = t.replace('{psmallmatrix}', '{pmatrix}')
            t = t.replace(r'(\xi^a)^{[m_a]}_{a=0}^{n-1}',
                          r'\bigl((\xi^a)^{[m_a]}\bigr)_{a=0}^{n-1}')
            parts[i] = t
        out.append(''.join(parts)); block.clear()
    for line in s.splitlines(keepends=True):
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            out.append(line)
            if m and m[1][0] == fence[0] and len(m[1]) >= len(fence): fence = None
        elif m:
            flush(); out.append(line); fence = m[1]
        else: block.append(line)
    flush()
    return ''.join(out)

def reconstruct(c: dict) -> bytes:
    chunks = []
    for part in c['original_parts']:
        compressed = safe_path(part['path']).read_bytes()
        if digest(compressed) != part['gzip_sha256']: raise ValueError('Archive gzip hash')
        raw = gzip.decompress(compressed)
        if len(raw) != part['raw_bytes'] or digest(raw) != part['raw_sha256']:
            raise ValueError('Archive part contents')
        chunks.append(raw)
    raw = b''.join(chunks)
    if len(raw) != c['source_bytes'] or digest(raw) != c['source_sha256']:
        raise ValueError('Complete source identity')
    return raw

def source_links(s: str, e: dict, entries: list[dict]) -> str:
    paths = {x['original_path']: x['target'] for x in entries}
    ids = {x['id']: x['target'] for x in entries}
    def link(m):
        target = m[2]; new = None
        if target.startswith('#') and target[1:] in ids:
            new = ids[target[1:]]
        elif not re.match(r'^[A-Za-z]+:', target):
            name, marker, fragment = target.partition('#')
            original = posixpath.normpath(posixpath.join(posixpath.dirname(e['original_path']), name))
            if original in paths:
                new = paths[original]
                if marker: new += '#' + fragment
        if new is None: return m[0]
        return m[1] + posixpath.relpath(new, posixpath.dirname(e['target'])) + ')'
    # Preserve fenced/inline code and explicit mathematics byte-for-byte.
    out = []; block = []; fence = None
    def flush():
        parts = re.split(r'(`+[^`\n]*`+|\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[\s\S]*?(?<!\\)\$)', ''.join(block))
        for i in range(0, len(parts), 2):
            parts[i] = re.sub(r'(\[[^\]\n]+\]\()([^\s)]+)\)', link, parts[i])
        out.append(''.join(parts)); block.clear()
    for line in s.splitlines(keepends=True):
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            out.append(line)
            if m and m[1][0] == fence[0] and len(m[1]) >= len(fence): fence = None
        elif m:
            flush(); out.append(line); fence = m[1]
        else: block.append(line)
    flush()
    return ''.join(out)

def projection(e: dict, raw: bytes, entries: list[dict]) -> bytes:
    start = e['raw_offset']; size = e['raw_bytes']
    if start < 0 or start + size > len(raw): raise ValueError('Invalid source slice')
    b = raw[start:start+size]
    if digest(b) != e['sha256']: raise ValueError('Source hash: ' + e['original_path'])
    mode = e['projection']
    if mode == 'byte-exact': return b
    if mode == 'gzip-byte-exact': return gzip.compress(b, mtime=0)
    s = b.decode('utf-8')
    if mode == 'container-front-matter':
        m = re.search(r'^# (?:Источник:|Приложение \d+[:.])', s, re.M)
        return source_links(project_md(s[:m.start()] if m else s), e, entries).encode()
    if mode != 'markdown-explicit-delimiters': raise ValueError('Unknown projection')
    level = 'Imported author proof or research attempt; consult the review matrix before using it as a theorem.'
    if e['classification'] == 'review-record':
        level = 'Imported research record or internal author audit; this is not a new independent review.'
    link = posixpath.relpath('mathematics/spectral_research/topics/' + e['topic'] + '.md',
                            posixpath.dirname(e['target']))
    prefix = (f'> Source status: {level}\n> Original source: `{e["original_path"]}`. '
              f'Embedded SHA256: `{e["sha256"]}`.\n> [Thematic guide]({link}).\n\n')
    return (prefix + source_links(project_md(s), e, entries)).encode()

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='Check every source/projection, without writing')
    ap.add_argument('--write', action='store_true', help='Regenerate projections and projection hashes')
    args = ap.parse_args()
    if args.check == args.write: ap.error('Choose exactly one of --check or --write')
    c = json.loads(CATALOG.read_text()); raw = reconstruct(c); failures = []; targets = set()
    for e in c['entries']:
        if e['target'] in targets: raise ValueError('Duplicate target: ' + e['target'])
        targets.add(e['target']); b = projection(e, raw, c['entries']); p = safe_path(e['target'])
        if args.write:
            p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
            e['projection_sha256'] = digest(b)
        elif not p.exists() or p.read_bytes() != b or digest(b) != e['projection_sha256']:
            failures.append(e['target'])
    if args.write:
        c['presentation_repairs'] = POLICY
        CATALOG.write_text(json.dumps(c, indent=2, ensure_ascii=False) + '\n')
    if failures: raise SystemExit('Projection mismatches: ' + ', '.join(failures))
    print(json.dumps({'source_sha256': digest(raw), 'bytes': len(raw),
                      'source_units': len(targets), 'mode': 'check' if args.check else 'write',
                      'historical_declared_hash_differences': sum(not e['verified'] for e in c['entries']),
                      'result': 'PASS'}))

if __name__ == '__main__': main()
