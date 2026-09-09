import importlib.util
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "lint_dag", Path("scripts") / "lint_dag.py")
LINT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(LINT)


def build(root: Path):
    """Minimal valid mini-wiki fixture."""
    root.joinpath("sources").mkdir(parents=True)
    root.joinpath("theory", "theorems").mkdir(parents=True)
    root.joinpath("problems", "demo-problem", "attempts").mkdir(parents=True)
    root.joinpath("scripts").mkdir()

    root.joinpath("sources", "demo-src.md").write_text(
        "---\ntype: source\nid: demo-src\ntitle: t\n"
        "author: a\ndate: 2026-09-09\n"
        "provenance: p\ntags: [demo-src-tag]\n---\n"
        "[demo-src-claim] body\n", encoding="utf-8")
    root.joinpath("theory", "theorems", "demo-thm.md").write_text(
        "---\ntype: theorem\nname: demo-thm\ncreated: 2026-09-09\n"
        "tags: [t]\nused-in: [[demo_problem]]\n"
        "provenance: [[demo-src]]\n---\nStatement.\n", encoding="utf-8")
    root.joinpath("problems", "demo-problem", "problem.md").write_text(
        "---\ntype: problem\nslug: demo-problem\ntitle: t\n"
        "status: in-progress\ndifficulty: medium\ncreated: 2026-09-09\n"
        "last-updated: 2026-09-09\ntags: [t]\n"
        "tools: [[demo-thm]]\nrelated: []\n---\n"
        "Uses [demo-src-tag].\n", encoding="utf-8")
    root.joinpath("problems", "demo-problem", "dag.md").write_text(
        "---\ntype: dag\nproblem: demo-problem\n"
        "last-updated: 2026-09-09\n---\n"
        "- id: demo-thm\n"
        "  kind: theorem\n"
        "  status: proven\n"
        "  uses: []\n"
        "  source: [[demo-thm]]\n"
        "  next: -\n"
        "- id: demo-conj\n"
        "  kind: conjecture\n"
        "  status: open\n"
        "  uses: [demo-thm]\n"
        "  source: problems/demo-problem/dag.md\n"
        "  next: prove it\n", encoding="utf-8")
    root.joinpath("problems", "demo-problem", "attempts",
                  "attempt-01.md").write_text(
        "---\ntype: attempt\nproblem: demo-problem\nattempt: 01\n"
        "date: 2026-09-09\napproach: a\noutcome: partial\n"
        "tags: [t]\n---\nCites [[demo-thm]] and [demo-src-tag].\n",
        encoding="utf-8")
    root.joinpath("index.md").write_text(
        "# Index\n"
        "- [demo thm](theory/theorems/demo-thm.md) — x\n"
        "- [demo problem](problems/demo-problem/problem.md) — x\n"
        "- [attempt 01](problems/demo-problem/attempts/attempt-01.md) — x\n"
        "- [dag](problems/demo-problem/dag.md) — x\n"
        "- [source](sources/demo-src.md) — x\n", encoding="utf-8")
    root.joinpath("log.md").write_text(
        "# Log\n\n## [INIT 2026-09-09] scaffold\nReady.\n", encoding="utf-8")


class LintTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        build(self.tmp)

    def report(self):
        return LINT.run_lint(self.tmp)

    def test_clean_wiki_passes(self):
        self.assertEqual(self.report().blockers, [])

    def test_broken_wikilink_is_blocker(self):
        p = self.tmp / "problems" / "demo-problem" / "problem.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n[[no-such-page]]\n",
                     encoding="utf-8")
        self.assertTrue(any("no-such-page" in b
                            for b in self.report().blockers))

    def test_undefined_claim_tag_is_blocker(self):
        p = self.tmp / "problems" / "demo-problem" / "problem.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n[ghost-tag].\n",
                     encoding="utf-8")
        self.assertTrue(any("ghost-tag" in b
                            for b in self.report().blockers))

    def test_missing_frontmatter_is_blocker(self):
        self.tmp.joinpath("theory", "theorems", "orphan.md").write_text(
            "no frontmatter\n", encoding="utf-8")
        self.assertTrue(any("orphan.md" in b
                            for b in self.report().blockers))

    def test_page_missing_from_index_is_blocker(self):
        self.tmp.joinpath("theory", "theorems", "extra.md").write_text(
            "---\ntype: theorem\nname: extra\ncreated: 2026-09-09\n"
            "tags: [t]\nused-in: [[demo_problem]]\nprovenance: []\n"
            "---\nS\n", encoding="utf-8")
        self.assertTrue(any("extra" in b
                            for b in self.report().blockers))

    def test_bad_log_prefix_is_blocker(self):
        self.tmp.joinpath("log.md").write_text(
            "# Log\n\n## [not-a-date]\nbad\n", encoding="utf-8")
        self.assertTrue(any("log.md" in b
                            for b in self.report().blockers))

    def test_dag_status_mismatch_is_blocker(self):
        self.tmp.joinpath("theory", "theorems", "demo-thm.md").write_text(
            "---\ntype: conjecture\nname: demo-thm\nstatus: open\n"
            "created: 2026-09-09\ntags: [t]\nused-in: [[demo_problem]]\n"
            "raised-by: [[demo_problem]]\nevidence: none\n---\nS\n",
            encoding="utf-8")
        self.assertTrue(self.report().blockers,
                        msg="proven dag node must anchor to a "
                            "theorem/lemma page or proven conjecture")

    def test_uncited_source_tag_is_warning_not_blocker(self):
        p = self.tmp / "sources" / "demo-src.md"
        p.write_text(p.read_text(encoding="utf-8").replace(
            "tags: [demo-src-tag]", "tags: [demo-src-tag, uncited-tag]"),
            encoding="utf-8")
        r = self.report()
        self.assertEqual(r.blockers, [], msg=str(r.blockers))
        self.assertTrue(any("uncited-tag" in w for w in r.warnings))

    def test_ci_flag_prints_blockers_only(self):
        buf = StringIO()
        with redirect_stdout(buf):
            code = LINT.main(["--root", str(self.tmp), "--ci"])
        self.assertEqual(code, 0)
        self.assertNotIn("warning", buf.getvalue().lower())


    def test_multiline_uses_list_fully_validated(self):
        p = self.tmp / "problems" / "demo-problem" / "dag.md"
        old = "  uses: [demo-thm]\n"
        new = "  uses:\n    - demo-thm\n    - ghost-node\n"
        p.write_text(p.read_text(encoding="utf-8").replace(old, new, 1),
                     encoding="utf-8")
        self.assertTrue(any("ghost-node" in b
                            for b in self.report().blockers))

if __name__ == "__main__":
    unittest.main()
