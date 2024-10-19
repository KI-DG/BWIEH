"""
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

2 3
2 3 4
"""
from collections import deque

n = int(input())

members = list([] for _ in range(n + 1))

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    members[a].append(b)
    members[b].append(a)


def bfs(x):
    queue = deque()
    visited[x] = 1
    queue.append(x)

    while queue:
        x = queue.popleft()
        for i in members[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1


president = []
cnt = 99999999
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    m = max(visited)
    if m == cnt:
        president.append(i)
    elif m < cnt:
        president = [i]
        cnt = m


print(cnt - 1, len(president))
print(*president)
