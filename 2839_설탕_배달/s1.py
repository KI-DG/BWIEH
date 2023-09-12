"""
18
4
"""

n = int(input())
# 3, 5를 담을 list 만들어준다.
bag = 0
# 반복문
while n >= 0:
    # 5의 배수이면 최소니까
    if n % 5 == 0:
        # 5의 배수의 몫을 더해준다
        bag += (n // 5)
        print(bag)
        break
    # 3만큼 계속 빼준다
    n -= 3
    bag += 1
# 이것도 안된다면 -1 출력
else:
    print(-1)
