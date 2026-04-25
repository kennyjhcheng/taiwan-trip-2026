# CLAUDE.md — Trip File Map & Rules

## Folder Structure

```
cities/<city>/index.md          ← city overview + Dataview aggregate queries
cities/<city>/activities/*.md   ← ONE FILE PER ACTIVITY (the source of truth)
itinerary/apr-DD.md             ← ONE FILE PER DAY (links to activities)
logistics/flights.md            ← flights only
logistics/accommodation.md      ← all bookings + status
logistics/bike-rental.md        ← bike booking
logistics/budget.md             ← full budget tracker
logistics/transport.md          ← HSR, buses, MRT
logistics/packing.md            ← packing list
logistics/emergency-contacts.md ← contacts
scripts/generate_map_data.py    ← auto-generates locations.json
index.md                        ← home page + at-a-glance calendar
taiwan-map.html                 ← interactive map (reads locations.json)
locations.json                  ← 🤖 AUTO-GENERATED — do not edit manually
```

---

## Activity File Frontmatter Standard

Every file in `cities/*/activities/*.md` MUST have this frontmatter:

```yaml
---
name: Display Name of Activity
city: city-slug            # taipei | kaohsiung | checheng | taitung | yuli |
                           # hualien | jiufen | sun-moon-lake | alishan | tainan | other
tags: [eat, sightseeing]   # see tag vocabulary below
priority: must             # must | worth-it | if-time
cost_ntd: "200-400"        # string, e.g. "0" or "200-400"
location: [23.97, 121.60]  # [lat, lng] — used by map
status: pending            # pending | done | skip
scheduled: "[[itinerary/apr-23]]"   # Obsidian wikilink or ""
address: "Full address, District, City Postal"
done: false                # true when completed
---
```

### Tag Vocabulary

| Tag | Meaning | Map pin color |
|-----|---------|---------------|
| `eat` | Restaurant, food stall, dish | 🔴 Red |
| `nightmarket` | Night market | 🟠 Orange |
| `sightseeing` | Temple, viewpoint, landmark | 🔵 Blue |
| `activity` | Hiking, cycling, lanterns, etc. | 🟢 Green |
| `hotspring` | Hot spring / onsen | 🟣 Purple |
| `cycling` | Bike-specific route or rental | 🟡 Amber |

---

## Ownership Rules — Single Point of Concern

| Want to update… | Edit this file | Do NOT also edit |
|-----------------|---------------|-----------------|
| Flight details | `logistics/flights.md` | — |
| Booking status / confirmation # | `logistics/accommodation.md` | — |
| Activity details, cost, schedule | `cities/<city>/activities/<slug>.md` | Day files auto-link |
| Day plan | `itinerary/<day>.md` | — |
| Budget numbers | `logistics/budget.md` | — |
| Bike rental info | `logistics/bike-rental.md` | — |
| Map pins | Edit the activity file's `location:` frontmatter | `locations.json` is auto-generated |

The at-a-glance table in `index.md` is a **summary only** — it does not need updating when activity details change, only when day-level themes change.

---

## Map Pipeline

`locations.json` is generated automatically by the pre-commit hook:

```bash
# Runs automatically on every git commit via .git/hooks/pre-commit
python3 scripts/generate_map_data.py
```

To regenerate manually (e.g. after editing coordinates):
```bash
python3 scripts/generate_map_data.py
```

---

## Git — Commit & Push After Every Update

```bash
git add -A
git commit -m "<short description>"
git push
```

The pre-commit hook will auto-regenerate `locations.json` and stage it before committing.

Example commit messages:
- `"Book Checheng Apr 20 — Checheng Backpackers Hostel"`
- `"Mark Dongdamen Night Market done"`
- `"Add coordinates to Alishan activities"`

---

## Cities Reference

| City slug | When | Key files |
|-----------|------|-----------|
| `taipei` | Apr 18–19, 25–27, May 3 | [[cities/taipei/index]] |
| `kaohsiung` | Apr 19 | [[cities/kaohsiung/index]] |
| `checheng` | Apr 20 | [[cities/checheng/index]] |
| `taitung` | Apr 21 | [[cities/taitung/index]] |
| `yuli` | Apr 22 | [[cities/yuli/index]] |
| `hualien` | Apr 23–24 | [[cities/hualien/index]] |
| `jiufen` | Apr 27 (day trip) | [[cities/jiufen/index]] |
| `sun-moon-lake` | Apr 28–29 | [[cities/sun-moon-lake/index]] |
| `alishan` | Apr 30 – May 1 | [[cities/alishan/index]] |
| `tainan` | May 1–3 | [[cities/tainan/index]] |
| `other` | Transit stops | [[cities/other/index]] |
