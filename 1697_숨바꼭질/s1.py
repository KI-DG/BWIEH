"""
5 17

4
"""
from collections import deque


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            print(visited[x])
            break
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= max_number and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


max_number = 10 ** 5
visited = [0] * (max_number + 1)
n, k = map(int, input().split())

bfs()
