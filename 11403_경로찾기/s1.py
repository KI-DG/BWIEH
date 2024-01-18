"""
3
0 1 0
0 0 1
1 0 0

1 1 1
1 1 1
1 1 1

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0

1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


# 플로이드-워셜 알고리즘
for i in range(n):
    for j in range(n):
        for k in range(n):
            # if graph[j][k] == 1 or (graph[j][i] == 1 and graph[i][k] == 1):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for r in graph:
    for c in r:
        print(c, end=" ")
    print()
