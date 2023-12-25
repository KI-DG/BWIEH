"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

27
6
64

2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2

1
2
3
4
"""

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            answer += arr[i][j]

    print(answer)

# 시간초과
