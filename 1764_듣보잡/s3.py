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
# list 로 말고 set 으로 받아줘서 중복을 줄여준다
listen_not = set(input() for _ in range(n))
look_not = set(input() for _ in range(m))
# intersection == set 에서 교집합을 찾아주는 함수 list 에서는 적용이 안됨
# set.intersection(a, b) 이렇게 사용도 가능
# set.difference(a, b) 차집합도 가능
listen_look_not = listen_not.intersection(look_not)
print(len(listen_look_not))

[print(j) for j in sorted(listen_look_not)]
