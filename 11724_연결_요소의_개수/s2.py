"""
6 5
1 2
2 5
5 1
3 4
4 6
2
"""


def dfs(x, depth):

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            answer += 1
            visited[i] = True
        else:
            dfs(i, 0)
            answer += 1

print(answer)
