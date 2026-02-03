i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

n = 5
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(total)


i = 2
while i <= 10:
    print(i, end=" ")
    i += 2
