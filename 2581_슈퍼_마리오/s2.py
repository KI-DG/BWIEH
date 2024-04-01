"""
10
20
30
40
50
60
70
80
90
100

100

1
2
3
5
8
13
21
34
55
89

87

40
40
40
40
40
40
40
40
40
40

120
"""
arr = [int(input()) for _ in range(10)]
answer = 0
for i in arr:
    answer += i
    if answer >= 100:
        if answer - 100 > 100 - (answer - i):
            answer -= i
            break

print(answer)

# 맞았습니다