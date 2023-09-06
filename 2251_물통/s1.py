"""
8 9 10
1 2 8 9 10
"""

# C의 물의 양을 구하는 것 대신 A가 0일때의 구해야된다
# A가 0 일때 경우의 수는?
# 처음 물을 부었을때 10L
# 두번째 B에만 부었을때 1L
# 세번째 A에게 처음으로 부었고 B에게 부었을때 (대신 A가 B보다 작아야된다) => 크면 다시 C에게 부어준다 2L
# 네번째 B에게 붓고 B가 다시 A에게 붓고 다시 A가 C에게 부어준다 9L
# 다섯번째 A에게 붓고 C의 나머지를 B에 붓고 다시 A를 C에 부어준다 8L
from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        queue.append((x, y))


def bfs():
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        if x > 0 and y < b:
            w = min(x, b - y)
            print(w, 'aaaa')
            pour(x - w, y + w)

        if x > 0 and z < c:
            w = min(x, c - z)
            print(w, 'bbbb')
            pour(x - w, y)

        if y > 0 and x < a:
            w = min(y, a - x)
            print(w, 'cccc')
            pour(x + w, y - w)

        if y > 0 and z < c:
            w = min(y, c - z)
            print(w, 'dddd')
            pour(x, y - w)

        if z > 0 and x < a:
            w = min(z, a - x)
            print(w, 'eeee')
            pour(x + w, y)

        if z > 0 and y < b:
            w = min(z, b - y)
            print(w, 'ffff')
            pour(x, y + w)


a, b, c = map(int, input().split())
queue = deque()
answer = []
visited = [[0] * (b + 1) for _ in range(a + 1)]
bfs()
# 오름차순 정렬
answer.sort()
print(*answer)
