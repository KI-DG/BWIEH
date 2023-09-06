"""
4 10 4
S..U
....
....
...E
6

4 2 6
S..U
....
....
...E
-1

4 3 3
S..U
....
....
...E
6
"""
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, stamina, 0, 0))
    # 체력으로 변환
    visited[x][y] = stamina
    while queue:
        # x,y 좌표, 체력, 우산, count
        x, y, hp, um, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 안전지대이면 종료
                if safe_arr[nx][ny] == "E":
                    return cnt + 1
                # 새롭게 갱신해준다
                new_hp, new_um = hp, um
                # 우산이라면 새롭게 우산만 갱신해준다
                if safe_arr[nx][ny] == 'U':
                    new_um = durability - 1
                # 비가 오는곳이면서
                else:
                    # 우산이 0 보다 크다면 내구도 -1
                    if new_um > 0:
                        new_um -= 1
                    # 체력이 0보다 크면 체력 -1
                    else:
                        new_hp -= 1
                # 체력이 없다면 넘어가자
                if new_hp == 0:

                    continue
                # 체력이
                if visited[nx][ny] < new_hp:
                    queue.append((nx, ny, new_hp, new_um, cnt + 1))
                    visited[nx][ny] = new_hp

    return -1


n, stamina, durability = map(int, input().split())

safe_arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

start_x, start_y = 0, 0

for i in range(n):
    for j in range(n):
        if safe_arr[i][j] == 'S':
            start_x, start_y = i, j

print(bfs(start_x, start_y))
