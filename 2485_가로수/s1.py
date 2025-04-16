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

n = int(input())

tree = []
tree_add = 9999999999999

for i in range(n):
    tree.append(int(input()))
    if i >= 1:
        tree_add = min(abs(tree[i] - tree[i - 1]), tree_add)
count = 0
for j in range(min(tree), max(tree), tree_add):
    if j not in tree:
        count += 1

print(count)

# 구현 실패.. 다시 처음으로