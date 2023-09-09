"""
4 6
101111
101010
101011
111011
15
4 6
110110
110110
111111
111101
9
"""
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] += arr[x][y]

    return arr[n - 1][m - 1]


n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))

print(bfs(0, 0))
