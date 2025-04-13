"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""

n = int(input())
arr = [str(input()) for _ in range(n)]

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for j in arr:
    print(j)
