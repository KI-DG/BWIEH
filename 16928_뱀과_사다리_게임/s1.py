"""
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

3

4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21

5
"""
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        x = queue.popleft()
        if x == 100:
            return visited[x] - 1

        for i in range(6, 0, -1):
            nx = x + i
            if nx <= 100:
                if ladder[nx]:
                    nx = ladder[nx]
                if not visited[nx]:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)


n, m = map(int, input().split())
ladder = [0] * 101
visited = [0] * 101

for _ in range(n + m):
    start, end = map(int, input().split())
    ladder[start] = end

print(bfs(1))