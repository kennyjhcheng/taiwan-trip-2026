---
city: jiufen
dates: "Apr 27 (day trip from Taipei)"
week: "Week 2"
nights: "Day trip only"
location: [25.1072, 121.8435]
---

# ⛩️ Jiufen + Shifen

> **When:** Apr 27 (day trip from Taipei)
> **Nights:** Day trip only
> **Stay:** N/A (day trip)

Northeast Taiwan day trip. Shifen in the morning (sky lanterns), Jiufen in the afternoon (tea houses). Monday = least crowded.

**Days:** [[itinerary/apr-27]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/jiufen/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/jiufen/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/jiufen/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/jiufen/activities"
WHERE done = true
SORT file.name ASC
```
