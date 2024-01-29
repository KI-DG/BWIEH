"""
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

2
4
"""
# 최소 신장 트리
t = int(input())


def dfs(node, cnt):

    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            cnt = dfs(i, cnt + 1)

    return cnt


for _ in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = 0
    print(dfs(1, 0))
