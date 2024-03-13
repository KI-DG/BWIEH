"""
6
10 30 10 20 20 10

3
"""

n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)
