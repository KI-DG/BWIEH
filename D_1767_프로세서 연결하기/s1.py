"""
3
1
7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
9
0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1
11
0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0 1 0 0
0 1 0 1 1 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
"""

t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def chek(y, x):
    # 상 하 좌 우 방향 연결될 갯수
    direction = [0, 0, 0, 0]
    for i in range(4):
        now_y, now_x = y, x
        length = 0
        # 인덱스 벗어나지 않고 직선으로 계속하려면
        while 0 < now_x < n - 1 and 0 < now_y < n - 1:
            length += 1
            now_y += dy[i]
            now_x += dx[i]
            # 코어를 마주했으면
            if arr[now_y][now_x] == 1:
                break
        else:
            direction[i] = length
    return direction


def connect(y, x, i):
    now_y, now_x = y, x
    while 0 < now_x < n - 1 and 0 < now_y < n - 1:
        now_y += dy[i]
        now_x += dx[i]
        arr[now_y][now_x] ^= 1


def dfs(current, min_sum, result_cnt):
    global answer
    # 연결된 수가 더 많으면 바꿔준다
    if result_cnt > answer[0]:
        answer[0] = result_cnt
        answer[1] = min_sum
    # 연결된 수가 같으면 더 작은것으로 바꿔준다
    elif result_cnt == answer[0]:
        if answer[1] > min_sum:
            answer[1] = min_sum
    if current == cnt:
        return
    y, x = core[current][0], core[current][1]
    # 방향 확인 막혀있는지 아닌지
    direction = chek(y, x)
    for i in range(4):
        # 움직이지 못하는 방향은 보지 않음 (막혀있을때)
        if direction[i] == 0:
            continue
        # 선을 열ㄴ결
        connect(y, x, i)
        dfs(current + 1, min_sum + direction[i], result_cnt + 1)
        connect(y, x, i)
    dfs(current + 1, min_sum, result_cnt)


for tc in range(1, t + 1):
    answer = [0, 0]
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 코어의 좌표 list
    core = []
    # 연결할 코어 의 수
    cnt = 0
    # 가장자리는 연결되어있으니 뺴준다
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j] == 1:
                core.append((i, j))
                cnt += 1

    dfs(0, 0, 0)
    result = answer[1]
    print(f"#{tc} {result}")
