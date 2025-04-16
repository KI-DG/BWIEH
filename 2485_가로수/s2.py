"""
4
1
3
7
13

3

4
2
6
12
18

5
"""
import math
n = int(input())

tree = list(int(input()) for _ in range(n))
space_tree = []

for i in range(1, n):
    space_tree.append(tree[i] - tree[i - 1])

min_space = math.gcd(*space_tree) # 최대 공약수

print(((tree[-1] - tree[0]) // min_space) - 1 - (n - 2))

# count = 0
# for j in range(tree[0], tree[-1], min_space):
#     if j not in tree:
#         count += 1
#
# print(count)
