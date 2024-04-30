"""
2 162

5

4 42

-1

100 40021

5
"""

a, b = map(int, input().split())

count = 1

while b != a:
    count += 1
    temp = b
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2

    if temp == b:
        print(-1)
        break
else:
    print(count)
