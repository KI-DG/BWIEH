"""
5
3 2 1 -3 -1

1 4 5 3 2
"""
from collections import deque

n = int(input())
# enumerate(index, value)
queue = deque(enumerate(map(int, input().split())))

result = []

while queue:
    idx, paper = queue.popleft()
    result.append(idx + 1)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(*result)
