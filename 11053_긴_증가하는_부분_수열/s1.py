"""
6
10 20 10 30 20 50
12
10 10 10 10 10 10 10 10 10 10 10 20
"""

n = int(input())
arr = list(map(int, input().split()))

answer = 1

for j in range(0, n - 1):
    cnt = 1
    start = arr[j]
    if answer < n - j:
        for i in range(j, n):
            if start < arr[i]:
                cnt += 1
                start = arr[i]

                if cnt > answer:
                    answer = cnt

print(answer)

'''
틀렸습니다
7
1 3 5 4 5 2 7
'''
