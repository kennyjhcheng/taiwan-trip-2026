---
city: alishan
dates: "Apr 29 (day trip only — no overnight)"
week: "Week 2"
nights: "0 nights"
location: [23.5136, 120.8035]
---

# 🌲 Alishan (阿里山)

> **When:** Apr 29 (day trip only — no overnight)
> **Nights:** 0
> **Stay:** [[logistics/accommodation#alishan]]

2,200m mountain. Ancient red cypress forest and a sunrise above a sea of clouds. ⚠️ Book accommodation 3+ weeks out.

**Days:** [[itinerary/apr-29]]

---

## 🔥 Must-Do

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/alishan/activities"
WHERE priority = "must"
SORT file.name ASC
```

---

## ✨ Worth It

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status", scheduled AS "Day"
FROM "cities/alishan/activities"
WHERE priority = "worth-it"
SORT file.name ASC
```

---

## 💭 If Time Allows

```dataview
TABLE cost_ntd AS "Cost (NT$)", tags AS "Type", status AS "Status"
FROM "cities/alishan/activities"
WHERE priority = "if-time"
SORT file.name ASC
```

---

## ✅ Done

```dataview
TABLE tags AS "Type", scheduled AS "Day"
FROM "cities/alishan/activities"
WHERE done = true
SORT file.name ASC
```
