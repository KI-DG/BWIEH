'''
55-50+40
'''
# 최소값을 구해야 되기 때문에 - 뒤에서 괄호를 쳐야된다
# -를 기준으로 나눠주고 나머지 +는 더해주고 그다음 다시 -를 해주면 된다.
# 생각을 고침
# 괄호를 치면 다 -로 변환시킬수 있으니 +를 -를 변환시켜주면 된다.

# -기준으로 나눠줌
arr = input().split('-')
# 최소값을 나타내주기 위해 변수 선언
answer = 0

# 첫번째 -가 나오기 전까지 값은 다 더해주기
for i in arr[0].split('+'):
    answer += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)

