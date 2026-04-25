---
city: hualien
dates: "Apr 23 (bike route ends 🎉) · Apr 24 (Taroko Gorge free day)"
week: "Week 1"
nights: "2 nights"
location: [23.9764, 121.6040]
---

# 🏔️ Hualien

> **When:** Apr 23 (bike route ends 🎉) · Apr 24 (Taroko Gorge free day)
> **Nights:** 2 nights
> **Stay:** [[logistics/accommodation#hualien]]

Bike route ends here. Apr 24 is the Taroko Gorge day trip. Known for mochi and milk popsicles.

**Days:** [[itinerary/apr-23]] · [[itinerary/apr-24]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/hualien/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/hualien/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/hualien/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/hualien/activities"
WHERE done = true
SORT file.name ASC
```
