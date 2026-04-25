#!/usr/bin/env python3
"""
generate_map_data.py
Walks all cities/*/activities/*.md, parses YAML frontmatter,
and outputs locations.json for taiwan-map.html.

Run manually:  python3 scripts/generate_map_data.py
Auto-runs:     on every git commit via .git/hooks/pre-commit
"""

import os
import json
import re
import sys

def parse_frontmatter(content):
    """Extract YAML frontmatter from a markdown file."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    fm = {}
    for line in match.group(1).split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, _, val = line.partition(':')
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        
        # Parse lists like [eat, sightseeing] or [23.97, 121.60]
        if val.startswith('[') and val.endswith(']'):
            inner = val[1:-1]
            items = [x.strip().strip('"').strip("'") for x in inner.split(',')]
            # Try to parse as numbers (location coordinates)
            try:
                val = [float(x) for x in items]
            except ValueError:
                val = items
        elif val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        
        fm[key] = val
    
    return fm

def get_priority_weight(priority):
    return {'must': 3, 'worth-it': 2, 'if-time': 1}.get(priority, 1)

def get_tag_color(tags):
    """Map first tag to a map pin color."""
    color_map = {
        'eat':         '#ef4444',   # red
        'nightmarket': '#f97316',   # orange
        'sightseeing': '#3b82f6',   # blue
        'activity':    '#10b981',   # green
        'hotspring':   '#8b5cf6',   # purple
        'cycling':     '#f59e0b',   # amber
    }
    if isinstance(tags, list) and tags:
        return color_map.get(tags[0], '#6b7280')
    return '#6b7280'

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(script_dir)
    cities_dir = os.path.join(root, 'cities')
    
    if not os.path.isdir(cities_dir):
        print(f"ERROR: cities/ directory not found at {cities_dir}", file=sys.stderr)
        sys.exit(1)
    
    locations = []
    count = 0
    skipped = 0
    
    for city in sorted(os.listdir(cities_dir)):
        acts_dir = os.path.join(cities_dir, city, 'activities')
        if not os.path.isdir(acts_dir):
            continue
        
        for fname in sorted(os.listdir(acts_dir)):
            if not fname.endswith('.md'):
                continue
            
            fpath = os.path.join(acts_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            fm = parse_frontmatter(content)
            
            # Skip if no location
            loc = fm.get('location')
            if not loc or not isinstance(loc, list) or len(loc) < 2:
                skipped += 1
                continue
            
            # Build obsidian:// deep link
            rel_path = os.path.relpath(fpath, root)
            slug = fname.replace('.md', '')
            
            entry = {
                'name':      fm.get('name', slug),
                'city':      fm.get('city', city),
                'tags':      fm.get('tags', []),
                'priority':  fm.get('priority', 'if-time'),
                'weight':    get_priority_weight(fm.get('priority', 'if-time')),
                'color':     get_tag_color(fm.get('tags', [])),
                'cost_ntd':  fm.get('cost_ntd', ''),
                'lat':       loc[0],
                'lng':       loc[1],
                'status':    fm.get('status', 'pending'),
                'done':      fm.get('done', False),
                'scheduled': fm.get('scheduled', ''),
                'address':   fm.get('address', ''),
                'file':      rel_path.replace('\\', '/'),
            }
            locations.append(entry)
            count += 1
    
    out_path = os.path.join(root, 'locations.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(locations, f, indent=2, ensure_ascii=False)
    
    print(f"✅ locations.json generated — {count} locations ({skipped} skipped, no coords)")
    return out_path

if __name__ == '__main__':
    main()
