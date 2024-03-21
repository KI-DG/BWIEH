"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

8
"""
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and gold_map[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                count = max(count, visited[nx][ny])
                queue.append((nx, ny))

    return count - 1


n, m = map(int, input().split())

gold_map = [list(map(str, input())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if gold_map[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
