"""
3
12 10 4
2

3
54 18 6
6
"""
n = int(input())

scv = list(map(int, input().split()))
# scv가 한마리 일수도 있어서 넣어준다
scv.extend([0, 0])

dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
# 조건문을 통과하기 위해
dp[scv[0]][scv[1]][scv[2]] = 1
# 뮤탈이 할수 있는 콤보
comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3)]

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                print(dp[i][j][k])
                for c in comb:
                    n_i = i - c[0] if i - c[0] >= 0 else 0
                    n_j = j - c[1] if j - c[1] >= 0 else 0
                    n_k = k - c[2] if k - c[2] >= 0 else 0
                    if dp[n_i][n_j][n_k] == 0 or dp[n_i][n_j][n_k] > dp[i][j][k] + 1:
                        dp[n_i][n_j][n_k] = dp[i][j][k] + 1
# 한마리 1로 먼저 넣어주고 했으니 1을 빼준다
print(dp[0][0][0] - 1)


