"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

2

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0

1
"""
import sys
n = int(sys.stdin.readline())

teams = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
points = 10000000000


def dfs(a, idx):
    global points
    if a == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += teams[i][j]
                elif not visited[i] and not visited[j]:
                    link += teams[i][j]
        points = min(points, abs(start - link))
        return

    for x in range(idx, n):
        if not visited[x]:
            visited[x] = 1
            dfs(a + 1, x + 1)
            visited[x] = 0


dfs(0, 0)
print(points)
