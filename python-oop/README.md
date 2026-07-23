## Python OOP Concepts 

A beginner-friendly Python file that demonstrates the core principles of **Object-Oriented Programming (OOP)** using clean and practical examples.

This repository covers important OOP topics such as:

* Classes & Objects
* Instance Methods
* Static Methods
* Class Methods
* Magic (Dunder) Methods
* Properties (`@property`)
* Decorators
* Inheritance & Multiple Inheritance
* Abstract Classes
* `super()`
* Polymorphism
* Duck Typing
* Composition
* Nested Classes

---

## 📂 File Structure

```bash
PythonOOP.py
README.md
```

---

##  Topics Covered

### 1. Classes & Objects

Learn how to create classes, constructors, and objects.

Example:

```python
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
```

---

### 2. Static Methods

Understand methods that belong to the class rather than an instance.

```python
@staticmethod
def is_valid_position(position):
    return position.lower() in Employee.VALID_POSITIONS
```

---

### 3. Class Methods

Track shared class data like student counts and GPA averages.

```python
@classmethod
def get_count(cls):
    return cls.count
```

---

### 4. Magic (Dunder) Methods

Customize object behavior using methods like:

* `__str__`
* `__eq__`
* `__lt__`
* `__add__`
* `__contains__`

Example:

```python
def __str__(self):
    return f'"{self.title}" by {self.author}'
```

---

### 5. Properties (`@property`)

Use getters and setters for controlled attribute access.

```python
@property
def width(self):
    return self._width
```

---

### 6. Decorators

Learn how decorators modify function behavior.

```python
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    pass
```

---

### 7. Inheritance & Multiple Inheritance

Reuse code and create class hierarchies.

```python
class Fish(Prey, Predator):
    pass
```

---

### 8. Abstract Classes

Force subclasses to implement required methods.

```python
from abc import ABC, abstractmethod
```

---

### 9. `super()`

Access parent class methods and constructors.

```python
super().__init__(color, filled)
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/python-oop-concepts.git
```

2. Navigate into the project folder

```bash
cd python-oop-concepts
```

3. Run the Python file

```bash
python3 PythonOOP.py
```


