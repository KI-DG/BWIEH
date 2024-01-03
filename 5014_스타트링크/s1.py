"""
10 1 10 2 1

6

100 2 1 1 0

use the stairs
"""
from collections import deque


def bfs(start_stair):
    queue = deque()
    queue.append(start_stair)
    visited[start_stair] = 1
    while queue:
        start_stair = queue.popleft()
        # 시작하는 층이 목표와 같으면 횟수를 return
        if start_stair == goal:
            return visited[start_stair] - 1

        up_stair = start_stair + up
        down_stair = start_stair - down

        if down_stair > 0 and not visited[down_stair]:
            queue.append(down_stair)
            visited[down_stair] = visited[start_stair] + 1

        if up_stair <= floor and not visited[up_stair]:
            queue.append(up_stair)
            visited[up_stair] = visited[start_stair] + 1

    return "use the stairs"


floor, start, goal, up, down = map(int, input().split())
visited = [0] * (floor + 1)

print(bfs(start))
