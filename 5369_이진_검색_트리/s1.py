"""
50
30
24
5
28
45
98
52
60

5
28
24
45
30
60
52
98
50
"""
import sys
sys.setrecursionlimit(10**9)


tree = []
# 따로 크기를 안 줬으니 다 받을 때까지 while 문을 이용해서 input 을 받아준다
while True:
    try:
        x = int(sys.stdin.readline())
        tree.append(x)
    except:
        break


# 재귀 함수 만들기
def post(start, end):
    if start > end:
        return
    mid = end + 1

    # 만약 root 보다 큰 값이 없는 경우 전부 왼쪽 서브트리로 취급
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            break
    # root 다음부터 왼쪽 서브트리 탐색
    post(start + 1, mid - 1)
    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    post(mid, end)
    # 왼쪽 오른쪽 서브트리 탐색 끝나면 root 출력
    print(tree[start])


post(0, len(tree) - 1)
