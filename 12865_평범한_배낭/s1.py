"""
4 7
6 13
4 8
3 6
5 12
14
"""


n, k = map(int, input().split())
dp = [[0, 0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = dp[i][0]
        v = dp[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i - 1][j - w], knapsack[i - 1][j])

print(knapsack[n][k])
