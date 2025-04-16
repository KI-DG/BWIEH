"""
1 1

1

3 5

15

1 123

123

121 199

24079
"""

a, b = map(int, input().split())

res = a * b
# 최대 공약수 (유클리드 호재법)
while b:
    if a > b:
        a, b = b, a
    b %= a
# 최소 공배수
print(res // a)
