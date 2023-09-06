"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""


def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        # 방문하지 않았다면
        if not visited[i]:
            dfs(i, num)


n = int(input())

a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

# 어떤 것들끼리 연결되어 있는지 확인
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)

if not result:
    print(-1)
else:
    print(result[0] - 1)
