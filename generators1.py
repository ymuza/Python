def topten():
    n = [2,3,4,5]
    yield n[1]
    # n = 1
    # while n <= 10:
    #     sq = n*n
    #     n = n+1
    #     yield sq

print(type(topten()))
for i in topten():
    print(type(i))