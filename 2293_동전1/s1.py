"""
3 10
1
2
5

10
"""

n, k = map(int, input().split())
# 값을 담을 dp를 만들어준다.
dp = [0 for _ in range(k + 1)]
dp[0] = 1
# 동전을 담을 리스트 만들어준다.
coin = []
# 동전을 넣어주고
for i in range(1, n + 1):
    a = int(input())
    coin.append(a)
# i = coin 리스트에서 하나씩 뽑아낸다.
for i in coin:
    for j in range(i, k + 1):
        # k까지의 수에서 코인의 값 뺏을 떄 0보다 크거나 같으면 경우의 수를 더해준다.
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
