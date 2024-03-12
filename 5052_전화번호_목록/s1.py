"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

NO
YES
"""

t = int(input())

for _ in range(1, t + 1):

    n = int(input())

    phone_num = []

    for _ in range(n):
        phone_num.append(input())

    phone_num.sort()

    answer = True
    for i in range(n - 1):
        if phone_num[i] == phone_num[i + 1][:len(phone_num[i])]:
            answer = False
            print('NO')
            break

    if answer:
        print('YES')
