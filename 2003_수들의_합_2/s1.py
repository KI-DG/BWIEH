''''
4 2
1 1 1 1

3

10 5
1 2 3 4 2 5 3 1 1 2

3
'''


n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
start = 0
end = 1
while True:
    if start > end or end > n:
        break
    total = sum(arr[start:end])
    if total < m:
        end += 1
    elif total > m:
        start += 1
    else:
        cnt += 1
        end += 1

print(cnt)

# 투포인트에 관한 문제
