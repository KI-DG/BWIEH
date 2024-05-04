"""
2
5 6
0 0 1 0

30
30

3
3 4 5
1 0 1 0

35
17

6
1 2 3 4 5 6
2 1 1 1

54
-24
"""


n = int(input())

data = list(map(int, input().split()))
plus, minus, multiplication, division = map(int, input().split())

max_count = -1000000000
min_count = 1000000000


def dfs(i, arr):
    global plus, minus, multiplication, division, max_count, min_count

    if i == n:
        max_count = max(max_count, arr)
        min_count = min(min_count, arr)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, arr + data[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, arr - data[i])
            minus += 1
        if multiplication > 0:
            multiplication -= 1
            dfs(i + 1, arr * data[i])
            multiplication += 1
        if division > 0:
            division -= 1
            dfs(i + 1, int(arr / data[i]))
            division += 1


dfs(1, data[0])

print(max_count)
print(min_count)
