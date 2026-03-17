nums = [1, 2, 3, 4]

squares = list(map(lambda x: x*x, nums))
print(squares)

nums = [1, 2, 3]

strings = list(map(str, nums))
print(strings)

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

words = ["hello", "", "world", ""]

clean = list(filter(lambda x: x != "", words))
print(clean)

nums = [1, 2, 3, 4, 5]

result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print(result)

from functools import reduce
nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)
print(total)

from functools import reduce

nums = [1, 2, 3, 4]

product = reduce(lambda a, b: a * b, nums)
print(product)

from functools import reduce

nums = [3, 7, 2, 9, 5]

maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)

