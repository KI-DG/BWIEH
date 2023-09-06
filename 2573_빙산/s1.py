"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

2
"""
# bfs(너비 우선탐색) 으로 풀어야 될거 같다!! deque 사용


from collections import deque
# 델타탐색 (범위) 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    # 들어오자마자
    visited[x][y] = True
    queue = deque([(x, y)])
    sea_list = []
    # queue에 들어 있으면
    while queue:
        x, y = queue.popleft()
        sea = 0
        # 지도에서 넘어가면 안됨
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 주변에 빙산이 아님 바다를 더해줌
                if not iceberg[nx][ny]:
                    sea += 1
                # 주변이 빙산이고 방문하지 않았으면 다시 queue에 넣어줌
                elif iceberg[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

        if sea > 0:
            sea_list.append((x, y, sea))
    # 년이 바뀌면 주변 바다 만큼 빼줘야 된다
    for x, y, sea in sea_list:
        iceberg[x][y] = max(0, iceberg[x][y] - sea)
    return 1


n, m = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        # 빙산이면 얼음 리스트에 넣어준다
        if iceberg[i][j]:
            ice.append((i, j))

year = 0
# 만일 얼음리스트가 비어있지 않으면
while ice:
    # 방문했는지 확인 리스트 만들어 주고
    visited = [[False] * m for _ in range(n)]
    # 녹는 리스트
    melts_list = []
    group = 0
    for i, j in ice:
        # 빙산이고 방문하지 않았으면 bfs
        if iceberg[i][j] and not visited[i][j]:
            group += bfs(i, j)
        # 바다면 녹는 리스트에 넣어준다
        if iceberg[i][j] == 0:
            melts_list.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(melts_list)))
    year += 1

if group < 2:
    print(0)

