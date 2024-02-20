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


def bfs():
    while queue:
        x, y = queue.popleft()
        # 도착지점에 오면 리턴
        if x == end_i and y == end_j:
            return visited[x][y]
        # 델타 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위
            if 0 <= nx < r and 0 <= ny < c:
                # 고슴도치 queue 이면
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and arr[x][y] == 'S':
                    # 시작 지점을 다시 바꿔줌
                    arr[nx][ny] = 'S'
                    # +1
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    # 물 queue 이면
                elif (arr[nx][ny] == '.' or arr[nx][ny] == 'S') and arr[x][y] == '*':
                    # 옆으로 퍼져가니까
                    arr[nx][ny] = '*'
                    queue.append((nx, ny))

    return 'KAKTUS'


r, c = map(int, input().split())

arr = [list(map(str, input())) for _ in range(r)]
# 방문 배열
visited = [[0] * c for _ in range(r)]

queue = deque()

for i in range(r):
    for j in range(c):
        # 고슴도치의 위치 저장
        if arr[i][j] == 'S':
            queue.append((i, j))
        elif arr[i][j] == 'D':
            end_i, end_j = i, j

for i in range(r):
    for j in range(c):
        # 물 위치 저장
        if arr[i][j] == '*':
            queue.append((i, j))

print(bfs())
