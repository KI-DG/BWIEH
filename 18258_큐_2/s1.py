"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

1
2
2
0
1
2
-1
0
1
-1
0
3
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

stack = deque()
for _ in range(n):
    i = list(map(str, input().split()))

    if i[0] == 'push':
        stack.append(i[1])

    elif i[0] == 'pop':
        if stack:
            print(stack.popleft())
        else:
            print(-1)

    elif i[0] == 'size':
        print(len(stack))

    elif i[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif i[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)

    elif i[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)


