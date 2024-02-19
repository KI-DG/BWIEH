"""
6
6
10
13
9
8
1

33
"""

n = int(input())

dp = [0] * 10001
wine = [0]
for i in range(1, n + 1):
    wine.append(int(input()))

dp[1] = wine[1]
# 이거를 안할시 index 에러
if n > 1:
    dp[2] = wine[1] + wine[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + wine[i], dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i])

print(max(dp))
