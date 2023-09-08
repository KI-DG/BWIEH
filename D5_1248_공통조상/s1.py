"""
2
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
10 9 2 10
1 2 1 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10
"""


def order_tree(son, parent_list):
    # 부모를 찾는 함수
    if node[son]:
        # 부모가 있다면 리스트에 넣어줌
        parent_list.append(node[son])
        order_tree(node[son], parent_list)


def cnt_tree(parent_list):
    # 노드 갯수 카운트 하는 함수
    global cnt
    for i in parent_list:
        cnt += 1
        cnt_tree(tree[i])


t = int(input())

for tc in range(1, t + 1):
    result = []
    cnt = 1
    # 정점의 갯수, 간선의 갯수, 두개의 노드
    v, e, node_f, node_s = map(int, input().split())

    tree = [[] for _ in range(v + 1)]
    node = [[] for _ in range(v + 1)]

    arr = list(map(int, input().split()))

    for i in range(0, len(arr), 2):
        # 부모, 자식
        a, b = arr[i], arr[i + 1]
        # 부모에 자식을 넣고
        tree[a].append(b)
        # 자식에는 부모를 넣어줌
        node[b] = a
    parent_f, parent_s = [], []

    order_tree(node_f, parent_f)
    order_tree(node_s, parent_s)

    for i in parent_f:
        for j in parent_s:
            if i == j:
                result.append(i)

    answer = result[0]
    cnt_tree(tree[answer])

    print(f"#{tc} {answer} {cnt}")
