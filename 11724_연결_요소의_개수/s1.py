"""
6 5
1 2
2 5
5 1
3 4
4 6
2
"""
from collections import deque


def bfs(x):
    global answer
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:

        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            answer += 1
            visited[i] = True
        else:
            bfs(i)
            answer += 1

print(answer)
