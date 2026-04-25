---
city: kaohsiung
dates: "Apr 19 (1 night) — bike start city"
week: "Week 1"
nights: "1 night"
location: [22.6273, 120.3014]
---

# 🏙️ Kaohsiung

> **When:** Apr 19 (1 night) — bike start city
> **Nights:** 1 night
> **Stay:** [[logistics/accommodation#kaohsiung]]

Taiwan's second city. Bike pickup at Giant Adventure. Airbnb is 5 min from Liouhe Night Market.

**Days:** [[itinerary/apr-19]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/kaohsiung/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/kaohsiung/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/kaohsiung/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/kaohsiung/activities"
WHERE done = true
SORT file.name ASC
```
