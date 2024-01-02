"""
3
1033 8179
1373 8017
1033 1033

6
7
0
"""
from collections import deque

t = int(input())


# 소수판별함수
def is_prime(number):
    if number == 1:
        return False
    for x in range(2, int(number**1/2)+1):
        if number % x == 0:
            return False
    return True


def bfs(s, e):
    queue = deque()
    queue.append((s, 0))

    while queue:
        s, count = queue.popleft()

        if s == e:
            return count

        # 네자리 수
        for i in range(4):
            # 각 자리마다 10번
            for j in range(10):
                new_s = list(str(s))
                new_s[i] = str(j)
                new_s = int(''.join(new_s))
                # 1000 이하로 떨어지면
                if 1000 < new_s and not visited[new_s] and prime[new_s]:
                    visited[new_s] = 1
                    queue.append((new_s, count + 1))


# 소수판별테이블
prime = [False]
for pri in range(1, 10000):
    prime.append(is_prime(pri))

for _ in range(1, t + 1):

    start, end = map(int, input().split())

    visited = [0] * 10000
    visited[start] = 1
    print(bfs(start, end))
