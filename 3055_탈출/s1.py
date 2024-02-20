"""
3 3
D.*
...
.S.

3

3 3
D.*
...
..S

KAKTUS

3 6
D...*.
.X.X..
....S.

6

5 4
.D.*
....
..X.
S.*.
....

4
"""
from collections import deque
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def water():
    water_queue = deque(water_area)

    while water_queue:
        water_x, water_y = water_queue.popleft()

        for z in range(4):
            water_nx = water_x + dx[z]
            water_ny = water_y + dy[z]

            if 0 <= water_nx < r and 0 <= water_ny < c:
                if arr[water_nx][water_ny] == '.' and visited[water_nx][water_ny] == 0:
                    arr[water_nx][water_ny] = '*'
                    visited[water_nx][water_ny] = -1
                    water_queue.append([water_nx, water_ny])


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                if arr[nx][ny] == 'D' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    return visited[nx][ny] - 1

        water()

    return 'KAKTUS'


r, c = map(int, input().split())

arr = [list(map(str, input())) for _ in range(r)]
# 방문 배열
visited = [[0] * c for _ in range(r)]
# 홍수가 나기 시작하는 곳 (여러 곳일 수도)
water_area = []
# 고슴도치가 시작지점
start_x, start_y = 0, 0

for i in range(r):
    for j in range(c):
        # 돌이 있으면 방문할 수 없음
        if arr[i][j] == 'X':
            visited[i][j] = -1
        # 물이 있으면 방문할 수 없음
        elif arr[i][j] == '*':
            visited[i][j] = -1
            water_area.append([i, j])
        # 고슴도치의 위치 저장
        elif arr[i][j] == 'S':
            start_x, start_y = i, j
            arr[i][j] = '.'

print(bfs(start_x, start_y))

# 오류