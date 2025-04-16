"""
3
6
20
100

7
23
101
"""


def is_prime_number(x):
    if x == 0 or x == 1:  # 0과 1을 처리
        return False
    elif x == 2:
        return True
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    else:
        return True


tc = int(input())

for _ in range(tc):
    n = int(input())

    while True:
        if is_prime_number(n):
            print(n)
            break
        else:
            n += 1


