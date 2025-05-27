i = int(input())

if i % 4 == 0 :
    if i % 100 != 0 or i % 400 == 0:
        print('1')
    else:
        print('0')
else:
     print('0')