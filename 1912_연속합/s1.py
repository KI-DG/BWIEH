"""
10
10 -4 3 1 5 6 -35 12 21 -1

33

10
2 1 -4 3 4 -4 6 5 -5 1

14

5
-1 -2 -3 -4 -5

-1
"""


n = int(input())

arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] + arr[i -1])

print(max(arr))
