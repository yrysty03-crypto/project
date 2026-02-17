class Student:
    school = "Green High School"   # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)
print(s2.school)

class Student:
    school = "Green High School"

    def __init__(self, name):
        self.name = name

Student.school = "Blue High School"

s = Student("Alice")
print(s.school)

class Person:
    count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person("A")
p2 = Person("B")

print(Person.count)

class Car:
    wheels = 4   # class variable

    def __init__(self, color):
        self.color = color   # instance variable

c1 = Car("Red")
c2 = Car("Blue")

print(c1.wheels, c2.wheels)