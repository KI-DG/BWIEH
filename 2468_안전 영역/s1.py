"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
"""

# 비가 얼만큼 오는지는 모르는듯??
# 안전한 영역의 최대 갯수
# 연결된 부분은 한 개
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and height_map[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))


n = int(input())

height_map = [list(map(int, input().split())) for _ in range(n)]

answer = []
max_num = 0

for i in range(n):
    for j in range(n):
        if height_map[i][j] > max_num:
            max_num = height_map[i][j]

for i in range(max_num):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if height_map[j][k] > i and not visited[j][k]:
                bfs(j, k, i)
                count += 1
    answer.append(count)


print(max(answer))
