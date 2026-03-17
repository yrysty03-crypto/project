words = ["apple", "banana", "orange"]

for i, word in enumerate(words):
    print(i, word)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

for x, y, z in zip(a, b, c):
    print(x, y, z)

names = ["Alice", "Bob"]
scores = [90, 85]

for i, (name, score) in enumerate(zip(names, scores)):
    print(i, name, score)

x = 10

print(type(x))   # <class 'int'>

x = 3.5

if isinstance(x, float):
    print("It's a float")

x = "hello"

if isinstance(x, (int, float)):
    print("Number")
else:
    print("Not a number")

a = "123"
b = int(a)       # string → int

c = float("3.14")  # string → float
d = str(100)       # int → string

nums = ["1", "2", "3"]

nums_int = list(map(int, nums))
print(nums_int)

names = ["Alice", "Bob", "Charlie"]
scores = ["85", "90", "78"]  # strings!

for i, (name, score) in enumerate(zip(names, scores), start=1):
    score = int(score)  # convert
    print(f"{i}. {name} scored {score}")

