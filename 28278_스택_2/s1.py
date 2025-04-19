"""
9
4
1 3
1 5
3
2
5
2
2
5

1
2
5
3
3
-1
-1
"""
import sys
# 시간초과 해결 방법
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        x = arr[0]
    else:
        x, y = arr[0], arr[1]

    if x == 1:
        stack.append(y)
    elif x == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x == 3:
        print(len(stack))
    elif x == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif x == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

