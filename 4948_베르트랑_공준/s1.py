"""
1
10
13
100
1000
10000
100000
0

1
4
3
21
135
1033
8392
"""


def prime_is(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    else:
        return True


while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for j in range(n + 1, (2 * n) + 1):
        if prime_is(j):
            count += 1

    print(count)

# 틀렸습니다.... ? 왜...?