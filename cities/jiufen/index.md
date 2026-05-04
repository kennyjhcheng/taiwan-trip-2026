---
city: jiufen
dates: "Apr 25 (day trip en route from Hualien to Taipei)"
week: "Week 1"
nights: "Day trip only"
location: [25.1072, 121.8435]
---

# ⛩️ Jiufen

> **When:** Apr 25 (day trip en route from Hualien to Taipei)
> **Nights:** Day trip only
> **Stay:** N/A (day trip)

Northeast Taiwan. Took the train from Hualien to Ruifang, then the bus up the winding hillside to Jiufen. Walked the old lantern-lit street, ate taro ball soup at Grandma Lai's, had beef noodles at Age Inn, then bussed back to Taipei in the afternoon.

**Days:** [[itinerary/apr-25]]

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
