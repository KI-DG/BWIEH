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
arr_sum = [0] * (n + 1)
for i in range(1, n + 1):
    arr_sum[i] = arr_sum[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr_sum[j] - arr_sum[i - 1])