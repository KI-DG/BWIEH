"""
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5

4
3
"""
t = int(input())

for _ in range(1, t + 1):
    n = int(input())
    tree = [0] * (n + 1)

    for _ in range(n - 1):
        # x 가 y 의 부모
        x, y = map(int, input().split())
        tree[y] = x

    a, b = map(int, input().split())
    target_a = [a]
    target_b = [b]

    while tree[a]:
        target_a.append(tree[a])
        a = tree[a]
    while tree[b]:
        target_b.append(tree[b])
        b = tree[b]
        if b in target_a:
            break
    print(b)
