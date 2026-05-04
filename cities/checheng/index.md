---
city: checheng
dates: "Apr 20 (1 night) — after 55mi ride"
week: "Week 1"
nights: "1 night"
location: [22.0055, 120.7101]
---

# 🏘️ Checheng & Southern Taiwan

> **When:** Apr 20 (1 night) — after 55mi ride
> **Nights:** 1 night
> **Stay:** [[logistics/accommodation#checheng]]

Small fishing town at Taiwan's southern tip. Stayed at 林會館 Lin House. Met fellow cyclists and backpackers here. Most Kenting/Hengchun sights were skipped in favor of resting and pushing south fast — with 74mi the next day, early sleep was the priority.

**Days:** [[itinerary/apr-20]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/checheng/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/checheng/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/checheng/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/checheng/activities"
WHERE done = true
SORT file.name ASC
```
