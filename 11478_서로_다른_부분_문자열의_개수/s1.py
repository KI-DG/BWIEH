"""
ababc

12
"""

str_s = str(input())

answer = set()
for i in range(len(str_s)):
    for j in range(i, len(str_s)):
        answer.add(str_s[i:j + 1])

print(len(answer))