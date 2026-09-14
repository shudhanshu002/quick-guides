# 📘 MongoDB Students Practice – Complete Query Guide

This repository contains structured MongoDB practice queries using a `students` collection.

It covers:
- ✅ Basic Queries
- 🟡 Intermediate Queries
- 🔴 Advanced Logical Queries
- 🔥 Aggregation Framework
- 🚀 Real-World Scenarios (Pagination, Sorting, Counting)

---

# 📂 Collection Structure (Assumed)

```js
{
  name: String,
  age: Number,
  gender: String,
  city: String,
  course: String,
  marks: Number,
  isActive: Boolean
}
```

---

# 🟢 LEVEL 1 – BASIC QUERIES

### 1️⃣ Students with marks > 85
```js
db.students.find({ marks: { $gt: 85 } })
```

### 2️⃣ Age ≤ 20
```js
db.students.find({ age: { $lte: 20 } })
```

### 3️⃣ Students from Delhi or Mumbai
```js
db.students.find({ city: { $in: ["Delhi", "Mumbai"] } })
```

### 4️⃣ Students not enrolled in BCA
```js
db.students.find({ course: { $ne: "BCA" } })
```

---

# 🟡 LEVEL 2 – INTERMEDIATE QUERIES

### 5️⃣ Marks between 70 and 90
```js
db.students.find({ marks: { $gte: 70, $lte: 90 } })
```

### 6️⃣ Female students with marks > 80
```js
db.students.find({
  gender: "Female",
  marks: { $gt: 80 }
})
```

### 7️⃣ Top 3 highest marks
```js
db.students.find().sort({ marks: -1 }).limit(3)
```

### 8️⃣ Name starts with "A"
```js
db.students.find({ name: { $regex: "^A" } })
```

### 9️⃣ Distinct courses
```js
db.students.distinct("course")
```

---

# 🔴 LEVEL 3 – ADVANCED QUERIES

### 🔟 Active students with marks > 80
```js
db.students.find({
  isActive: true,
  marks: { $gt: 80 }
})
```

### 1️⃣1️⃣ City not Delhi AND marks < 75
```js
db.students.find({
  city: { $ne: "Delhi" },
  marks: { $lt: 75 }
})
```

### 1️⃣2️⃣ Sort by age ↑ and marks ↓
```js
db.students.find().sort({ age: 1, marks: -1 })
```

### 1️⃣3️⃣ Skip 5, show next 5
```js
db.students.find().skip(5).limit(5)
```

### 1️⃣4️⃣ Count students with marks > 90
```js
db.students.countDocuments({ marks: { $gt: 90 } })
```

---

# 🧠 COMPLEX LOGICAL QUERIES

### 1️⃣ AND + OR Combination
```js
db.students.find({
  course: "BCA",
  isActive: true,
  $or: [
    { marks: { $gt: 80 } },
    { city: "Delhi" }
  ]
})
```

### 2️⃣ NOT + Range + Multiple Conditions
```js
db.students.find({
  marks: { $not: { $gte: 60, $lte: 80 } },
  age: { $gte: 21 },
  city: { $ne: "Mumbai" }
})
```

### 3️⃣ Filter + Projection + Sort + Limit
```js
db.students.find(
  {
    gender: "Female",
    marks: { $gt: 75 }
  },
  { name: 1, marks: 1, city: 1, _id: 0 }
)
.sort({ marks: -1 })
.limit(5)
```

### 4️⃣ Regex + Condition (Case Insensitive)
```js
db.students.find({
  name: { $regex: "^(A|S)", $options: "i" },
  marks: { $gte: 70 }
})
```

### 5️⃣ Logical NOR
```js
db.students.find({
  $nor: [
    { course: "BCA" },
    { city: "Delhi" }
  ]
})
```

### 6️⃣ Multi-Level Sorting
```js
db.students.find({
  age: { $gte: 20 }
})
.sort({ age: 1, marks: -1 })
```

### 7️⃣ Real Pagination Example
(Page size = 4, Page = 3 → Skip = 8)
```js
db.students.find()
.sort({ marks: -1 })
.skip(8)
.limit(4)
```

### 8️⃣ IN + NOT EQUAL + Range
```js
db.students.find({
  course: { $in: ["BCA", "BSc"] },
  city: { $ne: "Delhi" },
  marks: { $gte: 75 }
})
```

### 9️⃣ Count with Multiple Conditions
```js
db.students.countDocuments({
  marks: { $gt: 80 },
  isActive: true,
  gender: "Female"
})
```

### 🔟 Nested Condition Simulation
```js
db.students.find({
  city: "Delhi",
  marks: { $gt: 80 },
  age: { $lt: 23 },
  name: { $not: { $regex: "^R" } }
})
```

---

# 🔥 AGGREGATION FRAMEWORK

---

## 🟡 Aggregation Level 1

### 1️⃣ Average marks
```js
db.students.aggregate([
  {
    $group: {
      _id: null,
      avgMarks: { $avg: "$marks" }
    }
  }
])
```

### 2️⃣ Total students per city
```js
db.students.aggregate([
  {
    $group: {
      _id: "$city",
      totalStudents: { $sum: 1 }
    }
  }
])
```

### 3️⃣ Highest marks per course
```js
db.students.aggregate([
  {
    $group: {
      _id: "$course",
      highestMarks: { $max: "$marks" }
    }
  }
])
```

---

## 🔴 Aggregation Level 2

### 4️⃣ Average marks of active students
```js
db.students.aggregate([
  { $match: { isActive: true } },
  {
    $group: {
      _id: null,
      avgMarks: { $avg: "$marks" }
    }
  }
])
```

### 5️⃣ Top 2 cities by student count
```js
db.students.aggregate([
  {
    $group: {
      _id: "$city",
      totalStudents: { $sum: 1 }
    }
  },
  { $sort: { totalStudents: -1 } },
  { $limit: 2 }
])
```

### 6️⃣ Total students & avg marks per gender
```js
db.students.aggregate([
  {
    $group: {
      _id: "$gender",
      totalStudents: { $sum: 1 },
      avgMarks: { $avg: "$marks" }
    }
  }
])
```

---

## 🚀 Aggregation Level 3

### 7️⃣ Course-wise analytics
```js
db.students.aggregate([
  {
    $group: {
      _id: "$course",
      totalStudents: { $sum: 1 },
      avgMarks: { $avg: "$marks" },
      highestMarks: { $max: "$marks" }
    }
  }
])
```

### 8️⃣ Cities with avg marks > 75
```js
db.students.aggregate([
  {
    $group: {
      _id: "$city",
      avgMarks: { $avg: "$marks" }
    }
  },
  {
    $match: { avgMarks: { $gt: 75 } }
  }
])
```

### 9️⃣ Count students scoring > 80 per course
```js
db.students.aggregate([
  {
    $group: {
      _id: "$course",
      highScorers: {
        $sum: {
          $cond: [{ $gt: ["$marks", 80] }, 1, 0]
        }
      }
    }
  }
])
```


# 📘 MongoDB Aggregation Practice – Students, Courses & Enrollments

This project demonstrates advanced MongoDB aggregation using relational-style collections:

- 👨‍🎓 `students`
- 📚 `courses`
- 📝 `enrollments`

It covers:
- $lookup (Joins)
- $group
- $unwind
- $match
- $project
- $addFields
- Complex filtering
- Real-world aggregation scenarios

---

# 📂 Database Setup

## 🔹 Insert Students

```js
db.students.insertMany([
  { _id: 1, name: "Ram", age: 20, city: "Delhi" },
  { _id: 2, name: "Shyam", age: 22, city: "Mumbai" }
])
```

## 🔹 Insert Courses

```js
db.courses.insertMany([
  { _id: 101, courseName: "BCA", fees: 50000 },
  { _id: 102, courseName: "MCA", fees: 80000 }
])
```

## 🔹 Insert Enrollments

```js
db.enrollments.insertMany([
  { studentId: 1, courseId: 101, semester: 1 },
  { studentId: 1, courseId: 102, semester: 2 }
])
```

---

# 🎯 Base Aggregation Example

### Show each student with:
- Total number of courses
- Average course fees

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $lookup: {
      from: "courses",
      localField: "enrollments.courseId",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  {
    $group: {
      _id: "$_id",
      name: { $first: "$name" },
      totalCourses: { $sum: 1 },
      averageFees: { $avg: "$course.fees" }
    }
  }
])
```

---

# 🟢 LEVEL 1

## Q1 – Students enrolled in more than 1 course

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $group: {
      _id: "$_id",
      name: { $first: "$name" },
      totalCourses: { $sum: 1 }
    }
  },
  { $match: { totalCourses: { $gt: 1 } } },
  { $project: { _id: 0, name: 1, totalCourses: 1 } }
])
```

---

## Q2 – Students enrolled in course "BCA"

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $lookup: {
      from: "courses",
      localField: "enrollments.courseId",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  { $match: { "course.courseName": "BCA" } },
  { $project: { _id: 0, name: 1, city: 1 } }
])
```

---

## Q3 – Courses with number of students

```js
db.courses.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "courseId",
      as: "enrollments"
    }
  },
  {
    $project: {
      _id: 0,
      courseName: 1,
      totalStudents: { $size: "$enrollments" }
    }
  }
])
```

---

# 🔥 LEVEL 2

## Q4 – Average course fee per city

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $lookup: {
      from: "courses",
      localField: "enrollments.courseId",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  {
    $group: {
      _id: "$city",
      avgFee: { $avg: "$course.fees" }
    }
  },
  { $project: { _id: 0, city: "$_id", avgFee: 1 } }
])
```

---

## Q5 – Student who paid highest total fees

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $lookup: {
      from: "courses",
      localField: "enrollments.courseId",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  {
    $group: {
      _id: "$_id",
      name: { $first: "$name" },
      totalFees: { $sum: "$course.fees" }
    }
  },
  { $sort: { totalFees: -1 } },
  { $limit: 1 },
  { $project: { _id: 0, name: 1, totalFees: 1 } }
])
```

---

## Q6 – Courses where >1 student enrolled AND fees > 60000

```js
db.courses.aggregate([
  { $match: { fees: { $gt: 60000 } } },
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "courseId",
      as: "enrollments"
    }
  },
  {
    $project: {
      _id: 0,
      courseName: 1,
      fees: 1,
      totalStudents: { $size: "$enrollments" }
    }
  },
  { $match: { totalStudents: { $gt: 1 } } }
])
```

---

# 🔥 LEVEL 3

## Q7 – One document per student with courses array + totalFees

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  { $unwind: "$enrollments" },
  {
    $lookup: {
      from: "courses",
      localField: "enrollments.courseId",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  {
    $group: {
      _id: "$_id",
      name: { $first: "$name" },
      courses: { $push: "$course.courseName" },
      totalFees: { $sum: "$course.fees" }
    }
  },
  { $project: { _id: 0, name: 1, courses: 1, totalFees: 1 } }
])
```

---

## Q8 – Cities where avg age > 21 AND total enrolled courses > 2

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  {
    $group: {
      _id: "$city",
      avgAge: { $avg: "$age" },
      totalCourses: { $sum: { $size: "$enrollments" } }
    }
  },
  {
    $match: {
      avgAge: { $gt: 21 },
      totalCourses: { $gt: 2 }
    }
  }
])
```

---

# 🔥 LEVEL 4

## Q9 – Top 2 most popular courses

```js
db.enrollments.aggregate([
  {
    $group: {
      _id: "$courseId",
      totalStudents: { $sum: 1 }
    }
  },
  { $sort: { totalStudents: -1 } },
  { $limit: 2 },
  {
    $lookup: {
      from: "courses",
      localField: "_id",
      foreignField: "_id",
      as: "course"
    }
  },
  { $unwind: "$course" },
  {
    $project: {
      _id: 0,
      courseName: "$course.courseName",
      totalStudents: 1
    }
  }
])
```

---

## Q10 – Students enrolled in ALL courses Ram is enrolled in

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  {
    $addFields: {
      courseIds: "$enrollments.courseId"
    }
  },
  {
    $match: {
      courseIds: {
        $all: db.enrollments.find({ studentId: 1 }).map(e => e.courseId)
      }
    }
  },
  { $project: { _id: 0, name: 1 } }
])
```

---

# 🎁 BONUS

## Q11 – City-wise student list with totalCourses

```js
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "studentId",
      as: "enrollments"
    }
  },
  {
    $project: {
      city: 1,
      name: 1,
      totalCourses: { $size: "$enrollments" }
    }
  },
  {
    $group: {
      _id: "$city",
      students: {
        $push: {
          name: "$name",
          totalCourses: "$totalCourses"
        }
      }
    }
  },
  {
    $project: {
      _id: 0,
      city: "$_id",
      students: 1
    }
  }
])
```
