'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''
# DP 문제 - 거꾸로 해야될려나?
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + arr[i][0] > n:
        answer[i] = answer[i + 1]
    else:
        result = answer[i + arr[i][0]] + arr[i][1]
        if result > answer[i + 1]:
            answer[i] = result
        else:
            answer[i] = answer[i + 1]

print(answer)