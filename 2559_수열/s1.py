"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3

21

10 5
3 -2 -4 -9 0 3 7 13 8 -3

31
"""
n, k = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n + 1)
answer = -1 * 99999
for i in range(1, n + 1):
    dp[i] += dp[i - 1] + arr[i - 1]

for i in range(1, n - k + 2):
    temp_sum = dp[i + k - 1] - dp[i - 1]

    if temp_sum > answer:
        answer = temp_sum

print(answer)

