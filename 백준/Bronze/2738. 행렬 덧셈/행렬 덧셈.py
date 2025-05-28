n , m = map(int, input().split())

a =[list(map(int,input().split()))for _ in range (n)]
b =[list(map(int,input().split()))for _ in range (n)]

for i in range(n):
    s =[]
    for h in range(m):
        s.append(a[i][h]+b[i][h])
    print(*s)