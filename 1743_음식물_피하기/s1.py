"""
3 4 5
3 2
2 2
3 1
2 3
1 1
4
"""
# 쓰레기가 어디있는지 위치를 만들고
# 그 배열을 델타 탐색하여 인접한 곳을 BFS로 풀면 될거 같다. == deque
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    count = 0
    queue = deque()
    queue.append((x, y))
    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count


n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 쓰레기가 어디있는지 확인
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i, j))

print(answer)
