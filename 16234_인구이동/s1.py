"""
2 20 50
50 30
20 40
1

2 40 50
50 30
20 40
0

2 20 50
50 30
30 40
1
"""
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    visited[x][y] = 1
    queue = deque()
    population = []
    queue.append((x, y))
    population.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    population.append((nx, ny))

    return population


n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0

while True:
    visited = [[0] * n for _ in range(n)]
    union = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                country = bfs(i, j)
                if len(country) > 1:
                    union = 1
                    number = sum(arr[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        arr[x][y] = number
    if union == 0:
        break
    answer += 1

print(answer)
