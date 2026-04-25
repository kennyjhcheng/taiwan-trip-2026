---
city: taipei
dates: "Apr 18 (arrival) · Apr 19 (HSR south) · Apr 25 (farewell) · Apr 26–27 (Week 2) · May 3 (final night)"
week: "Week 1 + Week 2"
nights: "6 nights total (scattered)"
location: [25.0330, 121.5654]
---

# 🏙️ Taipei

> **When:** Apr 18 (arrival) · Apr 19 (HSR south) · Apr 25 (farewell) · Apr 26–27 (Week 2) · May 3 (final night)
> **Nights:** 6 nights total (scattered)
> **Stay:** [[logistics/accommodation#taipei]]

Taiwan's capital. Ultra-modern, safe, walkable, world-class food. Your home base for the trip.

**Days:** [[itinerary/apr-18]] · [[itinerary/apr-19]] · [[itinerary/apr-25]] · [[itinerary/apr-26]] · [[itinerary/apr-27]] · [[itinerary/may-03]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/taipei/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/taipei/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/taipei/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/taipei/activities"
WHERE done = true
SORT file.name ASC
```
