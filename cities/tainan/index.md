---
city: tainan
dates: "Apr 29 (arrive evening) · Apr 30 + May 1 (full days) · May 1 (depart afternoon)"
week: "Week 2"
nights: "3 nights (LIGHT Hostel)"
location: [22.9999, 120.2269]
---

# 🏛️ Tainan

> **When:** Apr 29 (arrive evening) · Apr 30–May 1 (full days) · May 1 (depart afternoon to Kaohsiung)
> **Nights:** 3 nights — LIGHT Hostel
> **Stay:** [[logistics/accommodation#tainan]]

Taiwan's oldest city and culinary capital. 300+ temples, 17th-century Dutch forts, and dishes you won't find in Taipei. Slow down here — the point is wandering, eating, and stumbling into temples.

**Days:** [[itinerary/apr-29]] · [[itinerary/apr-30]] · [[itinerary/may-01]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/tainan/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/tainan/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/tainan/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/tainan/activities"
WHERE done = true
SORT file.name ASC
```
