"""
6 4
0100
1110
1000
0000
0111
0000

15
"""
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    break_wall = False
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도 밖으로 넘어가지 않게 범위설정
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이고 벽을 부순적이 없으면
                if break_map[nx][ny] == 1 and not break_wall:
                    # 벽을 한번 부수면 True
                    break_wall = True
                    # 방문한 횟숫 +1 추가
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                # 벽이 아니고 방문하지 않았으면
                if break_map[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return -1


n, m = map(int, input().split())

break_map = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(bfs(0, 0))
# 틀렸습니다
