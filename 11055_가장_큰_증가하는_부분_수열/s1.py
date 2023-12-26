"""
10
1 100 2 50 60 3 5 6 7 8

113
"""

n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))
