numbers = [3, 7, 2, 9, 4]

for x in numbers:
    if x == 9:
        print("Found 9")
        break

arr = [5, 7, 9, 4, 8]

for x in arr:
    if x % 2 == 0:
        print("First even:", x)
        break

for i in range(100):
    x = int(input())
    if x == 0:
        break
    print(x)

for i in range(1, 11):
    if i == 6:
        break
    print(i)

total = 0

for i in range(1, 100):
    total += i
    if total > 50:
        break

print(total)

s = "python programming"

for ch in s:
    if ch == " ":
        break
    print(ch)
    