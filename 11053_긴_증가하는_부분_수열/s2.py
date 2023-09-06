'''
6
10 20 10 30 20 50
'''

n = int(input())

arr = list(map(int, input().split()))

# 값을 더해줄 dp 값을 초기화 한다
dp = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        # 현재의 위치보다 이전의 위치의 원소 값이 작은지 확인
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
