for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

numbers = [3, -2, 7, -5, 4]

for x in numbers:
    if x < 0:
        continue
    print(x)

s = "python"

for ch in s:
    if ch in "aeiou":
        continue
    print(ch)

for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)

for i in range(1, 10):
    if i > 5:
        continue
    print(i)
