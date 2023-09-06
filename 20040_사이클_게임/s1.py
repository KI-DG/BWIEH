"""
6 5
0 1
1 2
2 3
5 4
0 4
0

6 5
0 1
1 2
1 3
0 3
4 5
4
"""
# union find 문제인거 같다.
import sys

input = sys.stdin.readline


def find(x):
    # 배열의 길이가 같으면 리턴
    if parent[x] == x:
        return x
    # 배열의 값을 인덱스로 하는 값 리턴
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    # find를 통해 루트 노드를 가짐
    x = find(x)
    y = find(y)
    # 이미 연결된것
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
answer = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if not answer:
        # 싸이클이 형성되어 있다면
        if find(a) == find(b):
            # 순번을 찾아야 되니까 순번을 더해준다
            answer = i
        # 싸이클이 형성되어 있지 않다면
        else:
            union(a, b)

print(answer)
