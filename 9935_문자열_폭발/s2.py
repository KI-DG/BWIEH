'''
mirkovC4nizCC44
C4
'''

str1 = input()
str2 = input()

stack = []
length = len(str2)

for s in str1:
    stack.append(s)
    if ''.join(stack[-length:]) == str2:
        for num in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRUIA')