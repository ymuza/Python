
def is_even(n):
    return n % 2 == 0


nums = [2, 3, 4, 34, 67, 78, 9]


evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)
