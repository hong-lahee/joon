n = int(input())
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s = a+b
    print(f"Case #{i+1}: {a} + {b} = {s}")