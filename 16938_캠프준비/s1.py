"""
3 5 6 1
1 2 3

2

4 40 50 10
10 20 30 25
"""
# 문제는 두문제 이상 = 조합 문제??
# L <= 문제 난이도 합 <= R and 가장 어려운 문제와 가장 쉬운 문제의 차이는 X 보다 크거나 같아야됨


def combinations(arr, start, count):
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    global result
    if len(arr) >= 2 and l <= sum(arr) <= r and max(arr) - min(arr) >= x:
        count += 1
        result = max(result, count)

    for i in range(start, len(difficulty)):
        # 1) i번째 원소를 뽑는다.
        arr.append(difficulty[i])

        # 2) 재귀함수 진행
        combinations(arr, i + 1, count)

        # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
        arr.pop()


n, l, r, x = map(int, input().split())

difficulty = list(map(int, input().split()))

result = 0
combinations([], 0, 0)

print(result)
