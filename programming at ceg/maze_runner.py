def numberOfPaths(x, y):
    path = 1
    for i in range(y, (x + y - 1)):
        path *= i
        path //= (i - y + 1)
    return path % 100000000


n, m = [int(i) for i in input().split()]
print(numberOfPaths(n, m))
