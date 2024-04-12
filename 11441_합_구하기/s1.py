"""
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4

60
90
120
150
40

3
1 0 -1
6
1 1
2 2
3 3
1 2
2 3
1 3

1
0
-1
1
-1
0
"""

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    answer = 0
    i, j = map(int, input().split())
    # for 문을 두번 돌아서 시간초과
    for a in range(i - 1, j):
        answer += arr[a]

    print(answer)
# 시간초과
