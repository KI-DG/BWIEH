'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m)//2):
        start_x, start_y = i, i
        start_value = arr[start_x][start_y]

        # 좌
        for j in range(i + 1, n - i):
            start_x = j
            pre_value = arr[start_x][start_y]
            arr[start_x][start_y] = start_value
            start_value = pre_value
        # 하
        for j in range(i + 1, m - i):
            start_y = j
            pre_value = arr[start_x][start_y]
            arr[start_x][start_y] = start_value
            start_value = pre_value
        # 우
        for j in range(i + 1, n - i):
            start_x = n - j - 1
            pre_value = arr[start_x][start_y]
            arr[start_x][start_y] = start_value
            start_value = pre_value
        # 상
        for j in range(i + 1, m - i):
            start_y = m - j - 1
            pre_value = arr[start_x][start_y]
            arr[start_x][start_y] = start_value
            start_value = pre_value

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

# python 시간초과
