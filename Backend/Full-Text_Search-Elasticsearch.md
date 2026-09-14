# 🚀 Elasticsearch Full-Text Search — Complete Guide

## 📌 Overview

Elasticsearch is a distributed search engine designed for **fast, scalable, and intelligent full-text search**.
Unlike traditional databases, it uses **inverted indexing and relevance scoring** to deliver results in milliseconds.

---

## ❓ Why Not Traditional SQL Search?

```sql
SELECT * FROM products WHERE name LIKE '%phone%';
```

### Problems:

* ❌ Slow (full table scan)
* ❌ No understanding of language (plural, synonyms)
* ❌ No ranking (only match/no match)

### ✅ Elasticsearch Solves:

* Fast lookup using inverted index
* Relevance-based ranking
* Fuzzy, semantic, and complex queries
* Distributed scalability

---

## 🧠 Core Concept: Inverted Index

Instead of storing documents directly:

```
Doc1: "iphone is great"
Doc2: "samsung phone"
```

Elasticsearch builds:

```
iphone  → Doc1  
great   → Doc1  
samsung → Doc2  
phone   → Doc2  
```

👉 Enables **direct lookup → no full scan**

---

## 🏗️ Architecture

```
Cluster → Nodes → Indices → Shards
```

* **Cluster**: Entire system
* **Node**: Single server
* **Index**: Database-like structure
* **Shard**: Partition of index (for scaling)

👉 Parallel processing across shards = high speed

---

## 📄 Documents (JSON)

```json
{
  "name": "iPhone 15",
  "description": "Latest Apple smartphone",
  "price": 1200
}
```

---

## ⚙️ Mapping (Schema)

Defines field types:

```json
{
  "title": "text",
  "price": "keyword"
}
```

* `text` → analyzed (full-text search)
* `keyword` → exact match

---

## 🔍 Text Analysis Pipeline

### 1. Character Filters

* Remove HTML, normalize text

### 2. Tokenization

```
"I love programming"
→ ["I", "love", "programming"]
```

### 3. Token Filters

* Lowercase → `Programming → programming`
* Stopwords removed → `is, the`
* Stemming → `running → run`

### ✅ Final Tokens:

```
["love", "program"]
```

---

## 📦 Indexing Flow

```
Raw JSON → Analysis → Tokens → Inverted Index → Stored
```

---

## 🔎 Query Execution

### Example Search:

```
"running shoes"
```

### Steps:

1. Query analyzed → `["run", "shoe"]`
2. Match tokens in inverted index
3. Score results
4. Return ranked documents

---

## 📊 Scoring (Relevance)

Uses **BM25 algorithm**

### Factors:

* **TF (Term Frequency)** → more occurrences = higher score
* **IDF (Inverse Doc Frequency)** → rare terms = more important
* **Field Length** → shorter = more relevant

---

## 🔄 Query Types

### 1. Match (Full-text)

```json
{
  "query": {
    "match": {
      "description": "fast phone"
    }
  }
}
```

### 2. Term (Exact)

```json
{
  "query": {
    "term": {
      "price": 1000
    }
  }
}
```

### 3. Boolean

```json
{
  "query": {
    "bool": {
      "must": [{ "match": { "name": "iphone" } }],
      "filter": [{ "range": { "price": { "lte": 1500 } } }]
    }
  }
}
```

---

## ⚡ Query vs Filter

| Feature       | Query  | Filter        |
| ------------- | ------ | ------------- |
| Affects Score | ✅      | ❌             |
| Performance   | Medium | Fast (cached) |

---

## 🌍 Distributed Search

```
Query → All Shards → Local Search → Merge Results → Return Top Results
```

👉 Parallel execution = ultra-fast performance

---

## ⏱️ Near Real-Time (NRT)

* ~1 second delay after indexing
* Uses refresh interval
* Data first stored in buffer → then searchable

---

## 🚀 Advanced Features

### 🔹 Fuzzy Search

```
"iphnoe" → "iphone"
```

### 🔹 Autocomplete (Edge N-Grams)

```
laptop → l, la, lap, lapt...
```

### 🔹 Synonyms

```
car = automobile
```

### 🔹 Highlighting

```
Best <em>laptop</em> for gaming
```

---

## 📊 SQL vs Elasticsearch

| Feature          | SQL     | Elasticsearch |
| ---------------- | ------- | ------------- |
| Full-text Search | ❌ Slow  | ✅ Fast        |
| Ranking          | ❌       | ✅             |
| Fuzzy Search     | ❌       | ✅             |
| Scalability      | Limited | Distributed   |
| Schema           | Fixed   | Flexible      |

---

## 🧪 Use Cases

* E-commerce search (Amazon-like)
* Log analysis (DevOps)
* Autocomplete systems
* Recommendation engines

---

## 🔁 End-to-End Flow

```
User Query → Analyze → Token Match → Score → Rank → Return Results
```

---

## ⚡ Why It's Fast

* Inverted index (no scanning)
* Parallel shard execution
* Optimized scoring (BM25)
* Cached filters
* Efficient storage (memory + disk)

---

## ⚠️ When NOT to Use

* Heavy transactions → use SQL
* Complex joins → not supported
* Strict real-time systems → not ideal

---

## 🧠 Final Mental Model

> Elasticsearch =
> **"A distributed system that maps words → documents and ranks them instantly."**

---

## ❗ Common Mistakes

* Wrong mapping (`text` vs `keyword`)
* Poor analyzer configuration
* Overusing fuzzy queries
* Bad shard sizing

---

## 📌 Conclusion

Elasticsearch transforms raw text into a **search-optimized structure**, enabling:

* Lightning-fast queries
* Intelligent ranking
* Scalable distributed search
