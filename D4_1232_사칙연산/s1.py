"""
1
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
1
7
1 / 2 3
2 - 4 5
3 - 6 7
4 261
5 61
6 81
7 71
"""


def count(x):

    if x:
        count(parent_1[x])
        count(parent_2[x])

        if tree[x] == '-':
            tree[x] = str(int(tree[parent_1[x]]) - int(tree[parent_2[x]]))
        elif tree[x] == '+':
            tree[x] = str(int(tree[parent_1[x]]) + int(tree[parent_2[x]]))
        elif tree[x] == '*':
            tree[x] = str(int(tree[parent_1[x]]) * int(tree[parent_2[x]]))
        elif tree[x] == '/':
            tree[x] = str(int(tree[parent_1[x]]) // int(tree[parent_2[x]]))


t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    # 자식 노드 저장하는것
    parent_1 = [[] for _ in range(n + 1)]
    parent_2 = [[] for _ in range(n + 1)]
    # 정점 값
    tree = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        arr = list(map(str, input().split()))
        # 길이가 4개이면 자식 노드 있는거니 tree 와 parent에 값 저장
        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            parent_1[int(arr[0])] = int(arr[2])
            parent_2[int(arr[0])] = int(arr[3])
        # 아니면
        else:
            tree[int(arr[0])] = int(arr[1])

    count(1)

    print(f"#{tc} {tree[1]}")
