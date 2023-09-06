"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

# 집합 유니온 파인드 문제
# m은 연산의 갯수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)   # 재귀 갯수 제한


def union(x, y):
    # find를 통해 루트 노드를 가짐
    x = find(x)
    y = find(y)
    # 이미 연결된것
    if x == y:
        return
    parent[x] = y
    return


def find(x):
    # 배열의 길이가 같으면 리턴
    if parent[x] == x:
        return x
    # 배열의 값을 인덱스로 하는 값 리턴
    parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())

# 부모 로드를 만들어주고
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for i in range(m):
    x, a, b = map(int, input().split())
    # x가 0이면 합집합
    if x == 0:
        union(a, b)
    # 아니면
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            print('YES')
        else:
            print('NO')
