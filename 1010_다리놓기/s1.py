"""
3
2 2
1 5
13 29

1
5
67863915
"""
import math

t = int(input())

for _ in range(1, t + 1):
    n, m = map(int, input().split())
    answer = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))

    print(answer)

