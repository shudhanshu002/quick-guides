🔹 1. What is a Class?

👉 A class = blueprint/template to create objects

class Person:
    pass
🔹 2. What is an Object?

👉 An object = instance of a class

p1 = Person()
🔹 3. Basic Class Example
class Person:
    def greet(self):
        print("Hello")

p1 = Person()
p1.greet()
🔍 What is self?

👉 self = reference to current object

p1.greet()

Internally becomes:

Person.greet(p1)
🔹 4. Attributes (Variables inside class)
🔸 Instance attributes
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ram")
print(p1.name)
🔸 Constructor (__init__)

👉 Runs when object is created

def __init__(self, name):
    self.name = name
🔹 5. Methods
🔸 Instance method
def greet(self):
    print(self.name)
🔸 Class method
class Person:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
🔸 Static method
class Math:
    @staticmethod
    def add(a, b):
        return a + b
🔹 6. Class vs Instance Variables
class Person:
    species = "Human"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable
🔍 Difference
Type	Belongs to
Instance	object
Class	class
🔹 7. Encapsulation

👉 Hiding internal data

class Bank:
    def __init__(self):
        self._balance = 0   # protected
🔸 Access control (convention)
Type	Syntax
Public	x
Protected	_x
Private	__x
class A:
    def __init__(self):
        self.__x = 10
🔹 8. Inheritance

👉 Reusing code from another class

🔸 Example
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

d = Dog()
d.speak()
🔸 Method overriding
class Dog(Animal):
    def speak(self):
        print("Bark")
🔹 9. Polymorphism

👉 Same function, different behavior

def func(x):
    print(x)

func(10)
func("hello")
🔸 With classes
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")
🔹 10. Abstraction

👉 Hide implementation details

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
🔹 11. Magic Methods (Dunder Methods)
🔸 __str__
class A:
    def __str__(self):
        return "Hello"
🔸 __len__
class A:
    def __len__(self):
        return 10
🔸 __add__
class A:
    def __add__(self, other):
        return self.x + other.x
🔹 12. Object Memory Model (IMPORTANT)
class A:
    pass

a = A()

👉 Internally:

class stored once
object stores data separately
🔹 13. Everything is Object
print(type(10))
print(type("hi"))

👉 all are objects

🔹 14. Example (Real-world style)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)










🔹 PART 1: What does @something do?
🔸 Core Idea

👉 @something = decorator

It modifies or wraps a function/class.

🔹 1. Basic Understanding
@decorator
def func():
    pass

👉 Equivalent to:

def func():
    pass

func = decorator(func)
🔹 2. Example (IMPORTANT)
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

Apply:

@my_decorator
def say_hello():
    print("Hello")

say_hello()

Output:

Before
Hello
After
🔹 3. Why decorators?

Used to:

logging
authentication
validation
caching

👉 Very common in backend frameworks

🔹 4. Common Built-in Decorators
🔸 @staticmethod
class A:
    @staticmethod
    def add(a, b):
        return a + b

👉 No self, no cls
👉 behaves like normal function inside class

🔸 @classmethod
class A:
    count = 0

    @classmethod
    def show(cls):
        return cls.count

👉 gets class (cls), not object

🔸 @property (VERY IMPORTANT)
class A:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x

Usage:

a = A()
print(a.x)   # no parentheses
🔸 Setter
class A:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

👉 Used for controlled access

🔹 PART 2: Public / Protected / Private in Python

⚠️ Important truth:

Python does NOT have strict access control like Java/C++

It uses naming conventions + name mangling

🔹 1. Public
class A:
    def __init__(self):
        self.x = 10

👉 Access anywhere:

a = A()
print(a.x)
🔹 2. Protected (Convention)
class A:
    def __init__(self):
        self._x = 10

👉 _x means:

“You should not access this outside”

BUT:

a = A()
print(a._x)   # still works
🔥 So protected is just a warning, not restriction
🔹 3. Private (Name Mangling)
class A:
    def __init__(self):
        self.__x = 10
Try accessing:
a = A()
print(a.__x)   # ❌ ERROR
But internally:
print(a._A__x)   # works

👉 Python converts:

__x → _ClassName__x

This is called:

🔥 Name Mangling

🔹 4. Why Name Mangling?

👉 Prevent accidental override in inheritance

Example
class A:
    def __init__(self):
        self.__x = 10

class B(A):
    def __init__(self):
        self.__x = 20

👉 These are different:

_A__x
_B__x







