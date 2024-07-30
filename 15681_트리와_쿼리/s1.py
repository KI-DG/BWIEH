"""
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8

9
4
1
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, q = map(int, input().split())

tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(now):
    visited[now] = 1
    for i in tree[now]:
        if not visited[i]:
            dfs(i)
            visited[now] += visited[i]


dfs(r)
for _ in range(q):
    node = int(input())
    print(visited[node])
