export const meta = {
  name: 'write-book-chapters',
  description: 'Write textbook chapters from their outlines, then review (sceptical mathematician + editor), fix and re-review until clean',
  phases: [
    { title: 'Write', detail: 'one agent per chapter writes the LaTeX from its outline, compiles and lints it' },
    { title: 'Review', detail: 'sceptical mathematician and editor in parallel' },
    { title: 'Fix', detail: 'apply findings, recompile, re-review the mathematics (up to three rounds)' },
  ],
}

// Usage (from a Claude Code session in the repository):
//   Workflow({ scriptPath: "tools/workflows/write_chapters.js",
//              args: { chapters: [ { num: "10", slug: "reduction", title: "Elliptic curves over local fields: reduction, Kodaira types, Tate curves" } ] } })
// num is "01".."22"; titles and slugs are in PLAN.md Section 4. Run three chapters at a time.

const REPO = args.repo || '/home/user/modular_math_book'
const chapters = args.chapters

const CONTEXT = (ch) => `
You are one of the agents writing a graduate-level mathematics textbook in LaTeX, in the git repository ${REPO}.
Never run any git command (the orchestrator commits). Edit only the files named for your task. Never edit
preamble.tex, main.tex, PLAN.md, refs.bib, the outlines or the files in important/.

The book takes a reader with first courses in real analysis, linear algebra and complex analysis, basic
statistics and Riley-Hobson-Bence to the point of reading, with full understanding, the research note
"Local factors of the adjoint L-function and the l-adic valuations of the modular degree" (D. Soni). The
original version is ${REPO}/note_Oct10_7pm.tex; the revised version with the stronger results is
${REPO}/paper/note_v2.tex (labels are the same; when the two differ, follow the revised version and decision
D1 below). The book is read online and used as a reference by experts: every chapter opens with a card of
precise statements.

Your chapter: Chapter ${ch.num} "${ch.title}", label ch:${ch.slug}, file chapters/ch${ch.num}_${ch.slug}.tex.

Read before doing anything else, in this order:
1. ${REPO}/PLAN.md in full. Sections 7.1 to 7.4 are the writing conventions (structure of a chapter, labels,
   citations, environments, the strict typography rules: no em dash or en dash in any form, never "---" or
   "--", ASCII-only source). Section 7.5 lists binding decisions: B14 (bibliography), B17 (lem:crit is proved in
   Chapter 15), B2 (Jordan-Holder in Chapter 3), B24 (Appendix B conventions), D1 (where the book proves more
   than the paper states, the book states its stronger version as the theorem and a Commentary gives the
   paper's statement), D2 (length is a guideline, not a cap: write as long as a clear explanation and complete
   proofs need, never padding), D3 (quadratic characters chi_d by discriminant, chi_{q*}, never chi_q; chi_l is
   the cyclotomic character), D4 (Manin constant c_E > 0).
2. Your chapter's outline ${REPO}/outlines/ch${ch.num}_${ch.slug}.md in full. It is the specification: every
   line-up item must be written, with the statement as given there (improve it only where it is wrong, and say
   so in your report), in the planned order and at the planned level of rigour.
3. ${REPO}/outlines/chB_notation.md, Parts 1 and 2 (the binding conventions B-C1 to B-C16 and the symbol
   index): Frob is arithmetic, Phi = Frob^{-1} geometric, L-factors use Phi; ^vee linear dual, ^* Pontryagin dual,
   ^D Kummer dual, ^dagger adjoint; J_f for the abelian variety, A_f for the adjoint; and the rest.
4. ${REPO}/important/paper_memo.md: the final, reconciled list of corrections and strengthenings of the paper.
   Wherever your chapter states something the paper uses, state the CORRECT version (never repeat an error
   listed in Section B or C of the memo).
5. The paper (both versions) where your outline's paper hooks point, and ${REPO}/preamble.tex (the only macros
   available; chapters define none).
6. The outlines of the neighbouring chapters, to cite them correctly: cite other chapters only by
   \\Cref{ch:slug} and, in prose, by their outline item numbers ("Chapter 14, item 9.3") where useful.
`

const WRITE_SCHEMA = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    lines: { type: 'integer' },
    pages: { type: 'integer' },
    compiled: { type: 'boolean', description: 'tools/build_chapter.sh printed RESULT: OK' },
    lint_clean: { type: 'boolean', description: 'tools/lint.py printed clean' },
    items_written: { type: 'array', items: { type: 'string' } },
    omitted: { type: 'array', items: { type: 'string' }, description: 'outline items not written, with the reason' },
    outline_corrections: { type: 'array', items: { type: 'string' }, description: 'places where the outline was wrong and what the chapter says instead' },
    concerns: { type: 'array', items: { type: 'string' } },
    new_paper_points: { type: 'array', items: { type: 'string' }, description: 'problems in the paper not already in paper_memo.md' },
    bib_keys_added: { type: 'array', items: { type: 'string' } },
  },
  required: ['file', 'lines', 'pages', 'compiled', 'lint_clean', 'items_written', 'omitted', 'outline_corrections', 'concerns', 'new_paper_points', 'bib_keys_added'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          location: { type: 'string' },
          claim: { type: 'string' },
          problem: { type: 'string' },
          severity: { type: 'string', enum: ['blocking', 'major', 'minor'] },
          suggested_fix: { type: 'string' },
        },
        required: ['location', 'claim', 'problem', 'severity', 'suggested_fix'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['findings', 'summary'],
}

const FIX_SCHEMA = {
  type: 'object',
  properties: {
    applied: { type: 'array', items: { type: 'string' } },
    rejected: { type: 'array', items: { type: 'object', properties: { finding: { type: 'string' }, reason: { type: 'string' } }, required: ['finding', 'reason'] } },
    compiled: { type: 'boolean' },
    lint_clean: { type: 'boolean' },
    lines: { type: 'integer' },
    notes: { type: 'string' },
  },
  required: ['applied', 'rejected', 'compiled', 'lint_clean', 'lines', 'notes'],
}

const writePrompt = (ch) => `${CONTEXT(ch)}

YOUR TASK: WRITE THE CHAPTER, in full, to ${REPO}/chapters/ch${ch.num}_${ch.slug}.tex.

Structure (PLAN.md 7.1): \\chapter{${ch.title}}\\label{ch:${ch.slug}}; then \\section*{Core results at a glance}
(an enumerate with label=\\textbf{\\thechapter.\\arabic*}: one item per core result with its precise statement,
its rigour tag in italics and a \\Cref to the numbered environment); \\section*{Where the paper uses this chapter};
the numbered sections of the outline's section plan, each opening with a paragraph on its purpose and its use
in the paper, with \\begin{paperlink} at each point where a result the paper needs is established; a
\\section{Exercises} with the outline's exercises (8 to 20); a \\section{Notes and references}.

Mathematics: full proofs for everything the outline marks "proved here"; for "proof sketched here", a sketch
in \\begin{proof}[Sketch of proof] with a precise reference; for "stated; reference", the exact statement and
"We do not prove this; see ...". Never present a sketch as a proof. Expand every step the paper compresses.
Verify the computations you print (examples, tables, curve data): PARI/GP is available through the Python
package cypari2, and Cremona's ecdata files for conductor below 10,000 are in ${REPO}/data/ecdata (run
tools/setup_env.sh if they are missing).

LaTeX: only the macros of preamble.tex; every \\label prefixed kind:${ch.slug}:name; cite with keys from refs.bib
and bib/ch${ch.num}.bib (decision B14: a key needed by one chapter only may be added to bib/ch${ch.num}.bib as a
complete, verified entry; never duplicate a key that exists in refs.bib or another chapter's bib file; check
with grep first). Code in \\begin{lstlisting}[language=GP]. Kodaira symbols \\kod{I}_n, \\kod{II}^*.

Write section by section, appending with quoted heredocs (cat >> file <<'EOF' ... EOF). When done:
python3 ${REPO}/tools/lint.py chapters/ch${ch.num}_${ch.slug}.tex (must be clean) and
${REPO}/tools/build_chapter.sh ${ch.num} (must print RESULT: OK; log in build/ch${ch.num}/chapter.log). Check that
the card lists every numbered theorem, proposition, lemma and corollary. Re-read the chapter once as the
sceptical expert who will review it and fix what you find. Return the structured output.`

const mathReviewPrompt = (ch, round) => `${CONTEXT(ch)}

YOUR TASK: ADVERSARIAL MATHEMATICAL REVIEW (round ${round}) of ${REPO}/chapters/ch${ch.num}_${ch.slug}.tex. Read it in
full (in pieces), with its outline and the paper where it is used. Try to refute every definition, statement,
proof step, example, computation (recompute with PARI where possible), exercise and claim about the paper;
check that statements on the card agree with the numbered environments; check every reference number you can.
Check against important/paper_memo.md that no corrected error of the paper is repeated and that the book's
strengthened versions (decision D1) are stated and proved correctly. Severity: "blocking" for a false statement,
a missing hypothesis that makes a statement false, an invalid step in a proof, a wrong definition; "major" for
a misleading statement, a wrong reference number, a sketch labelled as a proof, a gap, a convention violation of
Appendix B that changes meaning; "minor" otherwise. If unsure, report as "major" with your reasoning. Do NOT edit
any file. Return the structured output.`

const editReviewPrompt = (ch) => `${CONTEXT(ch)}

YOUR TASK: EDITORIAL AND TECHNICAL REVIEW of ${REPO}/chapters/ch${ch.num}_${ch.slug}.tex. Read it in full, with its
outline. Report concretely: (1) build and lint (run both; every error, undefined reference or citation, lint
problem, and overfull box wider than 20pt); (2) structure per PLAN.md 7.1 (card complete and precise, paper
section, purpose paragraphs, paperlinks, exercises, notes); (3) coverage against the outline: every line-up item
present at the planned rigour, nothing duplicated from neighbouring chapters; (4) audience: every term defined
before use here or in an earlier chapter, no jumps in difficulty; (5) conventions of Appendix B and decisions
D1 to D4; typography (no dashes of any kind, ASCII only); labels and citations; (6) explanations that would
benefit from more length or an example (decision D2), and any padding or repetition to cut. Do NOT edit any
file. Return the structured output.`

const fixPrompt = (ch, math, edit, round) => `${CONTEXT(ch)}

YOUR TASK: APPLY THE REVIEW FINDINGS (round ${round}) to ${REPO}/chapters/ch${ch.num}_${ch.slug}.tex (and, for a
bibliography entry needed by this chapter only, bib/ch${ch.num}.bib). Read the chapter first.

Mathematical review:
${JSON.stringify(math, null, 1)}

Editorial review:
${JSON.stringify(edit, null, 1)}

Apply every blocking and major finding and every minor finding that is clearly right; verify each before
applying (reviewers can be wrong; say why you reject one). Fix content, never delete it to dodge a finding: an
unrepairable proof becomes a labelled sketch with a reference; a missing result is written; a false statement is
replaced by the true one. Then run the linter and tools/build_chapter.sh ${ch.num} until both are clean and check
the card still matches. Return the structured output.`

const sev = (fs, levels) => (fs || []).filter(f => levels.includes(f.severity))

const results = await pipeline(
  chapters,
  ch => agent(writePrompt(ch), { label: `write:ch${ch.num}`, phase: 'Write', schema: WRITE_SCHEMA }),
  async (written, ch) => {
    const history = []
    let round = 1
    let [math, edit] = await parallel([
      () => agent(mathReviewPrompt(ch, round), { label: `math-review:ch${ch.num}:r1`, phase: 'Review', schema: REVIEW_SCHEMA }),
      () => agent(editReviewPrompt(ch), { label: `edit-review:ch${ch.num}`, phase: 'Review', schema: REVIEW_SCHEMA }),
    ])
    math = math || { findings: [], summary: 'unavailable' }
    edit = edit || { findings: [], summary: 'unavailable' }
    history.push({ round, math: math.findings.length, edit: edit.findings.length })
    let fix = null
    while (round <= 3) {
      const serious = sev(math.findings, ['blocking', 'major']).length + sev(edit.findings, ['blocking', 'major']).length
      const minor = sev(math.findings, ['minor']).length + sev(edit.findings, ['minor']).length
      if (serious + minor === 0) { log(`ch${ch.num}: round ${round} clean`); break }
      log(`ch${ch.num}: round ${round}: ${serious} serious, ${minor} minor; fixing`)
      fix = await agent(fixPrompt(ch, math, edit, round), { label: `fix:ch${ch.num}:r${round}`, phase: 'Fix', schema: FIX_SCHEMA })
      round += 1
      if (round > 3) break
      const again = await agent(mathReviewPrompt(ch, round), { label: `math-review:ch${ch.num}:r${round}`, phase: 'Fix', schema: REVIEW_SCHEMA })
      math = again || { findings: [], summary: 'unavailable' }
      edit = { findings: [], summary: 'editorial review done in round 1' }
      history.push({ round, math: math.findings.length })
      if (sev(math.findings, ['blocking', 'major']).length === 0) {
        if (math.findings.length > 0) {
          fix = await agent(fixPrompt(ch, math, edit, round), { label: `fix:ch${ch.num}:r${round}`, phase: 'Fix', schema: FIX_SCHEMA })
        }
        break
      }
    }
    return { chapter: ch.num, slug: ch.slug, written, review_history: history, last_fix: fix, remaining_findings: math.findings }
  },
)

return results.filter(Boolean)
