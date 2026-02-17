class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

a = Animal()
d = Dog()

print(a.speak())
print(d.speak())

class Employee:
    def salary(self):
        return 3000

class Manager(Employee):
    def salary(self):
        base = super().salary()
        return base + 2000

m = Manager()
print(m.salary())

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return 5 * 4

r = Rectangle()
print(r.area())

class Vehicle:
    def move(self):
        return "Vehicle moves"

class Car(Vehicle):
    def move(self):
        return "Car drives on road"

c = Car()
print(c.move())
