#!/usr/bin/env python3
"""Lint a chapter file against the conventions of PLAN.md.

Usage: tools/lint.py chapters/chNN_slug.tex [more files]
Exit status 0 iff no violations.

Checks:
  * no em dash or en dash characters, no '---' or '--' ligatures (outside verbatim/lstlisting/comments)
  * no Unicode mathematics or other non-ASCII characters (the source is ASCII LaTeX)
  * no \\input, \\include, \\usepackage, \\newcommand, \\renewcommand, \\def, \\DeclareMathOperator,
    \\newtheorem, \\begin{document}, \\bibliography in a chapter
  * exactly one \\chapter, with \\label{ch:slug} matching the file name
  * every \\label is prefixed by the chapter slug (ch:slug is the only exception)
  * cross-chapter references only through \\Cref{ch:...} / \\ref{ch:...}
  * the two unnumbered sections 'Core results at a glance' and 'Where the paper uses this chapter' exist
  * sections 'Exercises' and 'Notes and references' exist
  * balanced \\begin/\\end environments
"""
import re
import sys
import os

FORBIDDEN = [r'\\input\b', r'\\include\b', r'\\usepackage\b', r'\\newcommand\b', r'\\renewcommand\b',
             r'\\def\\', r'\\DeclareMathOperator\b', r'\\newtheorem\b', r'\\begin\{document\}',
             r'\\bibliography\b', r'\\documentclass\b', r'\\providecommand\b', r'\\let\\']

def strip_verbatim_and_comments(lines):
    """Return list of (lineno, text) with verbatim/lstlisting bodies blanked and comments removed."""
    out = []
    inverb = False
    for i, line in enumerate(lines, 1):
        if inverb:
            if re.search(r'\\end\{(verbatim|lstlisting)\}', line):
                inverb = False
            out.append((i, ''))
            continue
        if re.search(r'\\begin\{(verbatim|lstlisting)\}', line):
            inverb = True
            out.append((i, ''))
            continue
        # remove \verb|...| content
        line2 = re.sub(r'\\verb(.)(.*?)\1', '', line)
        # remove comments (unescaped %)
        line2 = re.sub(r'(?<!\\)%.*$', '', line2)
        out.append((i, line2))
    return out

def lint(path):
    problems = []
    with open(path, encoding='utf-8', errors='replace') as fh:
        raw = fh.read()
    lines = raw.split('\n')
    base = os.path.basename(path)
    m = re.match(r'ch([0-9A-Z]+)_([a-z]+)\.tex$', base)
    if not m:
        problems.append((0, f'file name {base} does not match chNN_slug.tex'))
        slug = None
    else:
        slug = m.group(2)

    # non-ASCII anywhere (including comments and verbatim: the source must be ASCII)
    for i, line in enumerate(lines, 1):
        for ch in line:
            if ord(ch) > 127:
                problems.append((i, f'non-ASCII character {ch!r} (U+{ord(ch):04X}); use LaTeX macros'))
                break

    cleaned = strip_verbatim_and_comments(lines)
    for i, text in cleaned:
        if '---' in text:
            problems.append((i, "em dash ligature '---' is forbidden"))
        elif '--' in text:
            problems.append((i, "en dash ligature '--' is forbidden (use a hyphen or rewrite)"))
        for pat in FORBIDDEN:
            if re.search(pat, text):
                problems.append((i, f'forbidden command matching {pat}'))

    body = '\n'.join(t for _, t in cleaned)
    chapters = re.findall(r'\\chapter\{', body)
    if len(chapters) != 1:
        problems.append((0, f'expected exactly one \\chapter, found {len(chapters)}'))
    if slug:
        if not re.search(r'\\label\{ch:' + re.escape(slug) + r'\}', body):
            problems.append((0, f'missing \\label{{ch:{slug}}} after \\chapter'))
    # labels
    for i, text in cleaned:
        for lab in re.findall(r'\\label\{([^}]*)\}', text):
            if lab.startswith('ch:'):
                if slug and lab != 'ch:' + slug:
                    problems.append((i, f'label {lab} defines another chapter label'))
                continue
            parts = lab.split(':')
            if slug and (len(parts) < 3 or parts[1] != slug):
                problems.append((i, f'label {lab} is not of the form kind:{slug}:name'))
        for ref in re.findall(r'\\(?:[cC]ref|ref|eqref|autoref|pageref)\{([^}]*)\}', text):
            for lab in ref.split(','):
                lab = lab.strip()
                if lab.startswith('ch:'):
                    continue
                parts = lab.split(':')
                if slug and (len(parts) < 3 or parts[1] != slug):
                    problems.append((i, f'reference to {lab}: cross-chapter references must use ch:slug only'))
    # required sections (numbered chapters only; appendices are free-form)
    numbered = bool(m and m.group(1).isdigit())
    if numbered:
        for title in ['Core results at a glance', 'Where the paper uses this chapter']:
            if not re.search(r'\\section\*\{' + re.escape(title), body):
                problems.append((0, f"missing unnumbered section '{title}'"))
        for title in ['Exercises', 'Notes and references']:
            if not re.search(r'\\section\{' + re.escape(title), body):
                problems.append((0, f"missing section '{title}'"))
    # balanced environments
    stack = []
    for i, text in cleaned:
        for kind, env in re.findall(r'\\(begin|end)\{([A-Za-z*]+)\}', text):
            if kind == 'begin':
                stack.append((env, i))
            else:
                if not stack or stack[-1][0] != env:
                    problems.append((i, f'\\end{{{env}}} does not match an open environment'))
                    if stack and stack[-1][0] != env:
                        # try to recover
                        for k in range(len(stack) - 1, -1, -1):
                            if stack[k][0] == env:
                                del stack[k:]
                                break
                else:
                    stack.pop()
    for env, i in stack:
        problems.append((i, f'\\begin{{{env}}} is never closed'))
    return problems

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total = 0
    for path in sys.argv[1:]:
        probs = lint(path)
        total += len(probs)
        if probs:
            print(f'{path}: {len(probs)} problem(s)')
            for i, msg in probs[:200]:
                print(f'  line {i}: {msg}')
            if len(probs) > 200:
                print(f'  ... and {len(probs) - 200} more')
        else:
            print(f'{path}: clean')
    sys.exit(1 if total else 0)

if __name__ == '__main__':
    main()
