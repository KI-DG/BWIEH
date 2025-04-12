"""
5
3 4
1 1
1 -1
2 2
3 3

1 -1
1 1
2 2
3 3
3 4
"""

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

for i, j in arr:
    print(i, j)
