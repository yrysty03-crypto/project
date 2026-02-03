while True:
    x = int(input())
    if x == 0:
        break
    print("You entered:", x)

n = int(input())
i = 2

while i <= n:
    if n % i == 0:
        print("First divisor:", i)
        break
    i += 1

i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

while True:
    x = int(input())
    if x < 0:
        break
    print(x)

total = 0

while True:
    x = int(input())
    if x == 0:
        break
    total += x

print("Sum:", total)

i = 1
while True:
    if i % 7 == 0:
        print(i)
        break
    i += 1
