"""
5
-1 0 0 1 1
2

2

5
-1 0 0 1 1
1

1

5
-1 0 0 1 1
0

0

9
-1 0 0 2 2 4 4 6 6
4

2
"""


def dfs(del_num):
    tree[del_num] = -99999

    for i in range(n):
        if del_num == tree[i]:
            dfs(i)


n = int(input())

tree = list(map(int, input().split()))
k = int(input())

dfs(k)
cnt = 0

for i in range(n):
    if tree[i] != -99999 and i not in tree:
        cnt += 1

print(cnt)


