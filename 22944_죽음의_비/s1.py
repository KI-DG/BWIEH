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
# 상하좌우로 이동한다. 만약 이동할 곳이 격자 밖이라면 이동할 수 없다.
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 이동한 곳이 안전지대라면 반복을 종료한다.
# 이동한 곳에 우산이 있다면 우산을 든다. 만약, 이동할 때부터 우산을 가지고 있다면 가지고 있는 우산을 버리고 새로운 우산으로 바꾼다.
# 버린 우산은 더 이상 사용할 수 없다.
# 죽음의 비를 맞았을 때, 우산을 가지고 있다면 우산의 내구도가 1이 감소하고 만약 우산을 가지고 있지 않는다면 체력이 1 감소한다.
# 만약 우산의 내구도가 0이 되면 들고 있는 우산이 사라진다.
# 만약 체력이 0이 되면 죽는다...
# 아직 체력이 남았다면 안전지대까지 위 과정을 반복한다.


def bfs(x, y, hp, dur):
    global answer
    queue = deque()
    umbrella = False
    queue.append((x, y, hp, dur))
    while queue:

        x, y, hp, dur = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 체력이 0 이면 죽어서 -1을 출력
                if hp == 0:
                    answer = -1
                    return answer

                # 우산의 내구도가 다 떨어지면 우산이 없어짐
                if dur == 0:
                    umbrella = False
                # 안전지대가 아니고 우산이 없으면 피가 1깍임
                if safe_arr[nx][ny] == '.' and not umbrella:
                    hp -= 1
                    answer += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, hp, dur))
                # 안전지대가 아니고 우산이 있으면 내구도가 1깍임
                if safe_arr[nx][ny] == '.' and umbrella:
                    dur -= 1
                    answer += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, hp, dur))
                if safe_arr[nx][ny] == 'U':
                    umbrella = True
                    answer += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, hp, dur))
                # 안전지대이면 종료
                if safe_arr[nx][ny] == 'E':
                    return answer
    return -1


n, stamina, durability = map(int, input().split())

safe_arr = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    safe_arr.append(list(map(str, input())))
answer = 0
for i in range(n):
    for j in range(n):
        if safe_arr[i][j] == 'S':
            bfs(i, j, stamina, durability)

print(answer)

# 틀렸습니다.
