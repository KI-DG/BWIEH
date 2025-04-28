"""
5
5 4 1 3 2

Nice
"""

n = int(input())

arr = list(map(int, input().split()))
stack = []

now_turn = 1

for a in arr:
    stack.append(a)

    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn += 1

if stack:
    print('Sad')
else:
    print('Nice')
