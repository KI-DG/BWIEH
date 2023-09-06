import heapq

t = int(input())

for tc in range(1, t + 1):
    answer = 0
    lower = []
    higher = []

    n, m = map(int, input().split())
    for i in range(n):
        a, b = (map(int, input().split()))
        if a < m:
            heapq.heappush(lower, -1 * a)
        else:
            heapq.heappush(higher, a)

        if b < m:
            heapq.heappush(lower, -1 * b)
        else:
            heapq.heappush(higher, b)

        if len(lower) != len(higher):
            if len(lower) > len(higher):
                heapq.heappush(higher, m)
                val = heapq.heappop(lower)
                m = -1 * val
            elif len(lower) < len(higher):
                heapq.heappush(lower, -1 * m)
                m = heapq.heappop(higher)

        answer = (answer + m) % 20171109

    print(f"#{tc} {answer}")

