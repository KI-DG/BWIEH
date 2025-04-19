"""
3

1

24

4
"""

n = int(input())

result = 0
x = 1
while x*x <= n:
    x += 1
    result += 1
print(result)

# print(int(input() ** 0.5))
