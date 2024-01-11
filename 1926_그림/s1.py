"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4
9
"""
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0 <= nx < n and 0 <= ny < m and painting[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1

    return count


n, m = map(int, input().split())

painting = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0
result = 0
for i in range(n):
    for j in range(m):
        if painting[i][j] == 1 and not visited[i][j]:
            answer += 1
            result = max(bfs(i, j), result)

print(answer)
print(result)
