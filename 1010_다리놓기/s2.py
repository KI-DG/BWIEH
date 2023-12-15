"""
3
2 2
1 5
13 29

"""

t = int(input())
# 최대값이 30이다
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for _ in range(1, t + 1):
    n, m = map(int, input().split())
    print(dp[n][m])
