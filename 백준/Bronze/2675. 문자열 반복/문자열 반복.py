r = int(input())
for _ in range(r):
    s = input().split(' ')
    n = int(s[0])
    t =s[1]
    for i in t:
        print(i * n,end='')
    print()
