"""
10
1 2 0 1 3 2 1 5 4 2

5
"""
n = int(input())

arr = list(map(int, input().split()))

dp = [n + 1] * n
dp[0] = 0
for i in range(n):
    for j in range(1, arr[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
    print(-1)
else:
    print(dp[n - 1])


