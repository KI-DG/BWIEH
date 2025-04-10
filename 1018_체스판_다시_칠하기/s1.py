"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

1

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

12
"""

N, M = map(int, input().split())
arr = list(input() for i in range(N))
result = 999999999999

for a in range(N - 7):
    for b in range(M - 7):
        w_index = 0
        b_index = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if arr[i][j] != "W":
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if arr[i][j] != "W":
                        b_index += 1
                    else:
                        w_index += 1

        result = min(result, w_index, b_index)

print(result)
