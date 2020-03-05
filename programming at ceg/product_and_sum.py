import itertools


def product(l):
    temp = 1
    for i in l:
        temp *= i
    return temp


n, p, k = map(int, input().split())
flag = 0
l = [x for x in range(n)]
for e in itertools.combinations_with_replacement(l, k):
    if sum(e) == n and product(e) == p:
        flag = 1
        print(*e)
        break
if flag == 0:
    print("No")
