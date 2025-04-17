"""
5
6
8
10
12
100

1
1
2
1
6
"""
prime_is = list(True for _ in range(1000001))
prime_is[0], prime_is[1] = False, False

for i in range(2, 1000001):
    if prime_is[i]:
        for j in range(i * 2, 1000001, i):
            prime_is[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for x in range(2, n // 2 + 1):
        if prime_is[x] and prime_is[n - x]:
            count += 1
    print(count)
