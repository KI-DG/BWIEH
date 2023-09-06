"""
1
3 5
1 3
2 6
8 9

"""


t = int(input())

for tc in range(1, t + 1):
    answer = 0

    n, a = map(int, input().split())
    median = [a]
    for i in range(n):
        a, b = (map(int, input().split()))
        median.extend([a, b])
        median.sort()
        median_number = len(median) // 2

        answer += median[median_number] % 20171109

    print(f"#{tc} {answer}")

# 시간초과