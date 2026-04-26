#!/usr/bin/env python3
"""
convert_wikilinks.py — Obsidian vault → GitHub Pages build step.

Reads source files, converts [[wikilinks]] to relative markdown links,
replaces ```dataview blocks with static markdown tables, and writes
output to a build directory (default: _ghpages_build/).

Usage:
    python3 scripts/convert_wikilinks.py [--src REPO_ROOT] [--out BUILD_DIR]

The output directory is intended to be pushed to the gh-pages branch by
GitHub Actions, where GitHub Pages (Jekyll + jekyll-relative-links) will
render the .md links into correct HTML URLs.
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("PyYAML not found. Run: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)


# ── Regex patterns ───────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
WIKILINK_RE    = re.compile(r'\[\[([^\]]+)\]\]')
DATAVIEW_RE    = re.compile(r'```dataview\n(.*?)```', re.DOTALL)


# ── Dirs / files to skip in the build output ─────────────────────────────────

IGNORE_DIRS  = {'.git', '.github', 'node_modules', '__pycache__', '.obsidian', 'scripts', '_ghpages_build', '_site'}
IGNORE_FILES = {'CLAUDE.md'}   # internal planning doc — not for public consumption


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify_to_title(slug: str) -> str:
    """'apr-23' → 'Apr 23', 'sun-moon-lake' → 'Sun Moon Lake'."""
    return ' '.join(w.capitalize() for w in slug.replace('-', ' ').split())


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


# ── Activity index ────────────────────────────────────────────────────────────

def build_activity_index(repo_root: Path) -> dict:
    """
    Returns a dict keyed by wikilink path (no .md suffix), e.g.:
        "cities/hualien/activities/dongdamen-night-market"
            → { name, city, tags, priority, cost_ntd, status, done, scheduled, ... }
    """
    index: dict = {}
    for f in repo_root.glob('cities/*/activities/*.md'):
        rel = f.relative_to(repo_root)
        key = str(rel).replace('\\', '/').removesuffix('.md')
        fm  = parse_frontmatter(f.read_text(encoding='utf-8'))
        index[key] = {**fm, '_rel_path': str(rel).replace('\\', '/')}
    return index


# ── Wikilink conversion ───────────────────────────────────────────────────────

def split_wikilink(inner: str):
    """
    Split a wikilink interior into (target_path, anchor, label).
    Handles:  path | label    path#anchor | label    path#anchor
    """
    label: Optional[str] = None
    if '|' in inner:
        target_str, label = inner.split('|', 1)
        label = label.strip()
    else:
        target_str = inner

    if '#' in target_str:
        path, anchor = target_str.split('#', 1)
        return path.strip().rstrip('\\'), anchor.strip(), label
    return target_str.strip().rstrip('\\'), None, label


def derive_label(target_path: str, anchor: Optional[str], activity_index: dict) -> str:
    """Human-readable label for a wikilink when no explicit label is given."""
    # Activity name from index
    if target_path in activity_index:
        name = activity_index[target_path].get('name', '')
        if name:
            return name

    last = target_path.rstrip('/').split('/')[-1]

    # "cities/hualien/index" → "Hualien"
    if last == 'index':
        parts = target_path.split('/')
        if len(parts) >= 2:
            return slugify_to_title(parts[-2])
        return 'Index'

    # anchor is more descriptive than the filename for logistics links
    # e.g. [[logistics/accommodation#hualien]] → "Hualien"
    if anchor:
        return slugify_to_title(anchor)

    return slugify_to_title(last)


def compute_rel_path(source_file: Path, target_path: str, repo_root: Path) -> str:
    """
    Relative .md path from source_file's directory to target_path (no .md suffix).
    Uses forward slashes (safe for markdown links on all platforms).
    """
    target_abs = repo_root / (target_path + '.md')
    rel        = os.path.relpath(target_abs, source_file.parent)
    return rel.replace('\\', '/')


def convert_wikilinks(content: str, source_file: Path, repo_root: Path, activity_index: dict) -> str:
    """Replace every [[wikilink]] with a standard [Label](relative/path.md) link."""

    def replacer(m):
        path, anchor, label = split_wikilink(m.group(1))

        if not label:
            label = derive_label(path, anchor, activity_index)

        rel = compute_rel_path(source_file, path, repo_root)

        if anchor:
            # Jekyll normalises heading anchors to lowercase-hyphenated
            anchor_slug = re.sub(r'[^a-z0-9]+', '-', anchor.lower()).strip('-')
            return f'[{label}]({rel}#{anchor_slug})'
        return f'[{label}]({rel})'

    return WIKILINK_RE.sub(replacer, content)


# ── Dataview replacement ──────────────────────────────────────────────────────

def parse_dataview_query(query: str) -> dict:
    """Extract TABLE columns, FROM path, WHERE conditions from a Dataview query."""
    result: dict = {}

    for line in query.strip().splitlines():
        line = line.strip()
        up   = line.upper()

        if up.startswith('TABLE'):
            col_str = line[5:].strip()
            cols: list = []
            for part in col_str.split(','):
                part = part.strip()
                m = re.split(r'\s+AS\s+', part, flags=re.IGNORECASE, maxsplit=1)
                if len(m) == 2:
                    cols.append({'field': m[0].strip(), 'alias': m[1].strip().strip('"\'')})
                elif part:
                    cols.append({'field': part, 'alias': part})
            result['columns'] = cols

        elif up.startswith('FROM'):
            m = re.search(r'"([^"]+)"', line)
            if m:
                result['from'] = m.group(1)

        elif up.startswith('WHERE'):
            m = re.search(r'priority\s*=\s*["\']([^"\']+)["\']', line)
            if m:
                result['where_priority'] = m.group(1)
            m = re.search(r'done\s*=\s*(true|false)', line, re.IGNORECASE)
            if m:
                result['where_done'] = m.group(1).lower() == 'true'

    return result


def fmt_field(field: str, value, source_file: Path, repo_root: Path) -> str:
    """Render a single frontmatter value as a table cell string."""
    if value is None:
        return '—'

    if field == 'tags':
        if isinstance(value, list):
            return ', '.join(str(t) for t in value)
        return str(value)

    if field == 'scheduled':
        # "[[itinerary/apr-23]]" → link
        if isinstance(value, str):
            m = WIKILINK_RE.search(value)
            if m:
                path, anchor, label = split_wikilink(m.group(1))
                if not label:
                    label = derive_label(path, anchor, {})
                rel = compute_rel_path(source_file, path, repo_root)
                href = f'{rel}#{re.sub(r"[^a-z0-9]+", "-", anchor.lower()).strip("-")}' if anchor else rel
                return f'[{label}]({href})'
        return str(value) if value else '—'

    if field == 'done':
        return '✅' if value else '☐'

    return str(value)


def render_dataview(query_str: str, source_file: Path, repo_root: Path, activity_index: dict) -> str:
    """Convert a single ```dataview block to a static markdown table."""
    q        = parse_dataview_query(query_str)
    from_dir = q.get('from', '')
    columns  = q.get('columns', [])
    wp       = q.get('where_priority')
    wd       = q.get('where_done')

    if not from_dir or not columns:
        return '*<!-- dataview: unrecognised query -->*'

    # Collect matching activities
    matched = []
    for key, meta in activity_index.items():
        if not key.startswith(from_dir):
            continue
        if wp is not None and meta.get('priority') != wp:
            continue
        if wd is not None and bool(meta.get('done', False)) != wd:
            continue
        matched.append((key, meta))

    if not matched:
        return '*None*'

    matched.sort(key=lambda x: x[0].split('/')[-1])

    # Header row
    headers = ['Activity'] + [c['alias'] for c in columns]
    sep     = ['---'] * len(headers)

    rows = []
    for key, meta in matched:
        name  = meta.get('name') or slugify_to_title(key.split('/')[-1])
        rel   = compute_rel_path(source_file, key, repo_root)
        cells = [f'[{name}]({rel})']
        for col in columns:
            cells.append(fmt_field(col['field'], meta.get(col['field']), source_file, repo_root))
        rows.append(cells)

    lines = ['| ' + ' | '.join(headers) + ' |',
             '| ' + ' | '.join(sep)     + ' |']
    for row in rows:
        lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(lines)


def replace_dataview_blocks(content: str, source_file: Path, repo_root: Path, activity_index: dict) -> str:
    def replacer(m):
        return render_dataview(m.group(1), source_file, repo_root, activity_index)
    return DATAVIEW_RE.sub(replacer, content)


# ── File processing ───────────────────────────────────────────────────────────

def process_md_file(src: Path, dst: Path, repo_root: Path, activity_index: dict):
    text = src.read_text(encoding='utf-8')
    # Dataview first (the query strings themselves contain no wikilinks)
    text = replace_dataview_blocks(text, src, repo_root, activity_index)
    # Then wikilinks
    text = convert_wikilinks(text, src, repo_root, activity_index)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding='utf-8')


def copy_file(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description='Obsidian vault → GitHub Pages build')
    ap.add_argument('--src', default='.', help='Repo root (default: current directory)')
    ap.add_argument('--out', default='_ghpages_build', help='Output directory (default: _ghpages_build)')
    args = ap.parse_args()

    repo_root = Path(args.src).resolve()
    out_dir   = Path(args.out).resolve()

    print(f'[convert_wikilinks] src  = {repo_root}')
    print(f'[convert_wikilinks] dest = {out_dir}')

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # Build lookup table of all activity frontmatter
    activity_index = build_activity_index(repo_root)
    print(f'[convert_wikilinks] indexed {len(activity_index)} activities')

    md_count   = 0
    copy_count = 0
    skip_count = 0

    for src_path in sorted(repo_root.rglob('*')):
        if not src_path.is_file():
            continue

        rel   = src_path.relative_to(repo_root)
        parts = rel.parts

        # Skip ignored directories at any depth
        if any(p in IGNORE_DIRS for p in parts[:-1]) or parts[0] in IGNORE_DIRS:
            skip_count += 1
            continue

        # Skip ignored files
        if src_path.name in IGNORE_FILES:
            skip_count += 1
            continue

        dst_path = out_dir / rel

        if src_path.suffix == '.md':
            process_md_file(src_path, dst_path, repo_root, activity_index)
            md_count += 1
        else:
            copy_file(src_path, dst_path)
            copy_count += 1

    print(f'[convert_wikilinks] converted {md_count} markdown files')
    print(f'[convert_wikilinks] copied    {copy_count} other files')
    print(f'[convert_wikilinks] skipped   {skip_count} files')
    print(f'[convert_wikilinks] done → {out_dir}')


if __name__ == '__main__':
    main()
