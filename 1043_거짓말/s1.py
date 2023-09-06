"""
4 3
0
2 1 2
1 3
3 2 3 4
3

4 1
1 1
4 1 2 3 4
0

4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
2
"""
# 진실된 사람이 하나라도 들어가 있지 않으면 cnt +1
# 조합에 대한 것 같다!
n, m = map(int, input().split())

ture_people = list(map(int, input().split()))[1:]


cnt = 0

# 부모 로드를 만들어주고
parent = [i for i in range(n + 1)]
for i in ture_people:
    parent[i] = cnt


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


party = []
for _ in range(m):
    party_person = list(map(int, input().split()))[1:]
    for i in range(len(party_person) - 1):
        union(party_person[i], party_person[i + 1])
    party.append(party_person)

answer = 0
for p in party:
    know = False
    for i in range(len(p)):
        if find(p[i]) == cnt:
            know = True
            break
    if not know:
        answer += 1

print(answer)