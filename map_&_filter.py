from functools import reduce

nums = [2, 3, 4, 34, 67, 78, 9]


evens = list(filter(lambda n: n % 2 == 0, nums))

doubles = list(map(lambda n: n*2, evens))  # map

sum = reduce()

print(evens)
print(doubles)
