"""
3 5
1 2 4
2 3 4 5 6

4
"""

a, b = map(int, input().split())

a_num = set(list(map(int, input().split())))
b_num = set(list(map(int, input().split())))

a_answer = a_num - b_num
b_answer = b_num - a_num

print(len(a_answer) + len(b_answer))


