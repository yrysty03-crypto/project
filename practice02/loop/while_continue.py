i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

while True:
    x = int(input())
    if x < 0:
        continue
    if x == 0:
        break
    print(x)

i = 1
while i <= 10:
    if i == 6:
        i += 1
        continue
    print(i)
    i += 1

total = 0

while True:
    x = int(input())
    if x <= 0:
        continue
    total += x
    if total >= 50:
        break

print(total)

i = 0
while i <= 15:
    i += 1
    if i % 3 == 0:
        continue
    print(i)