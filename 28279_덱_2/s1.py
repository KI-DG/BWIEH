"""
11
6
1 3
1 8
7
8
3
2 5
1 2
5
4
4

1
8
3
8
3
5
3
"""
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = deque()
for _ in range(n):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        stack.insert(0, arr[1])

    elif arr[0] == 2:
        stack.append(arr[1])

    elif arr[0] == 3:
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif arr[0] == 4:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif arr[0] == 5:
        print(len(stack))

    elif arr[0] == 6:
        if stack:
            print(0)
        else:
            print(1)
    elif arr[0] == 7:
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif arr[0] == 8:
        if stack:
            print(stack[-1])
        else:
            print(-1)