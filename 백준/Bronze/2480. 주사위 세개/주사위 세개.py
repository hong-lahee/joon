a, b, c = map(int, input().split())

# 2. 조건 분기
if a == b == c:
    # 모두 같은 눈
    prize = 10000 + a * 1000
elif a == b or a == c:
    # a가 두 개 나옴
    prize = 1000 + a * 100
elif b == c:
    # b가 두 개 나옴
    prize = 1000 + b * 100
else:
    # 모두 다른 눈
    prize = max(a, b, c) * 100

# 3. 출력
print(prize)