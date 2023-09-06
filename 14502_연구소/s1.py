"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
9
"""

# bfs는 deque 로 풀어줘야된다
# 벽을 3개 세운다
# 그 다음에 바이러스를 델타탐색으로 다채워준다 deque 사용
# 안전영역 최대값을 가지게 하면된다.

from collections import deque
import copy
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    global result
    queue = deque()

    laboratory_map = copy.deepcopy(laboratory)
    for i in range(n):
        for j in range(m):
            if laboratory_map[i][j] == 2:
                queue.append((i, j))

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and laboratory_map[nx][ny] == 0:
                laboratory_map[nx][ny] = 2
                queue.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if laboratory_map[i][j] == 0:
                count += 1

    result = max(result, count)


# 벽 3개를 먼저 만들어 줘야된다
def make_wall(count):
    # 3개의 벽이 완성되면 bfs 실행
    if count == 3:
        bfs()
        return
    # 3개의 벽을 세우는 경우의 수를 만들어준다
    for i in range(n):
        for j in range(m):
            if laboratory[i][j] == 0:
                laboratory[i][j] = 1
                make_wall(count + 1)
                # 초기화
                laboratory[i][j] = 0


n, m = map(int, input().split())

laboratory = [list(map(int, input().split())) for _ in range(n)]

result = 0

make_wall(0)

print(result)

