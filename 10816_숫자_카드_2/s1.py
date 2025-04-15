"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2
"""

n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

n_dict = {}
for i in n_card:
    if i in n_dict:
        n_dict[i] = n_dict[i] + 1
    else:
        n_dict[i] = 1

result = []
for j in m_num:
    if j in n_dict:
        result.append(n_dict[j])
    else:
        result.append(0)
print(*result)
