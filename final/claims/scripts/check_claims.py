#!/usr/bin/env python3
"""Validate the claim ledger final/claims/claims.csv (and claims.yaml) against the paper, the book and the pipeline.

Usage (from any directory):
    python3 final/claims/scripts/check_claims.py              # validate; exit 1 on any failure
    python3 final/claims/scripts/check_claims.py --write-yaml # rewrite claims.yaml from claims.csv, then validate
    python3 final/claims/scripts/check_claims.py --compile    # recompile note.tex (latexmk, temporary outdir) first

Checks:
  1. claims.csv: UTF-8, the fixed header, unique ids of the form P-/C-/X-, kind and status in the vocabulary.
  2. paper_label is defined by \\label in final/paper/note.tex and paper_page equals the page of its \\newlabel entry
     in note.aux. If note.tex is newer than note.aux (or --compile is given), note.tex is compiled with latexmk into a
     temporary directory and that aux is used; the paper directory is not written to.
  3. book_location: each ';'-separated item is "<chapter label> <book label>"; the chapter label is defined by a
     \\chapter in final/book/chapters/*.tex and the book label is defined by \\label in that same chapter file.
  4. script: each item is a path under final/pipeline (scripts/...) that exists, or "book:<name>", a script of the book
     whose name occurs in final/book/chapters/*.tex. output: each item is a path under final/pipeline that exists.
  5. evidence is in its vocabulary; it is required for kind computation/example and for status computed/empirical,
     and must be empty otherwise. imported_from is required when status is imported.
  6. short_statement is nonempty and at most 200 characters; human_review is nonempty.
  7. claims.yaml holds exactly the same rows, in the same order, as claims.csv.
Prints the row counts by kind, status and evidence.
"""
import argparse, collections, csv, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLAIMS = HERE.parent
FINAL = CLAIMS.parent
PAPER = FINAL / 'paper'
CHAPTERS = FINAL / 'book' / 'chapters'
PIPELINE = FINAL / 'pipeline'

COLS = ['id', 'kind', 'paper_label', 'paper_page', 'short_statement', 'hypotheses', 'status',
        'imported_from', 'book_location', 'script', 'output', 'evidence', 'human_review', 'notes']
KINDS = {'statement', 'computation', 'example'}
STATUS = ['proved-in-paper', 'proved-in-book', 'imported', 'conjectural', 'empirical', 'computed']
EVIDENCE = ['quoted', 'saved-output', 'regenerated', 'independently-recomputed']

errors = []
def err(rid, msg):
    errors.append(f'{rid}: {msg}')


def split_items(s):
    return [x.strip() for x in s.split(';') if x.strip()]


# ------------------------------------------------------------------ YAML (a fixed, simple dialect)
def yaml_dump(rows):
    out = ['# Claim ledger for final/paper/note.tex; same content as claims.csv (see README.md).',
           '# Every value is a double-quoted string (JSON escaping, valid YAML).']
    for r in rows:
        first = True
        for c in COLS:
            out.append(('- ' if first else '  ') + f'{c}: ' + json.dumps(r[c], ensure_ascii=False))
            first = False
    return '\n'.join(out) + '\n'


def yaml_load(text):
    """Parse the dialect written by yaml_dump; use PyYAML as a cross-check when it is installed."""
    rows, cur = [], None
    for ln, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        m = re.match(r'^(- |  )([a-z_]+): (".*")$', line)
        if not m:
            raise ValueError(f'claims.yaml line {ln}: unexpected format')
        if m.group(1) == '- ':
            cur = {}
            rows.append(cur)
        cur[m.group(2)] = json.loads(m.group(3))
    try:
        import yaml
        parsed = yaml.safe_load(text)
        if parsed != rows:
            raise ValueError('claims.yaml: PyYAML and the dialect parser disagree')
    except ImportError:
        pass
    return rows


# ------------------------------------------------------------------ paper
def load_aux(compile_first):
    tex, aux = PAPER / 'note.tex', PAPER / 'note.aux'
    stale = (not aux.exists()) or tex.stat().st_mtime > aux.stat().st_mtime
    tmp = None
    if compile_first or stale:
        if not shutil.which('latexmk'):
            sys.exit('note.aux is stale or missing and latexmk is not available')
        tmp = Path(tempfile.mkdtemp(prefix='note_aux_'))
        print(f'compiling note.tex with latexmk into {tmp} (note.aux {"stale" if stale else "present"})')
        r = subprocess.run(['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', f'-outdir={tmp}', 'note.tex'],
                           cwd=PAPER, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if r.returncode != 0:
            sys.exit('latexmk failed:\n' + r.stdout[-3000:])
        aux = tmp / 'note.aux'
    pages = {}
    for line in aux.read_text(encoding='utf-8', errors='replace').splitlines():
        m = re.match(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]*)\}', line)
        if m:
            pages[m.group(1)] = m.group(3)
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)
    return pages, aux


def tex_labels(path):
    return set(re.findall(r'\\label\{([^}]+)\}', path.read_text(encoding='utf-8')))


# ------------------------------------------------------------------ book
def load_book():
    chapter_of = {}      # chapter label -> set of labels defined in that file
    alltext = []
    for f in sorted(CHAPTERS.glob('*.tex')):
        s = f.read_text(encoding='utf-8')
        alltext.append(s)
        m = re.search(r'\\chapter(?:\[[^\]]*\])?\{.*?\}\s*\\label\{(ch:[^}]+)\}', s, re.S)
        if m:
            chapter_of[m.group(1)] = set(re.findall(r'\\label\{([^}]+)\}', s))
    return chapter_of, '\n'.join(alltext).replace('\\_', '_')   # LaTeX writes moddeg\_check.py


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--write-yaml', action='store_true', help='rewrite claims.yaml from claims.csv before checking')
    ap.add_argument('--compile', action='store_true', help='recompile note.tex (temporary outdir) before reading the aux')
    a = ap.parse_args()

    raw = (CLAIMS / 'claims.csv').read_bytes()
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        sys.exit(f'claims.csv is not UTF-8: {e}')
    rdr = csv.DictReader(text.splitlines())
    if rdr.fieldnames != COLS:
        sys.exit(f'claims.csv header {rdr.fieldnames} differs from {COLS}')
    rows = list(rdr)

    if a.write_yaml:
        (CLAIMS / 'claims.yaml').write_text(yaml_dump(rows), encoding='utf-8')
        print('wrote claims.yaml')

    pages, auxpath = load_aux(a.compile)
    labels_tex = tex_labels(PAPER / 'note.tex')
    chapter_of, booktext = load_book()

    seen = set()
    for i, r in enumerate(rows, 2):
        rid = r['id'] or f'line {i}'
        if None in r.values() or len(r) != len(COLS):
            err(rid, 'wrong number of fields')
            continue
        if not re.fullmatch(r'[PCX]-\S+', r['id']):
            err(rid, 'id must start with P-, C- or X- and contain no spaces')
        if r['id'] in seen:
            err(rid, 'duplicate id')
        seen.add(r['id'])
        if r['kind'] not in KINDS:
            err(rid, f'kind {r["kind"]!r} not in {sorted(KINDS)}')
        # paper label and page
        lab = r['paper_label']
        if lab not in labels_tex:
            err(rid, f'paper_label {lab!r} is not a \\label in note.tex')
        elif lab not in pages:
            err(rid, f'paper_label {lab!r} has no \\newlabel in {auxpath}')
        elif pages[lab] != r['paper_page']:
            err(rid, f'paper_page {r["paper_page"]} but note.aux gives {pages[lab]} for {lab}')
        # status, evidence, imports
        if r['status'] not in STATUS:
            err(rid, f'status {r["status"]!r} not in the vocabulary')
        needs_ev = r['kind'] in ('computation', 'example') or r['status'] in ('computed', 'empirical')
        if r['evidence']:
            if r['evidence'] not in EVIDENCE:
                err(rid, f'evidence {r["evidence"]!r} not in the vocabulary')
            if not needs_ev:
                err(rid, 'evidence given for a row that is not a computation')
        elif needs_ev:
            err(rid, 'evidence missing for a computational row')
        if r['status'] == 'imported' and not r['imported_from'].strip():
            err(rid, 'status imported but imported_from is empty')
        # text fields
        if not r['short_statement'].strip():
            err(rid, 'short_statement empty')
        if len(r['short_statement']) > 200:
            err(rid, f'short_statement has {len(r["short_statement"])} > 200 characters')
        if not r['human_review'].strip():
            err(rid, 'human_review empty')
        # book locations
        for item in split_items(r['book_location']):
            parts = item.split()
            if len(parts) != 2:
                err(rid, f'book_location item {item!r} is not "<chapter label> <book label>"')
                continue
            ch, bl = parts
            if ch not in chapter_of:
                err(rid, f'book chapter label {ch!r} not found')
            elif bl not in chapter_of[ch]:
                err(rid, f'book label {bl!r} is not defined in the file of {ch}')
        # scripts and outputs
        for item in split_items(r['script']):
            if item.startswith('book:'):
                name = item[5:]
                if not name or name not in booktext:
                    err(rid, f'book script {name!r} not named in the book chapters')
            else:
                if not item.startswith('scripts/'):
                    err(rid, f'script {item!r} is not under final/pipeline/scripts')
                if not (PIPELINE / item).is_file():
                    err(rid, f'script {item!r} does not exist under final/pipeline')
        for item in split_items(r['output']):
            if not item.split('/')[0] in ('results', 'tables', 'samples'):
                err(rid, f'output {item!r} is not under results/, tables/ or samples/')
            if not (PIPELINE / item).is_file():
                err(rid, f'output {item!r} does not exist under final/pipeline')

    # YAML
    ypath = CLAIMS / 'claims.yaml'
    if not ypath.exists():
        err('claims.yaml', 'missing (run with --write-yaml)')
    else:
        try:
            yrows = yaml_load(ypath.read_text(encoding='utf-8'))
            if yrows != [dict(r) for r in rows]:
                err('claims.yaml', 'content differs from claims.csv (run with --write-yaml)')
        except ValueError as e:
            err('claims.yaml', str(e))

    # report
    print(f'{len(rows)} rows; paper pages from {auxpath}')
    for col in ('kind', 'status', 'evidence'):
        c = collections.Counter(r[col] or '(none)' for r in rows)
        print(f'  by {col}: ' + ', '.join(f'{k} {v}' for k, v in sorted(c.items())))
    se = collections.Counter((r['status'], r['evidence'] or '-') for r in rows if r['evidence'])
    print('  computational rows by (status, evidence): ' + ', '.join(f'{s}/{e} {n}' for (s, e), n in sorted(se.items())))
    if errors:
        print(f'FAIL: {len(errors)} problem(s)')
        for e in errors:
            print('  ' + e)
        sys.exit(1)
    print('check_claims: ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
