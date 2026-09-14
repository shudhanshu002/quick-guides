# def grp_by_services(data):
#     result = {}
    
#     for item in data:
#         service = item["service"]
#         cost = item["cost"]
        
#         if service in result:
#             result[service] += cost
#         else:
#             result[service] = cost
            
#     return result


from collections import defaultdict

def group_by_service(data):
    d = defaultdict(int)
    
    for item in data:
        d[item["service"]] += item["cost"]
        
    return dict(d)


# 1. defaultdict (you already saw this)

# 👉 Auto-creates values for missing keys

# from collections import defaultdict

# d = defaultdict(int)
# d["a"] += 1


# ✔ Use for:

# Counting
# Grouping
# Accumulation
# 2. Counter (VERY IMPORTANT)

# 👉 Counts frequency automatically

# from collections import Counter

# arr = [1, 2, 2, 3, 3, 3]
# c = Counter(arr)

# print(c)


# Output:

# {3: 3, 2: 2, 1: 1}

# 🔥 Powerful operations
# c.most_common(1)   # top element
# c[2]               # frequency of 2

# When to use
# Frequency problems
# Top K elements
# Anagram checks
# 3. deque (Double-ended queue)

# 👉 Faster than list for insert/delete at both ends

# from collections import deque

# dq = deque()

# dq.append(1)      # right
# dq.appendleft(2)  # left

# dq.pop()
# dq.popleft()



# def find_dup(arr):
#     dup = set()
#     seen = set()
#     for val in arr:
#         if val in seen:
#             dup.add(val)
#         seen.add(val)
        
#     return dup



def top_n_services(services, n):
    return sorted(services, key=lambda x: x["cost"], reverse=True)[:n]


# ---- Input ----
services = [
    {"name": "EC2",   "cost": 500},
    {"name": "S3",    "cost": 120},
    {"name": "RDS",   "cost": 340},
    {"name": "Lambda","cost": 80},
]

# ---- Output ----
print(top_n_services(services, 2))


def fibonaaci(n):
    if n == 0 or n == 1:
        return n
    return fibonaaci(n-1) + fibonaaci(n-2)




# ✅ Your code
# def flatten(nested):
#     return [item for sublist in nested for item in sublist]

# 🧠 What it means (expand it mentally)

# This:

# [item for sublist in nested for item in sublist]


# is exactly the same as:

# result = []

# for sublist in nested:
#     for item in sublist:
#         result.append(item)

# return result




def sol(services):
    d = {}
    
    for val in services:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
            
    lst = sorted(d, key=lambda x:d[x], reverse=True)
    return lst[0]


# return max(d, key=lambda x: d[x])


from collections import defaultdict

def group_by_service(data, threshold):
    d = defaultdict(int)
    
    for item in data:
        d[item["service"]] += item["amount"]
        
    lst = {}
    
    for key, val in d.items():
        if val > threshold:
            lst[key] = val
            
    return lst


def filter(resources, prefix):
    prefix = prefix.lower()
    return [res for res in resources if res.lower().startswith(prefix)]


def sliding(lst):
    n = len(lst)
    
    if n < 3:
        return -1
    if n == 3:
        return sum(lst)
    
    agg = 0
    
    
    for i in range(0,3):
        agg += lst[i]
    
    re = agg
    
    for i in range(3,n):
        agg += lst[i]
        agg -= lst[i-3]
        re = max(re, agg)
        
    return re