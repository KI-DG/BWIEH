'''
mirkovC4nizCC44
C4
'''


import sys

str1 = sys.stdin.readline()
str2 = sys.stdin.readline()

answer = str1

for a in str1:
    for b in str2:
        if a == b:
            answer = answer.replace(a, '')

if answer == '':
    print('FRULA')
else:
    print(answer)
# 시간초과
