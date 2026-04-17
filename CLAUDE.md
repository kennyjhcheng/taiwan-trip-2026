# CLAUDE.md — Trip File Map & Propagation Rules

## File Overview

| File | Role | Covers |
|------|------|--------|
| `index.md` | **Hub / home page** | Intro, links to all docs, "At a Glance" calendar (Apr 17–May 4) |
| `1-trip-plan.md` | **Week 1 master doc** | Apr 17–25: flights, daily bike route, bike rental, accommodation, budget, packing, to-do |
| `2-trip-plan.md` | **Week 2 master doc** | Apr 26–May 4: destinations, route options, food guide, daily itinerary, accommodation, budget, return flight |
| `taiwan-bucketlist.md` | **Master activity list** | All ~70 places/foods organized by city, each with an `Itinerary` column pointing to the relevant trip doc + date |
| `taiwan-map.html` | **Interactive map** | Leaflet map pinning all bucket list locations, color-coded by activity type |
| `_config.yml` | Jekyll site metadata | Title and theme only — no trip content |
| `Taiwan Bike Trip 2026.pdf` | Source PDF | Original reference doc; treat as read-only |

---

## File Dependency Map

```
index.md
├── links to → 1-trip-plan.md
├── links to → 2-trip-plan.md
├── links to → taiwan-bucketlist.md
└── links to → taiwan-map.html

taiwan-bucketlist.md
├── cross-references → 1-trip-plan.md  (Itinerary column: "Trip 1, Apr XX")
└── cross-references → 2-trip-plan.md  (Itinerary column: "Trip 2, Apr/May XX")

taiwan-map.html
└── pins sourced from → taiwan-bucketlist.md

2-trip-plan.md
└── explicitly defers to → 1-trip-plan.md  (Taroko Gorge covered Apr 24 in Week 1)

1-trip-plan.md
└── cross-references → 2-trip-plan.md  (notes about Week 2 extension, Apr 25 handoff)
```

---

## Propagation Rules — What to Update When Things Change

### ✈️ Flight changes (dates, times, confirmation numbers)
| Changed in | Also update |
|---|---|
| `1-trip-plan.md` §2 Flights + §10B Appendix | `index.md` At a Glance table |
| `2-trip-plan.md` §8 Return Flight | `index.md` At a Glance table (May 4 row) |

### 🗓️ Date or itinerary changes (any day shifts)
| Changed in | Also update |
|---|---|
| `1-trip-plan.md` §3 Daily Itinerary | `index.md` At a Glance table · `taiwan-bucketlist.md` Itinerary column for affected cities |
| `2-trip-plan.md` §5 Daily Itinerary | `index.md` At a Glance table · `taiwan-bucketlist.md` Itinerary column for affected cities |

### 🏨 Accommodation updates (booking confirmed, hotel changed)
| Changed in | Also update |
|---|---|
| `1-trip-plan.md` §5 Accommodation table + detailed cards | `1-trip-plan.md` §9 Pre-Trip To-Do (check off or update status) |
| `2-trip-plan.md` §6 Accommodation | `2-trip-plan.md` §9 Pre-Travel To-Do |

### 💰 Budget changes (new confirmed expense, estimate revised)
| Changed in | Also update |
|---|---|
| `1-trip-plan.md` §6 Budget Tracker | `2-trip-plan.md` §7 Full Trip Summary table (confirmed subtotal row) |
| `2-trip-plan.md` §7 Budget Tracker | `2-trip-plan.md` §7 Grand Total Estimate |

### ✅ Bucket list item scheduled or completed
| Changed in | Also update |
|---|---|
| `taiwan-bucketlist.md` Itinerary column or Done checkbox | `1-trip-plan.md` or `2-trip-plan.md` daily itinerary entry for that date |

### 🗺️ New location added to bucket list
| Changed in | Also update |
|---|---|
| `taiwan-bucketlist.md` (add row) | `taiwan-map.html` (add pin with matching color/category) |

---

## Key Cross-References to Keep in Sync

**Taroko Gorge** is the most explicitly shared item:
- `1-trip-plan.md` Apr 24 entry covers the day trip
- `2-trip-plan.md` §1 Anchors table and §2 Taroko section both note "covered Apr 24 during Week 1"
- `taiwan-bucketlist.md` Hualien section, Itinerary column: "Trip 1, Apr 24"
- If Taroko day moves, update all three.

**Return flight (Delta DL 68, May 4)**:
- `1-trip-plan.md` §2 + §10B + §9 To-Do note about Week 2 extension
- `2-trip-plan.md` §8 Return Flight + §5 May 4 daily itinerary
- `index.md` At a Glance table (May 4 row)

**Apr 25 Taipei farewell / Week 1→2 handoff**:
- `1-trip-plan.md` Apr 25 entry: "Kenny continues solo from here → see 2-trip-plan.md"
- `2-trip-plan.md` document header: "Starting point: Taipei (group farewell night April 25)"

**Week 1 dates header**:
- `1-trip-plan.md` top: "April 17–25, 2026"
- `index.md` intro: "Apr 17 – May 4, 2026"

---

## Current Booking Status (as of Apr 2026)

| Item | Status | Notes |
|------|--------|-------|
| ✅ Outbound flight SEA→TPE | Booked | Asiana OZ271/OZ711, conf. CRT3ZP |
| ✅ Return flight TPE→SEA | Booked | Delta DL68, May 4, conf. GPDGHD |
| ✅ Bike rental (Kenny) | Booked | Giant Adventure, NT$7,200, order TW_R1_269080542 |
| ✅ Taipei Apr 18 | Booked | MU House, $255.30 USD |
| ✅ Kaohsiung Apr 19 | Booked | Airbnb w/ 小玉, conf. HMX9EKYYMQ |
| ⚠️ Checheng Apr 20 | **BOOK ASAP** | Small town, limited options |
| ⚠️ Yuli Apr 22 | **BOOK ASAP** | Small town, limited options |
| ⚠️ Alishan Apr 30 | **BOOK ASAP** | Fills 3+ weeks out |
| ☐ Taitung Apr 21 | TBD | |
| ☐ Hualien Apr 23–24 | TBD | |
| ☐ Taipei Apr 25 | TBD | |
| ☐ Taipei Apr 26, 27, May 3 | TBD | Week 2 base |
| ☐ Sun Moon Lake Apr 28–29 | TBD | |
| ☐ Tainan May 1–2 | TBD | |

---

## Git — Commit & Push After Every Update

After making any change to any file in this project, always run:

```bash
git add -A
git commit -m "<short description of what changed>"
git push
```

Use a descriptive commit message, e.g.:
- `"Book Checheng Apr 20 — Qingquan Hot Spring Hotel"`
- `"Update budget: add Taitung accommodation confirmed"`
- `"Reschedule Taroko from Apr 24 to Apr 23"`

Never leave changes uncommitted. Every update — even a single checkbox — should be committed and pushed so the trip plan stays in sync on GitHub.

---

## Notes for Future Edits

- The `taiwan-bucketlist.md` footer says "Last updated: April 2026 · Cross-referenced with 1-trip-plan.md and 2-trip-plan.md" — update this date whenever the file changes.
- `_config.yml` only contains Jekyll metadata and does not need to be updated when itinerary changes.
- `Taiwan Bike Trip 2026.pdf` is a source/reference document — do not edit it; update the `.md` files instead.
- All budget figures use the exchange rate ~32 NTD = $1 USD. If this changes significantly, update the rate note in both `1-trip-plan.md` §6 and `2-trip-plan.md` §7.
