---
city: tainan
dates: "May 1 (arrive evening) · May 2 (full food day) · May 3 (morning departure)"
week: "Week 2"
nights: "2 nights"
location: [22.9999, 120.2269]
---

# 🏛️ Tainan

> **When:** May 1 (arrive evening) · May 2 (full food day) · May 3 (morning departure)
> **Nights:** 2 nights
> **Stay:** [[logistics/accommodation#tainan]]

Taiwan's oldest city and culinary capital. 300+ temples, 17th-century Dutch forts, and dishes you won't find in Taipei.

**Days:** [[itinerary/may-01]] · [[itinerary/may-02]] · [[itinerary/may-03]]

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
