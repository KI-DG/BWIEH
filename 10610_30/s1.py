"""
30

30

102

210

2931

-1

80875542

88755420
"""

arr = list(map(str, input()))

if '0' not in arr:
    print(-1)
else:
    num = 0
    for i in range(len(arr)):
        num += int(arr[i])

    if num % 3 != 0:
        print(-1)
    else:
        sort_num = sorted(arr, reverse=True)
        print("".join(sort_num))
