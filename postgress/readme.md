# PostgreSQL Developer Cheat Sheet

> A concise reference for backend developers. Includes only high-value concepts with definitions and examples.

---

# 1. MVCC (Multi-Version Concurrency Control)

### Definition

Allows multiple transactions to access the same data without blocking each other by keeping multiple versions of rows.

### Example

Transaction A

```sql
BEGIN;

SELECT balance FROM accounts WHERE id = 1;
```

Transaction B

```sql
UPDATE accounts
SET balance = 2000
WHERE id = 1;

COMMIT;
```

Transaction A still sees the old value until it ends.

---

# 2. WAL (Write Ahead Log)

### Definition

Every change is first written to WAL before being written to data files.

### Purpose

* Crash Recovery
* Replication
* Point-in-Time Recovery (PITR)

Flow

```
SQL
↓
WAL
↓
Disk
↓
Commit
```

---

# 3. VACUUM

### Definition

Removes dead tuples created by UPDATE and DELETE.

### Types

```
VACUUM
```

Reclaims dead tuples.

```
VACUUM ANALYZE
```

Updates planner statistics.

```
VACUUM FULL
```

Rewrites entire table (locks table).

---

# 4. ANALYZE

### Definition

Collects statistics used by PostgreSQL Query Planner.

```
ANALYZE users;
```

Without statistics PostgreSQL may choose poor execution plans.

---

# 5. Transaction

### Definition

Group of SQL statements executed as one unit.

```
BEGIN;

UPDATE ...

INSERT ...

COMMIT;
```

If one fails

```
ROLLBACK;
```

---

# 6. ACID

| Property    | Meaning                                  |
| ----------- | ---------------------------------------- |
| Atomicity   | All or nothing                           |
| Consistency | Database rules remain valid              |
| Isolation   | Concurrent transactions behave correctly |
| Durability  | Committed data survives crashes          |

---

# 7. Isolation Levels

| Level           | Dirty Read | Non-repeatable Read | Phantom Read   |
| --------------- | ---------- | ------------------- | -------------- |
| Read Committed  | ❌          | ✅                   | ✅              |
| Repeatable Read | ❌          | ❌                   | ❌ (PostgreSQL) |
| Serializable    | ❌          | ❌                   | ❌              |

Default

```
READ COMMITTED
```

---

# 8. Row Lock

```
SELECT *
FROM users
FOR UPDATE;
```

Locks selected rows until transaction completes.

Used in

* Banking
* Inventory
* Ticket Booking

---

# 9. Optimistic vs Pessimistic Locking

## Optimistic

No lock.

Uses version checking.

```
UPDATE users
SET version = version + 1
WHERE id = 1
AND version = 5;
```

---

## Pessimistic

Locks row before update.

```
SELECT *
FROM users
FOR UPDATE;
```

---

# 10. Index

### Definition

Special data structure for fast searching.

```
CREATE INDEX idx_email
ON users(email);
```

---

## Common Index Types

| Type   | Use Case                  |
| ------ | ------------------------- |
| B-Tree | Equality, Range (Default) |
| Hash   | Equality                  |
| GIN    | JSONB, Arrays, Full-text  |
| GiST   | Geometry, Ranges          |
| BRIN   | Huge sequential tables    |

---

# 11. EXPLAIN ANALYZE

Shows actual execution plan.

```
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email='abc@gmail.com';
```

Look for

* Sequential Scan
* Index Scan
* Cost
* Execution Time

---

# 12. Sequential Scan vs Index Scan

Sequential Scan

```
Reads every row
```

Index Scan

```
Uses Index
```

Rule

Small tables → Sequential Scan may be faster.

Large tables → Index Scan preferred.

---

# 13. Composite Index

```
CREATE INDEX idx_user_status
ON users(id,status);
```

Useful for

```
WHERE id = ?
AND status = ?
```

Order matters.

---

# 14. Partial Index

Indexes only matching rows.

```
CREATE INDEX idx_active_users
ON users(email)
WHERE active=true;
```

Smaller and faster.

---

# 15. Covering Index

Stores additional columns.

```
CREATE INDEX idx_email
ON users(email)
INCLUDE(name,age);
```

Can avoid reading the table.

---

# 16. Foreign Key

Maintains referential integrity.

```
user_id INT REFERENCES users(id)
```

Cannot reference non-existing parent.

---

# 17. ON DELETE Actions

| Action   | Meaning         |
| -------- | --------------- |
| CASCADE  | Delete children |
| RESTRICT | Prevent delete  |
| SET NULL | Set FK to NULL  |

---

# 18. CTE (Common Table Expression)

```
WITH high_salary AS (

SELECT *
FROM employees
WHERE salary>5000

)

SELECT *
FROM high_salary;
```

Improves readability.

Recursive CTEs support hierarchical queries.

---

# 19. Window Functions

Unlike GROUP BY, window functions do **not** collapse rows.

```
SELECT
name,
salary,
ROW_NUMBER() OVER(
ORDER BY salary DESC
)
FROM employees;
```

Common Functions

* ROW_NUMBER()
* RANK()
* DENSE_RANK()
* LAG()
* LEAD()

---

# 20. JSONB

Stores JSON efficiently.

```
SELECT data->>'city'
FROM users;
```

Supports GIN indexes.

---

# 21. Connection Pooling

Problem

```
1000 Requests

↓

1000 Connections
```

Solution

```
PgBouncer

↓

20 Shared Connections
```

---

# 22. Replication

```
Primary

↓

Read Replicas
```

Writes

↓

Primary

Reads

↓

Replicas

---

# 23. Partitioning

Splits large tables.

Example

```
Orders

2024

2025

2026
```

Types

* Range
* List
* Hash

---

# 24. Backup

Logical

```
pg_dump
```

Physical

```
Base Backup
```

Continuous

```
WAL + PITR
```

---

# 25. PostgreSQL System Catalogs

```
pg_stat_activity
```

Active connections.

```
pg_indexes
```

Indexes.

```
pg_stat_user_tables
```

Table statistics.

---

# 26. Common Production Practices

* Never use SUPERUSER for applications.
* Use connection pooling.
* Review `EXPLAIN ANALYZE`.
* Keep transactions short.
* Index foreign keys.
* Avoid `SELECT *`.
* Backup before migrations.
* Monitor slow queries.
* Use SSL in production.
