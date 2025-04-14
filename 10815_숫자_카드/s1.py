"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

1 0 0 1 1 0 0 1
"""

n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

result = []
for i in num:
    if i in card:
        result.append(1)
    else:
        result.append(0)

print(*result)

"""시간초과"""