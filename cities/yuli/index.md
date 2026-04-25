---
city: yuli
dates: "Apr 22 (1 night) — Huadong Valley ride"
week: "Week 1"
nights: "1 night"
location: [23.3397, 121.3067]
---

# 🌾 Yuli

> **When:** Apr 22 (1 night) — Huadong Valley ride
> **Nights:** 1 night
> **Stay:** [[logistics/accommodation#yuli]]

Small town famous for beef noodles and lamb hotpot. Book accommodation ASAP — very limited options.

**Days:** [[itinerary/apr-22]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/yuli/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/yuli/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/yuli/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/yuli/activities"
WHERE done = true
SORT file.name ASC
```
