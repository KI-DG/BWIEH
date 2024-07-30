"""
2
6
12

3
16
"""

t = int(input())

for _ in range(t):
    arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(10, 100):
        arr.append(arr[i - 1] + arr[i - 5])
    n = int(input())

    print(arr[n - 1])

