# 🚀 MongoDB Complete Master Guide
### From Basic CRUD to Sharding Architecture

This document covers:

- CRUD Operations
- Query Operators
- Aggregation Framework
- Indexing & Optimization
- Explain Plan Analysis
- Transactions (ACID)
- Embedding vs Referencing
- Write Concern
- Sharding Architecture

This is a complete backend + production-level MongoDB reference.

---

# 📌 TABLE OF CONTENTS

1. Database Setup
2. CRUD Operations
3. Query Operators
4. Aggregation Framework
5. Indexing Deep Dive
6. Explain Plan (Performance Analysis)
7. Embedding vs Referencing
8. Write Concern
9. Transactions
10. Sharding Architecture
11. Important Limits

---

# 🗄 1️⃣ DATABASE SETUP

```js
use practiceDB
```

## Students Collection

```js
db.students.insertMany([
  { _id: 1, name: "Ram", age: 20, city: "Delhi", marks: 85, course: "BCA", isActive: true },
  { _id: 2, name: "Shyam", age: 22, city: "Mumbai", marks: 75, course: "BSc", isActive: true },
  { _id: 3, name: "Amit", age: 21, city: "Delhi", marks: 60, course: "BCom", isActive: false }
])
```

---

# ✏️ 2️⃣ CRUD OPERATIONS

---

## 🟢 INSERT

### insertOne
```js
db.students.insertOne({
  name: "Kunal",
  age: 21,
  city: "Delhi",
  marks: 82,
  course: "BCA",
  isActive: true
})
```

### insertMany
```js
db.students.insertMany([
  { name: "Riya", age: 20, city: "Pune", marks: 77, course: "BSc", isActive: true },
  { name: "Manoj", age: 23, city: "Delhi", marks: 69, course: "BCom", isActive: false }
])
```

---

## 🟡 UPDATE

### updateOne
```js
db.students.updateOne(
  { name: "Ram" },
  { $set: { marks: 90 } }
)
```

### updateMany
```js
db.students.updateMany(
  { city: "Delhi" },
  { $inc: { marks: 5 } }
)
```

### Upsert
```js
db.students.updateOne(
  { name: "Unknown" },
  { $set: { age: 19 } },
  { upsert: true }
)
```

---

## 🔴 DELETE

```js
db.students.deleteOne({ name: "Ram" })
db.students.deleteMany({ isActive: false })
db.students.drop()
db.dropDatabase()
```

---

# 🔎 3️⃣ QUERY OPERATORS

---

## 🟢 Basic Find

```js
db.students.find()
db.students.find({ city: "Delhi" })
```

---

## 🟢 Comparison Operators

| Operator | Meaning |
|-----------|----------|
| $eq | Equal |
| $ne | Not Equal |
| $gt | Greater Than |
| $gte | Greater Than Equal |
| $lt | Less Than |
| $lte | Less Than Equal |
| $in | Match From List |
| $nin | Not In List |

Example:

```js
db.students.find({ marks: { $gt: 80 } })
db.students.find({ age: { $gte: 21 } })
db.students.find({ city: { $ne: "Delhi" } })
```

---

## 🟢 Logical Operators

```js
db.students.find({
  $and: [
    { city: "Delhi" },
    { marks: { $gt: 70 } }
  ]
})

db.students.find({
  $or: [
    { city: "Mumbai" },
    { marks: { $gt: 90 } }
  ]
})
```

---

## 🟢 Element Operators

```js
db.students.find({ age: { $exists: true } })
db.students.find({ marks: { $type: "int" } })
```

---

## 🟢 Array Queries

```js
db.students.find({ hobbies: "cricket" })
db.students.find({ hobbies: { $size: 2 } })
db.students.find({ hobbies: { $all: ["cricket", "music"] } })
```

---

## 🟢 Projection

```js
db.students.find(
  { city: "Delhi" },
  { name: 1, marks: 1, _id: 0 }
)
```

---

## 🟢 Sorting & Pagination

```js
db.students.find().sort({ marks: -1 })
db.students.find().skip(5).limit(5)
```

---

# ⚡ 4️⃣ AGGREGATION FRAMEWORK

---

## $match

```js
db.students.aggregate([
  { $match: { marks: { $gt: 80 } } }
])
```

---

## $group

```js
db.students.aggregate([
  {
    $group: {
      _id: "$course",
      avgMarks: { $avg: "$marks" },
      totalStudents: { $sum: 1 }
    }
  }
])
```

---

## $project with $cond

```js
db.students.aggregate([
  {
    $project: {
      name: 1,
      marks: 1,
      result: {
        $cond: {
          if: { $gte: ["$marks", 40] },
          then: "Pass",
          else: "Fail"
        }
      }
    }
  }
])
```

---

## $lookup (Join Example)

```js
db.students.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "course",
      foreignField: "courseName",
      as: "courseDetails"
    }
  }
])
```

---

# 📊 5️⃣ INDEXING (Deep Optimization)

---

## Create Index

```js
db.students.createIndex({ marks: 1 })
```

Check usage:

```js
db.students.find({ marks: 85 }).explain("executionStats")
```

---

## Compound Index

```js
db.students.createIndex({ city: 1, marks: -1 })
```

Golden Rule:
Equality → Range → Sort

---

## Partial Index

```js
db.students.createIndex(
  { marks: 1 },
  { partialFilterExpression: { marks: { $gt: 50 } } }
)
```

---

## TTL Index

```js
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }
)
```

---

## Text Index

```js
db.posts.createIndex({ content: "text" })
```

---

# 🔬 6️⃣ EXPLAIN PLAN

```js
db.students.find({ marks: 85 }).explain("executionStats")
```

Important fields:

- stage → COLLSCAN / IXSCAN
- nReturned
- totalDocsExamined
- totalKeysExamined
- executionTimeMillis

Golden Rule:

If  
`totalDocsExamined >> nReturned`  
👉 Query is inefficient.

---

# 🧱 7️⃣ EMBEDDING VS REFERENCING

---

## Embedding

```js
{
  name: "Aman",
  address: {
    city: "Delhi",
    pincode: 110001
  }
}
```

✔ Faster reads  
✔ No joins  
❌ 16MB document limit  

---

## Referencing

```js
{
  name: "Aman",
  courseId: ObjectId("abc123")
}
```

✔ No duplication  
✔ Scalable  
❌ Requires $lookup  

---

# 🛡 8️⃣ WRITE CONCERN

```js
db.students.insertOne(
  { name: "Ram" },
  { writeConcern: { w: "majority", j: true } }
)
```

Options:

- w: 0
- w: 1
- w: "majority"
- j: true
- wtimeout

---

# 🔐 9️⃣ TRANSACTIONS (ACID)

Only supported in:

- Replica Sets
- Sharded Clusters

---

### Transaction Example

```js
const session = db.getMongo().startSession()
session.startTransaction()

const accounts = session.getDatabase("practiceDB").accounts

try {

  accounts.updateOne({ _id: 1 }, { $inc: { balance: -200 } })
  accounts.updateOne({ _id: 2 }, { $inc: { balance: 200 } })

  session.commitTransaction()

} catch (error) {

  session.abortTransaction()

}

session.endSession()
```

---

# 🌍 🔥 1️⃣0️⃣ SHARDING ARCHITECTURE

---

## Components

1. Shards (Replica Sets)
2. Config Servers
3. Mongos (Query Router)

---

## Enable Sharding

```js
sh.enableSharding("practiceDB")
sh.shardCollection("practiceDB.students", { userId: "hashed" })
```

---

## Types of Sharding

### Range-Based
Splits by value ranges.

### Hashed
Even distribution (recommended for userId).

---

## Good Shard Key Rules

✔ High cardinality  
✔ Even distribution  
✔ Frequently used in queries  
❌ Not monotonically increasing  

---

# 📏 1️⃣1️⃣ IMPORTANT LIMITS

| Limit | Value |
|--------|--------|
| Max Document Size | 16 MB |
| Max BSON Size | 16 MB |
| Max Nesting Depth | 100 Levels |

MongoDB stores data in BSON format.
