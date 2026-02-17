def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8

def square(x):
    return x * x

print(square(4))   # 16

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(7, 3))   # 7
