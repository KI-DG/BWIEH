"""
3
happy
new
year
3

5
ab
aa
aca
ba
bb

4
"""

n = int(input())
answer = 0

for i in range(n):
    word = input()
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            new = word[j + 1:]
            if word[j] in new:
                answer -= 1
                break

print(n + answer)
