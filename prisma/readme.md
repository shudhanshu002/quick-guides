# Prisma Developer Cheat Sheet

> High-value Prisma concepts for production backend development.

---

# 1. Prisma Architecture

```
Application

↓

Prisma Client

↓

Query Engine

↓

PostgreSQL
```

Prisma Client generates SQL.

Database executes SQL.

---

# 2. schema.prisma

Central configuration file.

Contains

* Models
* Relations
* Datasource
* Generator
* Indexes

Example

```prisma
generator client {
  provider="prisma-client-js"
}

datasource db{
  provider="postgresql"
  url=env("DATABASE_URL")
}
```

---

# 3. Prisma Client

```
const prisma=new PrismaClient();
```

Reuse a single instance.

Do not create one per request.

---

# 4. CRUD

Create

```ts
prisma.user.create()
```

Read

```ts
findUnique()

findFirst()

findMany()
```

Update

```ts
update()

updateMany()
```

Delete

```ts
delete()

deleteMany()
```

---

# 5. findUnique vs findFirst

findUnique

Uses

```
@id

@unique
```

findFirst

Returns first matching row.

No unique constraint required.

---

# 6. select vs include

select

Returns selected fields.

```ts
select:{
 email:true
}
```

include

Returns related models.

```ts
include:{
 interviews:true
}
```

---

# 7. Filtering

Comparison

```
gt

gte

lt

lte

equals

not
```

String

```
contains

startsWith

endsWith

mode:"insensitive"
```

Logical

```
AND

OR

NOT
```

Collection

```
in

notIn
```

---

# 8. Pagination

Offset

```ts
skip

take
```

Cursor

```ts
cursor:{
 id:100
}
```

Prefer cursor pagination for large datasets.

---

# 9. Atomic Updates

```
increment

decrement

multiply

divide

set
```

Example

```ts
data:{
 views:{
   increment:1
 }
}
```

Avoids race conditions.

---

# 10. Transactions

Simple

```ts
await prisma.$transaction([
 ...
])
```

Interactive

```ts
await prisma.$transaction(async(tx)=>{

})
```

Use interactive transactions when business logic depends on previous queries.

---

# 11. Relations

One-to-One

```
User

↓

Profile
```

One-to-Many

```
User

↓

Interviews
```

Many-to-Many

```
Students

↓

Courses
```

---

# 12. Relation Operations

Create

```ts
create
```

Connect existing

```ts
connect
```

Disconnect

```ts
disconnect
```

Replace relations

```ts
set
```

Connect or create

```ts
connectOrCreate
```

Nested Upsert

```ts
upsert
```

---

# 13. Relation Filters

```
some
```

At least one child.

```
none
```

No children.

```
every
```

All children satisfy condition.

---

# 14. Referential Actions

```prisma
onDelete:Cascade
```

Options

* Cascade
* Restrict
* SetNull
* NoAction

---

# 15. Raw SQL

Read

```ts
$queryRaw
```

Write

```ts
$executeRaw
```

Never concatenate user input.

Correct

```ts
await prisma.$queryRaw`

SELECT *

FROM "User"

WHERE id=${id}

`;
```

Avoid

```
$queryRawUnsafe()
```

unless absolutely necessary.

---

# 16. Error Codes

| Code  | Meaning                   |
| ----- | ------------------------- |
| P2002 | Unique constraint         |
| P2003 | Foreign key violation     |
| P2025 | Required record not found |

---

# 17. Logging

```ts
const prisma=new PrismaClient({

log:[
"query",
"warn",
"error"
]

})
```

Useful for debugging slow queries.

---

# 18. Client Extensions

Create reusable client methods.

```ts
const prisma = new PrismaClient().$extends({
  model:{
    user:{
      findByEmail(email){
        return prisma.user.findUnique({
          where:{email}
        })
      }
    }
  }
})
```

Preferred over middleware for many customization cases.

---

# 19. Performance Tips

* Use `select` whenever possible.
* Avoid `findMany()` without pagination.
* Prevent N+1 queries with relation loading.
* Add database indexes.
* Use `createMany()` for bulk inserts.
* Use transactions for related writes.
* Profile slow queries with `EXPLAIN ANALYZE`.

---

# 20. Migrations

Development

```bash
npx prisma migrate dev
```

Production

```bash
npx prisma migrate deploy
```

Reset

```bash
npx prisma migrate reset
```

---

# 21. db push vs migrate

| Command     | Migration | History |
| ----------- | --------- | ------- |
| db push     | ❌         | ❌       |
| migrate dev | ✅         | ✅       |

Use

```
db push
```

Only for prototypes or rapid development.

---

# 22. db pull

Reads existing database.

```
Database

↓

schema.prisma
```

Used for introspection.

---

# 23. Shadow Database

Used internally by

```
migrate dev
```

Validates migrations before applying them.

---

# 24. Recommended Production Setup

```
Next.js

↓

Singleton Prisma Client

↓

PgBouncer

↓

Primary PostgreSQL

↓

Read Replicas
```

---

# 25. Best Practices

* Keep one `PrismaClient` instance.
* Commit migration folders.
* Review generated SQL.
* Use `migrate deploy` in production.
* Use transactions for multi-step writes.
* Prefer cursor pagination for feeds.
* Never use `db push` in production.
* Use parameterized raw SQL.
* Handle Prisma error codes explicitly.
* Learn SQL alongside Prisma—Prisma generates SQL, it doesn't replace it.
