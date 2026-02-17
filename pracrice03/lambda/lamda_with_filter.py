numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

numbers = [10, 15, 20, 25, 30]

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)

nums = [-3, -1, 0, 2, 4, -5]

positives = list(filter(lambda x: x > 0, nums))
print(positives)

words = ["hi", "hello", "bye", "world"]

long_words = list(filter(lambda s: len(s) > 3, words))
print(long_words)

names = ["Alice", "Bob", "Anna", "Mike"]

a_names = list(filter(lambda s: s.startswith("A"), names))
print(a_names)
