"""
3
21 Junkyu
21 Dohyun
20 Sunyoung

20 Sunyoung
21 Junkyu
21 Dohyun
"""

n = int(input())
arr = []

for _ in range(n):
    a, b = map(str, input().split())
    arr.append((int(a), b))

arr.sort(key=lambda x: x[0])

for i, j in arr:
    print(i, j)
