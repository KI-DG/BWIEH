"""
7
1 6
6 3
3 5
4 1
2 4
4 7

4
6
1
3
1
4

12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

1
1
2
3
3
4
4
5
5
6
6
"""
from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for i in tree[now]:
            if answer[i] == 0:
                answer[i] = now
                queue.append(i)


bfs()
print(*answer[2:], sep='\n')
