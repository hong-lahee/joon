e = int(input())
for i in range(e):
    s = input()
    if len(s) == 1:
        print(s[0]* 2)
    else:
        print(s[0]+s[-1])
