h, m = map(int,input().split())

if m < 45:
    h -= 1
    m += 60
if h < 0:
    h = 23
m -= 45

print(h, m)
    