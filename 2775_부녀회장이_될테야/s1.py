'''
2
1
3
2
3

6
10
'''

t = int(input())

for _ in range(1, t + 1):
    k = int(input())
    n = int(input())

    dp = [i for i in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    print(dp[-1])
