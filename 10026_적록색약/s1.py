"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
4 3
"""
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[False] * (n + 1) for _ in range(n)]
result = [0, 0]
# 색약이 아닌 사람들
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result[0] += 1
# 색약인 사람들을 구별하기 위해 초록을 빨간색으로 바꿔준다
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# 방문자 리스트 초기화
visited = [[False] * (n + 1) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result[1] += 1

print(*result)
