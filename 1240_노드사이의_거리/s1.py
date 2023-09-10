"""
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
2
7
"""
from collections import deque


def bfs(start, find):
    queue = deque()
    # 시작점과 거리의 초기값 설정
    queue.append((start, 0))
    # 방문했는지 만들어준다
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        x, y = queue.popleft()
        # 찾는 지점과 같다면 거리 리턴
        if x == find:
            return y
        # 연결된 노드의 모두 찾아본다
        for i, j in tree[x]:
            if not visited[i]:
                visited[i] = True
                # 이제까지 거리를 추가해준다
                queue.append((i, y + j))


n, m = map(int, input().split())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, distance = map(int, input().split())
    tree[a].append((b, distance))
    tree[b].append((a, distance))

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))
