"""
2143

4321
"""

n = list(map(str, input()))

for i in range(len(n) - 1, 0, -1):
    for j in range(0, i):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]

n.reverse()
print(''.join(n))



