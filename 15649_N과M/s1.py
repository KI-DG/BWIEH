"""
3 1

1
2
3

4 2

1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""

n, m = map(int, input().split())

arr = []


def dfs():

    if len(arr) == m:
        print(*arr, sep='\n')

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()


dfs()
