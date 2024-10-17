"""
5 5
1 3
1 4
4 5
4 3
3 2

3
"""

n, m = map(int, input().split())

a_list = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())

    a_list[a].append(b)
    a_list[b].append(a)

cnt = 0
cnt_number = []
for i in range(1, n + 1):
    if len(a_list[i]) > cnt:
        cnt = max(len(a_list[i]), cnt)
        cnt_number.append(i)

print(max(cnt_number))

# 친구가 많으면 횟수가 적을거라고 생각하고 풀어봄 역시나 실패 ^^

