"""
3 5 6 1
1 2 3

"""
# 문제는 두문제 이상 = 조합 문제??
# L <= 문제 난이도 합 <= R and 가장 어려운 문제와 가장 쉬운 문제의 차이는 X 보다 크거나 같아야됨

from itertools import combinations
# 첫째 줄 받아주고
n, l, r, x = map(int, input().split())
# 둘째 줄 받아주고
difficulty = list(map(int, input().split()))
# 결과값 출력하기 위해
result = 0
# 조합으로 풀어보자
for i in range(2, n + 1):
    difficulty_list = list(combinations(difficulty, i))
    # from itertools import combinations == 튜플로 나옴 (리스트, 갯수)
    for j in difficulty_list:
        # 조건
        if l <= sum(j) <= r and max(j) - min(j) >= x:
            result += 1

print(result)


