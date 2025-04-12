"""
5
0 4
1 2
1 -1
2 2
3 3

1 -1
1 2
2 2
3 3
0 4
"""

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))

arr.sort()

for i, j in arr:
    print(j, i)