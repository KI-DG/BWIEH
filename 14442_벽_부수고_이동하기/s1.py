'''
6 4 1
0100
1110
1000
0000
0111
0000
'''
# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 생각할것
# 델타검색 상하좌우 탐방
# 맵을 넘어가면 안됨
# 만약 벽을 k만큼 뚫으면 다음은 없다고 생각해야됨
# 왔던 길을 다시 가면 안됨 (최단거리가 안됨)


def distance(x, y):
    global answer, cnt
    for i in range(4):
        x = x + dx[i]
        y = y + dy[i]
        print(x)
        print(y)
        if arr[x][y] == 0 and cnt != k and arr[x][y] > m and arr[y][x] > n:
            print(visited[x][y], 1111)
            answer += 1
        elif arr[x][y] == 1 and cnt != k and arr[x][y] > m and arr[y][x]:
            print('else')
            answer = -1
    return answer


# 지도의 크기와 n * m, k = 부술수 있는 벽의 갯수
n, m, k = map(int, input().split())
# 지도 받아오기
arr = [list(map(int, input())) for _ in range(n)]

# 갔는지 안갔는지 확인
visited = [[0] * m for _ in range(n)]
answer = 1
cnt = 0
distance(0, 0)

print(answer)