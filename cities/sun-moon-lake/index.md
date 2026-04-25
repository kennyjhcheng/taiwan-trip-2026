---
city: sun-moon-lake
dates: "Apr 28 (arrive) · Apr 29 (full day)"
week: "Week 2"
nights: "2 nights"
location: [23.8625, 120.9170]
---

# 🌊 Sun Moon Lake (日月潭)

> **When:** Apr 28 (arrive) · Apr 29 (full day)
> **Nights:** 2 nights
> **Stay:** [[logistics/accommodation#sun-moon-lake]]

Taiwan's most beautiful alpine lake. 33km cycling loop, Thao indigenous culture, sunrise over the mist.

**Days:** [[itinerary/apr-28]] · [[itinerary/apr-29]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/sun-moon-lake/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/sun-moon-lake/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/sun-moon-lake/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/sun-moon-lake/activities"
WHERE done = true
SORT file.name ASC
```
