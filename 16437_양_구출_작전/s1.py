"""
4
S 100 3
W 50 1
S 10 1
60

7
S 100 1
S 100 1
W 100 1
S 1000 2
W 1000 2
S 900 6
1200
"""
# 그래프를 연결 (트리)
# W == (늑대이면) 마이너스 S == (양이면) 플러스를 해준다

# 깊이탐색으로 갚을 다 더해준다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(v):
    # dfs 돌려준다
    result = 0
    # 노드들의 탐색을 더해준다
    for x in tree[v]:
        result += dfs(x)
    # 늑대라면 빼주고
    if node[v][0] == 'W':
        result -= node[v][1]
        # 늑대가 양보다는 많아서 음수가 된다면 0을 더해준다(양이 다죽어서 이동을 0마리 하기 때문)
        if result < 0:
            result = 0
    # 양이라면 더해준다
    else:
        result += node[v][1]

    return result


n = int(input())
tree = [[] for _ in range(n + 1)]
# 양인지 늑대인지 구별해주기 위해 node를 만들어줌
node = [[], [0, 0]]

# 트리를 만들어준다
for i in range(n - 1):
    t, a, p = input().split()
    # 부모               i + 2는 여기서 몇번째 섬인지 확인
    tree[int(p)].append(i + 2)
    # print(tree)
    node.append([t, int(a)])

print(dfs(1))

