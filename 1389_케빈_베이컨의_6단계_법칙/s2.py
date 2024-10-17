"""
5 5
1 3
1 4
4 5
4 3
3 2

3
"""
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for t in a_list[target]:
            if not visited[t]:
                visited[t] = visited[target] + 1
                queue.append(t)


n, m = map(int, input().split())

a_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())

    a_list[a].append(b)
    a_list[b].append(a)

res = []
for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res)) + 1)

# bfs 문제
