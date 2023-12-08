"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

30
"""

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[n - 1]))
