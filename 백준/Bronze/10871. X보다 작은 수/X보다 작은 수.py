a = list(map(int, input().split()))  # a는 리스트로 변환
s = map(int, input().split())        # s는 그대로 사용 가능 (for문에서)

b = a[0]
c = a[1]
e = []

for i in s:
    if i < c:
        e.append(i)

print(*e)  # 출력 예시: 1 4 2 3