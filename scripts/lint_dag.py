#!/usr/bin/env python3
"""Deterministic structure verifier for the math wiki.

Report-only: never edits pages. Blockers fail CI; warnings never do.
Checks (spec 3.2): wikilink resolution, claim-tag definition,
frontmatter validity, index/log parity, dag status parity, orphans.
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

WIKILINK = re.compile(r"\[\[([A-Za-z0-9_\-]+)\]\]")
CLAIM_TAG = re.compile(r"(?<!\[)\[([a-z0-9][a-z0-9-]{2,40})\](?!\])(?!\()")
LOG_ENTRY = re.compile(r"^## \[([A-Z]+) (\d{4}-\d{2}-\d{2})\]")
FM_LINE = re.compile(r"^([A-Za-z_-]+):\s*(.*)$")
NODE_LINE = re.compile(r"-\s+id:\s*([A-Za-z0-9\-]+)\s*$")
FIELD_LINE = re.compile(r"([a-z_]+):\s*(.*)$")

RESERVED_TAGS = {"to-verify", "summary"}

REQUIRED = {
    # Extended to match SCHEMA.md frontmatter templates exactly (controller
    # ruling): problem += title/difficulty/tools/related; attempt += tags;
    # source += author/date. Theory pages: SCHEMA marks `provenance`
    # optional ("if external"), so the brief's dict stands there.
    "problem": ["type", "slug", "title", "status", "difficulty",
                "created", "last-updated", "tags", "tools", "related"],
    "attempt": ["type", "problem", "attempt", "date", "approach", "outcome",
                "tags"],
    "theorem": ["type", "name", "created", "tags", "used-in"],
    "lemma": ["type", "name", "created", "tags", "used-in"],
    "method": ["type", "name", "created", "tags", "used-in"],
    "definition": ["type", "name", "created", "tags", "used-in"],
    "conjecture": ["type", "name", "status", "raised-by", "created", "evidence"],
    "source": ["type", "id", "title", "author", "date", "provenance", "tags"],
    "dag": ["type", "problem", "last-updated"],
}

INDEXED_TYPES = {"problem", "theorem", "lemma", "method", "definition",
                 "conjecture", "source", "attempt", "dag"}
ROOT_BOOKKEEPING = {"index.md", "log.md", "board.md", "readme.md",
                    "qwen.md", "math wiki contribution plan.md",
                    "schema.md", "claude.md", "research-protocol.md",
                    "license.md"}


@dataclass
class LintReport:
    blockers: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


def _page_universe(root):
    """All governed pages: root-level + problems/ + theory/ + sources/."""
    out = list(root.glob("*.md"))
    for sub in ("problems", "theory", "sources"):
        out.extend((root / sub).rglob("*.md"))
    return out


def _pages(root):
    """slug (lower) -> page path, for wikilink resolution."""
    pages = {}
    for sub in ("theory", "sources"):
        for p in (root / sub).rglob("*.md"):
            pages.setdefault(p.stem.lower(), p)
    for p in (root / "problems").glob("*/problem.md"):
        pages.setdefault(p.parent.name.lower(), p)
    for p in (root / "problems").glob("*/wiki/**/*.md"):
        pages.setdefault(p.stem.lower(), p)
    for name in ("index.md", "SCHEMA.md", "README.md", "CLAUDE.md",
                 "research-protocol.md", "log.md", "BOARD.md"):
        p = root / name
        if p.exists():
            pages.setdefault(p.stem.lower(), p)
    return pages


def _resolve_link(slug, pages):
    for cand in (slug, slug.replace("_", "-"), slug.replace("-", "_")):
        hit = pages.get(cand.lower())
        if hit is not None:
            return hit
    return None


def _frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, False
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, False
    fm = {}
    for line in lines[1:end]:
        m = FM_LINE.match(line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, True


def run_lint(root):
    rep = LintReport()
    pages = _pages(root)
    texts = {}
    for p in _page_universe(root):
        try:
            texts[p] = p.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            rel = p.relative_to(root).as_posix()
            rep.blockers.append("unreadable: %s (%s)" % (rel, exc))
            texts[p] = ""
    index_text = texts.get(root / "index.md", "")

    defined_tags = set()
    for p, text in texts.items():
        if p.parent.name == "sources":
            defined_tags.update(t.lower() for t in CLAIM_TAG.findall(text))
            fm, ok = _frontmatter(text)
            if ok:
                for t in (fm.get("tags") or "").split(","):
                    t = t.strip().strip("[]").lower()
                    if t:
                        defined_tags.add(t)
    defined_tags.update(RESERVED_TAGS)

    cited_tags = set()
    for p, text in texts.items():
        if (len(rp := p.relative_to(root).parts) >= 2 and rp[0] in (
                "problems", "theory")
                and _frontmatter(text)[0].get("type") != "dag"):
            cited_tags.update(t.lower() for t in CLAIM_TAG.findall(text))

    for p, text in sorted(texts.items()):
        rel = p.relative_to(root).as_posix()

        for link in WIKILINK.findall(text):
            if _resolve_link(link, pages) is None:
                rep.blockers.append("%s: broken wikilink [[%s]]"
                                    % (rel, link))

        fm, ok = _frontmatter(text)
        if not ok:
            if p.name.lower() not in ROOT_BOOKKEEPING:
                rep.blockers.append("%s: missing frontmatter" % rel)
            continue
        ptype = fm.get("type", "")
        req = REQUIRED.get(ptype)
        if req is None:
            rep.warnings.append("%s: unknown page type '%s'" % (rel, ptype))
        else:
            missing = [k for k in req if k not in fm]
            if missing:
                rep.blockers.append("%s: frontmatter missing %s (type %s)"
                                    % (rel, missing, ptype))

        if (len(rp := p.relative_to(root).parts) >= 2
                and rp[0] in ("problems", "theory") and ptype != "dag"):
            for tag in CLAIM_TAG.findall(text):
                if tag.lower() not in defined_tags:
                    rep.blockers.append(
                        "%s: claim tag [%s] not defined in sources/"
                        % (rel, tag))

        if ptype in INDEXED_TYPES and "(%s)" % rel not in index_text:
            rep.blockers.append("%s: not cataloged in index.md" % rel)

        if ptype == "dag":
            _check_dag(p, text, texts, pages, rep)

    for i, line in enumerate(log_text := texts.get(root / "log.md", "")
                             .splitlines(), 1):
        if line.startswith("## [") and not LOG_ENTRY.match(line):
            rep.blockers.append("log.md line %d: unparseable entry '%s'"
                                % (i, line[:40]))

    for t in sorted(defined_tags - cited_tags):
        rep.warnings.append("sources: claim tag [%s] defined but never "
                            "cited" % t)

    for p in (root / "theory").rglob("*.md"):
        stem = p.stem.lower()
        alts = (stem, stem.replace("-", "_"), stem.replace("_", "-"))
        inbound = any(a in [l.lower() for l in WIKILINK.findall(t)]
                      for t in texts.values() for a in alts)
        if not inbound:
            fm, ok = _frontmatter(texts.get(p, ""))
            if ok and not (fm.get("used-in") or "").strip("[] \t"):
                rep.warnings.append("%s: orphan theory page"
                                    % p.relative_to(root).as_posix())

    return rep


def _check_dag(dag_path, text, texts, pages, rep):
    rel = dag_path.relative_to(dag_path.parents[2]).as_posix()
    nodes = []
    node = None
    for raw in text.splitlines():
        s = raw.strip()
        m = NODE_LINE.match(s)
        if m:
            if node:
                nodes.append(node)
            node = {"id": m.group(1)}
            continue
        if s.startswith("- ") and node is not None:
            nodes.append(node)
            node = None
            continue
        if node is not None and s:
            kv = FIELD_LINE.match(s)
            if kv and kv.group(1) in ("kind", "status", "uses", "source",
                                      "next") and kv.group(1) not in node:
                node[kv.group(1)] = kv.group(2)
    if node:
        nodes.append(node)

    ids = [nd.get("id") for nd in nodes]
    for nd in nodes:
        nid = nd.get("id", "?")
        status = nd.get("status", "open")
        if status not in ("open", "proven", "conditional", "dead"):
            rep.blockers.append("%s: node %s bad status '%s'"
                                % (rel, nid, status))
        if ids.count(nid) > 1:
            continue  # duplicate reported once below
        src = (nd.get("source") or "").strip()
        if not src:
            rep.blockers.append("%s: node %s has no source" % (rel, nid))
            continue
        for dep in re.findall(r"[A-Za-z0-9\-]+",
                              (nd.get("uses") or "").strip("[] ")):
            if dep not in ids:
                rep.blockers.append("%s: node %s uses undefined node '%s'"
                                    % (rel, nid, dep))
        if status != "proven":
            wl = WIKILINK.search(src)
            if wl:
                if _resolve_link(wl.group(1), pages) is None:
                    rep.blockers.append("%s: node %s source [[%s]] does "
                                        "not resolve"
                                        % (rel, nid, wl.group(1)))
            elif "/" in src:
                if not dag_path.parents[2].joinpath(src).exists():
                    rep.blockers.append("%s: node %s source '%s' does "
                                        "not resolve" % (rel, nid, src))
            else:
                rep.blockers.append("%s: node %s source '%s' unparseable"
                                    % (rel, nid, src))
            continue
        wl = WIKILINK.search(src)
        if not wl:
            rep.blockers.append("%s: proven node %s needs a wikilink "
                                "anchor to its theory/conjecture page "
                                "(got '%s')" % (rel, nid, src))
            continue
        target = _resolve_link(wl.group(1), pages)
        if target is None:
            rep.blockers.append("%s: proven node %s source [[%s]] does "
                                "not resolve" % (rel, nid, wl.group(1)))
            continue
        tfm, _ = _frontmatter(texts.get(target, ""))
        ttype = tfm.get("type")
        tstatus = tfm.get("status")
        if ttype not in ("theorem", "lemma") and not (
                ttype == "conjecture" and tstatus == "proven"):
            rep.blockers.append("%s: proven node %s but %s is type=%s "
                                "status=%s" % (rel, nid, target.name,
                                               ttype, tstatus))
        if "[to-verify]" in texts.get(target, ""):
            rep.blockers.append("%s: proven node %s but %s still carries "
                                "[to-verify]" % (rel, nid, target.name))
    for nid in set(ids):
        if ids.count(nid) > 1:
            rep.blockers.append("%s: duplicate node id %s" % (rel, nid))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=None)
    parser.add_argument("--ci", action="store_true",
                        help="print blockers only (warnings never fail)")
    args = parser.parse_args(argv)
    root = Path(args.root) if args.root else Path.cwd()
    rep = run_lint(root)
    for b in rep.blockers:
        print("BLOCKER: %s" % b)
    if not args.ci:
        for w in rep.warnings:
            print("warning: %s" % w)
        print("%d blocker(s), %d warning(s)"
              % (len(rep.blockers), len(rep.warnings)))
    return 1 if rep.blockers else 0


if __name__ == "__main__":
    sys.exit(main())
