"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

NO
NO
YES
NO
YES
NO
"""


def yes_no(arr_list):
    stack = []

    for a in arr_list:
        if a == '(':
            stack.append(a)
        elif a == ')' and stack:
            stack.pop()
        else:
            return 'NO'

    if not stack:
        return 'YES'
    else:
        return 'NO'


n = int(input())
for _ in range(n):
    arr = list(map(str, input()))
    print(yes_no(arr))
