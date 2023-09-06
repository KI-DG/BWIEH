"""
1
5
2
2 5
6 10
"""

t = int(input())

for tc in range(1, t + 1):
    L = int(input()) * 2
    N = int(input())
    arr = [0] * 100000

    start = 1
    for _ in range(N):
        s, e = map(int, input().split())
        for i in range(s * 2, (e * 2) + 1):
            arr[i] = 1

    while start <= L:
        answer = -9999999999
        count = 0
        for i in range(start, start + L):
            if arr[i] == 1:
                count += 1
            answer = max(answer, count)

        start += 1
    answer = answer // 2

    print(f"#{tc} {answer}")
