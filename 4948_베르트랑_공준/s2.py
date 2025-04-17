"""
1
10
13
100
1000
10000
100000
0

1
4
3
21
135
1033
8392
"""
num = 123456 * 2 + 1    # 문제에 제한 된 값 2 * n + 1 (index)
num_list = [1] * num    # 소수의 값을 저장하려고 만들었다
for i in range(2, num):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            num_list[i] = 0         # 소수가 아니면 0
            break

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for j in range(n + 1, (2 * n) + 1):
        count += num_list[j]
    print(count)
