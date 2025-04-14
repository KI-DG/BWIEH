"""
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

4
"""

n, m = map(int, input().split())

n_str = list(input() for _ in range(n))
m_str = list(input() for _ in range(m))

n_dict = {}
for i in range(n):
    n_dict[n_str[i]] = 0

count = 0
for i in range(m):
    if m_str[i] in n_dict:
        count += 1

print(count)
