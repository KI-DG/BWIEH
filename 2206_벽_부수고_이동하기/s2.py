from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(start_x, start_y, break_wall):
    queue = deque()
    queue.append([start_x, start_y, break_wall])
    visited[start_x][start_y][break_wall] = 1
    while queue:
        x, y, w = queue.popleft()

        if (x, y) == (n - 1, m - 1):
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if break_map[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    queue.append([nx, ny, w + 1])

                if break_map[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])

    return -1


n, m = map(int, input().split())

break_map = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, 0))
