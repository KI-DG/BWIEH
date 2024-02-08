"""
10
1 5 2 1 4 3 4 5 2 1

7
"""

n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

dp_increase = [1] * n
dp_decrease = [1] * n
answer = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

        if reverse_arr[i] > reverse_arr[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

dp_decrease.reverse()

for i in range(n):
    result = dp_decrease[i] + dp_increase[i] - 1
    answer = max(answer, result)

print(answer)



