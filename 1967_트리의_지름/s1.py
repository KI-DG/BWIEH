"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

45
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, distance = list(map(int, input().split()))
    tree[parent].append([child, distance])
    tree[child].append([parent, distance])


def dfs(x, dist):
    for i in tree[x]:
        node, dis = i
        if visited[node] == -1:
            visited[node] = dist + dis
            dfs(node, dist + dis)


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

res = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[res] = 0
dfs(res, 0)

print(max(visited))
