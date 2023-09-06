"""
3
1 2 3
4 5 6
4 9 0
18 6
"""

n = int(input())

dp_max = [0] * 3
dp_min = [0] * 3

dp_max_tmp = [0] * 3
dp_min_tmp = [0] * 3
for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            dp_max_tmp[j] = a + max(dp_max[j], dp_max[j + 1])
            dp_min_tmp[j] = a + min(dp_min[j], dp_min[j + 1])
        elif j == 1:
            dp_max_tmp[j] = b + max(dp_max[j - 1], dp_max[j], dp_max[j + 1])
            dp_min_tmp[j] = b + min(dp_min[j - 1], dp_min[j], dp_min[j + 1])
        else:
            dp_max_tmp[j] = c + max(dp_max[j - 1], dp_max[j])
            dp_min_tmp[j] = c + min(dp_min[j - 1], dp_min[j])

    for j in range(3):
        dp_min[j] = dp_min_tmp[j]
        dp_max[j] = dp_max_tmp[j]

print(f"{max(dp_max)} {min(dp_min)}")
