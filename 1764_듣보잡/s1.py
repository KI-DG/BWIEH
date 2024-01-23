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
listen_not = list(input() for _ in range(n))
look_not = list(input() for _ in range(m))
answer = 0
listen_look_not = []
for i in listen_not:
    for j in look_not:
        if i == j:
            answer += 1
            listen_look_not.append(i)
            break

listen_look_not.sort()

print(answer)
for a in listen_look_not:
    print(a)
# 시간초과 (list 를 사용하여 중복된 값이 많을 경우 시간초과가 발생)
