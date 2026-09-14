🔹 1. What is a Variable in Python?

A variable = name that refers to a value in memory

x = 10

👉 x points to an integer object 10

Unlike C++:

No need to write int x = 10
Python decides type automatically (dynamic typing)
🔹 2. Basic Data Types in Python
✅ 1. Integer (int)
a = 10
print(a)
✅ 2. Float (float)
b = 3.14
print(b)
✅ 3. String (str)
c = "Hello"
print(c)
✅ 4. Boolean (bool)
d = True
print(d)
✅ 5. None Type (NoneType)
e = None
print(e)

👉 means “no value”

🔹 3. Check Type of Variable
x = 10
print(type(x))

Output:

<class 'int'>
🔹 4. Printing Multiple Variables
a = 10
b = 20

print(a, b)

Output:

10 20
🔹 5. Different Ways to Print
✅ 1. Simple print
name = "Sudhanshu"
print(name)
✅ 2. With text
age = 20
print("Age is:", age)
✅ 3. Using f-string (MOST IMPORTANT)
name = "Sudhanshu"
age = 20

print(f"My name is {name} and age is {age}")

👉 Best and modern way

✅ 4. Using format()
print("My name is {} and age is {}".format(name, age))
✅ 5. Using + (not recommended much)
print("Name: " + name)

⚠️ Only works with strings

🔹 6. Special Print Options
Separator (sep)
print(1, 2, 3, sep="-")

Output:

1-2-3
End (end)
print("Hello", end=" ")
print("World")

Output:

Hello World
🔹 7. Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)
🔹 8. Type Conversion (IMPORTANT)
x = "10"
y = int(x)

print(y, type(y))
🔹 9. Input + Print Together
name = input("Enter name: ")
print(f"Hello {name}")
🔹 10. Advanced Types (VERY IMPORTANT)
List
lst = [1, 2, 3]
print(lst)
Tuple
t = (1, 2, 3)
print(t)
Dictionary
d = {"name": "Sudhanshu", "age": 20}
print(d)
Set
s = {1, 2, 3}
print(s)
🔹 11. Printing Each Element
lst = [10, 20, 30]

for x in lst:
    print(x)
🔹 12. Under the Hood (Important for you)

When you do:

print(x)

Python internally:

Converts object to string using __str__() or __repr__()
Sends output to stdout
🔹 13. Common Mistakes

❌ Mixing types:

age = 20
print("Age is " + age)  # ERROR

✅ Fix:

print("Age is", age)

or

print(f"Age is {age}")




🧠 3. DATA TYPES (DEEP UNDERSTANDING)
🔹 Immutable Types
int
float
str
tuple

👉 Cannot change after creation

x = 10
x = x + 1  # new object created


🔹 Mutable Types
list
dict
set
arr = [1, 2]
arr.append(3)  # same object modified


➤ Basic operations
print(a + b)   # 13  (Addition)
print(a - b)   # 7   (Subtraction)
print(a * b)   # 30  (Multiplication)
print(a / b)   # 3.333... (Division → always float)
print(a % b)   # 1   (Modulus → remainder)
print(a ** b)  # 1000 (Power → 10^3)
print(a // b)  # 3   (Floor division)


print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


print(x and y)  # False
print(x or y)   # True
print(not x)    # False

x += 5   # x = x + 5
x -= 2
x *= 3
x /= 2
x //= 2
x %= 3
x **= 2

lst = [1, 2, 3]

print(2 in lst)      # True
print(5 not in lst)  # True

a = 5   # 101
b = 3   # 011

print(a & b)  # 1   (AND)
print(a | b)  # 7   (OR)
print(a ^ b)  # 6   (XOR)
print(~a)     # -6  (NOT)
print(a << 1) # 10  (Left shift)
print(a >> 1) # 2   (Right shift)


🔹 8. Operator Precedence (VERY IMPORTANT)

Python follows priority:

**
* / // %
+ -
comparison (==, >, etc.)
not
and
or


print(2 + 3 * 4)   # 14

👉 not 20, because * runs first











2. Method 1: Using round() (for calculations)
x = 3.1415926535

print(round(x, 2))  # 3.14

👉 Syntax:

round(number, digits)
Important:
print(round(2.675, 2))  # 2.67 ❗

👉 Why? Because of floating-point precision issue

🔹 3. Method 2: Using f-string (BEST for printing)
x = 3.1415926535

print(f"{x:.2f}")  # 3.14

👉 .2f means:

2 digits after decimal
formatted as float
More examples:
print(f"{x:.3f}")  # 3.142
print(f"{x:.1f}")  # 3.1
🔹 4. Method 3: format() function
x = 3.1415926535

print("{:.2f}".format(x))  # 3.14







🧠 4. CONTROL FLOW

🔹 4. Truthy vs Falsy (VERY IMPORTANT)

Python doesn’t need strictly True/False

❌ False-like (Falsy):
False
0
0.0
''
[]
{}
None
✅ Everything else = True

if 0:
    print("Run")
else:
    print("Not Run")


🔹 If-Else
if x > 10:
    print("big")
elif x == 10:
    print("equal")
else:
    print("small")


🔹 8. One-Line (Ternary) if
x = 10

result = "Even" if x % 2 == 0 else "Odd"
print(result)











🔹 Example 1: Basic Loop
for i in range(5):
    print(i)

Output:

0 1 2 3 4







🔹 Example 2: Loop over List
lst = [10, 20, 30]

for x in lst:
    print(x)
🔹 Example 3: Loop over String
for ch in "hello":
    print(ch)


🔹 1. Difference: continue vs pass
✅ continue → skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

Output:

0 1 3 4

👉 What happened?

When i == 2, Python skips the rest of the loop body
Moves directly to next iteration
✅ pass → do nothing (placeholder)
for i in range(5):
    if i == 2:
        pass
    print(i)

Output:

0 1 2 3 4

👉 What happened?

pass literally does nothing
Execution continues normally
🔍 Key Difference
Feature	continue	pass
Effect	skips iteration	does nothing
Flow control	YES	NO
Use case	ignore certain cases	placeholder for future code
🔹 Visual Understanding
continue:
Loop → condition → SKIP → next loop
pass:
Loop → condition → DO NOTHING → continue same flow
🔹 Real Use Case
continue:
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)   # prints only even
pass:
for i in range(5):
    if i == 3:
        pass  # will add logic later
    print(i)
🔹 2. Delimiters (Arguments) of range()

range() is used in loops like:

range(start, stop, step)
✅ 1. Only one argument
range(5)

👉 means:

start = 0
stop = 5
step = 1

Output:

0 1 2 3 4
✅ 2. Two arguments
range(2, 6)

👉 means:

start = 2
stop = 6
step = 1

Output:

2 3 4 5
✅ 3. Three arguments
range(1, 10, 2)

👉 means:

start = 1
stop = 10
step = 2

Output:

1 3 5 7 9
🔹 Important Rules
❗ Stop is NOT included
range(0, 5)  # 0 to 4
❗ Step can be negative
range(5, 0, -1)

Output:

5 4 3 2 1
❗ Step cannot be 0
range(1, 10, 0)  # ERROR
🔍 Under the Hood

range() does NOT create a list:

range(1_000_000)

👉 It stores:

start
stop
step

and generates values on demand (memory efficient)


🔹 1. What is a Function?

👉 A function = reusable block of code

def greet():
    print("Hello")

Call it:

greet()
🔹 2. Basic Function Types
✅ 1. No parameter, no return
def say_hello():
    print("Hello World")

say_hello()
✅ 2. With parameter, no return
def greet(name):
    print(f"Hello {name}")

greet("Sudhanshu")
✅ 3. With parameter and return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
✅ 4. No parameter, but return
def get_number():
    return 10

print(get_number())
🔹 3. Multiple Return Values
def calc(a, b):
    return a + b, a * b

sum_val, prod_val = calc(2, 3)
print(sum_val, prod_val)

👉 Actually returns a tuple

🔹 4. Default Parameters
def greet(name="Guest"):
    print(f"Hello {name}")

greet()        # Guest
greet("Ram")   # Ram
🔹 5. Keyword Arguments
def info(name, age):
    print(name, age)

info(age=20, name="Sudhanshu")
🔹 6. Variable Length Arguments
✅ *args → multiple positional
def total(*nums):
    print(nums)
    return sum(nums)

print(total(1, 2, 3, 4))
✅ **kwargs → multiple keyword
def details(**data):
    print(data)

details(name="Sudhanshu", age=20)
🔹 7. Lambda Functions (One-line functions)
square = lambda x: x * x

print(square(5))

👉 Used for short, quick operations








🔹 8. Functions as Arguments (VERY IMPORTANT)
def apply(func, value):
    return func(value)

print(apply(lambda x: x*x, 5))

👉 Functions are first-class objects








🔹 PART 1: Built-in Functions (sum, max, min, etc.)

These are predefined functions that work on iterables (list, tuple, set, etc.).

🔸 1. sum()
lst = [1, 2, 3, 4]
print(sum(lst))   # 10
With start value:
print(sum(lst, 10))  # 20

👉 Internally:

Iterates through list
Keeps adding
🔸 2. max()
lst = [3, 7, 2, 9]
print(max(lst))  # 9
Multiple values:
print(max(3, 7, 2))  # 7
With key (VERY IMPORTANT):
words = ["apple", "banana", "kiwi"]
print(max(words, key=len))  # banana

👉 key decides comparison logic

🔸 3. min()
print(min([3, 7, 2, 9]))  # 2

Same as max, but smallest

🔸 4. len()
print(len([1,2,3]))  # 3
print(len("hello"))  # 5

👉 returns number of elements

🔸 5. sorted()
lst = [3,1,4,2]
print(sorted(lst))        # [1,2,3,4]
print(sorted(lst, reverse=True))  # [4,3,2,1]
With key:
words = ["apple", "banana", "kiwi"]
print(sorted(words, key=len))
🔸 6. reversed()
lst = [1,2,3]
print(list(reversed(lst)))  # [3,2,1]
🔸 7. any() and all() (VERY IMPORTANT)
any() → at least one True
print(any([0, False, 5]))  # True
all() → all must be True
print(all([1, True, 5]))  # True
print(all([1, 0, 5]))     # False
🔸 8. abs()
print(abs(-10))  # 10
🔸 9. round()
print(round(3.1415, 2))  # 3.14
🔸 10. enumerate()
lst = ['a','b','c']

for i, val in enumerate(lst):
    print(i, val)
🔸 11. zip()
a = [1,2,3]
b = ['x','y','z']

print(list(zip(a, b)))

Output:

[(1,'x'), (2,'y'), (3,'z')]
🔹 Summary (Built-ins)
Function	Use
sum()	total
max()	largest
min()	smallest
len()	count
sorted()	sorting
any()	at least one true
all()	all true
zip()	combine lists
enumerate()	index + value



🔹 PART 1: max() / min() — comparison logic + default behavior
✅ 1. Default behavior (VERY IMPORTANT)
words = ["apple", "banana", "kiwi"]
print(max(words))

👉 Output:

kiwi
Why?

Because by default Python compares lexicographically (dictionary order):

"kiwi" > "banana" > "apple"

👉 Comparison is done using:

"a" < "b"

Internally calls:

__lt__(), __gt__()
🔹 2. Using key (custom comparison logic)
print(max(words, key=len))  # banana

👉 What happens internally:

Python does:

apple  → len = 5
banana → len = 6
kiwi   → len = 4

Then compares based on key output, not actual value.

🔹 3. More Custom Logic Examples
🔸 Example: based on last character
words = ["apple", "banana", "kiwi"]
print(max(words, key=lambda x: x[-1]))

👉 compares:

apple → 'e'
banana → 'a'
kiwi → 'i'

Result:

kiwi   # because 'i' is max
🔸 Example: absolute value
nums = [-10, 5, -3]
print(max(nums, key=abs))  # -10

👉 compares:

10, 5, 3
🔸 Example: multiple criteria
words = ["a", "bb", "cc", "ddd"]

print(max(words, key=lambda x: (len(x), x)))

👉 First compare by length, then lexicographically

🔹 4. min() works exactly same
print(min(words, key=len))  # kiwi
🔹 5. Important Edge Case
print(max([], default=0))

👉 avoids error:

ValueError: max() arg is an empty sequence











🔹 1. Immutable Example (Looks like pass by value)
def change(x):
    x = x + 5
    print("Inside:", x)

a = 10
change(a)
print("Outside:", a)

Output:

Inside: 15
Outside: 10

👉 Why?

int is immutable
new object created inside function
🔹 2. Mutable Example (Looks like pass by reference)
def modify(lst):
    lst.append(4)

my_list = [1,2,3]
modify(my_list)
print(my_list)

Output:

[1,2,3,4]

👉 Why?

list is mutable
same object modified




PART 2: Pass by Value vs Reference (Deep Understanding)
❗ First: Python does NOT have pure pass-by-value or pass-by-reference

👉 Official term:

Pass-by-object-reference
(or pass-by-assignment)

🔹 1. Core Idea

When you pass a variable:

def func(x):
    ...

👉 You pass:

reference to object
NOT copy
NOT direct variable binding like C++
🔹 2. Why ints behave like pass-by-value
def change(x):
    x += 5

a = 10
change(a)
print(a)

Output:

10
🔍 Step-by-step (IMPORTANT)
Before:
a → 10
Function call:
x → 10 (same object)
Inside:
x += 5

👉 This creates NEW object:

x → 15 (new object)
a → 10 (unchanged)
🔹 Conclusion:

👉 int is immutable, so it behaves like pass-by-value

BUT actually:

reference was passed
object couldn’t be modified
🔹 3. Lists behave like pass-by-reference
def change(lst):
    lst.append(5)

a = [1,2]
change(a)
print(a)

Output:

[1,2,5]
🔍 Why?
a → [1,2]
x → same object

Then:

lst.append(5)

👉 modifies SAME object

🔹 4. Important Distinction
🔸 Modification vs Reassignment
def func(x):
    x = [9,9,9]   # reassignment

a = [1,2]
func(a)
print(a)

Output:

[1,2]
🔸 Modification
def func(x):
    x.append(9)

a = [1,2]
func(a)
print(a)

Output:

[1,2,9]
🔹 5. Final Classification
Type	Mutable?	Behavior
int	❌	behaves like value
float	❌	behaves like value
str	❌	behaves like value
tuple	❌	behaves like value
list	✅	behaves like reference
dict	✅	behaves like reference
set	✅	behaves like reference
🔹 6. What is it CALLED?

👉 Official name:

Pass-by-object-reference

Also called:

pass-by-assignment (most accurate)
🔹 7. One-line Understanding

👉 Python passes references,
but behavior depends on mutability

🔹 8. Advanced Insight (Important)

Everything in Python is:

print(type(10))

👉 object:

<class 'int'>











1. What is Namespace?

👉 A namespace = a mapping (dictionary) of
name → object

Example:

x = 10

Internally:

"x" → 10
🔹 2. What is Scope?

👉 Scope = where a variable can be accessed

🔹 3. LEGB Rule (Search Order)

When Python sees a variable like:

print(x)

It searches in this order:

L → E → G → B
🔹 4. Break it Down
🔸 L → Local Scope

Inside current function

def func():
    x = 5
    print(x)

func()

👉 Python finds x in local scope

🔸 E → Enclosing Scope

Function inside another function

def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()

👉 inner() doesn’t have x, so Python looks in enclosing (outer)

🔸 G → Global Scope

Defined outside functions

x = 100

def func():
    print(x)

func()

👉 Python finds x in global

🔸 B → Built-in Scope

Python’s predefined names

print(len([1,2,3]))

👉 len is from built-in namespace

🔹 5. Full Example (LEGB in action)
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()

Output:
local


Remove local:
def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

Output:

enclosing


🔹 1. What is a String?

👉 A string = sequence of characters

s = "hello"
"hello" is an object of type str
Internally: sequence like ['h','e','l','l','o']
🔹 2. String Properties (VERY IMPORTANT)
✅ Immutable
s = "hello"
s[0] = 'H'   # ❌ ERROR

👉 You cannot change characters directly

✅ Ordered
s = "hello"
print(s[0])  # h
✅ Iterable
for ch in "abc":
    print(ch)
🔹 3. Basic Operations
🔸 1. Concatenation (+)
a = "Hello"
b = "World"

print(a + " " + b)
🔸 2. Repetition (*)
print("ha" * 3)   # hahaha
🔸 3. Length
print(len("hello"))  # 5
🔸 4. Membership
print("a" in "apple")   # True
🔹 4. Indexing & Slicing (VERY IMPORTANT)
🔸 Indexing
s = "python"

print(s[0])   # p
print(s[-1])  # n
🔸 Slicing
s = "python"

print(s[1:4])   # yth
print(s[:3])    # pyt
print(s[3:])    # hon
🔸 Step slicing
print(s[::2])   # pto
print(s[::-1])  # nohtyp (reverse)
🔹 5. Common String Methods
🔸 Case conversion
s = "hello"

print(s.upper())   # HELLO
print(s.lower())   # hello
print(s.capitalize())  # Hello
🔸 Strip (remove spaces)
s = "  hello  "

print(s.strip())   # "hello"
print(s.lstrip())  # left remove
print(s.rstrip())  # right remove
🔸 Replace
s = "hello world"

print(s.replace("world", "python"))
🔸 Split
s = "a,b,c"

print(s.split(","))   # ['a','b','c']
🔸 Join (IMPORTANT)
lst = ["a", "b", "c"]

print("-".join(lst))   # a-b-c
🔸 Find / Index
s = "hello"

print(s.find("l"))   # 2
print(s.index("l"))  # 2

👉 difference:

find → returns -1 if not found
index → error if not found
🔸 Count
print("banana".count("a"))  # 3
🔹 6. String Formatting
🔸 f-string (BEST)
name = "Sudhanshu"
age = 20

print(f"My name is {name} and age is {age}")
🔸 format()
print("Name: {}, Age: {}".format(name, age))
🔹 7. Escape Characters
print("Hello\nWorld")
print("He said \"Hi\"")
🔹 8. Multiline String
s = """This is
multi-line
string"""
🔹 9. Important Concept: Immutability
s = "hello"

s = s + " world"

👉 New string is created:

"hello" → new object → "hello world"
🔍 Why important?
Safe
thread-friendly
but slightly memory-heavy if abused
🔹 10. Performance Tip

❌ Bad (creates many strings):

s = ""
for i in range(5):
    s += str(i)

✅ Better:

lst = []
for i in range(5):
    lst.append(str(i))

s = "".join(lst)
🔹 11. String Comparison
print("abc" < "abd")  # True

👉 Lexicographical (dictionary order)


🔹 2. Identity vs Equality
a = [1,2]
b = [1,2]

print(a == b)  # True (value)
print(a is b)  # False (memory)

👉 == → value
👉 is → memory location


3. Variable = Reference (VERY IMPORTANT)
a = [1,2]
b = a

b.append(3)

print(a)  # [1,2,3]

👉 Both point to same object

🔹 4. Copying Objects
❌ Wrong way
a = [1,2]
b = a
✅ Correct ways
b = a.copy()
# or
b = a[:]


🔹 5. Shallow vs Deep Copy (basic idea)
import copy

a = [[1,2],[3,4]]
b = copy.copy(a)      # shallow
c = copy.deepcopy(a)  # deep

👉 You’ll need this later for nested lists




🔹 1. What is a List?

👉 A list = ordered, mutable collection of elements

lst = [1, 2, 3, 4]
🔸 Key Properties
Feature	Meaning
Ordered	maintains order
Mutable	can change elements
Heterogeneous	can store different types
Indexed	supports indexing
🔹 2. Creating Lists
a = []
b = [1, 2, 3]
c = [1, "hello", 3.5]
🔹 3. Indexing & Access
lst = [10, 20, 30, 40]

print(lst[0])   # 10
print(lst[-1])  # 40
🔹 4. Slicing (VERY IMPORTANT)
lst = [1,2,3,4,5]

print(lst[1:4])   # [2,3,4]
print(lst[:3])    # [1,2,3]
print(lst[::2])   # [1,3,5]
print(lst[::-1])  # reverse
🔹 5. Modifying List (Mutability)
lst = [1,2,3]

lst[0] = 10
print(lst)  # [10,2,3]
🔹 6. Important List Methods
🔸 1. append() → add at end
lst = [1,2]
lst.append(3)
🔸 2. insert(index, value)
lst.insert(1, 99)
🔸 3. extend() → add multiple elements
lst.extend([4,5])
🔸 4. remove(value)
lst.remove(2)   # removes first occurrence
🔸 5. pop()
lst.pop()      # last
lst.pop(1)     # index
🔸 6. clear()
lst.clear()
🔸 7. index()
lst.index(3)
🔸 8. count()
lst.count(2)
🔸 9. sort()
lst = [3,1,2]
lst.sort()
🔸 10. reverse()
lst.reverse()
🔹 7. Built-in Functions on List
lst = [1,2,3]

len(lst)
sum(lst)
max(lst)
min(lst)
🔹 8. Looping Through List
🔸 Method 1
for x in lst:
    print(x)
🔸 Method 2 (index)
for i in range(len(lst)):
    print(lst[i])
🔸 Method 3 (best)
for i, val in enumerate(lst):
    print(i, val)
🔹 9. List Comprehension (VERY IMPORTANT)
lst = [x*x for x in range(5)]

Output:

[0,1,4,9,16]
🔸 With condition
lst = [x for x in range(10) if x % 2 == 0]
🔹 10. Nested Lists
lst = [[1,2], [3,4]]

print(lst[0][1])  # 2




🔹 1. What is a Tuple?

👉 A tuple = ordered, immutable collection

t = (1, 2, 3)
🔸 Key Properties
Feature	Meaning
Ordered	maintains order
Immutable	cannot change
Indexed	supports indexing
Heterogeneous	can store different types
🔹 2. Creating Tuples
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1, "hello", 3.5)
🔸 Special Case (VERY IMPORTANT)
Single element tuple
t = (5,)   # ✅ correct
t = (5)    # ❌ NOT tuple (just int)

👉 Comma defines tuple, not parentheses

🔹 3. Accessing Elements
t = (10, 20, 30)

print(t[0])   # 10
print(t[-1])  # 30
🔹 4. Slicing
t = (1,2,3,4,5)

print(t[1:4])   # (2,3,4)
print(t[::-1])  # reverse
🔹 5. Immutability (CORE CONCEPT)
t = (1,2,3)

t[0] = 10   # ❌ ERROR

👉 Cannot modify tuple

🔍 But tricky case:
t = ([1,2], 3)

t[0].append(5)
print(t)

Output:

([1,2,5], 3)

👉 Why allowed?

tuple is immutable
but inner list is mutable
🔹 6. Tuple Operations
🔸 Concatenation
t1 = (1,2)
t2 = (3,4)

print(t1 + t2)
🔸 Repetition
print((1,2) * 3)
🔸 Membership
print(2 in (1,2,3))  # True
🔹 7. Built-in Functions
t = (1,2,3)

len(t)
max(t)
min(t)
sum(t)
🔹 8. Tuple Methods (VERY LIMITED)

Only two:

t = (1,2,2,3)

t.count(2)   # 2
t.index(3)   # 3

👉 Unlike lists → very few methods

🔹 9. Packing & Unpacking (VERY IMPORTANT)
🔸 Packing
t = 1, 2, 3

👉 automatically becomes tuple

🔸 Unpacking
a, b, c = (1, 2, 3)
🔸 Extended unpacking
a, *b = (1,2,3,4)

print(a)  # 1
print(b)  # [2,3,4]
🔹 10. Returning Multiple Values
def func():
    return 1, 2

x, y = func()

👉 Actually returning a tuple

🔹 11. Tuple vs List (IMPORTANT)
Feature	Tuple	List
Mutability	❌	✅
Speed	faster	slower
Memory	less	more
Methods	few	many












🔹 1. What is a Dictionary?

👉 A dictionary = collection of key-value pairs

d = {
    "name": "Sudhanshu",
    "age": 20
}
🔸 Key Properties
Feature	Meaning
Unordered*	(insertion order preserved in modern Python)
Mutable	can change values
Key-Value	mapping structure
Fast lookup	O(1) average
🔹 2. Creating Dictionary
d = {}
d = {"a": 1, "b": 2}
🔸 Using dict()
d = dict(a=1, b=2)
🔸 From list of tuples
d = dict([("a",1), ("b",2)])
🔹 3. Accessing Values
d = {"name": "Ram", "age": 25}

print(d["name"])      # Ram
🔸 Safe access (get)
print(d.get("age"))        # 25
print(d.get("salary"))     # None

👉 No error if key missing

🔹 4. Adding / Updating
d["city"] = "Delhi"   # add
d["age"] = 30         # update
🔹 5. Removing Elements
d.pop("age")
d.popitem()   # removes last inserted
del d["name"]
d.clear()
🔹 6. Looping Through Dictionary
🔸 Keys
for k in d:
    print(k)
🔸 Values
for v in d.values():
    print(v)
🔸 Key + Value (MOST USED)
for k, v in d.items():
    print(k, v)
🔹 7. Important Methods
🔸 keys()
d.keys()
🔸 values()
d.values()
🔸 items()
d.items()
🔸 update()
d.update({"age": 40})
🔸 setdefault() (IMPORTANT)
d.setdefault("age", 25)

👉 adds only if key not present

🔹 8. Dictionary Comprehension
d = {x: x*x for x in range(5)}

Output:

{0:0, 1:1, 2:4, 3:9, 4:16}
🔹 9. Nested Dictionary
d = {
    "user": {
        "name": "Ram",
        "age": 25
    }
}

print(d["user"]["name"])
🔹 10. Key Rules (VERY IMPORTANT)
❗ Keys must be immutable

✅ allowed:

d = {1: "a", "key": "value", (1,2): "tuple"}

❌ not allowed:

d = {[1,2]: "value"}  # ERROR
🔍 Why?

Because dictionary uses hashing

🔹 11. Under the Hood (VERY IMPORTANT)

👉 Dictionary = hash table

🔸 How it works:
Key → hashed → index
Stored in array
Value stored with it
🔸 Example:
"age" → hash → index → store value
🔸 Why O(1)?
Direct access via hash
no linear search
🔹 12. Hash Function
print(hash("key"))

👉 unique integer used internally

🔹 13. Collision Handling

When two keys map to same index:

Python resolves using probing (advanced topic)










🔹 1. What is a Set?

👉 A set = unordered collection of UNIQUE elements

s = {1, 2, 3}
🔸 Key Properties
Feature	Meaning
Unordered	no indexing
Unique	no duplicates
Mutable	can add/remove
Fast lookup	O(1) average
🔹 2. Creating Sets
s = {1, 2, 3}
🔸 Empty set (IMPORTANT)
s = set()   # ✅ correct
s = {}      # ❌ this is dictionary
🔹 3. Duplicate Removal
s = {1, 2, 2, 3}
print(s)

Output:

{1, 2, 3}
🔹 4. Adding Elements
s = {1, 2}

s.add(3)
🔸 Add multiple
s.update([4,5])
🔹 5. Removing Elements
s.remove(2)   # error if not present
s.discard(2)  # safe (no error)
s.pop()       # removes random element
s.clear()
🔹 6. Membership Check (VERY FAST)
print(2 in s)

👉 O(1) average

🔹 7. Set Operations (VERY IMPORTANT)
🔸 Union (OR)
a = {1,2}
b = {2,3}

print(a | b)

Output:

{1,2,3}
🔸 Intersection (AND)
print(a & b)

Output:

{2}
🔸 Difference
print(a - b)

Output:

{1}
🔸 Symmetric Difference
print(a ^ b)

Output:

{1,3}
🔹 8. Methods Version
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
🔹 9. Subset / Superset
a = {1,2}
b = {1,2,3}

print(a.issubset(b))    # True
print(b.issuperset(a))  # True
🔹 10. Looping
for x in s:
    print(x)

👉 Order is NOT guaranteed

🔹 11. Important Rule: Elements must be immutable

✅ Allowed:

s = {1, "a", (1,2)}

❌ Not allowed:

s = {[1,2], 3}  # ERROR
🔹 12. Under the Hood (VERY IMPORTANT)

👉 Set is implemented using:

Hash table (same as dictionary)

🔸 How it works:
Element → hash
Stored in table
Lookup via hash
🔸 Why fast?
No linear search
Direct access via hash
🔹 13. Time Complexity
Operation	Complexity
add	O(1)
remove	O(1)
lookup	O(1)
union	O(n)
🔹 14. Set vs List
Feature	Set	List
Order	❌	✅
Duplicates	❌	✅
Access	❌ index	✅ index
Search	O(1)	O(n)
🔹 15. Real Use Cases
🔸 Remove duplicates
lst = [1,2,2,3]
lst = list(set(lst))
🔸 Check intersection
a = [1,2,3]
b = [2,3,4]

print(set(a) & set(b))
🔸 Fast lookup
s = {1,2,3}

if 2 in s:
    print("Found")
🔸 Unique characters
s = set("hello")
print(s)



