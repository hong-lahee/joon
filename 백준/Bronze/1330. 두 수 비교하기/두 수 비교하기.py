i = input()
i = i.split()
a = int(i[0])
b = int(i[1])

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')