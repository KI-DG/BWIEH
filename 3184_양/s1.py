"""
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###

0 2

9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
"""
from collections import deque
# 델타탐색
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    o_cnt = 0
    v_cnt = 0

    while queue:
        x, y = queue.popleft()

        if field[x][y] == 'o':
            o_cnt += 1
        # 늑대의 수를 체크
        if field[x][y] == 'v':
            v_cnt += 1
        # 델타탐색
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            # 마당 범위를 안넘어가고 방문하지 않았으며 울타리가 아닐때
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and not field[nx][ny] == '#':
                visited[nx][ny] = 1
                queue.append((nx, ny))
                # 양의 수를 체크

    if o_cnt > v_cnt:
        v_cnt = 0
    if o_cnt <= v_cnt:
        o_cnt = 0
    o_cnt_ans.append(o_cnt)
    v_cnt_ans.append(v_cnt)


# .은 빌필드 #은 울타리 'o'는 양 'v'는 늑대
# 행과 열
r, c = map(int, input().split())
# 마당을 받아온다
field = [list(map(str, input())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
o_cnt_ans = []
v_cnt_ans = []
for i in range(r):
    for j in range(c):
        if not field[i][j] == '#' and not visited[i][j]:
            bfs(i, j)

print(sum(o_cnt_ans), sum(v_cnt_ans))

# 내가 생각한 조건
# .인 부분만 시작
#
# 울타리를 만나면 bfs 종료후 양과 늑대의 수 비교
# 양 > 늑대 양은 다 살아남음
# 양 <= 늑대 늑대만 살아남음
#
# 살아남은 양과 늑대의 수 출력

