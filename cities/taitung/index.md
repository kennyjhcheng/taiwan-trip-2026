---
city: taitung
dates: "Apr 21 (1 night) — after the hardest riding day"
week: "Week 1"
nights: "1 night"
location: [22.7583, 121.1444]
---

# 🌊 Taitung

> **When:** Apr 21 (1 night) — after the hardest riding day
> **Nights:** 1 night
> **Stay:** [[logistics/accommodation#taitung]]

Arrive exhausted after 74mi + 4,300ft of climbing. Eat well, soak if possible, sleep hard.

**Days:** [[itinerary/apr-21]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/taitung/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/taitung/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/taitung/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/taitung/activities"
WHERE done = true
SORT file.name ASC
```
