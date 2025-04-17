"""
3 16

3
5
7
11
13
"""


def prime_is(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    else:
        return True


n, m = map(int, input().split())

for j in range(n, m + 1):
    result = prime_is(j)
    if result:
        print(j)

