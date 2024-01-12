"""
2
3 ABC
5 /HTP
"""

t = int(input())

for _ in range(t):
    n, word = map(str, input().split())
    n = int(n)
    result = []
    for i in word:
        result.append(i * n)

    print(''.join(result))

