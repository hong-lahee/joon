b = []
for i in range(9):
    num = int(input())
    b.append(num)

s = max(b)
i = b.index(s) + 1
print(s)
print(i)