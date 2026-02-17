nums = [-10, 5, -3, 2, -8]

result = sorted(nums, key=lambda x: abs(x))
print(result)

words = ["apple", "kiwi", "banana", "fig"]

result = sorted(words, key=lambda s: len(s))
print(result)

data = [(1, 3), (4, 1), (2, 2)]

result = sorted(data, key=lambda x: x[1])
print(result)

scores = {"Alice": 85, "Bob": 72, "Carol": 90}

result = sorted(scores.items(), key=lambda item: item[1])
print(result)

words = ["cat", "dog", "ant"]

result = sorted(words, key=lambda s: s[-1])
print(result)
