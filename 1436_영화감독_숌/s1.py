"""
187

66666

500

166699
"""

n = int(input())

cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        print(result)
        break
    result += 1
