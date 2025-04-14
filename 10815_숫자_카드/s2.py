"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

1 0 0 1 1 0 0 1
"""

n = int(input())
card = list(map(int, input().split()))
# card = set(map(int, input().split())
# card를 list가 아닌 set으로 중복을 없애주면 dict으로 안바꿔도 된다
m = int(input())
num = list(map(int, input().split()))

num_dict = {}

for i in range(n):
    num_dict[card[i]] = 0

# result = []
for j in range(m):
    if num[j] in num_dict:
        print(1, end=' ')
        # result.append(1)
    else:
        print(0, end=' ')
        # result.append(0)

# print(*result)


