"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다
# 최단경로의 지도를 만들어 줘야된다 버스 최단경로
# 최소화 == 최단경로

import heapq
# N개의 도시가 있다.
n = int(input())
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
m = int(input())
parent = [[] for _ in range(n + 1)]
deapq =[]

for _ in range(m):
    city_s, city_e, cost = map(int, input().split())
    # 시작한 도시가 부모 거기에 이제 도착하는 곳 경비
    parent[city_s].append((city_e, cost))
# 시작하는 곳, 도착하는 곳
start, end = map(int, input().split())

# heapq[]

print(start, end)

