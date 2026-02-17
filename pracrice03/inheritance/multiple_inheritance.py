class A:
    def show(self):
        return "Class A"

class B:
    def display(self):
        return "Class B"

class C(A, B):
    pass

obj = C()
print(obj.show())
print(obj.display())

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):
    pass

c = C()
print(c.greet())

class A:
    def message(self):
        return "A"

class B:
    def message(self):
        return "B"

class C(A, B):
    def message(self):
        return super().message()

c = C()
print(c.message())

class Father:
    def __init__(self):
        print("Father init")

class Mother:
    def __init__(self):
        print("Mother init")

class Child(Father, Mother):
    pass

c = Child()
