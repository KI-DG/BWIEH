"""
2
1

10
3
"""

n = int(input())
cnt = 0
while n >= 1:

    if n % 3 == 1:
        n -= 1
        cnt += 1
    elif n % 3 == 0:
        n = (n // 3)
        cnt += 1
    elif n % 2 == 0:
        n = (n // 2)
        cnt += 1

print(cnt - 1)
# 시간초과
