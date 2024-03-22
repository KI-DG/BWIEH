"""
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

0
0
3
0
0
8
6
3

3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3

0
0
0
3
0
1
0
6
0

2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2

0
0
0
0

3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2

0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2
"""
# east = 1 west = 2 north = 3 south = 4


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # east
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    # west
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    # north
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    # south
    elif dir == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


n, m, x, y, k = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

arr = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

nx, ny = x, y
for i in arr:
    nx += dx[i - 1]
    ny += dy[i - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i - 1]
        ny -= dy[i - 1]
        continue
    turn(i)

    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[-1]
    else:
        dice[-1] = maps[nx][ny]
        maps[nx][ny] = 0

    print(dice[0])
