"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

3
1 7 13
"""
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(m - y1 - 1, m - y2 - 1, -1):
            arr[j][i] = 1
result = []


def bfs(x, y):
    global result
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append((nx, ny))
                size += 1

    result.append(size)


for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
print(*result)