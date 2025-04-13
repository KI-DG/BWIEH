"""
5
2 4 -10 4 -9

2 3 0 3 1
"""

n = int(input())

x_coc = list(map(int, input().split()))

arr = sorted(set(x_coc))
dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i

# dic = {arr[i]: i for i in range(len(arr))}

for j in x_coc:
    print(dic[j], end=" ")