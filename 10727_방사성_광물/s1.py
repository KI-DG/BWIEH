"""
1
2 3 3
1 4 3
6 5 2
2 2 10
1 3 5
2 2 20
"""
# 방사선 물질 열과 행을 비교해서 자기가 제일 큰 수면 +1
# 갱신을 하고서 다시 비교 한다 거기서도 +1
t = int(input())

for tc in range(t):
    n, m, q = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    answer = 0
    # 처음 해준다
    # 갱신을 q번 할때마다 비교한다
    for z in range(q):
        r, c, z = map(int, input().split())
        # 갱신 해준다
        arr[r - 1][c - 1] = z
        # 처음 해준다
        r_max = [0, (-1, -1)]
        c_max = [0, (-1, -1)]
        for i in range(n):
            for j in range(m):
                if r_max[0] < arr[i][j]:
                    r_max[0], r_max[1] = arr[i][j], (i, j)
                if c_max[0] < arr[i][j]:
                    c_max[0], c_max[1] = arr[j][i], (j, i)

        if r_max[1] == c_max[1]:
            answer += 1
        print(arr)
        print(r_max)
        print(c_max)

    print(f"#{tc} {answer}")
