"""
Object-Oriented Programming in Python
-------------------------------------------

This file demonstrates core OOP concepts in Python:
- Classes & Objects
- Instance Methods
- Static Methods
- Class Methods
- Magic (Dunder) Methods
- Properties (@property)
- Decorators
- Inheritance & Multiple Inheritance
- Abstract Classes
- super()
- Polymorphism
- Duck typing
- composition
- nested classes

"""

#-------------------------------------------------BASIC CLASS & OBJECTS-----------------------------------------------------------------


class Car:
    """A simple Car class."""

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}.")

    def stop(self):
        print(f"You stop the {self.model}.")


car1 = Car("Ford Mustang", 2021, "Black", False)
car2 = Car("Chevrolet Camaro", 2023, "Silver", False)

print(car1.model)
print(car1.year)
print(car2.model)
print(car2.year)

car1.stop()


#------------------------------------------------STATIC METHODS----------------------------------------------



class Employee:
    """Represents an employee."""

    VALID_POSITIONS = ["manager", "cashier", "cook", "janitor"]

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def is_valid_position(position):
        return position.lower() in Employee.VALID_POSITIONS


print(Employee.is_valid_position("cook"))

# -------------------------------------------------CLASS METHODS----------------------------------------



class Student:
    """Tracks student data and GPA statistics."""

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} | GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"

    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return "No students available."

        average = cls.total_gpa / cls.count
        return f"Average GPA: {average:.2f}"


student1 = Student("Michael", 3.2)
student2 = Student("Emily", 3.8)
student3 = Student("Daniel", 4.0)

print(Student.get_count())
print(Student.average_gpa())


# ----------------------------------------MAGIC METHODS (DUNDER METHODS)------------------------------------




class Book:
    """Book class with custom magic methods."""

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def __eq__(self, other):
        return (
            self.title == other.title and
            self.author == other.author
        )

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return (
            keyword.lower() in self.title.lower() or
            keyword.lower() in self.author.lower()
        )

    def __getitem__(self, key):
        attributes = {
            "title": self.title,
            "author": self.author,
            "num_pages": self.num_pages
        }

        return attributes.get(key, f"Key '{key}' was not found.")


book1 = Book("The Great Escape", "John Walker", 324)
book2 = Book("The Great Escape", "John Walker", 104)
book3 = Book("Silent Storm", "Sarah Mitchell", 204)

print(book2["author"])



# ---------------------------------PROPERTIES (@property)----------------------------------------------------




class Rectangle:
    """Rectangle class using property decorators."""

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")


rectangle = Rectangle(3, 4)
rectangle.width = 5

print(rectangle.width)
print(rectangle.height)


#-----------------------------------------------------DECORATORS -----------------------------------------------------


def add_sprinkles(func):
    """Decorator that adds sprinkles."""

    def wrapper(*args, **kwargs):
        print("You add sprinkles!")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    """Decorator that adds fudge."""

    def wrapper(*args, **kwargs):
        print("You add fudge!")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream.")


get_ice_cream("Vanilla")



#-----------------------------------------MULTIPLE INHERITANCE------------------------------------------------


class Animal:
    """Base Animal class."""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Prey(Animal):

    def flee(self):
        print(f"{self.name} is fleeing.")


class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is hunting.")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Charlie")
hawk = Hawk("Hunter")
fish = Fish("Blue")

fish.eat()


#------------------------------------------------- ABSTRACT CLASSES ----------------------------------------------------------


from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class."""

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class SportsCar(Vehicle):

    def go(self):
        print("You drive the sports car.")

    def stop(self):
        print("You stop the sports car.")


class Bike(Vehicle):

    def go(self):
        print("You ride the bike.")

    def stop(self):
        print("You stop the bike.")


bike = Bike()

bike.go()
bike.stop()


# -------------------------------------------------------SUPER()-----------------------------------------------------------



class Shape:
    """Base shape class."""

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        status = "filled" if self.filled else "not filled"
        print(f"It is {self.color} and {status}.")


class Circle(Shape):

    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        area = 3.14 * self.radius ** 2
        print(f"It is a circle with an area of {area:.2f} cm².")
        super().describe()


class Square(Shape):

    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        area = self.width ** 2
        print(f"It is a square with an area of {area:.2f} cm².")
        super().describe()


class Triangle(Shape):

    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        area = (self.width * self.height) / 2
        print(f"It is a triangle with an area of {area:.2f} cm².")
        super().describe()


circle = Circle("Red", True, 4)
square = Square("Blue", False, 7)
triangle = Triangle("Yellow", True, 6, 8)

triangle.describe()



#----------------------------------------------------POLYMORPHISM----------------------------------------------------------------

from abc import ABC,abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        area = 3.14 * self.radius ** 2
        print(f"It is a circle with an area of {area:.2f} cm².")


class Square(Shape):

    def __init__(self, width):
        self.width = width


    def area(self):
        area = self.width ** 2
        print(f"It is a square with an area of {area:.2f} cm².")


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        area = (self.width * self.height) / 2
        print(f"It is a triangle with an area of {area:.2f} cm².")


class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("cheese",15)]

for shape in shapes:
    (shape.area())



#-----------------------------------------------------DUCK TYPING-----------------------------------------------------------------

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:

    alive = False

    def speak(self):
        print("HONK!")


animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)



#--------------------------------------------------------COMPOSITION-------------------------------------------------------------

class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car = Car("BMW","M3",500,19)

print(car.display_car())


#------------------------------------------------------NESTED CLASSES----------------------------------------------------------------
class Company:
    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Test comp")
company2 = Company("Test2 comp")

company.add_employee("test1", "manager")
company.add_employee("test2", "HR")
company.add_employee("test3", "lead")

company2.add_employee("test1", "CEO")
company2.add_employee("test2", "CFO")

for employee in company2.list_employees():
    print(employee)