a = int(input())
b = []
s = list(map(int,input().split(' ')))
b.extend(s)
print(min(b), max(b))