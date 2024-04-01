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
for i in range(1, 10):
    arr[i] = arr[i] + arr[i - 1]
    if arr[i] > 100:
        if abs(arr[i] - 100) > abs(arr[i - 1] - 100):
            answer = arr[i - 1]
        elif abs(arr[i] - 100) == abs(arr[i - 1] - 100):
            answer = max(arr[i], arr[i - 1])
        else:
            answer = arr[i]
        break
    elif arr[i] == 100:
        answer = arr[i]
        break

print(answer)

# 틀렸습니다