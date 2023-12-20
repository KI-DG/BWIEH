"""
4

5
"""

n = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])

# 메모리 초과 - 결과값에 나누기를 하면 나온다 (반복문으로 안으로 넣어서 해결)

