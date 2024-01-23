"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

2
baesangwook
ohhenrie
"""

n, m = map(int, input().split())
listen_not = set(input() for _ in range(n))
look_not = set(input() for _ in range(m))

answer = 0
listen_look_not = []

for i in listen_not:
    if i in look_not:
        answer += 1
        listen_look_not.append(i)
print(answer)
# 사전 순으로 정렬
listen_look_not.sort()

[print(j) for j in listen_look_not]
