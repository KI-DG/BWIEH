"""
3
8
10
16

3 5
5 5
5 11
"""


def is_prime_num(x):
    for y in range(2, x):
        # i로 나누어 떨어지면 소수가 아니므로 False 리턴
        if x % y == 0:
            return False
    # False 가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴
    return True


arr = [False] * (10**4)
for i in range(10**4):
    arr[i] = is_prime_num(i)

t = int(input())

for _ in range(1, t + 1):
    n = int(input())
    a, b = 0, 0
    for i in range(2, (n // 2) + 1):
        if arr[i] and arr[n - i]:
            a, b = i, n - i

    print(a, b)
