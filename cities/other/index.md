---
city: other
dates: "Various (transit stops or optional add-ons)"
week: "Both"
nights: "No overnight stays"
location: [23.5, 121.0]
---

# 🗺️ Other Destinations

> **When:** Various (transit stops or optional add-ons)
> **Nights:** No overnight stays
> **Stay:** N/A (day trip)

Taichung (Apr 28 transit), Chiayi (Apr 30 transit), Keelung and Wulai (optional from Taipei), Chishang (Apr 22 on-route).

**Days:** —

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/other/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/other/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/other/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/other/activities"
WHERE done = true
SORT file.name ASC
```
