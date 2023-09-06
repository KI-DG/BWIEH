"""
4
10
20
70
40
"""

#  작은것들을 찾고 작은것들이 더한뒤 다시 그 다음 작은 것들이랑 더하면 될듯
#  최소값으로 정렬해서 사용하려고 했는데 배열에 다시 넣고 다시 정렬 하고 해야 되어서 구현이 더 빡세게 들었음
#  잘모르겟어서 찾아보니 큐를 이용하면 된다고 해서 큐의 사용법을 알아봄
#  heapify 기존 리스트를 힙으로 변환하는 함수


import heapq

n = int(input())

arr = [int(input()) for i in range(n)]

heapq.heapify(arr)

# 하나만 있을때 섞는 값은 0 이어야 된다!!!
cnt = 0

# 하나만 남으면 끝이니 그전까지는 계속 해줘야 됨
while len(arr) > 1:
    answer = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.nsmallest()
    heapq.heappush(arr, answer)
    cnt += answer

print(cnt)
