class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

del p1

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Person:
  pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 20)
print(p1.name)
print(p1.age)
