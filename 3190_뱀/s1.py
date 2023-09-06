"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""
# 사과를 먹으면 뱀의 길이가 +1 커짐
# 뱀의 시작위치는 맨위 맨 왼쪽 (0,0) 처음 방향은 오른쪽임1
# 벽이나 자기 자신 만나면 끝
# 지도는 0 사과는 1 뱀은 2

# 방향 델타 탐색?
# end 조건 == 다음 방향일때 벽인지 자기자신인지 확인
# 크기 유지는???

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())

k = int(input())

# 1. 지도를 만들고
apple_map = [([0] * n) for _ in range(n)]

# 2. 사과의 위치를 만들어주고
for i in range(k):
    apple = list(map(int, input().split()))
    apple_map[apple[0] - 1][apple[1] - 1] = 1

line_count = int(input())
# 3. 뱀이 방향 정보를 받아주기 정수X == 초 문자 C == 방향 L == 왼쪽 D== 오른쪽
for i in range(line_count):
    sec, direction = input().split()

time = 0
start = (0, 0)
print(apple_map)

