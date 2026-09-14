# PostgreSQL Learning Guide 🚀

A structured guide to learning PostgreSQL from basics to advanced SQL concepts.

This README documents the journey of learning relational databases, focusing on practical query writing, schema design, and data relationships.

---

# 1. What is PostgreSQL?

PostgreSQL (often called **Postgres**) is an advanced **open-source relational database management system (RDBMS)**.

### Key Features

- Open source
- Strict schema enforcement
- ACID compliant transactions
- Highly extensible
- Powerful query engine
- Used in large production systems

PostgreSQL is widely used in backend development, analytics, and enterprise applications.

---

# 2. Installing PostgreSQL

### Windows Installation

1. Download PostgreSQL from the official website.
2. Run the installer.
3. During installation:
   - Set password for `postgres` user
   - Default port: `5432`
4. Install **pgAdmin** if you want a GUI.

---

# 3. Connecting to PostgreSQL

There are multiple ways to connect.

## Method 1 — Using `psql` (Command Line)

Open terminal and run:

```bash
psql -U postgres
```

Enter password when prompted.

Successful connection shows:

```
postgres=#
```

---

## Method 2 — Connect to a Specific Database

```bash
psql -U postgres -d mydatabase
```

---

## Method 3 — Using GUI (pgAdmin)

pgAdmin allows you to:

- Create databases
- Run SQL queries
- Browse tables
- View execution plans
- Manage roles and permissions

---

# 4. Basic PostgreSQL Commands

List all databases:

```sql
\l
```

Switch database:

```sql
\c database_name
```

List tables:

```sql
\dt
```

Exit psql:

```sql
\q
```

---

# 5. Creating Your First Database

```sql
CREATE DATABASE practice_db;
```

Connect to it:

```sql
\c practice_db
```

---

# 6. Creating Your First Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);
```

### Concepts

- `SERIAL` → Auto increment integer
- `PRIMARY KEY` → Unique identifier
- PostgreSQL enforces strict data types

---

# 7. Insert Data

```sql
INSERT INTO students (name, age, city)
VALUES
('Ram', 20, 'Delhi'),
('Shyam', 22, 'Mumbai'),
('Amit', 21, 'Delhi');
```

---

# 8. Basic SELECT Queries

Get all rows:

```sql
SELECT * FROM students;
```

Filter rows:

```sql
SELECT * FROM students
WHERE city = 'Delhi';
```

---

# 9. PostgreSQL vs MongoDB Syntax

MongoDB query:

```
{ city: "Delhi" }
```

PostgreSQL query:

```sql
WHERE city = 'Delhi'
```

Different syntax but same filtering concept.

---

# 10. PostgreSQL Roles & Users

PostgreSQL manages access using **roles**.

Create a new role:

```sql
CREATE ROLE prateek WITH LOGIN PASSWORD 'yourpassword';
```

Grant database access:

```sql
GRANT ALL PRIVILEGES ON DATABASE practice_db TO prateek;
```

---

# 11. Table Design and Constraints

Proper schema design ensures **data integrity and consistency**.

## Types of Constraints

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK
- DEFAULT

---

## PRIMARY KEY

Uniquely identifies each row.

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

Characteristics:

- Unique
- Not null
- Automatically indexed

---

## UNIQUE Constraint

Ensures values are not duplicated.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE
);
```

Composite unique example:

```sql
UNIQUE (email, phone)
```

---

## NOT NULL

Prevents empty values.

```sql
name VARCHAR(100) NOT NULL
```

---

## DEFAULT

Automatically assigns a value if none provided.

```sql
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

---

## CHECK Constraint

Validates a condition.

```sql
age INT CHECK (age >= 18)
```

Example:

```sql
salary NUMERIC CHECK (salary > 0)
```

---

# 12. Foreign Keys

Foreign keys define relationships between tables.

Example:

### Courses Table

```sql
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    fees NUMERIC CHECK (fees > 0)
);
```

### Students Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

This ensures `course_id` must exist in the `courses` table.

---

# 13. Foreign Key Delete Behavior

## CASCADE

Delete related rows automatically.

```sql
ON DELETE CASCADE
```

---

## SET NULL

Sets foreign key to NULL.

```sql
ON DELETE SET NULL
```

---

## RESTRICT (Default)

Prevents deletion if related rows exist.

---

# 14. Many-to-Many Relationship

Implemented using a junction table.

Example:

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

This prevents duplicate enrollments.

---

# 15. Normalization

Normalization reduces data redundancy.

### Bad Design

```
students
id | name | course_name | fees
```

Problems:

- Data duplication
- Update anomalies

### Correct Design

```
students
courses
enrollments
```

---

# 16. Relationship Types

Relational databases have three relationship types.

## One-to-One

Example:

```
users → user_profiles
```

---

## One-to-Many

Example:

```
department → employees
```

Foreign key stored in `employees`.

---

## Many-to-Many

Example:

```
students ↔ courses
```

Implemented using a junction table:

```
enrollments
```

---

# 17. SQL SELECT Mastery

## WHERE

```sql
SELECT * FROM students
WHERE marks > 80;
```

---

## Logical Operators

```sql
AND
OR
NOT
```

Example:

```sql
SELECT * FROM students
WHERE city='Delhi' AND marks > 80;
```

---

## BETWEEN

```sql
SELECT * FROM students
WHERE marks BETWEEN 70 AND 90;
```

---

## IN

```sql
SELECT * FROM students
WHERE city IN ('Delhi','Mumbai');
```

---

## LIKE

Starts with A:

```sql
WHERE name LIKE 'A%'
```

Ends with a:

```sql
WHERE name LIKE '%a'
```

Contains "ro":

```sql
WHERE name LIKE '%ro%'
```

---

# 18. Sorting and Limiting

Sort results:

```sql
ORDER BY marks DESC
```

Limit rows:

```sql
LIMIT 3
```

---

# 19. Aggregation Functions

Common SQL aggregations:

| Function | Purpose |
|--------|--------|
| COUNT | Number of rows |
| SUM | Total value |
| AVG | Average |
| MAX | Maximum |
| MIN | Minimum |

Example:

```sql
SELECT AVG(marks) FROM students;
```

---

# 20. GROUP BY

Used with aggregation.

Example:

```sql
SELECT city, AVG(marks)
FROM students
GROUP BY city;
```

---

# 21. HAVING

Filters grouped results.

```sql
SELECT city, AVG(marks)
FROM students
GROUP BY city
HAVING AVG(marks) > 80;
```

---

# 22. SQL JOINS

Joins combine data from multiple tables.

---

## INNER JOIN

Returns matching rows.

```sql
SELECT students.name, courses.course_name
FROM enrollments
JOIN students
ON enrollments.student_id = students.id
JOIN courses
ON enrollments.course_id = courses.id;
```

---

## LEFT JOIN

Returns all rows from left table.

```sql
SELECT students.name, courses.course_name
FROM students
LEFT JOIN enrollments
ON students.id = enrollments.student_id;
```

---

## RIGHT JOIN

Returns all rows from right table.

---

## FULL JOIN

Returns all rows from both tables.

---

# 23. Subqueries

Query inside another query.

Example:

```sql
SELECT name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);
```

---

# 24. EXISTS

Checks if records exist.

```sql
SELECT name
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);
```

---

# 25. CTE (Common Table Expressions)

Used to structure complex queries.

```sql
WITH city_avg AS (
    SELECT city, AVG(marks) AS avg_marks
    FROM students
    GROUP BY city
)
SELECT *
FROM city_avg;
```

---

# 26. Window Functions

Perform calculations across rows without collapsing them.

Example:

```sql
SELECT
name,
marks,
RANK() OVER (ORDER BY marks DESC)
FROM students;
```

---

## Common Window Functions

- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- `SUM() OVER()`

Example:

```sql
SELECT
name,
marks,
LAG(marks) OVER (ORDER BY id)
FROM students;
```

---

# 27. Important SQL Execution Order

SQL executes in this order:

```
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

---

# 28. What To Learn Next

After mastering these fundamentals, explore:

- Indexing
- Query Optimization
- Transactions
- Execution Plans
- Database Scaling

---

# 29. Recommended Practice Projects

### Student Management System

Tables:

```
students
courses
teachers
enrollments
```

---

### E-commerce Database

Tables:

```
users
products
orders
order_items
payments
```

---

# Conclusion

PostgreSQL is a powerful relational database system used in modern backend development.

Mastering:

- Schema design
- SQL queries
- Joins
- Aggregations

gives you strong database fundamentals.

Practice writing real queries to become comfortable with SQL.

---